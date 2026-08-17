---
name: publish-checklist
description: "Stage 7 — final go/no-go. Verifies every gate artifact, generates exact KDP disclosure answers from compliance_log.yaml (never from memory), emits the publish runbook, and after publish triggers the retrospective memory loop (LP6)."
model_tier: mid
stage: 7
context_budget:
  always_read: [books/<slug>/manifest.yaml, books/<slug>/constitution.md, books/<slug>/state.json, books/<slug>/compliance_log.yaml, .agents/rules/kdp-compliance.md, .agents/rules/quality-gates.md, .agents/rules/task-ledger.md]
  read: [books/<slug>/tasks.md (Stage 7, blocked work, and human decisions only), books/<slug>/scores/scorecard.json, books/<slug>/exports/, books/<slug>/edits/fact-report.md]
  never_read: [chapters/ (judgment is done — verify artifacts, not content)]
outputs: [books/<slug>/exports/publish-runbook.md, state.json final update, .agents/memories/<slug>-retrospective.md (post-publish), books/<slug>/tasks.md publication evidence]
---

# Publish Checklist

## Purpose
The last balancing loop (LP8) before the irreversible action. This skill verifies **artifacts, not content** — content judgment happened at Gates B–D. If this skill is re-reading chapters, something upstream failed.

## Go/No-Go verification (all required)
1. Gate A–E verdicts all PASS in state.json.
2. scorecard.json: book_score ≥ floor, no open loopbacks.
3. `compliance_log.yaml` is complete for every release artifact and its source/provenance. Recompute every hash listed in `exports/release/release-manifest.json`; sampling is insufficient at the irreversible boundary.
4. Release validity: the manifest is PASS; EPUB passes epubcheck; interior page dimensions/count match the locked settings; the cover is exactly one PDF page at the matching wrap dimensions.
5. Exact metadata equality: title, subtitle, author/pen name, language, edition, ISBN strategy, description, cover, title page, metadata export, and captured KDP form contain the approved values.
6. KDP Previewer has been inspected across the cover and complete interior. A first edition or materially changed build has a passing physical-proof record, or an explicit owner waiver names the accepted risk. A proof request alone is not approval.
7. Originality, rights, cover provenance, disclosure mapping, and platform-form snapshots are complete. A reader-facing AI disclosure is not required by this workflow; the private KDP answers must remain truthful.

## Disclosure answers (generated FROM the log)
- Text: `assisted` → "No AI-generated text" (AI tools used for research/editing only) | `generated` → "Yes, AI-generated text" with tool description.
- Images: from cover provenance entry.
- Translations: derive from the log and production record; never default to "None" when evidence is absent.
Emit exact answers in the runbook — the human copies them at publish time.

## Publish runbook (`exports/publish-runbook.md`)
Step-by-step for each platform in manifest.platforms: exact canonical filenames and hashes, locked print settings, exact metadata/form values, private disclosure answers, Previewer evidence, proof/waiver status, pricing, rollback, and post-upload reconciliation. KDP (ebook + print) and direct sales must respect the 3-titles/day cap.

## HITL GATE 2
Present go/no-go + runbook. **HALT.** The human publishes. No skill in this repo ever performs the publish action itself (fable authorization gate).

## Post-publish: retrospective (LP6 memory loop)
After the human confirms publication + 2 weeks of signals (or after M1 manually): reconcile the live listing against the runbook, archive identifiers/screenshots/upload hashes, then write `.agents/memories/<slug>-retrospective.md` — what scored well/poorly, loopback hotspots, cost per stage, lessons for skills/rules. Book N+1 inherits.

## Anti-patterns
- ❌ Answering disclosure from memory instead of the log — the log exists precisely for this.
- ❌ Skipping the retrospective — that's how the system drifts instead of learns.
- ❌ Uploading whichever file looks newest or contains `final` in its name — only the passing release manifest names upload candidates.
- ❌ Treating Previewer approval, proof request, and physical-proof approval as interchangeable states.
