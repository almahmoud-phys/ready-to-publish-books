# Decisions Log — Ready To Publish Books

*Architecture Decision Records. Each entry: decision, contradiction analysis (TRIZ), leverage check (Meadows), rationale, consequences. Status: LOCKED unless noted. Full ADR-001…009 text: see git history (commit d0b21cc) or the Notion Decisions page. Newest entries below.*

---

## ADR-010 — Work environment: self-reconstituting research workspace + book factory + catalog registry

**Status**: ✅ LOCKED (2026-08-08)

**Context**: The repo is for ALL books, not one. We need: where niche tools live, what scripts run them, and how each book is born as a uniform subproject — portable across machines.

**Decision**:

1. **Research workspace lives at `{repo}/.kdp-research/`** — INSIDE the repo root, **git-ignored**. Bootstrapped by `tooling/scripts/research-init.sh` (idempotent): clones/updates KDP Scout, creates an isolated venv, installs the tool + trendspyg, inits config, writes the ledger header. Rationale (founder caveat, accepted): an external `~/kdp-research/` dies when changing machines; the in-repo workspace + init script makes the repo a **self-reconstituting system** — clone on any PC, run one script, the whole research layer rebuilds itself (Meadows LP4 self-organization; TRIZ P25 Self-Service: the system carries its own environment). Only the script + structure contract are committed; the DB/exports/venv are data, never committed. `RTPB_RESEARCH_DIR` remains as an override for exotic setups.

2. **Thin wrapper scripts own the interface** (`tooling/scripts/`): `niche_mine.sh` (autocomplete → ledger, rate-limited), `niche_snapshot.sh` (ASIN snapshot, low-volume tier), `niche_report.sh` (ledger → per-book projection into `books/<slug>/research/`). **Skills never call KDP Scout directly** — they call wrappers (TRIZ P24 Intermediary: swap tools without touching skills).

3. **Every book is born by `tooling/scripts/new-book.sh <slug> "<title>"`** — validates kebab-case + uniqueness, copies `books/_template/`, fills manifest/state/compliance_log, creates the 10 stage dirs (research, outline, bible, chapters, summaries, audits, scores, edits, exports, assets), registers the book in **`books/registry.yaml`**, prints the stage-0 checklist.

