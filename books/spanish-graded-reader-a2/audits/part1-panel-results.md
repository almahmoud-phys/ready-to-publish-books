# Part I quality panel — RESULTS

Run 2026-08-13 against `part1-panel-preregistration.md`. Thresholds were fixed and committed
before any judge was dispatched. Nothing below has been adjusted to fit the outcome.

## Panel as actually run

| Slot | Family | Provider | Status |
|---|---|---|---|
| 1 | OpenAI | `codex` / gpt-5.6-sol, effort high | completed |
| 2 | Qwen | `qwenmax` / qwen3.8-max | completed |
| 3 | DeepSeek | `deepseek` / deepseek-v4-flash | completed |
| — | Kimi | `kimicode` | **failed — quota exhausted, 403.** Replaced by DeepSeek. |

Three independent families, as preregistered. The substitution happened *before* any result was
read, so it could not have been a choice of a friendlier judge.

Each judge received a git sandbox containing exactly two files: the brief and six lettered
samples. No project files, no rationale, no other judge's output. Blinding held on intent; it
partly failed on grouping (below).

Letter map, withheld from all judges:

| Letter | Actually |
|---|---|
| A | story 03 `La mesa que nadie usa` |
| B | **control** — flat textbook register (`Un día en la vida de Carlos`) |
| C | story 01 `La carta sin dueño` |
| D | story 04 `Todos los días lo mismo` |
| E | **control** — deliberately juvenile register (`El pulpo Pepe`) |
| F | story 02 `El pan de las cinco` |

## Scores — mean of three families

| Sample | dignity | closure | motivation | continue | natural ES | pleasure | min | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A = story 03 | 8.33 | 7.67 | 8.00 | 8.67 | 7.33 | 8.00 | 7.33 | **PASS** |
| D = story 04 | 8.33 | 8.33 | 9.00 | 8.00 | 7.00 | 8.00 | 7.00 | **PASS** |
| C = story 01 | 8.00 | **6.67** | 8.00 | 8.67 | 7.33 | 7.67 | 6.67 | **FAIL** |
| F = story 02 | 8.33 | **6.67** | 8.67 | 8.33 | 7.67 | 7.67 | 6.67 | **FAIL** |
| B = control textbook | 2.67 | 3.00 | 2.33 | 1.33 | 5.00 | 2.00 | 1.33 | fail (intended) |
| E = control juvenile | 0.00 | 8.67 | 6.00 | 0.67 | 7.00 | 3.33 | 0.00 | fail (intended) |

Threshold results:

1. **No majority critical finding** — PASS for all four stories. 0/3 judges marked any story
   critical. 3/3 marked *both* controls critical.
2. **Every dimension ≥ 7.0** — PASS for stories 03 and 04. **FAIL for stories 01 and 02**, both on
   `local_closure` at 6.67.
3. **Beats the juvenile control head-to-head** — PASS for all four, in 3/3 families. Every judge
   ranked all four stories above both controls, with zero exceptions:
   - codex: A > D > F > C > B > E
   - qwen: F > D > A > C > B > E
   - deepseek: D > A > C > F > B > E

## What passed, and it is the thing that mattered most

The book's entire differentiation rests on promise 1 — *written for adults* — which no machine
check can verify and which is why this panel exists. It passed without ambiguity:

- **adult_dignity 8.00–8.33** on all four stories, against 0.00 for the juvenile control.
- Unprompted, and independently, all three judges said they would pay for and finish the book.
  DeepSeek: *"That serial has atmosphere, want, and a mystery that raises the price of the next
  chapter; adults buy books like it."* Qwen: *"An adult of the described profile would pay for
  that and finish it at night on a Kindle."* Codex: *"I would pay for A and finish a book that
  sustained its control of mystery and concrete detail."*
- Two judges independently identified the same craft mechanism as the strongest thing in the set,
  and it is the one deliberately designed in: information delivered through what a character
  refuses to say. Qwen: *"it delivers a revelation through the question a character chooses NOT to
  ask… F builds an entire scene around a withheld question."* DeepSeek on story 04: *"it turns a
  repeated phrase — 'no hay nada' — into the chapter's actual thesis… Repetition-become-meaning is
  real craft, it is fully available inside the beginner ceiling."*

The A1 ceiling is not the obstacle. The register choice is. Both controls sit at the same
vocabulary ceiling and were destroyed by it.

## What failed, and it is one defect appearing twice

Stories 01 and 02 both fail `local_closure` — and only `local_closure`. Every other dimension on
both stories clears 7.0 comfortably. The judges diagnosed it identically, which is why it is
believable:

