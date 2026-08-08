---
name: niche-research
description: "Stage 0 — validate a book idea against demand, competition, and differentiation BEFORE any writing, using the KDP validation algorithm + the verified OSS tooling stack (ADR-009: KDP Scout, trendspyg, trademark gate). Produces research/niche.md with GO/PIVOT/KILL verdict decided by data thresholds, not enthusiasm. Run first for every book; check .agents/memories/ for prior niche patterns."
model_tier: strong_synthesis_cheap_gatherers
stage: 0
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/research/charter.md]
  read: [.agents/memories/, books/<slug>/research/niche-ledger.csv, books/<slug>/research/candidates.csv, books/<slug>/research/evidence.yaml, books/<slug>/research/reviews.md, books/<slug>/research/trademark.md]
  never_read: [books/<slug>/chapters/, other books' workspaces]
outputs: [books/<slug>/research/niche.md, books/<slug>/research/keywords.md, books/<slug>/research/evidence.yaml, books/<slug>/research/candidates.csv, books/<slug>/research/trademark.md]
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

## The charter — the thing this loop may not edit

Load `research/charter.md` before anything else. The human wrote it; you never edit it. It
fixes the reader problem, the useful outcome, the author's **authority envelope** and explicit
exclusions, which adjacencies a pivot may change, and `max_pivot_cycles`.

**If any charter field still holds its `<angle-bracket placeholder>`, stop.** An unfilled
charter cannot certify anything, and `niche_verdict.py` will refuse the run anyway.

**The pivot invariant.** Every pivot must preserve `reader_problem` and `authority_envelope`,
and cite evidence for its new angle. Fail either and this is not a pivot — it is a different
book. Stop and hand back to the human. Without this, a chain like *cost routing → inference →
AI engineering → generic AI guide* eventually finds demand while abandoning both the book the
human wanted and the authority that made it defensible.

## Autonomy boundary (what runs unattended, what does not)

| Runs unattended | Requires the human |
|---|---|
| Autocomplete mining, cached trend checks | Writing or widening the charter |
| Normalising, deduping, ranking harvested phrases | Attesting authority fit |
| Recording evidence + provenance | Verifying top-10 comps on live pages |
| Computing the verdict via `niche_verdict.py` | Confirming trademark evidence |
| Auto-continuing a **PIVOT** within the charter | Choosing a new niche after a **KILL** |

**Asymmetric confirmation**: the human may veto a computed GO. Neither human nor agent may
promote a PIVOT or KILL to GO without new evidence. The ratchet only turns one way.

### The provenance rule (non-negotiable)

You may classify, normalise, dedupe and rank phrases. **You may never originate a
market-facing seed.** Every candidate must appear verbatim in one of: the charter, autocomplete
output, an observed comp title/subtitle/category path, or sourced negative-review language —
recorded in `research/candidates.csv` with its `source` and `evidence_location`. A candidate
with no source row may not be mined.

Why: an invented phrase is validated by its own plausibility, then probed as if it were
evidence. That is precisely how a book got titled around `llm cost`, a phrase with zero
Amazon autocomplete presence.

### The bounded PIVOT loop

Auto-continue on PIVOT. **Stop on KILL. Stop on GO.** Terminate on any of:

1. every required field has evidence → hand the computed verdict to the human
2. verdict is KILL (and `collector_health: CONFIRMED` — see below)
3. `pivot_cycles` reaches `max_pivot_cycles` from the charter
4. no evidence-derived candidate remains inside the charter's allowed adjacency
5. the circuit breaker fired
6. required evidence cannot be obtained → **INCOMPLETE**, never GO

`pivot_cycles` lives in `state.json` under `0_niche-research`, not in your context. Increment it
as the loop's first write and read it before continuing — M1 is a manual walk across sessions,
and a counter held in memory silently resets to "3 per session".

### The circuit breaker

KDP Scout **cannot tell a CAPTCHA from an empty result**: `niche_scorer.py` returns `None` for
HTTP error, CAPTCHA and zero-parsed-results alike, and the CLI exits 0 either way. The wrappers
detect refusal themselves and **exit 3**.

On exit 3: **all Amazon activity ends for the session.** No retry, no backoff, no "try a
different keyword". Retrying to reduce uncertainty is what escalates blocking — more probes,
stronger refusal, less evidence, more probing. Degraded mode may still return a shortlist, a
PIVOT, or INCOMPLETE. **It may never return GO.**

KDP Scout's own CAPTCHA message suggests configuring a proxy. ADR-008 bans proxies
permanently. Never follow that advice.

### Collector health

An empty harvest is ambiguous: no buyer language, or a blocked collector. Mine a known-good
control seed (`historical fiction` returns ~28) and record `collector_health: CONFIRMED`.
**A KILL is not computable without it** — killing a viable book on a CAPTCHA is the exact
failure this guard exists to prevent.

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
- **Trademark screen**: on every title/series/imprint candidate. Keyword opportunity ≠ safe branding.
  - The official portals (WIPO Global Brand Database, EUIPO TMview, USPTO tmsearch) are
    JavaScript + CAPTCHA and return nothing to an agent — verified. Do **not** scrape them, and
    do not install a trademark library: what exists on PyPI/npm is unofficial scrapers of
    government portals, the ADR-008 tier-3 shape with near-zero benefit.
  - **Run the evidence pass by web search** over the indexed USPTO mirrors (Justia Trademarks,
    Trademarkia, uspto.report), in the classes books live in: **9** (downloadable e-books),
    **16** (printed matter), **41** (publishing services). Record mark, owner, serial,
    registration number, class, status and link into `research/trademark.md`.
  - **You may never write `clear`.** Write `no_conflict_found` — "no conflict found across N
    sources, classes 9/16/41, searched <date>". Absence of evidence with its scope stated. The
    human converts that to clear at sign-off; a real conflict goes to a lawyer, not to a rerun.
  - Same discipline as a zero-keyword harvest: a null result is a measurement, not a conclusion.
  - **GO requires a human sign-off line** in `research/trademark.md`: `human_signoff: <who> <date>`.
    `niche_verdict.py` checks for it. Your `no_conflict_found` is a search result; clearance is
    a legal judgment, and only that line represents it.

### Step 4 — Verdict (computed, not narrated)

**You do not write the verdict. `niche_verdict.py` computes it** from `research/evidence.yaml`:

```bash
python3 tooling/scripts/niche_verdict.py <slug>     # GO | PIVOT | KILL | INCOMPLETE
```

It cross-checks every claim against the artifact that backs it — autocomplete counts against
the ledger, `trademark_status` against `trademark.md`, the comp table against its own rows,
the charter against its placeholders — and refuses GO on any UNKNOWN or any failed check. Fill
`evidence.yaml` honestly and let it decide; a field you cannot evidence stays `UNKNOWN`.

`INCOMPLETE` is not a fourth verdict. It means the run cannot yet answer, and it names what is
missing. Never round it up to GO, and never round it down to KILL.

The thresholds it applies:
- **GO**: demand proven (trend not declining + autocomplete rich + ≥2 comps under 50k BSR or equivalent) AND competition enterable (<10k results or clear sub-niche) AND differentiation credible AND trademark clear.
- **PIVOT**: demand exists but entry angle wrong → reposition (sub-niche, retitle, different persona, different marketplace) and re-run Steps 1–2.
- **KILL**: no demand OR no shelf OR authority mismatch OR trademark blocked. Killing costs nothing — that's the point of the gate.

**Cross-check (adopted from KDP Scout's scoring rule)**: prioritize only when ALL four hold — Demand (autocomplete rich + trend not declining) · Buyers (several books with repeatable rank, not one outlier) · Weakness (comps reveal a gap) · Safety (trademark clear + original content).

## Niche ledger (per book, append over time)
`research/niche-ledger.csv` columns: keyword, marketplace, format, recurring_problem, audience_specificity, seasonality, competitor_concentration, median_review_count, observed_bsr_range, trademark_status, differentiation_hypothesis, last_checked.
- `last_checked` drives the staleness flag: research >30 days old must be refreshed before outline-architect runs (LP9 — niche data decays weekly).

## Procedure
0. **Load `research/charter.md`.** Placeholders remaining → stop, the human has not set the goal. Read `state.json` `0_niche-research.pivot_cycles` — at `max_pivot_cycles`, stop and hand back.
1. Load manifest (seed, genre) + `<slug>/research/niche-ledger.csv` for prior signals + `.agents/memories/` for patterns from earlier books.
2. **Confirm the collector** before trusting any zero: mine the control seed, record `collector_health`.
3. **Evidence fan-out** (cheap-model gatherers + wrapper runs, parallel, ONE batch + one follow-up): Steps 1–2 collection. Every candidate mined must already exist in `candidates.csv` with its source. **Exit 3 from any wrapper ends all Amazon activity for the session** — record what you have and continue in degraded mode.
4. Fill `research/evidence.yaml`. A field you cannot evidence stays `UNKNOWN`. Never fill one to make the verdict computable.
5. **Compute** the verdict: `python3 tooling/scripts/niche_verdict.py <slug>`. Synthesize Steps 3–4 into `research/niche.md` around what it printed — including a section listing what was *not* collected and why the verdict does not depend on it.
6. On PIVOT: increment `pivot_cycles`, append the new seed to `seed_lineage`, check the pivot invariant against the charter, and loop from 3. On KILL or GO: stop.
7. Append compliance log entries for every generated artifact.
8. **HITL checkpoint**: present the computed verdict with all recorded numbers. The human confirms, or vetoes a GO. Update `books/registry.yaml` `verdict` for this book.

## Output contract
Writes back to `manifest.yaml`: `persona` — **on a GO run only**. A PIVOT has not settled the positioning that defines the persona; writing it early makes a guess indistinguishable from research at every later stage.
Writes back to `books/registry.yaml`: `verdict` for this book's row.
Writes back to `state.json`: `pivot_cycles`, `seed_lineage`, `collector_health`, stage status + verdict.

`research/niche.md` must contain: persona, comp table WITH BSR + review dates + prices, autocomplete harvest (per seed, per marketplace), trend direction, result counts, 3-book shelf, category difficulty, publisher-mix note, negative-review findings, gap statement, differentiation contract (3 promises), asset-feasibility note, trademark status, and the verdict with the numbers that produced it. Missing any → stage incomplete.

## Anti-patterns
- ❌ Writing prose "to test the idea" — research first (separation in time).
- ❌ Cherry-picking comps that make the idea look good — include the strongest competitor.
- ❌ Verdict by enthusiasm — thresholds decide; the human confirms the DATA at the checkpoint.
- ❌ Skipping the asset-feasibility check — that's how screenshot-heavy books stall at stage 5.
- ❌ Skipping the trademark screen — a winning keyword can still be an unsafe brand.
- ❌ Aggressive tool settings — conservative rate limits always; the publishing account is the asset.
- ❌ **Originating a seed.** If the phrase is not in the charter, the harvest, a comp title, or a review, it is not a candidate — it is a guess wearing a candidate's clothes.
- ❌ **Retrying after a refusal.** Exit 3 means stop, not "wait and try a smaller batch". Configuring a proxy is permanently banned (ADR-008), including when the tool itself suggests it.
- ❌ **Filling an `evidence.yaml` field to unblock a verdict.** UNKNOWN is a legal, honest value; a fabricated one is indistinguishable from a measured one at every later stage.
- ❌ **Writing `clear` for a trademark.** You write `no_conflict_found`; only the human writes clear.
- ❌ **Pivoting past the charter.** A new reader problem or a new authority claim is a new book — hand it back.
- ❌ **Treating INCOMPLETE as a verdict.** It is the absence of one. Say what is missing.
