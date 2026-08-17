# Ready To Publish Books — Harness Router

> **Goal (Meadows LP3)**: a durable catalog of genuinely useful books — never book count.
> **IFR (TRIZ)**: the book researches, writes, audits, scores, and packages itself. The human chooses the niche, approves the outline, and clicks publish.

This file is the **single entry point** for any agent harness working in this repo. Read it fully before acting. Skills live in `.agents/skills/`, rules in `.agents/rules/`, per-book state in `books/<slug>/`.

`.claude/skills` is a symlink to `.agents/skills` — Claude Code only auto-discovers skills under `.claude/`, so the symlink makes the 13 pipeline skills invokable by name (`/scorer`, `/niche-research`, …) without duplicating them. `.agents/` stays the source of truth for every harness. **Auto-discovery does not relax the DAG**: a skill being invokable says nothing about it being due. Stage order and the HITL gates in this file decide what runs.

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
| 6 | `metadata-seo` → golden sample → `formatter-platform` + `cover-director` → `kdp-publishing` | cheap / external / tooling | `exports/release/` + release manifest |
| 7 | `publish-checklist` | mid | go/no-go + exact upload runbook |
| — | **HITL GATE 2**: human publishes | — | — |

## Non-negotiable operating rules

1. **Separation in time** — draft fast, judge later. In M1, `chapter-writer` should avoid scoring rubrics by contract; in M2, subprocess/context isolation enforces it. `scorer` runs only on complete drafts.
2. **Floor principle** — a book is its weakest dimension. Every score cites the manuscript (`.agents/rules/scoring-contract.md`).
3. **Loop-back, not restart** — a failed gate routes to the *exact failing stage* with cited evidence. Max 3 cycles, then escalate to human.
4. **Compliance by construction** — every generation event is appended to `books/<slug>/compliance_log.yaml` (`.agents/rules/kdp-compliance.md`).
5. **Record precedence** — `manifest.yaml` is authoritative for stage-earned operational facts, `state.json` is authoritative for stage status, `compliance_log.yaml` is append-only evidence, `outline/` owns content architecture, and `tasks.md` coordinates work without overriding any of them.
6. **Context discipline** — each skill's frontmatter declares what it may and may not read, including the per-book `constitution.md` that must be loaded at every stage.
7. **Constitution governance** — `constitution.md` is amend-only with explicit owner approval, and any approved change must be reconciled by rerunning affected stages before progression.
8. **Conflict stop** — if `manifest.yaml`, `state.json`, `compliance_log.yaml`, and `constitution.md` disagree, stop for human reconciliation before any next stage runs.
9. **Gates live in rules, not sessions** — thresholds change only via edits to `.agents/rules/quality-gates.md`, never mid-session (Drifting Goals tripwire).
10. **Detailed task evidence** — every skill reads `.agents/rules/task-ledger.md` and its active-stage section in `tasks.md`, expands work before execution, and records acceptance evidence before checking it complete. A checkbox never advances `state.json`.
11. **Working files are not release files** — only artifacts promoted into `exports/release/` and
    recorded in its machine-generated manifest may be named in an upload runbook. A filename such as
    `final.pdf`, a successful export, or a visual approval does not make an artifact authoritative.
12. **One production identity** — title, subtitle, author/pen name, language, trim, paper, bleed,
    cover finish, and edition must be frozen and reconciled across metadata, manuscript, cover, and
    platform forms before final packaging. Any later change invalidates every dependent artifact.

## Stage-6 production and release control

Stage 6 is a promotion pipeline, not a directory full of exports:

1. **Preflight:** prove the required toolchain and a representative build before production work.
2. **Freeze:** record the approved production identity and platform choices in repository state.
3. **Golden sample:** approve one representative print opening, one EPUB opening/navigation path,
   and cover thumbnail/full-wrap views before generating every page and derivative.
4. **Build from sources:** use one continuous full-wrap cover after the final page count is known;
   derive the ebook front cover from that approved master. Compile all interiors reproducibly.
5. **Promote:** copy only the exact upload candidates to `exports/release/`; run
   `.agents/skills/kdp-publishing/scripts/release_preflight.py`; write a manifest containing hashes,
   dimensions, page count, and relevant metadata.
6. **Platform proof:** record the uploaded hashes and exact KDP form answers, inspect the complete
   Previewer output, and inspect a physical proof for a first edition or materially changed build.
   A human may explicitly waive the physical proof, but the waiver and risk must be recorded.

Changing manuscript pagination, trim, paper, bleed, title/subtitle/byline, or cover art after a
promotion invalidates the release manifest and every downstream approval. Rebuild and promote again.

## Model routing

Which model to use for drafting, judging and reviewing is **measured, not assumed** — see
`.agents/rules/model-routing.md`. Two rules are load-bearing: no model is its own last reader (every
draft gets an independent read before it counts as done), and quality panels use **independent model
families, never personas on one model**, with thresholds preregistered before any judge is dispatched.

## Running a book

- **Interactive (Claude Code)**: work stage by stage. Load only the active skill's SKILL.md. Stop at HITL gates and wait for the human.
- **Batch (CLI)**: `pipeline/orchestrator.py` (built at M2) runs the DAG, invokes skills as subprocesses, enforces gates, writes `state.json` + `compliance_log.yaml`.

## Memory loop (LP6)

Every finished book ends with a retrospective distilled into `.agents/memories/` (patterns, pitfalls, scoring insights). Book N+1 must inherit book N's lessons — check memories at stage 0.

## Workflows

`.agents/workflows/` vendors the cognitive protocols used in this repo: `cead-protocol` (deep-reasoning engine) and `fable-loop` (plan → execute → adversarial verify → honest report). Complex stages (3, 4, 7) run under fable-loop discipline.
