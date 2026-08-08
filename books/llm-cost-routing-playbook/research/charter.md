# Charter — llm-cost-routing-playbook
# Stage-0 only. Deliberately not in manifest.yaml: the manifest is loaded at EVERY stage and
# capped at ~60 lines (managed context rule 1); this file is read by stage 0 alone.
#
# The loop may not edit this file. It is the goal, fixed in an artifact so the search runs
# inside it rather than around it (Meadows LP3). Written 2026-08-08, after stage-0 run 1.

reader_problem: A hands-on inference or platform engineer operates an LLM service but cannot compare routing, quantization, batching, caching and deployment choices in the unit that actually matters — cost per successful task under real traffic.

useful_outcome: The reader instruments one workload, calculates cost per successful task alongside quality and latency, runs reproducible before/after experiments, and ships a documented serving and routing policy with rollback thresholds.

authority_envelope: Has personally operated at least one LLM inference/serving workload under real production traffic for 30+ consecutive days, with access to both task-success/evaluation results and actual provider/cloud costs, and personally implemented and observed the before/after effects of routing plus at least one of quantization, batching, caching, fallback or capacity change. ATTESTED BY THE AUTHOR 2026-08-08.

authority_exclusions: Model training and fine-tuning economics; kernel and compiler engineering; vendor-wide performance claims; any benchmark not reproduced from the author's own data or explicitly cited; legal and security guidance.

allowed_adjacency: [retitle, sub-niche]   # only within sourced inference/serving language — see below

max_pivot_cycles: 2

INVARIANT:
A pivot must preserve reader_problem and authority_envelope and must cite evidence for its new angle.
Failing either means it is not a pivot, it is a different book — stop and hand back to the human.

Concretely, the chain this forbids: cost routing -> inference -> AI engineering -> generic AI
guide. Each step looks small, and the end of it is a book with demand and no author.

## Adjacency, precisely

Retitle or narrow only within sourced inference/serving language: `llm inference`,
`llm deployment`, `llm quantization`. Persona may move only among hands-on inference/platform
engineers holding the same operational responsibility. Cost and routing stay the internal
angle, never the shelf name. Do NOT drift to LLMOps or to a generic AI guide.

## Why these bounds — from run-1 evidence

Every claim cites `research/niche.md`; none of it is market intuition.

- **The shelf is inference, not cost.** `llm cost` and `llm routing` returned 0 autocomplete
  keywords against a healthy collector (control `historical fiction` = 28). `llm inference`
  rose 3.3x half-over-half on 12-month Trends. `llmops` averages 1.2/100 — that term never
  took, which is why it is excluded from adjacency rather than left open.
- **The shelf is enterable but not soft.** `llm inference` scored 43/100 (CHALLENGING): one
  219-review anchor (LLM Engineer's Handbook) surrounded by 13-41-review titles. Entering a
  challenging shelf is what makes the authority envelope load-bearing rather than decorative.
- **2 cycles, not 3.** Run 1 already spent one (cost/routing -> inference). One evidence-backed
  move remains, most likely toward `llm deployment` or `llm quantization`. After that, stop.

## OPEN RISK — carried into stage 1, must close before drafting

**Evidence publishability is UNRESOLVED.** The author has production data but has not yet
determined what may legally be shown: absolute figures, anonymized relative deltas, or
reproducible synthetic workloads only.

This is not a detail. It decides the differentiation contract, because "measured under real
production traffic" is the one promise on this shelf a better writer cannot simply copy — every
comp observed competes on explanation, and explanation is no longer scarce. It also decides
asset feasibility, and stage-5 fact-checking has teeth: a claim that cannot be verified is
rewritten or cut, so figures invented to fill a gap will not survive to publication.

Settle it before any chapter that depends on figures is drafted. Until then no chapter may
assume absolute cost numbers will be available.
