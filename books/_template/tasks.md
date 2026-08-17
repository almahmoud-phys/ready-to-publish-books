# Tasks — <book title>

> Detailed human/AI execution ledger. This file coordinates work; it does not replace
> `state.json`, `constitution.md`, or `outline/`. Read `.agents/rules/task-ledger.md` before editing.

## Control panel

- **Book:** `<slug>`
- **Lifecycle status:** Stage 0 — not started
- **Current focus:** Complete the human-owned Stage-0 charter and evidence collection.
- **Next handoff:** `niche-research` after prerequisites are complete.
- **Last reviewed:** `<iso8601>`
- **Ledger owner:** Human owner; pipeline agents maintain their task evidence.

### Status legend

- `[ ]` not started
- `[~]` in progress — child tasks and current evidence must show what remains
- `[x]` complete — acceptance criteria met and evidence linked
- `[!]` blocked — blocker, owner, and unblock condition recorded

### Required expansion block

Copy this beneath every task before execution:

```md
<details>
<summary>Execution contract</summary>

- **Owner:**
- **Why:**
- **Depends on:**
- **Generate / update:**
- **Inputs:**
- **Procedure:**
  1.
- **Acceptance criteria:**
  - [ ]
- **Verification / evidence:**
- **Blockers / escalation:** None.
- **Completion note:**

</details>
```

## Stage 0 — Niche validation

### Charter and candidate identity

- [ ] `S0-010` Confirm the human-owned reader problem, useful outcome, authority envelope,
  exclusions, allowed adjacency, and maximum pivot cycles in `research/charter.md`.
- [ ] `S0-020` Confirm `manifest.yaml` has a provenance-backed `niche_seed`, correct language,
  provisional title, platform scope, and disclosure track; leave stage-owned fields unresolved.
- [ ] `S0-030` Record every candidate and its provenance in `research/candidates.csv`; reject any
  model-originated market seed that lacks allowed provenance.

### Demand and competition evidence

- [ ] `S0-100` Collect Google Trends comparisons with region, timeframe, query type, retrieval
  date, raw export or screenshot, and interpretation limits.
- [ ] `S0-110` Collect marketplace autocomplete phrases without inventing or normalizing away the
  observed buyer language.
- [ ] `S0-120` Verify the live top-ten shelf and record title, author, publisher, format, price,
  rank/category evidence, review count, review dates, and accessibility limitations per comp.
- [ ] `S0-130` Calculate category difficulty and competition thresholds only from captured evidence;
  mark unavailable fields UNKNOWN rather than estimating them.
- [ ] `S0-140` Mine the required critical-review sample with attribution, date, rating when visible,
  edition caveats, source URL, and coded recurring gaps.
- [ ] `S0-150` Map promise occupancy across direct and adjacent competitors; distinguish an unoccupied
  combination from a genuinely unoccupied individual promise.

### Feasibility, risk, and verdict

- [ ] `S0-200` Prove that technical examples, datasets, claims, and assets can be produced and
  independently verified within the cost ceiling.
- [ ] `S0-210` Identify the named subject-matter reviewer requirement and obtain human commitment or
  record it as a publication blocker.
- [ ] `S0-220` Complete trademark screening for the working title, series, imprint, and material
  phrases; record scope limitations and required human signoff.
- [ ] `S0-230` Update `research/evidence.yaml`, `research/keywords.md`, `research/trademark.md`, and
  `research/niche.md` with traceable sources and collector health.
- [ ] `S0-240` Run the deterministic verdict tool and reconcile GO/PIVOT/KILL with `state.json`.
- [ ] `S0-250` If PIVOT, preserve the charter, append seed lineage, increment the cycle, and create
  the next evidence tasks. If GO or KILL, stop at the required human decision.

## Stage 1 — Content architecture and book bible

- [ ] `S1-010` Confirm Stage-0 GO and load the approved persona, gap, differentiation promises,
  keyword language, constitution, and word-count boundary.
- [ ] `S1-020` Generate `outline/outline.md` from `outline/outline.template.md`: thesis, promise chain,
  parts, chapter hierarchy, learning progression, dependencies, word budget, assets, and proof plan.
