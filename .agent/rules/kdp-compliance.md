# KDP & Platform Compliance (Rule file)

## Disclosure matrix (2026 KDP rules)

| Track | Who writes prose | KDP disclosure | Copyright |
|---|---|---|---|
| `assisted` | Human — AI researches, outlines, edits | **Not required** | Full — human authorship |
| `generated` | AI — human curates/approves | **Required**: text, cover images, translations — even after heavy editing | None on generated portions |

**Rule**: never mix undisclosed. If AI writes prose, the book is `generated`, full stop. Track is chosen at Gate 1 and locked in `manifest.yaml`.

## compliance_log.yaml (append-only, written at every generation event)

```yaml
- event: generate
  skill: chapter-writer
  model: <model-id>
  artifact: chapters/chapter_03.md
  sha256: <hash>
  timestamp: <iso8601>
```

- The orchestrator (M2) appends automatically; in manual (M1) mode, the active skill appends after each artifact.
- `publish-checklist` generates the exact KDP disclosure answers **from this log** — never from memory.
- This file IS the internal record KDP policy recommends. Treat as write-once: corrections are new entries, never edits.

## Hard rules

1. **Originality check** at Gate E: run flagged-passage review (scorer's Originality dimension + spot checks) before any publish.
2. **Fact-check resolution** at Gate D: every claim in non-fiction is `verified | rewritten | cut` — no flag survives export.
3. **Rate cap**: max 3 titles/day to KDP. Batch scheduler enforces; manual mode self-enforces.
4. **Cover provenance**: cover generation method (AI image API + model, or typographic) logged in compliance_log either way (ADR-005).
5. **No KU/KDP Select** enrollment (ADR-004) — exclusivity conflicts with multi-platform.
6. **Rights hygiene**: no living-author name-dropping as endorsement, no trademark in title/keywords without basis, no public-domain repackaging without added value.

## Platform notes

- **KDP**: disclosure questions at publish time; answers emitted by `publish-checklist`.
- **Direct (Gumroad/Lemon Squeezy)**: no AI disclosure regime; we still keep the log — honesty is cheaper than memory.
- **Wide (Draft2Digital, M5+)**: inherits KDP answers; verify per-channel AI policies at M5.
