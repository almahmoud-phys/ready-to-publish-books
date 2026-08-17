# Tasks — Spanish A2 Graded Reader — Volume 1

> Detailed human/AI execution ledger. This file coordinates work; it does not replace
> `state.json`, `constitution.md`, or `outline/`. Read `.agents/rules/task-ledger.md` before editing.

## Control panel

> **New here? Read `README.md` in this folder first.** It routes to every record and
> summarises the decisions already made, so you do not re-litigate them.

- **Book:** `spanish-graded-reader-a2` (renamed from `-a1` on 2026-08-13 with the retitle)
- **Lifecycle status:** Stage 6 — in progress. Gate B, Gate C, and Gate D passed; reconciled book score is 8/10.
- **Current focus:** Replace the failed separate-panel Canva construction with one continuous 265.56×209.55 mm full-wrap background and cover master. `Nina Marlo` is final-owner-locked; the 82-page 5×8 cream-paper geometry remains fixed. Full Gate E remains open on final cover review, originality evidence, and cover provenance/native resolution.
- **Next handoff:** Human generates the continuous text-free wrap background from the approved prompt, then supplies the native maximum-resolution result for full-cover composition and front-trim Kindle derivation.
- **Last reviewed:** `2026-08-16`
- **Ledger owner:** Human owner; pipeline agents maintain their task evidence.

> ⚠️ **The Stage 0–2 checkboxes below were never back-filled.** They still read `[ ]` for work
> that is demonstrably complete. Do **not** infer status from them, and do not "tidy" them by
> ticking retroactively — a checkbox is only meaningful when its acceptance evidence was recorded
> at the time, and that evidence now lives in `compliance_log.yaml` and in the dated sections at
> the bottom of this file. **`state.json` is the authority for stage status** (`CLAUDE.md` rule 5);
> this ledger coordinates work and never overrides it. Stage 3 onward starts clean — tick those
> honestly, with evidence, as you go.

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
- [ ] `S1-050` Instantiate the per-chapter task checklist below once per approved chapter using stable
  chapter IDs and the exact output paths.
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

### Stage-2 continuity evidence recovery

- [x] `S2-060` Create the missing rolling summaries and run the required continuity review before
  Stage 3.

<details>
<summary>Execution contract</summary>

- **Owner:** `chapter-writer` for summaries; `continuity-keeper` for the report.
- **Why:** Stage 2 has ten chapter files but no `summaries/chapter_NN.summary.md` files and no
  continuity report. The required summary-only review cannot be truthfully inferred from later
  drafting notes or machine gates.
- **Depends on:** Frozen chapter contracts in `outline/chapter_01.md`–`chapter_10.md`, the bible,
  the chapter files, and the compliance record.
- **Generate / update:** `summaries/chapter_01.summary.md`–`summaries/chapter_10.summary.md`,
  `summaries/continuity-report.md`, any narrowly-scoped chapter/bible fixes, `state.json`, and an
  append-only compliance event.
- **Inputs:** The chapter-writer must use each chapter’s frozen contract, bible, and drafting
  record. The continuity-keeper reads the resulting summaries, bible, and outline contracts only;
  it must not read full chapters.
- **Procedure:**
  1. Produce one factual rolling summary per chapter using the chapter-writer summary format.
  2. Run continuity-keeper over summaries, bible, and contracts; classify term drift, canon
     conflict, promise breakage, and dependency breaks.
  3. Apply only evidenced micro-fixes; update affected summaries and rerun the report if needed.
  4. Attach paths and findings to this task, append the compliance event, and remove the Stage-2
     blocker from `state.json` only when the report is complete.
- **Acceptance criteria:**
  - [ ] Ten rolling summaries exist, one for every manuscript chapter.
  - [ ] `summaries/continuity-report.md` exists and contains precise directives or an explicit
    no-finding verdict.
  - [ ] Every actionable directive is resolved or formally routes to its responsible stage.
  - [ ] `state.json` and this handoff agree that Stage 3 may begin.
- **Verification / evidence:** File existence plus summary-only continuity report; never a
  retroactive assertion without artifacts.
- **Blockers / escalation:** No Stage-2 blocker remains. The annual-light chronology conflict is
  routed to Stage 3 because it spans multiple story contracts and the binding causal ledger.
- **Completion note:** Completed 2026-08-13. Generated
  `summaries/chapter_01.summary.md`–`summaries/chapter_10.summary.md` and
  `summaries/continuity-report.md`. The summary-only audit found one actionable annual-light
  chronology conflict, formally routed to `S3-020`; it found no term, cast/locale,
  promise-chain, or grammar-sequencing drift.

</details>

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

- [x] `S3-010` Confirm the draft is structurally complete and freeze the audit input revision.
- [x] `S3-020` Attack the thesis, promise chain, chapter order, omissions, repetition, pacing,
  unsupported authority, exercise progression, and reader payoff in `audits/structural.md`.
- [x] `S3-030` Convert every actionable finding into an owned remediation task linked to chapter or
  outline artifacts; classify the responsible loopback stage.
- [x] `S3-040` Re-run the affected work and audit until Gate B passes or the loop limit escalates.
- [x] `S3-041` Resolve independent-audit findings F-01 through F-10 in `audits/structural.md`; critical findings must close before another Gate-B review.

<details>
<summary>Execution contract — independent re-audit blocker recorded 2026-08-14</summary>

- **Owner:** Human owner supplies one working independent provider; `adversarial-editor` performs the read-only audit.
- **Why:** The repair model cannot be its own last reader. The prior Gate-B PASS is superseded, so Gate B is `null` despite valid targeted repair checks.
- **Depends on:** `audits/independent-stage3-brief.md` and an authenticated, quota-available non-OpenAI model family.
- **Generate / update:** Proposed replacement content for `audits/structural.md`; then this ledger, `state.json`, and append-only compliance evidence.
- **Inputs:** The read scope and reporting contract in `audits/independent-stage3-brief.md`.
- **Procedure:**
  1. Configure or restore one independent provider.
  2. Dispatch the brief read-only; it must not read superseded audits or scores.
  3. Verify its citations against the manuscript before replacing the placeholder audit.
  4. Record Gate B. Proceed to Stage 4 only if Gate B passes.
- **Acceptance criteria:**
  - [ ] A non-OpenAI-family reviewer returns all required attack passes and citation-backed findings.
  - [ ] `audits/structural.md` contains an independent Gate-B recommendation and verification block.
  - [ ] `state.json` records the resulting Gate-B value.
- **Verification / evidence:** `audits/independent-stage3-brief.md`; provider transcript; citation checks against the cited manuscript files.
- **Blockers / escalation:** `qwenmax` returned `401 Invalid API-key`; native `claude` requires `/login`; `minimaxclaude` lacks `minimax-anthropic-token`; `k3-256k` returned `403` because its billing-cycle usage limit is exhausted. Unblock by logging into Claude CLI, correcting the Qwen key, restoring the MiniMax token, or replenishing Kimi/K3 quota. Do not use another OpenAI-family model as a substitute.
- **Completion note:** Unblocked 2026-08-14 through Jcode Claude OAuth. The final fresh Claude/Anthropic audit (`claude-opus-4-6`, session `session_chick_1786674816656_aeb24a226b6d11e9`) found zero critical findings and set Gate B to **PASS**. The active evidence is `audits/structural.md`.

</details>

<details>
<summary>S3-041 remediation contract — Gate B FAIL on independent evidence</summary>

- **Owner:** `outline-architect` for F-03/F-04/F-08; grammar-tooling maintainer for F-03/F-07; `chapter-writer` for F-01/F-02/F-06/F-09; later owner assignment for F-05.
- **Why:** Independent Claude/Anthropic review found three critical contract defects. Gate B requires zero open critical structural findings.
- **Depends on:** `audits/structural.md`; current Stage-1 contracts; grammar and lexical gates; `PIPE-001` remains separate and must not be bypassed by unowned translation work.
- **Generate / update:** Cited outline contracts, affected chapters, grammar checker plus regression coverage, affected summaries and vocabulary ledger, then a fresh independent structural audit.
- **Procedure:**
  1. Amend Story 02’s turn to remove the imperfected `estaba`, and correct stale Stage-1 metadata (F-03/F-04/F-08).
  2. Make `spanish_grammar_check.py` detect `estar` imperfect forms and pin the regression (F-03/F-07).
  3. Add the exact contracted exercises to Stories 02–10 (F-01).
  4. Extend Stories 07–08 to their 675-word floors and repair the Story-10 demonstrated payoff (F-02/F-06); resolve the Story-07 Lucía-identity drift (F-09).
  5. Establish answer-key ownership before producing answer keys (F-05); do not manufacture English translation ownership.
  6. After Spanish edits, rerun grammar and cumulative lexical/locale gates on every affected story, regenerate affected summaries, rerun continuity, and obtain another independent Stage-3 audit.
- **Acceptance criteria:**
  - [x] F-01, F-02, and F-03 are closed with file-and-command evidence.
  - [x] All affected Spanish gates pass; summaries and ledger are synchronized.
  - [x] A new independent audit has zero open critical findings and records Gate B PASS.
- **Verification / evidence:** `audits/structural.md`; story-level grammar and `graded_reader_check.py --ledger ... --story NN --locale latam` output; regression tests; `summaries/continuity-report.md`.
- **Blockers / escalation:** No external provider blocker remains. Do not alter Gate-B thresholds or call another OpenAI-family review independent. F-05 cannot be completed until answer-key ownership is explicitly assigned; `PIPE-001` still governs English parallel-text ownership.
- **Completion note:** Closed 2026-08-14. The repaired contracts, grammar regression coverage, exercises, narrative floors, summaries, vocabulary ledger, and continuity record passed their checks. Fresh independent Claude/Anthropic audit session `session_chick_1786674816656_aeb24a226b6d11e9` recorded zero critical findings and Gate B PASS. Its remaining S3-R1/S3-T1/S3-C1 quality directives are inputs to Stage 4, not hidden completion claims.

</details>

### Stage-3 loopback — annual-light chronology

- [x] `LB-S3-001` Establish an authoritative chronology for the annual lamp, the five-week volume
  span, Beto’s boat travel, and the Story-10 entry transition.

<details>
<summary>Execution contract</summary>

- **Owner:** `outline-architect`, then targeted `chapter-writer`.
- **Why:** `audits/structural.md` F-01 is critical: the binding causal ledger permits one annual
  lamp appearance within a roughly five-week volume, while Stories 01, 07, and 10 create an
  incompatible sequence and Story 10 claims a one-year interval.
- **Depends on:** `audits/structural.md`, `bible/letters-causal-ledger.md`, contracts 01/07/10,
  rolling summaries, and constitution.
- **Generate / update:** A reconciled timeline decision in the owning outline/bible artifact;
  a targeted change plan; only then the affected chapter files, their summaries, vocabulary ledger
  if lexical content changes, and gate evidence.
