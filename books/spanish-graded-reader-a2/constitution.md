# Book Constitution Contract

## Purpose
Per-book lifecycle governance contract for humans and AI.  
This file binds how stages should interpret the book contract, what is allowed to change,
and how conflicts are reconciled when inputs disagree.

## Authority order of records
- `books/<slug>/constitution.md`: highest-order lifecycle governance; controls amendment boundaries and conflict rules.
- `books/<slug>/manifest.yaml`: stage-earned operational facts (slug/title updates, track choice, gates, model overrides, outputs metadata).
- `books/<slug>/state.json`: stage status ledger (pending/in_progress/done), gate verdicts, loopback counters.
- `books/<slug>/compliance_log.yaml`: append-only audit event stream (tool, model, timestamp, artifact hash).
- `books/<slug>/outline/**`: Stage-1 content architecture and chapter contracts after Gate A.
- `books/<slug>/tasks.md`: detailed work coordination and evidence pointers; never independent state.
- `books/<slug>/research/**`, `books/<slug>/outline/**`, `books/<slug>/bible/**`, `books/<slug>/chapters/**`: evidence for the active stage.

## Immutable-at-a-stage principles
- A stage may read and update only its declared outputs, plus reconciled contract updates.
- Once a stage has emitted gate-facing artifacts, earlier stages do not mutate its operational facts.
- `state.json` is mutable only for stage status and gate evidence; `compliance_log.yaml` is immutable except by lawful append.

## Course-correction triggers
- Missing gate prerequisites, unresolved facts, or broken stage contracts.
- Evidence mismatch between `state.json`, `manifest.yaml`, and `compliance_log.yaml`.
- Any cross-stage dependency break reported by a later judge/editor stage.

## Amendment protocol
1. Only owner-approved amendments may change this contract.
2. Record a single-source reason, date, and scope in the amendment table below.
3. Re-run only affected stages (`scope`) after amendment.
4. If amendment conflicts with current `manifest.yaml` or `state.json`, pause all progression and reconcile.

## Conflict rule
If `constitution.md`, `manifest.yaml`, `state.json`, or `compliance_log.yaml` disagree, progression stops and human reconciliation is required before any new stage execution.

## Append-only amendment log
| date_utc | owner | section | rationale | affected-stage reruns |
|---|---|---|---|---|
| <YYYY-MM-DD> | <human> | <goal / persona / voice / platform constraint> | <decision + evidence link> | <stage numbers, comma-separated> |
| 2026-08-13 | Mouhamad | lexical gate (Gate L) | Occurrence coverage had been made non-fatal in-session via `--max-new-types` after story 01 missed 0.95 — a Drifting Goals violation of CLAUDE.md rule 9. External review (codex gpt-5.6-sol) refused to ratify it and found the real defect: the checker never consumed the cumulative vocabulary ledger. Correction: coverage measured against baseline + names + earlier-story glossaries; L1 (coverage) and L2 (new types) both independently fatal; thresholds RESTORED to the original 0.95/0.93 — no threshold was lowered. Recorded in `.agents/rules/quality-gates.md` and pinned by `tests/test_graded_reader_gate.py`. | 2 |
| 2026-08-13 | Mouhamad | CEFR level of the volume: A1 → **A2** | The book was titled A1 on an invented grammar ladder that nothing ever enforced. Measured against the Instituto Cervantes PCIC A1-A2 inventory (`_planning/pcic-ladder-table.md`, source read by codex `gpt-5.6-sol`), A2 grammar appears in **all ten stories** — irregular present (`dice`/`tiene`/`quiere`) at 19-39 tokens per story, including 21 in story 01, plus habitual present, 3rd-person clitics and the preterite. There is no A1 band anywhere in the manuscript, so "A1-A2" was rejected as a second mislabel rather than a correction. Strict-A1 conformance was rejected as a full re-authoring that would cut the 1998 arc and risk the child-primer register our own comp research names as the shelf's central failure. Prose is preserved unchanged; the label moves to match the measurement. Owner decision, evidence `_planning/pcic-ruling.md`. | 1, 6 |
| 2026-08-13 | Mouhamad | word budgets, stories 01-02 | Story 01 500→550, story 02 550→650. Story 01 was rewritten to pass restored coverage (0.928→0.955) and lands at 564 words; story 02 is 653 after a panel-mandated ending fix. Broad 550→900 progression retained; the unvalidated 500→550→650 micro-staircase dropped. | 1, 2 |

## New book placeholders
- book slug: `<slug>`
- owner: `<name or alias>`
- initial date: `<YYYY-MM-DD>`
- primary audience: `<audience statement>`
- authority source: `<human domain knowledge or external evidence>`
- scope boundary: `<what this book includes and excludes>`
