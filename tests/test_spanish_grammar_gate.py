"""Regression fixtures for the grammar-ladder checker.

Two kinds of test live here and they are NOT interchangeable:

  1. Defects the checker must catch. These are the real misses that motivated it —
     `Le gusta` in story 01 and `Escriba` in story 03 both survived roughly fifteen
     readings of the manuscript.
  2. Things it must stay QUIET about. A gate that fires on ordinary present-tense
     narration gets switched off within a day, so the false-positive tests matter as
     much as the true-positive ones. Both false positives pinned below were real bugs,
     found on the checker's first run against the manuscript.

The ceiling tests at the bottom assert what the checker CANNOT do. They look strange —
tests demanding that a defect go unreported — but they are load-bearing: the docstring
promises this is lint and not an oracle, and if a later change silently made those cases
fail, that promise would have become a lie with nobody noticing.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tooling" / "scripts" / "spanish_grammar_check.py"
sys.path.insert(0, str(SCRIPT.parent))

from spanish_grammar_check import (  # noqa: E402
    BANNED, MIN_STORY, UNLEVELLED, check, find_constructs,
)


def fails(text, story):
    return check(text, story)[0]


# --------------------------------------------------------------------------- catches

def test_selfcheck_passes():
    r = subprocess.run([sys.executable, str(SCRIPT), "--selfcheck"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "selfcheck ok" in r.stdout


def test_imperative_is_caught_anywhere():
    """`Escriba tres cosas` shipped in two stories' exercises and nobody saw it."""
    for story in (1, 5, 10):
        assert any("imperative" in f for f in fails("Escriba tres cosas.", story))


def test_gustar_before_its_story_is_caught():
    """The `le` is what raises the level, not `gustar`."""
    assert any("gustar" in f and "EARLY" in f for f in fails("Le gusta estar sola.", 1))
    assert not fails("A Ana le gusta el mar.", 6)


def test_imperfect_is_banned_even_in_the_last_story():
    assert any("imperfect" in f for f in fails("Ana era joven y trabajaba.", 10))
    assert any("imperfect" in f for f in fails("Iba al muelle.", 10))


def test_2026_08_14_story_02_estaba_defect_is_caught():
    """Story 02's banned `¿Dónde estaba?` escaped the grammar gate."""
    assert any("imperfect" in f and "estaba" in f
               for f in fails("¿Dónde estaba la carta?", 2))


def test_unlicensed_irregular_preterite_is_caught():
    """Story 09 licenses eight lemmas. `ver` and `dar` are not among them, and drafts
    have reached for `vio` before."""
    assert any("UNLICENSED" in f for f in fails("Ana vio la luz.", 10))
    assert any("UNLICENSED" in f and "leer" in f
               for f in fails("Rosa leyó la lista.", 8))
    assert not fails("Beto dijo la verdad.", 9)


def test_irregular_preterite_is_licensed_by_lemma_not_by_person():
    """The contract used to license eight 3sg FORMS while the prose used `dije`/`pude`."""
    for form in ("dije", "dijo", "pude", "pudo", "fui", "fue"):
        assert not fails(f"Ana {form} alli.", 9), form


def test_sequencing_fires_before_its_story_and_is_quiet_after():
    assert any("ir_a_infinitive" in f for f in fails("Mañana va a llegar el barco.", 2))
    assert not fails("Mañana va a llegar el barco.", 5)


def test_comparative_is_banned():
    assert any("comparative" in f for f in fails("Ana es más alta que Rosa.", 10))


# --------------------------------------------------------------- must stay quiet

def test_ordinary_present_narration_is_silent():
    """If this ever fails, the gate is crying wolf and will be switched off."""
    text = ("Ana mira el mar. Beto toma su café y habla con ella. "
            "El quiosco está abierto y hay pan en la mesa.")
    assert not fails(text, 1)


def test_desaparecer_is_an_er_verb():
    """Real bug: filed under -ar, so `desaparece` (3sg present) was read as an usted
    imperative and failed story 07."""
    assert not fails("El ruido de un bote suena lejos y desaparece.", 7)


def test_accent_separates_question_word_from_subordinator():
    """Real bug: the first version asked 'does this FILE contain a ?', so the
    subordinator in `cuando Ana vuelve del baño` was reported as a question word.
    Spanish marks the distinction with the accent; use that."""
    assert not fails("Cuando Ana vuelve del baño, hay una carta.", 1)
    assert any("cuando" in f and "EARLY" in f for f in fails("¿Desde cuándo trabaja?", 1))
    # basic question words are A1 and story 01 uses them in dialogue
    assert not fails("—¿Quién es Tomás Ferrer? —dice Ana.", 1)


# --------------------------------------------------------------- the stated ceiling

def test_temporal_misuse_is_NOT_detectable():
    """`Antes es de él` is present tense doing a past tense's job — a real bug that
    shipped. No form-based checker can see it. Asserted so the documented ceiling
    cannot quietly drift into an overclaim."""
    assert not fails("Antes es de él. Ahora es de usted.", 3)


def test_future_value_present_is_NOT_detectable():
    assert not fails("Mañana viene el barco.", 3)


# --------------------------------------------------------------- contract integrity

def test_unlevelled_constructs_are_declared_not_assumed():
    """PCIC cannot level these two. The checker must carry that fact, so it can never be
    cited as PCIC-backed evidence for them."""
    assert set(UNLEVELLED) == {"cuando", "mientras"}
    for k, why in UNLEVELLED.items():
        assert k in MIN_STORY, k
        assert "ouse decision" in why, (k, why)


def test_banned_constructs_carry_their_source():
    """A ban without a reason is an invented rule. Every entry cites PCIC or its absence."""
    for k, why in BANNED.items():
        assert "PCIC" in why, (k, why)


def test_house_decisions_are_reported_separately_from_failures():
    _, _, house = check("Mientras Ana mira, la luz se mueve.", 7)
    assert any("mientras" in h for h in house)


def test_evidence_is_returned_not_just_a_verdict():
    """A reviewer must see WHICH token triggered a finding."""
    hits = find_constructs("Le gusta el mar.")
    assert hits["gustar"] == ["le gusta"]
