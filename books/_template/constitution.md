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

## New book placeholders
- book slug: `<slug>`
- owner: `<name or alias>`
- initial date: `<YYYY-MM-DD>`
- primary audience: `<audience statement>`
- authority source: `<human domain knowledge or external evidence>`
- scope boundary: `<what this book includes and excludes>`
