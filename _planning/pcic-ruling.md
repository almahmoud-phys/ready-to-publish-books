# PCIC ruling — which grammar is A1, which is A2

Reviewer: codex `gpt-5.6-sol` xhigh, read-only, fetched the PCIC page 2026-08-13.
Settles a factual disagreement: my earlier reading of the A1/A2 columns was **wrong on four points**.
The page serialises the A1 cell, then a `|` separator, then the A2 cell; I misattributed the column.

> **Stale paths, left stale on purpose.** On 2026-08-13 the book was retitled A2 and its directory
> renamed `books/spanish-graded-reader-a1/` → `books/spanish-graded-reader-a2/`. The report below is
> quoted verbatim, so its file links point at the old path. It was **not** rewritten: editing a
> quotation to make it look current falsifies the record. Substitute `-a2` for `-a1` when following
> any link. The same applies to `grammar-gate-review-v1.md`.

```
--- provider final report ---
The central factual verdict is clear: the earlier classification of the imperfect, preterite, and imperative as A2 was correct. The owner’s column reading was wrong on those three—and also on basic reflexives.

## 1. PCIC fact settled

I checked the PCIC page directly, accessed 2026-08-13. Its tables serialize the A1 cell first, then a `|` separator, then the A2 cell. The decisive headings include “Tiempos verbales de indicativo,” “El imperativo,” “Pronombres átonos de OI: serie me, te, le,” “Los interrogativos,” “Valores de se,” and “El núcleo.” [Official PCIC A1–A2 grammar inventory](https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/02_gramatica_inventario_a1-a2.htm).

| Grammar point | PCIC result | Verdict |
|---|---|---|
| Present indicative | **Split**: core regular present plus `ser`, `estar`, `haber`, `ir`, current and durative uses are A1. Common stem/consonant irregularities, habitual present, and future-value present are A2. | “Present indicative is A1” is too broad. |
| Pretérito indefinido | **A2**, section 9.1.3, after the column separator. | Earlier review right; owner reading wrong. |
| Pretérito imperfecto | **A2**, section 9.1.2, after the separator. | Earlier review right; owner reading wrong. |
| Imperative | **A2**. Section 9.3 has an empty A1 cell; regular, irregular, and `usted/ustedes` imperatives are all in A2. | Earlier review right; `Escriba` is not A1. |
| `me gusta` / OI pronouns | **Split**. The limited first-person construction `me gusta` is A1. The broader OI system—including `te`, `le/les`, doubling and placement—is A2. | The combined row was wrong. Story 01’s `Le gusta` is A2 because of `le`, although `gustar` itself is introduced at A1. |
| `qué`, `quién`, `dónde` | **A1 in their basic uses**: basic `qué`, singular initial `quién`, and `dónde/cómo`. | Owner right; treating Story 01’s basic `¿quién...?` as non-A1 was wrong. |
| `ir a + infinitive` | **A2** as a verbal periphrasis in section 12.1. There is a narrow regional A1 entry for `voy a + infinitive` with present—not future—value. | Story 05’s future periphrasis is A2. |
| `estar + gerundio` | **A2**, under the gerund and verbal periphrases. | Owner right. |
| Reflexives such as `levantarse` | **A1** for basic reflexive `se`; the page explicitly places its reflexive examples before the separator. | Owner reading wrong. Full pronominal/clitic behavior is broader and should not all be collapsed into this entry. |
| `más... que` | **A2**, section 2.5 and the comparative-clause material. | Owner right. |

Two relevant ambiguities:

- `cuándo` is A2 under section 8.8, but section 13.3 gives an A1 direct-question example using it. The page genuinely cross-classifies it, so a checker should not pretend this is unambiguous.
- `mientras` does not appear on this A1–A2 grammar page. It cannot be assigned a level from this source alone.

Where the earlier review was wrong: it elevated house-ladder sequencing such as `¿quién?` in Story 01 and `sentarse` in Story 03 into apparent A1 violations. They violate the invented sequence, not PCIC. It also failed to distinguish A1 `me gusta` from A2 `le gusta`.

## 2. What the book should change

The best correction is: relabel the book A1–A2, rebuild the ladder from PCIC, and make a few early-story line edits so the internal staircase remains truthful. A ladder-only change is insufficient because several constructs occur before even the book’s own declared introduction point.

Minimum concrete action by story:

| Story | Required treatment |
|---|---|
| [01](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/01-la-carta-sin-dueno.md:12) | Move basic `qué/quién/dónde` and `querer + infinitive` into the early ladder. If Story 01 is meant to be the A1 band, rewrite the two `le gusta` sentences as first-person thought using `me gusta`, and simplify `Puedo dejarla` to avoid A2 clitic placement. A strict audit would also find A2 third-person object clitics, irregular present forms, and habitual present throughout this story. |
| [02](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/02-el-pan-de-las-cinco.md:83) | Replace `no va a contestar` with simple present such as `Rosa no contesta` if A2 begins later. Basic question words stay. Treat `desde cuándo` as PCIC-ambiguous, not a confident violation. |
| [03](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/03-la-mesa-que-nadie-usa.md:116) | `sentarse` may remain: basic reflexives are A1. Remove the A2 imperative `Escriba tres cosas`; the preceding question already works without it. Replace or explicitly adjudicate `mientras`, since this page does not classify it. Independently fix the incorrect `Antes es de él`; that is a correctness defect, not merely a level issue. |
| [04](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/04-todos-los-dias-lo-mismo.md:122) | Keep the reflexive routine forms. Remove the exercise imperative `Escriba`. Note that PCIC places habitual/cyclic present in A2, so the story’s daily-routine premise is A2 even though its reflexives are A1. |
| [05](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/05-manana-viene-el-barco.md:46) | Treat this as an explicit A2 transition and keep `ir a + infinitive`. If the book remains strictly A1, this story’s teaching promise needs major reconstruction. |
| [06](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/06-no-me-gusta-esperar.md:6) | Reframe the lesson: basic `me gusta` is A1, while `le/nos/te`, doubling, and the expanded psychological-verb system are A2. It works naturally as an A2 chapter. |
| [07](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/07-esta-pasando-algo.md:31) | Keep as A2. `estar + gerundio` is unambiguously A2. Do not claim a PCIC level for `mientras` from this page. |
| [08](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/08-lo-que-paso-en-1998.md:49) | Keep as A2. Regular preterite is A2. Continuing to omit the imperfect is a legitimate internal sequencing choice, but not evidence that preterite is A1. |
| [09](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/09-nadie-dijo-nada.md:40) | Keep as A2. Correct the contract to name licensed lemmas or the actual permitted forms; it currently names third-person forms while the prose also uses `dije` and `pude`. |
| [10](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/10-la-luz-otra-vez.md:3) | Keep as the A2 cumulative capstone. It uses preterite and `va a salir`, so it cannot be the capstone of a strictly A1 manuscript. |

The imperfect and subjunctive may remain excluded. An A1–A2 book does not have to teach every A2 structure.

## 3. Honest level label

Recommendation: **A1–A2**.

Cost ranking:

1. **Relabel A1–A2, correct the ladder, and make the few early-boundary edits above — low to medium cost.** The public metadata does not exist yet, so this is the cheapest moment to change the title/subtitle. Stories 05–10 can largely remain intact.
2. **Relabel A1–A2 and change documents only — lowest mechanical cost, but insufficient while claiming a strict per-story staircase.** Story 01 `le gusta`, Story 02 `va a contestar`, and Story 03/04 `Escriba` would still precede their boundary.
3. **Cut all A2 material and keep A1 — very high cost.** Stories 05, 07, 08, 09, and 10 require substantial rewriting; Story 06’s dialogue changes heavily; even Stories 01–04 need work because PCIC places third-person clitics, common irregular presents, and habitual present beyond core A1.
4. **Keep the current prose and retain an unqualified A1 label — reject.** That conflicts with the owner’s chosen authority.

## 4. Simplest checker that works

Use one stdlib-only `spanish_grammar_check.py` containing a reviewed surface-form table for the verbs actually present, a per-story minimum-story/CEFR policy, and a short list of multi-token patterns such as `le + gusta(n)`, `ir + a + infinitive`, and `estar + gerundio`; scan every learner-facing Spanish line, including exercises, and fail unknown verb forms instead of silently accepting them. `Le gusta` would be classified as the A2 `le` construction in Story 01, while `Escriba` would match the A2 imperative/subjunctive form in Story 03. Ambiguous forms such as `toma` can be reported for manual review. No spaCy, Stanza, Apertium, AnCora evaluation, or general morphological analyzer is needed for this closed 7,000-word manuscript.

## 5. “Attention, not knowledge”

That reasoning is sound. Knowing Spanish does not provide exhaustive recall across ten changing rule sets; fifteen missed readings are direct evidence that unaided review is unreliable for this job.

A per-story checklist is cheaper to start but not sufficient alone: it uses the same attention channel that already failed. The cheapest dependable arrangement is:

- A short checklist during drafting for contextual questions the script cannot settle.
- The deterministic checker afterward for forms and patterns.
- Manual review only of its small ambiguity list.

The checker is lint, not an oracle and not a marketing claim.

## 6. Manufactured obstacles remaining in the plan

These should be deleted or demoted in [_planning/grammar-gate.md](/Users/mouhamad/Development/ready-to-publish-books/_planning/grammar-gate.md) and [.local-tasks/grammar-gate.md](/Users/mouhamad/Development/ready-to-publish-books/.local-tasks/grammar-gate.md):

- **D1:** withdrawn marketing decision. Delete completely.
- **D2, T4.3, T4.4:** dependency debate, spaCy comparison, and ADR. The owner decided; build the small table-driven checker.
- **D3 and separate T1.1 owner gate:** exercise scope is not an owner-level decision. Scan all learner-facing Spanish, including questions; exclude the explicitly non-book pipeline proof.
- **T0.2 as written:** its violation list is factually stale. Replace it with findings from the corrected PCIC policy.
- **T0.3:** manuscript hashes as a prerequisite are ceremony. Git revision plus the checker report identifies the tested input sufficiently.
- **T2.4:** JSON-to-Markdown rendering machinery is unnecessary for one book.
- **T2.5:** a task to prove an unimplemented idea is absent is busywork.
- **T3.1:** extracting the entire PCIC A1–A2 inventory is unnecessary. Extract only constructs used by the ladder or manuscript.
- **T3.3’s “PCIC does not automatically win” debate:** overruled. Replace it with the already-answerable product action: label A1–A2.
- **T5.3’s proof-grade ambiguity policy:** inherited from the withdrawn “mechanically proven” premise. Report ambiguous cases for checklist review.
- **T5.4:** UD-specific `VerbForm=Fin` machinery is irrelevant when no UD analyzer is used.
- **T5.6:** missing-resource failure behavior is unnecessary for a self-contained table.
- **T6.1 and T6.2:** exhaustive generated paradigms and AnCora benchmarking are research projects, not requirements for this manuscript.
- **T6.3 and T6.4:** keep a handful of regression and mutation fixtures, but delete “every tense, mood, person, homograph, rule, boundary, and all ten stories.”
- **T7.1 assembled-export check now:** no export exists yet. Check chapters now and the export when Stage 6 creates it.
- **T7.4:** rerun the panel only after materially rewritten prose, not after labels, contracts, or tiny exercise edits.
- **T8.1 and T8.2:** a globally institutionalized Gate G with measured precision thresholds and changes to `CLAUDE.md`/schemas is premature for one Spanish book.
- **T8.3:** useful prevention, but a follow-up improvement—not a publication blocker.
- **T8.4:** adding a slogan to model-routing is retrospective commentary, not grammar work.

What remains real is much smaller: verify current text against a corrected targeted PCIC table; correct all ten chapter contracts; build the small checker and a few fixtures; run it; make genuine boundary edits; rerun the existing vocabulary gate on changed stories.

<debate>
  <agreed_points>
    <point>PCIC is authoritative for this book's A1 and A2 classifications.</point>
    <point>The marketing gate is withdrawn; the Stage 6 blurb must simply be honest.</point>
    <point>Sustained-attention failure justifies a small repeatable checker.</point>
    <point>The dependency question is closed; the simplest sufficient implementation should be used.</point>
  </agreed_points>
  <contested_points>
    <point id="1">
      <position_a>The preterite, imperfect and imperative are A1 in PCIC.</position_a>
      <position_b>They are A2 in PCIC.</position_b>
    </point>
    <point id="2">
      <position_a>The book needs only a corrected ladder document, not story rewrites.</position_a>
      <position_b>The book needs actual story rewrites to preserve its per-story progression.</position_b>
    </point>
    <point id="3">
      <position_a>A hand-written verb table plus banned-form and construction patterns is a sufficient checker.</position_a>
      <position_b>A real morphological analyzer is still required.</position_b>
    </point>
  </contested_points>
  <verdict contract="defend-or-concede">
    <for_point id="1">concede a</for_point>
    <for_point id="2">concede a</for_point>
    <for_point id="3">concede b</for_point>
  </verdict>
</debate>
--- end report ---
```
