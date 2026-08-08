#!/usr/bin/env bash
# tooling/scripts/niche_score.sh — competition scoring for candidate keywords (ADR-009/010).
# Usage: ./tooling/scripts/niche_score.sh "<keyword>" ["<keyword>" ...]
# Stage-0 Step 2: searches Amazon per keyword and scores the top results' BSR/reviews/revenue
# into a 0–100 opportunity score. MEDIUM-RISK TIER — search probes are rate-limited to 2.0s
# by KDP Scout config; keep the keyword list short and never loop this in a script.
#
# niche-score takes NO -m flag: marketplace comes from the MARKETPLACE env var (default us).
set -euo pipefail

[[ $# -gt 0 ]] || { echo "usage: niche_score.sh \"<keyword>\" [\"<keyword>\" ...]"; exit 1; }
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT_DIR="$RESEARCH_DIR/kdp-scout"
SCOUT="$SCOUT_DIR/.venv/bin/kdp-scout"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

cd "$SCOUT_DIR"
MARKETPLACE="${MARKETPLACE:-us}" "$SCOUT" niche-score "$@" --department books
echo "NOTE: a score is a prior, not a verdict — the top-10 comps still get human-verified (ADR-009)."
