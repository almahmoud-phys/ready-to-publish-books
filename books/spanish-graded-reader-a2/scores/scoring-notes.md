# Stage 4 scoring notes — reconciled panel

## Preconditions and protocol

- Gate B was PASS before scoring (`audits/structural.md`): zero open critical structural findings.
- The scoring floor, dimensions, evidence law, and reconciliation method were fixed in `scores/stage4-preregistration.md` before Claude Pass 2 dispatch.
- Pass 1 was manually run by the human owner with **Qwen 3.8 Max** and preserved in `scores/qwen-pass1-report.md`.
- Pass 2 was run with **Claude / Anthropic** through Jcode (`claude-opus-4-6`, session `session_frog_1786704066621_bfa293852a0231ec`) without reading Pass 1 or any prior score artifact.
- The scorer-required full-manuscript final read was run by Claude / Anthropic (`claude-opus-4-6`, session `session_microbe_1786704491515_3b6ed2ed3e41982a`) without reading Pass 1 or prior scorecards.
- English parallel text and Stage-6 frontmatter were excluded: `PIPE-001` has not assigned their production/verification owner. They are not current manuscript failures.

## Panel reconciliation

| Dimension | Qwen Pass 1 | Claude excerpt Pass 2 | Difference | Full-manuscript adjustment | Final |
|---|---:|---:|---:|---:|---:|
| Originality | 8 | 8 | 0 | 0 | 8 |
| Prose | 7 | 7 | 0 | +1 | 8 |
| Coherence | 8 | 8 | 0 | +1 | 9 |
| Market | 8 | 8 | 0 | 0 | 8 |
| Voice | 8 | 8 | 0 | 0 | 8 |
| Opening | 8 | 8 | 0 | 0 | 8 |

No Pass-1/Pass-2 dimension differed by more than one point, so the preregistered tiebreak condition did not occur.

The final full-manuscript pass adjusted only with new cited justification:

- **Prose 7→8:** It retained `chapters/08-lo-que-paso-en-1998.md:L33-L43` as the weakest passage because of `mirar` repetition, but cited stronger whole-book evidence in `chapters/01-la-carta-sin-dueno.md:L7-L9`, Story 09, and Story 10 showing the controlled-vocabulary voice remains adult and effective above the floor.
- **Coherence 8→9:** The full read verified all ten contracts, the resolved annual-light and monthly-letter causality, two-letter transition into Story 08, and the compatible 1998 accounts. The remaining Beto-register discrepancy is a bible-record correction, not a within-manuscript coherence failure.

## Gate C result

- **Book score:** 8/10 (floor principle)
- **Floor dimensions:** Originality, Prose, Market, Voice, Opening — all 8/10
- **Verdict:** **PASS**
- **Loopback counters:** none

## Non-blocking directives carried forward

1. **S3-R1 — Prose ceiling:** `mirar` density is a real quality limitation, especially `chapters/08-lo-que-paso-en-1998.md:L33-L43`. It does not justify a below-floor score; do not rewrite it merely to chase a 9. Revisit only if Stage 5 finds a natural low-risk revision.
2. **S3-T1 — Bible drift:** Update Beto’s speech-register line in `bible/cast.md` from “deflects with jokes” to the delivered terse/evasive register. This is record correction, not prose rework.
3. **S3-C1 — Rosa’s pre-dawn appearance:** The bread and established bakery hours make `chapters/10-la-luz-otra-vez.md:L92-L93` plausible. No edit is required unless the Stage-5 proofreader finds a minimal clarity improvement.
4. **Qwen F3 rejected:** `leyó` in Story 08 is the normal orthographic spelling of the preterite of `leer`, not an unlicensed irregular-lemma breach. Correcting the checker’s generated `leer` forms remains optional tooling accuracy work; it is not a manuscript defect or score penalty.

## Next stage

Stage 5 — proofreader and fact-checker may now start in parallel. Stage 6 and bilingual production remain blocked by `PIPE-001` ownership resolution.
