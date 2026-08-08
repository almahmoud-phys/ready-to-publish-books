# Niche research — llm-cost-routing-playbook

**Stage 0 · run 1 · 2026-08-08 · marketplace: us (amazon.com), department: books**
**Verdict: PIVOT** — demand is real, the *entry phrase is wrong*. Details in §6.

Every number below was produced by a tool run recorded in `.kdp-research/`, not estimated.
Rows are projected into `research/niche-ledger.csv` (102 rows). Raw exports:
`.kdp-research/exports/trends-pivot-2026-08-08.json`, `.../score-pivot-candidates-2026-08-08.txt`.

---

## 1. Demand evidence

### 1a. Autocomplete harvest (KDP Scout, depth 1, `--department books`)

A harvest of 0 is ambiguous — no buyer language, or a blocked collector. The control seed
distinguishes them and was run first.

| Seed | Keywords | Read |
|---|---:|---|
| `historical fiction` *(control)* | 28 | collector healthy — a 0 below is real signal |
| `llm` | 23 | the live shelf; see 1b |
| `generative ai` | 18 | broad shelf, adjacent |
| `ai agents` | 17 | adjacent shelf, hot |
| `ai engineering` | 14 | 9 of 14 are Chip Huyen author/format variants — one book owns this phrase |
| `prompt engineering` | 12 | crowded, established |
| `llmops` | 4 | thin; and see the trend line in §1c |
| `llm inference` | 3 | narrow but real |
| `llm evaluation` | 2 | narrow but real |
| `llm deployment` / `llm ops` / `llm quantization` | 1 each | narrow |
| `ai cost` | 1 | the single hit is "ai costume" — noise, not signal |
| **`llm cost`** | **0** | **the book's own title phrase has no buyer language** |
| **`llm routing`** | **0** | **same** |

### 1b. What buyers actually type after "llm" (23 harvested, noise removed)

`llm agent` · `llm books` · `llm deployment` · `llm evaluation` · `llm handbook` ·
`llm inference engineering handbook` · `llm for dummies 2026` · `llm java` · `llm ops` ·
`llm persona` · `llm quantization` · `llm rag` · `llm security` · `llm visibility`

Discarded as non-book intent: `lem meat grinder`, `llm t shirt`, `llm usb`, `llm gift`,
`llm computer 128gb ram`, `llm nas`, `llm kadai`, `llm wvals`, `llm let's launch more`.

The cost problem **is** in there — but expressed as *inference*, *quantization*, *deployment*,
*ops*. Never as "cost", never as "routing".

### 1c. Trend direction (Google Trends via trendspyg, `today 12-m`, 53 weekly points)

| Term | 12-mo avg | First 26 wk | Last 26 wk | Peak | Direction |
|---|---:|---:|---:|---:|---|
| `llm inference` | 17.3 | 8.1 | 26.5 | 45 | **rising — 3.3× half-over-half** |
| `prompt engineering` | 47.4 | 31.0 | 63.8 | 100 | rising, high volume |
| `llmops` | 1.2 | 0.8 | 1.7 | 5 | **flat at ~zero — the term never took** |

The last 4 weekly points decay for all three terms (`llm inference` 36 → 6), including the
partial current week. Weekly Trends data is noisy at this scale; the half-over-half direction
is the signal, the tail is not. Re-check at the next staleness refresh.

### 1d. Review velocity, price points, comp BSR
**NOT COLLECTED.** Requires product-page snapshots (medium-risk tier) and the top-10 human
verification. Deliberately not run: the PIVOT verdict below does not depend on them, and a
GO does. See §7.

---

## 2. Competition measurement

`niche-score` (Amazon search, top-10 analysed) returned one complete score before Amazon
began refusing the search probes:

| Keyword | Score | Reading |
|---|---:|---|
| `llm inference` | **43 / 100** | CHALLENGING — established competition, needs strong differentiation |
| `llm deployment`, `llm evaluation`, `llmops`, `llm cost optimization` | — | search refused (CAPTCHA) — backed off per ADR-008 |

Comps observed on those result pages:

