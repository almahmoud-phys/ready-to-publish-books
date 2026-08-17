# Paperback cover

Verified against official KDP help on 2026-08-15. Always download a new template after the final interior is stable.

## Deliverable

The upload is one continuous PDF containing back cover, spine, and front cover. All covers have bleed.

## Full-wrap-first construction

- Create one continuous background at the exact full-cover dimensions from the current KDP
  template: outside bleed + back + spine + front + outside bleed.
- The continuous background must reach every canvas edge and cross both spine folds without a
  seam, panel border, blank spine strip, or hard color change.
- Do not generate or assemble separate back, spine, and front background images. Even perfect
  on-screen alignment can expose a discontinuity after normal folding and trimming variance.
- Safe areas constrain important text and focal elements only. They are never background bounds.
- Add typography, back copy, and barcode treatment as editable overlays on the full-wrap master.
- Once that master is approved, derive the eBook cover by cropping the exact front trim box (not
  the bleed or spine) from the completed wrap, then export to the current eBook-cover specification.
- Any later print pagination change invalidates the spine width, full-wrap geometry, and derived
  front crop; recalculate before re-exporting.

## Geometry

Current KDP formulas:

- Cover width = outside bleed + back width + spine width + front width + outside bleed.
- Cover height = top bleed + trim height + bottom bleed.
- Bleed is 0.125 in per outside edge (3.175 mm; KDP may display 3.17 or 3.2 mm).

Current paperback spine factors:

| Interior | Thickness per page |
|---|---:|
| Black ink, white paper | 0.002252 in / 0.0572 mm |
| Black ink, cream paper | 0.0025 in / 0.0635 mm |
| Premium color | 0.002347 in / 0.0596 mm |
| Standard color | 0.002252 in / 0.0572 mm |

Use `../scripts/paperback_cover_geometry.py` to check the arithmetic. Use the calculator/template for production.

## Spine text

- KDP's live page uses inconsistent phrasings—“at least 79,” “more than 79,” and an 80-page Cover Creator minimum. Use 80 production pages as the conservative operational threshold.
- Keep spine text at least 0.0625 in (1.6 mm) from each fold.
- Page-count eligibility is not geometric fit. Subtract both fold margins and verify that a legible wordmark fits; omit spine text on a technically eligible but very narrow spine.

## Safe placement and variance

- Keep front/back text inside the template's safe area and never let it enter the spine.
- KDP's page states a minimum 0.125 in inside trim lines for front/back text. Use the downloaded template's safe-area guides when they are more conservative.
- Avoid narrow borders and hard color changes exactly on fold or trim lines; normal production movement makes them look uneven.
- Reserve the template's barcode area. If the cover has no barcode, KDP can place one.

## Image and PDF checks

- Images at final placed size: minimum 300 DPI.
- Flatten layers/transparencies and embed fonts.
- Use a consistent print color space; KDP recommends CMYK and no spot colors.
- Text must be at least 7 pt and have sufficient contrast.
- Remove the downloaded template, guides, crop marks, color bars, and software labels before export.
- No encryption/security. One PDF. KDP maximum is 650 MB; it recommends 40 MB or less for performance.
- Title, subtitle, author, edition, and ISBN must exactly match title setup.

## Freeze order

1. Freeze trim, ink, paper, and bleed.
2. Build and validate the final interior.
3. Obtain the final production page count in Previewer.
4. Download the matching calculator template.
5. Build the wrap, validate it in Previewer, and order a proof.

Any pagination change after step 3 invalidates the spine and wrap width.
