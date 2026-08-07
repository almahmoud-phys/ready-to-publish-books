# M0 Harvest Checklist (ADR-006)

> Clone the five references into `~/reference/` (NEVER inside this repo), extract per below, then delete the clones. License rule: check each repo's LICENSE before copying any file verbatim; where unclear, reimplement the pattern — patterns aren't copyrightable, files are.

## 1. book-generator — github.com/wesleyscholl/book-generator
- [ ] Check LICENSE
- [ ] Extract → `tooling/pandoc/`: EPUB template, epub.css, metadata.yaml
- [ ] Extract → `tooling/latex/`: print interior template (6×9), margins/page-count table
- [ ] Extract → `tooling/scripts/`: epubcheck wrapper, cover assembly (ImageMagick)
- [ ] Reimplement → `pipeline/router.py`: multi-provider fallback logic (pattern, not code)
- [ ] Note their KDP checklist lessons → merge into publish-checklist skill if gaps found

## 2. Book Genesis v4 — github.com/felipelobomotta/book-genesis (v4 branch)
- [ ] Check LICENSE
- [ ] Extract → `.agent/rules/scoring-contract.md`: verify our adaptation matches their floor/citation discipline; merge any missing judge rules
- [ ] Extract → `books/_template/manifest.yaml`: compare manifest schema; adopt useful fields
- [ ] Read their prompts for adversarial-audit ordering → validate our stage 3/4 split

## 3. kindle-book-agency — github.com/Harshil-Jani/kindle-book-agency
- [ ] Check LICENSE
- [ ] Reimplement → `CLAUDE.md`: their router/index structure (already drafted — refine)
- [ ] Reimplement → `pipeline/orchestrator.py` (M2): dependency-aware parallel-phase logic (pattern only)

## 4. libriscribe — github.com/guerra2fernando/libriscribe
- [ ] Check LICENSE
- [ ] Compare per-project workspace layout vs our `books/<slug>/` — adopt filename conventions that are better (e.g., characters.json analog = bible/canon.md)

## 5. Claude-Code book skills — github.com/PhilipSt/book-gen (MIT per author) + the 15-skill repo
- [ ] Verify MIT LICENSE file exists
- [ ] Read chapter-writing + context-passing skills → harvest prompt techniques into `chapter-writer` and `continuity-keeper`
- [ ] Note anything they do for KDP export worth adding to `formatter-platform`

## Done criteria
- [ ] All five LICENSEs recorded here (name + type)
- [ ] Extractions merged; references deleted from disk
- [ ] Any skill/rules changes committed with message "harvest: <source> → <what>"
