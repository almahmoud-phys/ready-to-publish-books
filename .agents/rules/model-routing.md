# Model routing — which model for which job

Measured, not assumed. Every claim here comes from a controlled run in this repo on
`spanish-graded-reader-a2`, 2026-08-13. Update it when a new measurement contradicts it; delete
a line rather than let it rot.

Providers are dispatched through the `delegate` skill's relay:
`node ~/.claude/skills/delegate/scripts/relay.mjs --provider codex --model <id> --effort <level>`

## Drafting prose (stage 2)

| Model | Use it for | Known failure mode |
|---|---|---|
| `gpt-5.6-luna` @ xhigh | **First drafts where the ending has to land.** Best sentences, best structural instinct, repairs *structurally* — when told a prop appeared from nowhere it went back and planted the prop earlier rather than deleting the sentence. | **Physical continuity.** Invented a cup in a room with no cup; had a character lower a hand he never raised; moved a bag to a scene it had no reason to be in. Also broke the grammar ceiling twice (a comparative, `al` + infinitive). |
| `gpt-5.6-terra` @ xhigh | **Chapters that are mostly constraint satisfaction**, and crowd/ensemble scenes. Zero grammar-ceiling breaches on the hardest tier in the book. Cheaper. | **Tells instead of shows**, even when the brief quotes judges forbidding it. Broke Spanish dash-dialogue speaker alternation. Dropped a clitic in the chapter whose grammar tier *is* clitics. Repairs **literally** — it satisfies the letter of a fix with the smallest possible edit, so a fix needing a structural change comes back thin and you finish it yourself. |

### The failure both models share: they optimise what is measured

Measured again on stories 07–10 (2026-08-13). Every draft passed every machine check, and the
machine checks were the problem.

Given a "≤25 new word types" budget, `luna` returned glossaries of **9** and **5** — and paid for
those numbers in ways nothing automated could see. In story 07 it padded: *"nadie entra"* ×3,
*"Ana está esperando"* ×4, *"mira la puerta"* ×7, rather than spend a word. In story 10, the
volume's finale, it **renamed the town** — `bodega` became "el trabajo de Beto", `panadería` became
"tienda", `botes` became "barco pequeño", `quiosco` became "el lugar" — because the real nouns cost
glossary slots, in a book that had spent nine stories teaching exactly those nouns.

**A ceiling stated as a number will be read as a target.** Say so explicitly in the brief: name the
budget, name the current usage, and say that spending it is the intended behaviour. Then check the
metric a model did *best* on — that is where the hidden cost is.

Both models, consistently:

- **Self-reports were accurate.** Every number either one claimed — word count, coverage, glossary
  size, exit status — verified true on independent re-run. Neither faked a passing gate.
- **Scope was clean.** Both touched only the files the brief permitted.
- **Neither can be its own last reader.** Each produced ~6 defects per first draft that the machine
  gate cannot see. A human or a separate model must read every draft before it counts as done.

Practical routing: **luna drafts, terra is the cheaper substitute, and neither ships unreviewed.**
Budget one repair round per story as normal, not exceptional.

## Judging (stages 3, 4, and any quality panel)

**Independent model families, never personas on one model.** Distinct personas on a single model
are correlated simulations and prove nothing. Three families is the working minimum; a 2-of-3
majority is one model away from flipping, so say so when reporting.

Families used and confirmed working: `codex` (OpenAI), `qwenmax` (Qwen), `deepseek` (DeepSeek).
`kimicode` (Kimi) hit a 403 quota wall on 2026-08-13 — substitute *before* reading any result, so
the swap cannot be a search for a friendlier judge.

Judging rules that earned their place:

- **Preregister thresholds before dispatching any judge.** A threshold chosen after seeing scores
  is a rationalization. Write it to a file first.
- **Blind the judges.** Give them a sandbox containing only the samples and the rubric — no
  project rationale, no other judge's opinion, no hint which sample is the candidate.
- **Include a deliberately bad control** and a same-constraint neutral control. Both must be
  length-matched, or difficulty leaks the answer.
- **Include an unchanged calibration anchor** in any second round. Judge scales drift up to ±1.0
  between rounds; without an anchor you cannot tell a real improvement from a friendlier mood.
- **codex's `<debate>` verdict block has contradicted its own prose in 3 of 3 reviews.** Use the
  prose and the scores; discard the block. `concede a` means position A concedes and B prevails —
  misreading that once cost this repo a full re-litigation.

## Reviewing / second opinions

`codex` @ high (`--read-only`) is the default reviewer and has caught real structural defects the
authoring model could not see in its own work. Its findings have been worth applying even when its
verdict block was malformed.
