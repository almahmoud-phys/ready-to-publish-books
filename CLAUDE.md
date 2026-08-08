# Ready To Publish Books — Harness Router

> **Goal (Meadows LP3)**: a durable catalog of genuinely useful books — never book count.
> **IFR (TRIZ)**: the book researches, writes, audits, scores, and packages itself. The human chooses the niche, approves the outline, and clicks publish.

This file is the **single entry point** for any agent harness working in this repo. Read it fully before acting. Skills live in `.agent/skills/`, rules in `.agent/rules/`, per-book state in `books/<slug>/`.

## Pipeline map (dependency-aware DAG)

| Stage | Skill | Model tier | Output |
|---|---|---|---|
| 0 | `niche-research` | cheap gatherers → strong synthesis | `research/niche.md` |
| 1 | `outline-architect` + `story-bible` | strong | `outline/`, `bible/` |
| — | **HITL GATE 1**: human approves outline; `track` locked in manifest | — | manifest updated |
| 2 | `chapter-writer` ×N (parallel) + `continuity-keeper` | mid / cheap | `chapters/`, `summaries/` |
| 3 | `adversarial-editor` | strong | `audits/structural.md` |
| 4 | `scorer` | strong | `scores/scorecard.json` |
| 5 | `proofreader` + `fact-checker` (parallel) | cheap / mid | `edits/` |
| 6 | `metadata-seo` → `formatter-platform` + `cover-director` | cheap / external | `exports/` |
| 7 | `publish-checklist` | mid | go/no-go + disclosure answers |
| — | **HITL GATE 2**: human publishes | — | — |

## Non-negotiable operating rules

1. **Separation in time** — draft fast, judge later. In M1, `chapter-writer` should avoid scoring rubrics by contract; in M2, subprocess/context isolation enforces it. `scorer` runs only on complete drafts.
2. **Floor principle** — a book is its weakest dimension. Every score cites the manuscript (`.agent/rules/scoring-contract.md`).
3. **Loop-back, not restart** — a failed gate routes to the *exact failing stage* with cited evidence. Max 3 cycles, then escalate to human.
4. **Compliance by construction** — every generation event is appended to `books/<slug>/compliance_log.yaml` (`.agent/rules/kdp-compliance.md`).
5. **Context discipline** — each skill's frontmatter declares what it may and may not read. Honor it strictly (see `.agent/rules/` + skill frontmatter).
6. **Gates live in rules, not sessions** — thresholds change only via edits to `.agent/rules/quality-gates.md`, never mid-session (Drifting Goals tripwire).

## Running a book

- **Interactive (Claude Code)**: work stage by stage. Load only the active skill's SKILL.md. Stop at HITL gates and wait for the human.
- **Batch (CLI)**: `pipeline/orchestrator.py` (built at M2) runs the DAG, invokes skills as subprocesses, enforces gates, writes `state.json` + `compliance_log.yaml`.

## Memory loop (LP6)

Every finished book ends with a retrospective distilled into `.agent/memories/` (patterns, pitfalls, scoring insights). Book N+1 must inherit book N's lessons — check memories at stage 0.

## Workflows

`.agent/workflows/` vendors the cognitive protocols used in this repo: `cead-protocol` (deep-reasoning engine) and `fable-loop` (plan → execute → adversarial verify → honest report). Complex stages (3, 4, 7) run under fable-loop discipline.