- **Procedure:**
  1. Decide whether Story 01 or Story 10 contains the annual lamp ritual and whether Story 07’s
     observed light is distinct; do not add an uncontracted second annual ritual.
  2. Make the volume elapsed time, Beto’s return, and Story-10 transition consistent with that
     decision.
  3. Revise only cited chapters/bible records; rerun vocabulary/locale and grammar gates on each
     changed Spanish chapter; regenerate its summary.
  4. Re-run continuity review if canon or summaries change, then rerun the structural audit.
- **Acceptance criteria:**
  - [x] Exactly one coherent annual lamp/sea-letter chronology exists across the causal ledger and
    manuscript.
  - [x] The reader can follow elapsed time into Story 10 without an unsupported jump.
  - [x] All affected machine gates pass and the re-audit has no critical finding.
- **Verification / evidence:** `audits/structural.md` re-audit; targeted Story 07 and Story 10
  grammar plus vocabulary/locale runs; updated `summaries/continuity-report.md`.
- **Blockers / escalation:** Resolved without a constitution amendment.
- **Completion note:** Repair completed 2026-08-13. Stories 01–09 span roughly five weeks; Story 10
  explicitly returns almost a year later for the next annual lamp ritual. Story 07's light is an
  ordinary boat light. Targeted grammar and vocabulary/locale gates passed. The same-model re-audit
  PASS was later superseded, so independent Gate-B verification remains blocked under `S3-040`.

</details>

<details>
<summary>Stage 3 execution contract — active 2026-08-13</summary>

- **Owner:** `adversarial-editor`.
- **Why:** The complete manuscript must survive a structural attack before it can be scored.
- **Depends on:** Stage 2 complete: summaries, `summaries/continuity-report.md`, frozen outline,
  bible, manuscript chapters, constitution, manifest, and compliance record.
- **Generate / update:** `audits/structural.md`; then remediation tasks and state/compliance updates.
- **Inputs:** Whole manuscript plus Stage-2 continuity report. First mandatory target: the annual
  light conflict between the report and `bible/letters-causal-ledger.md`.
- **Acceptance criteria:**
  - [x] Audit records evidence-based findings and an explicit Gate B verdict.
  - [x] Every actionable finding has an owner and responsible loopback stage.
  - [x] No finding is silently repaired or dismissed without evidence.
- **Verification / evidence:** `audits/structural.md` F-01/F-02 and `LB-S3-001`.
- **Blockers / escalation:** The repair is complete, but Gate B remains undecided until an independent
  model family re-audits it. The prior same-model PASS is superseded as gate evidence.

</details>

## Stage 4 — Evidence-based scoring

- [x] `S4-010` Score every required dimension using manuscript citations and the locked scoring
  contract; never compensate for a below-floor dimension with a stronger average.

<details>
<summary>Execution contract — Stage-4 independent-panel blocker recorded 2026-08-14</summary>

- **Owner:** Human owner configures a second independent provider; `scorer` runs the panel.
- **Why:** The scorer requires an excerpt judge and fresh re-judge with independent model families. The book’s OpenAI family drafted/repaired manuscript content and cannot be counted as an independent scoring vote.
- **Depends on:** Gate B PASS; `.agents/rules/model-routing.md`; `.agents/rules/scoring-contract.md`; a configured second non-OpenAI model family.
- **Generate / update:** Preregistration artifact with thresholds, blinded excerpt seeds and calibration control; then `scores/scorecard.json`, `scores/scoring-notes.md`, `state.json`, and compliance evidence.
- **Acceptance criteria:**
  - [ ] At least two independent model families complete the required scoring passes.
  - [ ] Disagreements over one point receive the required tiebreak.
  - [ ] Every sub-nine score has two manuscript citations; every sub-floor score has a weakest passage and exact loopback.
- **Verification / evidence:** Judge transcripts, preregistration artifact, scorecard schema validation, and cited manuscript locations.
- **Blockers / escalation:** Jcode Claude/Anthropic is available. Jcode has no Qwen, DeepSeek, Gemini, Kimi, or other second non-OpenAI family configured. Existing Qwen authentication, MiniMax token, and K3 quota failures remain unresolved; do not use Codex/OpenAI as a substitute panel family.
- **Completion note:** Completed 2026-08-14. Qwen 3.8 Max Pass 1 and Claude/Anthropic Pass 2 independently returned `8/7/8/8/8/8`; no tiebreak was required. The cited Claude full-manuscript pass adjusted Prose to 8 and Coherence to 9. `scores/scorecard.json` records Gate C **PASS**, book score 8, and no loopbacks.

</details>
- [x] `S4-020` Write `scores/scorecard.json` and `scores/scoring-notes.md`, including uncertainty,
  evidence locations, and exact remediation ownership.
- [x] `S4-030` Expand failed dimensions into loopback tasks, increment counters in `state.json`, and
  rescore only after the cited defects are demonstrably corrected. No dimension failed the 7/10 floor; no counters incremented.

> **Superseded attempt — 2026-08-14:** The single-model scorecard skipped the required independent
> re-judge protocol, reused the repair model as judge, and penalized later-stage/unowned artifacts.
> It is preserved under `scores/superseded/` as non-gate evidence. It did not produce a Gate-C verdict
> or valid loopback counters.

### Unresolved pipeline ownership — bilingual product components

- [!] `PIPE-001` Assign an explicit stage/skill owner for English parallel-text production and
  verification before those components are generated.

<details>
<summary>Ownership decision contract</summary>

- **Owner:** Pipeline architecture / human owner.
- **Why:** `outline/outline.md` contracts English translations, but `chapter-writer` owns only one
  chapter and summary, while `formatter-platform` assembles/exports and does not own translation
  generation. No current skill lawfully owns producing and verifying parallel text.
- **Decision required:** Amend an existing skill contract or add a dedicated translation stage/skill,
  including context permissions, outputs, independent verification, KDP disclosure logging, and its
  position relative to Gates C and D.
- **Blockers / escalation:** This ownership gap does not authorize Stage 2 to invent translations or
  Stage 4 to score Stage-6 frontmatter as missing. Resolve it before bilingual production begins.

</details>

## Stage 5 — Proofreading and fact verification

- [x] `S5-010` Proof every chapter mechanically and record each applied change in `edits/edit-log.md`.

<details>
<summary>Execution contract — activated 2026-08-14</summary>

- **Owner:** `proofreader`.
- **Why:** Gate D requires all supported mechanical corrections to be applied and auditable without reopening Stage-3/4 prose or structural judgment.
- **Depends on:** Gate B PASS, Gate C PASS, active manuscript chapters 01–10, house style, cast/place/causal records, and the grammar and lexical/locale gates.
- **Generate / update:** `edits/edit-log.md`; only supported corrections to affected chapter files; `bible/cast.md` only for the already-evidenced Beto-register record correction; append-only compliance events; this ledger.
- **Inputs:** `chapters/01-*.md`–`10-*.md` only; `.agents/rules/style.md` as the fallback because `bible/style-sheet.md` does not exist; `bible/cast.md`, `bible/places.md`, and `bible/letters-causal-ledger.md`.
- **Procedure:**
  1. Review each chapter for spelling, grammar, punctuation, dialogue-dash form, Markdown/exercise presentation, canon terminology, and the mechanical banlist.
  2. Apply only corrections that preserve meaning; record every applied change as `chapter | before | after | rule`.
  3. Record any issue that would require a voice/quality rewrite as `VOICE-DECISION` rather than silently changing it.
  4. After every Spanish edit, rerun `spanish_grammar_check.py` and the cumulative `graded_reader_check.py --ledger ... --story NN --locale latam` command for that chapter; rebuild the vocabulary ledger and summaries only if lexical content changes.
  5. Correct Beto's stale bible register only if the delivered prose confirms the supported terse/evasive description; consider no `mirar` rewrite or Rosa cue unless a mechanical defect requires it.
- **Acceptance criteria:**
  - [x] All ten publishable chapter files were reviewed; the excluded pipeline-proof file is not treated as manuscript content.
  - [x] Every applied correction appears in `edits/edit-log.md`; no silent change remains.
  - [x] The non-mechanical `mirar` note was resolved as retain-as-is; no Gate-D voice blocker remains.
  - [x] Required gates pass for every changed Spanish chapter.
- **Verification / evidence:** `edits/edit-log.md`; targeted gate output recorded there; `S5-030` repository validation; compliance events with hashes.
- **Blockers / escalation:** The missing `bible/style-sheet.md` is recorded as a fallback limitation, not a license to invent voice. `PIPE-001` continues to prohibit parallel-translation work.
- **Completion note:** Complete 2026-08-14. `edits/edit-log.md` records seven supported changes, including the Story-08 grammar/continuity repair and the checker regression fix. All ten grammar and lexical/locale gates pass; targeted regression suite: 30 passed.

</details>

- [x] `S5-020` Verify every checkable claim, citation, version, command, output, table, diagram, and
  link; resolve every flag in `edits/fact-report.md`.

<details>
<summary>Execution contract — activated 2026-08-14</summary>

- **Owner:** `fact-checker`.
- **Why:** Gate D requires all reader-facing factual, attribution, and publication-process claims to have a documented final disposition.
- **Depends on:** Gate C PASS; active reader-facing manuscript and claim-bearing source records; live primary sources where a claim requires currency.
- **Generate / update:** `edits/fact-report.md`; minimal rewrites only where an active reader-facing claim is false, stale, or unverifiable; append-only compliance events; this ledger.
- **Inputs:** Publishable chapter files, `manifest.yaml`, `assets/WORDLIST-PROVENANCE.md`, `research/niche.md`, `.agents/rules/kdp-compliance.md`, and official/primary external sources as required. Fictional plot events are explicitly out of scope.
- **Procedure:**
  1. Separate fictional plot from checkable reader-facing/process claims.
  2. Verify wordlist source/license, machine-check limitation wording, level/locale claims, and active KDP disclosure/process statements against primary sources or exact local evidence.
  3. Do not treat future Stage-6 title, metadata, translations, frontmatter, or claims as present artifacts; record their ownership boundary instead.
  4. Record every reviewed claim with source/evidence, access date where external, and exactly one resolution: `verified`, `rewritten`, or `cut`.
- **Acceptance criteria:**
  - [x] No plot event is misclassified as an external factual claim.
  - [x] Every identified checkable claim is resolved as `verified`, `rewritten`, or `cut`.
  - [x] No unsupported certification, coverage-threshold, locale, KDP, licensing, or attribution statement remains in an active reader-facing artifact.
  - [x] `PIPE-001` is accurately recorded as an ownership blocker, not bypassed.
- **Verification / evidence:** `edits/fact-report.md` with local paths, exact source URLs, access dates, and final resolutions.
- **Blockers / escalation:** If a reader-facing claim lacks a current primary source, it must be rewritten or cut; no reliance on model memory.
- **Completion note:** Complete 2026-08-14. `edits/fact-report.md` resolves nine claims against official/local evidence; it prohibits certification, unimplemented-check, and translation claims from Stage-6 copy.

