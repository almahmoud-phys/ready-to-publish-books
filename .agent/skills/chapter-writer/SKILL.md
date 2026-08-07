---
name: chapter-writer
description: "Stage 2 — write ONE chapter per invocation from its outline contract. Runs N times in parallel (worktree/subprocess isolation). Write-only discipline: never evaluates, never reads scores. Track-aware: assisted track produces draft scaffolds for human authoring; generated track produces full prose."
model_tier: mid
stage: 2
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/bible/]
  read: [books/<slug>/outline/chapter_NN.md (this chapter), books/<slug>/summaries/ (prior chapter summaries only)]
  never_read: [books/<slug>/scores/, .agent/rules/scoring-contract.md, other chapters in full, audits/]
outputs: [books/<slug>/chapters/chapter_NN.md, books/<slug>/summaries/chapter_NN.summary.md]
---

# Chapter Writer

## Purpose
Produce one chapter that **keeps its contract**: the promise, the word budget (±10%), the key claims, the style sheet. Nothing else. Draft fast — judgment happens at stages 3–4, never here (separation in time, law 1 of the scoring contract).

## Track behavior (ADR-002 — read manifest.track)
- **`assisted`**: produce a *scaffold* — section skeleton, key points per section, placeholders `[HUMAN: experience/example needed here]`, draft transitions. Human authors the prose; this skill later (loop-back) integrates their text without rewriting voice.
- **`generated`**: produce full prose. Append compliance_log entry (orchestrator does this in batch mode).

## Procedure
1. Load: manifest, bible (all three files), this chapter's contract, prior summaries (never full chapters).
2. Check dependencies: contract's `builds_on` must be satisfiable from summaries alone. If not → STOP, flag to continuity-keeper.
3. Write to contract: open by stating the promise in motion (no filler openers), deliver, end with "Try this".
4. Honor the banlist (style.md) mechanically while drafting — cheaper than cleanup (P10).
5. Emit the 200-word summary file: what was claimed, what terms defined, what examples used, what it sets up. **The summary is the only thing future chapters see — write it for them.**
6. Word budget check ±10%. Self-fix once; do not polish further.

## Anti-patterns
- ❌ Reading scoring rubrics or "improving" against imagined judges — draft-before-judgment is structural.
- ❌ Introducing terms/examples not in the bible without adding them to your summary's "new canon candidates" section.
- ❌ Exceeding context budget: if you need a prior chapter's exact text, the summary was defective — flag it, don't load the chapter.
