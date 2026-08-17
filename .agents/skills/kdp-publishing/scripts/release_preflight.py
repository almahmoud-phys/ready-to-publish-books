#!/usr/bin/env python3
"""Validate the exact files proposed for a KDP release and write their hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader

MM_PER_POINT = 25.4 / 72
PLACEHOLDER = re.compile(r"<[^<>]+>")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_info(path: Path) -> dict:
    reader = PdfReader(str(path))
    sizes = []
    for page in reader.pages:
        box = page.mediabox
        sizes.append([
            round(float(box.width) * MM_PER_POINT, 3),
            round(float(box.height) * MM_PER_POINT, 3),
        ])
    return {"pages": len(reader.pages), "page_sizes_mm": sizes}


def artifact(path: Path, details: dict | None = None) -> dict:
    result = {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}
    if details:
        result.update(details)
    return result


def close(actual: float, expected: float, tolerance: float) -> bool:
    return abs(actual - expected) <= tolerance


def placeholders(value, location: str = "$") -> list[str]:
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            found.extend(placeholders(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(placeholders(child, f"{location}[{index}]"))
    elif isinstance(value, str) and PLACEHOLDER.search(value):
        found.append(location)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--interior", type=Path, required=True)
    parser.add_argument("--cover", type=Path, required=True)
    parser.add_argument("--trim-width-mm", type=float, required=True)
    parser.add_argument("--trim-height-mm", type=float, required=True)
    parser.add_argument("--cover-width-mm", type=float, required=True)
    parser.add_argument("--cover-height-mm", type=float, required=True)
    parser.add_argument("--expected-pages", type=int)
    parser.add_argument("--epub", type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--tolerance-mm", type=float, default=0.25)
    parser.add_argument("--write-manifest", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    manifest = {"schema_version": 1, "artifacts": {}}
    for path in [args.interior, args.cover, args.epub, args.metadata]:
        if path is not None and not path.is_file():
            errors.append(f"missing file: {path}")
    if errors:
        print("FAIL: " + "; ".join(errors))
        return 2

    interior = pdf_info(args.interior)
    if args.expected_pages is not None and interior["pages"] != args.expected_pages:
        errors.append(f"interior pages {interior['pages']} != expected {args.expected_pages}")
    for number, (width, height) in enumerate(interior["page_sizes_mm"], 1):
        if not (close(width, args.trim_width_mm, args.tolerance_mm) and
                close(height, args.trim_height_mm, args.tolerance_mm)):
            errors.append(f"interior page {number} is {width}x{height} mm")
    manifest["artifacts"]["paperback_interior"] = artifact(args.interior, interior)

    cover = pdf_info(args.cover)
    if cover["pages"] != 1:
        errors.append(f"cover must contain exactly 1 page, found {cover['pages']}")
    if cover["page_sizes_mm"]:
        width, height = cover["page_sizes_mm"][0]
        if not (close(width, args.cover_width_mm, args.tolerance_mm) and
                close(height, args.cover_height_mm, args.tolerance_mm)):
            errors.append(f"cover is {width}x{height} mm")
    manifest["artifacts"]["paperback_cover"] = artifact(args.cover, cover)

    if args.epub:
        try:
            with zipfile.ZipFile(args.epub) as archive:
                mimetype = archive.read("mimetype")
            if mimetype != b"application/epub+zip":
                errors.append("EPUB mimetype is invalid")
        except (zipfile.BadZipFile, KeyError) as exc:
            errors.append(f"invalid EPUB container: {exc}")
        manifest["artifacts"]["kindle_epub"] = artifact(args.epub)

    if args.metadata:
        try:
            metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
            unresolved = placeholders(metadata)
            if unresolved:
                errors.append("metadata placeholders at " + ", ".join(unresolved))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid metadata JSON: {exc}")
        manifest["artifacts"]["metadata"] = artifact(args.metadata)

    manifest["result"] = "FAIL" if errors else "PASS"
    manifest["errors"] = errors
    if args.write_manifest:
        args.write_manifest.parent.mkdir(parents=True, exist_ok=True)
        args.write_manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    if errors:
        print("FAIL: " + "; ".join(errors))
        return 2
    print(f"PASS: {interior['pages']} interior pages; one-page cover; hashes recorded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
