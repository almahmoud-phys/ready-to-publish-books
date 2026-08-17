# Stage 6 Review Build Report

Built: 2026-08-15

This is the review package requested by the owner. It is a complete bilingual reading draft, not
a publication authorization. No new manuscript revision loop was opened.

## Deliverables

| Deliverable | Size | SHA-256 | Result |
|---|---:|---|---|
| `master.epub` | 853,003 bytes | `552625f23f6ed2888d74ff107b75dd105765e97a94ce5dbac93a7bd0295e47bc` | EPUB 3.3 valid; embedded 1600×2560 front cover; author `Nina Marlo` |
| `print/interior.pdf` | 139,191 bytes | `90aaa29bf4d77a5f27858e228873085b30aa31c13ef453cab774cd5b2f1d5d2f` | 81 manuscript pages / 82 KDP production pages; 360×576 pt (5×8 in) |
| `direct/reader.pdf` | 136,615 bytes | `d5cdbb089208a7034e83f07693d65aeb45601e5a20f1316795c4401da77e1159` | 63 pages; US Letter |
| `kdp/front-cover.jpeg` | 825,422 bytes | `6a75f6b496f5cc091ff43811a11afedfc0199f0f6fca39c7550da54e91f798a4` | 1600×2560 ebook-cover candidate; byline `Nina Marlo` |
| `kdp/print-cover.pdf` | 5,696,534 bytes | `1992b9366afe05c737a0ffc6204d00f267b7a41729f98fe70130449f3fca9c36` | One-page back/spine/front wrap using the owner-supplied back background; 265.557×209.55 mm; blank 5.207 mm spine; no baked-in barcode field |

The KDP EPUB/PDF copies are byte-identical to their master/print sources. The direct EPUB is also
byte-identical to `master.epub`.

## Assembly

Order: title page; ten Spanish narratives; English Translations with ten aligned stories; Spanish
exercises at the back. The reader-facing AI disclosure was removed by explicit owner instruction;
the private provenance record and mandatory KDP upload disclosure remain. The assembled Markdown
contains 15,733 whitespace-delimited tokens including its Pandoc metadata block.

The title/subtitle are document metadata rather than duplicate body headings. The print build uses
an unnumbered, two-sided `book` layout with `openany`. Each story opening now separates a small,
blue small-caps `Historia N` / `Story N` label from its larger display title, while the complete
combined heading remains available to the TOC, bookmarks, and running heads.
The EPUB now uses the same hierarchy: each opening contains a separately styled small label and
larger serif title, while its navigation entry retains the full label and title.
The restored contents lists the ten Spanish stories, the ten English translations, and the exercise
section exactly once. Repeated exercise labels stay out of navigation. All 20 narrative openings
carry an explicit page-break marker; the exercise sets do not.

## Validation

- EPUBCheck 5.3.0 against EPUB 3.3: 0 fatals, 0 errors, 0 warnings, 0 infos.
- Translation alignment/source-freshness gate: 10/10 chapters pass.
- Spanish XHTML language switching: 21 `lang="es"` and 21 `xml:lang="es"` attributes.
- LaTeX verbose render: no overfull or underfull boxes. Only harmless template rerun/caption
  warnings appeared; Pandoc completed its reruns.
- Visual PDF checks: first Spanish opening and first English opening confirm the two-level heading
hierarchy and increased title-to-body spacing; page geometry is 5×8 in / US Letter respectively.
Text extraction found 20/20 story openings at page tops in each PDF. The wrap preview confirms the
back copy, uninterrupted manual-barcode area, blank spine, safe-area placement, and approved
front-cover match.
- The downloaded KDP template independently confirms the 5×8 trim, 82-page cream-paper setup,
  5.21 mm spine, 265.56×209.55 mm outer size, fold lines, live area, and exact barcode rectangle.
- Regression checks: 45 passed; generated frontmatter tests confirm no reader-facing AI disclosure.

Toolchain: Pandoc 3.10.2; XeTeX 0.999994 / TeX Live 2022; EPUBCheck 5.3.0.

## Gate Status and Remaining Human Inputs

The EPUB/PDF format checks pass. Full repository Gate E remains `FAIL` because originality evidence
is unrun and the generated cover background's provider, model, and actual cost have not been logged.
The Gate-E rule now correctly separates private KDP upload-form answers from reader-facing book
copy. No reader-facing AI notice is required by that gate.

The trim, paperback specification, pen name, bilingual claim boundary, interior, and review wrap are
now locked. Before publication, replace or supply background 02 at native ≥300-DPI output and record
its provider/model/cost, then run KDP Previewer and order a physical proof. Translation meaning
remains subject to the owner's requested read.
