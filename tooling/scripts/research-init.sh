#!/usr/bin/env bash
# tooling/scripts/research-init.sh — bootstrap the research workspace (ADR-010).
# Creates {repo}/.kdp-research/ with KDP Scout (isolated venv) + trendspyg + ledger dirs.
# Idempotent: safe to re-run (updates the tool instead of recloning).
# Works on any machine with git + python3 — this is what makes the repo portable.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RD="$REPO/.kdp-research"
VENV="$RD/kdp-scout/.venv"

mkdir -p "$RD/ledger" "$RD/exports"

# clone or update KDP Scout (MIT — github.com/rxpelle/kdp-scout)
if [[ ! -d "$RD/kdp-scout/.git" ]]; then
  echo "Cloning KDP Scout..."
  git clone https://github.com/rxpelle/kdp-scout.git "$RD/kdp-scout"
else
  echo "Updating KDP Scout..."
  git -C "$RD/kdp-scout" pull --ff-only || echo "(update skipped — local changes)"
fi

# isolated venv + install (inspect the tool's SECURITY.md once before first run — ADR-009)
[[ -d "$VENV" ]] || python3 -m venv "$VENV"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -e "$RD/kdp-scout" trendspyg

# init config if absent (idempotent)
(cd "$RD/kdp-scout" && "$VENV/bin/kdp-scout" config init 2>/dev/null) || true

# ledger header if absent
LEDGER="$RD/ledger/niche-ledger.csv"
[[ -f "$LEDGER" ]] || echo "keyword,marketplace,format,recurring_problem,audience_specificity,seasonality,competitor_concentration,median_review_count,observed_bsr_range,trademark_status,differentiation_hypothesis,last_checked" > "$LEDGER"

# verify
"$VENV/bin/kdp-scout" --help >/dev/null 2>&1 || { echo "ERROR: kdp-scout did not install cleanly"; exit 1; }

echo ""
echo "✅ Research workspace ready at .kdp-research/"
echo "   Tool:    $RD/kdp-scout (venv: $VENV)"
echo "   Ledger:  $LEDGER"
echo "   Exports: $RD/exports/"
echo ""
echo "Next: ./tooling/scripts/new-book.sh <slug> \"<title>\" to birth a book, then niche_mine.sh \"<seed>\" to start stage 0."
