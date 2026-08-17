# Implementation Plan — "Ready To Publish Books"

> **What this file is**: the canonical build plan for the *pipeline itself* — the evidence base
> it was designed from, the TRIZ/Meadows analysis behind its shape, the repo layout, the stage
> DAG, the managed-context rules, the model-routing table, and the M0–M5 milestones. It answers
> *why the system is built this way*.
>
> **Status: LIVE — M0 done, M1 active, M2–M5 open.** Not an archive. It moves to `docs/` only
> once M5 ships, at which point it becomes the design record.
>
> **What this file is not**: the runtime contract. `CLAUDE.md` routes an agent through the
> pipeline, `.agents/rules/*.md` hold the enforcing thresholds, and `decisions-log.md` holds the
> locked ADRs. Where this plan and a rule disagree, **the rule wins** — this document describes
> intent, the rules are what execute. Sections below marked with a milestone (M2, M4…) describe
> components that do not exist yet.

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
- **LP6 (Information flows)**: per-book retrospective → distilled patterns → `.agents/memories/` (Tier-2 memory protocol). Book N+1 inherits book N's lessons.
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
├── books/_template/constitution.md # per-book governance contract copied into every new workspace
├── .agents/
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
│   ├── constitution.md            # per-book governance contract (read at every stage)
│   ├── manifest.yaml              # goal, genre, track (generated|assisted), gates, models
│   ├── state.json                 # resumable stage ledger
│   ├── compliance_log.yaml        # every generation event: tool, model, artifact hash
│   ├── tasks.md                    # detailed human/AI checklist; never pipeline state
│   ├── research/ outline/ bible/   # outline owns hierarchy + per-chapter contracts
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

1. `manifest.yaml`, `constitution.md`, and `bible/` are the core artifacts loaded at every stage.
2. Chapters never re-enter context in full after writing. Continuity runs on 200-word rolling summaries in `summaries/`.
3. Each SKILL.md frontmatter declares its **context budget**: files to read, files forbidden to read.
4. Draft-before-judgment is a M1 contract expectation, not a hard runtime guarantee: chapter-writer should avoid scoring rubrics, and this is enforced by isolation in M2; scorer runs only on complete drafts.
5. Judges get excerpts + summaries per pass; full read only at final audit.
6. Retrospective at book end → `.agents/memories/` pattern entries.

### Book contract and amendment protocol

- `books/_template/constitution.md` is copied verbatim into every new workspace by `new-book.sh`, making `constitution.md` part of factory inheritance.
- Every stage contract should list `books/<slug>/constitution.md` under `always_read`.
- Amendment rule: owner approval required; any amendment records scope and trigger; affected stages must re-run before progress resumes.
- Conflict rule: when `constitution.md`, `manifest.yaml`, `state.json`, or `compliance_log.yaml` disagree, stop for reconciliation before any new stage starts.

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
| M0 ✅ | Repo scaffold, all 13 SKILL.md drafts, rules, CLAUDE.md | **Met 2026-08-08** — skills load in Claude Code via the `.claude/skills` → `.agents/skills` symlink; router table agreed |
| M1 ▶ | First book, manual skill walk-through (no orchestrator) | Gate E reached; you approve the prose · *stage 0 run 1 complete: PIVOT (`books/llm-cost-routing-playbook/research/niche.md`)* |
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

---

# M1 First Real Book Launch Plan — 2026-08-09

## Objective

Take one **new, authority-backed non-fiction practitioner guide** from a human-supplied seed to a verified KDP + direct-sales package, then stop at the human publish action. The existing `books/llm-cost-routing-playbook/` workspace remains a Stage-0 sample/fixture and is not the first real publication.

**Classification:** plan-first. The book choice is not yet present in the repo, the sample has been explicitly retired as a publication candidate by the owner, and publication is outward-facing.

**Definition of done:**

- a fresh `books/<slug>/` workspace reaches Gates A–E with reproducible evidence;
- every score dimension is at least 7/10 and cites the manuscript;
- all factual claims are verified, rewritten, or cut;
- EPUB passes `epubcheck`, the print PDF is visually inspected, and cover/metadata/compliance/originality checks pass;
- the owner reads and approves the complete book and performs the final publish action;
- the retrospective is captured for Book 2.

## Context & Reflection

### Evidence loaded