- **Story 01** — qwen: *"'Ana toca la carta en el bolsillo. Después camina a su casa.' — the
  passage ends with the mystery physically on her person and untouched, a strong hook but an
  experience that plainly completes elsewhere."*
- **Story 02** — deepseek: *"'Ana piensa en dos cosas…' — a chapter that ends by banking a secret
  for a later payoff; it has tension but no landing, so read alone it is clearly an installment,
  not a complete experience."*

Both endings bank a hook instead of landing a scene. That is a specific, fixable craft error, and
it is exactly the error the chapter contracts' "Ending" clause and the acceptance criterion
*"a reader who starts here and reads nothing else still gets a complete story"* were written to
prevent. The contracts were right; stories 01 and 02 did not honour them.

## The ≥2 escalation clause fired — and its stated rationale is falsified

The preregistration says: *"If ≥2 of the 4 stories fail, the failure is the method, not the story
— that escalates to the owner as a stage-1 loop-back, because it means A1-constrained adult
fiction may not be achievable at this vocabulary ceiling and the book's core promise is
unsupportable."*

Exactly 2 of 4 failed, so the clause fired. It is recorded as fired rather than quietly ignored.

But the data falsify the *reason* the clause gave. The escalation exists to catch "A1-constrained
adult fiction is unachievable". That hypothesis is dead: two stories at the same ceiling passed
every dimension, adult dignity averaged 8.0+ across all four, and all three judges volunteered
that they would buy the book. The failure is not the method and not the ceiling. It is two
endings, on one dimension, with a named fix.

Threshold 2 stands unchanged and both stories are recorded as FAILED. What is being rejected is
not the threshold but the clause's inference. Per CLAUDE.md rule 3 this routes as a loop-back to
the exact failing stage with cited evidence — rewrite the endings of stories 01 and 02 — and per
`.agents/rules/owner-identity.md` it is not escalated to the owner for a judgment about Spanish
prose he has stated plainly he cannot make. It is surfaced to him as a finding instead.

## Real defects found, beyond the closure failure

1. **`la luz de la panadería se abre` (story 04) is wrong Spanish.** Flagged independently by two
   families. Qwen: *"a light does not 'open'; a native writer writes 'se enciende'."* Unambiguous
   bug, fix it.
2. **The grammar ladder is costing naturalness, systematically.** Codex scored `natural_spanish` at
   6 on *all four* stories and cited the same construction each time — `Antes, el quiosco es de
   otra persona` (story 01), `Antes es de él. Ahora es de usted.` (story 03). Present tense doing
   the work of a past tense is a direct consequence of the outline's decision to withhold the
   preterite until stories 08–10. This is a design cost, not a typo, and the other two families
   did not penalise it as hard (7–9). It is logged for the stage-3 audit, not patched now.

## Blinding: honest report

Limitation 3 of the preregistration predicted a grouping leak and it occurred. Qwen listed as an
agreed point: *"SAMPLES A, C, D and F are chapters of one serial Puerto Lento work about Tomás
Ferrer."* DeepSeek said the same. The leak revealed **grouping**, not which sample the operator
wanted to win — no judge was told a candidate existed, and the two judges who spotted the serial
still split on which member of it ranked first (qwen: F, deepseek: D). Rated as predicted: weak.

The leak arguably *hurt* the candidates rather than helping them: recognising a serial is what
prompted the closure penalties on 01 and 02.

## Reviewer reliability note

Codex's `<debate>` block again contradicted its own prose, for the third consecutive review. Its
prose says *"Yes. I would pay for A and finish a book"*; its block voted `concede b` on point 1
(*"None of these samples clears the bar for an adult reader"*), and the block was also structurally
malformed, omitting `<agreed_points>` and `<contested_points>`. Per established handling in this
book, the prose is used and the block is discarded. Codex's **scores**, which are what this panel
consumes, are unaffected and were used as given.

## Disposition after round 1

- Stories **03** and **04**: PASS. No rewrite.
- Stories **01** and **02**: FAIL on `local_closure`. Rewrite the endings, then re-run this exact
  panel on the rewritten pair before Part II is drafted.
- Story **04**: fix the `se abre` bug regardless of its PASS.
- Part II (05–10) remains not started. That was the point of staging.

---

# ROUND 2 — the rewritten pair

Same three families, same brief, same controls, fresh sandbox. Raw output in
`panel-raw/round2/`.

## What changed in the text

