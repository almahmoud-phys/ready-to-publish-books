#!/usr/bin/env python3
"""compile_book.py — deterministic book compiler (clean-room reimplementation of the
compile pattern, ADR-006 license rule; replaces shell pipelines with one testable file).

Usage:
    python tooling/scripts/compile_book.py books/<slug>

Does:
  1. Write/refresh books/<slug>/frontmatter.md (track-aware)
  2. Assemble master.md (front matter + story text in outline order + English parallel
     text, if any + exercises collected at the back + back matter)
  2. pandoc -> exports/master.epub  (css + metadata.yaml)
  3. epubcheck exports/master.epub  (MUST exit 0 — Gate E)
  4. pandoc -> exports/print/interior.pdf (xelatex + owner-approved 5x8 preamble)
  5. Platform variants: exports/kdp/, exports/direct/
  6. Word count + artifact hashes appended to compliance_log.yaml
Refuses to run if Gate D has not passed or Stage 6 has an active PIPE-001 blocker.
"""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parallel_text_check import CHAPTER_GLOB, split_story  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
PANDOC_CSS = REPO / "tooling/pandoc/epub.css"
PANDOC_META = REPO / "tooling/pandoc/metadata.yaml"
PRINT_PREAMBLE = REPO / "tooling/latex/print-preamble-5x8.tex"
STORY_HEADING_STYLE = REPO / "tooling/latex/story-heading-style.tex"
STORY_HEADING_FILTER = REPO / "tooling/pandoc/story-headings.lua"
KDP_METADATA_KEYS = ("title", "author", "subtitle", "description")


def tagged(text: str, lang: str) -> str:
    """Fenced div carrying a lang attribute. Without it a screen reader reads the Spanish
    with an English voice — the document lang cannot cover a bilingual interior.

    BOTH spellings are required. EPUB XHTML is parsed as XML, where `xml:lang` governs;
    HTML `lang` is what a browser honours. The first build emitted `lang="es"` on 21
    sections and `xml:lang` on zero, and epubcheck reported 0 warnings — Gate E does not
    catch this, so the redundancy is the check."""
    return f"::: {{lang={lang} xml:lang={lang}}}\n\n{text}\n\n:::"


def demote(text: str) -> str:
    """`# Title` -> `## Title` on the first line, so a section's units nest under it."""
    head, sep, rest = text.partition("\n")
    return ("#" + head if head.startswith("# ") else head) + sep + rest


def mark_story_opening(text: str) -> str:
    """Mark a narrative heading for page-break and designed-opening treatment.

    Exercise headings deliberately remain unmarked: a new page belongs to each story,
    not to every repeated story label in the collected drills section.
    """
    head, sep, rest = text.partition("\n")
    if head.startswith("# ") and "{.story-opening}" not in head:
        head += " {.story-opening}"
    return head + sep + rest


def mark_unlisted_heading(text: str) -> str:
    """Keep a heading in the document structure while excluding it from the TOC."""
    head, sep, rest = text.partition("\n")
    if head.startswith("# ") and ".unlisted" not in head:
        head += " {.unnumbered .unlisted}"
    return head + sep + rest


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


def load_manifest(book_dir: Path) -> dict[str, str]:
    manifest = {}
    path = book_dir / "manifest.yaml"
    if not path.exists():
        return manifest

    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text()) or {}
        if isinstance(loaded, dict):
            return loaded
    except Exception:
        pass

    # Lightweight fallback if PyYAML is unavailable.
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.split("  #", 1)[0].strip()
        if value.startswith('"') and value.endswith('"') or value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        if key and not key.startswith("-"):
            manifest[key] = value
    return manifest


def resolved(*values: str) -> str:
    """First filled value. `<like-this>` is an unfilled manifest placeholder, not a value —
    it must never reach an interior (it did: `## <keyword-loaded subtitle>` shipped once)."""
    for v in values:
        v = (v or "").strip()
        if v and not (v.startswith("<") and v.endswith(">")):
            return v
    return ""