- The [Project Hub](https://app.notion.com/p/3b50c17b1b0c81f59fbafef8d28988ad) and its complete visible child tree were loaded on 2026-08-09. The hub's goal is a durable catalog of useful books, not throughput.
- The [Stage-0 guide](https://app.notion.com/p/3b70c17b1b0c819c8d8ce33eea5b2b17), [numbers guide](https://app.notion.com/p/3b70c17b1b0c81328724e8ce9b9e81dd), [Book 1 case study](https://app.notion.com/p/3b70c17b1b0c81a9a891f7a12aa88c3d), [failure guide](https://app.notion.com/p/3b70c17b1b0c812b9075c0c68ec97185), [post-GO route](https://app.notion.com/p/3b70c17b1b0c81878b27f034757571c3), and [stage reference](https://app.notion.com/p/3b70c17b1b0c81c6922ae160e0398bbe) confirm that a false Stage-0 signal is the most expensive upstream failure.
- The sample is a `PIVOT` with no outline, manuscript, score, or export. It is useful as a test fixture, not as book content: [`state.json`](books/llm-cost-routing-playbook/state.json), [`research/niche.md`](books/llm-cost-routing-playbook/research/niche.md).
- The current verdict prefers the ignored machine-global ledger over the committed book-local ledger: [`tooling/scripts/niche_verdict.py`](tooling/scripts/niche_verdict.py). The sample therefore changes result between this machine and a clean checkout.
- The Stage-0 contract requires refusal detection and exit 3, but [`tooling/scripts/niche_mine.sh`](tooling/scripts/niche_mine.sh) does not inspect KDP Scout output for refusal markers before reading its persistent database.
- M1 is intentionally a manual walkthrough. The M2 orchestrator does not exist yet, and building it now would automate contracts that the first real book has not validated.
- Codanna was used first, as requested. Its Python symbol index works, but documentation search is disabled and the index contains no document embeddings; Markdown contracts were therefore confirmed with narrow primary-file reads.

### Systems diagnosis

**Core contradiction:** move quickly toward a first publication without weakening evidence reliability, quality, or account safety.

- **Active archetypes:** Fixes That Fail (bad evidence produces a fast but wrong verdict) and Drifting Goals (schedule pressure invites weaker gates).
- **Highest accessible leverage:** LP5 rules and LP6 information flows. A trustworthy Stage-0 decision has more leverage than additional pipeline automation.
- **TRIZ resolution:** P10 Preliminary Action repairs the gate before book creation; P1 Segmentation isolates the new book from the sample and machine-global state; P23 Feedback makes refusals and provenance observable; P2 Taking Out excludes unrelated M2 work.
- **Ideal Final Result:** a book advances only when its committed local evidence reproduces the same verdict in a clean environment, a blocked collector cannot masquerade as absent demand, and unknowns remain `UNKNOWN` rather than guesses.

## Chosen Strategy

Run a **manual M1 critical path**:

1. harden only the two Stage-0 integrity seams;
2. obtain one human-authored seed and authority fence;
3. create a fresh book workspace;
4. run the existing skills stage by stage with their gates;
5. harden export tooling just before Stage 6, when the manuscript has earned that investment;
6. stop for the owner's final publish action.

Alternatives dismissed:

- **Continue the sample:** contradicts the owner's current instruction and would inherit sample-specific evidence, authority claims, and hidden-state defects.
- **Build M2 first:** expands scope into orchestration before the manual pipeline and its contracts have passed once.
- **Start drafting before GO:** shifts the burden from market validation to prose and makes sunk cost pressure part of the verdict.

## Execution Plan

### 0. Approval and decision record

- Obtain approval for this plan.
- Append an ADR amendment stating that `llm-cost-routing-playbook` is a non-publishing sample and the first real M1 title will use a fresh workspace. Do not rewrite historical ADR-007.
- Keep Notion as planning history and the repo as the runtime source of truth.

**Verification:** the decision is recorded without modifying the sample workspace.

### 1. Repair the Stage-0 trust boundary

Scope:

- `tooling/scripts/niche_mine.sh`
- `tooling/scripts/niche_verdict.py`
- `tests/test_niche_verdict.py`
- new deterministic `tests/test_niche_mine.py`
- `decisions-log.md` for the ADR amendment

Changes:

- capture and scan the current KDP Scout invocation for refusal markers; return exit 3 and append no rows on refusal;
- make verdict computation use only `books/<slug>/research/niche-ledger.csv` for book evidence;
- make the mining-to-book evidence transfer explicit rather than allowing the verdict to read shared machine state;
- replace environment-dependent tests with temporary, book-local fixtures;
- test empty-but-healthy, refused, consistent, inconsistent, unsigned-trademark, PIVOT, and GO paths.

**Verification:** shell syntax passes; both test programs pass; a clean-state run and a run with `.kdp-research/ledger/` present produce the same verdict; simulated refusal exits 3 and leaves the ledger unchanged.

### 2. Select and birth the real book

The owner supplies the one input the system cannot derive:

- reader problem and useful outcome;
- authority envelope and explicit exclusions;
- one seed idea plus allowed adjacent pivots;
- intended author identity/brand boundary.

I will convert that into one recommended seed/working title, then run:

```bash
./tooling/scripts/new-book.sh <slug> "<working title>"
```

Only `manifest.niche_seed` and the human-owned charter are filled before research. No persona, subtitle, market number, or differentiation promise is guessed.

**Verification:** factory validation passes; registry entry and all stage directories exist; the workspace contains no copied sample evidence or state.

### 3. Run Stage 0 to an honest verdict

- prove collector health with the control seed before interpreting zeros;
- mine charter-, harvest-, competitor-, or review-derived candidates only, with provenance;
- collect current trends, top-10 competitor facts, negative-review gaps, asset feasibility, and preliminary trademark evidence;
- require human verification for live comps and trademark risk acceptance;
- run `niche_verdict.py` and obey `GO | PIVOT | KILL | INCOMPLETE`;
- allow at most three charter-bounded pivots; never promote PIVOT/KILL without new evidence.

**Verification:** verdict recomputes from committed book-local evidence; every load-bearing current figure has a source and date; GO is impossible with an unknown field, failed control, refusal, or missing human trademark signoff.

### 4. Design the book and pass Gate A

- run `outline-architect`, then derive `story-bible` from the approved outline rather than pretending they are independent;
- reconcile the 8–12k M1 acceptance target with the 30k template default using the validated reader outcome and shelf evidence; record one explicit word target before drafting;
- present chapter promises, dependencies, asset needs, and track choice for approval;
- lock `assisted` or `generated` in both manifest and registry.

**Verification:** every chapter has a promise, word budget, dependency links, and required assets; bible matches the outline; owner approval is recorded.

### 5. Draft, attack, score, and correct

- write one chapter per invocation using only its contract and the bible;
- run continuity after each batch using summaries;
- run the adversarial structural audit on the complete draft;
- resolve critical findings, then score the complete post-audit manuscript;
- route every sub-7 dimension backward to its responsible stage with citations, maximum three cycles;
- sequence proofreader and fact-checker edits to avoid concurrent writes to the same chapters.

**Verification:** Gates B–D pass; no critical structural finding or factual flag remains; all compliance events and costs are logged; surrounding stage checks remain green.

### 6. Harden and run packaging just in time

- install/verify Pandoc, epubcheck, XeLaTeX, and the selected cover composition tool only when Stage D passes;
- resolve the byline/author field, direct-sales PDF/EPUB variants, export hashes, and the originality-check artifact before Gate E;
- run metadata first, formatter next, and cover print-spread work after final page count;
- render and visually inspect EPUB/PDF/cover, not merely infer success from file existence.

**Verification:** EPUB validation exits 0; print PDF and cover dimensions render correctly; every export is hashed in the append-only compliance log; metadata, rights, disclosure, originality, and platform variants are complete.

### 7. Publish and close the loop

- run `publish-checklist` and produce a go/no-go plus exact disclosure answers;
- obtain explicit owner authorization for the outward publication action;
- owner performs the KDP/direct-sales publish step;
- record publication state and write the first retrospective into `.agents/memories/`.

**Verification:** all Gates A–E are PASS; owner has read the complete book; live listings are observed; registry/state are updated; retrospective names reusable lessons and failures.

## Human Interaction Contract

There are two formal HITL gates, but the honest M1 workload includes these human inputs:

1. seed + authority charter;
2. live top-10 competitor verification + trademark signoff;
3. outline/track approval (formal Gate 1);
4. title/description and cover selection;
5. cover-to-cover manuscript approval + publish click (formal Gate 2).

This replaces the misleading claim that M1 needs only two human touches while preserving the two formal pipeline gates.

## Verification Plan

- **Preflight:** deterministic Stage-0 tests, refusal simulation, shell syntax, clean-state reproducibility.
- **Per stage:** emit the required Gate A–E verification block with file-and-line evidence.
- **Surrounding health:** run all repo tests after production-code changes; validate shell and Python syntax; run the relevant exporter checks after packaging changes.
- **Adversarial checks:** after consequential edits, use distinct attackers for behavioral correctness, scope drift, and contract contradiction.
- **Final observation:** validate files, inspect renders, recompute disclosure from the log, and observe the live listing after the owner publishes.

## Approval Gate

No Stage-0 code, decision record, or new book workspace will be changed until the owner approves this plan. After approval, execution starts at Step 1; the first book seed is collected only after the trust-boundary tests pass.
