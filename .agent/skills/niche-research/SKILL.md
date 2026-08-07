---
name: niche-research
description: "Stage 0 — validate a book idea against demand, competition, and differentiation BEFORE any writing. Produces research/niche.md. Run first for every book; check .agent/memories/ for prior niche patterns."
model_tier: strong_synthesis_cheap_gatherers
stage: 0
context_budget:
  always_read: [books/<slug>/manifest.yaml]
  read: [.agent/memories/]
  never_read: [books/<slug>/chapters/, other books' workspaces]
outputs: [books/<slug>/research/niche.md, books/<slug>/research/keywords.md]
---

# Niche Research

## Purpose
Kill bad books cheaply. A book that can't win its niche must die at stage 0, not at stage 7. (Meadows: the cheapest leverage is information — LP6 — before structure is built.)

## Procedure

1. **Load manifest**: seed idea, audience hypothesis, track, genre.
2. **Evidence fan-out** (cheap-model gatherers, parallel, ONE batch + one follow-up):
   - Demand: search volume signals, bestseller ranks of comps, review counts/velocity.
   - Competition: top 5–10 comp titles — price, page count, strengths, **top 20 negative reviews** (unmet needs = our differentiation).
   - Keywords: 7 KDP keyword candidates + 2 category candidates.
3. **Synthesize** (strong model) into `research/niche.md`:
   - Persona: who buys, what job they're hiring the book for.
   - Gap statement: the one sentence this book owns that comps don't.
   - Differentiation contract: 3 concrete promises no comp keeps.
   - Pricing hypothesis + comp table.
   - **Verdict: GO / PIVOT / KILL** with evidence.
4. **Append compliance log** entry for any AI-generated research artifact.
5. **HITL checkpoint**: present niche.md summary; human confirms GO before stage 1.

## Output contract
`research/niche.md` must contain: persona, gap statement, differentiation contract (3 promises), comp table, keyword/category candidates, verdict. Missing any → stage incomplete.

## Anti-patterns
- ❌ Writing prose "to test the idea" — research first (separation in time).
- ❌ Cherry-picking comps that make the idea look good — include the strongest competitor.
