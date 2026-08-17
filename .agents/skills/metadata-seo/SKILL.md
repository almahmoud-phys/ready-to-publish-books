---
name: metadata-seo
description: "Stage 6 (prior to formatter-platform compile) — the book's discoverability package: title/subtitle, 7 KDP keywords, categories, blurbs in 3 lengths, platform variants (KDP vs direct-sales landing copy). Grounded in niche.md research, never invented in a vacuum."
model_tier: cheap
stage: 6
context_budget:
  always_read: [books/<slug>/research/niche.md, books/<slug>/research/keywords.md, books/<slug>/manifest.yaml, books/<slug>/constitution.md, .agents/rules/task-ledger.md]
  read: [books/<slug>/tasks.md (Stage 6 metadata tasks only), books/<slug>/outline/outline.md (spine only)]
  never_read: [chapters/, scores/, audits/]
outputs: [books/<slug>/exports/metadata.json, books/<slug>/exports/blurbs.md, books/<slug>/tasks.md metadata evidence]
---

# Metadata-SEO

## Purpose
Metadata is the book's interface with the marketplace's rules (Meadows LP5 — work the actual rules, not wishes). Discovery is decided by keywords/categories; conversion is decided by title + blurb. Different jobs, different copy.

Writes one human-approved identity package back to `manifest.yaml` and the structured metadata export; downstream work may not mix values from rejected candidates.

## Procedure
1. **Identity freeze**: approve title, subtitle, author/pen name, language, edition, ISBN strategy, and description together before cover typography and final front matter. Record the exact values and a metadata hash.
2. **Title/subtitle**: title = memorable promise. Subtitle must answer, naturally: what the book is, who it serves, what it contains, and the concrete benefit promised. Check against comp titles — distinct but category-legible. Rights check: no trademarks, no misleading claims (kdp-compliance.md rule 6).
3. **KDP keywords (up to 7 slots)**: use evidence-grounded, buyer-intent phrases from research/keywords.md. Do not waste slots through needless duplication, but natural overlap with the title is not automatically prohibited. Never use comp author names, "free", "bestseller", or misleading terms.
4. **Categories**: select up to the platform's current maximum only after checking the live UI/docs. Accuracy and buyer expectation outrank a merely low-competition placement. Record the exact category paths selected in KDP.
5. **Blurbs — three lengths**:
   - Short (1 line): for ads/social.
   - KDP description (150–300 words): hook → problem → promise → proof → CTA. HTML-allowed subset for KDP formatting.
   - Direct-sales landing copy (longer): persona-first, includes "what you'll be able to do" bullets pulled from chapter promises (outline), guarantee line.
6. Emit `metadata.json` (structured, all fields) + `blurbs.md` (human review). Record language separately from the language of the description or translations; the primary book language follows the main reading text.
7. **HITL micro-gate**: human approves the complete identity package, KDP description, keywords, and exact category paths before downstream release work.

## Anti-patterns
- ❌ Inventing keywords not grounded in the niche research.
- ❌ Blurb as chapter-summary — blurbs sell the transformation, not the table of contents.
- ❌ One blurb for all platforms — KDP browsers and direct visitors are different contexts (LP3: serve each channel's goal).
- ❌ Changing the pen name, subtitle, language, or edition after covers/interiors are rendered without invalidating and rebuilding every dependent artifact.
- ❌ Choosing categories because they contain vaguely similar books when the placement misdescribes the product.
