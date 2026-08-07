---
name: niche-research
description: "Stage 0 — validate a book idea against demand, competition, and differentiation BEFORE any writing, using the explicit KDP validation algorithm. Produces research/niche.md with GO/PIVOT/KILL verdict decided by data thresholds, not enthusiasm. Run first for every book; check .agent/memories/ for prior niche patterns."
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
Kill bad books cheaply. A book that can't win its niche must die at stage 0, not at stage 7. The verdict is decided by **data thresholds** below — never by how good the idea feels. (Meadows LP6: the cheapest leverage is information before structure is built. The expert's-curse bias — "I know it, so it's trivial" — is neutralized by measuring the BUYER's demand, not the author's familiarity.)

## The KDP Validation Algorithm (follow in order; record every number)

### Step 1 — Demand evidence (does money change hands here?)
- [ ] **Comp BSR pull**: for the top 5–10 comparable titles, record Best Sellers Rank (overall Kindle store + category). Estimate daily sales with a BSR-to-sales calculator (bands: BSR ~10k ≈ 10–20/day, ~50k ≈ 3–8/day, ~100k ≈ 1–3/day, >1M ≈ ~0).
- [ ] **Review velocity**: reviews ≈ 1–2% of buyers. Recent review dates (last 90 days) = CURRENT demand; only old reviews = historical, treat with suspicion.
- [ ] **Price points**: what do comps charge? Practitioner non-fiction healthy band: $9.99–29.99 ebook, $19–45 print. A niche where everything is $2.99 signals weak willingness-to-pay.

### Step 2 — Competition measurement (can we enter?)
- [ ] **Search result count** on Amazon for the 3 main keywords: <1,000 results = low competition; 1,000–10,000 = contested; >10,000 = saturated (default PIVOT unless differentiation is overwhelming).
- [ ] **Autocomplete mining** (incognito browser): type seed keywords, harvest Amazon autocomplete long-tail phrases — these are recorded real buyer searches. Note misspellings/awkward phrasings: underserved demand no comp titles for.
- [ ] **3-book rule**: name 3 books that would share a shelf with ours. No shelf = no market (KILL or reposition). Shelf entirely A-list bestsellers with thousands of reviews = too hard (PIVOT to sub-niche).
- [ ] **Category difficulty**: BSR of rank #20 in 2 target categories — winnable top-20 = realistic visibility.
- [ ] **Negative-review mining**: top 20 one-to-three-star reviews across comps → unmet needs = our differentiation contract.

### Step 3 — Differentiation (why us?)
- Gap statement: the ONE sentence this book owns that comps don't.
- Differentiation contract: 3 concrete promises no comp keeps (drawn from negative reviews).
- Authority fit: can the author plausibly own this? (assisted track: real experience required — ADR-002)
- Asset-feasibility check: screenshots/figures the book needs vs. what we can actually produce (ADR-007 figure policy). Heavy authentic-screenshot needs = schedule risk, flag it.

### Step 4 — Verdict (thresholds, not vibes)
- **GO**: demand proven (≥2 comps under 50k BSR or equivalent channel evidence) AND competition enterable (<10k results or clear sub-niche) AND differentiation contract credible.
- **PIVOT**: demand exists but entry angle wrong → reposition (sub-niche, retitle, different persona) and re-run Steps 1–2.
- **KILL**: no demand (comps >1M BSR, stale reviews) OR no shelf OR authority mismatch. Killing costs nothing — that's the point of the gate.

## Tools (optional but worth it at M1)
Publisher Rocket / KDSpy / K-lytics for search volume, competition scores, earnings estimates (~EUR 100 one-time). Record tool outputs in research/niche.md.

## Procedure
1. Load manifest: seed idea, audience hypothesis, track, genre. Check `.agent/memories/` for prior niche patterns.
2. **Evidence fan-out** (cheap-model gatherers, parallel, ONE batch + one follow-up): Steps 1–2 data collection via web research.
3. **Synthesize** (strong model) Steps 3–4 into `research/niche.md`.
4. Append compliance log entry for AI-generated research artifacts.
5. **HITL checkpoint**: present niche.md summary incl. all recorded numbers; human confirms verdict before stage 1.

## Output contract
`research/niche.md` must contain: persona, comp table WITH BSR + review dates + prices, autocomplete/keyword harvest, result counts, 3-book shelf, category difficulty, negative-review findings, gap statement, differentiation contract (3 promises), asset-feasibility note, and the verdict with the numbers that produced it. Missing any → stage incomplete.

## Anti-patterns
- ❌ Writing prose "to test the idea" — research first (separation in time).
- ❌ Cherry-picking comps that make the idea look good — include the strongest competitor.
- ❌ Verdict by enthusiasm — thresholds decide; the human confirms the DATA at the checkpoint.
- ❌ Skipping the asset-feasibility check — that's how screenshot-heavy books stall at stage 5.
