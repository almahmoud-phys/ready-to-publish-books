# Plan — grammar ladder correction

**v3.** Author: claude-opus-5, 2026-08-13. Supersedes v1 (rejected) and v2 (over-scoped).
Evidence: `grammar-gate-review-v1.md`, `pcic-ruling.md`. Tasks: `.local-tasks/grammar-gate.md`.

## What this is now

Not "build a grammar gate". That framing produced 40 tasks, most of them obstacles I invented.
The real problem is smaller and more embarrassing:

**I invented the book's grammar ladder myself, it was never checked by anything, and it is wrong
in both directions.**

The owner's ruling settles the authority question: *"we MUST follow what Instituto Cervantes
decides. we do not invent."* So the Plan Curricular del Instituto Cervantes (PCIC) is the source of
truth, and the job is to rebuild the ladder from it, fix the few places the prose genuinely breaks
its own sequence, and leave behind a small script so this cannot silently rot again.

## What the PCIC actually says

Verified by codex against the source; my own first reading was wrong on four rows because the
page serialises the A1 cell, a `|` separator, then the A2 cell.

| Construct | PCIC | Book currently |
|---|---|---|
| Present indicative | **split** — regular + `ser/estar/haber/ir` A1; common irregulars, habitual present, future-value present **A2** | treated as all-A1 |
| Basic reflexives (`sentarse`) | **A1** | deferred to story 04 |
| Basic `qué/quién/dónde` | **A1** | deferred to story 02 |
| `me gusta` | **A1** | deferred to story 06 |
| `le/les` clitics (`le gusta`) | **A2** | used in story 01 |
| `ir a` + infinitive | **A2** | story 05 |
| `estar` + gerundio | **A2** | story 07 |
| Preterite (`indefinido`) | **A2** | story 08 |
| Imperfect | **A2** | banned entirely (fine — an A1–A2 book need not teach every A2 form) |
| Imperative | **A2**; §9.3's A1 cell is empty | banned, but `Escriba` appears in stories 03/04 |
| Comparatives `más…que` | **A2** | banned |

Two honest ambiguities to adjudicate rather than assume: `cuándo` is cross-classified (A2 in §8.8,
an A1 example in §13.3), and **`mientras` does not appear on this page at all**.

## The consequence

The book is labelled A1 and contains A2 grammar in most stories. Two options, and the review ranked
them: **relabel A1–A2** (recommended — no public metadata exists yet, so this is the cheapest
moment, and stories 05–10 stay intact), or **cut all A2 material** (very high cost — stories 05,
07, 08, 09, 10 need substantial rewriting, and even 01–04 need work because PCIC puts third-person
clitics and habitual present beyond core A1).

Only a handful of edits are genuinely required either way, and only where a construct appears
*before its own declared introduction*: `le gusta` in story 01, `va a contestar` in story 02,
`Escriba` in stories 03/04, and the unrelated correctness bug `Antes es de él` in story 03.

## The checker

One stdlib file, `tooling/scripts/spanish_grammar_check.py`: a reviewed surface-form table for the
verbs actually present, a per-story policy, and a few multi-token patterns (`le`+gustar,
`ir`+`a`+infinitive, `estar`+gerundio). No spaCy, Stanza, Apertium or AnCora — the manuscript is a
closed 7,000-word world and the owner closed the dependency question.

It is **lint, not an oracle**. It catches forms and patterns; it cannot catch temporal misuse like
`mañana viene` or `Antes es de él`. That limit gets stated wherever it is cited.

## Why a script at all, given I know Spanish

Because I read story 01 about fifteen times without noticing `Le gusta` broke my own rule, or that
`Escriba` was an imperative. Not a knowledge gap — an attention gap. Checking 7,000 words against
ten rule sets is mechanical work where sustained attention fails, for me as much as for anyone.
A drafting checklist alone is not enough: it runs on the same attention channel that already
failed.

## Lesson recorded

Both gate failures this session were the same shape: **a contract nothing checks is not a
contract.** The vocabulary gate declared a coverage threshold it silently stopped enforcing; the
grammar ladder declared a sequence nothing ever enforced. Declaring a rule and measuring it are
different acts, and only the second one is real.
