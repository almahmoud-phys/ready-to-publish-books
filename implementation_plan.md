# Implementation Plan — "Ready To Publish Books"

# Objective

Build an automated, harness-driven pipeline that takes a one-line book idea to a **ready-to-publish** package (EPUB + print PDF + cover + KDP metadata + compliance record), with quality gates, adversarial verification, managed context, and a learning loop that makes every subsequent book better. Human touches only two gates: outline approval and the publish click.

## Context & Reflection (evidence base)

### Reference architectures (all converge on the same shape)

| Project | Shape | Key lesson |
|---|---|---|
| `Harshil-Jani/kindle-book-agency` | 8 agents, CLAUDE.md-driven, deps-aware parallel phases, `.docx` output | Zero-setup in Claude Code; agent prompts as markdown files; parallel same-phase agents |
| `guerra2fernando/libriscribe` | Multi-agent Python CLI, per-project workspace (outline.md, characters.json, chapter_N.md) | Per-book workspace as the unit of state |
| `wesleyscholl/book-generator` | Shell + Pandoc + LaTeX + ImageMagick, multi-provider fallback | **Proven**: 2 books passed KDP checks, <$50/book, ~85% automated; Pandoc/LaTeX is the export backbone |
| Book Genesis v4 (felipelobomotta) | Agent-agnostic folder-of-markdown: manifests, prompts, scoring contracts | Draft BEFORE judgment; adversarial audit BEFORE scoring; evidence-based scoring (every dimension cites the manuscript); **floor principle** over 10 dimensions |
| Reddit Claude-Code book skills (x2) | 15–20 Claude Code skills, one sentence → 60k words | Skills-as-pipeline is a validated pattern in this exact harness |

### Book Genesis v4 scoring dimensions (adopt as our scoring contract)

Originality · Theme · Characters · Prose · Pacing · Emotion · Coherence · Market · Voice · Opening. **Book score = min(dimensions)** (floor principle). Every score must cite manuscript lines. No vibes.

### KDP compliance reality (2026)

- AI-generated **text, images (incl. cover), translations must be disclosed** at publish time — even after substantial editing. Disclosure is an internal compliance record, not a public badge.
- AI-*assisted* (human wrote the prose; AI brainstormed/outlined/edited) requires **no disclosure** and retains full copyright.
- Enforcement: automated detection + human review. Non-disclosure → book removal; patterns of non-disclosure or low-quality AI catalogs → **account termination / account-wide restrictions**.
- 3 titles/day publish cap.
- AI-generated portions are **not copyrightable** (US). If IP matters for a title, it must run the AI-assisted track with genuinely human-authored prose.
- Internal record-keeping of which tools generated what is recommended practice → we make it structural (`compliance_log.yaml`).

## Systems-Innovation Analysis (TRIZ × Meadows)

### Core contradiction

Improving **throughput and cost** (P9 Speed, P25 Loss of time, P39 Productivity) worsens **quality and account safety** (P27 Reliability, P24 Loss of information).

Resolutions:

| TRIZ principle | Application |
|---|---|
| Separation in time (physical contradiction) | Generation and evaluation never co-occur. Chapters are write-only until the adversarial stage. Draft fast, judge later. |
| P1 Segmentation | Skill-per-stage; chapter-level parallelism with worktree/subprocess isolation. |
| P10 Preliminary Action | Story bible + style sheet + outline contracts BEFORE prose — eliminates most coherence rework. |
| P23 Feedback | Failed gates loop back to the exact failing stage with the judge's cited evidence, not a full re-run. |
| P26 Copying | Judges read excerpts + rolling summaries per pass; full-manuscript read only at final audit. |
| P11 Beforehand Cushioning | Compliance log + originality/fact-check gates BEFORE anything approaches KDP. |

### Meadows leverage map

- **LP3 (Goals)**: System goal = *"durable catalog of genuinely useful books"* — explicitly NOT book count. Volume is LP12 parameter-pushing and triggers the KDP enforcement archetypes.
- **Archetypes designed against**:
  - *Fixes That Fail*: publish slop → account restriction → catalog dies. Gate: floor-principle scoring, no publish below threshold.
  - *Tragedy of the Commons*: KDP is flooded with AI books (releases ~tripled 2022–2025). Response: niche quality + series depth, not volume.
  - *Drifting Goals*: never lower the score floor to hit throughput. The floor is in `rules/quality-gates.md`, not in a session prompt.
