# Release control

Treat generated files as working artifacts until they are promoted into one canonical release
package. A filename containing `final` is not evidence that a file is upload-ready.

## Promotion sequence

1. **Freeze identity metadata**: title, subtitle, author/pen name, language, edition, and ISBN
   strategy. Propagate the exact values to the manifest, title page, cover, metadata export, and
   KDP entry record.
2. **Accept a golden sample** before the complete build:
   - print: title page, populated contents, one story/chapter opening, a representative body
     spread, the transition between major sections, exercises/back matter, and the last page;
   - EPUB: navigation, the two-level story/chapter heading, forced openings, language tags, and
     reflow at small and large font sizes;
   - cover: 100 px front thumbnail and the complete wrap over the current KDP template.
3. Build from source. Never repair an exported PDF or EPUB by hand.
4. Promote only the accepted candidates to `exports/release/` using stable names:
   `paperback-interior.pdf`, `paperback-cover.pdf`, `kindle.epub`, and `kindle-cover.jpg`.
5. Run `scripts/release_preflight.py` and write `exports/release/release-manifest.json`.
6. Upload only files named in that manifest. Record the uploaded hashes, KDP form answers,
   Previewer result, and upload date in `exports/publish-runbook.md`.
7. A first edition, changed trim/paper, changed wrap, or materially changed interior receives a
   physical proof. The owner may waive it only by recording the risk explicitly.

## Dependency invalidation

- Interior content or pagination change -> rebuild the interior, recalculate production page
  count and spine, rebuild the wrap, rerun Previewer, and reconsider the proof.
- Identity metadata change -> rebuild every reader-facing and marketplace artifact.
- Cover artwork or typography change -> rebuild the full wrap, then crop the Kindle front from
  that approved wrap.
- KDP print-setting change -> download a new template and rebuild the wrap.

Never silently reuse a downstream artifact after an upstream dependency changes.

## Canva and other GUI exports

- Set the document to the exact full-cover dimensions from the current KDP calculator/template.
- Export one PDF page only, with no crop marks, guides, template layer, or extra design pages.
- PDF flattening is optional interoperability treatment, not validation. Whether flattened or
  not, inspect the exported page count, MediaBox dimensions, fonts/transparency rendering, and
  Previewer result.
- Do not bake a white barcode box or barcode into the artwork when KDP will place its own barcode.
  Keep the barcode zone free of important text and focal detail; the continuous background may
  remain behind it.

## Proof acceptance

Check trim and fold placement, spine centering, barcode clearance, dark-area detail, small type,
paper show-through, contents accuracy, story/chapter openings, missing or blank pages, final page,
and physical readability. Record pass/fail and photographs or notes. A Previewer pass is not a
physical-proof pass.
