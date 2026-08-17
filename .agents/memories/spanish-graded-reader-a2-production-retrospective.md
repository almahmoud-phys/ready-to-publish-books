# Spanish graded reader A2 — production retrospective

**Captured:** 2026-08-17  
**Scope:** Stage 6 through the first KDP paperback proof request. This is an interim production
retrospective, not evidence that Gate E or publication passed.

## Outcome at capture

The book reached KDP Previewer as an 81-page, 5×8-inch, no-bleed paperback on cream paper with a
matte cover. The owner reviewed the page thumbnails and requested one proof copy. Gate E remains
failed in repository state until originality and cover-provenance issues are closed, the exact
uploaded files are reconciled, and the physical proof is inspected. A proof request is not a pass.

## What worked

- The outline, story bible, cumulative vocabulary/grammar gates, continuity pass, adversarial audit,
  scorer, proofreader, and fact-checker created a strong content spine before packaging.
- Keeping Spanish narratives, complete English translations, and exercises as separate source
  components made it possible to change assembly order without rewriting the stories.
- Source-hash and block-parity checks caught translation drift. Their claim boundary stayed honest:
  structural alignment is not semantic translation quality.
- Human review found presentation failures machines missed: primitive story headings, missing
  contents, missing page breaks, insufficient title spacing, a moving badge, and visible cover seams.
- A continuous full-wrap background solved the seam problem created by separately designed front,
  back, and spine panels. Deriving the ebook front from the wrap preserves one visual identity.
- KDP's calculator/template and Previewer were indispensable final environment checks. Local size
  checks alone could not prove barcode placement, fold tolerance, or platform rendering.
- The final metadata discussion improved the subtitle by forcing four answers: what the book is,
  who it is for, what it contains, and what benefit it credibly promises.

## What went wrong or consumed avoidable time

| Failure mode | Cost | Default control for future books |
|---|---|---|
| Bilingual text was in scope but had no explicit producer/verifier/assembly owner | Late translation and compiler work | Stage-1 component-ownership matrix |
| Pandoc and validation dependencies were discovered during final production | Work stalled while tools installed | Representative print/EPUB build in Stage 1 |
| Full books were exported before one opening was visually approved | Rebuilt PDF and EPUB repeatedly | Golden-sample approval before bulk export |
| Print and EPUB inherited different heading behavior | One-line EPUB headings survived after PDF repair | Shared semantic heading model plus format-specific sample checks |
| Contents, story page breaks, and title spacing were not acceptance tests | Regressions reached review files | Deterministic contents/page-start checks and rendered inspection |
| Front, back, and spine were designed independently | Visible discontinuity at folds | One continuous full-wrap master after final page count |
| Asset resolution and provenance were checked late | Approved-looking art remained a Gate-E blocker | Asset intake records provider, model/source, license, cost, pixels, placed DPI |
| Pen name, subtitle, and related metadata settled late | Cover/interior/store fields diverged and required rework | Freeze one production identity before final packaging |
| Rasterizers silently changed SVG text alignment | A2 badge shifted in PNG | Inspect the exact raster/PDF produced by the shipping toolchain |
| Canva's design dimensions were treated as proof of the exported PDF | A local Canva PDF contains three pages despite the correct canvas size | Machine-check exported page count and MediaBox dimensions |
| Many files were called “final” | It became unclear which bytes were uploaded | Promote to `exports/release/` and generate a hash manifest |
| Public AI-disclosure prose and KDP's private form were conflated | Unnecessary reader-facing copy and policy confusion | Keep public copy editorial; keep truthful private form answers in the runbook |
| Categories and keywords were optimized while operating the live form | Slow, screenshot-driven decisions | Prepare an approved metadata worksheet before opening KDP |
| State lagged behind KDP actions | “Proof requested” risked being mistaken for readiness | Explicit Previewer, upload-record, proof-requested, proof-passed states |

## Reusable decisions

1. Plan the whole product, not only chapters. Translations, exercises, front matter, navigation,
   cover assets, platform metadata, and validation each need an owner and test.
2. Use a single release-candidate boundary. Working exports remain replaceable; promoted artifacts
   are immutable and identified by hashes.
3. Verify exports, not editor canvases. A correct Canva document, SVG, or Markdown source does not
   prove the PDF/PNG/EPUB delivered to KDP.
4. Cover workflow is page-count dependent: finalize interior → calculate wrap → build one continuous
   master → derive ebook front → preflight → Previewer → physical proof.
5. Visual and semantic quality need human checkpoints. Automated gates remain valuable, but cannot
   judge narrative translation meaning, thumbnail persuasion, page rhythm, or physical print.
6. Do not publish a first edition merely because Previewer looks clean. Inspect the physical proof,
   or record an explicit owner waiver and accept the risk.

## Current book follow-up

- Reconcile the exact local files and hashes with what was uploaded to KDP.
- Do not promote `cover-Mouhamad-Canva.pdf`: local preflight finds three PDF pages. The one-page
  `print-wrap.pdf` passes geometry preflight, but its content/provenance must match the approved and
  uploaded cover before it can replace anything.
- Close originality and cover-provenance/resolution blockers.
- Inspect the received proof: trim, crop, fold/spine, barcode, color/density, fonts, contents,
  story starts, title spacing, blank pages, and final page.
- Rebuild/re-upload if the proof exposes a material defect; otherwise complete Gate E and Stage 7,
  then reconcile the live storefront after publication.
