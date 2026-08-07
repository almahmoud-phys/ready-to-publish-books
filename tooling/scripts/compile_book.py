#!/usr/bin/env python3
"""compile_book.py — deterministic book compiler (clean-room reimplementation of the
compile pattern, ADR-006 license rule; replaces shell pipelines with one testable file).

Usage:
    python tooling/scripts/compile_book.py books/<slug>

Does:
  1. Assemble master.md (front matter + chapters in outline order + back matter)
  2. pandoc -> exports/master.epub  (css + metadata.yaml)
  3. epubcheck exports/master.epub  (MUST exit 0 — Gate E)
  4. pandoc -> exports/print/interior.pdf (xelatex + 6x9 preamble)
  5. Platform variants: exports/kdp/, exports/direct/
  6. Word count + artifact hashes appended to compliance_log.yaml
Refuses to run if Gate D not passed (state.json) — formatter-platform SKILL.md owns judgment.
"""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PANDOC_CSS = REPO / "tooling/pandoc/epub.css"
PANDOC_META = REPO / "tooling/pandoc/metadata.yaml"
PRINT_PREAMBLE = REPO / "tooling/latex/print-preamble-6x9.tex"


def sh(cmd: list[str]) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def log_event(book_dir: Path, artifact: Path, event: str = "export") -> None:
    log = book_dir / "compliance_log.yaml"
    with log.open("a") as f:
        f.write(
            f"- event: {event}\n"
            f"  skill: formatter-platform\n"
            f"  model: none (deterministic tooling)\n"
            f"  artifact: {artifact.relative_to(book_dir)}\n"
            f"  sha256: {sha256(artifact)}\n"
            f"  timestamp: {datetime.now(timezone.utc).isoformat()}\n"
        )


def main() -> int:
    book_dir = Path(sys.argv[1]).resolve()
    state = json.loads((book_dir / "state.json").read_text())
    if state["stages"]["5_proof-fact"].get("gate_d") != "PASS":
        print("REFUSED: Gate D not passed — fix edits/fact flags first.")
        return 2

    exports = book_dir / "exports"
    for sub in ["", "kdp", "direct", "print", "cover"]:
        (exports / sub).mkdir(parents=True, exist_ok=True)

    chapters = sorted((book_dir / "chapters").glob("chapter_*.md"))
    if not chapters:
        print("REFUSED: no chapters found.")
        return 2

    master = exports / "master.md"
    front = book_dir / "frontmatter.md"   # title + copyright page (track-aware)
    back = book_dir / "backmatter.md"     # about + mailing-list CTA (ADR-004)
    parts = ([front] if front.exists() else []) + chapters + ([back] if back.exists() else [])
    master.write_text("\n\n".join(p.read_text() for p in parts))

    epub = exports / "master.epub"
    sh(["pandoc", str(master), "-o", str(epub),
        "--css", str(PANDOC_CSS), "--metadata-file", str(PANDOC_META), "--toc", "--toc-depth=2"])
    sh(["epubcheck", str(epub)])  # exit non-zero -> subprocess raises -> Gate E fails (by design)

    pdf = exports / "print" / "interior.pdf"
    sh(["pandoc", str(master), "-o", str(pdf), "--pdf-engine=xelatex",
        "-H", str(PRINT_PREAMBLE), "--toc", "--toc-depth=1"])

    for variant in ["kdp", "direct"]:
        target = exports / variant / epub.name
        target.write_bytes(epub.read_bytes())
        log_event(book_dir, target)
    log_event(book_dir, epub)
    log_event(book_dir, pdf)

    words = len(master.read_text().split())
    print(f"OK: {len(chapters)} chapters, {words} words -> {epub.name}, interior.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
