---
name: publish-checklist
description: "Stage 7 — final go/no-go. Verifies every gate artifact, generates exact KDP disclosure answers from compliance_log.yaml (never from memory), emits the publish runbook, and after publish triggers the retrospective memory loop (LP6)."
model_tier: mid
stage: 7
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/state.json, books/<slug>/compliance_log.yaml, .agent/rules/kdp-compliance.md, .agent/rules/quality-gates.md]
  read: [books/<slug>/scores/scorecard.json, books/<slug>/exports/, books/<slug>/edits/fact-report.md]
  never_read: [chapters/ (judgment is done — verify artifacts, not content)]
outputs: [books/<slug>/exports/publish-runbook.md, state.json final update, .agent/memories/<slug>-retrospective.md (post-publish)]
---

# Publish Checklist

## Purpose
The last balancing loop (LP8) before the irreversible action. This skill verifies **artifacts, not content** — content judgment happened at Gates B–D. If this skill is re-reading chapters, something upstream failed.

## Go/No-Go verification (all required)
1. Gate A–E verdicts all PASS in state.json.
2. scorecard.json: book_score ≥ floor, no open loopbacks.
3. compliance_log.yaml: complete — every artifact in exports/ has a generation event with hash. Spot-verify 3 hashes.
4. Export validity: epubcheck exit 0 on kdp EPUB; print PDF page count matches spine width used by cover-director.
5. metadata.json complete; title/description human-approved.

## Disclosure answers (generated FROM the log)
- Text: `assisted` → "No AI-generated text" (AI tools used for research/editing only) | `generated` → "Yes, AI-generated text" with tool description.
- Images: from cover provenance entry.
- Translations: from log (default none).
Emit exact answers in the runbook — the human copies them at publish time.

## Publish runbook (`exports/publish-runbook.md`)
Step-by-step for each platform in manifest.platforms: KDP (ebook + print), direct sales (Gumroad/Lemon Squeezy listing fields), respecting the 3-titles/day cap.

## HITL GATE 2
Present go/no-go + runbook. **HALT.** The human publishes. No skill in this repo ever performs the publish action itself (fable authorization gate).

## Post-publish: retrospective (LP6 memory loop)
After the human confirms publication + 2 weeks of signals (or after M1 manually): write `.agent/memories/<slug>-retrospective.md` — what scored well/poorly, loopback hotspots, cost per stage, lessons for skills/rules. Book N+1 inherits.

## Anti-patterns
- ❌ Answering disclosure from memory instead of the log — the log exists precisely for this.
- ❌ Skipping the retrospective — that's how the system drifts instead of learns.
