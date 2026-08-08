#!/usr/bin/env bash
# tooling/scripts/new-book.sh — the book factory.
# Usage: ./tooling/scripts/new-book.sh <slug> "<title>"
# Births a compliant per-book subproject from books/_template/ and registers it.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
SLUG="${1:?usage: new-book.sh <slug> \"<title>\"}"
TITLE="${2:?usage: new-book.sh <slug> \"<title>\"}"

[[ "$SLUG" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "ERROR: slug must be kebab-case (got: $SLUG)"; exit 1; }
BOOK_DIR="$REPO/books/$SLUG"
[[ ! -e "$BOOK_DIR" ]] || { echo "ERROR: books/$SLUG already exists"; exit 1; }
grep -q "slug: $SLUG" "$REPO/books/registry.yaml" 2>/dev/null && { echo "ERROR: $SLUG already in registry"; exit 1; }

cp -r "$REPO/books/_template" "$BOOK_DIR"
mkdir -p "$BOOK_DIR"/{research,outline,bible,chapters,summaries,audits,scores,edits,exports,assets}

sed -i.bak \
  -e "s|^slug:.*|slug: $SLUG|" \
  -e "s|^title:.*|title: \"$TITLE\"|" \
  "$BOOK_DIR/manifest.yaml" && rm -f "$BOOK_DIR/manifest.yaml.bak"
sed -i.bak "s|<slug>|$SLUG|g" "$BOOK_DIR/state.json" "$BOOK_DIR/compliance_log.yaml" && rm -f "$BOOK_DIR"/*.bak

TODAY="$(date +%F)"
cat >> "$REPO/books/registry.yaml" <<EOF
  - slug: $SLUG
    title: "$TITLE"
    track: assisted
    stage: 0
    verdict: null
    created: $TODAY
    published: null
    book_score: null
    cost_usd: null
EOF

echo "✅ books/$SLUG created and registered."
echo ""
echo "Stage 0 — niche-research checklist:"
echo "  1. Edit books/$SLUG/manifest.yaml (niche_seed, persona, track)"
echo "  2. ./tooling/scripts/niche_mine.sh \"<seed>\" -m com"
echo "  3. Human-verify top-10 comps on the live marketplace (ADR-009)"
echo "  4. Run the niche-research skill → research/niche.md → GO/PIVOT/KILL"