- [ ] `S1-030` Generate one `outline/chapter_NN.md` from `outline/chapter.template.md` per chapter;
  no chapter may exist only as a title in the master outline.
- [ ] `S1-040` Build `bible/style-sheet.md`, `bible/terminology.md`, and `bible/canon.md`; reconcile
terminology, example entities, datasets, claims, and voice across the outline.
- [ ] `S1-045` Define a component-ownership matrix for every promised element—main text,
translations, exercises, answer material, front/back matter, data, images, and companion files—with
its source, producer, verifier, assembly position, and acceptance test. No promised component may
remain implicit.
- [ ] `S1-050` Instantiate the per-chapter task checklist below once per approved chapter using stable
chapter IDs and the exact output paths.
- [ ] `S1-055` Prove production feasibility early: install and pin the formatter/validator toolchain,
compile one representative print page and EPUB section, and record any platform-specific constraints
that affect the outline, asset plan, trim, or page budget.
- [ ] `S1-060` Validate Gate A: promise coverage, dependency order, non-overlap, word-budget sum,
  opening-page value, differentiators, source feasibility, exercises, and conclusion payoff.
- [ ] `S1-070` Present the outline, track, risks, and unresolved choices for explicit HITL Gate 1
  approval; record the approval and reconcile `manifest.yaml`, `state.json`, and compliance log.

## Stage 2 — Chapter production

- [ ] `S2-010` Confirm Gate 1 approval and freeze the approved outline version for this drafting pass.
- [ ] `S2-020` Schedule chapter batches according to `builds_on` dependencies and shared dataset or
  asset dependencies; do not parallelize chapters with unresolved shared contracts.
- [ ] `S2-030` Run the instantiated checklist for every chapter; retain task-level evidence.
- [ ] `S2-040` Run continuity review after each parallel batch and resolve terminology, canon,
  progression, duplication, and broken-promise findings before the next batch.
- [ ] `S2-050` Verify every approved chapter, summary, source record, exercise, and required asset
  exists; reconcile `chapters_done` in `state.json` only after verification.

## Repeat for every approved chapter

> Duplicate this section after Gate 1. Replace `NN` everywhere. Never check the template itself.

### Chapter NN — `<approved assertion-style title>`

- [ ] `CH-NN-010` Revalidate the chapter contract against the master spine, prior summaries,
  constitution, bible, and current dependencies.
- [ ] `CH-NN-020` Assemble the chapter evidence pack: authoritative sources, claims ledger, original
  examples, dataset/schema version, permissions, and asset requirements.
- [ ] `CH-NN-030` Implement and verify executable examples, exercises, reference solutions, adverse
  cases, and expected outputs before prose makes claims about them.
- [ ] `CH-NN-040` Draft the opening problem, reader promise, prerequisite bridge, and roadmap without
  duplicating the introduction or preceding chapter.
- [ ] `CH-NN-050` Draft every contracted section in dependency order and satisfy its purpose,
  examples, citations, transitions, and word budget.
- [ ] `CH-NN-060` Add tables, diagrams, code, queries, exercises, answer guidance, captions, alt text,
  source/provenance records, and cross-references required by the contract.
- [ ] `CH-NN-070` Verify all claims and examples; record commands, versions, outputs, normalization,
  limitations, and reviewer-visible evidence.
- [ ] `CH-NN-080` Write the chapter recap, reader capability check, next-chapter bridge, and
  `summaries/chapter_NN.summary.md`.
- [ ] `CH-NN-090` Run chapter-level style, continuity, originality, citation, accessibility, and
  placeholder scans; create explicit child tasks for every failure.
- [ ] `CH-NN-100` Confirm the chapter acceptance criteria in `outline/chapter_NN.md`, attach evidence,
  and only then propose it for `chapters_done`.

## Stage 3 — Adversarial structural audit

- [ ] `S3-010` Confirm the draft is structurally complete and freeze the audit input revision.
- [ ] `S3-020` Attack the thesis, promise chain, chapter order, omissions, repetition, pacing,
  unsupported authority, exercise progression, and reader payoff in `audits/structural.md`.
- [ ] `S3-030` Convert every actionable finding into an owned remediation task linked to chapter or
  outline artifacts; classify the responsible loopback stage.
