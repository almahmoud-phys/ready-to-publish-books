---
chapter: 03
title: La mesa que nadie usa
promise: Hold a description in mind without translating it
builds_on: [2]
sets_up: [4]
word_budget: 650
key_claims: ["The window table was Tomás's", "Rosa keeps it set for him", "Tomás is Doña Lucía's son — stated by the fisherman, seeded for later", "Doña Lucía watches the bakery"]
sources_needed: [invented fiction only; no external sources; cast, places and bible/letters-causal-ledger.md]
---

# Story 03 — La mesa que nadie usa

## Reader promise

Hold a description in mind without translating it.

## Local dramatic contract

- **Goal:** Ana wants to sit down and eat at the one free table in a full bakery.
- **Obstacle:** Rosa will not let her use it — the table by the window is always set and always empty.
- **Turn:** An old fisherman sits at it anyway, orders 'un café, como siempre', and calls Ana by name though she has never met him. When she asks how he knows her, he says: 'Usted tiene el trabajo del hijo de Lucía.'
- **Ending:** LOCAL CLOSURE: Ana now knows whose job she has and whose son he was. The table is Tomás's table. Rosa keeps it set. Ana sits somewhere else — and, at the edge of the window, Doña Lucía is standing outside looking in.

**Local-closure test:** a reader who starts here and reads nothing else must finish this story with
a question answered, not merely a new question raised. Round 2 of the Gate 1 review rejected 03,
06, 07 and 09 for failing exactly this — "an acceptance criterion cannot make an unresolved episode
complete." Each now ends with something Ana learns, decides, or pays for.

## Grammar

> **Rebuilt 2026-08-13 from the Instituto Cervantes PCIC A1–A2 inventory**
> (`_planning/pcic-ladder-table.md`; source read by codex `gpt-5.6-sol`). The previous ladder was
> written by the agent, never checked against any external source, and wrong in **both** directions:
> it banned A1 material (basic reflexives, basic question words) and taught A2 material as if it
> were A1. Every construct below now carries its PCIC level.
>
> The volume is an **A2 reader** (see the `constitution.md` amendment log). This ladder therefore
> sequences *when* each construct arrives; it no longer claims an A1 band the manuscript never had.
> A level tag is a classification, not a permission — the sequence is what the book promises.

**Introduced in this story:**
adjectives and agreement; descriptive `ser` vs `estar`; `tener` expressions; basic reflexives — all **[A1]**

**Allowed in this story — the CUMULATIVE union of stories 01–03:**
- 01: present indicative — regular -ar/-er/-ir **[A1]**; `ser`, `estar`, `hay`, `ir` **[A1]**; articles
  **[A1]**; plus the high-frequency irregular and stem-changing verbs narrative Spanish cannot avoid:
  `tener`, `decir`, `hacer`, `poner`, `poder`, `querer`, `saber`, `venir`, `salir`, `volver`,
  `cerrar`, `conocer`, `pensar` **[A2]**; third-person object clitics including enclitic
  (`la pone`, `dejarla`) **[A2]**; basic interrogatives `qué`, `quién`, `dónde`, `cómo`
  **[A1]** — story 01's dialogue uses them, and PCIC puts them at A1
- 02: interrogative `cuándo` **[unlevelled — see below]**; `por qué` **[A1]**. The basic
  question words moved to story 01, where the prose actually introduces them
- 03: adjectives and agreement **[A1]**; descriptive `ser` vs `estar` **[A1]**; `tener` expressions
  **[A1]**; basic reflexives — `sentarse`, `levantarse` **[A1]**

The cumulative list is the drafting rule: a construct introduced in story 03 is still
available in story 09. The earlier contract listed only *newly* introduced structures while
its acceptance criterion said "only the allowed grammar above" — which would have forbidden
story 10 from using the present tense. That was a contract defect, not a style note.

**Not yet available:** anything not in the cumulative list above — in particular the imperfect,
comparatives (`más… que`) and any subjunctive, none of which volume 1 teaches. The **imperative**
is also absent by design: PCIC puts it at A2 with an empty A1 cell, and the two `Escriba` exercise
prompts that used it were removed on 2026-08-13, leaving every prompt in the book a question.

**Two constructs PCIC cannot level — decided here, not assumed:**
- **`cuándo`** — the source page cross-classifies it: A2 under §8.8, but §13.3 gives an A1
  direct-question example. *Decision: allowed from story 02, as a direct question only, never as a
  subordinator* — that is exactly the shape §13.3 exemplifies.
- **`mientras`** — **does not appear on the PCIC A1–A2 page at all**, so no level is derivable from
  this source. *Decision: allowed from story 07*, where simultaneity is the story's whole point.

Both are **house decisions recorded as such**. A checker must never report either as a PCIC-backed
rule, because the source does not support one.

## Continuity facts this story establishes

- The window table was Tomás's
- Rosa keeps it set for him
- Tomás is Doña Lucía's son — stated by the fisherman, seeded for later
- Doña Lucía watches the bakery

## Acceptance criteria

- [ ] Spanish narrative within ±10% of 650 words
- [ ] Goal, obstacle, turn and ending all present, in that order
- [ ] Passes the local-closure test above
- [ ] `graded_reader_check.py --locale latam` — **zero** locale violations
- [ ] **Gate L1** occurrence coverage ≥95% (stories 08–10: ≥93%) against
      `assets/wordlist-es-opensubtitles-top2000.txt` **plus the cumulative known set** —
      names, and every type closed in EARLIER stories per `bible/vocabulary-ledger.md`.
      Run with `--ledger bible/vocabulary-ledger.md --story NN`.
- [ ] Only grammar from the cumulative list; nothing from "not yet available"
- [ ] **Gate L2** ≤25 new *normalized surface types* (not words, not lexemes — no
      lemmatizer yet); all appended to `bible/vocabulary-ledger.md`.
      L1 and L2 are INDEPENDENTLY fatal: neither may disable the other
      (`.agents/rules/quality-gates.md`, Gate L).
- [ ] Obeys `bible/letters-causal-ledger.md` — no letter may move by an unexplained route
- [ ] No talking animals, no primer register, no teacher-voice
