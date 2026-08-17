# Quality Gates (Rule file — change control enforced)

> ⚠️ **Drifting Goals tripwire**: thresholds in this file change ONLY via deliberate, committed edits (PR-style). Never adjust a threshold mid-session to make a book pass. If pressure exists to lower the floor, that pressure IS the archetype — escalate to the human instead.

## The five gates

| Gate | Position | Criterion | On failure |
|---|---|---|---|
| **A** | Post-outline | Every chapter has: `promise`, word budget, dependency links (what it builds on / sets up). Plus HITL approval. | Return to `outline-architect` with the specific gaps |
| **B** | Post-audit | Zero open **critical** structural findings in `audits/structural.md` | Return to `chapter-writer` (targeted chapters only) with citations |
| **C** | Scoring | **Floor principle**: every dimension ≥ **7/10** (default). Book score = min(dimensions). All scores cite manuscript. | Route to exact failing stage per loop-back table below |
| **D** | Pre-export | Edit log applied 100%; every fact-check flag resolved (verified / rewritten / cut) | Return to `proofreader`/`fact-checker` |
| **E** | Pre-publish | Production toolchain preflight passed; identity metadata frozen and equal across all surfaces; golden print/EPUB/cover samples accepted; epubcheck exit 0; every print page renders at the locked trim; one-page cover matches the locked wrap; release preflight and manifest PASS; `compliance_log.yaml`, rights/provenance, and originality checks complete; accurate private KDP disclosure answers generated from the log; KDP Previewer inspected; physical proof PASS or explicit owner risk waiver recorded. No reader-facing AI disclosure note is required | Return to the exact failing stage; invalidate downstream artifacts; never publish with E open |

## Gate L — lexical load (graded readers / controlled-vocabulary books)

Added 2026-08-13 by owner reconciliation after a Drifting Goals incident.

**Two metrics, both independently fatal. Neither may disable the other.**

| Metric | What it bounds | Threshold | Unit |
|---|---|---|---|
| **L1 — occurrence coverage** | *Reading friction*: how often the reader stalls | ≥ **0.95**; a book may declare a documented late-stage relaxation to **0.93** in its outline (this book: stories 08–10, where the preterite arrives) | tokens |
| **L2 — new types** | *Learning load*: how much must be taught | ≤ **25** per story | normalized surface types |
| **L3 — locale** | Assembled-not-written tells | **zero** violations | marker forms |

**The known set for L1 and L2 is cumulative**: baseline frequency list + declared proper
names + every type genuinely closed in *earlier* stories, read from the book's
`bible/vocabulary-ledger.md`. A word taught in story 01 is known in story 02. Measuring
every story against the baseline alone contradicts the cumulative-ledger pedagogy and
was a real defect, not a conservative choice.

**Why both.** They measure different risks and must be allowed to fight. One unknown
word repeated three hundred times is a single type: it sails through L2 and destroys
the reading experience. Conversely a text can stall a reader rarely while still
introducing eighty distinct words to memorise. `tests/test_graded_reader_gate.py`
asserts both failure modes; deleting or weakening those tests is itself a gate change.

**Unit honesty.** L2 counts *normalized surface types* — casefolded, accent-stripped,
no lemmatizer. Do not call them words or lexemes in a contract. `casa`/`casas` count
twice until a lemmatizer exists.

**Provenance of the numbers.** 0.95 traces to the lexical-coverage literature on
reading comprehension (Hu & Nation 2000; Schmitt et al. 2011 find a broadly linear
relationship rather than a sharp threshold, and argue 98% for unassisted academic
reading; Kremmel et al. 2023 replicate the linearity and question the canonical 98%).
It is a defensible internal minimum, **not a validated Spanish-A1 constant**.
**The 25-type budget has no research behind it at all** — it is a project convention.
Neither number may be cited as evidence-based in reader-facing copy.

**On failure:** rewrite the story. A failing check is a rewrite, never a threshold
change — and never a flag that makes the inconvenient half of the contract non-fatal.

### The incident this gate exists to prevent (2026-08-13)

Story 01 measured 0.912 coverage against a 0.95 contract. Instead of rewriting it,
`--max-new-types` was made to **suppress the coverage failure**, and the justification
written down was that occurrence-coverage "punishes the teaching method". The
observation was half true; the response was a threshold change after a failure, made
in-session, with no edit to this file and no compliance event — the exact archetype
the tripwire at the top of this file names.

External review (codex `gpt-5.6-sol`) refused to ratify it and found the real bug
underneath: the checker never consumed the vocabulary ledger. Correcting that raised
nine of ten stories above the original thresholds with **no gate change required**.
Only story 01 still failed, honestly.

The lesson is not "don't fix bad metrics". It is: **when a metric is wrong, fix the
metric in the rule file and re-run — never make it non-fatal from the command line.**
If a proposed change would make a currently-failing artifact pass, that is the moment
to get an outside opinion, not the moment to ship the change.

## Loop-back routing (TRIZ P23 — feedback to the right place)

| Failing dimension / finding | Route back to |
|---|---|
| Accuracy, Usefulness, factual claims | `fact-checker` → `chapter-writer` (targeted) |
| Structure, Coherence, Pacing | `outline-architect` (if systemic) or `chapter-writer` (if local) |
| Prose, Voice | `chapter-writer` with style-sheet citation |
| Originality | `niche-research` (reposition) or `chapter-writer` (rewrite flagged passages) |
| Market, Opening | `outline-architect` (and/or `niche-research` for Market; and/or `chapter-writer` for Opening) |

Loop-backs must never route work to a forward stage.

**Hard bound**: max **3 loop-back cycles** per dimension. After the third failure, stop and hand to the human with the full evidence trail (fable-loop discipline).

## Verification block (required at every gate)

```
✅ Gate [A–E] result:
- Criterion: [restated]
- Evidence: [file + lines]
- Verdict: [PASS/FAIL]
- If FAIL → routed to: [stage] with [citations]
```
