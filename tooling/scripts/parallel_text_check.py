#!/usr/bin/env python3
"""parallel_text_check.py — mechanical gate for the English parallel text (PIPE-001).

Usage:
    python tooling/scripts/parallel_text_check.py books/<slug>
    python tooling/scripts/parallel_text_check.py books/<slug> --update-hashes

Checks, per Spanish chapter `chapters/NN-*.md`:
  1. a translation `translations/NN-*.en.md` exists;
  2. its block count equals the Spanish chapter's NARRATIVE block count
     (blocks before the first exercise marker — exercises stay Spanish on purpose);
  3. the Spanish source hash matches `translations/sources.sha256`, so a later
     edit to the Spanish cannot leave a stale English block silently in place.

This is lint, not a translation-quality judgement. Quality is a human/model read.
"""
import hashlib
import sys
from pathlib import Path

EXERCISE_HEADS = ("**Preguntas**",)  # first one ends the narrative
CHAPTER_GLOB = "[0-9][0-9]-*.md"
HASH_FILE = "sources.sha256"


def blocks(text: str) -> list:
    return [b.strip() for b in text.split("\n\n") if b.strip()]


def split_story(text: str):
    """(narrative blocks, exercise blocks). Exercises start at the first `**Preguntas**`."""
    parts = blocks(text)
    for i, b in enumerate(parts):
        if b in EXERCISE_HEADS:
            return parts[:i], parts[i:]
    return parts, []


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def chapters(book_dir: Path) -> list:
    return sorted((book_dir / "chapters").glob(CHAPTER_GLOB))


def translation_for(book_dir: Path, chapter: Path):
    num = chapter.name[:2]
    hits = sorted((book_dir / "translations").glob(f"{num}-*.en.md"))
    return hits[0] if len(hits) == 1 else None


def read_hashes(path: Path) -> dict:
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        digest, _, name = line.partition("  ")
        if digest and name:
            out[name.strip()] = digest
    return out


def main() -> int:
    book_dir = Path(sys.argv[1]).resolve()
    update = "--update-hashes" in sys.argv[1:]
    hash_path = book_dir / "translations" / HASH_FILE

    srcs = chapters(book_dir)
    if not srcs:
        print(f"FAIL: no chapters matching {CHAPTER_GLOB} in {book_dir}/chapters")
        return 2

    if update:
        hash_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Spanish source hashes at translation time. Regenerate ONLY after re-reading",
            "# the affected English file against the changed Spanish.",
        ]
        lines += [f"{sha256(c)}  {c.name}" for c in srcs]
        hash_path.write_text("\n".join(lines) + "\n")
        print(f"OK: wrote {len(srcs)} source hashes -> translations/{HASH_FILE}")
        return 0

    recorded = read_hashes(hash_path)
    failures = []
    for src in srcs:
        en = translation_for(book_dir, src)
        if en is None:
            failures.append(f"{src.name}: no unique translations/{src.name[:2]}-*.en.md")
            continue

        es_narrative, _ = split_story(src.read_text())
        en_blocks, en_exercises = split_story(en.read_text())
        if en_exercises:
            failures.append(f"{en.name}: contains an exercise block — exercises stay Spanish")
        if len(en_blocks) != len(es_narrative):
            failures.append(
                f"{en.name}: {len(en_blocks)} blocks vs {len(es_narrative)} Spanish narrative blocks"
            )

        want = recorded.get(src.name)
        if want is None:
            failures.append(f"{src.name}: no recorded source hash in {HASH_FILE}")
        elif want != sha256(src):
            failures.append(f"{src.name}: Spanish changed since translation — re-read {en.name}")

    for f in failures:
        print(f"FAIL: {f}")
    if failures:
        return 2
    print(f"OK: {len(srcs)} chapters aligned with their English parallel text.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
