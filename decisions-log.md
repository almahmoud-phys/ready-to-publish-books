# Decisions Log — Ready To Publish Books

*Architecture Decision Records. Each entry: decision, contradiction analysis (TRIZ), leverage check (Meadows), rationale, consequences. Status: LOCKED unless noted.*

---

## ADR-001 — Non-fiction first

**Status**: ✅ LOCKED (2026-08-07)

**Decision**: The pipeline's first books are **non-fiction practitioner guides**. Fiction is deferred to M5+ at earliest.

**TRIZ read**: The coherence contradiction (long-form consistency vs. generation speed) is an order of magnitude harder with plot, character arcs, and foreshadowing. Non-fiction resolves it by **P1 Segmentation** — chapters are near-independent units with explicit outline contracts; there is no hidden narrative state to corrupt.

**Meadows read**: Quality must be *verifiable* for the balancing loops (LP8) to work. Non-fiction claims are fact-checkable → the fact-checker gate has teeth. Fiction quality is taste-based → weak feedback, Drifting Goals risk.

**Rationale**:
- Domain authority: your photonics/AI/engineering expertise is a real resource (TRIZ resource inventory: use what the system already has).
- Higher price points ($9.99–29.99 vs. $2.99 fiction norms) → fewer sales needed per unit of effort.
- Natural fit for the AI-assisted track (ADR-002) → full copyright.
- Comp titles and niche research are objectively analyzable (keywords, categories).

**Consequences**: Scorer rubric needs non-fiction dimensions (Accuracy, Usefulness, Structure) alongside the 10 fiction-leaning ones — weighted per genre in manifest.

---

## ADR-002 — Assisted vs. Generated track → DUAL-TRACK, decided per title at Gate 1

**Status**: ✅ LOCKED (2026-08-07)

**Decision**: The system supports **two tracks**, chosen per book in `manifest.yaml` at Gate 1, with a default rule:

- **Assisted track (default for anything under your name/brand)**: AI does research, outline, and editing; prose is human-authored (writing or dictation + cleanup). → Full copyright, no KDP disclosure required.
- **Generated track (pen-name niche experiments only)**: AI drafts prose end to end, human curates and approves. → No copyright on generated portions, mandatory KDP disclosure, logged in `compliance_log.yaml`.

**TRIZ read — the physical contradiction**: *The prose must be human-written (for copyright and authority) AND machine-written (for speed and scale).*
Resolution via the 4 separation principles:
1. **Separation by condition** → per-title track choice (the decision above).
2. **Separation between whole and parts** → within assisted-track books, the human owns the load-bearing substance (frameworks, experience, case studies, voice); the machine owns scaffolding (research, structure, edits, packaging).
3. **P10 Preliminary Action** → AI front-loads everything *before* prose, so the human's writing time is spent only on what machines can't own.
4. **P6 Universality** → one pipeline serves both tracks; the track flag only changes who writes chapters and what gets disclosed.

**Meadows read**: Copyrighted IP is an appreciating **stock**; disclosed AI-generated text is a non-ownable, platform-risk-carrying flow. The LP3 goal is a *durable catalog* → the default must maximize owned assets. Generated track exists for **LP4 self-organization**: cheap niche experiments that gather market information (LP6) without risking the brand account.

**Cost honesty**: Assisted ≈ 10–20 h human per book; Generated ≈ 1–2 h. The rule encodes this: spend human hours only where they create ownable, durable value.

**Consequences**:
- `track: assisted | generated` required in every manifest.
- publish-checklist emits different disclosure answers per track.
- Never mix undisclosed: if AI writes prose, the book is Generated, full stop.

---

## ADR-003 — Orchestrator: plain Python + subprocess CLI

**Status**: ✅ LOCKED (2026-08-07)

**Decision**: `pipeline/` is a thin Python DAG runner invoking skills via CLI subprocesses (Claude Code headless or any agent harness). No LangGraph/CrewAI/AutoGen.

**TRIZ read**: TESE #6 *Increasing Trimming* — eliminate elements without losing function. The folder-of-markdown already carries the intelligence; the orchestrator only needs: dependency ordering, parallel same-phase execution, resumability, model routing, and the compliance ledger. IFR-leaning: the orchestrator that barely exists.

**Meadows read**: LP10 structure decisions are expensive to rebuild — so keep the structure *minimal and replaceable*. If a framework is ever justified, the skill contracts survive the swap because they are markdown, not framework code.

**Consequences**: `orchestrator.py` ≤ ~400 LOC target; growth beyond that is a Drifting-Goals tripwire triggering re-evaluation of this ADR.

---

## ADR-004 — Multi-platform, not KDP-only

**Status**: ✅ LOCKED (2026-08-07)

