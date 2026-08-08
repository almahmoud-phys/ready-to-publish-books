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
shift
MARKET="us"
if [[ "${1:-}" == "-m" ]]; then
  [[ "${2:-}" ]] || { echo "usage: niche_snapshot.sh <ASIN> [-m us] [\"<display name>\"]"; exit 1; }
  MARKET="$2"
  shift 2
fi
NAME="${1:-}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT_DIR="$RESEARCH_DIR/kdp-scout"
SCOUT="$SCOUT_DIR/.venv/bin/kdp-scout"
TMP_OUTPUT="$(mktemp)"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

echo "Snapshot $ASIN (-m $MARKET)"
cd "$SCOUT_DIR"

# Exit 3 is the circuit-breaker for refusal: one CAPTCHA/refusal ends all Amazon probing
# for this session. No retry/backoff — reduced uncertainty comes from stopping, not guessing.
set +e
if [[ -n "$NAME" ]]; then
  "$SCOUT" track add "$ASIN" -m "$MARKET" --name "$NAME" 2>&1 | tee "$TMP_OUTPUT"
else
  "$SCOUT" track add "$ASIN" -m "$MARKET" 2>&1 | tee "$TMP_OUTPUT"
fi
SCOUT_RC=${PIPESTATUS[0]}
set -e

if grep -Fq "CAPTCHA detected" "$TMP_OUTPUT" || \
   grep -Fq "search failed or CAPTCHA" "$TMP_OUTPUT" || \
   grep -Fq "No niches could be analyzed" "$TMP_OUTPUT"; then
  echo "Refusal detected in track add output — circuit-breaker triggered (exit 3)."
  echo "If KDP Scout suggests configuring a proxy, ignore it: ADR-008 bans proxies permanently."
  rm -f "$TMP_OUTPUT"
  exit 3
fi

if [[ $SCOUT_RC -ne 0 ]]; then
  rm -f "$TMP_OUTPUT"
  exit "$SCOUT_RC"
fi

set +e
"$SCOUT" track list 2>&1 | tee "$TMP_OUTPUT"
SCOUT_RC=${PIPESTATUS[0]}
set -e

if grep -Fq "CAPTCHA detected" "$TMP_OUTPUT" || \
   grep -Fq "search failed or CAPTCHA" "$TMP_OUTPUT" || \
   grep -Fq "No niches could be analyzed" "$TMP_OUTPUT"; then
  echo "Refusal detected in track list output — circuit-breaker triggered (exit 3)."
  echo "If KDP Scout suggests configuring a proxy, ignore it: ADR-008 bans proxies permanently."
  rm -f "$TMP_OUTPUT"
  exit 3
fi
rm -f "$TMP_OUTPUT"
[[ $SCOUT_RC -eq 0 ]] || exit "$SCOUT_RC"
echo "NOTE: verify this comp manually on the live page before it feeds a verdict (ADR-009)."