def frontmatter_for_track(manifest: dict[str, str], meta: dict[str, str] | None = None) -> str:
    meta = meta or {}
    track = (manifest.get("track", "assisted") or "assisted").strip().lower()
    title = resolved(meta.get("title"), manifest.get("title")) or "Untitled"
    subtitle = resolved(meta.get("subtitle"), manifest.get("subtitle"))
    author = resolved(meta.get("author"), manifest.get("author"), manifest.get("pen_name"))
    # Keep bibliographic data in Pandoc's document metadata. Rendering the title as
    # an H1 as well creates a second, navigable "chapter" after Pandoc's title page.
    # JSON strings are valid YAML scalars and safely preserve punctuation/non-ASCII.
    lines = ["---", f"title: {json.dumps(title, ensure_ascii=False)}"]
    if subtitle:
        lines.append(f"subtitle: {json.dumps(subtitle, ensure_ascii=False)}")
    if author:
        lines.append(f"author: {json.dumps(author, ensure_ascii=False)}")
    else:
        print("NOTICE: no approved author/pen name; byline omitted from frontmatter.md.")
    lines += ["---"]
    if track != "generated":
        year = datetime.now(timezone.utc).year
        lines += [
            "",
            "# Copyright",
            f"© {year} {author}".rstrip(),
            "All rights reserved.",
        ]
    return "\n".join(lines) + "\n"


def load_metadata_for_injection(meta_path: Path) -> dict[str, str]:
    if not meta_path.exists():
        print(f"NOTICE: {meta_path.relative_to(meta_path.parents[1])} missing; skipping metadata injection.")
        return {}
    try:
        raw = json.loads(meta_path.read_text())
    except Exception as exc:
        print(f"NOTICE: cannot parse {meta_path}: {exc}; skipping metadata injection.")
        return {}
    if not isinstance(raw, dict):
        print(f"NOTICE: {meta_path} is not an object; skipping metadata injection.")
        return {}
    # metadata-seo records the owner's locked pick under human_selection; flat keys win if both.
    selection = raw.get("human_selection") if isinstance(raw.get("human_selection"), dict) else {}
    injected = {}
    for key in KDP_METADATA_KEYS:
        value = resolved(raw.get(key), selection.get(key))
        if value:
            injected[key] = value
    if injected:
        pretty = ", ".join(sorted(injected.keys()))
        print(f"NOTICE: injecting {pretty} from {meta_path}.")
    return injected


def metadata_args(meta: dict[str, str]) -> list[str]:
    out = []
    for key in KDP_METADATA_KEYS:
        if key in meta:
            out.extend(["--metadata", f"{key}={meta[key]}"])
    return out