</details>

- [x] `S5-030` Re-run companion-repository tests and manuscript scans after edits to detect regressions. Evidence: `python3 -m pytest tests/test_spanish_grammar_gate.py tests/test_graded_reader_gate.py` — 30 passed; grammar and cumulative lexical/locale gates — 10/10 pass; banlist scan — no matches.
- [x] `S5-040` Confirm Gate D has no unresolved fact, citation, placeholder, formatting, or compliance
  flags before packaging. **Gate D PASS**: edit log complete, fact-report dispositions complete, validation evidence recorded, and Stage-6 ownership limits preserved.

## Stage 6 — Metadata, cover, and platform packages

- [x] `S6-005` Repair Stage-6 evidence, canonical paths, governance, and pre-compilation safety before the human micro-gates.

<details>
<summary>Execution contract — activated 2026-08-14 after adversarial Stage-6 review</summary>

- **Owner:** `metadata-seo` + `cover-director` + governance/tooling maintainer; human retains final mark and cover selection.
- **Why:** The first candidate pass used non-canonical metadata paths, lacked the required keyword and comp-cover evidence, proposed a mismatched phrasebook category, relied on unobserved thumbnail predictions, inherited the wrong manifest genre, and left `PIPE-001` as prose rather than an executable compiler refusal.
- **Depends on:** Gate D PASS; the read-only Stage-6 adversarial review approved for repair by the owner; `metadata-seo`, `cover-director`, and `formatter-platform` contracts; `research/niche.md`; `edits/fact-report.md`; append-only compliance law.
- **Generate / update:** `research/keywords.md`; `research/cover-comps.md`; canonical `exports/metadata.json` and `exports/blurbs.md`; `exports/cover/cover-notes.md`; three deterministic concept mockups and 100px thumbnails under `exports/cover/concepts/`; `manifest.yaml`; `state.json`; `README.md`; `tooling/scripts/compile_book.py`; targeted regression tests; append-only `compliance_log.yaml`; this ledger. Remove the superseded nested metadata copies only by moving them to the canonical paths, preserving their historical log entries.
- **Inputs:** Current Stage-6 candidate artifacts; `research/niche-ledger.csv`; official KDP metadata/category guidance; accessible competitor publisher/catalog cover assets; `research/trademark.md`; `.agents/rules/kdp-compliance.md`; `PIPE-001` decision contract.
- **Procedure:**
  1. Separate observed buyer/cover evidence from inference; record sources, dates, limitations, and inaccessible Amazon pages.
  2. Canonicalize metadata outputs to the paths declared by `metadata-seo` and consumed by `formatter-platform`.
  3. Rebuild the seven slots without duplicate title/subtitle words or repeated stems; replace the phrasebook category with a content-accurate conditional fiction category.
  4. Replace near-duplicate cover concepts with three distinct strategies, render deterministic approval mockups, and inspect real 100px thumbnails before asking for selection.
  5. Correct `manifest.yaml` to fiction without reopening Gate C: fiction additions are explicitly deferred by `.agents/rules/scoring-contract.md`, while the completed universal panel remains valid.
  6. Append correction evidence for the invalid Stage-6 timestamps; never edit or reorder historical compliance entries.
  7. Make `compile_book.py` refuse before writing anything while `PIPE-001` is listed as an active Stage-6 blocker; pin the refusal with a regression test.
  8. Run JSON/YAML/SVG/image checks, the targeted test, artifact-path searches, and an independent adversarial review.
- **Acceptance criteria:**
  - [x] `research/keywords.md` and `research/cover-comps.md` distinguish observed evidence from inference and record source limitations.
  - [x] Canonical metadata exists only at `exports/metadata.json` and `exports/blurbs.md`; downstream contracts resolve those paths.
  - [x] Exactly seven compliant keyword phrases have no repeated title/subtitle words or duplicate stems; the phrasebook mismatch is removed.
  - [x] Three strategically distinct visual mockups and actual 100px thumbnails exist; cover claims cite observed comparison results.
  - [x] `manifest.yaml` says `genre: fiction`; Stage 6 remains `in_progress`; Gate C and Gate D evidence remain preserved.
  - [x] Compliance history is unchanged and append-only correction events explicitly invalidate the five non-monotonic Stage-6 timestamps.
  - [x] The compiler exits non-zero before creating exports/frontmatter when `PIPE-001` is active, with a passing targeted regression test.
  - [x] Final title, subtitle, KDP description, pen name, series, imprint, and cover remain unselected pending human approval and final-mark screening.
- **Verification / evidence:** JSON/YAML parsing; `python3 -m pytest` targeted compiler test; whole-project path/twin searches; SVG/XML parsing; PNG dimensions; 100px visual inspection; independent attacker reports.
- **Blockers / escalation:** Amazon product pages remain behind a sign-in/interstitial wall and must not be bypassed. Final AI artwork, final mark screening, print spread, and bilingual interior remain outside this repair until their human/architecture gates clear.
- **Completion note:** Completed 2026-08-14 after two adversarial repair cycles. Created `research/keywords.md` and `research/cover-comps.md`; canonicalized `exports/metadata.json` and `exports/blurbs.md`; replaced the phrasebook category; rendered three 1600×2560 SVG/PNG concepts plus 100×160 thumbnails; corrected `manifest.yaml` to fiction; appended timestamp corrections and per-artifact generation hashes; recorded `PIPE-001` in `state.json`; and added a pre-write compiler refusal pinned by `tests/test_compile_book_guard.py` (`1 passed`). Attacker findings repaired: stale README state, temporary debris, T3 audience mismatch, overbroad/stale keyword claims, omitted cover locale contract, unrendered/clipped candidate subtitle, 2:3 prompts, and ambiguous skill output paths. The real compiler invocation refused with exit 2 before Pandoc.

</details>

- [!] `S6-010` Generate evidence-grounded title/subtitle candidates, keywords, categories, and blurbs;
  record human approval and trademark recheck for the final selection.

<details>
<summary>Execution contract — activated 2026-08-14</summary>

- **Owner:** `metadata-seo`, with human approval for the final marks and KDP description.
- **Why:** Title, subtitle, search phrases, categories, and channel-specific conversion copy must reflect the validated adult-reader niche without making unsupported level, certification, locale-authenticity, audio, or translation claims.
- **Depends on:** Gate D PASS in `state.json`; `research/niche.md`; `edits/fact-report.md`; and final-mark trademark screening before any candidate becomes a selected title.
- **Generate / update:** `exports/metadata.json` and `exports/blurbs.md`; update `manifest.yaml` title/subtitle only after human selection and final-mark screening; then update this ledger and append compliance evidence.
- **Inputs:** `research/niche.md`, `research/keywords.md`, `research/gtm-series-decision.md`, `outline/outline.md`, `assets/WORDLIST-PROVENANCE.md`, `edits/fact-report.md`, `research/trademark.md`, and `.agents/rules/kdp-compliance.md`.
- **Procedure:**
  1. Derive category-legible candidates and buyer-intent phrases strictly from the validated niche evidence.
  2. Draft short, KDP, and direct-sales blurbs that preserve the adult-reader differentiation and claim boundaries.
  3. Identify a recommended candidate without treating it as final.
  4. Hold final selection for the human, then re-screen the actual title, subtitle, pen name, series name, and imprint before updating `manifest.yaml`.
- **Acceptance criteria:**
  - [x] Metadata artifacts contain title/subtitle candidates, exactly seven KDP keyword phrases, two evidence-grounded category targets, and three channel-appropriate blurbs.
  - [x] Every reader-facing claim conforms to `edits/fact-report.md`; no translation, audio, CEFR-certification, or regional-authenticity claim appears.
  - [ ] A final selection has human approval and a dated, scoped final-mark trademark re-screen before `manifest.yaml.subtitle` changes.
- **Verification / evidence:** `research/keywords.md`; source-to-claim traceability in `exports/metadata.json`; JSON parse and seven-slot/no-overlap command recorded under `S6-005`; parallel read-only Luna + Terra review in `audits/stage6-gtm-review-results.md`; human decision and final trademark report to be recorded here.
- **Blockers / escalation:** T1 title/subtitle, KDP description, no-series/no-imprint launch, and exact pen name `Nina Marlo` are human-locked. The prospective `Puerto Lento Spanish Readers` umbrella is not launch metadata and remains unscreened. The Stage-0 trademark finding does not cover future marks.
- **Completion note:** Repaired candidates exist at canonical `exports/metadata.json` and `exports/blurbs.md`. Human selected T1 — `The Letter at Puerto Lento` / `10 Linked Spanish Stories for Adult Learners (A2 Graded Reader)` — on 2026-08-14. The adopted GTM architecture launches it standalone and unnumbered; internal/historical “Volume 1” language does not become reader-facing metadata. Seven slots have zero exact title/subtitle overlap and no duplicate phrases; the phrasebook mismatch is replaced by a conditional fiction/short-stories target. The proposed internal-series explanation was rejected by the human and must not enter customer-facing copy. Parallel read-only Luna + Terra reviews (`audits/stage6-gtm-review-results.md`) converged on story-first copy, one conventional human-sounding pen name for this product line, and no bespoke imprint. The human locked the synthesized KDP description and confirmed no bespoke imprint. `Avery Calder` was rejected because an active author already uses it; the owner then approved `Nina Marlo`, which the independent comparative `S6-110` review unanimously retained over `Nina Marlow`.

</details>

- [!] `S6-020` Produce three category-legible cover concepts, record human selection, generate licensed
  assets, and verify thumbnail, trim, bleed, spine, typography, and accessibility requirements.

<details>
<summary>Execution contract — activated 2026-08-14</summary>

- **Owner:** `cover-director`, with human selection at the Stage-6 cover micro-gate.
- **Why:** The cover must signal an adult Spanish graded reader at thumbnail size while differentiating it from child-primer and generic textbook visuals.
- **Depends on:** Gate D PASS; observed comp evidence; metadata positioning; human visual selection before final image-API generation; formatter page count before a print-spread/spine build.
- **Generate / update:** `research/cover-comps.md`; `exports/cover/cover-notes.md`; three deterministic approval comps and 100px thumbnails under `exports/cover/concepts/`. Generate final image assets only after human selection and log each actual generation in `compliance_log.yaml`.
- **Inputs:** `research/niche.md`, `research/cover-comps.md`, `exports/metadata.json`, `edits/fact-report.md`, `manifest.yaml`, and `.agents/rules/kdp-compliance.md`.
- **Procedure:**
  1. Observe accessible competitor covers and record source/thumbnail limits; do not infer blocked Amazon evidence.
  2. Develop three strategically distinct thumbnail-first concepts and record the hybrid-typography decision.
  3. Render deterministic approval comps and actual 100px thumbnails; present those visuals for human selection before final image-API generation.
  4. After selection and page-count availability, generate/refine final assets, overlay exact approved metadata, repeat the 100px test, and build a print spread with required bleed/spine/barcode space.
