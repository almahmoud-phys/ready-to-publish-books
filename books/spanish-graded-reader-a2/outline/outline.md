# Book Architecture — Spanish A2 Graded Reader, Volume 1

> **Level, corrected 2026-08-13.** This volume was titled A1 on a grammar ladder I invented and
> nothing ever enforced. Measured against the Instituto Cervantes PCIC inventory
> (`_planning/pcic-ladder-table.md`), A2 grammar appears in **all ten stories** — so the label
> moved to match the manuscript, and the manuscript was not cut to fit the label. The vocabulary
> control (Gate L) is unchanged and still machine-measured. See the `constitution.md` amendment log.

## Control metadata

- **Status:** APPROVED by delegation 2026-08-13 (see `.agents/rules/owner-identity.md`)
- **Outline version:** 1.2 (round-2 Gate 1 revisions applied)
- **Based on niche evidence version/date:** `research/niche.md`, 2026-08-13 (verdict GO)
- **Constitution version:** as created 2026-08-12, unamended
- **Track:** generated (locked at Gate 1 per ADR-002; already set in manifest to match the charter)
- **Prepared by:** agent, under the owner's standing authorization (`.agents/rules/owner-identity.md`)
- **Human approval:** delegated — the owner does not read Spanish and cannot judge this artifact.
  Substituted by two independent codex review rounds (2026-08-13), all required changes applied
  or rejected in writing. Recorded as cleared-by-delegation, NOT as owner-approved.

## Reader transformation

- **Starting state:** Finished a beginner app or course. Recognises common words and can point at a
  conjugation table. Has never finished anything written in Spanish.
- **Persistent problem:** Reads by decoding — stops at every unknown word, translates the sentence,
  loses the thread, and concludes they are "bad at languages". The failure is stamina, not vocabulary.
- **Ending capability:** Reads a ~900-word Spanish story straight through, for meaning, without
  stopping — and can say what happened, in Spanish, in a sentence or two.
- **Proof of transformation:** Story 10 is the capstone: the longest text, no new grammar, and its
  comprehension questions ask *why* characters acted, not *what* the words meant. A reader who
  answers those has stopped decoding.
- **Explicit non-reader:** children, classrooms, absolute beginners, heritage speakers wanting
  literary Spanish, and exam candidates.

## Thesis and differentiation

- **One-sentence thesis:** An adult learns to read Spanish by finishing something worth finishing,
  not by understanding every word.
- **Book-level promise:** Ten linked stories you can actually finish, in real Latin American
  Spanish, where every sentence has been checked by a published, reproducible process.
- **Differentiation promises** (from `research/niche.md`, each cited to a dated review):
  1. Stories written for adults — no talking animals, no primer register, no textbook framing.
  2. One declared Latin American locale, enforced mechanically throughout.
  3. Every Spanish sentence passes a published check before it ships.
- **Scope exclusions inherited from the constitution/charter:** no claim of native or near-native
  fluency; no teaching credential; no personal learning story; no promised fluency timeframe; no
  medical/legal/financial/emergency Spanish; no children's pedagogy; no pronunciation or audio
  authority; **no claim of CEFR certification** — our baseline is a frequency proxy.
- **Claims requiring external authority or named review:** none asserted. The book makes no
  pedagogical claim beyond citing public extensive-reading research in the introduction.

## Locale decision (charter required this be cited, not preferred)

**Mexican-neutral Latin American Spanish.** Evidence: Shawn's 2019-08-05 review of the trade
incumbent — peninsular Spanish sold to a US audience whose real exposure is Mexican/Central
American. Enforced by `graded_reader_check.py --locale latam`: any `vosotros`/`vuestro` fails the
build. Regionalisms narrower than "widely understood across Latin America" are excluded, because
the charter forbids claiming regional authenticity beyond the declared locale.

## Spine narrative

