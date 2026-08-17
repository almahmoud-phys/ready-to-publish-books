# Cumulative vocabulary ledger

The mechanism that makes `builds_on` real rather than decorative.

## The rule

A word glossed in story N is **assumed known** from story N+1 onward and must not be glossed
again. Each story may introduce at most ~25 new words beyond the frequency baseline.

Baseline: `assets/wordlist-es-opensubtitles-top2000.txt` (MIT, OpenSubtitles-derived).
A word is "new" if it is NOT in that baseline and NOT already in this ledger.

## How to update

After each story's Spanish is frozen:

```bash
python3 tooling/scripts/graded_reader_check.py \
  --wordlist books/spanish-graded-reader-a2/assets/wordlist-es-opensubtitles-top2000.txt \
  --text books/spanish-graded-reader-a2/chapters/<story>.md \
  --ledger books/spanish-graded-reader-a2/bible/vocabulary-ledger.md --story NN \
  --locale latam --min-coverage 0.95 --max-new-types 25 \
  --names "ana,beto,rosa,lucia,ferrer,morales,delgado,miguel,ortiz,puerto,lento"
```

`--ledger` and `--story` are **not optional**. Without them every story is graded against the
baseline alone, so a word taught in story 01 is charged to the reader again in 02–10. That was the
2026-08-13 defect. Use `--min-coverage 0.93` for stories 08–10 (the declared late-stage band).

The reported out-of-vocabulary list IS that story's glossary. Paste it below, then it is closed.

## Ledger

The measured table below is the ledger. An empty placeholder table used to sit here from the
template and was deleted on 2026-08-13: two tables in one file, one of them blank, is exactly the
record conflict `CLAUDE.md` rule 8 stops the pipeline for.

**Budget:** ~250 new words across the volume. If the total runs past ~300, the book has outgrown
its declared lexical control and the overflow must be **cut, not re-labelled**.

That rule survived the 2026-08-13 A1→A2 retitle and is not weakened by it. The retitle corrected a
**grammar** classification that had never been checked against any external source; this budget is
a **vocabulary** ceiling that has been measured and enforced from the start. Currently 101 of ~250.
Nobody may cite the retitle as precedent for relabelling past this ceiling.


## Measured state — rebuilt 2026-08-13 against the CUMULATIVE known set

The gate reads THIS file (`--ledger ... --story NN`), so the glossaries below are load-bearing: a
word listed under story 03 is known from story 04 onward. Coverage and new-type count are both
fatal and neither disables the other (`.agents/rules/quality-gates.md`, Gate L). Thresholds are the
ORIGINAL 0.95 / 0.93 — none was lowered during the 2026-08-13 reconciliation.

| Story | Words | Target | Band | New | Run | Coverage | Min | Gate |
|---|---:|---:|:--:|---:|---:|---:|---:|---|
| 01 | 575 | 550 | OK | 16 | 16 | 0.956 | 0.95 | PASS |
| 02 | 687 | 650 | OK | 13 | 29 | 0.968 | 0.95 | PASS |
| 03 | 703 | 650 | OK | 16 | 45 | 0.953 | 0.95 | PASS |
| 04 | 688 | 650 | OK | 14 | 59 | 0.968 | 0.95 | PASS |
| 05 | 781 | 650 | OK | 3 | 62 | 0.985 | 0.95 | PASS |
| 06 | 756 | 700 | OK | 6 | 68 | 0.992 | 0.95 | PASS |
| 07 | 794 | 750 | OK | 10 | 78 | 0.975 | 0.95 | PASS |
| 08 | 766 | 750 | OK | 14 | 92 | 0.973 | 0.93 | PASS |
| 09 | 896 | 800 | OK | 5 | 97 | 0.992 | 0.93 | PASS |
| 10 | 1087 | 900 | OK | 4 | 101 | 0.985 | 0.93 | PASS |

**Volume total: 101 genuinely new surface types.** Story 01 carries the heaviest load because
nothing is pre-taught there, which is also why it is the shortest.

**NOT verified here:** grammar-ladder conformance — this checker does vocabulary and locale only.
That gap is now covered separately by `tooling/scripts/spanish_grammar_check.py`, which all ten
stories also pass (10/10). It is lint, not certification: it reads forms and patterns and cannot
see temporal misuse such as `Antes es de él` or future-value present such as `mañana viene`.

## Glossaries (closed — each word is assumed known from the NEXT story onward)

### Story 01
amarilla, bodega, bolsillo, botes, camina, clara, conocen, contesta, dejarla, doce, importantes, marzo, mostrador, muelle, quiosco, tranquilas

### Story 02
cincuenta, contestar, corta, duerme, gris, limpia, miran, pagas, panaderia, pide, pides, sonrie, toman

### Story 03
explica, frias, levanta, llenas, madera, mesas, monedas, once, pesadas, quieta, sentarse, sienta, sillas, taza, vacia, viejas

### Story 04
acuesta, arregla, cerrada, cuarenta, decidir, devolver, iguales, mismas, motores, papeles, quince, salen, sucias, veinte

### Story 05
cajas, frase, frases

### Story 06
late, mueve, opiniones, quieto, saca, trabajan

### Story 07
bote, columnas, cuerda, desaparece, frota, golpea, motor, moviendo, poste, vacio

### Story 08
abri, dona, guardo, lei, llegan, llovio, manda, mandaste, mande, miraste, movio, subieron, subio, veintiocho

### Story 09
comio, escribo, llora, miente, moneda

### Story 10
aparecio, espanol, lampara, remo