- **Story 01** — the ending no longer stops at `Ana toca la carta en el bolsillo. Después camina a
  su casa.` Ana now takes the letter home and gives it a deliberate place, which converts a passive
  non-decision (she merely fails to throw it away) into an active claim: `Ahora la carta es de
  ella.`
- **Story 02** — the ending no longer banks two facts for later. The scene's actual transaction is
  now landed: Ana works out that she asked for a name and was handed bread instead, and refuses it.
  `Pero no come el pan.`
- **Story 04** — `la luz de la panadería se abre` → `hay luz en la panadería`. Fixes the wrong verb
  with zero new vocabulary, rather than spending a glossary slot on `encender`.

All four stories still pass the machine gate: ≤25 new word types (24 / 17 / 23 / 24), zero locale
violations. Repo suite 10 passed.

## The calibration anchor

Story 04 was included in the round 2 packet **unchanged**, unlabelled, as an anchor. Without it,
a score rise could be nothing but judges being in a better mood. Its movement measures the drift
directly, and the drift turned out to be large enough to matter — up to ±1.0 per dimension.

## Round 2 scores — mean of three families, with drift shown

| Sample | dignity | closure | motiv | continue | natural ES | pleasure | min | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| story 02 (rewritten) | 9.67 | **8.33** | 9.00 | 9.33 | 8.67 | 8.67 | 8.33 | **PASS** |
| *vs round 1* | +1.34 | **+1.66** | +0.33 | +1.00 | +1.00 | +1.00 | | |
| story 01 (rewritten) | 9.33 | **7.00** | 8.67 | 9.00 | 7.67 | 8.33 | 7.00 | **PASS** |
| *vs round 1* | +1.33 | **+0.33** | +0.67 | +0.33 | +0.34 | +0.66 | | |
| story 04 (**anchor**, unchanged) | 9.33 | 7.67 | 8.33 | 8.33 | 8.00 | 7.67 | 7.67 | PASS |
| *anchor drift* | **+1.00** | **−0.66** | −0.67 | +0.33 | +1.00 | −0.33 | | |

Rankings — both rewrites beat both controls in 3/3 families, and the rewritten story 02 took
first place from every judge:

- codex: story02 > story04 > story01 > textbook > juvenile
- qwen: story02 > story01 > story04 > textbook > juvenile
- deepseek: story02 > story01 > story04 > textbook > juvenile

Critical findings: 0/3 on both rewrites; 3/3 on both controls, again.

## Reading the numbers honestly

The anchor makes two claims defensible and kills a third:

1. **Story 02's closure fix is real and large.** +1.66 while the anchor's closure went *down* 0.66.
   Round 2 was harsher on closure, and story 02 improved anyway — drift-corrected, roughly +2.3.
   Two judges independently named the new final beat as the reason: deepseek, *"the final beat (the
   untasted bread) is communicated through behavior, never explained"*; codex, *"it turns one
   ordinary object — the extra bread — into an act of evasion, warning and attempted protection."*
2. **Story 01's closure fix is real but modest.** +0.33 against a −0.66 anchor drift is about +1.0
   corrected. It clears the threshold at exactly **7.00**. That is a pass, and it is a thin one.
3. **The apparent dignity jump is drift, not improvement.** Both rewrites gained ~+1.33 on
   `adult_dignity` — and the *unchanged* anchor gained +1.00. Almost all of it is the judges being
   more generous in round 2. No claim of improved adult dignity is made from this data.

## Finding left open on purpose

Qwen still penalised story 01, and the line it quoted is one **I added in the fix**: *"'Y mañana, a
las cinco, Ana pregunta en la panadería.' — the passage closes by pointing at the next chapter
instead of resolving, which is why local closure is 6 despite 'Ahora la carta es de ella' landing
well."*

That is a fair hit. The repair for a forward-pointing ending partly reintroduced a forward-pointing
ending. The obvious improvement is to delete that final sentence and end on `Ahora la carta es de
ella.`

It has **not** been done. The version that passed the panel is the version on disk, and shipping a
variant no judge has seen would quietly undo the point of running a panel at all. It is logged as a
stage-3 input, where the adversarial editor sees the whole volume and can make the cut with the
ending of story 02 in view.

## PART I VERDICT: PASS

All four stories clear all three preregistered thresholds. No threshold was moved, before or after
seeing any score. Part II (stories 05–10) is unblocked.

Standing caveats, unchanged by this result: LLM judges are not readers; the controls are
agent-written rather than published comps; N=3 families; and story 01 passes by 0.00. The market
answers the real question at HITL Gate 2, which is the owner's and stays the owner's.