- **LP6 (Information flows)**: per-book retrospective → distilled patterns → `.agent/memories/` (Tier-2 memory protocol). Book N+1 inherits book N's lessons.
- **LP8 (Negative feedback)**: adversarial editor + evidence-based scorer as standing balancing loops; their strength scales with output volume.

### Ideal Final Result

*The book researches, writes, audits, scores, and packages itself. The human chooses the niche, approves the outline, and clicks publish.*

## Chosen Strategy

**Agent-agnostic repo, Claude Code-first.** The product is a folder of markdown contracts (skills, rules, manifests, scoring rubrics) + a thin Python orchestrator. Claude Code runs it interactively via CLAUDE.md; the same skills run headless via CLI subprocesses for batch mode. This matches the CEAD portability principle: no harness-specific lock-in, nothing halts because a file is missing.

Alternatives dismissed:
- *Single mega-prompt generator* — fails coherence at book length, no gates. (P1 segmentation wins.)
- *Heavy agent framework (LangGraph/CrewAI/AutoGen) from day one* — premature structure (LP10); the folder-of-markdown proves the pipeline first, framework later if needed.
- *Volume-first KDP strategy* — LP12; triggers Fixes-That-Fail with account enforcement.

## Execution Plan

### Repo layout

```
ready-to-publish-books/
├── CLAUDE.md                      # router: pipeline map, stage table, gate rules
├── AGENTS.md                      # harness-agnostic mirror of CLAUDE.md
├── .agent/
│   ├── skills/                    # one SKILL.md per stage (the prepared skills)
│   │   ├── niche-research/SKILL.md
│   │   ├── outline-architect/SKILL.md
│   │   ├── story-bible/SKILL.md
│   │   ├── chapter-writer/SKILL.md
│   │   ├── continuity-keeper/SKILL.md
│   │   ├── adversarial-editor/SKILL.md
│   │   ├── scorer/SKILL.md
│   │   ├── proofreader/SKILL.md
│   │   ├── fact-checker/SKILL.md
│   │   ├── formatter-platform/SKILL.md
│   │   ├── cover-director/SKILL.md
│   │   ├── metadata-seo/SKILL.md
│   │   └── publish-checklist/SKILL.md
│   ├── rules/                     # quality-gates.md, kdp-compliance.md, style.md, scoring-contract.md
│   ├── workflows/                 # vendored cead-protocol + fable-loop
│   └── memories/                  # tier-2 retrospectives + pattern library
├── pipeline/
│   ├── orchestrator.py            # deps-aware DAG runner, parallel same-phase, resumable (M2)
│   ├── router.py                  # model routing table (stage → model tier) (M2)
│   └── state.py                   # state.json ledger read/write (M2)
├── books/<slug>/                  # per-book workspace = the managed context
│   ├── manifest.yaml              # goal, genre, track (generated|assisted), gates, models
│   ├── state.json                 # resumable stage ledger
│   ├── compliance_log.yaml        # every generation event: tool, model, artifact hash
│   ├── research/ outline/ bible/
│   ├── chapters/                  # chapter_NN.md (write-only until stage 3)
│   ├── summaries/                 # 200-word rolling chapter summaries
│   ├── audits/ scores/ edits/
│   └── exports/                   # epub, pdf, cover, metadata.json
├── tooling/
│   ├── pandoc/ (templates, epub.css, metadata.yaml)
│   ├── latex/ (print interior template)
│   └── scripts/ (epubcheck wrapper, cover assembly, word counts)
└── tests/                         # golden-book regression: fixed seed idea → gate outputs
```

### Pipeline DAG (deps-aware; same-phase stages parallel)

```
0  niche-research                                    → research/niche.md
1  outline-architect + story-bible                   → outline/, bible/
   ── HITL GATE 1: human approves outline ──
2  chapter-writer × N (parallel, worktree isolation) → chapters/
   continuity-keeper (after each batch)              → summaries/
3  adversarial-editor (structure attack, no score)   → audits/structural.md
4  scorer (10-dim, floor, citations)                 → scores/scorecard.json
   loop-back: any dim < floor → exact stage, with cited evidence (max 3 cycles)
5  proofreader + fact-checker (parallel)             → edits/
6  metadata-seo                                      → exports/metadata.json, exports/blurbs.md
   cover-director + formatter-platform                → exports/
7  publish-checklist                                 → go/no-go + disclosure answers
   ── HITL GATE 2: human publishes ──
```

### Managed context rules (the differentiator)

