---
name: metadata-seo
description: "Stage 6 (prior to formatter-platform compile) — the book's discoverability package: title/subtitle, 7 KDP keywords, categories, blurbs in 3 lengths, platform variants (KDP vs direct-sales landing copy). Grounded in niche.md research, never invented in a vacuum."
model_tier: cheap
stage: 6
context_budget:
  always_read: [books/<slug>/research/niche.md, books/<slug>/research/keywords.md, books/<slug>/manifest.yaml]
  read: [books/<slug>/outline/outline.md (spine only)]
  never_read: [chapters/, scores/, audits/]
outputs: [books/<slug>/exports/metadata.json, books/<slug>/exports/blurbs.md]
---

# Metadata-SEO

## Purpose
Metadata is the book's interface with the marketplace's rules (Meadows LP5 — work the actual rules, not wishes). Discovery is decided by keywords/categories; conversion is decided by title + blurb. Different jobs, different copy.

Writes back to `manifest.yaml`: `subtitle` (single source of truth).

## Procedure
1. **Title/subtitle**: title = memorable promise; subtitle = keyword-loaded clarity ("X: How to Y in Z without W"). Check against comp titles — distinct but category-legible. Rights check: no trademarks, no misleading claims (kdp-compliance.md rule 6).
2. **KDP keywords (7 slots)**: from research/keywords.md — long-tail, buyer-intent phrases. No repeating title words (wasted slots), no comp author names / "free" / "bestseller" (KDP ToS).
3. **Categories (2)**: from niche research; prefer categories where the comp table shows winnable bestseller ranks.
4. **Blurbs — three lengths**:
   - Short (1 line): for ads/social.
   - KDP description (150–300 words): hook → problem → promise → proof → CTA. HTML-allowed subset for KDP formatting.
   - Direct-sales landing copy (longer): persona-first, includes "what you'll be able to do" bullets pulled from chapter promises (outline), guarantee line.
5. Emit `metadata.json` (structured, all fields) + `blurbs.md` (human review).
6. **HITL micro-gate**: human approves title + KDP description before stage 7.

## Anti-patterns
- ❌ Inventing keywords not grounded in the niche research.
- ❌ Blurb as chapter-summary — blurbs sell the transformation, not the table of contents.
- ❌ One blurb for all platforms — KDP browsers and direct visitors are different contexts (LP3: serve each channel's goal).
