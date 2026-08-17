#!/usr/bin/env python3
"""Regression checks for formatter pre-write safety gates."""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COMPILER = REPO_ROOT / "tooling" / "scripts" / "compile_book.py"
sys.path.insert(0, str(COMPILER.parent))

from compile_book import (  # noqa: E402
    demote,
    frontmatter_for_track,
    mark_story_opening,
    mark_unlisted_heading,
)


def test_compile_refuses_pipe_001_before_writing(tmp_path: Path):
    book = tmp_path / "book"
    book.mkdir()
    _ = (book / "state.json").write_text(
        json.dumps(
            {
                "stages": {
                    "5_proof-fact": {"gate_d": "PASS"},
                    "6_exports": {"blockers": ["PIPE-001"]},
                }
            }
        ),
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(COMPILER), str(book)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "PIPE-001 is unresolved" in result.stdout
    assert not (book / "exports").exists()
    assert not (book / "frontmatter.md").exists()


def test_generated_frontmatter_has_one_metadata_title_and_no_reader_disclosure():
    text = frontmatter_for_track(
        {"track": "generated", "title": "Manifest Placeholder"},
        {"title": "Selected Title", "subtitle": "Selected Subtitle"},
    )

    assert text.startswith('---\ntitle: "Selected Title"\nsubtitle: "Selected Subtitle"\n---')
    assert "# Selected Title" not in text
    assert "AI Disclosure" not in text
    assert "AI-generated" not in text
    assert "©" not in text
    assert "All rights reserved" not in text


def test_assisted_frontmatter_keeps_author_and_rights():
    text = frontmatter_for_track(
        {"track": "assisted", "title": "Selected Title", "author": "A. Writer"}
    )

    assert 'author: "A. Writer"' in text
    assert "# Copyright" in text
    assert "©" in text
    assert "A. Writer" in text
    assert "All rights reserved" in text


def test_story_opening_marker_survives_english_heading_demotion():
    marked = demote(mark_story_opening("# Story 1 — The Letter\n\nBody."))

    assert marked.startswith("## Story 1 — The Letter {.story-opening}")


def test_exercise_heading_is_not_marked_implicitly():
    exercise_heading = demote(mark_unlisted_heading("# Historia 1 — La carta\n\n**Preguntas**"))

    assert "story-opening" not in exercise_heading
    assert exercise_heading.startswith("## Historia 1 — La carta {.unnumbered .unlisted}")
