#!/usr/bin/env python3
"""Controlled-vocabulary and locale checks for a graded reader.

This is the artifact that makes books/spanish-graded-reader-a2/research/charter.md
honest. The charter claims no fluency and no lived authority; it claims only that
every Spanish sentence passes a reproducible check. That claim is worth nothing
unless this runs before a chapter is written, not after.

Scope on purpose (ponytail): stdlib only, checks that actually fail on real
mistakes. Morphology, entailment and back-translation are NOT here — they need a
real analyzer and a model call, and stubbing them would fake coverage the charter
would then cite. They stay listed as unimplemented in the book's tasks.md.

  ponytail: naive whitespace/punctuation tokenizer, no lemmatizer. An A1 wordlist is
  a surface-form list, so surface matching is the honest comparison. Swap in a real
  lemmatizer (spaCy es_core_news_sm) only when the OOV rate is dominated by
  inflection rather than by genuinely new words. Until then the unit is a
  NORMALIZED SURFACE TYPE, not a word or a lexeme — do not overstate it in a contract.

THE CUMULATIVE KNOWN-SET (added 2026-08-13, and the reason this file was rewritten)
-----------------------------------------------------------------------------------
The original version compared every story against the baseline frequency list ALONE.
That silently contradicted the book's own pedagogy: a word glossed in story 01 was
counted as brand-new again in stories 02..10, so `quiosco` and `muelle` were charged
to the reader eight times over. Measured coverage looked far worse than the reading
experience actually was — story 04 read as 0.911 when, counting what the reader had
already been taught, it is 0.968.

The wrong fix was applied first: `--max-new-types` was made to DISABLE the coverage
failure, which is a threshold change dressed as a metric change, made after stories
had already missed the number. That is the Drifting Goals archetype and
`.agents/rules/quality-gates.md` exists to prevent it.

The right fix is here: pass `--ledger` and `--story NN` so the known set is
baseline + names + everything genuinely closed in earlier stories, and let BOTH
gates fail independently. They measure different risks and must be allowed to fight:

  * coverage bounds READING FRICTION — how often the reader stalls;
  * new-type count bounds LEARNING LOAD — how much they must be taught.

A type-only gate is unsafe on its own: one unknown word repeated three hundred times
passes a 25-type cap while making the text unreadable. `selfcheck()` asserts exactly
that case, so this cannot silently regress.

Usage:
    graded_reader_check.py --wordlist a1.txt --text story04.md \\
        --ledger bible/vocabulary-ledger.md --story 04 \\
        --names "ana,beto" --locale latam --max-new-types 25
    graded_reader_check.py --selfcheck
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata

# Forms that are mutually exclusive between the two locales a Spanish reader may
# declare. Mixing them inside one book is the single most visible tell that the text
# was assembled rather than written, and it is cheap to catch.
LOCALE_MARKERS = {
    "peninsular": {"vosotros", "vuestro", "vuestra", "vuestros", "vuestras"},
    "latam": {"ustedes"},
}

TOKEN_RE = re.compile(r"[^\W\d_]+", re.UNICODE)
# Matches "### Story 04" / "### Historia 4" headings in the vocabulary ledger.
LEDGER_HEADING_RE = re.compile(
    r"^#{2,4}\s*(?:Story|Historia)\s*0*(\d+)\s*$", re.IGNORECASE | re.MULTILINE
)


def normalize(word: str) -> str:
    """Casefold and strip accents so `Él` and `el` do not count as two words.

    Accent-stripping is deliberate: A1 wordlists are published unaccented about as
    often as not, and an accent mismatch is a typography bug, not a vocabulary breach.
    """
    folded = unicodedata.normalize("NFD", word.casefold())
    return "".join(c for c in folded if unicodedata.category(c) != "Mn")


def tokenize(text: str) -> list[str]:
    return [normalize(m.group()) for m in TOKEN_RE.finditer(text)]


def prior_words(ledger_text: str, story: int) -> set[str]:
    """Normalized words closed by stories numbered strictly BEFORE `story`.

    The vocabulary ledger is the single source of truth for what the reader has
    already been taught, so this reads it directly rather than depending on a
    generated side-file that could drift out of date.
    """
    out: set[str] = set()
    matches = list(LEDGER_HEADING_RE.finditer(ledger_text))
    for i, m in enumerate(matches):
        n = int(m.group(1))
        if n >= story:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(ledger_text)
        body = ledger_text[m.end():end]
        out |= {normalize(t.group()) for t in TOKEN_RE.finditer(body)}
    return out


def coverage(text: str, wordlist: set[str]) -> tuple[float, dict[str, int]]:
    """Return (in-vocabulary ratio, out-of-vocabulary word -> count).

    The ratio is over token occurrences, not unique words: one unknown word repeated
    twelve times is twelve chances for the reader to stall, and averaging it away
    would hide exactly the failure this check exists to catch. That is why this
    metric survives alongside the new-type budget instead of being replaced by it.
    """
    tokens = tokenize(text)
    if not tokens:
        return 1.0, {}
    known = {normalize(w) for w in wordlist}
    oov: dict[str, int] = {}
    for tok in tokens:
        if tok not in known:
            oov[tok] = oov.get(tok, 0) + 1
    in_vocab = len(tokens) - sum(oov.values())
    return in_vocab / len(tokens), oov


def locale_violations(text: str, locale: str) -> set[str]:
    """Markers belonging to a locale the book did not declare."""
    if locale not in LOCALE_MARKERS:
        raise ValueError(f"unknown locale {locale!r}; expected one of {sorted(LOCALE_MARKERS)}")
    tokens = set(tokenize(text))
    forbidden: set[str] = set()
    for name, markers in LOCALE_MARKERS.items():
        if name != locale:
            forbidden |= {normalize(m) for m in markers}
    return tokens & forbidden


def selfcheck() -> None:
    wl = {"el", "gato", "come", "pescado", "ustedes", "y"}

    ratio, oov = coverage("El gato come pescado.", wl)
    assert ratio == 1.0, ratio
    assert oov == {}, oov

    # Accented and capitalised forms must not read as unknown words.
    ratio, oov = coverage("Él comé pescado", {"el", "come", "pescado"})
    assert ratio == 1.0, (ratio, oov)

    # One unknown word repeated is counted every time, not once.
    ratio, oov = coverage("gato zzz zzz zzz", wl)
    assert oov == {"zzz": 3}, oov
    assert ratio == 0.25, ratio

    # Empty text is vacuously covered rather than a ZeroDivisionError.
    assert coverage("", wl) == (1.0, {})

    # A latam book must not contain peninsular second-person plural forms.
    assert locale_violations("¿Vosotros venís?", "latam") == {"vosotros"}
    assert locale_violations("¿Ustedes vienen?", "latam") == set()
    # ...and the check is symmetric.
    assert locale_violations("¿Ustedes vienen?", "peninsular") == {"ustedes"}

    try:
        locale_violations("hola", "castellano")
    except ValueError:
        pass
    else:  # pragma: no cover
        raise AssertionError("unknown locale must raise")

    # --- the cumulative known-set, which is why this file was rewritten ---
    ledger = (
        "## Glossaries\n"
        "### Story 01\nquiosco, muelle,\n"
        "### Story 02\npanaderia,\n"
        "### Story 03\ntaza,\n"
    )
    assert prior_words(ledger, 1) == set(), prior_words(ledger, 1)
    assert prior_words(ledger, 2) == {"quiosco", "muelle"}, prior_words(ledger, 2)
    assert prior_words(ledger, 3) == {"quiosco", "muelle", "panaderia"}, prior_words(ledger, 3)
    # Accented ledger entries normalise to the same key the tokenizer produces.
    assert "panaderia" in prior_words("### Story 01\npanadería\n", 2)
    # A story's OWN section must never count as already-known.
    assert "taza" not in prior_words(ledger, 3)

    # A word taught earlier stops being out-of-vocabulary later.
    assert coverage("quiosco", {"el"})[0] == 0.0
    assert coverage("quiosco", {"el"} | prior_words(ledger, 2))[0] == 1.0

    # THE CASE A TYPE-ONLY GATE CANNOT SEE: one unknown word, repeated until the text
    # is unreadable, is a single type. Coverage must catch what the type budget misses.
    hostile = "el " + "zzz " * 300
    ratio, oov = coverage(hostile, {"el"})
    assert len(oov) == 1, oov              # passes any sane --max-new-types
    assert ratio < 0.01, ratio             # and coverage must still fail it
    print("selfcheck ok")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--wordlist", help="one surface form per line (the baseline frequency list)")
    ap.add_argument("--text", help="the Spanish text to check")
    # Character names are not vocabulary burden — every graded reader introduces them and no
    # learner is expected to have them in an A1 list. Counting them as out-of-vocabulary made a
    # perfectly compliant story read as 76% coverage, which would have sent a real chapter back
    # for rewriting for no reason.
    ap.add_argument("--names", default="",
                    help="comma-separated proper nouns to treat as known (character/place names)")
    ap.add_argument("--ledger", help="vocabulary-ledger.md; words closed in EARLIER stories count as known")
    ap.add_argument("--story", type=int,
                    help="this story's number; required with --ledger so its own glossary is excluded")
    ap.add_argument("--locale", default="latam", choices=sorted(LOCALE_MARKERS))
    ap.add_argument("--min-coverage", type=float, default=0.95,
                    help="fail below this in-vocabulary ratio (default 0.95)")
    # Bounds LEARNING LOAD, where coverage bounds READING FRICTION. Both are fatal; neither
    # disables the other. `25` is this book's working budget and is NOT research-backed — no
    # source establishes a distinct-new-word-per-story figure for Spanish A1. Treat it as a
    # project convention recorded in .agents/rules/quality-gates.md, not as a finding.
    ap.add_argument("--max-new-types", type=int, default=None,
                    help="fail if distinct out-of-vocabulary types exceed this (glossary budget)")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args()

    if args.selfcheck:
        selfcheck()
        return 0
    if not (args.wordlist and args.text):
        ap.error("--wordlist and --text are required unless --selfcheck")
    if bool(args.ledger) != (args.story is not None):
        ap.error("--ledger and --story must be given together")

    with open(args.wordlist, encoding="utf-8") as fh:
        wordlist = {line.strip() for line in fh if line.strip()}
    wordlist |= {n.strip() for n in args.names.split(",") if n.strip()}
    taught: set[str] = set()
    if args.ledger:
        with open(args.ledger, encoding="utf-8") as fh:
            taught = prior_words(fh.read(), args.story)
        wordlist |= taught
    with open(args.text, encoding="utf-8") as fh:
        text = fh.read()

    ratio, oov = coverage(text, wordlist)
    bad_locale = locale_violations(text, args.locale)
    total = len(tokenize(text))
    unknown = sum(oov.values())

    if taught:
        print(f"known set: baseline + names + {len(taught)} types taught before story {args.story:02d}")
    # Unrounded evidence, not just three decimals: a reviewer must be able to recompute this.
    print(f"coverage: {ratio:.3f}  ({total - unknown}/{total} tokens known, "
          f"{unknown} unknown)  threshold {args.min_coverage}")
    print(f"new word types (glossary): {len(oov)}"
          + (f" (budget {args.max_new_types})" if args.max_new_types is not None else ""))
    if oov:
        print("glossary — every distinct word the reader must be given:")
        for word, n in sorted(oov.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {word}\t{n}")
    if bad_locale:
        print(f"locale violations for {args.locale}: {sorted(bad_locale)}")

    # All three gates are INDEPENDENTLY fatal. An earlier version let --max-new-types
    # suppress the coverage failure; that made the inconvenient half of the contract
    # non-fatal by passing a flag, which is a gate change, not a measurement.
    failures = []
    if bad_locale:
        failures.append(f"locale: {sorted(bad_locale)}")
    if ratio < args.min_coverage:
        failures.append(f"coverage {ratio:.3f} < {args.min_coverage}")
    if args.max_new_types is not None and len(oov) > args.max_new_types:
        failures.append(f"new types {len(oov)} > {args.max_new_types}")
    if failures:
        print("FAIL: " + "; ".join(failures))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
