# Qwen Stage 4 — Pass 1 Excerpt Score Report

- **Provider/model:** Qwen 3.8 Max (Qwen family)
- **Pass:** 1 — fixed excerpt set, manual user-run
- **Read-only declaration:** yes
- **Prior scores/superseded audits read:** no, as reported by the judge
- **Status:** Panel evidence only. This is not a Gate-C scorecard or final verdict.

## Fixed excerpt result

| Dimension | Score |
|---|---:|
| Originality | 8/10 |
| Prose | 7/10 |
| Coherence | 8/10 |
| Market | 8/10 |
| Voice | 8/10 |
| Opening | 8/10 |

- **Provisional floor score:** 7/10 (Prose)
- **Provisional Pass-1 verdict:** PASS
- **Panel status:** A fresh independent Pass 2 and, if any dimension differs by more than one point, the required tiebreak remain pending.

## Evidence-bearing findings for Pass 2

### Q1-P1-F1 — major: late-story `mirar` density

- **Locations:** `chapters/06-no-me-gusta-esperar.md`; `chapters/07-esta-pasando-algo.md`; `chapters/08-lo-que-paso-en-1998.md`; `chapters/10-la-luz-otra-vez.md`.
- **Evidence:** Qwen independently identified especially dense clusters at `chapters/08-lo-que-paso-en-1998.md:33-45` and a flatter rowing stretch at `chapters/10-la-luz-otra-vez.md:48-57`. It judged the repetition a material prose weakness partly, but not entirely, explained by controlled vocabulary.
- **Pass-2 question:** Is the trade-off sufficient for a 7/10 Prose score, or does it fall below the locked floor and require targeted Stage-2 rewrite?

### Q1-P1-F2 — major: Beto bible register differs from delivered prose

- **Locations:** `bible/cast.md:12`; `chapters/01-la-carta-sin-dueno.md:36-48`; `chapters/10-la-luz-otra-vez.md:26-46,120-133`.
- **Evidence:** The bible says Beto “deflects with jokes”; the delivered dialogue is terse and evasive rather than humorous.
- **Provisional directive:** Prefer a bible correction over retrofitting jokes into controlled-vocabulary prose, subject to Pass 2 confirmation.

### Q1-P1-F3 — rejected after local verification: `leyó` is not an unlicensed irregular

- **Location:** `chapters/08-lo-que-paso-en-1998.md:127`.
- **Qwen claim:** `leyó` was classified as an irregular preterite introduced too early, and the grammar gate was said to be blind to it.
- **Local verification:** Rejected. `leyó` is the standard third-person singular preterite spelling of `leer`; it is an orthographic spelling change within the regular preterite pattern, not an irregular-lemma breach under the chapter’s “regular preterite of -ar/-er/-ir” contract. The checker’s generated surface-form table should eventually be corrected for accurate recognition, but the manuscript form is not a grammar-ladder violation.
- **Pass-2 instruction:** Do not treat this as a manuscript defect or score penalty.

### Q1-P1-F4 — minor: Story 07→08 door staging

- **Locations:** `chapters/07-esta-pasando-algo.md:42,59-60`; `chapters/08-lo-que-paso-en-1998.md:38-39`.
- **Evidence:** Story 07 says the door opens while Ana remains seated; Story 08 says Ana opened it for Lucía. This is a real small continuity wrinkle.
- **Pass-2 question:** Is it materially distracting, and if so should the Story-08 recollection be changed to a subject-neutral description?

### Q1-P1-F5 — minor: Rosa’s pre-dawn Story-10 presence

- **Location:** `chapters/10-la-luz-otra-vez.md:92-93`.
- **Qwen verdict:** Not a causality break; a small explanatory clause remains optional.

### Q1-P1-F6 — record gap: no `bible/style-sheet.md`

- **Evidence:** The requested style-sheet path does not exist. The judge instead used `.agents/rules/style.md`, outline records, and `bible/cast.md` for Voice.
- **Scope:** Record/process issue only; not a current manuscript score penalty.

### Q1-P1-F7/F8 — minor prose observations

- Present-for-past phrasing at `chapters/01-la-carta-sin-dueno.md:8-10` is noted as a known form-lint limitation rather than a scored grammar failure.
- Repetitions such as `cambia de lugar` in Story 10 should be considered alongside F1 rather than as independent defects.

## Qwen citations supporting the provisional scores

- **Originality:** `chapters/02-el-pan-de-las-cinco.md:112-113`; `chapters/09-nadie-dijo-nada.md:93-94`; `chapters/10-la-luz-otra-vez.md:82-84`.
- **Prose:** `chapters/08-lo-que-paso-en-1998.md:33-45`; `chapters/10-la-luz-otra-vez.md:48-57`; counterexamples at `chapters/02-el-pan-de-las-cinco.md:112-113`, `chapters/09-nadie-dijo-nada.md:93-94`.
- **Coherence:** The judge cited all fixed excerpts against their matching chapter contracts and independently confirmed exercise presence, word-budget conformance, annual-light distinction, and monthly-letter mechanics.
- **Market:** `research/niche.md:26-30,101-106,114-126`; delivered adult-register evidence in `chapters/02-el-pan-de-las-cinco.md:112-113` and `chapters/04-todos-los-dias-lo-mismo.md:98-100`.
- **Voice:** `chapters/07-esta-pasando-algo.md:27-33`; `chapters/09-nadie-dijo-nada.md:106-109`; cast dialogue cited above.
- **Opening:** `chapters/01-la-carta-sin-dueno.md:3-13,15-23,40-46,61-66,85`; `research/niche.md:26-30`.

## Handoff to Pass 2

Pass 2 must use a different fixed excerpt seed, independently retest F1, F2, F4, and F5, avoid carrying Qwen’s rejected F3 forward as a manuscript defect, and return dimension scores with the same locked evidence law. If any Pass-2 dimension differs from this pass by more than one point, dispatch the preregistered tiebreak and use the median.
