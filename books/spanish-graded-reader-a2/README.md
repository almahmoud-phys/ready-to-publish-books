# Spanish A2 Graded Reader — Volume 1

**Orientation for whoever opens this folder next.** Read this first, then the record you need.

> ⚠️ **This file is a ROUTER, not a record.** It owns no facts. Per `CLAUDE.md` rule 5,
> authority lives in `manifest.yaml` (operational facts), `state.json` (stage status),
> `compliance_log.yaml` (append-only evidence), `constitution.md` (governance),
> `outline/` (content architecture) and `tasks.md` (coordination). **If this file ever
> disagrees with one of those, the other one wins and this file is the bug.** Do not
> resolve a conflict by editing this file to match — that is how a sixth source of truth
> gets born.

---

## What the book is

Ten linked Spanish stories, ~7,000 Spanish words, one continuous narrative. Ana runs a night
kiosk in Puerto Lento, receives a letter addressed to a stranger, and there is a light on the
water. Story 10 is the payoff — **this is not an anthology and cannot be split.**

Reader: an adult English speaker who finished a beginner app, recognises words and conjugation
tables, but cannot read continuous Spanish without translating every sentence. Not children,
not a classroom, not exam prep. The full persona is in `manifest.yaml`.

Track is `generated` (ADR-002), set at birth deliberately rather than by default — the charter
already fixes this as a machine-verified book with no lived authority.

## Where things stand

Read `state.json` for the authoritative status. As of the last update:

| Stage | Status |
|---|---|
| 0 niche-research | **done** — verdict GO, computed by `niche_verdict.py`, not asserted |
| 1 outline | **done** — Gate A passed, two codex review rounds |
| 2 chapters | **done** — all ten drafts, rolling summaries, continuity report, and targeted post-repair machine gates exist |
| 3 adversarial-editor | **done** — Gate B passed after an independent Claude/Anthropic re-audit |
| 4 scorer | **done** — Gate C passed; reconciled book score 8/10 |
| 5 proofreader + fact-checker | **done** — Gate D passed; edit and fact reports complete |
| 6 metadata, cover, and exports | **in progress** — human metadata/cover gates open; `PIPE-001` blocks compilation |
| 7 publication readiness | pending |

**Gates currently green:** vocabulary/locale 10/10, grammar-ladder 10/10, 39 repo tests.
Reproduce both with the command in `bible/vocabulary-ledger.md` and the usage block in
`tooling/scripts/spanish_grammar_check.py`. Do not take this table's word for it — rerun them.

## The four decisions that shape everything

Full reasoning lives in `constitution.md`'s amendment log and `state.json`. Summarised so a
newcomer does not re-litigate them:

**1. The volume is A2, not A1** *(owner, 2026-08-13)*. It was titled A1 on a grammar ladder the
agent invented and nothing ever enforced. Measured against the Instituto Cervantes PCIC A1–A2
inventory, A2 grammar appears in **all ten stories** — irregular present at 19–39 tokens each,
including 21 in story 01. There is no A1 band anywhere in the manuscript, so "A1–A2" was
rejected as a *second* mislabel. Strict-A1 conformance was rejected as full re-authoring: it
would cut the 1998 backstory the mystery runs on, and risk the child-primer register our own
competitor research names as this shelf's central failure. **The label moved to match the
measurement; no prose was cut to fit a label.**

**2. Instituto Cervantes decides levels, we do not invent them** *(owner)*.
`_planning/pcic-ladder-table.md` is the source of truth for what is A1 and what is A2. Where
PCIC is silent or self-contradictory, that is recorded as a **house decision**, never resolved
by guessing — see `cuándo` and `mientras` in any `outline/chapter_NN.md`.

**3. Thresholds change only in the rule file, never in a session** *(`CLAUDE.md` rule 9)*. This
book already produced one Drifting Goals incident: after story 01 missed 0.95 coverage,
`--max-new-types` was made to *suppress* the coverage failure. External review refused to ratify
it and found the real bug underneath — the checker never read the cumulative ledger. Thresholds
were restored to the original 0.95/0.93 and **none was ever lowered**. The full write-up is in
`.agents/rules/quality-gates.md`. If you feel pressure to move a number, that pressure *is* the
archetype.

**4. No human beta readers and no native-speaker reviewer. Ever.** Standing owner constraint on
every book this operation publishes. Everything is machine checks plus blinded LLM panels with
preregistered thresholds. Plan around it; do not propose it.

## What is measured, and what only looks measured

This matters more than anything else here, because the book's credibility rests on not
overclaiming.

**Genuinely machine-verified:**
- Lexical coverage and new-type load, cumulative across stories — `tooling/scripts/graded_reader_check.py`
- Latin-American locale consistency — same script
- Grammar-ladder conformance — `tooling/scripts/spanish_grammar_check.py`

