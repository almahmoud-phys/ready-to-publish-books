#!/usr/bin/env bash
# tooling/scripts/niche_score.sh — competition scoring for candidate keywords (ADR-009/010).
# Usage: ./tooling/scripts/niche_score.sh "<keyword>" ["<keyword>" ...]
# Stage-0 Step 2: searches Amazon per keyword and scores the top results' reviews plus a
# position/review-based BSR heuristic into a 0–100 opportunity score. The displayed BSR is
# NOT a live product-page BSR and cannot satisfy the Stage-0 comp-table gate. MEDIUM-RISK
# TIER — search probes are rate-limited to 2.0s
# by KDP Scout config; keep the keyword list short and never loop this in a script.
#
# niche-score takes NO -m flag: marketplace comes from the MARKETPLACE env var (default us).
set -euo pipefail

[[ $# -gt 0 ]] || { echo "usage: niche_score.sh \"<keyword>\" [\"<keyword>\" ...]"; exit 1; }
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT_DIR="$RESEARCH_DIR/kdp-scout"
SCOUT="$SCOUT_DIR/.venv/bin/kdp-scout"
TMP_OUTPUT="$(mktemp)"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

cd "$SCOUT_DIR"
# Exit 3 is the circuit-breaker for refusal: one CAPTCHA/refusal ends all Amazon probing
# for this session. No retry/backoff — repeated probing only increases block risk.
set +e
MARKETPLACE="${MARKETPLACE:-us}" "$SCOUT" niche-score "$@" --department books 2>&1 | tee "$TMP_OUTPUT"
SCOUT_RC=${PIPESTATUS[0]}
set -e

if grep -Eqi \
   'CAPTCHA detected|search failed or CAPTCHA|No niches could be analyzed|Network error querying|NameResolutionError|Failed to resolve|Max retries exceeded|HTTP[^[:alnum:]]*(403|429)' \
   "$TMP_OUTPUT"; then
  echo "Refusal detected in niche-score output — circuit-breaker triggered (exit 3)."
  echo "If KDP Scout suggests configuring a proxy, ignore it: ADR-008 bans proxies permanently."
  rm -f "$TMP_OUTPUT"
  exit 3
fi

rm -f "$TMP_OUTPUT"
[[ $SCOUT_RC -eq 0 ]] || exit "$SCOUT_RC"
echo "WARNING: KDP Scout's displayed BSR is a search-position/review heuristic, not a live BSR."
echo "NOTE: use this only for shelf discovery; top-10 live comps still require human verification (ADR-009)."
