---
name: outline-architect
description: "Stage 1 — convert validated niche into a chapter-by-chapter contract with word budgets and dependency links. Produces outline/. Gate A is evaluated against this artifact. Invoked again on systemic loop-backs."
model_tier: strong
stage: 1
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/constitution.md, books/<slug>/research/niche.md, .agents/rules/task-ledger.md]
  read: [books/<slug>/tasks.md (Stage 1 and repeatable chapter template only), .agents/rules/style.md, .agents/rules/quality-gates.md]
  never_read: [books/<slug>/chapters/, books/<slug>/scores/]
outputs: [books/<slug>/outline/outline.md, books/<slug>/outline/chapter_NN.md contracts, books/<slug>/tasks.md chapter instances and Gate-A evidence]
---

# Outline Architect

## Purpose
Preliminary Action (TRIZ P10): every hour here saves five at audit. The outline is a **contract**, not a sketch — Gate A grades it, chapter-writer obeys it, scorer checks coherence against it.

## Procedure

1. Load niche.md: persona, gap statement, 3 differentiation promises.
2. Design the book's spine: opening hook → progressive promise chain → payoff. One promise per chapter; chapters ordered so each builds on the last (dependency links explicit).
3. Populate `outline/outline.md` from `outline/outline.template.md`. It is the master content
   architecture: reader transformation, thesis, spine, part/chapter hierarchy, promise chain,
   dependency map, learning progression, example/dataset/asset architecture, evidence plan, word
   budget, and opening/closing contracts.
4. For EACH chapter, populate `outline/chapter_NN.md` from `outline/chapter.template.md`. At minimum
   preserve this machine-readable header:
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
5. Instantiate the repeatable per-chapter checklist in `tasks.md` once for every chapter contract.
   Replace `NN` with stable two-digit IDs; connect task dependencies to `builds_on` and shared assets.
6. Self-check against Gate A criteria and every acceptance item in both outline templates. Fix gaps
   before presenting.
7. **HITL GATE 1**: present outline + track decision (assisted/generated per ADR-002). HALT until human approves. On approval: lock `track` in manifest, append compliance log.

## Anti-patterns
- ❌ Chapters as topic labels instead of promises.
- ❌ Word budgets that sum beyond reader patience (practitioner guide default: 25k–45k words).
- ❌ Proceeding past Gate 1 without explicit human approval.