def main() -> int:
    book_dir = Path(sys.argv[1]).resolve()
    state = json.loads((book_dir / "state.json").read_text())
    if state["stages"]["5_proof-fact"].get("gate_d") != "PASS":
        print("REFUSED: Gate D not passed — fix edits/fact flags first.")
        return 2

    stage6 = state["stages"].get("6_exports", {})
    if "PIPE-001" in stage6.get("blockers", []):
        print("REFUSED: PIPE-001 is unresolved — assign English parallel-text production and independent verification before compiling.")
        return 2

    # A resolved state flag is not enough: a bilingual build must prove that every
    # translation still aligns mechanically with the current Spanish source before
    # any generated artifact is written.
    translation_dir = book_dir / "translations"
    if translation_dir.exists() and any(translation_dir.glob("*.en.md")):
        try:
            sh([sys.executable, str(REPO / "tooling/scripts/parallel_text_check.py"), str(book_dir)])
        except subprocess.CalledProcessError:
            print("REFUSED: English parallel-text alignment/source-freshness gate failed.")
            return 2

    exports = book_dir / "exports"
    for sub in ["", "kdp", "direct", "print", "cover"]:
        (exports / sub).mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(book_dir)
    metadata = load_metadata_for_injection(book_dir / "exports" / "metadata.json")
    front = book_dir / "frontmatter.md"
    front.write_text(frontmatter_for_track(manifest, metadata))

    chapters = sorted((book_dir / "chapters").glob(CHAPTER_GLOB))
    if not chapters:
        print(f"REFUSED: no chapters matching {CHAPTER_GLOB} found.")
        return 2
    back = book_dir / "backmatter.md"     # about + mailing-list CTA (ADR-004)

    # Story text first, then any English parallel text, then the drills. Exercises are
    # pulled out of each chapter so the Look Inside sample opens on a story, not a quiz
    # (stage-6 decision; books/<slug>/exercises.md explains the move to the reader).
    src_lang = resolved(manifest.get("source_language"))
    if not src_lang:
        print("NOTICE: manifest has no source_language; chapters inherit the document language.")

    sections = [front.read_text()] if front.exists() else []
    drills = []
    for ch in chapters:
        narrative, exercises = split_story(ch.read_text())
        body = mark_story_opening("\n\n".join(narrative))
        sections.append(tagged(body, src_lang) if src_lang else body)
        if exercises:
            exercise_heading = demote(mark_unlisted_heading(narrative[0]))
            drills.append("\n\n".join([exercise_heading] + exercises))

    english = sorted((book_dir / "translations").glob("*.en.md"))
    en_intro = book_dir / "translations" / "00-english-translations.md"
    if english and en_intro.exists():
        sections.append(en_intro.read_text())
        sections += [demote(mark_story_opening(p.read_text())) for p in english]

    drill_intro = book_dir / "exercises.md"
    if drills and drill_intro.exists():
        intro = drill_intro.read_text()
        sections.append(tagged(intro, src_lang) if src_lang else intro)
        sections += [tagged(d, src_lang) if src_lang else d for d in drills]

    if back.exists():
        sections.append(back.read_text())

    master = exports / "master.md"
    master.write_text("\n\n".join(sections))

    epub = exports / "master.epub"
    cover_image = exports / "cover" / "final" / "front-cover.jpeg"
    cover_args = ["--epub-cover-image", str(cover_image)] if cover_image.exists() else []
    if not cover_args:
        print("NOTICE: no final JPEG cover found; EPUB will not contain a cover image.")
    sh(
        [
            "pandoc",
            str(master),
            "-o",
            str(epub),
            "--css",
            str(PANDOC_CSS),
            "--metadata-file",
            str(PANDOC_META),
            "--lua-filter",
            str(STORY_HEADING_FILTER),
            *cover_args,
            *metadata_args(metadata),
            "--toc",
            "--toc-depth=2",
        ]
    )
    sh([str(REPO / "tooling/scripts/epubcheck.sh"), str(epub)])  # exit non-zero -> subprocess raises -> Gate E fails (by design)

    pdf = exports / "print" / "interior.pdf"
    sh(["pandoc", str(master), "-o", str(pdf), "--pdf-engine=xelatex",
        "-H", str(PRINT_PREAMBLE), "--variable", "documentclass=book",
        "--variable", "classoption=twoside,openany", "--top-level-division=chapter",
        "--lua-filter", str(STORY_HEADING_FILTER), "--metadata", "story-heading-top=chapter",
        "--toc", "--toc-depth=2", *metadata_args(metadata)])

    direct_pdf = exports / "direct" / "reader.pdf"
    sh(["pandoc", str(master), "-o", str(direct_pdf), "--pdf-engine=xelatex",
        "-H", str(STORY_HEADING_STYLE),
        "--lua-filter", str(STORY_HEADING_FILTER), "--metadata", "story-heading-top=section",
        "--toc", "--toc-depth=2", *metadata_args(metadata)])

    platform_copies = [
        (epub, exports / "kdp" / "master.epub"),
        (pdf, exports / "kdp" / "interior.pdf"),
        (epub, exports / "direct" / "master.epub"),
    ]
    if cover_image.exists():
        platform_copies += [
            (cover_image, exports / "kdp" / "front-cover.jpeg"),
            (cover_image, exports / "direct" / "front-cover.jpeg"),
        ]
    for source, target in platform_copies:
        target.write_bytes(source.read_bytes())
        log_event(book_dir, target)
    log_event(book_dir, epub)
    log_event(book_dir, pdf)
    log_event(book_dir, direct_pdf)

    words = len(master.read_text().split())
    print(f"OK: {len(chapters)} chapters, {words} words -> EPUB, KDP print PDF, direct reader PDF")
    return 0


if __name__ == "__main__":
    sys.exit(main())
