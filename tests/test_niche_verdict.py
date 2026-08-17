#!/usr/bin/env python3
"""Self-check for the stage-0 verdict script. Run: python3 tests/test_niche_verdict.py

No framework by design — plain asserts, stdlib only. This exists because niche_verdict.py is
the one place in the pipeline that can say GO, and a checklist renderer that always says yes
would look exactly like a working gate until a bad book shipped.

The autocomplete cross-check reads the REAL ledger (.kdp-research/ledger/niche-ledger.csv),
which this test cannot write. That is deliberate: a test able to forge the artifact it is
verified against proves nothing. When the workspace has not been initialised the ledger is
absent and those cases are skipped, not silently passed.
"""

import csv
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tooling" / "scripts" / "niche_verdict.py"
LEDGER = REPO / ".kdp-research" / "ledger" / "niche-ledger.csv"

FILLED_CHARTER = """# charter
reader_problem: teams cannot predict what an LLM feature costs in production
useful_outcome: ship a routing policy with a defensible cost per successful task
authority_envelope: ran inference infrastructure; has real traffic and billing data
authority_exclusions: cannot write about model training or fine-tuning economics
allowed_adjacency: retitle, sub-niche
max_pivot_cycles: 3
"""

TEMPLATE_CHARTER = FILLED_CHARTER.replace(
    "teams cannot predict what an LLM feature costs in production", "<the problem in the reader's words>"
)


