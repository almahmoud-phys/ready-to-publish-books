# Final Stage 6 GTM review — Luna + Terra

**Date:** 2026-08-14  
**Mode:** parallel enforced read-only Codex reviews, `gpt-5.6-luna` and `gpt-5.6-terra`, both at `xhigh`  
**Brief:** `audits/stage6-final-gtm-brief.md`  
**Status:** reconciled recommendations; human decisions retain authority

## Unanimous findings

1. The human-locked KDP description has no concrete factual or compliance defect. Keep it unchanged.
2. `Avery Calder` must be replaced. Both reviewers found an active publishing identity under that exact name, creating author-page, attribution, retail-search, and discoverability collision risk. This is a market-identity finding, not a legal determination.
3. Starting without a bespoke imprint is appropriate. A KDP free paperback ISBN displays `Independently published`; a custom imprint can be introduced for future books with owned ISBNs. Retrofitting the first published paperback generally requires a new ISBN/new-edition workflow.
4. Keep the first launch standalone, unnumbered, and outside a KDP series.
5. Default the next validated book to another standalone A2 story in Puerto Lento. After two real titles, screen and consider the non-sequential umbrella `Puerto Lento Spanish Readers`.
6. Not every future Spanish graded reader must take place in Puerto Lento. A new setting should become a separate micro-line unless it genuinely belongs to the Puerto Lento narrative world, and it must pass its own niche, quality, and mark gates.
7. The Spanish manuscript source exists, but no verified English parallel text, compiled bilingual interior, or publishable export exists. `PIPE-001` must not be bypassed.

## Background split and owner ruling

- Luna selected background 02 for its stronger adult-literary mood, navy/amber coastal contrast, and more distinctive mystery signal.
- Terra selected background 01 for its broader quiet typography field and smaller envelope.
- Human owner explicitly preferred background 02.

**Ruling:** background 02 is selected. The owner decision breaks the same-family model split. The final composition must keep all title/category text in the pale upper field and use a controlled dark footer for supporting copy.

Both source backgrounds are `816×1312`, below the preferred `1600×2560` production size. The final SVG embeds and scales background 02 to the target canvas. This is acceptable as a visual front-cover candidate because the artwork is deliberately soft and all typography is vector, but the source-resolution limitation remains a production caveat until the owner accepts the rendered result or supplies a native higher-resolution generation.

## Pen-name follow-up

`Avery Calder` is rejected.

Additional accessible checks performed after the panel:

- `Mara Ellison`: rejected; active Amazon/Goodreads author footprint surfaced.
- `Julian Mercer`: rejected; active Open Library author records surfaced.
- `Nina Marlow`: no clear exact author collision surfaced in accessible Open Library, Goodreads, or exact-name web checks.
- `Nora Whitfield`: no clear exact author collision surfaced in accessible checks.

Limitations:

- Google Books API returned a shared-quota `429` and produced no evidence.
- Justia trademark search returned Cloudflare `403` and was not bypassed.
- Search-engine exact-match quality was inconsistent.
- No result is legal clearance.

**Current replacement screening candidate:** `Nina Marlow`, pending human sign-off and the best available final-mark screen.

## Imprint and series answer

A custom imprint may be introduced later for future books by purchasing ISBNs and registering the imprint consistently. It should not be retrofitted onto this first paperback unless a deliberate new edition justifies a new ISBN.

KDP permits adding existing titles to a series later. Therefore the scalable route is:

1. launch this book standalone;
2. validate a second A2 Puerto Lento title;
3. screen `Puerto Lento Spanish Readers`;
4. add both eligible titles to the non-sequential umbrella if the catalog exists;
5. allow other adult graded-reader settings to form their own lines rather than forcing all stories into Puerto Lento.

## Draft-status reconciliation

- Spanish manuscript source: complete, ten chapter files.
- English parallel text: absent as an approved and independently verified production source.
- Compiled bilingual interior: absent.
- Publishable EPUB/PDF/print interior: absent.
- Final print spread: absent because page count, trim, spine, and barcode geometry depend on the interior.

The user's statement that the book draft has not been generated is correct if “book draft” means a compiled bilingual reader/package. It is not correct if it means the Spanish manuscript source.
