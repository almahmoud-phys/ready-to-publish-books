#!/usr/bin/env python3
"""Contract checks for task-ledger maintenance and book architecture templates."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TASK_TEMPLATE = REPO_ROOT / "books" / "_template" / "tasks.md"
TASK_RULE = REPO_ROOT / ".agents" / "rules" / "task-ledger.md"
OUTLINE_DIR = REPO_ROOT / "books" / "_template" / "outline"
NEW_BOOK_SCRIPT = REPO_ROOT / "tooling" / "scripts" / "new-book.sh"
REGISTRY = REPO_ROOT / "books" / "registry.yaml"
SKILLS = sorted((REPO_ROOT / ".agents" / "skills").glob("*/SKILL.md"))

TASK_PATH = "books/<slug>/tasks.md"
TASK_RULE_PATH = ".agents/rules/task-ledger.md"
STAGE_HEADINGS = [f"## Stage {stage}" for stage in range(8)]
DETAIL_FIELDS = [
    "**Owner:**", "**Why:**", "**Depends on:**", "**Generate / update:**", "**Inputs:**",
    "**Procedure:**", "**Acceptance criteria:**", "**Verification / evidence:**",
    "**Blockers / escalation:**",
]
OUTLINE_FILES = ["README.md", "outline.template.md", "chapter.template.md"]


def _frontmatter_list(text: str, field: str) -> str:
    match = re.search(rf"^\s*{re.escape(field)}:\s*\[(.*)\]\s*$", text, re.M)
    return match.group(1) if match else ""


def _registered_slugs() -> list[str]:
    text = REGISTRY.read_text(encoding="utf-8")
    return re.findall(r"^\s*- slug:\s*([^\s#]+)", text, re.M)


def test_task_template_is_detailed_and_expandable():
    assert TASK_TEMPLATE.exists(), "books/_template/tasks.md does not exist"
    text = TASK_TEMPLATE.read_text(encoding="utf-8")
    for heading in STAGE_HEADINGS:
        assert heading in text, f"task template missing lifecycle heading: {heading}"
    for field in DETAIL_FIELDS:
        assert field in text, f"task template missing required expansion field: {field}"
    for task_id in ["S0-010", "S1-020", "S2-030", "CH-NN-100", "S7-040"]:
        assert f"`{task_id}`" in text, f"task template missing task: {task_id}"
    assert "Repeat for every approved chapter" in text
    assert "## Blocked work" in text
    assert "## Decisions needed from the human" in text
    assert len(text.splitlines()) >= 200, "task template is not detailed enough"


def test_task_rule_defines_record_boundaries_and_evidence():
    text = TASK_RULE.read_text(encoding="utf-8")
    for term in ["state.json", "constitution.md", "outline/outline.md", "Acceptance criteria"]:
        assert term in text, f"task rule missing boundary/evidence term: {term}"
    assert "checkbox never advances state" in text.lower()
    assert "per-chapter rule" in text.lower()


def test_all_skills_consume_and_update_task_ledger():
    assert len(SKILLS) == 14, f"expected 14 skills, found {len(SKILLS)}"
    failures = []
    for skill in SKILLS:
        text = skill.read_text(encoding="utf-8")
        always_read = _frontmatter_list(text, "always_read")
        read = _frontmatter_list(text, "read")
        outputs = _frontmatter_list(text, "outputs")
        if TASK_RULE_PATH not in always_read:
            failures.append(f"{skill}: task-ledger rule not in always_read")
        if TASK_PATH not in read:
            failures.append(f"{skill}: tasks.md not in scoped read")
        if TASK_PATH not in outputs:
            failures.append(f"{skill}: tasks.md evidence not in outputs")
    assert not failures, "; ".join(failures)


def test_registered_books_have_task_and_outline_scaffolds():
    slugs = _registered_slugs()
    assert slugs, "registry has no books"
    missing = []
    for slug in slugs:
        book = REPO_ROOT / "books" / slug
        if not (book / "tasks.md").exists():
            missing.append(f"{slug}/tasks.md")
        for name in OUTLINE_FILES:
            if not (book / "outline" / name).exists():
                missing.append(f"{slug}/outline/{name}")
    assert not missing, "registered books missing planning artifacts: " + ", ".join(missing)


def test_outline_templates_define_master_and_chapter_hierarchy():
    for name in OUTLINE_FILES:
        assert (OUTLINE_DIR / name).exists(), f"missing outline scaffold: {name}"
    master = (OUTLINE_DIR / "outline.template.md").read_text(encoding="utf-8")
    chapter = (OUTLINE_DIR / "chapter.template.md").read_text(encoding="utf-8")
    for term in ["Reader transformation", "Hierarchy and promise chain", "Dependency map",
                 "Learning and difficulty progression", "Gate A self-check"]:
        assert term in master, f"master outline template missing: {term}"
    for term in ["Section skeleton", "Teaching and example contract", "Evidence contract",
                 "Asset and dependency contract", "Acceptance criteria"]:
        assert term in chapter, f"chapter template missing: {term}"


def test_factory_materializes_task_identity():
    text = NEW_BOOK_SCRIPT.read_text(encoding="utf-8")
    assert '"$BOOK_DIR/tasks.md"' in text
    assert 's|<book title>|$TITLE_MD_ESC|g' in text
    assert 's|<slug>|$SLUG|g' in text
    assert 's|<iso8601>|$NOW|g' in text


def main():
    checks = [test_task_template_is_detailed_and_expandable,
              test_task_rule_defines_record_boundaries_and_evidence,
              test_all_skills_consume_and_update_task_ledger,
              test_registered_books_have_task_and_outline_scaffolds,
              test_outline_templates_define_master_and_chapter_hierarchy,
              test_factory_materializes_task_identity]
    for check in checks:
        check()
        print(f"PASS  {check.__name__}")
    print(f"all {len(checks)} task/outline contract checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