The book opens in a single small coastal town and never leaves it. That is a deliberate
constraint, not a limitation: one setting means the reader re-meets the same nouns — *el puerto*,
*la panadería*, *la lancha* — story after story, so vocabulary compounds instead of resetting. The
comps' most common structural failure is ten disconnected vignettes; a reader who finishes story 3
has no reason to open story 4.

Here, a thread runs underneath. In story 1 Ana finds a letter left in her kiosk, addressed to a man
nobody will admit to knowing. Each story delivers a tangible clue, a decision and a consequence:
the name, the empty table, the broken routine, the boat, the years of letters, the figure leaving
the shed, two accounts of 1998 that prove compatible — and, almost a year after the opening, Ana
rows out to the next annual light and finds an entirely ordinary explanation that resolves nothing
that matters.

**Revised at Gate 1.** The first version of this spine made the light itself the engine: Ana sees
it, someone denies it, repeat. The review called that passive and repetitive, and it was — a book
that postpones its only question for ten instalments. The letter device replaces it because a
letter can be picked up, read, kept, handed over or refused. The light survives as atmosphere and
as the story-10 payoff, which is what it was always good for.

The reader's *narrative* reason to continue and their *pedagogical* reason to continue are the
same reason. That is part of the mechanism behind differentiation promise 1 — but only part, and
the outline no longer claims otherwise: structure supplies connective tissue, not voice.

Grammar advances underneath the plot, never announced in it. Present tense carries stories 1–4;
near future and progressive arrive when the plot needs anticipation and simultaneity; the past
tense arrives in story 8 exactly when a character finally tells someone what happened years ago.
Grammar is introduced because the story needs it, which is the opposite of a textbook.

## Hierarchy and promise chain

### Part I — "I can read a whole page" (stories 1–4)

**Part purpose:** convert decoding into reading. **Entry capability:** knows isolated words.
**Exit capability:** reads 550 words of present-tense Spanish without stopping.
**Why it comes here:** stamina must be built before grammar is added, or the reader quits.

| Ch. | Assertion-style title | Reader promise | Builds on | Sets up | Proof / exercise | Words |
|---:|---|---|---|---|---|---:|
| 01 | La carta sin dueño | Read 550 words of present-tense narration without stopping | — | 02 | 5 comprehension Qs, in Spanish, answerable from the text | 550 |
| 02 | El pan de las cinco | Follow a conversation carried by questions | 01 | 03 | Reorder 6 events; answer 5 Qs | 650 |
| 03 | La mesa que nadie usa | Hold a description in mind without translating it | 02 | 04 | Match 8 descriptions to 4 characters | 650 |
| 04 | Todos los días lo mismo | Track a daily routine and notice what breaks it | 03 | 05 | Spot 3 changes from the established routine | 650 |

### Part II — "I can follow time" (stories 5–7)

**Part purpose:** add anticipation and simultaneity. **Entry:** present tense fluent.
**Exit:** reads across three time frames. **Why here:** plot now needs a future to worry about.

| Ch. | Assertion-style title | Reader promise | Builds on | Sets up | Proof / exercise | Words |
|---:|---|---|---|---|---|---:|
| 05 | Mañana viene el barco | Understand plans and predictions (`ir a` + infinitive) | 04 | 06 | Separate 8 statements into happening-now vs going-to-happen | 650 |
| 06 | No me gusta esperar | Read opinions and reactions (`gustar`-type verbs) | 05 | 07 | Attribute 6 opinions to the right character | 700 |
| 07 | Está pasando algo | Follow two things happening at once (progressive) | 06 | 08 | Build a 2-column timeline of simultaneous action | 750 |

### Part III — "I can read a story that happened" (stories 8–10)

**Part purpose:** unlock the past, then pay off the thread. **Entry:** three present-time frames.
**Exit:** reads mixed-tense narrative and answers *why*, not *what*.