- **Acceptance criteria:**
  - [x] Three distinct concepts and prompts are documented with observed category signal, differentiation, actual 100px results, cost boundary, disclosure implications, and an ADR-005 recommendation.
  - [x] No concept implies audio, available translations, CEFR certification, human authorship, or regional-authenticity beyond the declared convention.
  - [ ] Human selection, final image generation/refinement, final 100px evidence, and print-production measurements are recorded before this task is complete.
- **Verification / evidence:** `research/cover-comps.md`; rendered images and observed results in `exports/cover/cover-notes.md`; Luna + Terra refinement consensus and background-only prompt in `audits/stage6-gtm-review-results.md`; per-asset compliance entries; future final-cover selection recorded here.
- **Blockers / escalation:** Concept 1 and generated background 02 were selected by the human owner. The refined front-cover candidate exists under `exports/cover/final/`. Remaining front-cover blockers: human confirms the replacement pen name; supplies provider/model/actual cost for both generated backgrounds; and accepts the 816×1312 source-resolution caveat or supplies a native higher-resolution background. Print spine and final geometry depend on formatter output, which is machine-blocked while `PIPE-001` remains unresolved.
- **Completion note:** Three distinct visual directions exist as 1600×2560 SVG/PNG comps plus 100×160 thumbnails. Human selected Concept 1, the category-first literary bridge, on 2026-08-14. This authorizes controlled final-background and editable-typography refinement only; final image provenance and the print spread remain open. Parallel Luna + Terra review identified the remaining professionalization work. It has now been applied in `exports/cover/final/front-cover.svg`: background 02 is embedded, internal/unapproved straplines are removed, clip art is replaced, typography is editable and deliberate, and a true 100×160 test exists. Luna selected background 02; Terra selected 01; the owner's explicit preference for 02 controls. The approved byline is `Nina Marlo`.

</details>

- [!] `S6-030` Compile and validate EPUB, print PDF, direct-sale files, front matter, navigation,
  metadata, fonts, images, links, code blocks, tables, and page geometry.

<details>
<summary>Execution contract — blocked 2026-08-14</summary>

- **Owner:** `formatter-platform`, after the human/pipeline architecture assigns bilingual production.
- **Why:** The published product contract calls for English parallel text, but no skill currently owns its production or independent verification.
- **Depends on:** `PIPE-001` resolved with an explicit translation owner, source placement, independent fidelity verification, disclosure logging, Spanish-span language tagging, and a decision on exercise placement in Kindle Look Inside.
- **Generate / update:** On unblock, source assembly, EPUB/PDF packages, validation reports, and this ledger.
- **Acceptance criteria:**
  - [ ] No bilingual interior is compiled before every `PIPE-001` decision is evidenced.
  - [ ] Any intermediate Spanish-only preview is explicitly non-publishable and does not misrepresent the contracted bilingual product.
- **Verification / evidence:** Future formatter reports and platform validation output.
- **Blockers / escalation:** `PIPE-001` is blocked by the human/pipeline architecture owner and now enforced before compiler writes. Unblock only with a documented owner and verification method; no agent may generate translations as a workaround. On unblock, repair the compiler's stale `chapter_*.md` source glob to select the actual `01-*.md`–`10-*.md` manuscript explicitly and exclude `sample-story-pipeline-proof.md` before any real build.
- **Completion note:**

</details>

- [ ] `S6-040` Record reproducible build commands, tool versions, checksums, validation reports, and
  platform-specific deviations for every export.

- [x] `S6-090` Lock the owner-approved pen name `Nina Marlo` and propagate the exact spelling to
  authoritative metadata and generated presentation artifacts.

<details>
<summary>Execution contract — activated 2026-08-15</summary>

- **Owner:** Human owner for approval; `metadata-seo`, `formatter-platform`, and `cover-director` for propagation.
- **Why:** KDP requires the cover author name to exactly match title setup, and the current candidate artifact says `Nina Marlow`, not the newly approved `Nina Marlo`.
- **Depends on:** Owner approval in the 2026-08-15 conversation; best-available exact-name screening already recorded for the prior spelling, supplemented for the approved spelling before lock.
- **Generate / update:** `manifest.yaml`, `exports/metadata.json`, `research/trademark.md`, current cover and interior artifacts, `exports/cover/cover-notes.md`, `exports/build-report.md`, `state.json`, append-only `compliance_log.yaml`, and this ledger.
- **Inputs:** Exact owner-approved spelling `Nina Marlo`; official KDP cover/detail-match requirement; current Stage-6 artifacts.
- **Procedure:**
  1. Re-screen the exact approved spelling for obvious author collisions and record scope limits.
  2. Replace candidate-status records with a dated owner approval without rewriting historical evidence.
  3. Rebuild the front cover and interior exports so every live artifact uses the approved spelling.
- **Acceptance criteria:**
  - [x] Authoritative metadata and all current reader-facing artifacts say exactly `Nina Marlo`.
  - [x] Historical references remain identifiable as superseded evidence rather than silently rewritten.
  - [x] Cover and interior metadata/bylines agree.
- **Verification / evidence:** Exact-name web search; repository-wide exact-string search; SVG/XML and image dimension checks; EPUB/PDF rebuild reports.
- **Blockers / escalation:** Exact-name screening is practical collision screening, not legal trademark clearance.
- **Completion note:** Owner approval recorded 2026-08-15. A fresh exact-name screen found no clear active author collision in accessible results; a 1951 theatre-program credit is historical, not a contemporary author identity. Manifest, metadata, current cover source/renders, and rebuilt interior metadata use exact `Nina Marlo`. This remains a practical screen, not legal clearance.

</details>

- [~] `S6-100` Decide the final paperback trim from an actual formatted interior page count and
  create a reusable official-source KDP publishing skill.

<details>
<summary>Execution contract — activated 2026-08-15</summary>

- **Owner:** `formatter-platform` for the diagnostic; human owner for the final trim decision; skill maintainer for reusable KDP guidance.
- **Why:** The calculator input of 63 pages describes the Letter-size direct PDF, not the KDP interior. Cover geometry must be based on the final formatted trim and exact resulting page count.
- **Depends on:** Current bilingual `exports/master.md`; official KDP trim, margin, bleed, spine, and cover-calculator documentation; `skill-creator` workflow.
- **Generate / update:** A non-release 5x8 diagnostic PDF/report; `.agents/skills/kdp-publishing/` with source-backed modular references and deterministic geometry tooling; this ledger. Do not replace the current release interior until the owner accepts the trim recommendation.
- **Inputs:** KDP help topics `GVBQ3CMEQW3W2VL6` and `G201953020`, KDP Cover Calculator, current 69-page 6x9 print interior, and attached 63-page calculator screenshot.
- **Procedure:**
  1. Verify the official limits and formulas and distinguish eligibility from merchandising quality.
  2. Format the actual interior at 5x8, count pages, and check margins/legibility.
  3. Compare 5x8 and 6x9 using exact page/spine geometry; recommend one, leaving the release artifact unchanged pending owner decision.
  4. Scaffold, write, validate, and forward-test the reusable KDP skill.
- **Acceptance criteria:**
  - [x] The recommendation uses the final-formatted 5x8 page count, not 63 or an estimate.
  - [x] Every numerical rule is traceable to an official KDP URL with a verification date.
  - [x] The skill passes `quick_validate.py`; bundled scripts pass representative tests; a fresh-agent forward test identifies no blocking ambiguity.
- **Verification / evidence:** PDF page geometry/count inspection; KDP calculator/formula cross-check; skill validator and script tests.
- **Blockers / escalation:** The print wrap remains blocked until the human locks trim, paper, final page count, and cover-background provenance/resolution.
- **Completion note:** Official-source assessment recommends 5×8 black ink on cream, no interior bleed. The actual manuscript formats to 81 pages; KDP production count is 82, with a 5.207 mm spine and 265.557 × 209.550 mm wrap. The release artifact remains 6×9 pending owner confirmation. New `.agents/skills/kdp-publishing/` passes validation and independent forward testing; the test's minor spine-eligibility wording findings were applied.

</details>

- [x] `S6-110` Re-screen `Nina Marlo` against `Nina Marlow` and make a documented final pen-name recommendation.

<details>
<summary>Execution contract — activated 2026-08-15</summary>

- **Owner:** `metadata-seo`, with independent Terra and Luna reviewers; human owner retains final approval.
- **Why:** Raw Google-result scarcity is not automatically safer, while an exact-name social footprint can create attribution, search, impersonation, or reputational collision risk.
- **Depends on:** `S6-090`; current exact-name metadata; public indexed web/catalog/social evidence available without bypassing access controls.
- **Generate / update:** `research/trademark.md`, `exports/metadata.json`, `manifest.yaml`, affected cover/interior exports only if the selected spelling changes, and this ledger.
- **Inputs:** Exact queries for `Nina Marlo` and `Nina Marlow`; author/book catalogs; visible social profiles; Terra and Luna independent findings.
- **Procedure:** Compare exact-name publishing collisions, broader identity footprints, search distinctiveness, reputational ambiguity, and long-term brand usability; distinguish verified facts from profile-authenticity inference; reconcile the independent reviews into one recommendation.
- **Acceptance criteria:** Both names receive symmetric searches; Terra and Luna independently state a choice and evidence; the final recommendation explains why result count alone is insufficient; no unsupported claim labels a person or profile as AI-generated.
- **Verification / evidence:** Dated query/source ledger in `research/trademark.md`; agent findings; repository exact-string scan after any approved change.
- **Blockers / escalation:** Search indexing is incomplete and social-profile authenticity generally cannot be proven from appearance alone. This is practical collision screening, not legal clearance.
- **Status:** Complete and final-owner-locked 2026-08-15. Terra, Luna, and the primary reviewer independently selected `Nina Marlo`; the owner then explicitly instructed “I choose Nina Marlo. lock it.” The comparative evidence and inference boundary are recorded in `research/trademark.md`; no metadata or export spelling changed. Reopen only for a concrete legal, marketplace, or identity-conflict defect.

</details>

- [x] `S6-120` Build the owner-approved 5×8 cream-paper paperback interior and exact full-cover wrap.

<details>
<summary>Execution contract — activated 2026-08-15</summary>

