---
name: story-bible
description: "Stage 1 (parallel with outline) — build the book's single source of truth: style sheet, terminology, persona constants, example canon. Everything stage 2+ loads. Non-fiction: 'story' = the book's argument and voice."
model_tier: strong
stage: 1
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/research/niche.md, .agents/rules/style.md]
  read: [books/<slug>/outline/outline.md]
  never_read: [books/<slug>/scores/]
outputs: [books/<slug>/bible/style-sheet.md, books/<slug>/bible/terminology.md, books/<slug>/bible/canon.md]
---

# Story Bible (non-fiction: Argument & Voice Bible)

## Purpose
The bible is the only artifact (with the manifest) loaded at EVERY stage — it is the book's immune system against drift. (Context rule 1.) Keep it under 2,000 words total: it's a context resident, not a document.

## Artifacts

1. **`bible/style-sheet.md`** — per-book override of house style: voice quirks, persona address, banned/preferred terms, formatting deviations, code style (if technical), citation style.
2. **`bible/terminology.md`** — canonical definitions. Every term used consistently or the fact-checker flags it. Include: terms, abbreviations, product names with exact casing, version numbers.
3. **`bible/canon.md`** — the example canon: recurring case studies, the book's running example project (if any), persona constants (reader's assumed skill level, tools, budget), and the argument spine in 5 sentences.

## Procedure
1. Derive from niche.md + outline spine.
2. Every entry must be **load-bearing**: if no stage would ever check against it, cut it (TESE trimming).
3. Reconcile approved canonical additions from `summaries/continuity-canon-proposals.md` into `bible/canon.md` before handing back to chapter pipeline.
4. Human review at Gate 1 (presented with the outline — one approval covers both).

## Anti-patterns
- ❌ Bible bloat — it's read on every invocation; every line costs every stage.
- ❌ Contradicting the house style silently — overrides must be explicit and marked.
