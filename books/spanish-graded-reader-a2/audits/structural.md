# Structural audit — Spanish A2 Graded Reader, Volume 1

- **Auditor:** Independent Stage-3 adversarial editor — Claude / Anthropic via Jcode (`claude-opus-4-6`, session `session_chick_1786674816656_aeb24a226b6d11e9`)
- **Audit date:** 2026-08-14
- **Scope:** Fresh post-remediation read of all ten chapters, all chapter contracts, outline, bible files, summaries, continuity report, manifest, constitution, and quality-gate rules.
- **Independence:** The auditor did not author the remediation and was instructed not to read prior active, superseded, or scoring audits.

## Pass 1 — chapter-contract / promise audit

**PASS — no critical or major contract failure.**

- Stories 01–10 deliver their contracted goal, obstacle, turn, and local closure. The repaired Story-02 turn is present-tense `¿Dónde está?` at `chapters/02-el-pan-de-las-cinco.md:58,64`, consistent with its grammar contract.
- Every contracted exercise is present: Story 02 has five questions plus six ordering events; Story 03 has eight matching descriptions; Story 04 has three routine changes; Story 05 has eight now/future statements; Story 06 has six attributions; Story 07 has a fillable two-column simultaneous-action timeline; Story 08 has eight then/now items; Story 09 has six inference questions; Story 10 has eight distinct questions (at least four `por qué`) plus its two-sentence Spanish capstone.
- Narrative word floors are met: Stories 07 and 08 are 700 and 677 tokens respectively against their 675-token floors; Story 10 is 986 tokens against its 990-token ceiling.
- The grammar gate now catches prohibited `estar` imperfect forms; its regression is pinned in `tests/test_spanish_grammar_gate.py`.

## Pass 2 — spine, order, and pacing

**PASS — no finding.** The letter thread proceeds from discovery (01), town evasions (02–06), identification of Lucía (07), the two compatible 1998 accounts (08–09), and public acknowledgement at the annual-lamp ritual (10). Grammar sequencing supports, rather than interrupts, this arc.

## Pass 3 — redundancy hunt

### S3-R1 — `mirar` density is high in late stories

- **Severity:** major
- **Locations:** `chapters/06-no-me-gusta-esperar.md`; `chapters/07-esta-pasando-algo.md`; `chapters/08-lo-que-paso-en-1998.md`; `chapters/10-la-luz-otra-vez.md`.
- **Evidence:** The audit’s text scan found `mirar`-family forms especially concentrated in Stories 06–08 and 10; for example Story 08 repeatedly uses `mira` in its opening exchange (`chapters/08-lo-que-paso-en-1998.md:9-10,22,33-43`).
- **Directive:** During the Stage-4 prose/voice assessment, decide whether controlled-vocabulary alternatives such as `escuchar`, `esperar`, `tomar`, or physical actions improve the adult-reading experience without weakening lexical control. If scoring cites this as below-floor prose, route a targeted Stage-2 rewrite.
- **Loopback:** Stage 4 assessment → Stage 2 only if score evidence requires it.

## Pass 4 — thin-spot detection

### S3-T1 — Beto’s bible register differs from delivered dialogue

- **Severity:** major
- **Location:** `bible/cast.md:12` versus Beto’s dialogue in `chapters/01-la-carta-sin-dueno.md`, `chapters/05-manana-viene-el-barco.md`, and `chapters/10-la-luz-otra-vez.md`.
- **Evidence:** The bible says Beto “deflects with jokes,” while his delivered speech is terse and evasive (`No hay nada`, `Puede`, `Yo no voy`) rather than humorous.
- **Directive:** Prefer correcting the bible register to match the established prose (“terse, evasive, deflects with silence or platitudes”), unless Stage 4 finds the prose itself needs a targeted character-voice rewrite.
- **Loopback:** `story-bible` / Stage 1 record correction, or Stage 2 only if score evidence requires prose change.

## Pass 5 — cold opening

**PASS — persona would continue.** `chapters/01-la-carta-sin-dueno.md:3-30` establishes adult work, place, readable short sentences, and the letter mystery without teacher voice or child framing.

## Pass 6 — canon, causality, and chronology

### S3-C1 — Rosa’s pre-dawn presence needs a small causal cue

- **Severity:** minor
- **Location:** `chapters/10-la-luz-otra-vez.md:92-93`.
- **Evidence:** Rosa is near the bakery holding bread when Ana returns after the annual-lamp trip; the scene does not say why she is awake or present.
- **Directive:** If this remains distracting in Stage 4, add one controlled-vocabulary clause linking her presence to the bakery’s early work or seeing Ana’s boat light.
- **Loopback:** Stage 4 assessment → Stage 2 only if score evidence requires it.

### Canon / causality checks with no finding

- **Annual light:** `chapters/01-la-carta-sin-dueno.md`, `chapters/07-esta-pasando-algo.md:18-21`, `chapters/10-la-luz-otra-vez.md`, and `bible/letters-causal-ledger.md` agree: Stories 01 and 10 are nearly a year apart annual-lamp events; Story 07 is a noisy passing boat light.
- **Monthly letters:** Story 10 accounts for the near-year interval: Lucía leaves one monthly, Ana stores them in a box, and only the newest remains on the counter.
- **1998 accounts:** Rosa’s crew-list account and Lucía’s non-boarding account are compatible.
- **Story 07→08 letters:** Story 08 explicitly begins with two letters, resolving the previous plural-to-singular discontinuity.

## Gate B result

```text
✅ Gate B result:
- Criterion: Zero open critical structural findings in audits/structural.md.
- Evidence: All six adversarial passes completed against the complete manuscript and its contracts. Open findings: 0 critical, 2 major (S3-R1, S3-T1), 1 minor (S3-C1).
- Verdict: PASS.
- If FAIL → routed to: Not applicable. The remaining directives are carried into Stage 4 and route to their cited owning stage only if scoring evidence makes them below-floor defects.
```
