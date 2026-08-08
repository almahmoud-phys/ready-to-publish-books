#!/usr/bin/env bash
# tooling/scripts/niche_mine.sh — autocomplete mining via KDP Scout (ADR-009/010).
# Usage: ./tooling/scripts/niche_mine.sh "<seed>" [-m com]
# Conservative rate limits by default. Appends to the cross-book ledger in .kdp-research/.
set -euo pipefail

SEED="${1:?usage: niche_mine.sh \"<seed>\" [-m com]}"
MARKET="${3:-com}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT="$RESEARCH_DIR/kdp-scout/.venv/bin/kdp-scout"
LEDGER="$RESEARCH_DIR/ledger/niche-ledger.csv"
TODAY="$(date +%F)"

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

OUT="$RESEARCH_DIR/exports/mine-$(echo "$SEED" | tr ' ' '-')-$MARKET-$TODAY.json"
echo "Mining '$SEED' (-m $MARKET) → $OUT"
(cd "$RESEARCH_DIR/kdp-scout" && "$SCOUT" mine "$SEED" -m "$MARKET" --department books --format json > "$OUT")

python3 - "$OUT" "$SEED" "$MARKET" "$TODAY" "$LEDGER" <<'PY'
import csv, json, sys
out, seed, market, today, ledger = sys.argv[1:6]
try:
    data = json.load(open(out))
    suggestions = data if isinstance(data, list) else data.get("suggestions", data.get("keywords", []))
except Exception:
    suggestions = []
with open(ledger, "a", newline="") as f:
    w = csv.writer(f)
    for s in suggestions:
        kw = s if isinstance(s, str) else s.get("keyword", str(s))
        w.writerow([kw, market, "", "", "", "", "", "", "", "", f"mined from seed: {seed}", today])
print(f"ledger += {len(suggestions)} rows")
PY