**NOT verified, and must not be described as if it were:**
- **Comprehension.** Nobody has read this book. Coverage is not comprehension.
- **Temporal correctness.** No form-based checker can see `Antes es de él` (present doing a past
  tense's job — a real bug that shipped here) or `mañana viene` (future-value present). Habitual
  present is equally invisible. `tests/test_spanish_grammar_gate.py` *asserts* the checker stays
  blind to these, so the stated ceiling cannot quietly drift into an overclaim.
- **CEFR certification.** The wordlist is a frequency proxy, not a CEFR list; the grammar checker
  is lint. The 0.95 threshold is a defensible internal minimum from the lexical-coverage
  literature, **not** a validated Spanish-level constant, and the 25-type budget has no research
  behind it at all — it is a project convention. None of this may appear in reader-facing copy.

## Traps this book has already fallen into

Recorded so the next agent does not repeat them:

- **A contract nothing checks is not a contract.** Both gate failures here were this shape: the
  vocabulary gate declared a threshold it silently stopped enforcing; the grammar ladder declared
  a sequence nothing ever enforced. Declaring a rule and measuring it are different acts.
- **Inventing obstacles.** A previous plan grew to 40 tasks, most manufactured — a marketing-claim
  gate, a dependency ADR, manuscript hashing, benchmark corpora. The owner's words: *"you are
  inventing traps and you put us all in the traps."* `.local-tasks/grammar-gate.md` keeps a
  **"do not re-add"** list. Read it before proposing infrastructure.
- **Metric gaming.** Both authoring models, given a numeric ceiling, optimised for the number:
  one padded by repetition to stay inside a glossary budget, another renamed the town to avoid
  new nouns. A ceiling stated as a number will be read as a target. See
  `.agents/rules/model-routing.md`.
- **Judge-scale drift.** Panel scores moved by up to ±1.0 between rounds on *unchanged* text. Any
  panel here must carry an unchanged calibration anchor, or an improvement claim is unfalsifiable.
- **False positives are bugs too.** The grammar checker's first run produced two, both mine: a
  verb filed under the wrong conjugation, and interrogatives detected by "does this file contain
  a question mark" instead of by the accent Spanish actually uses. A gate that cries wolf gets
  switched off.

## Reading order for a cold start

1. This file
2. `constitution.md` — governance and the amendment log (every decision, dated, with reasons)
3. `manifest.yaml` — title, persona, track, budgets
4. `state.json` — real stage status and the open-issue trail in `2_chapters.open_contract_drift`
5. `outline/outline.md` — the spine; then `outline/chapter_NN.md` for the chapter you touch
6. `research/charter.md` — what this book may and may not claim
7. `.agents/rules/quality-gates.md` — Gate L and the incident behind it

Then, only for the stage you are running: that skill's `SKILL.md` in `.agents/skills/`.

## Before you change anything

- Load `constitution.md` at every stage; it is amend-only with owner approval.
- Expand your stage's section in `tasks.md` **before** executing, and record acceptance evidence
  before ticking anything. A checkbox never advances `state.json`.
- Append to `compliance_log.yaml` for every generation event. It is append-only: corrections are
  new entries, never edits.
- Re-run **both** gates on any story whose Spanish you touch, and resync
  `bible/vocabulary-ledger.md` — the checker *reads* that file, so a stale glossary silently
  changes what counts as known.
- If `manifest.yaml`, `state.json`, `compliance_log.yaml` and `constitution.md` disagree,
  **stop** and escalate. Rule 8, no exceptions.

## Deliberate inconsistencies — do not "fix" these

- The **slug** is `spanish-graded-reader-a2`, renamed from `-a1` by owner instruction along with
  the title. Two classes of file kept the old path on purpose: the verbatim codex reports in
  `_planning/` (editing a quotation to look current falsifies it) and this book's
  `compliance_log.yaml`, including its header comment, because it is append-only.
- `audits/`, earlier `compliance_log.yaml` entries and the dated `research/trademark.md` screening
  still say **A1**. That is what was true when they were written. The trademark file records that
  the retitle was *not* re-screened, rather than pretending it was.
- `chapters/sample-story-pipeline-proof.md` is **not part of the book**. It is a stage-0 pipeline
  proof. Exclude it from gates and exports. **Nothing enforces this** — no script filters it, so a
  glob like `--text 'chapters/*.md'` will happily pick it up. Address the story files explicitly,
  or fix the gap properly rather than trusting this bullet.

## Known-open, carried forward

- English parallel text is contracted, but no current skill explicitly owns generation and
  verification. `tasks.md` records this as `PIPE-001`; do not assign it ad hoc to `chapter-writer`
  or penalize completed Stage 4 scoring for Stage-6 frontmatter.
- Stage 6 is active: evidence-backed metadata and rendered cover directions await the human
  micro-gates and final-mark screening. `PIPE-001` is recorded in `state.json` and must prevent
  translation generation or bilingual compilation until ownership and verification are explicit.
- The `Preguntas` block sits inside what will be the Amazon sample; that is a stage-6 formatter
  decision, not settled here.
- Pandoc metadata hardcodes `lang: en` while the interior is bilingual. The Spanish spans need
  their own language tagging before export, or screen readers mispronounce the whole book. See
  `docs/discovery-log.md`.
