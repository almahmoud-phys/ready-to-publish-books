#!/usr/bin/env python3
"""Contract checks for the per-book constitution and template inheritance."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = REPO_ROOT / "books" / "_template" / "constitution.md"
NEW_BOOK_SCRIPT = REPO_ROOT / "tooling" / "scripts" / "new-book.sh"
REGISTRY = REPO_ROOT / "books" / "registry.yaml"
SKILLS = sorted((REPO_ROOT / ".agents" / "skills").glob("*/SKILL.md"))

CONSTITUTION_PATH = "books/<slug>/constitution.md"
EXPECTED_HEADINGS = [
    "## Purpose",
    "## Authority order of records",
    "## Immutable-at-a-stage principles",
    "## Course-correction triggers",
    "## Amendment protocol",
    "## Conflict rule",
    "## Append-only amendment log",
]
EXPECTED_TERMS = [
    "stage-earned operational facts",
    "state.json",
    "compliance_log.yaml",
    "append-only",
    "append-only amendment log",
    "conflicts",
]


def _always_read_block(text: str) -> str:
    match = re.search(r"^\s*always_read:\s*\[(.*)\]\s*$", text, re.M)
    if not match:
        return ""
    return match.group(1)


def test_template_constitution_exists_and_has_governance_terms():
    assert TEMPLATE.exists(), "books/_template/constitution.md does not exist"
    text = TEMPLATE.read_text(encoding="utf-8")
    for heading in EXPECTED_HEADINGS:
        assert heading in text, f"constitution.md missing heading: {heading}"
    lower = text.lower()
    for term in EXPECTED_TERMS:
        assert term in lower, f"constitution.md missing governance term: {term}"


def test_all_skills_read_constitution():
    assert SKILLS, "no SKILL.md files discovered"
    missing = []
    for skill in SKILLS:
        text = skill.read_text(encoding="utf-8")
        block = _always_read_block(text)
        if not block:
            missing.append(f"{skill}: no always_read block")
            continue
        if CONSTITUTION_PATH not in [s.strip() for s in block.split(",")]:
            missing.append(f"{skill}: constitution.md not in always_read")
    assert not missing, "some skills do not read constitution: " + ", ".join(missing)


def test_new_book_factory_inherits_template_as_whole():
    text = NEW_BOOK_SCRIPT.read_text(encoding="utf-8")
    expected_copy = 'cp -r "$REPO/books/_template" "$BOOK_DIR"'
    assert expected_copy in text, "new-book.sh no longer copies template directory wholesale"
    assert (CONSTITUTION_PATH in TEMPLATE.read_text(encoding="utf-8")), "new-book.sh should inherit constitution.md via template copy"
    assert "books/_template/constitution.md" not in text, "new-book.sh should not reference template constitution file directly"


def test_registered_books_have_constitution():
    registry = REGISTRY.read_text(encoding="utf-8")
    slugs = re.findall(r"^\s*- slug:\s*([^\s#]+)", registry, re.M)
    assert slugs, "books/registry.yaml contains no registered books"
    missing = [slug for slug in slugs if not (REPO_ROOT / "books" / slug / "constitution.md").exists()]
    assert not missing, "registered books missing constitution.md: " + ", ".join(missing)


def main():
    checks = [
        test_template_constitution_exists_and_has_governance_terms,
        test_all_skills_read_constitution,
        test_new_book_factory_inherits_template_as_whole,
        test_registered_books_have_constitution,
    ]
    for check in checks:
        check()
        print(f"PASS  {check.__name__}")
    print(f"all {len(checks)} constitution contract checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