- **Owner:** `formatter-platform` for the interior; `cover-director` for the wrap; human owner approved the production specification with “approved.”
- **Why:** The diagnostic established that 5×8 gives this short bilingual reader a book-like page count and reading measure. The owner approved that specification and the review package now implements it.
- **Depends on:** Gate D PASS; `PIPE-001` closed; `S6-100`; final pen name `Nina Marlo`; selected cover concept 1/background 02.
- **Generate / update:** `manifest.yaml`; `tooling/scripts/compile_book.py`; `exports/print/interior.pdf`; `exports/kdp/interior.pdf`; exact-geometry print-wrap source, preview, and single-page PDF under `exports/cover/final/`; cover notes, build evidence, and this ledger.
- **Locked inputs:** Paperback; 127×203.2 mm (5×8); black ink; cream paper; left-to-right; no interior bleed; page count taken from the rebuilt final PDF; no spine text; KDP-supplied barcode area reserved.
- **Acceptance criteria:**
  - [x] Final interior pages are exactly 127×203.2 mm; the 81-page manuscript yields KDP's even 82-page production count.
  - [x] Every story begins on a new page; contents and split story-title hierarchy remain present.
  - [x] Wrap geometry is recalculated from the final page count using the official cream-paper factor.
  - [x] Wrap is one PDF containing back, text-free spine, and front; all live text is inside safe areas and at least 7 pt; no guides or crop marks are exported.
  - [x] Title, subtitle, and author match the approved metadata and front cover exactly; barcode placement is left for KDP.
  - [x] Interior and wrap received structural and rendered-page inspection as a review package; upload-ready status remains withheld for the background-resolution/provenance blocker below.
- **Verification / evidence:** Compiler/EPUB checks; PDF MediaBox/page-count checks; deterministic KDP geometry script; font/image inspection; raster previews and hashes.
- **Blockers / escalation:** Background 02 is only 816×1312 at native resolution and its provider/model/cost record remains incomplete. A geometrically correct review wrap may be built, but Gate E and upload-ready status stay blocked until a native ≥300-DPI replacement and provenance record exist.
- **Result:** `exports/kdp/interior.pdf` is 81 pages at 360×576 pt; KDP production count is 82. `exports/kdp/print-cover.pdf` is one 265.557×209.55 mm page with a 5.207 mm blank spine. The owner-supplied `cover-background-02-back.jpeg` now fills the back panel, and the downloaded KDP template independently confirms every trim/fold/bleed/barcode coordinate. EPUBCheck, translation alignment, geometry, page-opening, font, and rendered-preview checks pass.

</details>

## Stage 7 — Publication readiness and release

- [ ] `S7-010` Verify Gates A–E, required artifacts, disclosures, rights, metadata, prices, categories,
  author/imprint fields, reviewer signoff, and cost ceiling from repository evidence.
- [ ] `S7-020` Generate `exports/publish-runbook.md` with exact upload files, form answers, preview
  checks, rollback procedure, and post-publication verification steps.
- [ ] `S7-030` Present final GO/NO-GO and stop for HITL Gate 2; never upload or publish without explicit
  authorization.
- [ ] `S7-040` After human publication, record identifiers and links, verify storefront rendering,
  archive release evidence, and write the retrospective memory.

## Blocked work

- `S6-010` — resolved 2026-08-15. T1 title/subtitle, KDP description, no-imprint/no-series launch, and exact pen name `Nina Marlo` are owner-approved; `S6-110` independently reconfirmed the pen-name decision.
- `S6-020` — owner: `cover-director` + human cost approval. Concept 1/background 02 is selected and the exact print spread exists. Gate E still requires a native ≥300-DPI replacement plus provider/model/cost provenance.
- `PIPE-001` / `S6-030` — resolved. The bilingual assembly, aligned translations, language tagging, and exercises-at-back architecture are implemented and verified.

## Decisions needed from the human

1. `S6-020`: provide the image-source provenance required for `assets/cover-background-01.jpeg`, `cover-background-02.jpeg`, and `cover-background-02-back.jpeg`.
2. `S6-020`: accept the 816×1312 background-source caveat for the 1600×2560 composite or provide a native higher-resolution version of background 02.

## Completed-stage archive

When a stage closes, retain its task IDs and evidence links here. Do not erase failure history,
loopbacks, approvals, or replacement evidence.

---

## Production plan — drafted 2026-08-12 under owner "GO"

> Scope discipline: this is a **production** plan (what must exist, in what order).
> It is deliberately NOT the content architecture — which stories, which arc, which
> chapter contracts — because that is Stage 1's output and Stage 1 is gated behind a
> Stage-0 verdict this book does not have yet. `niche_verdict.py` currently prints
> `INCOMPLETE`. Writing the outline now would be the exact gate-jump the SQL candidate
> was stopped for.

### Gate status

- [x] Book workspace created and registered (`new-book.sh`)
- [x] Charter drafted (agent, under explicit owner delegation)
- [!] Charter **attested** — blocked on owner. `research/charter.md: owner_attested` is
      still `<name> <YYYY-MM-DD>`. Until it is filled, the charter is drafted, not attested,
      and `state.json.charter_attested` stays `false`.
- [x] `evidence.yaml` filled honestly; unmeasured fields left `UNKNOWN`
- [x] `candidates.csv` carries a provenance row per candidate
- [ ] Stage-0 verdict is `INCOMPLETE` — see blockers below

### Stage-0 blockers, in the order that actually unblocks the verdict

- [ ] **Low-star review sample.** The differentiation contract cannot be written without it,
      and it is the one input that decides whether this book has a reason to exist beyond
      "the shelf sells". Amazon review pages redirect to sign-in; ADR-008 bans evasion and
      proxies, so the lawful routes are: the owner's own logged-in browser session, or
      Goodreads editions of the same titles. **Do not** solve this with a proxy.
- [ ] **Differentiation contract** — 3 promises, each citing a specific negative review.
      Depends entirely on the item above. Currently `UNKNOWN`, deliberately not guessed.
- [ ] **Category rank-20 difficulty** in two target categories
      (`Spanish Language Instruction`, plus one of the phrasebook paths — note codex's
      caveat that a phrasebook shelf is not a reader shelf).
- [ ] **Trend direction** via trendspyg.
- [ ] **Healthy autocomplete run.** Today's collector was DEGRADED (control 7 vs ~27).
      Re-run through `tooling/scripts/niche_mine.sh`, not the raw completion endpoint.
- [ ] **Trademark screen** across classes 9 / 16 / 41 into `research/trademark.md`,
      plus the `human_signoff:` line only the owner can write.
- [ ] **Locale decision** — exactly one, cited to shelf evidence, not preference.

### The check suite — build before drafting, not after

The charter's authority claim is "machine-verified". Every unbuilt check below is a
claim the book is not yet entitled to make.

- [x] Controlled-vocabulary coverage + single-locale consistency —
      `tooling/scripts/graded_reader_check.py`, self-check green
- [ ] Source an A1 wordlist with a citable provenance and a license that permits this use
      (this gates the coverage check being *meaningful* rather than merely *running*)
- [ ] Morphology / agreement analysis (needs a real analyzer, e.g. spaCy `es_core_news_sm`)
- [ ] Sentence-ID alignment between Spanish and English parallel text
- [ ] Entailment + independent back-translation on each aligned pair
- [ ] Story-integrity checks: names, chronology, locations, comprehension answers
- [ ] CEFR-drift proxies: sentence length, clause depth, tense inventory, new-word rate
- [ ] False-cognate lint against a curated list
- [ ] Wire all of the above into one command that fails the build

### Known risks, recorded now so they are not discovered late

- **Audio.** Several comps ship an audio download. We have none. It must not be implied
  anywhere in metadata or cover copy.
- **`lang` tagging.** Pandoc metadata hardcodes `lang: en`. A bilingual interior needs the
  Spanish spans tagged, or screen readers mispronounce the entire book. This is an
  accessibility defect, not a nicety.
- **AI-content saturation.** Language learning is among the most AI-flooded KDP categories.
  KDP AI disclosure is mandatory and non-negotiable.
- **Review-manipulation smell.** The leading comp shows 0% one- and two-star across 188
  ratings. Do not model our launch on whatever produced that distribution.
- **Series economics.** Codex put Book 1 alone at roughly $30–100/month central, $0–300 band,
  35% confidence. The business case is the series; a one-off is a weak bet. Plan volume 2
  before volume 1 ships.

---

## Pipeline proof — 2026-08-12

End-to-end test: can Claude write A1 Spanish that the check suite certifies? **Yes, demonstrated.**

- Wrote `chapters/sample-story-pipeline-proof.md` ("La última mesa", 240 Spanish words, Latin
  American locale, a small ghost-story hook aimed at ADULTS — the differentiation promise).
- Ran `tooling/scripts/graded_reader_check.py`: **coverage 0.979, locale violations 0, exit 0.**
- Residual out-of-vocabulary: `tranquila, desde, madera, diferente, favor` — 5 words in 240.
  That residual IS the per-story glossary. ~98% known + a short glossed remainder is the standard
  graded-reader model, and "highlighting of possibly difficult vocabulary" is the feature reviewers
  explicitly PRAISED in the incumbent (Mikael 2021-10-05).

### What the proof exposed (all fixed, all real)

1. English frontmatter was being counted as Spanish. The checker must receive Spanish-only text.
2. Character names counted as unknown vocabulary — wrong. Added `--names`; names are not
   vocabulary burden in any graded reader.
3. The provisional wordlist was missing inflections/plurals of words already on it (`mesas`,
   `sillas`, `vuelve`). Added those. This was wordlist incompleteness, NOT lowering a threshold
   and NOT adding genuinely new words to make a check pass — that distinction is the whole point.
4. Confirmed empirically what the script's own `ponytail:` note predicted: OOV is now dominated by
   inflection, so a real lemmatizer (spaCy `es_core_news_sm`) is the correct next upgrade.

### Still required before real drafting

- [ ] **Replace `assets/wordlist-a1-provisional.txt`.** It is agent-assembled, 435 forms, with NO
      citable source or license. Every coverage number is only as trustworthy as this file. This is
      the single most important open item: the charter's authority claim rests on it.
- [ ] Lemmatizer, so inflections stop consuming the vocabulary budget.
- [ ] Delete the sample story. It is a toolchain test, not book content, and Stage 1 has not run.

---

## Codex go/no-go + wordlist resolution — 2026-08-13

**Codex verdict: NO-GO on drafting prose, GO on outlining.** Its verdict block agreed with its
prose this time (concede b / concede a / concede b), so it was used rather than discarded.

Its three findings, and what happened to each:

1. *"The wordlist blocks WRITING, not merely publishing: vocabulary is a generative constraint
   for a graded reader, and replacing it afterward could force extensive rewriting."*
   **RESOLVED.** See `assets/WORDLIST-PROVENANCE.md`.
2. *"Keyword evidence is corroborative, not strong enough to carry the GO. Verified BSR carries
   the demand case."* **ACCEPTED AS RECORDED** — `evidence.yaml` already says only ~12 of 63
   autocomplete rows are on-target. The GO rests on BSR and category rank. Do not later cite the
   raw 63 as if it were buyer intent.
3. *"The highest-risk untested assumption is that constrained, generated A1 stories can remain
   genuinely compelling to adults across a complete volume."* **OPEN — the real risk.** The
   240-word proof tested vocabulary and locale, not sustained narrative quality. This is also
   differentiation promise 1, the one promise no machine check can verify.

### Wordlist: resolved, and a self-inflicted error found

