#!/usr/bin/env python3
"""Regression checks for canonical KDP release promotion."""

import json
import subprocess
import sys
from pathlib import Path

from pypdf import PdfWriter

REPO_ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT = (
    REPO_ROOT
    / ".agents"
    / "skills"
    / "kdp-publishing"
    / "scripts"
    / "release_preflight.py"
)
MM_TO_POINTS = 72 / 25.4


def _pdf(path: Path, width_mm: float, height_mm: float, pages: int) -> None:
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width_mm * MM_TO_POINTS, height_mm * MM_TO_POINTS)
    with path.open("wb") as handle:
        writer.write(handle)


def _run(interior: Path, cover: Path, manifest: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(PREFLIGHT),
            "--interior",
            str(interior),
            "--cover",
            str(cover),
            "--trim-width-mm",
            "127",
            "--trim-height-mm",
            "203.2",
            "--cover-width-mm",
            "265.56",
            "--cover-height-mm",
            "209.55",
            "--expected-pages",
            "81",
            "--write-manifest",
            str(manifest),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def test_release_preflight_writes_pass_manifest(tmp_path: Path):
    interior = tmp_path / "paperback-interior.pdf"
    cover = tmp_path / "paperback-cover.pdf"
    manifest = tmp_path / "release-manifest.json"
    _pdf(interior, 127, 203.2, 81)
    _pdf(cover, 265.56, 209.55, 1)

    result = _run(interior, cover, manifest)

    assert result.returncode == 0, result.stdout + result.stderr
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["result"] == "PASS"
    assert data["artifacts"]["paperback_interior"]["pages"] == 81
    assert data["artifacts"]["paperback_cover"]["pages"] == 1
    assert len(data["artifacts"]["paperback_cover"]["sha256"]) == 64


def test_release_preflight_rejects_multipage_cover(tmp_path: Path):
    interior = tmp_path / "paperback-interior.pdf"
    cover = tmp_path / "paperback-cover.pdf"
    manifest = tmp_path / "release-manifest.json"
    _pdf(interior, 127, 203.2, 81)
    _pdf(cover, 265.56, 209.55, 3)

    result = _run(interior, cover, manifest)

    assert result.returncode == 2
    assert "cover must contain exactly 1 page, found 3" in result.stdout
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["result"] == "FAIL"
