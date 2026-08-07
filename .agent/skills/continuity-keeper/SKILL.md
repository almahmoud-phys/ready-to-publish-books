---
name: continuity-keeper
description: "Stage 2 (after each parallel batch) — guard the book's consistency using rolling summaries only. Detects term drift, promise breakage, canon conflicts. Runs on summaries, never full chapters."
model_tier: cheap
stage: 2
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/bible/terminology.md, books/<slug>/bible/canon.md]
  read: [books/<slug>/summaries/, books/<slug>/outline/]
  never_read: [books/<slug>/chapters/ (full), scores/, audits/]
outputs: [books/<slug>/summaries/continuity-report.md]
---

# Continuity Keeper

## Purpose
The balancing loop (Meadows LP8) inside drafting: cheap, frequent correction beats expensive late repair. Parallel chapter-writing creates drift; this skill catches it after each batch while fixes are still cheap.

## Procedure
1. Load all summaries + bible + outline contracts.
2. Scan for four drift classes:
   - **Term drift**: same concept, different names (violates terminology.md).
   - **Canon conflict**: examples/case studies contradicting canon.md or each other.
   - **Promise breakage**: a chapter summary doesn't deliver its contract promise, or delivers another chapter's promise (duplication).
   - **Dependency breaks**: chapter NN uses something only defined in NN+3.
3. Emit `continuity-report.md`: findings as precise directives — "chapter 4: rename X→Y", "chapter 7 summary missing claim Z".
4. Route: directives go to `chapter-writer` as micro-fix loop-backs (not full rewrites). Update summaries after fixes.
5. New canon candidates from summaries → propose additions to bible/canon.md (human approves at next gate; bible stays append-disciplined).

## Constraints
- **Never read full chapters.** If a summary is too thin to judge, the fix is a better summary — flag "defective summary: chapter NN".
- Reports are directives, not essays. One line per finding.

## Anti-patterns
- ❌ Scope creep into editing — style/quality is stage 3–5's job.
- ❌ Letting the report grow unactionably long — if > 15 findings, the batch was too big; recommend smaller batches.