Codex recommended OpenSLR SLR21 (CC BY-SA 3.0). Tested and REJECTED on register: it is a news
crawl whose top-2000 is `crisis, guerra, mercado, muertos` and which lacks `ventana`, `silla`,
`mira`, `vieja`. It never reaches threshold even at rank 5000.

Adopted instead: **hermitdave/FrequencyWords `es_50k.txt` (OpenSubtitles-derived, MIT)**, top 2000.
Spoken register, commercially usable.

| Corpus | top-1000 | top-2000 | top-3000 | top-5000 |
|---|---:|---:|---:|---:|
| OpenSLR SLR21 (news) | 0.707 | 0.799 | — | 0.904 |
| OpenSubtitles (spoken) | 0.895 | **0.971** | 0.987 | — |

**The error worth remembering:** the earlier 0.979 was INFLATED. That wordlist was assembled by
the agent around its own story, then had the exact missing inflections added — grading its own
homework. The 0.971 above is honest: the story was written before that list existed, and the list
comes from an independent licensed corpus. Never validate a check against a list you tuned to it.

### Now unblocked

- [x] Licensed, citable, commercially usable wordlist with documented cutoff and provenance
- [x] Sample story independently validated at 0.971 / 0 locale violations
- [ ] **Stage 1 outline** — now the correct next step (codex: "outlining may begin")
- [ ] Lemmatizer, so inflections stop consuming the vocabulary budget
- [ ] An answer to risk 3: how do we know the stories are good? Proposed: hold volume 1 to
      10 stories and judge narrative quality at stage 3/4 against the rubric, treating a fail as
      a rewrite rather than a threshold change.
- [ ] Delete `chapters/sample-story-pipeline-proof.md` when real drafting starts
- [ ] Back matter must carry the MIT attribution for the wordlist

---

## Stage 1 — outline + bible (proposed 2026-08-13, awaiting HITL Gate 1)

Artifacts: `outline/outline.md`, `outline/chapter_01.md`..`chapter_10.md`,
`bible/cast.md`, `bible/places.md`, `bible/vocabulary-ledger.md`.

**Nothing below may be drafted until the owner approves the outline at Gate 1.**

| Story | Title | Grammar target | Words | Draft | Checks | Glossary | Continuity |
|---:|---|---|---:|---|---|---|---|
| 01 | La luz en el agua | present tense; ser/estar; hay | 500 | [ ] | [ ] | [ ] | [ ] |
| 02 | El pan de las cinco | questions | 550 | [ ] | [ ] | [ ] | [ ] |
| 03 | La mujer que no duerme | adjectives + agreement | 600 | [ ] | [ ] | [ ] | [ ] |
| 04 | Todos los dias lo mismo | reflexives; time expressions | 600 | [ ] | [ ] | [ ] | [ ] |
| 05 | Manana viene el barco | ir a + infinitive | 650 | [ ] | [ ] | [ ] | [ ] |
| 06 | No me gusta esperar | gustar-type verbs | 700 | [ ] | [ ] | [ ] | [ ] |
| 07 | Esta pasando algo | present progressive | 700 | [ ] | [ ] | [ ] | [ ] |
| 08 | Lo que paso en 1998 | regular preterite | 750 | [ ] | [ ] | [ ] | [ ] |
| 09 | Nadie dijo nada | irregular preterite | 800 | [ ] | [ ] | [ ] | [ ] |
| 10 | La luz, otra vez | mixed — no new grammar | 900 | [ ] | [ ] | [ ] | [ ] |

Per-story definition of done (all four boxes, in order — a later box may not be ticked first):

1. **Draft** — Spanish narrative within +/-10% of budget, contract in `outline/chapter_NN.md` obeyed.
2. **Checks** — run with the CUMULATIVE known set, or the numbers are meaningless:
   `graded_reader_check.py --wordlist assets/wordlist-es-opensubtitles-top2000.txt --text <story>
   --ledger bible/vocabulary-ledger.md --story NN
   --names "ana,beto,rosa,miguel,tomas,ferrer,delgado,ortiz,lucia,puerto,lento"
   --locale latam --max-new-types 25`
   Must return **zero locale violations**, coverage **>=0.95** (08-10: >=0.93), and **<=25** new
   types. All three are independently fatal; the exit code is the gate.
3. **Glossary** — the checker's out-of-vocabulary list IS the glossary; append it to
   `bible/vocabulary-ledger.md` and close it. <=25 new normalized surface types (NOT "words" —
   there is no lemmatizer, so `casa`/`casas` count twice).
4. **Continuity** — cast, places and established facts checked against `bible/`. Beto's tell
   ("no hay nada") appears verbatim in 01, 04 and 10.

**A failing check is a rewrite, never a threshold change.** That rule exists because this session
already produced one inflated coverage number by tuning the wordlist to the story.

### Gate 1 review by codex — 2026-08-13 — APPROVE-WITH-CHANGES, changes applied

**CORRECTION (2026-08-13, round 2).** An earlier version of this section claimed the reviewer's
verdict block contradicted its prose, here and in the 2026-08-12 review. **That claim was wrong and
the fault was ours.** In this contract `concede a` means *position A concedes, so B prevails* — we
read it as *vote for A*. Re-checked under the correct semantics, all three reviews were internally
consistent. The reviewer was reliable; our reading was not. The blocks should have been used as
written. Recorded here rather than quietly deleted, because a false reliability claim about a
reviewer is exactly the kind of thing that would otherwise propagate into the next book's decisions.

| # | Required change | Status |
|---|---|---|
| 1 | Draft Part I first, then pause and test with five human beta readers | **PARTIALLY REJECTED** — staged release adopted; beta readers are not available under the owner's standing constraint. Substitution recorded openly in `outline/outline.md`. |
| 2 | Give every chapter a local dramatic contract: goal, obstacle, turn, ending | **DONE** — all 10 contracts rewritten |
| 3 | Absorb "La última mesa" rather than deleting it | **DONE** — it is now story 03, `La mesa que nadie usa`, adapted to Ana and Puerto Lento |
| 4 | Replace the blanket "no later structure" rule with an explicit per-story allowed-grammar inventory | **DONE** — each contract lists allowed AND forbidden |
| 5 | State where the English translation appears | **DONE** — after each complete story, never interleaved |
| 6 | Fix missing Spanish accents in contract metadata | **DONE** — `días`, `Mañana`, `Está`, `pasó`, `Doña Lucía`, `Tomás` |

**The finding that mattered most**, and which the agent had not caught itself: the outline
"promises ten independently complete stories but contracts a serialized novella divided by grammar
lessons". Stories 03, 04, 06, 07 and 09 delivered information without a local turn — which is the
textbook framing the book claims to escape. Every contract now carries goal/obstacle/turn/ending
and an acceptance criterion that a reader starting there still gets a complete story.

**Engine changed.** The light-as-engine was passive and repetitive: Ana sees it, someone denies it,
repeat for ten instalments. Replaced with the letter device — a letter can be picked up, kept,
handed over or refused, so every story yields a clue, a decision and a consequence. The light
survives as atmosphere and as the story-10 payoff.

### Still open after this revision

- [ ] Prose quality remains untested and untestable in-repo. Volume 1 is short on purpose; do not
      commit to volumes 3+ until the market answers.
- [ ] Draft Part I (01–04) only, then STOP for adversarial review before Part II.
- [ ] Delete `chapters/sample-story-pipeline-proof.md` — its narrative asset has now been
      transferred to `chapter_03.md`, so the reason to keep it is gone.
- [ ] Lemmatizer still unbuilt; morphology, alignment and back-translation checks still unbuilt.


### Gate 1 review round 2 by codex — 2026-08-13 — REVISE AGAIN FIRST, revisions applied

Verdict, read correctly this time: point 1 **B prevails** (revise before drafting); point 2
**A prevails** (the letter engine is genuinely better); point 3 **A prevails** (the no-human-reader
substitution is adequate for a limited, reversible Part I experiment).

| Finding | Response |
|---|---|
| **Letter engine physically incoherent.** Story 01 finds a letter *inside the kiosk*; story 10 has Doña Lucía posting letters *into the sea*. Nothing explained how one becomes the other. "Unresolved grief may remain emotionally unresolved; the physical mechanism may not remain incoherent." | **FIXED** — `bible/letters-causal-ledger.md`. Tomás worked the kiosk before Ana. His mother leaves letters at his old post by hand — no delivery system at all — and rows out once a *year*, not monthly, to put one in the water. Every downstream question (why Ana finds them, why "for years", why the stranger knows her name) falls out of that one fact. |
| **Stories 03, 06, 07, 09 have false turns** — teasers and clue deliveries, not local closure. 04 and 08 borderline. | **FIXED** — every one now ends with something Ana learns, decides or pays for. 03 answers whose table it is; 06 gets a public answer at a social cost; 07 ends the who-question in the middle of the volume on purpose; 09 makes Ana keep both women's secrets and become the thing the town feared. |
| **Grammar inventories were newly-introduced-only, while the acceptance criterion said "only the allowed grammar above"** — which would have forbidden story 10 from using the present tense. | **FIXED** — each contract now carries the CUMULATIVE union of 01–NN as the drafting rule. |
| **Doña Lucía as Tomás's mother was hoped-for inference, never seeded.** | **FIXED** — stated by the fisherman in 03; Rosa's "esa señora" in 06. |
| **Beto's reversal was sentimental punctuation, not payoff.** | **FIXED** — he leaves because nobody in the town ever answers anything. When Ana answers something out loud and the town survives it, his reason is gone. |
| **`tasks.md` required "no hay nada" in story 10 while the ending depends on its absence.** | **FIXED** — the phrase is now forbidden in 10; its absence is the ending. |
| **`cast.md` said five named characters and listed six.** | **FIXED** — five living, plus one absent name. |
| **500–700 words may be too tight for clue + grammar + character beat + closure.** | **APPLIED** — 03, 04, 07 grew by 50–100 words. Capstone stays 900. Volume not padded for KU: "adding pages that lower completion is not an economic win." |
| **Best no-human proxy: a preregistered comparative panel** — multiple model families, blinded, pairwise against matched adult graded readers plus a deliberately juvenile negative control, thresholds set before seeing the draft. | **ADOPTED as the Part I gate.** Distinct personas on one model are "correlated simulations, not independent judges" — so the panel must span families. A high score is not evidence humans enjoyed it; it detects embarrassment, childishness and exposition. |

**Deliberately NOT answered in volume 1:** where Tomás actually went. Rosa believes he drowned;
his mother knows he walked away. That is the volume-2 hook, and the closing note states it plainly
instead of baiting the reader.

---

## Stage 2 closed — 2026-08-13. Handoff to Stage 3.

All ten stories drafted. **Vocabulary/locale gate 10/10, grammar-ladder gate 10/10, 39 repo tests
green.** Reproduce both before trusting this section; the commands are in
`bible/vocabulary-ledger.md` and the usage block of `tooling/scripts/spanish_grammar_check.py`.

### What happened in this stage, beyond drafting

