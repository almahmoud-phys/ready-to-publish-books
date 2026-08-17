# Per-book task ledger contract

`books/<slug>/tasks.md` is the detailed execution checklist shared by the human and every
pipeline agent. It answers **what must happen next and what evidence proves it happened**.

It is not a second state machine:

- `state.json` alone owns stage status, verdicts, gate results, counters, and publication state.
- `constitution.md` owns purpose, principles, exclusions, and course-correction boundaries.
- `outline/outline.md` and `outline/chapter_NN.md` own the book's content architecture.
- `tasks.md` owns actionable work, dependencies, handoffs, blockers, and completion evidence.

## Required agent behavior

At the beginning of every invocation:

1. Read the task-ledger header and the active stage section only.
2. Confirm that the requested work is represented by a task ID.
3. Before execution, expand that task with owner, dependencies, expected outputs, acceptance
   criteria, verification commands or review method, and known blockers.
4. If no suitable task exists, add one under the correct stage before doing the work.
5. Do not start a task whose dependencies or governing gate are unsatisfied.

At the end of every invocation:

1. Check off only work whose acceptance criteria have been met.
2. Add concrete evidence: repository paths, commands and outcomes, source URLs, gate verdicts,
   or human approval references.
3. Record remaining work as child tasks; never hide partial completion behind a checked parent.
4. Update `Last reviewed`, `Current focus`, and `Next handoff`.
5. Reconcile any stage transition with `state.json`. Editing a checkbox never advances state.

## Task detail standard

Every executable task must eventually contain:

- **Owner:** Human, AI, named skill, or named reviewer.
- **Why:** The reader, quality, compliance, or gate risk it controls.
- **Depends on:** Task IDs, artifacts, or approvals required first.
- **Generate / update:** Exact artifact paths or external records.
- **Inputs:** Files, sources, data, or decisions to use.
- **Procedure:** Ordered, reproducible work steps.
- **Acceptance criteria:** Observable conditions, not “looks good.”
- **Verification / evidence:** Commands, reports, URLs, or approval records.
- **Blockers / escalation:** Current blocker and the condition or authority needed to remove it.
- **Status:** `[ ]`, `[~]`, `[x]`, or `[!]` as defined in the template.

The detail may live immediately below the checkbox or inside an expandable `<details>` block.
Never delete completed evidence to make the file shorter. Move fully closed stage detail to the
archive section while retaining IDs and evidence links.

## Per-chapter rule

After Gate 1 approval, instantiate the repeatable chapter checklist once per approved chapter.
Use stable IDs such as `CH-03-010`. A chapter is not complete merely because prose exists: its
contract, assets, executable examples, citations, summary, continuity pass, and task evidence
must all be complete.

## Prohibited uses

- Do not duplicate stage verdicts or scores as independently editable truth.
- Do not put speculative chapter content in `tasks.md`; put it in the outline contracts.
- Do not use vague tasks such as “research more,” “improve chapter,” or “finish book.”
- Do not mark a parent complete while any required child remains open.
- Do not rewrite history after a failure; append the correction and link the replacement evidence.