| Ch. | Assertion-style title | Reader promise | Builds on | Sets up | Proof / exercise | Words |
|---:|---|---|---|---|---|---:|
| 08 | Lo que pasó en 1998 | Read a story told in the past (regular preterite) | 07 | 09 | Sort 8 events into then vs now | 750 |
| 09 | Nadie dijo nada | Read the past with irregular verbs (`fue`, `tuvo`, `dijo`) | 08 | 10 | Answer 6 Qs requiring inference, not lookup | 800 |
| 10 | La luz, otra vez | Read a full mixed-tense story and explain why people acted | 09 | — | Capstone: 8 Qs, at least 4 asking *why*; write 2 sentences in Spanish | 900 |

**Every row above also carries a local dramatic contract** — goal, obstacle, turn, ending — in its
`chapter_NN.md`. That was added at Gate 1: the reviewer found the outline "promises ten
independently complete stories but contracts a serialized novella divided by grammar lessons",
which was true of stories 03, 04, 06, 07 and 09. A story that only delivers information is the
textbook framing this book claims to escape.

**Total Spanish narrative: 7,000 words.** With English parallel text, glossaries, comprehension
questions and answer keys, front and back matter, the volume lands near the manifest's 20,000-word
target. That is deliberately short: both verified comps are short, and padding a graded reader breaks
the level rather than adding value.

## The letters — physical causality

`bible/letters-causal-ledger.md` is binding. Tomás Ferrer worked the kiosk before Ana; his mother
leaves letters at his old post by hand, monthly, and rows out once a year with a lamp to put one in
the sea. There is no delivery system and no carrier. Round 2 of the Gate 1 review found the
previous version incoherent on exactly this point, and it was right.

## Dependency map

- **Strictly sequential:** the grammar ladder (01→10). No story may use a structure introduced later.
- **Strictly sequential:** the letter thread — 01 introduces, 04 and 07 complicate, 10 resolves.
  Lucía's annual lamp appears in 01 and then again after the explicit near-year jump into 10; Story
  07 uses an ordinary boat light, not the annual ritual.
- **Parallelisable:** English parallel text, glossaries, and comprehension questions for any story
  may be produced once that story's Spanish is frozen.
- **Shared assets:** one cast list, one place list, one cumulative vocabulary ledger. All three live
  in `bible/` and every story reads them. The cumulative ledger is what makes `builds_on` real
  rather than decorative.
- **Hard constraint:** no story may be drafted before `bible/` exists, or the cast and vocabulary
  will drift and continuity-keeper will have nothing to check against.

## Learning and difficulty progression

