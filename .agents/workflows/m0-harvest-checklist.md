# M0 Harvest Checklist (ADR-006) — RECON COMPLETE 2026-08-08

> Remote recon done via GitHub connector. Deep-read phase happens LOCALLY (clone → read → extract) because the connector does not surface file content in this environment.

## License status (RECORDED)

| Repo | License | Rule applied |
|---|---|---|
| wesleyscholl/book-generator | ❌ NONE — all rights reserved | Patterns only. NO file copies. |
| Harshil-Jani/kindle-book-agency | ✅ Present (~1KB, MIT-class) — verify text locally | Read/adapt with attribution after verification |
| guerra2fernando/libriscribe | ❌ NONE — all rights reserved | Patterns only. NO file copies. |
| Book Genesis v4 (felipelobomotta?) | ⚠️ Not found remotely | Locate via original LinkedIn post link |
| PhilipSt/book-gen | ⚠️ Not found remotely | Locate via original Reddit post link |

## Asset inventory (from structure recon)

### book-generator (patterns → reimplemented clean-room, see tooling/)
- scripts/compile_book.sh (79KB) — the pandoc+latex compile pipeline → REIMPLEMENTED as tooling/scripts/compile_book.py (clean-room)
- scripts/generate_covers.sh — cover assembly via ImageMagick → pattern noted for cover-director (M4)
- scripts/get_keywords.sh + kdp_topic_finder.sh + kdp_market_analyzer.sh + topic_market_research.sh → patterns for niche-research/metadata-seo (M1+)
- scripts/multi_provider_ai.sh + multi_provider_ai_simple.sh → fallback-chain pattern for pipeline/router.py (M2)
- scripts/plagiarism_report_manager.sh → originality-check pattern for Gate E
- scripts/optimized_chapter_handler.sh → chapter parallelization pattern (M2)
- [ ] LOCAL: clone and read compile_book.sh + multi_provider_ai.sh to validate our reimplementation covers their edge cases (provider failover order, retry/backoff, KDP checklist items)

### kindle-book-agency (license OK pending verification)
- [ ] LOCAL: verify LICENSE text (MIT-class, 1069 bytes)
- [ ] LOCAL: read CLAUDE.md (8.6KB router) — refine our CLAUDE.md router structure
- [ ] LOCAL: read agents/ prompts — compare with our SKILL.md drafts
- [ ] LOCAL: read compile_kindle.py (31KB Python compiler) + write_chapters.py + diagram_renderer.py — patterns for formatter-platform + M2 orchestrator

### libriscribe (patterns only)
- [ ] LOCAL: read prompts/ directory — harvest chapter-prompt + context-passing techniques into chapter-writer/continuity-keeper
- [ ] LOCAL: compare src/ project-state layout vs books/<slug>/

### Book Genesis v4 + PhilipSt/book-gen
- [ ] LOCAL: locate repos via the original LinkedIn/Reddit post URLs; record licenses; harvest scoring-contract refinements + skill prompt techniques

## Done criteria
- [x] All reachable licenses recorded
- [x] Structure recon + asset inventory
- [x] Clean-room reimplementation of the compile/export pattern (tooling/)
- [ ] LOCAL deep-read pass (clone all five, checklist above)
- [ ] References deleted from disk after local pass
- [ ] Skill/rules changes committed with message "harvest: <source> → <what>"
