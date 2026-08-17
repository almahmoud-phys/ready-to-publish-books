---
name: cover-director
description: "Stage 6 (parallel) — art-direct the cover: concepts, AI image generation prompts, typography overlay, back cover + spine for print. ADR-005: AI images locked; pure-imagery vs hybrid-typographic sub-decision made HERE with cost/quality data."
model_tier: mid_plus_external_image_api
stage: 6
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/constitution.md, books/<slug>/research/niche.md (persona + comps), .agents/rules/task-ledger.md]
  read: [books/<slug>/tasks.md (Stage 6 cover tasks only), books/<slug>/bible/style-sheet.md]
  never_read: [chapters/, scores/]
outputs: [books/<slug>/exports/cover/front.png, books/<slug>/exports/cover/print-spread.pdf, books/<slug>/exports/cover/cover-notes.md, books/<slug>/tasks.md cover evidence]
---

# Cover Director

## Purpose
The cover is a market artifact, not art: it must win a 1-inch thumbnail comparison against the comps in niche.md. Judge everything at thumbnail size.

## Procedure
1. **Identity and asset intake**: require frozen title, subtitle, author/pen name, language, edition, and ISBN strategy before final typography. For every source asset, record provenance/license or AI provider/model, cost, pixel dimensions, intended crop, and effective print DPI. Reject undersized or untraceable assets before concept approval.
2. **Comp scan**: covers of the top comps — extract category visual conventions (color, typography, imagery). The cover must signal the category instantly, then differentiate (Meadows: rules of the system first — LP5 — then local quality).
3. **Concept generation**: 3 concepts, each one sentence + prompt. Selection criteria: thumbnail legibility, category signal, differentiation.
4. **Sub-decision (ADR-005)**: choose per concept — pure AI imagery vs hybrid typographic composition. Decide with data: generation cost, legibility test results, disclosure implications. Record the decision + rationale in cover-notes.md.
4. **Lock print geometry first**: coordinate with `formatter-platform` to freeze binding, trim,
   ink, paper, reading direction, bleed, and the final production-PDF page count. Calculate the
   wrap independently, then download the matching KDP template. The template is authoritative.
5. **Generate one continuous wrap background**: generate a single, text-free image covering the
   complete bleed + back + spine + front canvas. Compose it as one uninterrupted scene or pattern;
   never create separate front/back/spine backgrounds and join them at the folds. Keep the back
   quieter for copy and the front stronger for the focal image, but do not draw panel boundaries,
   seams, borders, spine strips, guides, barcode boxes, or typography into the artwork. Safe-area
   dimensions constrain text placement only; backgrounds extend to every file edge and through
   both spine folds.
6. **Build the full cover master**: overlay editable typography, back-cover copy, optional spine
   text, and the barcode treatment on the continuous wrap background. Title must remain readable
   at 100px-wide front-cover thumbnail size. Do not introduce a hard color transition at a fold.
7. **Derive the eBook cover**: after the print master is approved, crop the exact front **trim**
   region from the completed full wrap and export it to the eBook specification. Do not create or
   regenerate an independent Kindle composition; the print wrap is the visual source of truth.
8. **Render validation**: inspect the actual raster/PDF export, not just the SVG or Canva canvas. Verify pixel dimensions, one-page PDF structure, full-wrap dimensions, safe areas, thumbnail, embedded fonts/transparency, and barcode clearance. Converter exit success is not visual equivalence.
9. **Compliance**: append source provenance and cover generation method (API + model when applicable) to compliance_log — mandatory regardless of sub-decision.
10. **HITL micro-gate**: human approves the final thumbnail and the complete wrap over the current KDP template.

## Anti-patterns
- ❌ Full-size aesthetic judgments — buyers see thumbnails.
- ❌ Text rendered by the image model — typography is overlaid, never baked in (image models mangle text; also makes the title uneditable).
- ❌ Joining independently generated front and back images at the spine — normal trim/fold
  variance exposes the discontinuity.
- ❌ Fitting artwork to the safe area — safe areas are for important text and focal objects, not
  background boundaries.
- ❌ Designing Kindle first and expanding it into a wrap — generate and approve the continuous
  print master, then crop its front trim region for Kindle.
- ❌ Forgetting the compliance log entry — cover disclosure is part of KDP's AI questions.
- ❌ Approving an image before verifying it can deliver at the required effective print resolution.
- ❌ Trusting `sips`, `qlmanage`, Canva, or any converter without inspecting the exact exported file.
- ❌ Baking in a white barcode box when KDP will place the barcode — reserve the zone, but let the continuous background run beneath it.
