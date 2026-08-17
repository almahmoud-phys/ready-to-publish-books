# Codex review of grammar-gate plan v1 — 2026-08-13

Reviewer: codex `gpt-5.6-sol`, effort xhigh, read-only. Verdict: **reject v1 as written.**
v2 of `_planning/grammar-gate.md` is the response. Kept verbatim as evidence.

```
--- provider final report ---
Verdict: reject the plan as written. Keep the fail-closed goal and structured ladder, but replace the universal spaCy architecture with a Spanish-first deterministic checker and rebuild the validation strategy.

## 1. Architecture

The useful seam is “book policy as data versus checking code.” The premature seam is “language-neutral UD engine versus language-specific data.”

The case for Spanish-specific code is strong:

- There is one book, one language, and no published catalog.
- The difficult rules are inherently Spanish: `ir a + infinitive`, clitics, `ser`/`estar`, gustar constructions, regular versus irregular preterites, and imperative homographs.
- The plan itself concedes this by adding executable `patterns/es.py`, contradicting its claim that Spanish knowledge lives only in YAML ([plan lines 97–99 and 206–208](/Users/mouhamad/Development/ready-to-publish-books/_planning/grammar-gate.md:97)).
- UD normalizes annotation names, not pedagogical meanings. French passé composé, German Konjunktiv, and Spanish preterite still require different language logic. “Only the ladder file changes” is false.
- The ladder is much broader than the proposed engine: question words, adjective agreement, reflexives, time/frequency expressions, indirect-object pronouns, and discourse constructions also have contracted introductions.

Recommended first architecture:

- `tooling/scripts/spanish_grammar_check.py`
- Canonical structured contract under `books/<slug>/outline/`, because the outline owns content architecture under CLAUDE.md rule 5.
- JSON or TOML rather than introducing YAML parsing into this gate.
- Spanish morphology and pattern logic in the checker; book-specific story thresholds in data.
- Extract a generic engine only after a second language reveals actual commonality.
- Do not move Gate L while building Gate G. That is unrelated churn in recently repaired, heavily pinned code.

Also, the YAML must become the canonical contract, not be “generated” by parsing informal Markdown prose. Rendering readable grammar sections from structured data is safe; parsing those sections back into policy is not.

Rule: position B. Separate policy from implementation now, but write the implementation Spanish-first.

## 2. Dependency

A statistical model is not required for the core task.

For “no preterite before story 08,” a deterministic map of:

```text
surface form -> {(lemma, tense, mood, person, number), ...}
```

is a better gate primitive. Generate it from the book’s closed verb-lemma inventory, regular conjugation rules, and a reviewed irregular-form table. At runtime it is tiny, stdlib-only, versionable, and immune to model drift or out-of-domain guesses. Add token patterns for `ir a + infinitive`, `estar + gerundio`, temporal markers, and clitics.

Spanish resources already support this approach:

- UniMorph publishes about 383,000 Spanish forms over 5,460 paradigms, directly mapping lemmas and inflections to morphological bundles. It can be an upstream data source or test oracle, subject to provenance/license review. [UniMorph Spanish data](https://unimorph.github.io/)
- Apertium already performs Spanish morphological analysis from language dictionaries, proving that statistical tagging is not a prerequisite. It does bring native tooling, so I would use it as prior art or a differential oracle, not necessarily as the runtime dependency. [Apertium Spanish morphological analysis](https://github.com/apertium/apertium-spa-ast)
- UD Spanish AnCora supplies over 547,000 tokens with manually produced morphology converted to UD, useful for fixtures and evaluation. [UD Spanish AnCora](https://universaldependencies.org/treebanks/es_ancora/index.html)

A deterministic analyzer returns all possible analyses instead of pretending an ambiguous analysis is certain. Fatal rules should fail only on unambiguous forbidden readings. Ambiguous cases should be rewritten or explicitly resolved; unresolved warnings cannot support a “mechanically proven” marketing claim.

If broader contextual parsing ultimately proves necessary, spaCy is the more proportionate statistical prototype than Stanza. But it should be optional evidence, not the source of truth:

- spaCy’s Spanish model is trained on news, unlike this short-dialogue A1 prose. Its inspected model card reports approximately 97% F1 for Mood/Tense but only about 79% F1 for `xcomp`, precisely the dependency relation implicated in modal and periphrastic constructions. [Official `es_core_news_sm` model card](https://huggingface.co/spacy/es_core_news_sm/blob/main/meta.json)
- Stanza reports 98.54 UFeats accuracy for Spanish AnCora, but remains neural, PyTorch-based, heavier, and still imperfect. [Stanza model performance](https://stanfordnlp.github.io/stanza/performance.html)

The plan’s prior-art argument is also partly unsupported: its cited paper is about contextual vocabulary assessment using the English Vocabulary Profile, not detection of English Grammar Profile constructs ([paper abstract](https://arxiv.org/abs/2506.02758)). And ordinary graded-reader corpora are not “gold-standard” morphology or ladder annotations.

Rule: position B. Use deterministic morphology first; add a statistical analyzer only for genuinely unresolved contextual rules.

## 3. Ambiguities and missed failure modes

The imperative problem is much larger than `toma`.

- Almost every Spanish third-person present form is also a tú imperative: `mira`, `deja`, `abre`, `cierra`, `pone`, `sale`, `sigue`, and many others. `ve` is additionally present `ver` or imperative `ir`.
- Formal imperatives overlap present subjunctive. The current manuscript contains `Escriba tres cosas` in story 3 ([line 116](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/03-la-mesa-que-nadie-usa.md:116)) and again in story 4. These are real commands, not hypothetical ambiguity.
- First-person-plural present and preterite coincide for many `-ar` and `-ir` verbs: `hablamos`, `vivimos`.
- `fue` is preterite of both `ser` and `ir`. `vino` can be a verb or noun. `como`, `nada`, `para`, `trabajo`, `camino`, `lista`, and `remo` all have verb/non-verb analyses relevant to this manuscript.
- Reflexive clitics are contextual. `se`, `me`, and `te` may be reflexive, reciprocal, pronominal, passive/impersonal, or objects. Attached forms such as `sentarse` also complicate tokenization. Story 3 already uses `sentarse` before story 4 introduces reflexives ([lines 5 and 24–25](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/03-la-mesa-que-nadie-usa.md:5)).
- A raw `Tense=Past` test is wrong. Spanish UD also assigns past tense to participles, which may function as adjectives. The actual early stories contain `cansado`, `abierta`, `cerrada`, and `sentado`. Preterite detection must require `VerbForm=Fin`. [UD Spanish morphology](https://universaldependencies.org/es/)
- “Regular preterite” is a pedagogical category absent from UD. The plan does not define whether spelling changes, `-ir` stem changes, `leer → leyó`, or short paradigms such as `dar` and `ver` count as regular.
- The contract names eight surface forms, while YAML licenses whole lemmas and every person. Story 9 uses `dije` and `pude`, although the outline names `dijo` and `pudo`. That policy ambiguity must be resolved before implementation.
- `allow_lemmas_any_form` is dangerous: it appears intended to allow present-tense irregulars, but literally licenses `dijo`, `hizo`, `pudo`, future, and subjunctive forms in story 1.
- Present morphology does not reveal temporal meaning. `mañana viene` is future-oriented present; `Antes es de él` is erroneous present-for-past and would pass Gate G ([story 3 lines 63–64](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/03-la-mesa-que-nadie-usa.md:63)).
- The checker’s input scope is undefined. Exercise questions are Spanish sentences and contain grammar unavailable to their stories. Excluding them contradicts “every Spanish sentence”; including them makes current stories fail.
- Most importantly, the proposed rules miss obvious actual contract violations: story 1 uses adjectives, frequency adverbs, gustar, modal-plus-infinitive, and question words before their introductions ([story 1 lines 12–17, 29–30, 34, 52 and 70–71](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/chapters/01-la-carta-sin-dueno.md:12)); story 3 uses `mientras` before story 7.

The plan’s known-violation inventory is stale as well. Its story-1 future line, story-5 comparative/`al` construction, and story-9/10 `vi`/`vio` examples are absent from the current manuscripts. A baseline reconciliation must precede implementation.

## 4. Ground truth

Two stories and roughly 150 verbs are inadequate, and “hand-label” is impossible under the stated no-human constraint.

It cannot estimate per-rule recall because compliant stories probably contain zero positive examples of forbidden subjunctives, imperfects, futures, or imperatives. Even aggregate accuracy would say little about rare rules; per-rule denominators would be tiny or zero.

LLM labelling is not formally circular with a spaCy model, but it is pseudo-ground-truth, not ground truth. If the LLM also generated or reviewed the prose, shared errors and stylistic priors make it especially non-independent. It measures agreement between systems.

The cheapest non-circular replacement is:

1. Use an externally annotated corpus such as AnCora for feature-level evaluation.
2. Generate a stratified morphology corpus from reviewed conjugation paradigms: every relevant tense, mood, person, regular class, irregular class, and homograph. Labels are known by construction.
3. Add contrastive ambiguity fixtures: narrative `Ana toma…` versus command `Toma…`, noun `trabajo` versus verb `trabajo`, participial adjective versus compound tense.
4. Mutation-test all ten stories: inject one known violation for every rule at every applicable boundary and require a fatal result with the correct line and licensing story.
5. Treat analyzer disagreements as diagnostic evidence, never as gold labels.
6. Require unresolved ambiguous manuscript cases to be rewritten or explicitly adjudicated before publication. With no human oracle, “warn and ship” is not verification.

## 5. Sequencing

Validating policy before production engine code is correct. Choosing spaCy in Phase 0 is not.

PCIC may force a product decision: its A1/A2 grammar table places the imperfect, preterite, and imperative in the A2 column, while this “A1” book introduces the preterite in stories 8–9. [PCIC A1–A2 grammar inventory](https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/02_gramatica_inventario_a1-a2.htm)

But PCIC must not automatically “win.” Cervantes explicitly says its inventories are not a language program ready to take directly into the classroom and require adjustment for the particular teaching situation. It also warns that a phenomenon can appear at different levels in different inventories. [PCIC introduction](https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/introduccion.htm)

Recommended sequence:

1. Reconcile the stale state/plan/manuscript findings and freeze hashes.
2. Define what “grammar ladder” covers: prose, dialogue, exercises, titles, glossary, and final export.
3. Make one structured outline-owned contract canonical; define every construct and the exact meaning of “regular” and “named irregular.”
4. Audit that contract against PCIC and decide whether the product remains A1, becomes A1→A2, or changes its ladder.
5. Spike deterministic morphology against spaCy on the real token inventory and constructed fixtures; then write the ADR.
6. Build the minimal Spanish checker with golden and mutation tests.
7. Run all ten manuscripts and the assembled export; repair content and rerun Gate L.
8. Add Gate G to the rule file and stage transition before stage 3.

Cut entirely:

- Moving Gate L.
- A speculative Stanza swap interface.
- General French/German rule abstractions.
- Calibration against unannotated graded-reader corpora.
- The two-story LLM-labelled “gold” sample.
- DependencyMatcher where simple deterministic token patterns suffice.

Missing:

- Export-level coverage.
- Markdown/source-span extraction.
- Configuration-parser choice.
- Pinning and hashing any external model/data.
- Ambiguity/waiver governance.
- Known-violation regression fixtures.
- Exact blocking thresholds in `quality-gates.md`.
- The distinction between conformance and correctness.
- Reconciliation of morphology, agreement, alignment, and back-translation promises.

## 6. The real decision

Gate G must block this book before sale. A hand or LLM check is not compatible with the existing contract.

The promises are explicit:

- “Correctness that is mechanically proven rather than asserted” ([niche lines 100–104](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/research/niche.md:100)).
- “Every Spanish sentence passes a published, reproducible check” ([lines 116–118](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/research/niche.md:116)).
- “Verification is fully computational” ([lines 120–123](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/research/niche.md:120)).
- The owner-attested authority envelope additionally promises version-pinned morphology and agreement analysis, alignment, entailment, and independent back-translation ([charter line 25](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/research/charter.md:25)).
- `state.json` already requires grammar conformance before stage 3 ([line 73](/Users/mouhamad/Development/ready-to-publish-books/books/spanish-graded-reader-a1/state.json:73)).

Therefore Gate G is necessary—but not sufficient. Either complete the promised reproducible suite for book 1, or obtain an owner-approved contract amendment that narrows the claim and rerun affected stages. Shipping the current claim with an LLM “hand-check” would be false advertising by the repository’s own definitions.

<debate>
  <agreed_points>
    <point>The grammar-conformance gap is real and the gate must fail closed.</point>
    <point>The per-book ladder should be canonical machine-readable data separate from checking code.</point>
    <point>PCIC validation belongs before implementation but cannot automatically dictate the book's internal sequence.</point>
    <point>Unresolved ambiguity cannot support a mechanically-proven marketing claim.</point>
  </agreed_points>
  <contested_points>
    <point id="1">
      <position_a>The language-neutral engine + per-book ladder data split is the right architecture now.</position_a>
      <position_b>It is premature generalisation; write a Spanish-specific checker and generalise when a second language exists.</position_b>
    </point>
    <point id="2">
      <position_a>A statistical POS/morphology model (spaCy) is required for this task.</position_a>
      <position_b>A deterministic verb-form lexicon would do this job better, with no heavy dependency.</position_b>
    </point>
    <point id="3">
      <position_a>Gate G must block this book before it goes on sale.</position_a>
      <position_b>Book 1 may ship with a hand-checked ladder provided the marketing claim is worded honestly.</position_b>
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
