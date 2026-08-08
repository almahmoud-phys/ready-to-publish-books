#!/usr/bin/env bash
# tooling/scripts/niche_snapshot.sh — BSR/price/review snapshot for one ASIN via KDP Scout (ADR-009/010).
# Usage: ./tooling/scripts/niche_snapshot.sh <ASIN> [-m us] ["<display name>"]
# LOW VOLUME ONLY — product-page snapshots are the medium-risk tier; top-10 comps are always
# human-verified on the live page regardless of what this returns.
#
# KDP Scout has no `asin` command and no JSON export. A comp is TRACKED: `track add` scrapes
# the product page once and stores it in the scout DB; `track list` reads snapshots back.
# Re-running for a known ASIN is cheap — add is idempotent, snapshot re-scrapes on demand.
set -euo pipefail

ASIN="${1:?usage: niche_snapshot.sh <ASIN> [-m us] [\"<display name>\"]}"
MARKET="${3:-us}"
NAME="${4:-}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT_DIR="$RESEARCH_DIR/kdp-scout"
SCOUT="$SCOUT_DIR/.venv/bin/kdp-scout"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

echo "Snapshot $ASIN (-m $MARKET)"
cd "$SCOUT_DIR"
if [[ -n "$NAME" ]]; then
  "$SCOUT" track add "$ASIN" -m "$MARKET" --name "$NAME"
else
  "$SCOUT" track add "$ASIN" -m "$MARKET"
fi
"$SCOUT" track list
echo "NOTE: verify this comp manually on the live page before it feeds a verdict (ADR-009)."
