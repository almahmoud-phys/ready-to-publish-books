#!/usr/bin/env python3
"""Compute stage-0 verdict from evidence.yaml + charter.md without trust.

The script only reads artifacts, never infers or writes results.
"""

from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


REPO = Path(__file__).resolve().parents[2]
# RTPB_BOOKS_DIR lets the self-check point at a scratch book without polluting books/.
# The real ledger stays repo-relative: a test must not be able to fake the artifact it
# is cross-checked against, or the cross-check proves nothing.
BOOKS_DIR = Path(os.environ.get("RTPB_BOOKS_DIR", REPO / "books"))
REQUIRE_KEYS = [
    "collector_health",
    "trend_direction",
    "autocomplete_richness",
    "comps_under_50k_bsr",
    "comp_table",
    "result_count_or_subniche",
    "category_difficulty",
    "gap_statement",
    "differentiation_contract",
    "authority_fit",
    "asset_feasibility",
    "trademark_status",
]
REQUIRE_CHARTER = [
    "reader_problem",
    "useful_outcome",
    "authority_envelope",
    "authority_exclusions",
    "allowed_adjacency",
    "max_pivot_cycles",
]
REFUSAL_MARKERS = (
    "CAPTCHA detected",
    "search failed or CAPTCHA",
    "No niches could be analyzed",
)


def _unknown(v: Any) -> bool:
    return isinstance(v, str) and v.strip() == "UNKNOWN"


