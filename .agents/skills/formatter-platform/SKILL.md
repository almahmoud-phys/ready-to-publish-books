---
name: formatter-platform
description: "Stage 6 (after metadata-seo) — compile chapters into platform-ready packages: EPUB master → KDP EPUB, print PDF, direct-sales EPUB/PDF. Deterministic tooling (Pandoc/LaTeX/epubcheck), not LLM judgment. Toolchain harvested from book-generator (ADR-006)."
model_tier: cheap_with_tooling
stage: 6
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/constitution.md, .agents/rules/style.md (formatting section), .agents/rules/task-ledger.md]
  read: [books/<slug>/tasks.md (Stage 6 packaging tasks only), books/<slug>/chapters/ (final, post-Gate-D), books/<slug>/exports/metadata.json, tooling/pandoc/, tooling/latex/]
  never_read: [scores/, audits/, research/]
outputs: [books/<slug>/frontmatter.md, books/<slug>/exports/master.epub, books/<slug>/exports/kdp/, books/<slug>/exports/direct/, books/<slug>/exports/print/, books/<slug>/tasks.md packaging evidence]
---

# Formatter-Platform

## Purpose
One EPUB master, many channel packages (TRIZ P17 — the channel is a packaging transform, not a new production). Output must pass machine validation, not just look right.

## Prerequisites
Gate D passed (edit log applied, fact flags resolved). Identity metadata is frozen and the required toolchain has passed a representative build. `PIPE-001` must also be absent from the active Stage-6 blockers in `state.json`: formatter-platform may assemble verified English parallel text, but it never generates or verifies translations. No bilingual EPUB/PDF, front matter, or final page count may be produced while translation ownership or independent verification is unresolved. Refuse before writing any output and route back.

## Procedure
1. **Preflight**: record converter/validator versions, fonts, templates, and one small successful build before committing to final pagination. Never discover a missing production dependency during the final export.
2. **Assemble master**: own `books/<slug>/frontmatter.md` (title page and track-appropriate copyright page), chapters in outline order, and back matter. KDP's private AI form answers come from `compliance_log.yaml`; do not insert a reader-facing AI disclosure unless the owner independently requests that copy.
3. **Golden sample**: render and obtain approval for the title page, populated contents, one chapter/story opening, representative body spread, major-section transition, exercise/back-matter page, and final page. For EPUB, verify navigation, two-level headings, language tags, reflow, and forced openings at small and large font sizes. Only then run the full build.
4. **EPUB master**: Pandoc with `tooling/pandoc/epub.css` + metadata.yaml. Validate with **epubcheck** — exit 0 required. A valid EPUB can still be visually wrong, so inspect it in a real reader/Previewer.
5. **Print PDF**: use the template for the locked trim, not an assumed default. Render-check every page; verify contents, page breaks, heading spacing, section transitions, final page, and absence of overfull boxes.
6. **Platform variants**:
   - `exports/kdp/`: EPUB + print PDF + KDP metadata injected.
   - `exports/direct/`: EPUB + reader PDF (no print crop settings), bonus-ready folder structure for Gumroad.
   - `exports/wide/`: (M5+) Draft2Digital-compatible EPUB.
7. For bilingual books, run structural alignment automatically and require a named human semantic-translation review; block parity does not prove translation quality.
8. Log working artifacts to compliance_log, but do not call them release files. The KDP release-control step promotes accepted candidates to `exports/release/` and records their hashes.

## Gate E contribution
Golden sample accepted; epubcheck exit 0; PDF renders page-by-page; contents, openings, and endings are correct; artifacts exist and are hashed; semantic translation review is recorded when applicable.

## Anti-patterns
- ❌ Hand-tweaking output files — fix the source or the template, regenerate (Fixes That Fail archetype: patched outputs drift from sources).
- ❌ Skipping epubcheck because "Pandoc output is usually fine."
- ❌ Running every export before approving representative pages — this multiplies small styling defects across the whole book.
- ❌ Treating compile success, a PDF filename, or block parity as reader-quality approval.
