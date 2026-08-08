# Quality Gates (Rule file — change control enforced)

> ⚠️ **Drifting Goals tripwire**: thresholds in this file change ONLY via deliberate, committed edits (PR-style). Never adjust a threshold mid-session to make a book pass. If pressure exists to lower the floor, that pressure IS the archetype — escalate to the human instead.

## The five gates

| Gate | Position | Criterion | On failure |
|---|---|---|---|
| **A** | Post-outline | Every chapter has: `promise`, word budget, dependency links (what it builds on / sets up). Plus HITL approval. | Return to `outline-architect` with the specific gaps |
| **B** | Post-audit | Zero open **critical** structural findings in `audits/structural.md` | Return to `chapter-writer` (targeted chapters only) with citations |
| **C** | Scoring | **Floor principle**: every dimension ≥ **7/10** (default). Book score = min(dimensions). All scores cite manuscript. | Route to exact failing stage per loop-back table below |
| **D** | Pre-export | Edit log applied 100%; every fact-check flag resolved (verified / rewritten / cut) | Return to `proofreader`/`fact-checker` |
| **E** | Pre-publish | epubcheck exit 0; print PDF renders; `compliance_log.yaml` complete; originality check run; disclosure answers generated; `books/<slug>/frontmatter.md` exists for `manifest.track == generated` and includes KDP disclosure note | Return to failing stage; never publish with E open |

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