4. **`books/registry.yaml` = the catalog ledger** — one entry per book: slug, title, track, stage, verdict (GO/PIVOT/KILL), created, published, book_score, cost_usd. The single glance-view of the whole catalog (LP6 at catalog level — without it, multi-book state lives in the founder's head).

**TRIZ read**: P1 Segmentation (each book an independent subproject) + P6 Universality (one template serves all) + P10 Preliminary Action (the factory builds compliance structure before any content exists) + P24 Intermediary (wrappers decouple skills from tools) + P25 Self-Service (the repo rebuilds its own tooling layer).

**Meadows read**: registry.yaml closes the catalog-level information gap; the git-ignored workspace keeps the market-knowledge stock (ledger) inside the system's boundary but outside its versioned surface — portable because structure is code, data is regenerate-able.

**Uniform book workflow**: `research-init.sh` (once per machine) → `new-book.sh` (once per book) → stage 0 niche-research (wrappers → ledger → niche.md) → HITL gate → stages 1–7 → publish → retrospective → registry updated.

---

## ADR-011 — manifest.yaml is the single source of truth; owning stages write back

**Status**: 🔒 LOCKED (2026-08-08)

**Context**: `manifest.yaml` is the only artifact loaded at EVERY stage (managed context rule 1), yet several of its fields (`persona`, `subtitle`) are *outputs* of stages that never wrote them back. Every stage ≥1 read a literal placeholder forever, and a hand-written guess in those slots is indistinguishable downstream from a researched value.

**Decision**: The manifest is the distilled single source of truth. The stage that owns a field writes it back on completion: niche-research → `persona`, metadata-seo → `subtitle`, outline-architect → `track` (already did). The stage artifact (`research/niche.md`, `exports/metadata.json`) remains the evidence; the manifest field is the distilled value. Fields carry ownership tags — `[HUMAN]` / `[FACTORY]` / `[STAGE n]` / `[DEFAULT]` — so neither human nor agent fills what it does not own.

**Alternative rejected**: consumers read `research/*` directly. Rejected because every later stage would need extra reads, breaking the declared per-skill context budgets — the differentiator of this pipeline.

**Meadows read**: the manifest is the highest-traffic information channel in the system (LP6). Fabricated information there is worse than missing information: missing announces itself, invented does not. Ownership tags make provenance travel with the value.

**TRIZ read**: physical contradiction — the manifest must be complete (stages load it) and empty (facts not yet known). Resolved by **Separation in Time**, the same principle the pipeline already uses for draft-before-judgment: fields fill progressively, each at the stage that earns it, never as a form completed at birth. P10 Preliminary Action is scoped to structure, never to content.

**Consequences**: each owning SKILL.md declares its write-back explicitly. Enforcement is by contract in M1; the M2 orchestrator can assert it.

---

## ADR-012 — Gate C loop-backs never route forward

**Status**: 🔒 LOCKED (2026-08-08)

**Context**: the Gate C loop-back table routed the Market and Opening dimensions to `metadata-seo` — stage 6, forward of the stage-4 scorer and past stage 5 — while the plan states a failed gate "routes to the exact failing stage".

**Decision**: loop-backs route backward only. Opening → `outline-architect` (stage 1) and/or `chapter-writer` (stage 2). Market → `niche-research` (stage 0, repositioning) and/or `outline-architect`. `metadata-seo` is removed from that row, and the rule states explicitly that a loop-back never routes forward.

**Rationale**: metadata-seo is stage-6 packaging — it writes keywords and a blurb. It cannot fix a book whose market fit or opening chapter is weak. Routing a quality failure to the packaging stage would let a book pass Gate C by relabelling itself.

**Meadows read**: this closes a *Drifting Goals* mechanism. A forward-route lets the system satisfy the floor by changing the description rather than the book — the goal quietly degrades from "genuinely useful book" to "book that scores".

**Consequences**: a Market failure can send a book back to stage 0, where the honest outcome may be PIVOT or KILL. That is the intended behavior, not a defect.

---

## ADR-013 — A wrapper is unverified until it has run against the real tool

**Status**: 🔒 LOCKED (2026-08-08)

**Context**: stage 0 was run for the first time. Every KDP Scout wrapper in `tooling/scripts/` had been written from a plausible reading of the tool and had never been executed against it. `niche_mine.sh` passed `--format json` (no such option) and `-m com` (the marketplace enum is `us|de|uk|fr|es|it|ca|au`); `niche_snapshot.sh` called `kdp-scout asin`, a command that does not exist. Both were syntactically valid, both were referenced by the skill contracts, and both would have failed the moment a stage depended on them.

**Decision**: a wrapper script counts as delivered only after it has been run end to end against the real tool and its output inspected. Documented CLI shapes in skills and ADRs are transcribed from `--help`, never inferred. Where a tool's output cannot be trusted to be non-empty, the wrapper exits non-zero rather than passing an empty result forward — and where an empty result is genuinely ambiguous, the wrapper names the control test that disambiguates it (`niche_mine.sh` points at a known-good seed).

**Rationale**: the M2 orchestrator will invoke these scripts unattended. A wrapper that fails loudly costs one run; a wrapper that returns nothing quietly poisons a verdict.

**Meadows read**: LP6 again, one layer down. The wrappers *are* the information channel between the market and every downstream stage. An unexercised channel is not a channel — it is an assumption with a filename.

**TRIZ read**: P23 Feedback. The measurement instrument must itself be measured before its readings are trusted; the control seed is the calibration standard that separates "no demand" from "no data".

**Consequences**: `niche_score.sh` was added (stage-0 Step 2 needs `niche-score`, and skills call wrappers, not tools — ADR-009 P24). Amazon began refusing search probes during the first stage-0 run; backing off is the correct response under ADR-008, and any Step-2 data gap is recorded in `niche.md` rather than filled in by estimate.