- [ ] `S3-040` Re-run the affected work and audit until Gate B passes or the loop limit escalates.

## Stage 4 — Evidence-based scoring

- [ ] `S4-010` Score every required dimension using manuscript citations and the locked scoring
  contract; never compensate for a below-floor dimension with a stronger average.
- [ ] `S4-020` Write `scores/scorecard.json` and `scores/scoring-notes.md`, including uncertainty,
  evidence locations, and exact remediation ownership.
- [ ] `S4-030` Expand failed dimensions into loopback tasks, increment counters in `state.json`, and
  rescore only after the cited defects are demonstrably corrected.

## Stage 5 — Proofreading and fact verification

- [ ] `S5-010` Proof every chapter mechanically and record each applied change in `edits/edit-log.md`.
- [ ] `S5-020` Verify every checkable claim, citation, version, command, output, table, diagram, and
  link; resolve every flag in `edits/fact-report.md`.
- [ ] `S5-030` Re-run companion-repository tests and manuscript scans after edits to detect regressions.
- [ ] `S5-040` Confirm Gate D has no unresolved fact, citation, placeholder, formatting, or compliance
  flags before packaging.

## Stage 6 — Metadata, cover, and platform packages

- [ ] `S6-010` Re-run the production toolchain preflight and freeze title, subtitle, author/pen name,
  language, edition, trim, paper, bleed, finish, and target platforms as one reconciled identity.
- [ ] `S6-020` Generate evidence-grounded metadata and blurb candidates. The subtitle must state what
  the book is, for whom, what it contains, and the credible reader benefit; obtain human approval and
  re-screen the exact final title, subtitle, series, imprint, and byline.
- [ ] `S6-030` Produce and approve golden samples before bulk export: one styled print story/chapter
  opening with contents and page breaks, one EPUB opening/navigation path, a cover thumbnail, and a
  full-wrap proof with safe areas visible only in the review copy.
- [ ] `S6-040` Compile and validate the full EPUB, print PDF, direct-sale files, front matter,
  navigation, metadata, fonts, images, links, code blocks, tables, language tags, and page geometry.
  Bilingual work also requires a human semantic sample or full review; block parity alone is not a
  translation-quality claim.
- [ ] `S6-050` After the final production page count is known, create one continuous full-wrap cover
  master at the exact calculator dimensions; keep all essential copy in safe areas, omit baked-in
  templates/barcodes, and derive the ebook front cover from the approved wrap.
- [ ] `S6-060` Promote only the authoritative upload candidates to `exports/release/`; run the KDP
  release preflight and generate a manifest with hashes, dimensions, page count, metadata identity,
  build commands, tool versions, and validation reports.
- [ ] `S6-070` Record the exact uploaded hashes and KDP form answers, inspect every page and cover in
  Previewer, and request/inspect a physical proof for a first edition or record an explicit owner
  waiver and its risks. A proof request is not a proof pass.

## Stage 7 — Publication readiness and release

- [ ] `S7-010` Verify Gates A–E, the release manifest and hashes, rights/provenance, exact metadata
  identity, private KDP AI-form answers, prices, categories, reviewer signoff, Previewer approval,
  physical-proof pass or explicit waiver, and cost ceiling from repository evidence.
- [ ] `S7-020` Generate `exports/publish-runbook.md` naming only manifest-listed release files, with
  their hashes, exact form answers, prices, preview/proof evidence, rollback procedure, and
  post-publication reconciliation steps.
- [ ] `S7-030` Present final GO/NO-GO and stop for HITL Gate 2; never upload or publish without explicit
  authorization.
- [ ] `S7-040` After human publication, record identifiers and links, reconcile the live storefront
  title/subtitle/byline/language/categories/format/price/cover against the approved identity, archive
  release evidence, and write the retrospective memory.

## Blocked work

Move `[!]` tasks here or link them here. Each entry must name the blocker owner, failed attempt,
unblock condition, and whether other work may proceed safely.

## Decisions needed from the human

List only decisions that cannot be earned from evidence or safely defaulted. Link the governing task.

## Completed-stage archive

When a stage closes, retain its task IDs and evidence links here. Do not erase failure history,
loopbacks, approvals, or replacement evidence.