1. `manifest.yaml` + `bible/` are the ONLY artifacts loaded at every stage.
2. Chapters never re-enter context in full after writing. Continuity runs on 200-word rolling summaries in `summaries/`.
3. Each SKILL.md frontmatter declares its **context budget**: files to read, files forbidden to read.
4. Draft-before-judgment is a M1 contract expectation, not a hard runtime guarantee: chapter-writer should avoid scoring rubrics, and this is enforced by isolation in M2; scorer runs only on complete drafts.
5. Judges get excerpts + summaries per pass; full read only at final audit.
6. Retrospective at book end → `.agent/memories/` pattern entries.

### Model routing (router.py defaults; overridable per-book in manifest)

| Stage | Tier | Rationale |
|---|---|---|
| outline-architect, adversarial-editor, scorer | strong (Opus-class) | decisions and judgment live here |
| chapter-writer | mid (Sonnet-class) | quality/cost sweet spot, parallelizable |
| continuity, proofreader, metadata, keyword extraction | cheap (Haiku-class / local) | mechanical, high volume |
| niche-research evidence gatherers | cheap | fable-loop model economy: gatherers cheap, deciders strong |
| cover prompts → image gen | external (image API or manual) | cost control, per book-generator precedent |

Target: **<$30–50 per book** end-to-end (proven benchmark: book-generator).

### Quality gates (rules/quality-gates.md)

- **Gate A (post-outline)**: outline contract completeness — every chapter has purpose, word budget, and dependency links. HITL approval.
- **Gate B (post-audit)**: structural attack must be answered — zero open critical findings.
- **Gate C (scoring)**: floor principle — every dimension ≥ threshold (default 7/10, non-negotiable in-session; changes only via PR to the rules file). Max 3 loop-back cycles per dimension, then escalate to human with evidence.
- **Gate D (pre-export)**: proofread edit log applied 100%; fact-check flags all resolved (verified / rewritten / cut).
- **Gate E (pre-publish)**: epubcheck passes; PDF renders; compliance_log complete → disclosure answers generated; originality check run.

### Compliance architecture (rules/kdp-compliance.md)

- `compliance_log.yaml` is append-only and written by the orchestrator at every generation event (timestamp, skill, model, artifact, hash). This IS the internal record KDP policy recommends.
- Per-book `track: generated | assisted` in the manifest, decided at Gate 1. Assisted track = human-authored prose workflow (AI outlines/edits only) for titles where copyright retention matters.
- publish-checklist emits the exact disclosure answers (text/images/translation) from the log — no reliance on memory.
- Rate discipline: respect 3 titles/day cap; batch scheduler enforces it.

## Verification Plan

- **Golden-book regression** (`tests/`): fixed-seed short book (3 chapters) runs the full DAG; assert gate artifacts exist, scorecard schema valid, compliance log complete, epubcheck exit 0.
- **Adversarial verification** (fable-loop Stage 3): attacker subagents per consequential change — "prove this chapter contradicts the bible", "find an unresolvable claim in this non-fiction draft", "diff outputs against declared scope".
- **M1 acceptance**: one real non-fiction book (8–12k words, niche you know — e.g., a photonics/AI-adjacent practitioner guide) walks through skills manually and reaches Gate E. Quality judged by YOU reading it cover to cover.
- **Cost audit**: router logs token spend per stage per book into state.json; alert if a book exceeds budget ceiling.

## Milestones

| # | Deliverable | Exit criteria |
|---|---|---|
| M0 | Repo scaffold, all 13 SKILL.md drafts, rules, CLAUDE.md | Skills load in Claude Code; router table agreed |
| M1 | First book, manual skill walk-through (no orchestrator) | Gate E reached; you approve the prose |
| M2 | Orchestrator: DAG, parallelism, resumability, model router | Interrupted run resumes correctly; parallel chapters don't collide |
| M3 | Scoring contracts + adversarial loop + loop-back wiring | Floor principle enforced; failed gate routes to correct stage |
| M4 | Export hardening: epubcheck, print PDF, cover assembly, metadata | KDP-ready package; first book published |
| M5 | Batch mode + memory loop + cost dashboard | Book 2 cheaper and better-scored than book 1 |

## Decisions (locked 2026-08-07 — see decisions-log.md)

1. **Non-fiction first** (ADR-001) ✅
2. **Dual-track assisted/generated per title at Gate 1** (ADR-002) ✅
3. **Plain Python + subprocess CLI** orchestrator (ADR-003) ✅
4. **Multi-platform: KDP + direct sales + wide later; no KU** (ADR-004) ✅
5. **AI-image covers; typography-vs-imagery sub-decision deferred to M4** (ADR-005) ✅
6. **Greenfield repo + M0 harvest phase; no cloning** (ADR-006) ✅
