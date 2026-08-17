# Tasks — grammar ladder correction

Plan: `_planning/grammar-gate.md`. Evidence: `_planning/grammar-gate-review-v1.md`,
`_planning/pcic-ruling.md`.

**Authority: the Plan Curricular del Instituto Cervantes (PCIC). We follow it. We do not invent.**
(Owner instruction, 2026-08-13: "we MUST follow what Instituto Cervantes decides. we do not invent.")

This list was cut from 40 tasks to 14. The deleted ones are recorded at the bottom so nobody
re-adds them. They were obstacles I manufactured, not requirements.

---

## The one decision for the owner

- [ ] **D1 — Level label.** The book is titled A1. Per PCIC it contains A2 grammar in stories
      02, 04, 05, 06, 07, 08, 09, 10 (preterite, `ir a` + infinitive, `estar` + gerundio,
      `le` clitics, imperative, habitual present). Choose:
      - **(a) Relabel A1–A2** — recommended. No public metadata exists yet, so this is the
        cheapest possible moment. Stories 05–10 stay intact. Cost: title, subtitle, blurb, plus
        the small boundary edits in T3.
      - **(b) Stay strictly A1** — rejected by review as very high cost: stories 05, 07, 08, 09,
        10 need substantial rewriting, 06's dialogue changes heavily, and even 01–04 need work
        because PCIC puts third-person clitics and habitual present beyond core A1.
      **DoD:** decision recorded in `constitution.md` amendment log.

---

## Phase 1 — Get the facts right (no code)

- [ ] **T1.1** Build a targeted PCIC table covering **only** the constructs this book actually uses
      or bans. Not the whole inventory.
      **DoD:** `_planning/pcic-ladder-table.md`, one row per construct, A1/A2 + source URL.
      Must record the two genuine ambiguities: `cuándo` is cross-classified (A2 in §8.8, A1 example
      in §13.3), and **`mientras` does not appear on this page at all** — it cannot be assigned a
      level from this source.
- [ ] **T1.2** Re-audit all ten stories against T1.1. My previous violation lists were wrong twice:
      once stale, once based on a misread of the PCIC columns.
      **DoD:** one table, story × construct × PCIC level × verdict, each with a grep command.

## Phase 2 — Fix the contracts

- [ ] **T2.1** Rewrite the grammar section of all ten `outline/chapter_NN.md` from the PCIC table.
      The current ladder is invented and wrong in both directions — it bans A1 material
      (basic reflexives, basic question words) and teaches A2 material as if it were A1.
      **DoD:** every construct in every contract carries its PCIC level.
- [ ] **T2.2** Fix story 09's contract: it names third-person forms (`dijo`, `pudo`) while the prose
      uses `dije`, `pude`. Decide lemma-licensing vs form-licensing, once.
      **DoD:** contract and prose agree.
- [ ] **T2.3** Record the two ambiguous constructs as explicitly adjudicated, not silently assumed.
      **DoD:** `cuándo` and `mientras` each carry a written decision and a reason.

## Phase 3 — Real boundary edits

Only where a construct appears **before its own declared introduction**. Nothing else.

- [ ] **T3.1** Story 01: `Le gusta estar sola` / `A Ana le gusta así` → first-person `me gusta`
      (A1) or recast. The `le` is what makes it A2.
      **DoD:** grep for `le gusta` in story 01 returns 0.
- [ ] **T3.2** Story 02: `no va a contestar` → simple present, if A2 starts later than story 02.
      **DoD:** resolved per the corrected ladder.
- [ ] **T3.3** Stories 03 and 04: remove the imperative `Escriba tres cosas` from the exercises.
      PCIC puts the imperative at A2 and §9.3's A1 cell is empty. The preceding question works
      without it.
      **DoD:** grep for `Escriba` across all chapters returns 0.
- [ ] **T3.4** Story 03: fix `Antes es de él`. This is a **correctness** defect (present tense doing
      a past tense's job), independent of level.
      **DoD:** line rewritten.
- [ ] **T3.5** Re-run the vocabulary gate on every story whose text changed; rebuild the ledger.
      **DoD:** all ten still pass 0.95/0.93 cumulative.

## Phase 4 — The small checker

One file, stdlib only. No spaCy, no Stanza, no Apertium, no AnCora. The owner closed this question
and the review confirmed nothing more is needed for a closed 7,000-word manuscript.

- [ ] **T4.1** `tooling/scripts/spanish_grammar_check.py`: a reviewed surface-form table for the
      verbs actually present, a per-story policy, and multi-token patterns for `le`/`les` + gustar,
      `ir` + `a` + infinitive, `estar` + gerundio.
      **DoD:** flags `Le gusta` in story 01 and `Escriba` in story 03 — the two real misses.
- [ ] **T4.2** Scan **all learner-facing Spanish**, exercises included. Exclude only
      `chapters/sample-story-pipeline-proof.md`, which is not part of the book.
      **DoD:** asserted in a test.
- [ ] **T4.3** Unknown verb forms **fail**, never silently pass. Ambiguous forms (`toma` as
      imperative vs 3sg present) are reported for manual review, not auto-failed.
      **DoD:** fixture for each behaviour.
- [ ] **T4.4** A handful of regression fixtures — the known violations plus a few contrastive pairs.
      Not an exhaustive paradigm corpus.
      **DoD:** `pytest` green.
- [ ] **T4.5** Run on all ten chapters; fix what it finds; re-run T3.5.
      **DoD:** exit 0 for all ten; report saved under `books/<slug>/audits/`.

## Later, not now

- [ ] **T5.1** `chapter-writer` skill quotes the licensed constructs into each drafting brief.
      Prevention, not a publication blocker.
- [ ] **T5.2** Run the checker on the assembled export once stage 6 creates one.

---

## Deleted — manufactured obstacles, do not re-add

Named by review as invented rather than required:

- The marketing/false-advertising gate. `niche.md` is an internal note; no blurb exists yet.
- The dependency debate, the spaCy comparison, and its ADR. Owner closed it.
- "Does the gate read exercises" as an *owner* decision. It isn't one — scan everything.
- Manuscript hashing as a prerequisite. Git revision plus the report identifies the input.
- JSON canonical ladder + Markdown rendering machinery. Unnecessary for one book.
- A task to prove an unimplemented idea is absent.
- Extracting the *entire* PCIC A1–A2 inventory.
- Proof-grade ambiguity policy — inherited from the withdrawn "mechanically proven" premise.
- `VerbForm=Fin` / UD machinery. Irrelevant with no UD analyzer.
- Missing-resource degradation. The table is self-contained.
- Generated paradigm corpus and AnCora benchmarking. Research projects, not requirements.
- Exhaustive mutation testing across every rule × boundary × story.
- Checking an export that does not exist.
- Re-running the quality panel after label or contract edits.
- A globally institutionalised "Gate G" with measured precision thresholds, plus `CLAUDE.md` and
  schema changes. Premature for one Spanish book.
- Adding a slogan to `model-routing.md`.

## Known limit — state it, don't imply it away

The checker is **lint, not an oracle**. It catches forms and patterns. It cannot catch temporal
misuse: `mañana viene` and `Antes es de él` pass any form-based check. Say so wherever it is cited.
