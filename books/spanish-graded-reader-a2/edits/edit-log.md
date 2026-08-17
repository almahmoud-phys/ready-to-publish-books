# Stage 5 edit log

**Date:** 2026-08-14  
**Scope:** Ten publishable Spanish chapters only. `chapters/sample-story-pipeline-proof.md` was excluded because it is a Stage-0 toolchain proof, not manuscript content.

## Review record

All ten publishable chapters were reviewed for spelling, Spanish punctuation, dialogue-dash consistency, Markdown headings/tables, exercise presentation, canon terminology, and the house banlist. The banlist scan returned no matches. Dialogue em dashes are the manuscript's required Spanish dialogue convention, not prose em-dash usage.

| Chapter | Result |
|---|---|
| 01–07 | No supported mechanical correction found. |
| 08 | Two supported corrections applied; see entries E-001 and E-002. |
| 09–10 | No supported mechanical correction found. |

## Applied changes

| ID | Artifact | Before | After | Rule / evidence |
|---|---|---|---|---|
| E-001 | `chapters/08-lo-que-paso-en-1998.md` | `Yo abrí la puerta para ella.` | `La puerta se abrió para ella.` | Canon continuity: Story 07 states that the door opens while Ana remains seated. The correction removes the false action attribution without altering the event. |
| E-002 | `chapters/08-lo-que-paso-en-1998.md` | `Rosa leyó la lista.` | `Rosa habló de la lista.` | Grammar sequencing: `leyó` is an unlicensed y-shifting preterite in Story 08; the replacement is true to the narrative and uses a licensed regular preterite. |
| E-003 | `bible/cast.md` | `Deflects with jokes.` | `Terse and evasive.` | Record correction: delivered Beto dialogue in Stories 01, 05, and 10 is terse/evasive rather than jokey. |
| E-004 | `tooling/scripts/spanish_grammar_check.py` and `tests/test_spanish_grammar_gate.py` | The generated `leer` paradigm accepted nonexistent `leió` and did not detect `leyó`; `llovió` was unclassified. | Recognize `leyó`/`leyeron` as unlicensed irregular preterites, exclude generated non-forms, add `llover`, and pin `leyó` in regression coverage. | Qwen Stage-4 finding Q1-P1-F3; regression test passes. |
| E-005 | `bible/vocabulary-ledger.md` | Story 08: 15 new types / run 93; volume 102. | Story 08: 14 new types / run 92; volume 101; subsequent running totals synchronized. | The Story 08 exercise replacement removes `leyó` from the cumulative glossary. Re-measured with the required lexical gate. |
| E-006 | `README.md` | Stale Stage-3/4 status and stale independent-audit handoff. | Current authoritative Stage-5 status and completed Gate-B/Gate-C results. | Router accuracy; `state.json` remains authoritative. |
| E-007 | `tooling/scripts/spanish_grammar_check.py` | `__doc__.split(...)` could dereference `None`. | Uses `(__doc__ or "").split(...)`. | Safe runtime hardening; no behavior change with the module docstring present. |

## Deliberately not changed

- **Story 08 `mirar` density:** **resolved retain-as-is decision**, not a mechanical defect. Stage 4 scored prose above the floor; no unauthorized quality rewrite was made.
- **Story 10 Rosa pre-dawn cue:** no defect found. Her bakery opens at five and the return is already inferably near dawn; no speculative clarification was added.
- **Parallel English text:** excluded under `PIPE-001`; no translation work was generated or edited.

## Verification

- `python3 tooling/scripts/spanish_grammar_check.py --selfcheck` — PASS.
- `python3 tooling/scripts/spanish_grammar_check.py --text <chapter> --story NN` for all ten publishable chapters — PASS.
- Required cumulative `graded_reader_check.py --ledger ... --story NN --locale latam` gate for all ten chapters — PASS. Story 08 after E-002: coverage `0.973` (minimum `0.93`), `14` new surface types (maximum `25`), zero locale violations.
- `python3 -m pytest tests/test_spanish_grammar_gate.py tests/test_graded_reader_gate.py` — **30 passed**.
- House-banlist scan across all ten publishable chapters — no matches.

No pending unapplied correction remains.