**Decision**: Export architecture is multi-target from M4:
1. **Amazon KDP** (EPUB + print) — reach.
2. **Direct sales** (Gumroad / Lemon Squeezy) — ~90% margin, no disclosure regime, and **you own the customer email**.
3. **Wide distribution** (Draft2Digital → Kobo/Apple/B&N) — deferred to M5+.

**KU exclusivity waived**: KDP Select/Kindle Unlimited requires ebook exclusivity and rewards page-read volume — an LP12 volume incentive that contradicts both this ADR and the LP3 quality goal. No KU enrollment.

**TRIZ read**: P17 *Another Dimension* — the same EPUB master serves multiple channels; the channel becomes a packaging transform, not a new production. P23 *Feedback*: direct sales create the only channel where reader information flows back to you (emails, refunds, reading behavior).

**Meadows read**: The email list is the **reinforcing loop that compounds**: direct buyers → launch list → day-one sales velocity → reviews/rank → more buyers. KDP-only leaves this loop entirely inside Amazon's boundary (system boundary mistake — Tragedy of the Commons exposure: one account ban kills 100% of distribution; multi-platform is LP8 resilience).

**Consequences**:
- formatter-kdp becomes formatter-platform: EPUB master → per-platform packaging.
- metadata-seo emits platform variants (KDP categories/keywords vs. direct-sales landing copy).
- Print remains KDP-only at M4 (IngramSpark evaluated at M5).

---

## ADR-005 — Covers: AI images, sub-decision deferred

**Status**: 🔒 LOCKED (AI images chosen); ⏳ sub-decision DEFERRED to M4 cover-director build

**Decision**: Covers use **AI-generated images**. The sub-decision — pure AI imagery (disclosed as AI-generated cover on KDP) vs. hybrid typographic composition over AI art — is deferred until the cover-director skill is built, when concrete cost/quality data exists.

**Meadows read**: This is a *decision delay done right* — the delay is matched to the rate of system change (LP9); deciding now would be parameter-guessing without feedback. The compliance log records the cover's generation method either way, so deferral creates zero compliance debt.

**Consequences**: cover-director SKILL.md must declare image provenance in `compliance_log.yaml` by construction.

---

## ADR-006 — Build vs. Clone: greenfield repo + M0 harvest phase

**Status**: ✅ LOCKED (2026-08-07)

**Decision**: Build our own repo from scratch. Do NOT clone any reference project. Run a deliberate **harvest phase** at M0: clone the five references into a throwaway folder outside our repo, extract the proven components below, delete when done. *Fork the ideas, not the codebase.*

**Why not clone (Meadows)**:
- **LP3 Goals**: every reference optimizes a different goal (cheap production, fiction assistance, great fiction drafts) — none optimizes a durable, compliant, multi-platform catalog. Cloning imports their goal silently.
- **LP10 Structure**: their structure carries their hidden archetypes (shell-script fragility = Fixes-That-Fail factory; one-shot pipelines with no gates). Import structure → import dysfunction.
- **Iceberg layer 4**: a codebase is a frozen mental model. Greenfield lets us choose our paradigm (dual-track, compliance-by-construction, folder-of-markdown).

**Why harvest (TRIZ)**:
- **P26 Copying + P2 Taking Out**: copy only the inexpensive, proven parts; extract only what is necessary. Ideality = a repo containing nothing that does not serve the goal.
- **TESE S-curve**: others already paid the infancy cost on KDP-proven export tooling and scoring contracts. Re-deriving those is waste; reinventing orchestration is not — ours (ADR-003) is deliberately thinner than all of theirs.

**Harvest map**:

| Source | Take (adapt) | Avoid (excluded day 1) |
|---|---|---|
| book-generator | Pandoc/LaTeX templates, epubcheck wrapper, cover assembly, multi-provider fallback → router.py. KDP-proven tooling, zero paradigm risk | Shell orchestration; no gates; prompt-chaining |
| Book Genesis v4 | Scoring contract format, manifest YAML schema, the four hard-won lessons | Fiction-only focus; manual execution |
| kindle-book-agency | CLAUDE.md router pattern; dependency-aware parallel-phase logic → Python DAG | One-shot output; .docx endpoint; no scoring/compliance |
| libriscribe | Per-book workspace conventions → books/<slug>/ layout | Interactive assistant paradigm; no export hardening |
| Reddit skill repos | Chapter-prompting + context-passing techniques → chapter-writer, continuity-keeper skills | Weak compliance; unknown gate discipline |

**Our differentiators (exist in none of them)**: compliance_log.yaml, dual-track manifests, Gates A–E with floor principle, multi-platform export, model-tier routing with cost ceilings.

**License rule**: check each repo license before copying any file verbatim; where unclear, reimplement the pattern — patterns are not copyrightable, files are.
