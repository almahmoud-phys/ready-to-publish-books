---
name: kdp-publishing
description: Verify and prepare Kindle eBook, paperback, and hardcover assets for Amazon KDP. Use when choosing trim size or paper, calculating a print cover or spine, checking manuscript and cover PDFs, styling EPUBs, preparing KDP metadata, interpreting Previewer errors, or making a final upload checklist.
metadata:
  model_tier: cheap_with_tooling
  stage: 6
  context_budget:
    always_read: [books/<slug>/manifest.yaml, books/<slug>/constitution.md, .agents/rules/task-ledger.md, .agents/rules/quality-gates.md, .agents/rules/kdp-compliance.md]
    read: [books/<slug>/tasks.md (active KDP publishing task only), books/<slug>/state.json, books/<slug>/exports/, books/<slug>/compliance_log.yaml]
    never_read: [books/<slug>/chapters/ unless content inspection is required, books/<slug>/audits/]
  outputs: [books/<slug>/exports/ KDP assessment or validated assets, books/<slug>/tasks.md KDP evidence]
---

# KDP Publishing

Use current official Amazon KDP documentation as the authority. The local references are an operational digest, not a substitute for rechecking rules that may have changed.

## Required workflow

1. Identify the product: eBook, paperback, or hardcover. For print, record binding, ink, paper, reading direction, trim size, bleed choice, and the page count of the **final PDF at that trim**.
2. Run a production preflight before final design work: required converters/validators installed, fonts available, source-image dimensions and provenance recorded, and a tiny representative build succeeds.
3. Freeze identity metadata before cover typography or final front matter: title, subtitle, author/pen name, language, edition, and ISBN strategy. One approved record must drive the book, cover, metadata file, and KDP form.
4. Inspect the actual deliverables. Never infer print dimensions or page count from a review PDF, source manuscript, word count, or a different trim.
5. Read only the relevant reference files:
   - `references/print-interior.md` for trim, bleed, margins, pagination, and manuscript PDF checks.
   - `references/print-cover.md` for cover geometry, spine, barcode, image, and cover-PDF checks.
   - `references/ebook.md` for EPUB structure, CSS, navigation, and Previewer checks.
   - `references/metadata-compliance.md` for exact-match metadata, rights, and disclosure decisions.
   - `references/source-index.md` for official URLs and refresh triggers.
   - `references/release-control.md` for golden samples, promotion, upload records, GUI exports, and physical-proof acceptance.
6. Reopen the relevant official KDP pages whenever the answer will drive an upload, a costly design, or a compliance claim. Record the verification date.
7. Separate:
   - **KDP requirement**: an explicit platform rule.
   - **Production recommendation**: a conservative choice that reduces rejection or print-variance risk.
   - **Editorial judgment**: whether the physical object feels suitably substantial or readable.
8. Approve representative golden samples before the complete build: print title/contents/story-opening/body/back matter, EPUB navigation/reflow/story headings, and cover thumbnail/full wrap.
9. For a print cover, wait until trim, paper, ink, and final production page count are locked. Run `scripts/paperback_cover_geometry.py` as an independent arithmetic check, then download a fresh KDP template and design against that template. Build one continuous full-wrap background across bleed, back, spine, and front; never assemble independently rendered panel backgrounds at the folds. Safe areas constrain important content, not the background. Derive the eBook cover by cropping the completed wrap's exact front-trim region after approval.
10. Promote only accepted artifacts to `exports/release/`. Run `scripts/release_preflight.py`, write `release-manifest.json`, and upload only the files and hashes recorded there.
11. Validate in KDP Previewer and inspect a physical proof for every first edition or materially changed build. If the owner waives a proof, record the risk explicitly; a proof request is not a proof pass.

## Non-negotiable safeguards

- A cover-calculator entry is only valid for the manuscript formatted at that same trim.
- KDP's formatting guidance says its production count rounds an odd manuscript count up to even. Confirm the resulting count in Previewer before freezing the wrap.
- Cover title, subtitle, author/contributor, edition, and ISBN must exactly match KDP title setup.
- A print-cover upload must be one PDF page at the expected full-wrap dimensions. A GUI document's displayed canvas size does not validate its exported PDF.
- No file becomes authoritative because its name contains `final`. Only promotion into `exports/release/` plus a passing manifest makes it an upload candidate.
- Do not put template guides, crop marks, color bars, placeholder text, or production notes in upload files.
- Do not turn a private KDP upload-form disclosure into reader-facing book copy unless the publisher explicitly wants that copy.
- Do not advise a false upload-form answer. KDP currently distinguishes AI-generated content from AI-assisted content; see `references/metadata-compliance.md` and recheck the live policy.

## Useful command

```bash
python3 .agents/skills/kdp-publishing/scripts/paperback_cover_geometry.py \
  --trim-width 127 --trim-height 203.2 --pages 82 --paper cream --units mm
```

Treat its output as a calculation check. The downloaded KDP template and Previewer remain authoritative for the final upload.

Before upload, run the release check with the locked dimensions and page count:

```bash
python3 .agents/skills/kdp-publishing/scripts/release_preflight.py \
  --interior books/<slug>/exports/release/paperback-interior.pdf \
  --cover books/<slug>/exports/release/paperback-cover.pdf \
  --trim-width-mm <width> --trim-height-mm <height> \
  --cover-width-mm <width> --cover-height-mm <height> \
  --expected-pages <count> \
  --write-manifest books/<slug>/exports/release/release-manifest.json
```
