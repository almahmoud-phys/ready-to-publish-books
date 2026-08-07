---
name: outline-architect
description: "Stage 1 — convert validated niche into a chapter-by-chapter contract with word budgets and dependency links. Produces outline/. Gate A is evaluated against this artifact. Invoked again on systemic loop-backs."
model_tier: strong
stage: 1
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/research/niche.md]
  read: [.agent/rules/style.md, .agent/rules/quality-gates.md]
  never_read: [books/<slug>/chapters/, books/<slug>/scores/]
outputs: [books/<slug>/outline/outline.md, books/<slug>/outline/chapter_NN.md contracts]
---

# Outline Architect

## Purpose
Preliminary Action (TRIZ P10): every hour here saves five at audit. The outline is a **contract**, not a sketch — Gate A grades it, chapter-writer obeys it, scorer checks coherence against it.

## Procedure

1. Load niche.md: persona, gap statement, 3 differentiation promises.
2. Design the book's spine: opening hook → progressive promise chain → payoff. One promise per chapter; chapters ordered so each builds on the last (dependency links explicit).
3. For EACH chapter, emit `outline/chapter_NN.md`:
   ```yaml
   chapter: NN
   title: <assertion-style heading per style.md>
   promise: <the one thing the reader can do/know after>
   builds_on: [NN-1, ...]
   sets_up: [NN+1, ...]
   word_budget: <n>
   key_claims: [<claims that must survive fact-check>]
   sources_needed: [<experiences/examples/data required>]
   ```
4. Emit `outline/outline.md`: spine narrative, total word budget (target ±10%), chapter map, opening-chapter special requirements (Gate: opening earns page 4).
5. Self-check against Gate A criteria. Fix gaps before presenting.
6. **HITL GATE 1**: present outline + track decision (assisted/generated per ADR-002). HALT until human approves. On approval: lock `track` in manifest, append compliance log.

## Anti-patterns
- ❌ Chapters as topic labels instead of promises.
- ❌ Word budgets that sum beyond reader patience (practitioner guide default: 25k–45k words).
- ❌ Proceeding past Gate 1 without explicit human approval.
