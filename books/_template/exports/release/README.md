# Release candidates only

This directory is the promotion boundary between working exports and platform upload files.

- Do not author or manually edit files here.
- Promote only validated artifacts built from repository sources.
- Generate `release-manifest.json` with the KDP release-preflight script.
- The publish runbook may name only files recorded in that manifest.
- Any change to content, pagination, trim, paper, bleed, cover, or metadata identity invalidates the
  manifest and requires a fresh promotion, Previewer inspection, and proof decision.

The words `final`, `approved`, or `print-ready` in a filename are not release evidence.
