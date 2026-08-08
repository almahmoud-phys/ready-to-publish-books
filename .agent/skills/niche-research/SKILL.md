---
name: niche-research
description: "Stage 0 — validate a book idea against demand, competition, and differentiation BEFORE any writing, using the KDP validation algorithm + the verified OSS tooling stack (ADR-009: KDP Scout, trendspyg, trademark gate). Produces research/niche.md with GO/PIVOT/KILL verdict decided by data thresholds, not enthusiasm. Run first for every book; check .agent/memories/ for prior niche patterns."
model_tier: strong_synthesis_cheap_gatherers
stage: 0
context_budget:
  always_read: [books/<slug>/manifest.yaml]
  read: [.agent/memories/, books/<slug>/research/niche-ledger.csv]
  never_read: [books/<slug>/chapters/, other books' workspaces]
outputs: [books/<slug>/research/niche.md, books/<slug>/research/keywords.md]
tooling: [kdp-scout (local CLI, MIT), trendspyg (Google Trends), USPTO+EUIPO trademark search]
---

# Niche Research

## Purpose
Kill bad books cheaply. A book that can't win its niche must die at stage 0, not at stage 7. The verdict is decided by **data thresholds** below — never by how good the idea feels. (Meadows LP6: the cheapest leverage is information before structure is built. The expert's-curse bias — "I know it, so it's trivial" — is neutralized by measuring the BUYER's demand, not the author's familiarity.)

## Tooling (ADR-009 — verified OSS stack, local-first)

- **KDP Scout** (MIT, local SQLite, no account/telemetry): autocomplete A–Z mining, category scans, BSR/price/review snapshots, scoring, CSV export (`export ads`/`export backend` — there is no generic JSON dump; `mine` returns nothing on stdout and writes rows to its own DB). Marketplaces: us/ca/au/de/uk/fr/es/it.
- **trendspyg** (MIT): Google Trends demand-direction — sustained/rising vs declining. Cache results.
- **Trademark gate**: USPTO + EUIPO search for final title/series/brand candidates.
- **Risk tiers (hard rule)**: suggestion-API mining = allowed with conservative rate limits · product-page snapshots = low volume, top-10 ALWAYS human-verified · bulk scraping/proxies/UA evasion = banned permanently (ADR-008).

## The KDP Validation Algorithm (follow in order; record every number)

### Step 1 — Demand evidence (does money change hands here?)
- [ ] **Trend direction**: trendspyg on the 2–3 seed topics — sustained or rising = pass; clearly declining = flag.
- [ ] **Autocomplete mining**: `./tooling/scripts/niche_mine.sh "<seed>" -m us` per seed (marketplace enum: us|de|uk|fr|es|it|ca|au — never `com`; call the wrapper, not KDP Scout directly, per ADR-009 P24). Rich, buyer-intent suggestions = pass; an empty harvest = either the phrase is wrong (mine adjacent seeds) or the collector is blocked — distinguish the two with a known-good control seed ("historical fiction" returns ~28) before recording it as signal.
- [ ] **Comp BSR pull**: top 5–10 comps — record BSR (overall + category). Estimate daily sales (bands: ~10k ≈ 10–20/day, ~50k ≈ 3–8/day, ~100k ≈ 1–3/day, >1M ≈ ~0). KDP Scout snapshots assist; **top-10 verified by human on the live page**.
- [ ] **Review velocity**: reviews ≈ 1–2% of buyers; recent dates (90 days) = CURRENT demand.
- [ ] **Price points**: healthy practitioner band $9.99–29.99 ebook / $19–45 print. All-$2.99 niche = weak willingness-to-pay.