| Book | Reviews | Rating |
|---|---:|---:|
| LLM Engineer's Handbook | 219 | 4.6 |
| AI Systems Performance Engineering: Optimizing… | 41 | 4.4 |
| LLMs in Production: Engineering AI Applications | 35 | 4.5 |
| Knowledge Graphs and LLMs in Action | 20 | 4.4 |
| 50 ML Projects To Understand LLMs | 13 | 5.0 |
| LLM Inference Optimization: State-of-the-Art Re… | — | — |
| Mastering LLM Evaluation: How to Judge, Score… | — | — |
| Top 150 Interview Questions and Answers on LLM… | — | — |

**3-book shelf**: LLM Engineer's Handbook · LLMs in Production · AI Systems Performance
Engineering. The shelf exists — that is the point. One strong anchor (219 reviews = validated
buyers) surrounded by 13–41-review titles = a beatable neighbourhood, not a wall.

**Category difficulty / result counts / publisher mix**: NOT COLLECTED (same probe block).

---

## 3. Differentiation

**Gap statement (provisional, pending the GO data):** the shelf teaches how to *build* and
*serve* LLM systems; none of the observed comps is organised around the number the buyer is
actually judged on — cost per successful task in production.

**Differentiation contract**: NOT WRITTEN. It must be drawn from negative-review mining of
the comps above (§7), not from intuition. Writing it now would be exactly the
enthusiasm-over-thresholds anti-pattern the gate exists to stop.

**Authority fit / asset feasibility / trademark screen**: NOT RUN — all three are GO-gate
inputs, and the verdict is PIVOT.

---

## 4. Persona

**NOT WRITTEN.** The manifest tags `persona` as a stage-0 output, and a PIVOT means the
positioning that would define the persona is not settled. It gets written back to the
manifest on the GO run, not this one.

---

## 5. What this run cost

Autocomplete mining: 16 seeds × ~27 rate-limited queries. Search probes: 8 (4 completed,
4 refused). Trends: 1 browser session. No product-page scraping. No proxies, no UA evasion.

---

## 6. Verdict — PIVOT

**Not KILL:** demand and a shelf both exist. `llm inference` is rising 3.3× half-over-half,
its Amazon shelf has a 219-review anchor and several beatable titles, and the buyer language
around cost (`quantization`, `inference`, `deployment`, `ops`) is present in autocomplete.

**Not GO:** the book's own title words score zero. `llm cost` = 0 keywords, `llm routing` = 0,
`ai cost` = 1 and it is "ai costume". Nobody is searching for this book by the name it has.
A book that cannot be found by its own subject is a discoverability failure decided at stage 0,
not at stage 7.

**The positioning question is answered by the data, not by preference:**

- ❌ **Micro-niche on cost/routing as the shelf** — no buyer vocabulary. Rejected.
- ❌ **Reposition to the LLMOps shelf** — `llmops` averages 1.2/100 on Trends over 12 months
  and yields 4 autocomplete keywords. The term never crossed into buyer language. Rejected.
- ✅ **Enter on the inference/serving shelf, keep cost as the angle** — the phrase people
  search (`llm inference`, `llm deployment`, `llm quantization`) carries the problem the book
  actually solves. Cost-per-token and routing become the *differentiator inside* that shelf,
  not the shelf itself.

**Recommended next seed:** `llm inference` (primary), `llm deployment` and `llm quantization`
(secondary). Title language should lead with inference/serving and carry cost as the promise.

**Re-run scope (Steps 1–2 on the new seeds):** review velocity + price points + comp BSR,
result counts and category difficulty, negative-review mining on the 8 comps above, then the
trademark screen on the retitle candidates. Only then can this book earn a GO.

---

## 7. Data deliberately not collected on this run

| Missing | Why | Needed for |
|---|---|---|
| Comp BSR, prices, review dates | Medium-risk product-page tier; top-10 needs live human verification | GO |
| Search result counts, category difficulty, publisher mix | Amazon began refusing search probes; backed off (ADR-008) | GO |
| Negative-review mining | Depends on the comp set above | GO (differentiation contract) |
| Trademark screen (USPTO + EUIPO) | Runs on the retitle candidates, which the pivot produces | GO |
| Persona, differentiation contract | Outputs of the settled positioning, not of this run | GO |

The verdict above rests only on data that was actually collected. Nothing in §6 depends on a
row in this table.
