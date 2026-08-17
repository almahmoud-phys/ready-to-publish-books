"""The lexical gate must not be silently weakenable.

This suite exists because it already happened once. On 2026-08-13 `--max-new-types`
was made to DISABLE the coverage failure, after stories had missed the coverage
number — a threshold change wearing a metric change's clothes. External review
(codex gpt-5.6-sol) caught it, and the root cause turned out to be a real bug:
the checker never consumed the vocabulary ledger, so a word taught in story 01 was
charged to the reader again in every later story.

These tests pin both halves down: the cumulative known-set, and the rule that
neither gate may switch the other off.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tooling" / "scripts" / "graded_reader_check.py"
sys.path.insert(0, str(SCRIPT.parent))

from graded_reader_check import coverage, normalize, prior_words  # noqa: E402


def run(*args, **kw):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True, **kw)


def write(tmp_path, name, body):
    p = tmp_path / name
    p.write_text(body, encoding="utf-8")
    return str(p)


LEDGER = (
    "## Glossaries\n"
    "### Story 01\nquiosco, muelle,\n"
    "### Story 02\npanadería,\n"
    "### Story 03\ntaza,\n"
)


def test_selfcheck_passes():
    r = run("--selfcheck")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "selfcheck ok" in r.stdout


def test_prior_words_excludes_own_and_later_stories():
    assert prior_words(LEDGER, 1) == set()
    assert prior_words(LEDGER, 2) == {"quiosco", "muelle"}
    # Its own glossary must never count as already-taught, or a story grades itself.
    assert "taza" not in prior_words(LEDGER, 3)
    # Later stories must not leak backwards either.
    assert "taza" not in prior_words(LEDGER, 2)


def test_prior_words_normalizes_accents():
    # The ledger stores "panadería"; the tokenizer produces "panaderia".
    assert "panaderia" in prior_words(LEDGER, 3)


def test_taught_words_stop_counting_as_unknown():
    """The bug that caused the whole reconciliation: no ledger, no credit."""
    baseline = {"el"}
    assert coverage("quiosco", baseline)[0] == 0.0
    assert coverage("quiosco", baseline | prior_words(LEDGER, 2))[0] == 1.0


def test_repeated_unknown_word_defeats_a_type_only_gate(tmp_path):
    """One unknown word x300 is ONE type. Coverage is the only thing that catches it.

    This is the concrete reason a distinct-new-types budget cannot replace coverage:
    it bounds learning load, not reading friction.
    """
    wl = write(tmp_path, "wl.txt", "el\n")
    txt = write(tmp_path, "t.md", "el " + "zzz " * 300)
    r = run("--wordlist", wl, "--text", txt, "--max-new-types", "25")
    assert r.returncode == 1, r.stdout
    assert "new word types (glossary): 1" in r.stdout   # sails through the type cap
    assert "coverage" in r.stdout and "FAIL" in r.stdout  # and is still rejected


def test_max_new_types_does_not_suppress_coverage_failure(tmp_path):
    """The exact regression that triggered this file. Never again."""
    wl = write(tmp_path, "wl.txt", "el\ngato\n")
    txt = write(tmp_path, "t.md", "el gato zzz qqq")
    without = run("--wordlist", wl, "--text", txt)
    with_cap = run("--wordlist", wl, "--text", txt, "--max-new-types", "25")
    assert without.returncode == 1
    # Passing a generous type budget must NOT turn a coverage failure into a pass.
    assert with_cap.returncode == 1, with_cap.stdout


def test_type_budget_is_independently_fatal(tmp_path):
    """Coverage fine, too many distinct new words -> still a failure."""
    # Note: the tokenizer drops digits, so filler words must be purely alphabetic
    # or they all collapse to the same type.
    filler = ["".join(("q", chr(97 + i // 26), chr(97 + i % 26))) for i in range(200)]
    wl = write(tmp_path, "wl.txt", "\n".join(filler))
    body = " ".join(filler) + " aa bb cc"
    txt = write(tmp_path, "t.md", body)
    ok = run("--wordlist", wl, "--text", txt, "--max-new-types", "25")
    assert ok.returncode == 0, ok.stdout          # 3 new types, coverage ~0.985
    tight = run("--wordlist", wl, "--text", txt, "--max-new-types", "2")
    assert tight.returncode == 1, tight.stdout
    assert "new types 3 > 2" in tight.stdout


def test_locale_violation_is_independently_fatal(tmp_path):
    wl = write(tmp_path, "wl.txt", "vosotros\nvenis\n")
    txt = write(tmp_path, "t.md", "vosotros venis")
    r = run("--wordlist", wl, "--text", txt, "--locale", "latam")
    assert r.returncode == 1                       # perfect coverage, wrong continent
    assert "locale" in r.stdout


def test_ledger_and_story_must_be_given_together(tmp_path):
    wl = write(tmp_path, "wl.txt", "el\n")
    txt = write(tmp_path, "t.md", "el")
    led = write(tmp_path, "led.md", LEDGER)
    assert run("--wordlist", wl, "--text", txt, "--ledger", led).returncode == 2
    assert run("--wordlist", wl, "--text", txt, "--story", "2").returncode == 2


def test_coverage_evidence_is_printed_not_just_rounded(tmp_path):
    """A reviewer must be able to recompute the ratio from the output."""
    wl = write(tmp_path, "wl.txt", "el\n")
    txt = write(tmp_path, "t.md", "el el zzz")
    r = run("--wordlist", wl, "--text", txt, "--min-coverage", "0.0")
    assert "2/3 tokens known" in r.stdout, r.stdout


def test_names_are_not_vocabulary_burden(tmp_path):
    wl = write(tmp_path, "wl.txt", "el\n")
    txt = write(tmp_path, "t.md", "el Ana")
    assert run("--wordlist", wl, "--text", txt).returncode == 1
    assert run("--wordlist", wl, "--text", txt, "--names", "ana").returncode == 0


def test_normalize_is_case_and_accent_insensitive():
    assert normalize("Él") == normalize("el") == "el"
    assert normalize("PANADERÍA") == "panaderia"
