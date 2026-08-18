#!/usr/bin/env bash
# tooling/scripts/research-init.sh — bootstrap the research workspace (ADR-010).
# Creates {repo}/.kdp-research/ with KDP Scout (isolated venv) + trendspyg + ledger dirs.
# Idempotent: safe to re-run and pins the tested collector revision.
# Works on any machine with git + python3 — this is what makes the repo portable.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
RD="$REPO/.kdp-research"
VENV="$RD/kdp-scout/.venv"
KDP_SCOUT_REPO="${KDP_SCOUT_REPO:-https://github.com/almahmoud-phys/kdp-scout.git}"
# v0.3.1-rtpb.1 — Amazon.fr routing/parsing plus the bounded Playwright collector.
KDP_SCOUT_REF="${KDP_SCOUT_REF:-d69ff17030f32ff8bd39d19ed3d155b3dd05468e}"
KDP_SCOUT_UPSTREAM="https://github.com/rxpelle/kdp-scout.git"

mkdir -p "$RD/ledger" "$RD/exports"

# Clone the maintained fork, retain the original project as upstream, and
# detach at an immutable tested revision. Override REPO/REF explicitly when
# evaluating a newer fork release; never float silently on a branch head.
if [[ ! -d "$RD/kdp-scout/.git" ]]; then
  echo "Cloning KDP Scout..."
  git clone "$KDP_SCOUT_REPO" "$RD/kdp-scout"
else
  echo "Preparing pinned KDP Scout..."
  if [[ -n "$(git -C "$RD/kdp-scout" status --porcelain --untracked-files=no)" ]]; then
    echo "ERROR: KDP Scout has tracked local changes; refusing to replace them."
    exit 1
  fi
  if git -C "$RD/kdp-scout" remote get-url origin >/dev/null 2>&1; then
    git -C "$RD/kdp-scout" remote set-url origin "$KDP_SCOUT_REPO"
  else
    git -C "$RD/kdp-scout" remote add origin "$KDP_SCOUT_REPO"
  fi
fi

if ! git -C "$RD/kdp-scout" remote get-url upstream >/dev/null 2>&1; then
  git -C "$RD/kdp-scout" remote add upstream "$KDP_SCOUT_UPSTREAM"
fi
git -C "$RD/kdp-scout" fetch --quiet --tags origin
git -C "$RD/kdp-scout" cat-file -e "$KDP_SCOUT_REF^{commit}" || {
  echo "ERROR: pinned KDP Scout revision is unavailable: $KDP_SCOUT_REF"
  exit 1
}
git -C "$RD/kdp-scout" checkout --quiet --detach "$KDP_SCOUT_REF"

# isolated venv + install (inspect the tool's SECURITY.md once before first run — ADR-009)
[[ -d "$VENV" ]] || python3 -m venv "$VENV"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -e "$RD/kdp-scout[browser]" trendspyg

# init config if absent (idempotent)
(cd "$RD/kdp-scout" && "$VENV/bin/kdp-scout" config init 2>/dev/null) || true

# ledger header if absent
LEDGER="$RD/ledger/niche-ledger.csv"
[[ -f "$LEDGER" ]] || echo "keyword,marketplace,format,recurring_problem,audience_specificity,seasonality,competitor_concentration,median_review_count,observed_bsr_range,trademark_status,differentiation_hypothesis,last_checked" > "$LEDGER"

# harness view: .claude/skills must resolve to .agents/skills or Claude Code sees no skills
# (ADR-014). A checkout without symlink support — Windows, or `core.symlinks=false` — leaves a
# small TEXT FILE containing the link target instead. That failure is silent: the repo looks
# complete and the harness simply finds nothing. Detect it here rather than trying to prevent
# every environment in advance; this is the one script every new machine runs.
LINK="$REPO/.claude/skills"
if [[ -d "$LINK" && -f "$LINK/scorer/SKILL.md" ]]; then
  :  # resolves — symlink or real dir, either way the harness can read it
elif [[ -e "$LINK" && ! -d "$LINK" ]]; then
  echo "WARNING: .claude/skills is a plain file, not a link — this checkout has no symlink support."
  echo "         Claude Code will discover ZERO skills. Fix with:"
  echo "           git config core.symlinks true && git checkout -- .claude/skills"
  echo "         (or copy .agents/skills to .claude/skills and keep .agents/ authoritative)"
else
  mkdir -p "$REPO/.claude"
  ln -s ../.agents/skills "$LINK" && echo "Recreated .claude/skills -> ../.agents/skills"
fi

# verify
"$VENV/bin/kdp-scout" --help >/dev/null 2>&1 || { echo "ERROR: kdp-scout did not install cleanly"; exit 1; }

echo ""
echo "✅ Research workspace ready at .kdp-research/"
echo "   Tool:    $RD/kdp-scout (venv: $VENV)"
echo "   Version: $KDP_SCOUT_REF (v0.3.1-rtpb.1)"
echo "   Ledger:  $LEDGER"
echo "   Exports: $RD/exports/"
echo ""
echo "Next: ./tooling/scripts/new-book.sh <slug> \"<title>\" to birth a book, then niche_mine.sh \"<seed>\" to start stage 0."