Two contracts turned out to be **declared but never measured**. Both are written up in full in
`README.md` and `.agents/rules/quality-gates.md`; the short version:

1. **The lexical gate stopped being enforced.** After story 01 missed 0.95 coverage,
   `--max-new-types` was made to *suppress* the coverage failure — a threshold change wearing a
   metric change's clothes, made mid-session, exactly what `CLAUDE.md` rule 9 forbids. External
   review refused to ratify it and found the real bug: the checker never read the cumulative
   ledger, so a word taught in story 01 was charged to the reader again in 02–10. Fixed properly.
   **Thresholds were restored to the original 0.95/0.93; none was ever lowered.** Nine of ten
   stories then passed with no gate change needed.
2. **The grammar ladder was invented and enforced by nothing.** Settled against the Instituto
   Cervantes PCIC inventory, which found the ladder wrong in *both* directions. The volume was
   retitled **A2** by owner decision, all ten contracts were rebuilt with per-construct levels, and
   `tooling/scripts/spanish_grammar_check.py` now enforces the sequence.

### Prose defects fixed as a result

| Story | Defect | Fix |
|---|---|---|
| 01 | `Le gusta` ×2 — gustar belongs to story 06 | `Está bien sola` / `Ana está bien así` |
| 02 | `no va a contestar` — `ir a`+inf belongs to 05 | `Rosa no contesta` |
| 02 | `no le gusta` | `una cosa que no quiere entender` |
| 03 | `Antes es de él` — present doing a past tense's job, a **correctness** bug | `Antes, de él. Ahora, de usted.` |
| 03 | `Mientras` — simultaneity belongs to 07 | `Come y mira la mesa` |
| 03, 04 | `Escriba` — imperative, taught nowhere in the book | reworded as questions, like all 48 other prompts |

`Mientras` was found by the checker, not by reading. So was nothing else on this list — the rest
came from the PCIC audit, which is the honest way to report it.

### Open when Stage 3 starts

- [ ] **Story 01's Part I panel result is STALE.** The story was rewritten after it was judged, and
      then edited again for the staircase. Any claim about its quality is currently unevidenced.
- [ ] **Prose quality remains the real untested risk** (codex's finding 3, still open since
      2026-08-12). No machine check here speaks to whether the stories are good. This is Stage 3's
      job and it is the reason Stage 3 exists.
- [ ] `chapters/sample-story-pipeline-proof.md` still present and still not part of the book.
      **Nothing filters it** — a `chapters/*.md` glob will pick it up.
- [ ] Lemmatizer unbuilt; alignment, entailment and back-translation checks unbuilt. The charter's
      "machine-verified" claim covers vocabulary, locale and grammar sequence — **not** these.
- [ ] Pandoc `lang: en` hardcoded against a bilingual interior — an accessibility defect, due before
      export (`docs/discovery-log.md`).

### Rules that bind Stage 3

- A failing gate is a **rewrite**, never a threshold change. If moving a number would make a
  currently-failing artifact pass, stop and get an outside opinion instead.
- Any quality panel needs **independent model families** and an **unchanged calibration anchor**.
  Drift measured here reached ±1.0 per dimension on unchanged text, so without an anchor an
  improvement claim is unfalsifiable. Personas on one model are correlated simulations, not judges.
- No human beta readers, no native-speaker reviewer. Standing owner constraint. Do not propose it.
- Re-run **both** gates on any story whose Spanish changes, and resync
  `bible/vocabulary-ledger.md` — the checker reads it, so a stale glossary silently redefines what
  counts as known.

## Stage 6 — PIPE-001 closed, bilingual draft assembled — 2026-08-14

Owner ruling: the parallel-text architecture is approved and there is to be no further revision
cycle. Acted on it rather than re-opening it.

### Done

