#!/usr/bin/env bash
# tooling/scripts/niche_mine.sh — autocomplete mining via KDP Scout (ADR-009/010).
# Usage: ./tooling/scripts/niche_mine.sh "<seed>" [-m us]
# Conservative rate limits by default. Appends to the cross-book ledger in .kdp-research/.
#
# Marketplace is an enum KDP Scout validates: us|de|uk|fr|es|it|ca|au. Not "com".
# KDP Scout has no JSON output and no stdout harvest: `mine` writes rows into its own
# sqlite DB, keyed by seed in the `category` column. The harvest reads them back from
# there — an empty read is a failed measurement, not evidence of no demand (F9).
set -euo pipefail

SEED="${1:?usage: niche_mine.sh \"<seed>\" [-m us]}"
MARKET="${3:-us}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RESEARCH_DIR="${RTPB_RESEARCH_DIR:-$REPO/.kdp-research}"
SCOUT_DIR="$RESEARCH_DIR/kdp-scout"
SCOUT="$SCOUT_DIR/.venv/bin/kdp-scout"
DB="$SCOUT_DIR/data/kdp_scout.db"
LEDGER="$RESEARCH_DIR/ledger/niche-ledger.csv"
TODAY="$(date +%F)"
TMP_OUTPUT="$(mktemp)"

cleanup() {
  rm -f "$TMP_OUTPUT"
}
trap cleanup EXIT

[[ -x "$SCOUT" ]] || { echo "ERROR: KDP Scout not found — run ./tooling/scripts/research-init.sh first."; exit 1; }

echo "Mining '$SEED' (-m $MARKET) — ~40s at the default 1.5s autocomplete rate limit."
set +e
(cd "$SCOUT_DIR" && "$SCOUT" mine "$SEED" -m "$MARKET" --department books) 2>&1 | tee "$TMP_OUTPUT"
SCOUT_RC=${PIPESTATUS[0]}
set -e

# KDP Scout logs network/CAPTCHA failures but may still exit 0 and leave cached rows in its
# SQLite database. Never let those stale rows masquerade as a successful current harvest.
if grep -Eqi \
  'CAPTCHA detected|search failed or CAPTCHA|No niches could be analyzed|Network error querying|NameResolutionError|Failed to resolve|Max retries exceeded|HTTP[^[:alnum:]]*(403|429)' \
  "$TMP_OUTPUT"; then
  echo "Refusal or collector failure detected — circuit-breaker triggered (exit 3)."
  echo "No cached database rows were appended. All Amazon activity must stop for this session."
  echo "If KDP Scout suggests configuring a proxy, ignore it: ADR-008 bans proxies permanently."
  exit 3
fi

[[ $SCOUT_RC -eq 0 ]] || exit "$SCOUT_RC"

python3 - "$DB" "$SEED" "$MARKET" "$TODAY" "$LEDGER" <<'PY'
import csv, sqlite3, sys
db, seed, market, today, ledger = sys.argv[1:6]
try:
    con = sqlite3.connect(db)
    # Two predicates, because `category` records the seed that FIRST inserted a keyword.
    # Mining "llm" then "llm deployment" finds the same phrases, but the second run inserts
    # nothing new — category stays "llm" and a category-only harvest reads zero and calls it
    # a failed measurement. Matching the phrase prefix as well recovers the real harvest.
    rows = [r[0] for r in con.execute(
        "select distinct keyword from keywords where category = ? or keyword like ? order by keyword",
        (seed, seed + "%"))]
except Exception as exc:
    print(f"ERROR: failed to read {db}: {exc}")
    sys.exit(2)

# Zero suggestions is real signal about the SEED (the phrase has no buyer language),
# but it is also what a blocked scraper looks like. Stop and make the caller check —
# a stage-0 verdict must never rest on a harvest nobody looked at.
if not rows:
    print(f"ERROR: no suggestions harvested for '{seed}' ({market}).")
    print("       Either the phrase has no Amazon autocomplete presence — mine adjacent")
    print("       seeds — or the collector is blocked. Control test: a known-good seed")
    print("       such as \"historical fiction\" should return ~28 keywords.")
    sys.exit(2)

with open(ledger, "a", newline="") as f:
    w = csv.writer(f)
    for kw in rows:
        w.writerow([kw, market, "", "", "", "", "", "", "", "", f"mined from seed: {seed}", today])
print(f"ledger += {len(rows)} rows")
PY
