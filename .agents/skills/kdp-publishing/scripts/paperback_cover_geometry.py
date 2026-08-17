#!/usr/bin/env python3
"""Check KDP paperback cover geometry using current published spine factors."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_CEILING


MM_PER_INCH = Decimal("25.4")
BLEED_IN = Decimal("0.125")
SPINE_IN = {
    "white": Decimal("0.002252"),
    "cream": Decimal("0.0025"),
    "premium-color": Decimal("0.002347"),
    "standard-color": Decimal("0.002252"),
}


def number(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.001")))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trim-width", required=True, type=Decimal)
    parser.add_argument("--trim-height", required=True, type=Decimal)
    parser.add_argument("--pages", required=True, type=int, help="PDF manuscript page count")
    parser.add_argument("--paper", required=True, choices=sorted(SPINE_IN))
    parser.add_argument("--units", choices=("mm", "in"), default="mm")
    args = parser.parse_args()

    if args.trim_width <= 0 or args.trim_height <= 0 or args.pages < 1:
        parser.error("trim dimensions and page count must be positive")

    production_pages = int(
        (Decimal(args.pages) / Decimal(2)).to_integral_value(rounding=ROUND_CEILING) * 2
    )
    multiplier = MM_PER_INCH if args.units == "mm" else Decimal(1)
    trim_width_in = args.trim_width / multiplier
    trim_height_in = args.trim_height / multiplier
    spine_in = Decimal(production_pages) * SPINE_IN[args.paper]
    full_width_in = BLEED_IN + trim_width_in * 2 + spine_in + BLEED_IN
    full_height_in = BLEED_IN + trim_height_in + BLEED_IN

    values_in = {
        "trim_width": trim_width_in,
        "trim_height": trim_height_in,
        "bleed_each_outside_edge": BLEED_IN,
        "spine_width": spine_in,
        "full_cover_width": full_width_in,
        "full_cover_height": full_height_in,
    }
    values = {key: number(value * multiplier) for key, value in values_in.items()}
    output = {
        "units": args.units,
        "paper": args.paper,
        "manuscript_pages": args.pages,
        "production_pages": production_pages,
        "odd_page_added": production_pages != args.pages,
        "spine_text_page_count_eligible": production_pages >= 80,
        **values,
        "warning": "Confirm production page count and dimensions with a fresh KDP template and Previewer.",
    }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