def ledger_counts():
    """Seed -> harvested row count, straight from the real ledger."""
    if not LEDGER.exists():
        return None
    counts = {}
    with LEDGER.open(newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if len(row) < 11:
                continue
            marker = row[10].strip()
            if marker.startswith("mined from seed:"):
                seed = marker.split(":", 1)[1].strip()
                counts[seed] = counts.get(seed, 0) + 1
    return counts


def run(books_dir, slug):
    env = {**os.environ, "RTPB_BOOKS_DIR": str(books_dir)}
    p = subprocess.run([sys.executable, str(SCRIPT), slug], capture_output=True, text=True, env=env)
    return p.stdout.strip()


def make_book(root, slug, charter, evidence, trademark=None):
    d = root / slug / "research"
    d.mkdir(parents=True, exist_ok=True)
    (d / "charter.md").write_text(charter)
    (d / "evidence.yaml").write_text(evidence)
    if trademark is not None:
        (d / "trademark.md").write_text(trademark)
    return d


ALL_UNKNOWN = "\n".join(
    f"{k}: UNKNOWN"
    for k in [
        "collector_health", "trend_direction", "autocomplete_richness", "comps_under_50k_bsr",
        "comp_table", "result_count_or_subniche", "category_difficulty", "gap_statement",
        "differentiation_contract", "authority_fit", "asset_feasibility", "trademark_status",
    ]
) + "\n"


def full_evidence(seed, count, trademark_status="no_conflict_found"):
    return f"""collector_health: CONFIRMED
trend_direction: rising
autocomplete_richness:
  {seed}: {count}
comps_under_50k_bsr: 2
comp_table:
  - {{title: A, asin: B001, bsr: 12000, price: 24.99, review_count: 41, latest_review_date: 2026-07-01}}
  - {{title: B, asin: B002, bsr: 30000, price: 19.99, review_count: 35, latest_review_date: 2026-06-11}}
result_count_or_subniche: 4200
category_difficulty: "#20 at 48k and 61k"
gap_statement: no comp organises around cost per successful task
differentiation_contract: three promises drawn from negative reviews
authority_fit: y
asset_feasibility: screenshots reproducible from own dashboards
trademark_status: {trademark_status}
"""


def main():
    counts = ledger_counts()
    failures = []

    def check(name, got, want_prefix, want_substr=None):
        ok = got.startswith(want_prefix) and (want_substr is None or want_substr in got)
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n      -> {got[:150]}")
        if not ok:
            failures.append(name)

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # 1. A fresh book refuses everything: unset goal AND no evidence.
        make_book(root, "fresh", TEMPLATE_CHARTER, ALL_UNKNOWN)
        check("fresh book is INCOMPLETE", run(root, "fresh"), "INCOMPLETE", "charter placeholder")

        if counts:
            seed, n = next(iter(counts.items()))

            # 2. Everything measured and consistent, goal set, trademark evidenced -> GO.
            make_book(root, "go", FILLED_CHARTER, full_evidence(seed, n),
                      trademark="screen 2026-08-08\nverdict: no_conflict_found\nhuman_signoff: owner 2026-08-08\n")
            check("complete + consistent is GO", run(root, "go"), "GO")

            # 3. The gate's whole purpose: a claim the artifact does not support must not pass.
            make_book(root, "liar", FILLED_CHARTER, full_evidence(seed, n + 999),
                      trademark="verdict: no_conflict_found\n")
            check("inflated autocomplete claim is refused", run(root, "liar"), "INCOMPLETE", "ledger has")

            # 4. trademark_status asserted with no trademark.md behind it.
            make_book(root, "notm", FILLED_CHARTER, full_evidence(seed, n))
            check("trademark claim without evidence is refused", run(root, "notm"),
                  "INCOMPLETE", "trademark_status cross-check failed")

            # 5. `clear` is not a value an agent may write.
            make_book(root, "clear", FILLED_CHARTER, full_evidence(seed, n, trademark_status="clear"),
                      trademark="verdict: clear\n")
            check("trademark 'clear' is rejected", run(root, "clear"), "INCOMPLETE", "invalid value")

            # 5b. An agent-written search result is not legal clearance: without the human
            #     sign-off line, GO must not be reachable however complete the rest is.
            make_book(root, "nosign", FILLED_CHARTER, full_evidence(seed, n),
                      trademark="verdict: no_conflict_found\n")
            got = run(root, "nosign")
            ok = not got.startswith("GO")
            print(f"{'PASS' if ok else 'FAIL'}  unsigned trademark cannot reach GO\n      -> {got[:110]}")
            if not ok:
                failures.append("unsigned trademark cannot reach GO")

            # 6. Partial evidence still yields PIVOT — this is what run 1 actually produced,
            #    and a gate that could only say INCOMPLETE until every field was filled would
            #    make the cheap redirect impossible.
            partial = f"""collector_health: CONFIRMED
trend_direction: rising
autocomplete_richness:
  {seed}: {n}
comps_under_50k_bsr: UNKNOWN
comp_table: UNKNOWN
result_count_or_subniche: UNKNOWN
category_difficulty: UNKNOWN
gap_statement: UNKNOWN
differentiation_contract: UNKNOWN
authority_fit: UNKNOWN
asset_feasibility: UNKNOWN
trademark_status: UNKNOWN
"""
            make_book(root, "partial", FILLED_CHARTER, partial)
            check("partial evidence still yields PIVOT", run(root, "partial"), "PIVOT")
        else:
            print("SKIP  ledger-backed cases: no .kdp-research ledger (run research-init.sh)")

        # A book-local ledger is the reproducible evidence artifact and must outrank the
        # ignored workstation cache. This is the only precedence that survives a clean clone.
        local_seed = "book-local-test-seed"
        local_dir = make_book(
            root,
            "local-ledger",
            FILLED_CHARTER,
            full_evidence(local_seed, 2),
            trademark="verdict: no_conflict_found\nhuman_signoff: owner 2026-08-09\n",
        )
        with (local_dir / "niche-ledger.csv").open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "keyword", "marketplace", "format", "recurring_problem",
                "audience_specificity", "seasonality", "competitor_concentration",
                "median_review_count", "observed_bsr_range", "trademark_status",
                "differentiation_hypothesis", "last_checked",
            ])
            for suffix in ("one", "two"):
                writer.writerow([
                    f"{local_seed} {suffix}", "us", "", "", "", "", "", "", "", "",
                    f"mined from seed: {local_seed}", "2026-08-09",
                ])
        check(
            "book-local ledger outranks machine cache",
            run(root, "local-ledger"),
            "GO",
            "autocomplete_ledger=book-local",
        )

    print()
    if failures:
        print(f"{len(failures)} FAILED: {', '.join(failures)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