### Step 2 — Competition measurement (can we enter?)
- [ ] **Search result count** per main keyword: <1,000 = low; 1,000–10,000 = contested; >10,000 = saturated (default PIVOT unless differentiation is overwhelming).
- [ ] **3-book rule**: name 3 books that would share a shelf with ours. No shelf = no market. All-A-list shelf = PIVOT to sub-niche.
- [ ] **Category difficulty**: BSR of rank #20 in 2 target categories — winnable top-20 = realistic visibility.
- [ ] **Publisher mix**: count comp authors with farm signatures (generic team names, ALL-CAPS titles, zero-rating clusters). A slop shelf = opportunity for the quality moat, but confirms nothing about demand by itself.
- [ ] **Negative-review mining**: top 20 one-to-three-star reviews across comps → unmet needs = differentiation contract.

### Step 3 — Differentiation (why us?)
- Gap statement: the ONE sentence this book owns that comps don't.
- Differentiation contract: 3 concrete promises no comp keeps (drawn from negative reviews).
- Authority fit: can the author plausibly own this? (assisted track: real experience required — ADR-002)
- Asset-feasibility check: screenshots/figures needed vs. producible (ADR-007 figure policy). Heavy authentic-screenshot needs = schedule risk, flag it.
- **Trademark screen**: USPTO + EUIPO on title/series candidates. Keyword opportunity ≠ safe branding.

### Step 4 — Verdict (thresholds, not vibes)
- **GO**: demand proven (trend not declining + autocomplete rich + ≥2 comps under 50k BSR or equivalent) AND competition enterable (<10k results or clear sub-niche) AND differentiation credible AND trademark clear.
- **PIVOT**: demand exists but entry angle wrong → reposition (sub-niche, retitle, different persona, different marketplace) and re-run Steps 1–2.
- **KILL**: no demand OR no shelf OR authority mismatch OR trademark blocked. Killing costs nothing — that's the point of the gate.

**Cross-check (adopted from KDP Scout's scoring rule)**: prioritize only when ALL four hold — Demand (autocomplete rich + trend not declining) · Buyers (several books with repeatable rank, not one outlier) · Weakness (comps reveal a gap) · Safety (trademark clear + original content).

## Niche ledger (per book, append over time)
`research/niche-ledger.csv` columns: keyword, marketplace, format, recurring_problem, audience_specificity, seasonality, competitor_concentration, median_review_count, observed_bsr_range, trademark_status, differentiation_hypothesis, last_checked.
- `last_checked` drives the staleness flag: research >30 days old must be refreshed before outline-architect runs (LP9 — niche data decays weekly).

## Procedure
1. Load manifest: seed idea, audience hypothesis, track, genre. Load `<slug>/research/niche-ledger.csv` for source signals and `.agent/memories/` for prior niche patterns.
2. **Evidence fan-out** (cheap-model gatherers + KDP Scout/trendspyg runs, parallel, ONE batch + one follow-up): Steps 1–2 data collection.
3. **Synthesize** (strong model) Steps 3–4 into `research/niche.md`; write the niche ledger.
4. Append compliance log entry for AI-generated research artifacts.
5. **HITL checkpoint**: present niche.md summary incl. all recorded numbers; human confirms verdict before stage 1.

## Output contract
Writes back to `manifest.yaml`: `persona`.

`research/niche.md` must contain: persona, comp table WITH BSR + review dates + prices, autocomplete harvest (per seed, per marketplace), trend direction, result counts, 3-book shelf, category difficulty, publisher-mix note, negative-review findings, gap statement, differentiation contract (3 promises), asset-feasibility note, trademark status, and the verdict with the numbers that produced it. Missing any → stage incomplete.

## Anti-patterns
- ❌ Writing prose "to test the idea" — research first (separation in time).
- ❌ Cherry-picking comps that make the idea look good — include the strongest competitor.
- ❌ Verdict by enthusiasm — thresholds decide; the human confirms the DATA at the checkpoint.
- ❌ Skipping the asset-feasibility check — that's how screenshot-heavy books stall at stage 5.
- ❌ Skipping the trademark screen — a winning keyword can still be an unsafe brand.
- ❌ Aggressive tool settings — conservative rate limits always; the publishing account is the asset.