- **English parallel text exists.** `translations/NN-*.en.md`, ten files, plus
  `translations/00-english-translations.md` telling the reader to read Spanish first and naming the
  two things English cannot carry (*usted*/*tú*, *doña*).
- **The alignment claim is machine-checked, not asserted.** `tooling/scripts/parallel_text_check.py`
  fails on a missing translation, a block-count mismatch against the Spanish *narrative*, an English
  file that leaked an exercise, or a Spanish source edited after translation
  (`translations/sources.sha256`). Currently `OK: 10 chapters aligned`.
- **Exercises moved to the back.** Closes the last OPEN COMMERCIAL drift item — the Look Inside
  sample now opens on story text, not a quiz. No exercise was cut; `exercises.md` explains the move
  to the reader in Spanish, and states on purpose that there is no answer key.
- **Screen readers get the language right.** `compile_book.py` wraps every Spanish section in
  `::: {lang=es}` (new `source_language: es` in `manifest.yaml`). Without it a bilingual interior is
  read end to end in an English voice.
- **A placeholder that had already shipped into an interior is now impossible.** `resolved()` treats
  `<like-this>` as unfilled, and the compiler prefers `exports/metadata.json` `human_selection` over
  the frozen manifest fields — so the approved title reaches the page without touching the
  metadata lock.
- `exports/metadata.json` `claim_boundary`: parallel text moved from prohibited to allowed, worded
  as AI-generated and disclosed; "human/professionally translated" added to prohibited.

### Not done, and not to be reported as done

- **Semantic verification of the translations is the owner's read.** Mechanical parity is not
  meaning. Nothing in this stage checked that story 7's English says what story 7's Spanish says.
- **Gate E is UNRUN.** pandoc is not installed on this machine, so no EPUB, no epubcheck, no
  `interior.pdf`. `exports/master.md` (15,696 words) is the reviewable artefact until it is.
- `exports/blurbs.md` line 5 still disclaims "English translation/parallel text". That copy is
  owner-locked as of 2026-08-14 and is now factually wrong. Flagged, deliberately not rewritten.
- `manifest.yaml` `title`/`subtitle`/`pen_name` remain frozen pending the fresh final-mark screen and
  second sign-off. `© 2026` currently carries no name because no pen name is approved.

## Stage 6 — review package built; export checks pass — 2026-08-14

Owner instruction, verbatim: *"please generate the book so I can review it during your work."*

pandoc 3.10.2 installed; the compile that has been dying at `FileNotFoundError: 'pandoc'` now runs end to end.

### Done, with evidence

- **Export-format checks pass.** EPUBCheck against EPUB 3.3 rules: `0 fatals / 0 errors /
  0 warnings / 0 infos`; both PDFs render. Full Gate E is still `FAIL` because the repository
  gate additionally requires an originality check and a complete compliance record. Originality
  is unrun, and the cover background's provider/model/cost are unrecorded.
- **Artifacts built** (hashes in `compliance_log.yaml`, logged by `compile_book.py log_event`):
  | artifact | sha256 (first 16) | geometry |
  |---|---|---|
  | `exports/master.epub` | `85911099cb6ec465` | embedded 1600×2560 cover |
  | `exports/print/interior.pdf` | `917d43f1f2d122fe` | 65 pp, 432×648 pt = 6×9 in exactly |
  | `exports/direct/reader.pdf` | `fc10e54de25da09b` | 50 pp, US Letter |
  mirrored into `exports/kdp/`; the cover JPEG is packaged separately too.
- **Accessibility defect found and fixed — by inspecting the built EPUB, not by Gate E.** The first
  build carried `lang="es"` on the 21 Spanish sections and `xml:lang="es"` on **zero**. EPUB XHTML is
  parsed as XML, where `xml:lang` is the attribute that governs, so a reading system could still have
  narrated ten Spanish stories in an English voice. epubcheck reported no warnings either way.
  Pandoc now renders each `lang=es` fenced div as both attributes; rebuild carries 21 of each.
  Formatter and graded-reader regression checks: `15 passed`.
- **Cover title restyled** on owner instruction; see `exports/cover/cover-notes.md` for the measured
  extents and the four new hashes.

### Not done, and not to be reported as done

- **Semantic verification of the ten translations is the owner's read.** The gate proves block-count
  parity and source freshness. It proves nothing about meaning.
- **65 pages forbids spine text.** KDP requires 79+ pages before any text may sit on a paperback spine.
  The spine is a rule, colour, and nothing else — or the interior gains pages.
- **The interior has no copyright page.** On the `generated` track `frontmatter_for_track()` emits the
  AI Disclosure instead. Coupled to the pen-name decision: no approved name, no copyright line to write.
- **Interior and cover disagree about the author.** The interior byline is omitted
  (`NOTICE: no approved author/pen name`); the cover prints `NINA MARLOW`. One of the two must move.
- **`exports/blurbs.md` line 5 is now false** — it still disclaims "English translation/parallel text".
  Owner-locked, so flagged rather than rewritten.
- **Background 02 provider/model/cost still unlogged**, and its 816×1312 native size is below the
  ≥1800×2700 a 6×9 print wrap needs at 300 dpi.

## Stage 6 — disclosure removal and story-opening redesign — 2026-08-15

### `S6-050` — remove reader-facing disclosure and redesign PDF story openings `[x]`

- **Owner:** `formatter-platform`, on explicit human-owner instruction.
- **Why:** The review PDFs exposed an undifferentiated `Story N — Title` treatment, and the owner
  chose not to place AI disclosure prose inside the reader-facing book.
- **Depends on:** Existing bilingual assembly and passing translation alignment gate.
- **Generate / update:** `tooling/scripts/compile_book.py`,
  `tooling/latex/story-heading-style.tex`, `tooling/pandoc/story-headings.lua`, generated
  frontmatter and export packages, `exports/build-report.md`, and the Stage-6 ledger/state record.
- **Procedure:** Omit disclosure prose from generated-track frontmatter; preserve the internal
  compliance trail; split localized `Historia N` / `Story N` labels from titles during PDF
  conversion; rebuild both PDF variants and the EPUB.
- **Acceptance criteria:** No reader-facing export contains an AI-disclosure page; story labels are
  visibly smaller and stylistically distinct from their titles; full headings remain in navigation;
  EPUBCheck exits zero; both PDFs render at their prior target geometry.
- **Verification / evidence:** `pytest -q tests/test_compile_book_guard.py` → 3 passed; compiler
  completed for ten aligned chapters; EPUBCheck 5.3.0 → zero findings; Ghostscript raster review of
  print pages 1 and 26 confirmed the Spanish and English two-level openings; output geometry remains
  65 pages at 6×9 in and 50 pages at US Letter. `rg` found no disclosure phrase in
  `frontmatter.md` or `exports/master.md`.
- **Blockers / escalation:** Reader-facing removal is complete. The private append-only provenance
  record and truthful KDP upload disclosure are retained. On 2026-08-15 the owner deliberately
  amended Gate E to separate those private answers from reader-facing copy, resolving the former
  `READER-DISCLOSURE-OWNER-OVERRIDE` blocker.

### `S6-060` — restore contents and story-opening pagination `[x]`

- **Owner:** `formatter-platform`, on explicit human-owner instruction.
- **Why:** The review PDF lost its populated contents page, stories no longer reliably begin on a
  fresh page, and the story-title treatment needs more breathing room before body text.
- **Generate / update:** Compiler story-opening markers, Pandoc heading filter, shared PDF heading
  styles, EPUB CSS, rebuilt exports, and the Stage-6 evidence record.
- **Acceptance criteria:** The PDF contents lists all Spanish and English stories; each of the 20
  narrative story openings starts on a new page; exercise headings do not force page breaks; title
  spacing is visibly increased; EPUBCheck and PDF render checks pass.
- **Verification / evidence:** Final contents contains the 10 Spanish and 10 English story entries
  exactly once, plus the English and exercise section dividers; repetitive exercise labels are
  unlisted. Ghostscript per-page extraction found 20/20 story openings at page tops in both PDFs.
  Raster review confirmed the increased title-to-body gap. EPUBCheck reported zero findings,
  Ghostscript parsed both PDFs with `PDFSTOPONERROR`, and the full suite passed 45/45 tests.
- **Artifacts:** `exports/print/interior.pdf` is 69 pages at exactly 6×9 in;
  `exports/direct/reader.pdf` is 63 US-Letter pages; platform mirrors were refreshed.

### `S6-070` — carry the two-level story-opening design into EPUB `[x]`

- **Owner:** `formatter-platform`, on human review feedback.
- **Why:** The valid EPUB still renders each narrative heading as one undifferentiated line even
  though the PDF separates the localized story number from the story title.
- **Generate / update:** `tooling/pandoc/story-headings.lua`, `tooling/pandoc/epub.css`, rebuilt
  EPUB/PDF packages, and Stage-6 build evidence.
- **Acceptance criteria:** EPUB story openings expose separately styled label/title spans; the
  contents retains the complete conventional heading; all 20 narrative openings keep their page
  break; EPUBCheck exits zero; PDF output does not regress.
- **Verification / evidence:** The rebuilt XHTML contains separate `story-label` and `story-title`
  spans on all 20 narrative headings; scoped EPUB CSS renders them as two levels while the nav XHTML
  retains both complete headings. EPUBCheck 5.3.0 reported zero findings; the full test suite passed
  45/45; the PDF packages remain 69 pages at 6×9 and 63 pages at US Letter.

### `S6-120` — correct back-cover outline and expose the spine `[x]`

- **Owner:** `cover-director`, on human review feedback.
- **Why:** The lower back-cover field had an unintended rectangle outline and the fold-blending
  treatment made the spine area visually unclear.
- **Generate / update:** Deterministic print-wrap renderer, SVG source, full-wrap PDF/preview,
  KDP mirror, and separate Canva-ready back PDF/PNG.
- **Acceptance criteria:** No outline around the lower field; a solid text-free 5.207 mm spine at
  the official template fold coordinates; back-only export ends at the back/spine fold.
- **Verification / evidence:** Rendered inspection confirmed the outline is gone and the spine is
  explicit. The full PDF is 752.760×594 pt; the back PDF is 369×594 pt; the back PNG is
  1538×2475 pixels; the full-wrap source and KDP mirror are byte-identical.

### `S6-130` — export the exact Canva-ready front panel `[x]`

- **Owner:** `cover-director`, on human review feedback.
- **Why:** The Canva handoff included a print-panel back PNG but omitted the matching front-panel
  PNG, forcing the owner to infer bleed geometry from the ebook cover.
- **Depends on:** `S6-120`; locked full-wrap geometry and approved front art.
- **Generate / update:** `tooling/scripts/render_print_wrap.py`,
  `exports/cover/final/front-cover-canva.pdf`, and
  `exports/cover/final/front-cover-canva-300dpi.png`.
- **Inputs:** Current one-page print wrap and official x=135.382 mm front/spine fold.
- **Procedure:** Clip the front panel from the fold through the outside bleed; export lossless PDF
  and 300-DPI PNG; inspect dimensions and rendered appearance; record hashes.
- **Acceptance criteria:** Front and back Canva assets have identical 130.175×209.55 mm panel
  geometry and 1538×2475 pixel raster dimensions; the front includes bleed and no spine pixels.
- **Verification / evidence:** `front-cover-canva.pdf` is 369×594 pt and
  `front-cover-canva-300dpi.png` is 1538×2475 pixels, exactly matching the back-panel geometry.
  Rendered inspection confirms the front is complete and contains no spine pixels. The full test
  suite passes 45/45 and `git diff --check` passes.
- **Blockers / escalation:** The original front image is 1600×2560, sufficient for this compact
  panel export; the broader provenance record remains a separate Gate-E issue.

### `S6-140` — remove the visible barcode reservation for manual placement `[x]`

- **Owner:** `cover-director`, on explicit human-owner instruction.
- **Why:** The owner will place the barcode manually in Canva and does not want a visible cream
  placeholder baked into the supplied back artwork.
- **Depends on:** `S6-120` and `S6-130`; exact KDP template geometry remains unchanged.
- **Generate / update:** Print-wrap renderer and SVG, full-wrap outputs, KDP mirror, and both
  Canva-ready panel exports.
- **Inputs:** Owner instruction and the official barcode-safe coordinates retained in production
  notes for manual placement.
- **Procedure:** Remove only the visible reservation rectangle; rebuild; inspect the back and full
  wrap; verify unchanged panel/spine geometry and output dimensions.
- **Acceptance criteria:** No visible barcode rectangle in any back/full-wrap export; the area is
  otherwise uninterrupted artwork; exact wrap and panel dimensions remain unchanged.
- **Verification / evidence:** Rendered inspection of both the back-only PNG and full-wrap preview
  confirms uninterrupted harbor artwork with no barcode box. The full PDF remains 752.760×594 pt;
  both panel PDFs remain 369×594 pt; both panel PNGs remain 1538×2475 pixels. The full suite passes
  45/45 and `git diff --check` passes.
- **Blockers / escalation:** Manual Canva assembly must still keep barcode artwork within the
  official x=73.025–123.825 mm, y=169.545–200.025 mm back-panel region.

### `S6-150` — replace panel assembly with a continuous full-wrap master `[~]`

- **Owner:** `cover-director` + human owner, on explicit owner course correction dated 2026-08-16.
- **Why:** Independently prepared front, back, and spine panels expose visible discontinuities at
  their joins and amplify normal KDP fold variance. One continuous scene removes the structural
  seam and creates a single visual source for print and Kindle.
- **Depends on:** Locked paperback contract: 5×8 in, black ink, cream paper, left-to-right,
  82 production pages; matching KDP calculator template.
- **Generate / update:** Continuous text-free wrap background, full-cover editable master,
  print-ready PDF, derived Kindle front crop, cover notes, provenance log, and final review renders.
- **Inputs:** Official full-cover dimensions 265.56×209.55 mm; spine 5.21 mm; front/back trim
  127×203.2 mm; existing approved harbor-letter concept and locked `Nina Marlo` byline.
- **Procedure:** Generate one uninterrupted landscape background; place it across the entire wrap;
  overlay front/back typography and barcode separately; omit panel seams and hard fold transitions;
  crop the approved front trim region for Kindle; validate against the template and Previewer.
- **Acceptance criteria:** Background reaches every file edge and crosses both folds continuously;
  no visible join or template artifact; all important copy remains in safe areas; barcode placement
  complies with the template; print PDF geometry matches the template; Kindle is a crop of the
  approved wrap rather than an independent redesign.
- **Verification / evidence:** Integrated the owner-selected Nano Banana Pro candidate as one
  uninterrupted image across the complete 265.56×209.55 mm canvas. Generated a clean production
  SVG, a separate review-only safe-area SVG, an exact-size one-page PDF, a 1600 px preview, and an
  exact front-trim Kindle crop. PDF geometry verifies at 752.7685×594 pt; the production SVG has no
  fold, safe-area, template, or barcode marks. Rendered review confirms continuous artwork across
  both folds and all essential text inside the downloaded template's white live areas. Test suite
  passes 45/45 and `git diff --check` passes. KDP Previewer and physical-proof review remain open.
- **Blockers / escalation:** The selected background is 1168×912 px, only about 112 effective DPI
  at full-wrap size. The composition is approved-review quality, not print-upload quality. Replace
  or upscale the same image to at least 3137×2475 px (300 DPI target) and rebuild before upload.
  Do not reuse the separate-panel Canva PDF as the print master or upload the guides SVG.

### `S6-160` — distill production failures into reusable release controls `[x]`

- **Owner:** pipeline maintainer, on explicit owner request for a pragmatic retrospective.
- **Depends on:** The complete Stage-6 edit history, KDP calculator/Previewer evidence, and proof
  request reached during this edition.
- **Generate / update:** `CLAUDE.md`; Stage-6/7 quality and compliance rules; `metadata-seo`,
  `formatter-platform`, `cover-director`, `kdp-publishing`, and `publish-checklist` skills; new-book
  state/tasks/component templates; deterministic KDP release preflight; retrospective memory.
- **Acceptance criteria:** Future books must establish component ownership and toolchain feasibility
  in Stage 1; approve golden samples before bulk export; build a continuous full wrap after final page
  count; promote exact upload candidates into a release directory; verify hashes, PDF page count and
  geometry; distinguish Previewer approval, proof request, proof pass, and publication.
- **Verification / evidence:** `.agents/memories/spanish-graded-reader-a2-production-retrospective.md`
  maps every observed failure to a reusable control. The new preflight passes the 81-page 5×8
  interior plus one-page `print-wrap.pdf`, and correctly rejects `cover-Mouhamad-Canva.pdf` because
  the local export contains three PDF pages. Modified skill packages pass `quick_validate.py`.
- **Completion note:** Controls are reusable defaults; they do not retroactively clear this book's
  Gate-E blockers or certify the file already uploaded to KDP.

### `S6-170` — reconcile the KDP draft, release candidates, and physical proof `[~]`

- **Owner:** human owner + `kdp-publishing`.
- **Depends on:** Proof request submitted from the current KDP draft; Gate E remains failed.
- **Generate / update:** `exports/release/`, `release-manifest.json`, exact upload/form record,
  physical-proof checklist/evidence, `state.json`, and final publish runbook.
- **Acceptance criteria:** The exact interior and cover bytes used for the approved edition are
  identified by hash; cover is a one-page PDF at the calculator dimensions; identity metadata and
  KDP fields agree; originality/provenance/resolution blockers close; the received proof is inspected
  or an explicit owner waiver is recorded; any resulting rebuild receives a fresh Previewer pass.
- **Verification / evidence:** KDP Previewer displayed the complete 81-page interior and continuous
  wrap, and KDP accepted a proof request. This proves neither which local file hash was uploaded nor
  physical print quality. Local preflight currently rejects `cover-Mouhamad-Canva.pdf` (three pages)
  and passes `print-wrap.pdf` geometrically; content/provenance equivalence is still unresolved.
- **Blockers / escalation:** Await the physical proof and exact upload-file reconciliation. Do not
  publish while Gate E is failed.
