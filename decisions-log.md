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

---

## ADR-014 — `.agents/` is the source of truth; `.claude/` is a symlinked harness view

**Status**: 🔒 LOCKED (2026-08-08)

**Context**: the 13 skills lived at `.agent/skills/` and were invisible to Claude Code, which auto-discovers only `.claude/skills/<name>/SKILL.md`. Every session therefore loaded them by hand through CLAUDE.md routing — the skills existed but the harness could not see them, which is precisely the M0 exit criterion ("skills load in Claude Code") going unmet while looking met.

**Decision**: the directory is `.agents/` (plural, harness-neutral) and remains the single source of truth for skills, rules, workflows and memories. `.claude/skills` is a committed **relative symlink** to `../.agents/skills`. Any future harness gets its own symlinked view; no skill file is ever duplicated. `.gitignore` commits the symlink and ignores the rest of `.claude/` as per-machine session state.

**TRIZ read**: P24 Intermediary — the symlink is a temporary carrier between a harness's fixed expectation and the repo's neutral layout, and it costs nothing to add or remove. P6 Universality: one skill file serves every runtime. The alternative (copy skills into `.claude/`) creates two sources of truth that silently diverge — a physical contradiction resolved by *separation in representation*, not by choosing a side.

**Meadows read**: LP6. A skill the harness cannot see is not a channel, and the failure is silent: the pipeline still "has" 13 skills. Making discovery structural rather than documentary closes the gap.

**Consequence and guard**: auto-discovery makes every stage skill invokable at any time, which is a *Drifting Goals* risk — invokable is not the same as due. CLAUDE.md states explicitly that discovery does not relax the DAG; stage order and the HITL gates decide what runs.

---

## ADR-015 — Stage 0 is a bounded PIVOT explorer, not an autonomous niche hunter

**Status**: 🔒 LOCKED (2026-08-08)

**Context**: the obvious next step after the first stage-0 run was to let the agent loop: set a goal, run the scripts, and on KILL or PIVOT generate new seeds and re-run until something earns a GO. The mechanical half of that is real work worth automating. The other half quietly replaces the system's goal.

**Decision**: stage 0 runs unattended **inside a human-locked charter** (`books/<slug>/research/charter.md`: reader problem, useful outcome, authority envelope + exclusions, allowed adjacency, `max_pivot_cycles`). Within it:

1. **PIVOT auto-continues; KILL stops; GO stops.** A pivot must preserve `reader_problem` and `authority_envelope` and cite evidence for its new angle. Failing either, it is not a pivot — it is a different book, and that is the human's call.
2. **Asymmetric confirmation.** The human may veto a computed GO. Nobody — human or agent — may promote a PIVOT or KILL to GO without new evidence.
3. **The provenance rule.** The model may classify, dedupe and rank phrases; it may never originate a market-facing seed. Every candidate traces to the charter, the harvest, a comp title, or sourced review language, recorded in `candidates.csv`.
4. **The verdict is computed, not narrated.** `tooling/scripts/niche_verdict.py` reads `evidence.yaml`, cross-checks each claim against the artifact backing it, and refuses GO on any `UNKNOWN` or failed check. `INCOMPLETE` is the absence of a verdict, never rounded up or down.
5. **Circuit breaker.** The wrappers detect refusal and exit 3; the first refusal ends all Amazon activity for the session. No retry, no backoff.
6. **Loop state lives in `state.json`** (`pivot_cycles`, `seed_lineage`, `collector_health`), not in context.

**Rejected: auto-continue until GO.** Its termination condition is "found something", and it will always find something. The stated goal is a durable catalog of genuinely useful books, never book count — a loop that cannot stop silently substitutes "produce a passing market" for it. **Drifting Goals**, and it inverts the gate's purpose: stage 0 exists to kill cheaply, and a loop that cannot terminate never kills. Generating another seed instead of collecting the missing comp and trademark evidence is also **Shifting the Burden** — the cheap symptomatic move crowding out the fundamental one.

**Meadows read**: the charter is an LP3 intervention — it fixes the goal in a file so the loop optimizes inside it rather than around it. The circuit breaker is LP8: a negative feedback loop protecting the publishing account, the stock the whole catalog depends on. Retry-with-backoff would have been **Fixes That Fail** — more probes, stronger blocking, less evidence, more probing.

**TRIZ read**: Separation by Condition resolves the automation-versus-reliability contradiction. Automate the safe, repetitive, verifiable measurement; keep the human exactly where truth lives outside the system — lived experience (authority fit), live-page reality (comps), and legal judgment (trademark). P23 Feedback: `collector_health` calibrates the instrument before its readings are trusted, so a CAPTCHA can never be recorded as "no demand".

**Two tool findings that shaped this** (verified in the vendored source, not assumed):
- `kdp-scout` returns `None` for HTTP error, CAPTCHA and zero-results alike (`niche_scorer.py:63-84`) and exits 0 either way (`cli.py:2178`). Refusal is undetectable from exit status — hence exit 3 in the wrappers.
- `kdp-scout score` scores unmeasured components as `0.0` rather than unknown (`keyword_engine.py:626`), and `discover` defaults to 200 reverse-ASIN probes (`cli.py:1427`). Neither is wrapped: the first makes "unmeasured" look like "measured badly", the second is an account-risk multiplier.

**Consequences**: a GO now requires evidence that cannot all be gathered in one unattended pass — comp BSRs, prices, review dates, negative-review language and a trademark screen all need a human in the loop. That is the intended cost. The loop's job is to reach a defensible PIVOT cheaply and often; earning a GO is deliberately slower than earning a KILL.
