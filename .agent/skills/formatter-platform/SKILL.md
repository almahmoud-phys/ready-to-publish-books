---
name: formatter-platform
description: "Stage 6 (after metadata-seo) — compile chapters into platform-ready packages: EPUB master → KDP EPUB, print PDF, direct-sales EPUB/PDF. Deterministic tooling (Pandoc/LaTeX/epubcheck), not LLM judgment. Toolchain harvested from book-generator (ADR-006)."
model_tier: cheap_with_tooling
stage: 6
context_budget:
  always_read: [books/<slug>/manifest.yaml, .agent/rules/style.md (formatting section)]
  read: [books/<slug>/chapters/ (final, post-Gate-D), books/<slug>/exports/metadata.json, tooling/pandoc/, tooling/latex/]
  never_read: [scores/, audits/, research/]
outputs: [books/<slug>/frontmatter.md, books/<slug>/exports/master.epub, exports/kdp/, exports/direct/, exports/print/]
---

# Formatter-Platform

## Purpose
One EPUB master, many channel packages (TRIZ P17 — the channel is a packaging transform, not a new production). Output must pass machine validation, not just look right.

## Prerequisites
Gate D passed (edit log applied, fact flags resolved). Building exports from unresolved content is wasted compute — refuse and route back.

## Procedure
1. **Assemble master**: own `books/<slug>/frontmatter.md` (title page, copyright page — track-aware: assisted includes full copyright assertion; generated includes disclosure note per kdp-compliance.md), chapters in outline order, back matter (about, CTA to mailing list per ADR-004).
2. **EPUB master**: Pandoc with `tooling/pandoc/epub.css` + metadata.yaml. Validate with **epubcheck** — exit 0 required.
3. **Print PDF**: LaTeX interior template (6×9 default; margins per page-count table in tooling/). Render check: page count, no overfull boxes on TOC/chapter starts.
4. **Platform variants**:
   - `exports/kdp/`: EPUB + print PDF + KDP metadata injected.
   - `exports/direct/`: EPUB + reader PDF (no print crop settings), bonus-ready folder structure for Gumroad.
   - `exports/wide/`: (M5+) Draft2Digital-compatible EPUB.
5. Log artifacts to compliance_log (formatter events too — the log is complete or it's useless).

## Gate E contribution
epubcheck exit 0; PDF renders; artifacts exist and are hashed into the compliance log.

## Anti-patterns
- ❌ Hand-tweaking output files — fix the source or the template, regenerate (Fixes That Fail archetype: patched outputs drift from sources).
- ❌ Skipping epubcheck because "Pandoc output is usually fine."
