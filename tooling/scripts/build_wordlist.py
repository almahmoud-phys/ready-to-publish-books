#!/usr/bin/env python3
"""Derive a citable, licensed Spanish frequency baseline for the graded-reader checks.

WHY THIS EXISTS. The first wordlist was agent-assembled with no source and no license, which
made every coverage number unfalsifiable — the check ran, but it certified nothing. Codex called
this a blocker for WRITING rather than publishing, and it was right: vocabulary is a generative
constraint for a graded reader, so swapping the list after drafting forces rewrites.

SOURCE. OpenSLR SLR21, "es_wordlist.json" (Spanish word frequency list built from a news/web
crawl), https://www.openslr.org/21/ — licensed CC BY-SA 3.0. Attribution and the license must
appear in the book's back matter; CC BY-SA is share-alike, so the DERIVED WORDLIST FILE is
redistributed under CC BY-SA 3.0 too. That obligation does not extend to the book's prose, which
is an independent work, but the wordlist artifact itself carries it. Do not lose this note.

WHAT THIS IS NOT. A frequency list is not a CEFR A1 list. High frequency correlates with early
acquisition but does not certify a level, and the source is a news/web crawl, so its register
skews journalistic. The book's charter already forbids claiming CEFR certification; this file is
a defensible PROXY with a documented cutoff, nothing more. A real A1 list (e.g. ELELex) is
A1-graded but noncommercially licensed, so it is unusable here without separate permission.

  ponytail: rank-cutoff only, no lemmatizer. The check compares surface forms, so a surface-form
  list is the honest comparison. Lemmatize on both sides at once (spaCy es_core_news_sm) or not
  at all — lemmatizing one side silently inflates coverage.

Usage:
    build_wordlist.py --source es_wordlist.json --out wordlist.txt --top 2000
    build_wordlist.py --selfcheck
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata

# Spanish letters only. Excludes digits, punctuation, and anything with crawl noise, which the
# raw source is full of ("1525GMT", "ppymeesb", "IrakconferenciaEEUUIrancena").
WORD_RE = re.compile(r"^[a-záéíóúüñ]+$")

# Crawl artifacts frequent enough to survive a rank cutoff but not Spanish words.
STOP_ARTIFACTS = {"http", "https", "www", "com", "html", "gmt", "efe", "ap", "reuters"}


def is_plausible_word(token: str, min_len: int = 1, max_len: int = 16) -> bool:
    """Keep lowercase Spanish alphabetic tokens of a sane length.

    Lowercase-only is deliberate and does real work: it drops the crawl's enormous proper-noun
    tail (`Eniutin`, `Hoogestijn`, `Seyud`) without needing a named-entity model. Character names
    are handled separately by the checker's --names flag.
    """
    if not (min_len <= len(token) <= max_len):
        return False
    if token in STOP_ARTIFACTS:
        return False
    return bool(WORD_RE.match(token))


def load_freqs(path: str) -> dict[str, int]:
    """Accept either a JSON {token: count} map or a `word count` per line text list.

    Two formats because the two corpora that matter ship differently, and the REGISTER matters
    far more than the format:
      - OpenSLR SLR21 (JSON): news/web crawl. Measured against a story it tops out around 0.90
        coverage even at rank 5000, and the words it misses are `ventana`, `silla`, `mira`,
        `vieja` — the basic furniture of narrative. Its top-2000 is `crisis, guerra, mercado,
        muertos`. Wrong register for fiction; keep it only as a cross-check.
      - hermitdave/FrequencyWords (text): derived from OpenSubtitles, i.e. spoken dialogue.
        That is the register a graded reader actually writes in.
    """
    if path.endswith(".json"):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    freqs: dict[str, int] = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                freqs[parts[0]] = int(parts[1])
            except ValueError:
                continue
    return freqs


def top_words(freqs: dict[str, int], n: int) -> list[str]:
    """Highest-count plausible words first, ties broken alphabetically for reproducibility."""
    kept = [(w, c) for w, c in freqs.items() if is_plausible_word(w)]
    kept.sort(key=lambda wc: (-wc[1], wc[0]))
    return [w for w, _ in kept[:n]]


def selfcheck() -> None:
    assert is_plausible_word("casa")
    assert is_plausible_word("niña")
    assert is_plausible_word("está")
    assert not is_plausible_word("Madrid"), "proper nouns must be dropped"
    assert not is_plausible_word("1525gmt"), "digits must be dropped"
    assert not is_plausible_word("http"), "crawl artifacts must be dropped"
    assert not is_plausible_word(""), "empty token must be dropped"
    assert not is_plausible_word("a" * 30), "absurd length must be dropped"

    freqs = {"el": 100, "casa": 50, "Madrid": 999, "zzz9": 999, "gato": 50}
    out = top_words(freqs, 10)
    assert out == ["el", "casa", "gato"], out          # Madrid/zzz9 filtered despite high counts
    assert top_words(freqs, 2) == ["el", "casa"]       # cutoff respected
    # Ties break alphabetically, so the same input always yields the same file.
    assert top_words({"b": 5, "a": 5}, 2) == ["a", "b"]
    print("selfcheck ok")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", help="OpenSLR SLR21 es_wordlist.json ({token: count})")
    ap.add_argument("--out", help="output path, one surface form per line")
    ap.add_argument("--top", type=int, default=2000, help="rank cutoff (default 2000)")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args()

    if args.selfcheck:
        selfcheck()
        return 0
    if not (args.source and args.out):
        ap.error("--source and --out are required unless --selfcheck")

    freqs = load_freqs(args.source)
    words = top_words(freqs, args.top)

    with open(args.out, "w", encoding="utf-8") as fh:
        for w in words:
            fh.write(unicodedata.normalize("NFC", w) + "\n")

    print(f"wrote {len(words)} forms to {args.out} (top {args.top} of {len(freqs)} raw tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
