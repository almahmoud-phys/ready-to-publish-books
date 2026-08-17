# Stage 6 GTM review — Luna + Terra

**Date:** 2026-08-14  
**Mode:** parallel, independent, enforced read-only Codex reviews at `xhigh`  
**Brief:** `audits/stage6-gtm-review-brief.md`  
**Status:** recommendations only; no marketplace copy, pen name, imprint, or final cover asset approved by this review

## Reviewers

| Reviewer | Session | Result |
|---|---|---|
| `gpt-5.6-luna`, `xhigh` | `01a00172-ca0e-7e80-80b1-adbca5682bff` | Completed, read-only, untainted, no changed files |
| `gpt-5.6-terra`, `xhigh` | `01a00172-ca02-7103-9235-1100c16eba9a` | Completed, read-only, untainted, no changed files |

Both reviewers independently read the required book evidence rather than judging from a conversation summary.

## Unanimous recommendations

1. Reject the proposed customer-facing sentence explaining that no earlier Puerto Lento book is required. It exposes internal product architecture rather than selling a reader benefit.
2. Replace the existing KDP description with story-first copy. Preserve the letter hook, the adult learner's stop-and-translate problem, ten linked stories, bounded A2 positioning, and a narrative CTA. Reduce internal QA/process vocabulary.
3. Use one conventional human-sounding pen name for this book and future adult Spanish-learning fiction in the same line. Multiple pen names are operationally possible under one legal KDP identity, but fragment Author Pages, reviews, ads, and recognition.
4. Do not use a language-learning brand as the author name and do not invent credentials, native-speaker authority, or a biography.
5. Use no bespoke imprint for this first launch. With a KDP free paperback ISBN, use the platform's `Independently published` treatment; the ebook does not require an ISBN. Introduce a custom imprint only with owned ISBNs and a real catalog/distribution reason.
6. Keep the initial KDP series field empty and the cover unnumbered.
7. Retain Concept 1's category-first hierarchy, but replace its flat envelope icon/clip-art quality, default font feeling, internal candidate labels, and unapproved mystery/series strapline.
8. Generate background imagery only. Keep title, subtitle, level, convention line, and author as deterministic editable typography. Repeat the real 100px thumbnail test after composition.

## Description comparison

### Luna

Strengths:

- Strong quiet-shift opening.
- Concrete story objects: name, empty table, town silence, harbor light.
- Atmospheric closing image.

Weaknesses:

- `adult-focused` remains somewhat project-like.
- `present-tense scenes` and `mixed-tense ending` still expose instructional architecture.
- The QA bullet remains more technical than necessary for conversion.

### Terra

Strengths:

- Stronger learner-problem transition.
- Better explanation of how recurring people and places help the reader keep the thread.
- More customer-facing overall.

Weaknesses:

- `documented checks`, `locale markers`, and `grammar sequencing` still sound like internal process.
- The final `clues` framing slightly overstates how clue-driven the quiet mystery is.

### Synthesis recommendation

Use Terra's structure with Luna's atmospheric specificity, but rewrite the proof bullets in reader language rather than exposing check-suite terminology. The final copy still requires human approval.

## Pen-name recommendation

Architecture: one conventional human-sounding pseudonym for the adult Spanish-reader line, used with identical spelling across ebook, paperback, cover, metadata, and Author Central.

Unscreened candidates proposed by Luna:

- Mara Ellison
- Clara Bennett
- Avery Calder
- Julian Mercer
- Nora Whitfield

Unscreened candidates proposed by Terra:

- Mira Calder
- Elena Vale
- Clara Rowan
- Nina Marlow
- Mara Penn

No candidate is selected or cleared. Exact marketplace/trademark screening is required before use.

## Imprint recommendation

Initial launch: no bespoke imprint. This is separate from the pen name and from a series:

- **Pen name:** public author identity.
- **Series:** groups books for reader navigation.
- **Imprint:** publisher identity associated with an ISBN/catalog.

The trade-off is deliberate: a custom imprint can be introduced for a later catalog, but retrofitting paperback publisher identity may require a new ISBN or edition workflow.

## Concept 1 refinement consensus

Remove:

- `A PUERTO LENTO MYSTERY`;
- `STAGE-6 CANDIDATE · NOT FINAL ART`;
- any volume, book-number, series, or level-sequence label;
- flat clip-art envelope treatment;
- playful/sticker-like badge styling.

Preserve:

- cream/rust/navy/moss palette;
- oversized `SPANISH`;
- unmistakable `A2`;
- recognizable `GRADED READER`;
- two-line title silhouette;
- full-size subtitle and bounded convention line;
- editable typography and a reserved screened-author area.

## Panel-recommended background-only prompt

```text
BACKGROUND ONLY — no typography. Create a sophisticated editorial book-cover background for an adult literary coastal mystery and Spanish graded reader, exactly 1600×2560 pixels, portrait 1:1.6, sRGB.

Use a warm ivory uncoated-paper field with subtle tactile fibers and restrained tonal variation. In the lower-middle area, place one blank, unaddressed, slightly weathered cream envelope resting at a natural three-quarter angle on a dark blue-gray kiosk counter. Give it believable paper edges, a soft directional shadow, and mature editorial realism. Add only a very subtle deep-water blue atmosphere near the lower edge and one small, distant muted-amber harbor glow—quiet enough to suggest Puerto Lento at night without becoming a scenic travel illustration.

Keep the upper 55–60 percent and the central title zone pale, calm, low-detail, and high-contrast so large editable typography can be overlaid later. Preserve broad negative space at the top for category text, in the center for the title, and at the bottom for subtitle, convention line, and author name. The mood is adult, literary, restrained, intelligent, coastal, and quietly suspenseful.

The envelope must be completely blank. Create background imagery only. Do not render any title, subtitle, author, category label, level, words, handwriting, address, stamp, postmark, alphabetic glyph, number, punctuation, logo, brand mark, signature, barcode, QR code, or watermark.
```

### Negative prompt

```text
text, words, letters, alphabet, glyphs, numerals, punctuation, handwriting, fake writing, scribbles, address, stamp, postmark, logo, emblem, brand mark, signature, watermark, barcode, QR code, title, subtitle, author name, label, typography, child illustration, cartoon, clip art, kawaii, picture book, primer, classroom, workbook, flashcards, pencils, notebooks, toys, children, cute animals, flags, maps, country outlines, tourist postcard, travel poster, resort imagery, cultural stereotypes, people, faces, hands, multiple envelopes, supernatural ghost, fantasy, neon, glossy 3D, clutter, busy background, hard detail in text zones, distorted perspective, low resolution
```

## Required next gate

The human must still decide:

1. final KDP description;
2. exact pen name;
3. acceptance of no bespoke imprint;
4. AI image provider/model and cost authorization for the background-only comparison.

After the exact pen name is chosen, run the final-mark screen before changing `manifest.yaml` or producing final cover typography.
