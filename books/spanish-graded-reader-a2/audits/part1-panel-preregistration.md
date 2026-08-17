# Part I quality panel — PREREGISTRATION

Written **2026-08-13, before any judge was dispatched and before any judge output was seen.**
This file is the reason the panel result is worth anything. A threshold chosen after seeing the
scores is not a gate, it is a rationalization, and this book's whole differentiation rests on
promise 1 ("written for adults") which no machine check can prove.

Fixing the rule first is the only defence available to an operation that has, by permanent
constraint, **zero human readers** (`.agents/rules/owner-identity.md`, and the owner's standing
statement: no beta readers, no native-speaker reviewer, ever).

## What is being tested

Stories 01–04 (`chapters/01..04`), the complete Part I of `spanish-graded-reader-a2`.

The hypothesis under test is NOT "is the Spanish correct" — `graded_reader_check.py` already
answers that mechanically, and all four pass. The hypothesis is the one codex named as the
highest-risk untested assumption of the entire book:

> constrained, generated A1 stories can remain genuinely compelling to adults.

## Panel design (fixed by codex's specification, 2026-08-13)

Codex's requirement, quoted, because I am not allowed to soften it later:

> Use multiple model families if available. Distinct personas on one model are correlated
> simulations, not independent judges. Blind each judge to the project rationale and other
> judgments. Compare each story pairwise against matched adult graded-reader samples and a
> deliberately juvenile negative control. Score adult dignity, local closure, character
> motivation, desire to continue, natural Spanish within A1 constraints, and sentence-level
> pleasure. Require cited passages for every failure.

Implementation:

- **Independent families, not personas.** Three distinct model families via the delegate relay.
  Personas on one model would agree with each other and prove nothing.
- **Blinded.** Judges receive lettered samples and the six dimensions. They receive no project
  rationale, no niche research, no differentiation promises, no indication which sample is the
  candidate, and no other judge's opinion.
- **Controls in the same packet.** A deliberately juvenile/primer control (the exact register the
  book promises not to be) and a flat textbook-exercise control (the register reviewers attack the
  trade incumbent for). Both are A1-constrained and length-matched so register, not difficulty or
  length, is what varies.
- **Ranking forced.** Every judge ranks all samples 1..N. Absolute scores drift between models;
  ranks do not.

## Thresholds — SET NOW, BINDING

A story passes Part I only if **all three** hold:

1. **No majority critical finding.** A "critical finding" is a judge stating the sample is
   unsuitable for an adult reader or that they would not continue. Critical from ≥2 of 3 families
   on the same story = that story fails.
2. **Every dimension ≥ 7/10**, averaged across the three families, per story. Six dimensions:
   adult dignity, local closure, character motivation, desire to continue, natural Spanish within
   A1 constraints, sentence-level pleasure.
3. **Beats the juvenile control head-to-head** in the majority of families. A story ranked below
   the deliberately-bad control by ≥2 of 3 families is a fail, whatever its absolute scores say.

## What a failure routes to

A fail routes to **rewrite of the named story**, citing the judges' quoted passages. It never
routes to a lowered threshold. Quality gates change only by editing
`.agents/rules/quality-gates.md`, never mid-session (CLAUDE.md rule 9, Drifting Goals tripwire).

If ≥2 of the 4 stories fail, the failure is the **method**, not the story — that escalates to the
owner as a stage-1 loop-back, because it means A1-constrained adult fiction may not be achievable
at this vocabulary ceiling and the book's core promise is unsupportable.

Part II (stories 05–10) is not drafted until Part I passes. That staging is the whole point:
it caps the loss at four stories instead of ten.

## Known limitations of this panel — stated before results, not after

1. **The "matched adult graded reader" control is agent-written, not a published comp.** Scraping
   and republishing a competitor's text is banned permanently (ADR-008) and no licensed A1 sample
   is on hand. The controls therefore test *register*, not *market quality*. A win over my own
   textbook-style control is weaker evidence than a win over a real published one, and this is
   recorded as a weakness rather than dressed up.
2. **LLM judges are not readers.** They are correlated with human taste, not identical to it. This
   panel can catch "obviously juvenile" and "obviously flat". It cannot certify "an adult will
   enjoy this". The market answers that at HITL Gate 2, which is the reason volume 1 ships alone
   and volumes 3+ are not committed.
3. **Grouping leak.** Stories 01–04 share characters, so a judge can infer they belong to one book.
   The leak reveals grouping, not which sample the operator wants to win, and no judge is told a
   candidate exists. Rated a weak leak; accepted rather than hidden.
4. **N=3 families.** Small. A 2-of-3 majority is one model away from flipping.
