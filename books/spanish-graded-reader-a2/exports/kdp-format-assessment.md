# KDP Paperback Format Assessment

Verified: 2026-08-15 against current official Amazon KDP help and the Cover Calculator.

## Recommendation

The owner approved **5 × 8 in (127 × 203.2 mm), paperback, black ink, cream paper,
left-to-right, no interior bleed**. The final review interior and exact print wrap now implement
that specification.

## What the current files actually show

| Artifact | Purpose | Size | Pages |
|---|---|---:|---:|
| `exports/print/interior.pdf` | final-trim KDP review interior | 5 × 8 in | 81 manuscript / 82 KDP production |
| `exports/direct/reader.pdf` | direct/review PDF | US Letter | 63 |
| `exports/kdp/print-cover.pdf` | exact back/spine/front wrap | 265.557 × 209.55 mm | 1 |

The calculator screenshot's 63-page input describes the direct US-Letter reader, not the KDP
interior. A cover template must use the page count produced at the final
trim.

## Final 5 × 8 geometry

- KDP production count: **82 pages** (81-page PDF rounded up to even).
- Cream-paper spine: **5.207 mm**.
- Full wrap including bleed: **265.557 × 209.550 mm**.
- Page-count threshold permits spine text, but the spine is too narrow for a comfortable wordmark:
  after the two 1.6 mm fold clearances only about 2.0 mm remains. Recommend **no spine text**.
- Interior margins: 0.75 in inner, 0.625 in outer, and 0.70 in top/bottom—comfortably above
  KDP's current 24–150-page minimums.

## Is the book too small?

It is short, not underbuilt. The assembled bilingual book is about 15,700 words and contains ten
Spanish stories, ten aligned English translations, and the exercises. At 6 × 9 it presents as a
thin 69-page book. At 5 × 8 it becomes an approximately 82-page compact paperback with better prose
line length and stronger physical presence, without padding or enlarging the type artificially.

KDP accepts black-ink cream-paper 5 × 8 paperbacks from 24 through 776 pages, so either count is
technically valid. The 5 × 8 recommendation is an editorial/product judgment, not an acceptance
requirement.

Interior SHA-256: `90aaa29bf4d77a5f27858e228873085b30aa31c13ef453cab774cd5b2f1d5d2f`.
Print-cover SHA-256: `1992b9366afe05c737a0ffc6204d00f267b7a41729f98fe70130449f3fca9c36`.

## Official sources

- https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6
- https://kdp.amazon.com/en_US/help/topic/G201953020
- https://kdp.amazon.com/cover-calculator
- https://kdp.amazon.com/en_US/help/topic/G201834260
