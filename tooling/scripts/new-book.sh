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
STAGE_DIRS=(research outline bible chapters summaries audits scores edits exports assets)
mkdir -p "${STAGE_DIRS[@]/#/$BOOK_DIR/}"
# git stores no empty dirs — .gitkeep preserves the stage structure across clones (ADR-010 portability).
for d in "${STAGE_DIRS[@]}"; do touch "$BOOK_DIR/$d/.gitkeep"; done

# TITLE is arbitrary user text and needs two layers of escaping. YAML first: the
# template wraps the title in double quotes, so `"` and `\` must be escaped for a
# double-quoted scalar. Then sed: `&` means "the whole match", `|` closes the
# expression. Miss either and the line corrupts silently (the script still exits 0).
# SLUG is kebab-case-validated above and can contain none of these.
TITLE_YAML="$(printf '%s' "$TITLE" | sed -e 's|\\|\\\\|g' -e 's|"|\\"|g')"
TITLE_ESC="$(printf '%s' "$TITLE_YAML" | sed -e 's|[\\&|]|\\&|g')"
sed -i.bak \
  -e "s|^slug:.*|slug: $SLUG|" \
  -e "s|^title:.*|title: \"$TITLE_ESC\"  # [FACTORY] provisional — a stage-0 PIVOT may rename the book|" \
  "$BOOK_DIR/manifest.yaml" && rm -f "$BOOK_DIR/manifest.yaml.bak"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
sed -i.bak -e "s|<slug>|$SLUG|g" -e "s|<iso8601>|$NOW|g" \
  "$BOOK_DIR/state.json" "$BOOK_DIR/compliance_log.yaml" && rm -f "$BOOK_DIR"/*.bak

TODAY="$(date +%F)"
# TITLE_YAML, not raw TITLE: the registry is the catalog ledger and a title containing
# a double quote corrupts it exactly as it corrupted the manifest.
cat >> "$REPO/books/registry.yaml" <<EOF
  - slug: $SLUG
    title: "$TITLE_YAML"
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