Word count climbs 500 → 900. New words per story are capped at ~25 and every one is glossed at
first use; a word glossed once is thereafter assumed known and enters the cumulative ledger.
Sentence length grows from ~8 words to ~14. Comprehension questions move from retrieval ("¿Dónde
trabaja Marta?") to inference ("¿Por qué no dice nada?") — by story 9 at least half require
inference, which is the actual test of reading rather than decoding. Repetition is deliberate:
core nouns recur across stories by design, not by accident.

## Example / dataset / asset architecture

- **Vocabulary baseline:** `assets/wordlist-es-opensubtitles-top2000.txt` (MIT, OpenSubtitles-derived).
- **Coverage target (Gate L1):** ≥95% of tokens known, per story, measured against the
  **cumulative** known set — baseline + `--names` + every type closed in EARLIER stories
  (`bible/vocabulary-ledger.md`, read via `--ledger`/`--story`). A word taught in story 01 is
  known in story 02; measuring every story against the baseline alone contradicts this book's own
  cumulative-ledger pedagogy and was a real defect, corrected 2026-08-13.
  Stories 8–10 may fall to 93% as the preterite arrives; that is a planned, recorded exception,
  not a moved threshold.
- **Glossary budget (Gate L2):** ≤25 new *normalized surface types* per story. L1 and L2 are
  independently fatal — neither may disable the other. One unknown word repeated 300 times is a
  single type and would sail through L2 while destroying the reading experience; L1 is what
  catches it. See `.agents/rules/quality-gates.md`, Gate L.
- **Word budgets amended 2026-08-13:** story 01 → 550, story 02 → 650. Story 01 stays the
  shortest on purpose: nothing is pre-taught there, so it carries the heaviest vocabulary load and
  must still feel easy. The broad 550→900 progression is retained; the original 500→550→650
  micro-staircase was never validated.
- **Locale gate:** zero violations, every story, no exceptions.
- **English translation placement: AFTER each complete Spanish story, never sentence-by-sentence
  and never side-by-side.** Interleaving would rehearse exactly the decode-then-translate habit
  the book exists to break. The buyer-language row `spanish stories with english translation`
  means translations must be present and findable — it does not mean they must be adjacent.
- **No audio.** Comps ship it; we do not have it and must never imply it in metadata or cover copy.
- **Language tagging:** Spanish spans need explicit `lang="es"` before export — Pandoc metadata
  hardcodes `lang: en`, which would make a screen reader mispronounce the entire book.

## Evidence plan

The book asserts almost nothing factual, which is deliberate: it is fiction plus a checked
vocabulary. The only external claims live in the introduction — that reading slightly-easy text in
volume builds fluency — and those cite public extensive-reading research. Every other claim is
about our own process and is reproducible from the repository.

## Word budget

| Component | Words |
|---|---:|
| Spanish narrative (10 stories) | 7,000 |
| English parallel text | ~7,000 |
| Glossaries (10 × ~25 entries) | ~1,500 |
| Comprehension questions + answer keys | ~2,000 |
| Introduction, how-to-use, locale note, back matter, attribution | ~1,500 |
| **Total** | **~19,000** |

## Opening and closing contracts

- **Opening (first 200 words the buyer sees):** must state who the book is for, that the Spanish is
  Latin American, that stories are linked, and that nothing here requires a dictionary — and must
  do it without a single word of teacher-voice. The sample on Amazon is the sales page.
- **Closing:** the capstone, then an honest "what to read next" pointing at volume 2 (A2 — buyer
  language `spanish stories a2`, 499 results), then the MIT wordlist attribution.

## Gate A self-check

| Criterion | Status |
|---|---|
| Every chapter is a promise, not a topic label | Pass — each row states what the reader can do |
| Promise chain is ordered and dependency-linked | Pass — grammar and plot both strictly sequential |
| Word budget within sane bounds | Pass — ~18.7k against a 20k target; short by design |
| Differentiation promises traceable to evidence | Pass — all three cite dated reviews |
| Scope exclusions carried from the charter | Pass — listed above, including the CEFR exclusion |
| Assets feasible with no human/hardware dependency | Pass — text only |
| Per-chapter contracts exist | Pass — `outline/chapter_01.md` … `chapter_10.md` |

## Known risk this outline does not solve

Differentiation promise 1 — that these stories are genuinely good to an adult — **cannot be
verified by any check in this repository.** Codex named it the highest-risk untested assumption and
it is, and the Gate 1 review was blunt that structure does not fix it: "a boring serialized mystery
is still boring… the design supplies connective tissue, not voice, characterization, tension, or
sentence-level pleasure." That criticism is accepted rather than argued with.

The reviewer's proposed mitigation was five human beta readers on Part I. **That is not available:
the owner's standing constraint is that no human beta readers, native reviewers or personal
authorship will ever be supplied.** Recording the substitution honestly rather than pretending the
prescribed control was run:

- **Draft Part I (stories 01–04) first, then STOP** — the review's staged-release instinct is right
  and costs nothing. Do not release all ten into drafting.
- **Judge Part I adversarially before continuing**, at stage 3/4, against the rubric, with the
  explicit question "would an adult be embarrassed to be seen reading this?" A fail routes to
  rewrite, never to a lowered threshold.
- **Publish volume 1 and let the market answer.** With no beta readers, the first honest signal is
  the Amazon sample and early reviews. That is a slower and more expensive test, and the series
  plan should not commit to volumes 3+ until it returns.

This is a real, unclosed risk. It is the reason volume 1 is deliberately short.
