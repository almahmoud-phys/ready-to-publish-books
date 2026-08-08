#!/usr/bin/env bash
# tooling/scripts/niche_snapshot.sh — BSR/price/review snapshot for one ASIN via KDP Scout (ADR-009/010).
# Usage: ./tooling/scripts/niche_snapshot.sh <ASIN> [-m com]
# LOW VOLUME ONLY — product-page snapshots are the medium-risk tier; top-10 comps are always
# human-verified on the live page regardless of what this returns.
set -euo pipefail

ASIN="${1:?usage: niche_snapshot.sh <ASIN> [-m com]}"
MARKET="${3:-com}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT="$RESEARCH_DIR/kdp-scout/.venv/bin/kdp-scout"
TODAY="$(date +%F)"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

OUT="$RESEARCH_DIR/exports/snapshot-$ASIN-$MARKET-$TODAY.json"
echo "Snapshot $ASIN (-m $MARKET) → $OUT"
(cd "$RESEARCH_DIR/kdp-scout" && "$SCOUT" asin "$ASIN" -m "$MARKET" --format json > "$OUT")
echo "NOTE: verify this comp manually on the live page before it feeds a verdict (ADR-009)."
