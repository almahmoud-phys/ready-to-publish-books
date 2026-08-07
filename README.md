# ready-to-publish-books

Harness-driven pipeline: one-line book idea → ready-to-publish package (EPUB + print PDF + cover + metadata + compliance record).

- **Status**: M0 scaffold complete (2026-08-08)
- **Entry point**: `CLAUDE.md`
- **Structure**: `.agent/` (skills, rules, workflows, memories) · `books/` (per-book workspaces) · `pipeline/` (orchestrator, M2) · `tooling/` (pandoc/latex, harvest) · `tests/` (golden-book regression)
- **Governance**: `implementation_plan.md` + `decisions-log.md` (ADR-001…006)
- **Private**: contains unpublished manuscripts and niche research.

## Operating principles

Goal (Meadows LP3): a durable catalog of genuinely useful books — never book count.
Draft before judgment · floor principle (book = weakest dimension) · compliance by construction · loop-back not restart · gates live in rules, not sessions.
