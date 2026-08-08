#!/usr/bin/env bash
# tooling/scripts/niche_report.sh — project the cross-book ledger into a book's research dir.
# Usage: ./tooling/scripts/niche_report.sh <book-slug> [keyword-filter]
set -euo pipefail

SLUG="${1:?usage: niche_report.sh <book-slug> [filter]}"
FILTER="${2:-}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
LEDGER="$RESEARCH_DIR/ledger/niche-ledger.csv"
OUT="$REPO/books/$SLUG/research/niche-ledger.csv"

[[ -f "$LEDGER" ]] || { echo "ERROR: no ledger — run research-init.sh + niche_mine.sh first."; exit 1; }
[[ -d "$REPO/books/$SLUG" ]] || { echo "ERROR: books/$SLUG not found — run new-book.sh first."; exit 1; }

if [[ -n "$FILTER" ]]; then
  head -1 "$LEDGER" > "$OUT"
  grep -i "$FILTER" "$LEDGER" >> "$OUT" || true
else
  cp "$LEDGER" "$OUT"
fi
echo "→ $OUT ($(($(wc -l < "$OUT") - 1)) rows)"
