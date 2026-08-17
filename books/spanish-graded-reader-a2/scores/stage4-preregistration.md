# Stage 4 scoring preregistration — Spanish A2 Graded Reader, Volume 1

- **Created:** 2026-08-14
- **Purpose:** Lock the valid Stage-4 panel protocol before Pass 2 dispatch. The floor is already fixed in `.agents/rules/quality-gates.md`; this file records fixed pass scopes and decision handling.
- **Gate-B precondition:** PASS — `audits/structural.md` contains zero open critical findings.

## Locked scoring contract

- **Dimensions:** Originality, Prose, Coherence, Market, Voice, Opening — exactly the universal dimensions in `.agents/rules/scoring-contract.md`.
- **Scale:** integer 1–10.
- **Floor:** 7/10 on every dimension; the book score is the minimum, never an average.
- **Evidence law:** each score below 9 must have at least two manuscript citations. Every score below 7 also needs a `weakest_passage`, exact directive, and responsible loopback stage.
- **Excluded from Stage 4:** English parallel text and Stage-6 frontmatter, because `PIPE-001` has no assigned production owner. No judge may penalize their absence.

## Panel members and fixed scopes

### Pass 1 — Qwen 3.8 Max, Qwen family

- **Status:** completed manually by the human owner; report preserved at `scores/qwen-pass1-report.md`.
- **Prompt provenance:** `/tmp/spanish-a2-stage4-qwen/qwen-pass1.md` was generated before manual dispatch. It locked the threshold and excerpt set.
- **Fixed excerpts:** Stories 01, 02, 04, 06, 07, 08, 09, and 10 plus matching contracts.

### Pass 2 — Claude / Anthropic via Jcode, `claude-opus-4-6`

- **Status:** pending dispatch.
- **Independence:** Must not read `scores/`, any Qwen report, prior scorecards, or superseded audits.
- **Fixed excerpts:** Stories 01, 03, 05, 06, 09, and 10 plus matching contracts. Story 01 is repeated only because Opening requires it; Stories 03 and 05 are the distinct random/calibration seed.
- **Required inputs:** persona/niche, active contracts, constitution, active Gate-B audit for precondition only, rules, and relevant bible records.

## Reconciliation

1. Compare each dimension’s Pass-1 and Pass-2 integer scores.
2. If any dimension differs by more than one point, dispatch a third independent tiebreak using a fixed, new excerpt seed; use the median score for that dimension.
3. If all dimensions are at least 7, create the final scorecard with `verdict: PASS` and activate Stage 5.
4. If any final dimension is below 7, create the final scorecard with the exact cited loopback; increment only the affected dimension’s loopback counter.
5. No scorecard is valid until this reconciliation is complete.