def _parse_int(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    text = str(value).replace(",", "").strip()
    if not text:
        return None
    try:
        return int(float(text))
    except ValueError:
        return None


def _read_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a YAML mapping")
    return data


def _parse_charter(path: Path) -> Tuple[Dict[str, str], List[str]]:
    values: Dict[str, str] = {}
    missing: List[str] = []
    line_re = re.compile(r"^\s*([a-z_]+)\s*:\s*(.+?)\s*(?:#.*)?$")

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            m = line_re.match(line)
            if not m:
                continue
            key, raw_value = m.groups()
            if key in REQUIRE_CHARTER:
                values[key] = raw_value.strip()

    for key in REQUIRE_CHARTER:
        if key not in values:
            missing.append(f"charter field missing: {key}")
            continue
        if key != "max_pivot_cycles" and re.search(r"<[^>]+>", values[key]):
            missing.append(f"charter placeholder not replaced: {key}")
    return values, missing


def _ledger_path(book_dir: Path) -> Tuple[Path | None, str | None]:
    global_ledger = REPO / ".kdp-research" / "ledger" / "niche-ledger.csv"
    if global_ledger.exists():
        return global_ledger, "global"

    book_ledger = book_dir / "research" / "niche-ledger.csv"
    if book_ledger.exists():
        return book_ledger, "book-local"

    return None, None


def _audit_autocomplete(evidence: Dict[str, Any], book_dir: Path) -> Tuple[Dict[str, int], List[str], str | None]:
    if _unknown(evidence.get("autocomplete_richness", "UNKNOWN")):
        return {}, [], None

    claim = evidence.get("autocomplete_richness")
    if not isinstance(claim, dict):
        return {}, [f"autocomplete_richness must be a map, got {type(claim).__name__}"], None

    ledger, source = _ledger_path(book_dir)
    if ledger is None:
        return {
            "unverifiable": 1
        }, [  # un-verifiable means script cannot legally score this field
            "UNVERIFIABLE: no ledger found for autocomplete_richness"
        ], None

    actual: Dict[str, int] = {}
    with ledger.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # header
        for row in reader:
            if len(row) < 11:
                continue
            marker = row[10].strip()
            if not marker.startswith("mined from seed:"):
                continue
            seed = marker.split(":", 1)[1].strip()
            actual[seed] = actual.get(seed, 0) + 1

    problems: List[str] = []
    verified: Dict[str, int] = {}
    for seed, raw_claim in claim.items():
        seed_name = str(seed).strip()
        claimed = _parse_int(raw_claim)
        if claimed is None:
            problems.append(f"autocomplete_richness[{seed_name}] is not numeric: {raw_claim!r}")
            continue
        harvested = actual.get(seed_name, 0)
        verified[seed_name] = harvested
        if claimed != harvested:
            problems.append(
                f"autocomplete_richness[{seed_name}] claimed {claimed} but ledger has {harvested}"
            )

    return verified, problems, source


def _audit_trademark(evidence: Dict[str, Any], book_dir: Path) -> List[str]:
    if _unknown(evidence.get("trademark_status", "UNKNOWN")):
        return []

    claimed = evidence.get("trademark_status")
    if claimed not in {"no_conflict_found", "conflict", "uncertain"}:
        return [f"trademark_status invalid value: {claimed!r}"]

    path = book_dir / "research" / "trademark.md"
    if not path.exists():
        return [f"trademark_status cross-check failed: missing {path}"]

    claimed = str(claimed).strip().lower()
    target = f"{claimed}"
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            m = re.search(r"(?i)\bverdict\b\s*[:=]\s*([a-z_]+)", line)
            if not m:
                continue
            if m.group(1).strip().lower() == target:
                return []

    return [
        f"trademark_status cross-check failed: {path} has no line with matching verdict '{claimed}'"
    ]


def _audit_comp_table(evidence: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[str], int, int]:
    comp_table = evidence.get("comp_table")
    if _unknown(comp_table):
        return [], [], 0, 0

    if not isinstance(comp_table, list):
        return [], [f"comp_table must be a list, got {type(comp_table).__name__}"], 0, 0

    row_count = len(comp_table)
    valid_rows: List[Dict[str, Any]] = []
    problems: List[str] = []
    under_50k = 0
    required_row_keys = {"title", "asin", "bsr", "price", "review_count", "latest_review_date"}

    for idx, row in enumerate(comp_table, start=1):
        if not isinstance(row, dict):
            problems.append(f"comp_table row {idx} is not a mapping")
            continue
        missing = sorted(required_row_keys - row.keys())
        if missing:
            problems.append(f"comp_table row {idx} missing keys: {', '.join(missing)}")
            continue

        bsr = _parse_int(row.get("bsr"))
        review_count = _parse_int(row.get("review_count"))
        if bsr is None or review_count is None:
            problems.append(f"comp_table row {idx} must have non-null bsr and review_count")
            continue

        valid_rows.append(row)
        if bsr <= 50_000:
            under_50k += 1

    return valid_rows, problems, row_count, under_50k


def _normalize_trend(value: Any) -> str:
    if _unknown(value) or value is None:
        return "UNKNOWN"
    text = str(value).strip().lower()
    if text == "rising":
        return "rising"
    if text == "flat":
        return "flat"
    if text == "declining":
        return "declining"
    return "other"


def _to_bool_like(value: Any) -> str:
    if _unknown(value):
        return "UNKNOWN"
    return str(value).strip().lower()


def _is_competition_enterable(value: Any) -> Tuple[bool | None, int | None]:
    if _unknown(value):
        return None, None
    if isinstance(value, (int, float)):
        n = int(value)
        return (n < 10_000, n)
    text = str(value).strip().lower()
    try:
        n = int(text)
        return (n < 10_000, n)
    except ValueError:
        if "sub-niche" in text or "subniche" in text or "clear" in text:
            return True, None
        return None, None


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python3 tooling/scripts/niche_verdict.py <book-slug>")
        raise SystemExit(2)

    slug = sys.argv[1]
    book_dir = BOOKS_DIR / slug
    evidence_path = book_dir / "research" / "evidence.yaml"
    charter_path = book_dir / "research" / "charter.md"

    if not evidence_path.exists():
        raise SystemExit(2)
    if not charter_path.exists():
        raise SystemExit(2)

    evidence = _read_yaml(evidence_path)
    charter_values, charter_issues = _parse_charter(charter_path)

    missing_evidence = [k for k in REQUIRE_KEYS if k not in evidence]
    unknown_evidence = [k for k in REQUIRE_KEYS if k in evidence and _unknown(evidence[k])]

    # Two different kinds of "not ready", and conflating them is what made the first draft of
    # this script unable to reproduce the verdict the pipeline actually reached on 2026-08-08.
    #
    # BLOCKING = the evidence base is broken or the goal was never set: a claim contradicted by
    # the artifact behind it, or a charter still holding placeholders. Nothing can be computed
    # on top of that, so it forces INCOMPLETE outright.
    #
    # GAPS = fields still UNKNOWN. These block GO — you cannot certify what you did not measure
    # — but PIVOT and KILL stay computable, because deciding "the entry angle is wrong" needs
    # far less evidence than deciding "this book is worth writing". Stage 0 exists to kill and
    # redirect cheaply; requiring a full dossier before it may say PIVOT would defeat the gate.
    blocking: List[str] = []
    gaps: List[str] = []

    blocking.extend([f"evidence key missing: {k}" for k in missing_evidence])
    blocking.extend(charter_issues)
    gaps.extend([f"evidence field unknown: {k}" for k in unknown_evidence])

    verified_seed_counts, autocomplete_issues, ledger_source = _audit_autocomplete(evidence, book_dir)
    blocking.extend(autocomplete_issues)

    trademark_issues = _audit_trademark(evidence, book_dir)
    blocking.extend(trademark_issues)

    valid_comp_rows, comp_issues, comp_row_count, under_50k = _audit_comp_table(evidence)
    blocking.extend(comp_issues)
    issues = blocking + gaps
    claimed_under_50k = evidence.get("comps_under_50k_bsr")
    if not _unknown(claimed_under_50k):
        claimed_under_50k_int = _parse_int(claimed_under_50k)
        if claimed_under_50k_int is None:
            issues.append(f"comps_under_50k_bsr is not numeric: {claimed_under_50k!r}")
        elif claimed_under_50k_int != under_50k:
            issues.append(
                f"comps_under_50k_bsr claimed {claimed_under_50k_int} but comp_table yields {under_50k}"
            )

    # Step 4 in .agents/skills/niche-research/SKILL.md: GO/PIVOT/KILL thresholds.
    trend = _normalize_trend(evidence.get("trend_direction", "UNKNOWN"))
    demand_direction = trend != "declining"
    competition_enterable, result_count = _is_competition_enterable(
        evidence.get("result_count_or_subniche", "UNKNOWN")
    )
    authority_fit = _to_bool_like(evidence.get("authority_fit"))
    # Harvested KEYWORDS, not comps. Naming this "comps_total" once printed a keyword count
    # under a comp label in the verdict line — the kind of number a later stage would cite.
    autocomplete_total = sum(_parse_int(v) or 0 for v in evidence.get("autocomplete_richness", {}).values()) \
        if isinstance(evidence.get("autocomplete_richness"), dict) else 0
    demand_proven = trend in {"rising", "flat"} and autocomplete_total > 0
    has_shelf = (competition_enterable is True) or (comp_row_count > 0)
    demand_angle_wrong = demand_proven and (
        (result_count is not None and result_count >= 10_000) or (competition_enterable is False)
    )
    differentiation_credible = (
        not _unknown(evidence.get("gap_statement", "UNKNOWN"))
        and not _unknown(evidence.get("differentiation_contract", "UNKNOWN"))
        and authority_fit == "y"
    )
    trademark_clear = evidence.get("trademark_status") == "no_conflict_found"

    go_conditions = (
        not issues  # every field measured AND every cross-check passed
        and demand_direction
        and not _unknown(evidence.get("autocomplete_richness", "UNKNOWN"))
        and (autocomplete_total > 0)
        and (_parse_int(evidence.get("comps_under_50k_bsr", 0)) or 0) >= 2
        and (competition_enterable is True)
        and differentiation_credible
        and trademark_clear
    )

    # A contradicted claim or an unset goal ends the run. We do not compute a verdict on top of
    # an evidence base we already know is wrong — that is the failure this script exists to stop.
    if blocking:
        reason = "; ".join(blocking)
        if ledger_source:
            reason += f"; autocomplete ledger source: {ledger_source}"
        print(f"INCOMPLETE: {reason}")
        return

    if go_conditions:
        summary = [
            f"trend_direction={trend}",
            f"autocomplete_total={autocomplete_total}",
            f"comps_under_50k_bsr={evidence['comps_under_50k_bsr']}",
            f"result_count_or_subniche={evidence['result_count_or_subniche']}",
            f"trademark_status={evidence['trademark_status']}",
        ]
        if ledger_source:
            summary.append(f"autocomplete_ledger={ledger_source}")
        print(f"GO: {', '.join(summary)}")
        return

    # KILL demands POSITIVE evidence of absence. Never an unmeasured field.
    #
    # The first version had `not has_shelf` as a trigger, and has_shelf is false whenever the
    # comp data is UNKNOWN — so a book nobody had looked at yet was killed for having "no
    # shelf". collector_health does not catch it: the collector was fine, the measurement was
    # simply never taken. Absence of evidence is not evidence of absence, and this gate is the
    # one place where confusing the two destroys a viable book instead of merely delaying it.
    shelf_measured = not _unknown(evidence.get("result_count_or_subniche", "UNKNOWN")) or not _unknown(
        evidence.get("comp_table", "UNKNOWN")
    )
    kill_conditions = (
        (trend == "declining" and not demand_proven)
        or (shelf_measured and not has_shelf)
        or (authority_fit == "n")
        or (evidence.get("trademark_status") == "conflict")
    )
    # collector_health gates the whole KILL branch: an empty harvest from a blocked collector
    # must never be recorded as "no demand".
    if kill_conditions and evidence.get("collector_health") == "CONFIRMED":
        summary = [
            f"collector_health={evidence['collector_health']}",
            f"trend_direction={trend}",
            f"comps_under_50k_bsr={evidence['comps_under_50k_bsr']}",
            f"authority_fit={authority_fit}",
            f"trademark_status={evidence['trademark_status']}",
        ]
        print(f"KILL: {', '.join(summary)}")
        return

    if demand_proven and demand_angle_wrong:
        summary = [
            f"trend_direction={trend}",
            f"autocomplete_total={autocomplete_total}",
            f"result_count_or_subniche={result_count}",
            f"comps_under_50k_bsr={evidence['comps_under_50k_bsr']}",
        ]
        print(f"PIVOT: {', '.join(summary)}")
        return

    if demand_proven:
        print(f"PIVOT: trend_direction={trend}, autocomplete_total={autocomplete_total}, authority_fit={authority_fit}")
        return

    print("INCOMPLETE: insufficient complete evidence to support GO/PIVOT/KILL")


if __name__ == "__main__":
    main()
