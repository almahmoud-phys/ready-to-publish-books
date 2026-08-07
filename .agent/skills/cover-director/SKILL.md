---
name: cover-director
description: "Stage 6 (parallel) — art-direct the cover: concepts, AI image generation prompts, typography overlay, back cover + spine for print. ADR-005: AI images locked; pure-imagery vs hybrid-typographic sub-decision made HERE with cost/quality data."
model_tier: mid_plus_external_image_api
stage: 6
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/research/niche.md (persona + comps)]
  read: [books/<slug>/bible/style-sheet.md]
  never_read: [chapters/, scores/]
outputs: [books/<slug>/exports/cover/front.png, exports/cover/print-spread.pdf, exports/cover/cover-notes.md]
---

# Cover Director

## Purpose
The cover is a market artifact, not art: it must win a 1-inch thumbnail comparison against the comps in niche.md. Judge everything at thumbnail size.

## Procedure
1. **Comp scan**: covers of the top comps — extract category visual conventions (color, typography, imagery). The cover must signal the category instantly, then differentiate (Meadows: rules of the system first — LP5 — then local quality).
2. **Concept generation**: 3 concepts, each one sentence + prompt. Selection criteria: thumbnail legibility, category signal, differentiation.
3. **Sub-decision (ADR-005)**: choose per concept — pure AI imagery vs hybrid typographic composition. Decide with data: generation cost, legibility test results, disclosure implications. Record the decision + rationale in cover-notes.md.
4. **Generate**: image API per concept; typography overlay via ImageMagick/CSS templates (tooling/). Title must be readable at 100px wide.
5. **Print spread**: front + spine (width from page count — coordinate with formatter-platform) + back cover (blurb from metadata-seo, bio, barcode space).
6. **Compliance**: append cover generation method (API + model) to compliance_log — mandatory regardless of sub-decision.
7. **HITL micro-gate**: human picks the final concept from the 3 (thumbnails side by side).

## Anti-patterns
- ❌ Full-size aesthetic judgments — buyers see thumbnails.
- ❌ Text rendered by the image model — typography is overlaid, never baked in (image models mangle text; also makes the title uneditable).
- ❌ Forgetting the compliance log entry — cover disclosure is part of KDP's AI questions.
