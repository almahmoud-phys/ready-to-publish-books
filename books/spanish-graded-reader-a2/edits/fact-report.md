# Stage 5 fact and claim verification report

**Date:** 2026-08-14  
**Scope:** Reader-facing and publication-process claims only. The ten stories are fiction; plot events, characters, and Puerto Lento are not external factual claims and were not fact-checked as such.

## Sources consulted

1. Instituto Cervantes, *Plan curricular. Gramática. Inventario A1-A2* — https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/02_gramatica_inventario_a1-a2.htm (accessed 2026-08-14).
2. Hermit Dave, *FrequencyWords* MIT License — https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/LICENSE (accessed 2026-08-14).
3. Hermit Dave, `content/2018/es/es_50k.txt` repository page — https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/es/es_50k.txt (accessed 2026-08-14).
4. Amazon KDP, *Content Guidelines* — https://kdp.amazon.com/en_US/help/topic/G200672390 (accessed 2026-08-14).
5. Local authoritative evidence: `manifest.yaml`, `state.json`, `assets/WORDLIST-PROVENANCE.md`, `bible/vocabulary-ledger.md`, `tooling/scripts/graded_reader_check.py`, `tooling/scripts/spanish_grammar_check.py`, and `.agents/rules/kdp-compliance.md`.

## Claim dispositions

| ID | Claim / location | Evidence | Resolution |
|---|---|---|---|
| F-001 | The working title identifies this as a Spanish **A2** graded reader (`manifest.yaml`). | The PCIC A1-A2 inventory is the external grammar reference; the level decision and its limits are documented in `constitution.md`. | **VERIFIED** as an internal, evidence-backed classification. It must not become a claim of CEFR certification. |
| F-002 | The Spanish text is machine checked for cumulative lexical coverage, locale markers, and grammar sequencing (`README.md`, `bible/vocabulary-ledger.md`). | Reproducible local scripts ran successfully in Stage 5 for all ten chapters; the grammar script explicitly states that it is lint, not certification. | **VERIFIED.** Reader-facing copy may describe only these measured checks and must retain the stated limitations. |
| F-003 | The active frequency wordlist derives from Hermit Dave/FrequencyWords OpenSubtitles data and is MIT-licensed (`assets/WORDLIST-PROVENANCE.md`). | The upstream repository contains `content/2018/es/es_50k.txt`; its MIT license permits use, modification, distribution, sublicensing, and sale subject to retaining the copyright and permission notice. | **VERIFIED.** Stage 6 back matter must carry the attribution/license notice; no unsourced “CEFR wordlist” claim is permitted. |
| F-004 | The book uses a Latin-American locale consistency check. | `graded_reader_check.py` checks only selected mutually-exclusive locale markers; Stage 5 gate outputs have zero violations. It does not establish regional authenticity. | **VERIFIED** with boundary. Metadata may say the text uses a declared Latin-American Spanish convention, not that it is authenticated for every Latin-American region. |
| F-005 | Extensive-reading research supports a reader-facing introduction. | No active reader-facing introduction or extensive-reading citation is present. | **CUT.** No such claim exists in the publishable manuscript; any later Stage-6 introduction must obtain and cite its own sources. |
| F-006 | Generated text/images/translations must be disclosed to KDP (`.agents/rules/kdp-compliance.md`). | KDP’s current Content Guidelines require disclosure of AI-generated text, images, and translations, including after substantial edits; they distinguish these from AI-assisted content. `manifest.yaml` declares `track: generated`. | **VERIFIED.** Exact KDP form answers remain Stage-7 work and must be generated from `compliance_log.yaml`, not copied from this report. |
| F-007 | The Stage-0 `research/charter.md` lists morphology/agreement analysis, sentence-aligned translations, entailment, and back-translation as if available. | `graded_reader_check.py` explicitly says morphology, entailment, and back-translation are not implemented; `PIPE-001` remains unresolved. The charter is historical Stage-0 input, not active reader-facing copy. | **CUT from all Stage-6/reader-facing claims.** Do not amend the historical charter in Stage 5; its mismatch is documented here as a prohibited claim source. |
| F-008 | The README’s stage-status table is a current process claim. | `state.json` is authoritative and records Gate B/C passed and Stage 5 in progress. | **REWRITTEN** in `README.md` (see edit-log E-006). |
| F-009 | English parallel text is currently available or verified. | No owned translation workflow exists; `tasks.md` records `PIPE-001`. | **CUT.** No translation claim or translation artifact may enter the package until an owner and verification method exist. |

## Result

Every identified claim has one disposition: **verified**, **rewritten**, or **cut**. There are no unresolved external factual flags in active reader-facing artifacts. Stage-6 copy must use this report’s boundaries, especially the bans on CEFR-certification, unimplemented-check, and translation claims.
