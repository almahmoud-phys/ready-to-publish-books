#!/usr/bin/env python3
"""Grammar-ladder conformance for a graded reader. Lint, NOT an oracle.

WHY THIS EXISTS
---------------
The book's per-story grammar ladder was its core pedagogical claim and **nothing ever
checked it**. `graded_reader_check.py` does vocabulary and locale only; morphology is
explicitly absent there. The result, found on 2026-08-13: the ladder had been invented
by an agent, was never compared against any external source, and was wrong in both
directions — it banned A1 material and taught A2 material as if it were A1. Meanwhile
the prose used constructs several stories before the contract introduced them.

Levels here are not invented. They come from the Instituto Cervantes PCIC A1-A2
inventory via `_planning/pcic-ladder-table.md`.

WHY A SCRIPT AT ALL, GIVEN AN LLM "KNOWS SPANISH"
-------------------------------------------------
Story 01 was read about fifteen times without anyone noticing that `Le gusta` broke the
book's own rule, or that `Escriba` was an imperative. That is not a knowledge gap, it is
an ATTENTION gap: checking 7,000 words against ten rule sets is mechanical work where
sustained attention fails. A drafting checklist alone is not enough — it runs on the same
attention channel that already failed.

THE CEILING, STATED SO IT IS NOT IMPLIED AWAY
---------------------------------------------
This catches FORMS and PATTERNS. It cannot catch temporal misuse:
  * `mañana viene el barco`  - present with future value, morphologically identical to present
  * `Antes es de él`         - present doing a past tense's job (a real bug that shipped)
Both pass any form-based check. Habitual/cyclic present is likewise undetectable from
morphology alone. Say so wherever this script is cited. It is lint, not certification,
and never a marketing claim.

DESIGN (ponytail): stdlib only. No spaCy, no Stanza, no Apertium, no UD treebank.
The manuscript is a closed ~7,000-word world, so a reviewed surface-form table for the
verbs actually present beats a general morphological analyzer that would need installing,
pinning and trusting.

  ponytail: forms are GENERATED from a declared lemma set rather than pattern-matched on
  endings. That is deliberate. 483 of the manuscript's 558 distinct tokens end in something
  verb-shaped (`-a`, `-o`, `-e`, `-ir`...), because Spanish nouns and adjectives do too, so
  an ending heuristic produces mostly false positives. Generating from known lemmas means a
  hit is a real verb form, not a guess.

Usage:
    spanish_grammar_check.py --text chapters/03-*.md --story 3
    spanish_grammar_check.py --text 'chapters/*.md' --story 3 --inventory assets/tokens.txt
    spanish_grammar_check.py --write-inventory assets/tokens.txt --text 'chapters/*.md'
    spanish_grammar_check.py --selfcheck
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
import unicodedata

# --------------------------------------------------------------------------------------
# The ladder. Minimum story at which each construct may appear.
# Source of the LEVELS: PCIC (_planning/pcic-ladder-table.md).
# Source of the STORY NUMBERS: the book's own outline/chapter_NN.md contracts.
# These are different kinds of fact and are kept visibly separate on purpose: PCIC says
# what is A1 or A2, the book says when it teaches it. Only the second is ours to move.
# --------------------------------------------------------------------------------------
MIN_STORY = {
    "pres_irregular":      1,   # A2 — narrative Spanish cannot avoid dice/tiene/quiere
    "clitic_object_3p":    1,   # A2 — la pone, dejarla
    "interrogative_basic": 1,   # A1 — and story 01 uses `¿quién?` and `¿cómo?` in dialogue.
                                # The old ladder held these back to story 02, which was one of
                                # the two directions the invented ladder was wrong in: it banned
                                # material PCIC puts at A1.
    "cuando":              2,   # UNLEVELLED house decision (see below). Interrogative `cuándo`
                                # only; the unaccented subordinator is a different construct.
    "reflexive_basic":     3,   # A1
    "ir_a_infinitive":     5,   # A2
    "gustar":              6,   # me gusta A1 / le-les A2
    "estar_gerundio":      7,   # A2
    "mientras":            7,   # UNLEVELLED house decision (see below)
    "preterite_regular":   8,   # A2
    "preterite_irregular": 9,   # A2
}

# Never allowed, in any story. Volume 1 does not teach these at all.
BANNED = {
    "imperfect":   "PCIC A2 (§9.1.2). Volume 1 never teaches it.",
    "imperative":  "PCIC A2 (§9.3 — the A1 cell is empty). Absent from the book by design.",
    "subjunctive": "Beyond the PCIC A1-A2 inventory.",
    "comparative": "PCIC A2 (§2.5). Volume 1 never teaches it.",
}

# Constructs the PCIC A1-A2 page CANNOT level. Flagged in output as house decisions so
# nobody can cite this script as PCIC-backed evidence for them.
UNLEVELLED = {
    "cuando":   "cross-classified on the source page: A2 in §8.8, but §13.3 gives an A1 "
                "direct-question example. House decision: direct questions only, from story 02.",
    "mientras": "does not appear on the PCIC A1-A2 page at all. No level is derivable from "
                "that source. House decision: from story 07.",
}

# --------------------------------------------------------------------------------------
# Declared lemma set: the verbs the manuscript actually uses.
# A verb missing here is not silently ignored — the inventory guard catches any token
# this file cannot account for.
# --------------------------------------------------------------------------------------
AR = """abrazar arreglar ayudar bajar buscar caminar cerrar comprar contestar dejar
empezar encontrar esperar frotar golpear guardar hablar limpiar llamar llegar llevar llorar mandar
mirar necesitar pagar parar pasar pensar preguntar quedar quitar sacar tomar trabajar""".split()
ER = """aparecer beber comer conocer correr deber desaparecer entender leer llover mover parecer romper
temer vender volver""".split()
IR = """abrir decidir escribir mentir pedir recibir salir seguir subir vivir""".split()

# Irregular preterites the book licenses, BY LEMMA, 1sg and 3sg only (contract story 09).
PRET_IRREGULAR = {
    "fui": "ser/ir", "fue": "ser/ir",
    "tuve": "tener", "tuvo": "tener",
    "dije": "decir", "dijo": "decir",
    "hice": "hacer", "hizo": "hacer",
    "estuve": "estar", "estuvo": "estar",
    "pude": "poder", "pudo": "poder",
    "vine": "venir", "vino": "venir",
    "quise": "querer", "quiso": "querer",
}
# Irregular preterites NOT licensed anywhere — these have appeared in drafts before.
PRET_IRREGULAR_UNLICENSED = {"vi": "ver", "vio": "ver", "di": "dar", "dio": "dar",
                             "supe": "saber", "supo": "saber", "puse": "poner", "puso": "poner",
                             "leyó": "leer", "leyeron": "leer"}

IRREGULAR_PRESENT = {
    "tengo", "tienes", "tiene", "tenemos", "tienen",
    "digo", "dices", "dice", "decimos", "dicen",
    "hago", "haces", "hace", "hacemos", "hacen",
    "pongo", "pones", "pone", "ponemos", "ponen",
    "puedo", "puedes", "puede", "podemos", "pueden",
    "quiero", "quieres", "quiere", "queremos", "quieren",
    "sabes", "sabe", "sabemos", "saben",
    "vengo", "vienes", "viene", "venimos", "vienen",
    "salgo", "sales", "sale", "salimos", "salen",
    "vuelvo", "vuelves", "vuelve", "volvemos", "vuelven",
    "cierro", "cierras", "cierra", "cerramos", "cierran",
    "conozco", "conoces", "conoce", "conocemos", "conocen",
    "pienso", "piensas", "piensa", "pensamos", "piensan",
    "duermo", "duermes", "duerme", "dormimos", "duermen",
    "pido", "pides", "pide", "pedimos", "piden",
    "entiendo", "entiendes", "entiende", "entienden",
    "sigo", "sigues", "sigue", "siguen",
}

REFLEXIVE_LEMMAS = {"sentarse", "levantarse", "acostarse", "irse", "moverse", "llamarse"}
REFLEXIVE_FORMS = {
    "sentarse", "sientas", "sienta", "sientan",
    "levantarse", "levanto", "levantas", "levanta", "levantan",
    "acostarse", "acuesto", "acuestas", "acuesta", "acuestan",
}

GUSTAR_VERBS = {"gusta", "gustan", "encanta", "encantan", "molesta", "molestan",
                "importa", "importan", "parece", "parecen"}

CLITICS_3P = {"lo", "la", "los", "las", "le", "les"}

# Accented = interrogative. Their unaccented twins (`que`, `cuando`, `como`, `donde`) are
# relatives and subordinators, a different construct that the ladder does not sequence.
INTERROGATIVES = {"qué", "quién", "quiénes", "dónde", "adónde", "cómo",
                  "cuánto", "cuánta", "cuántos", "cuántas"}


def _regular_forms() -> dict[str, set[str]]:
    """Generate regular paradigms for the declared lemmas.

    Only the categories this checker judges. Present indicative is NOT generated: it is
    allowed everywhere from story 01, so a hit would carry no information.
    """
    pret, imperf, subj, imper, ger = set(), set(), set(), set(), set() # type: ignore
    for v in AR:
        s = v[:-2]
        pret |= {s + e for e in ("é", "aste", "ó", "aron")} # type: ignore
        imperf |= {s + e for e in ("aba", "abas", "ábamos", "aban")} # type: ignore
        subj |= {s + e for e in ("e", "es", "emos", "en")} # type: ignore
        imper |= {s + e for e in ("e", "en")}       # type: ignore # usted / ustedes only — see below
        ger.add(s + "ando") # type: ignore
    for v in ER + IR:
        s = v[:-2]
        pret |= {s + e for e in ("í", "iste", "ió", "ieron")} # type: ignore
        imperf |= {s + e for e in ("ía", "ías", "íamos", "ían")} # type: ignore
        subj |= {s + e for e in ("a", "as", "amos", "an")} # type: ignore
        imper |= {s + e for e in ("a", "an")} # type: ignore
        ger.add(s + "iendo") # type: ignore
    return {"preterite_regular": pret, "imperfect": imperf,
            "subjunctive": subj, "imperative": imper, "gerundio": ger}


REG = _regular_forms()
# `leer` is regular in 1sg/2sg (`leí`, `leíste`) but y-shifts in 3sg/3pl
# (`leyó`, `leyeron`). Do not silently accept generated non-forms `leió`/`leieron`.
REG["preterite_regular"] -= {"leió", "leieron"}

# Irregular imperfects — Spanish has only three, so this set is complete, not a sample.
REG["imperfect"] |= {"era", "eras", "éramos", "eran", "iba", "ibas", "íbamos", "iban",
                     "veía", "veías", "veíamos", "veían", "estaba", "estabas", "estábamos", "estaban"}
REG["gerundio"] |= {"diciendo", "haciendo", "poniendo", "pudiendo", "viniendo", "yendo",
                    "durmiendo", "pidiendo", "siguiendo", "moviendo", "leyendo", "cayendo"}

# PRECISION over recall: a gate that fails a build must not cry wolf.
#   - regular -ar tú-imperative is identical to 3sg present (`mira`, `habla`)
#   - -er/-ir subjunctive is identical to 3sg present of an -ar verb
# So `imperative` is trusted only for USTED forms, which are unambiguous here, and any
# form claimed by both categories is dropped from `subjunctive`.
REG["subjunctive"] -= REG["imperative"]
# 1sg/1pl preterite of -ar and -ir verbs is homographic with the present (`hablamos`,
# `vivimos`, `miro`/`miró` differ only by accent). Those persons are simply not generated
# above; `--story` sequencing would otherwise fire on ordinary present-tense narration.

TOKEN_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")


def normalize(word: str) -> str:
    w = unicodedata.normalize("NFD", word.lower())
    return "".join(c for c in w if unicodedata.category(c) != "Mn")


def tokens(text: str) -> list[str]:
    return [m.group().lower() for m in TOKEN_RE.finditer(text)]


def find_constructs(text: str) -> dict[str, list[str]]:
    """Return construct -> evidence strings."""
    hits: dict[str, list[str]] = {}

    def add(k: str, ev: str) -> None:
        hits.setdefault(k, [])
        if ev not in hits[k]:
            hits[k].append(ev)

    toks = tokens(text)
    low = text.lower()

    for i, t in enumerate(toks):
        nxt = toks[i + 1] if i + 1 < len(toks) else ""
        nxt2 = toks[i + 2] if i + 2 < len(toks) else ""

        # --- multi-token patterns ---
        # gustar: the CLITIC is what raises the level, not the verb.
        if nxt in GUSTAR_VERBS and t in {"me", "te", "le", "les", "nos"}:
            add("gustar", f"{t} {nxt}")
        # ir a + infinitive (future value)
        if t in {"voy", "vas", "va", "vamos", "van"} and nxt == "a" \
                and nxt2.endswith(("ar", "er", "ir")):
            add("ir_a_infinitive", f"{t} a {nxt2}")
        # estar + gerundio
        if t in {"estoy", "estas", "está", "estamos", "estan", "están"} and nxt in REG["gerundio"]:
            add("estar_gerundio", f"{t} {nxt}")
        # proclitic 3rd-person object pronoun before a known finite verb form
        if t in CLITICS_3P and nxt and nxt not in GUSTAR_VERBS:
            if nxt in IRREGULAR_PRESENT or nxt in REG["preterite_regular"] or nxt in PRET_IRREGULAR:
                add("clitic_object_3p", f"{t} {nxt}")

        # --- single tokens ---
        if t in IRREGULAR_PRESENT:
            add("pres_irregular", t)
        if t in PRET_IRREGULAR:
            add("preterite_irregular", f"{t} ({PRET_IRREGULAR[t]})")
        if t in PRET_IRREGULAR_UNLICENSED:
            add("preterite_unlicensed", f"{t} ({PRET_IRREGULAR_UNLICENSED[t]})")
        if t in REG["preterite_regular"]:
            add("preterite_regular", t)
        if t in REG["imperfect"]:
            add("imperfect", t)
        if t in REG["imperative"]:
            add("imperative", t)
        elif t in REG["subjunctive"]:
            add("subjunctive", t)
        if t in REFLEXIVE_FORMS or t in REFLEXIVE_LEMMAS:
            add("reflexive_basic", t)
        if t == "mientras":
            add("mientras", t)
        # Spanish marks the interrogative/subordinator split ORTHOGRAPHICALLY, so the accent
        # is the signal — not a "does this file contain a ?" heuristic, which cannot tell
        # `cuando Ana vuelve` (subordinator, story 01) from `¿desde cuándo?` (a question).
        if t == "cuándo":
            add("cuando", t)
        if t in INTERROGATIVES:
            add("interrogative_basic", t)

    # enclitic object pronoun on an infinitive: dejarla, verlo, decirle
    for m in re.finditer(r"\b([a-záéíóúñ]+(?:ar|er|ir))(lo|la|los|las|le|les)\b", low):
        add("clitic_object_3p", m.group(0))

    # comparative
    for m in re.finditer(r"\bm[áa]s\b[^.!?]{1,40}?\bque\b", low):
        add("comparative", m.group(0).strip())

    return hits


def check(text: str, story: int) -> tuple[list[str], list[str], list[str]]:
    """Return (failures, notes, house_decisions)."""
    hits = find_constructs(text)
    failures, notes, house = [], [], []

    for construct, evidence in sorted(hits.items()):
        ev = ", ".join(evidence[:4]) + (" …" if len(evidence) > 4 else "")
        if construct in BANNED:
            failures.append(f"BANNED {construct}: {ev}  — {BANNED[construct]}") # type: ignore
        elif construct == "preterite_unlicensed":
            failures.append(f"UNLICENSED irregular preterite: {ev} " # type: ignore
                            f"— not in the story-09 lemma list")
        elif construct in MIN_STORY:
            need = MIN_STORY[construct]
            if story < need:
                failures.append(f"EARLY {construct}: {ev} — introduced in story {need:02d}, " # type: ignore # type: ignore
                                f"this is story {story:02d}")
            else:
                notes.append(f"{construct}: {ev}") # type: ignore
            if construct in UNLEVELLED:
                house.append(f"{construct}: {UNLEVELLED[construct]}") # type: ignore
        else:
            notes.append(f"{construct}: {ev}") # type: ignore

    return failures, notes, house # type: ignore


def inventory_guard(text: str, inventory: set[str]) -> list[str]:
    """Any token not in the frozen inventory needs classifying.

    The anti-rot mechanism, deliberately dumb: it does not claim to know what is a verb,
    only to notice that something changed. Because it cannot be fooled by morphology, it
    is the part of this script least likely to quietly stop working.
    """
    return sorted({t for t in tokens(text) if normalize(t) not in inventory})


def selfcheck() -> None:
    # the two real misses that motivated this script
    f, _, _ = check("Escriba tres cosas.", 3)
    assert any("imperative" in x for x in f), f
    f, _, _ = check("Le gusta estar sola.", 1)
    assert any("gustar" in x and "EARLY" in x for x in f), f

    # in level once its story arrives
    f, _, _ = check("A Ana le gusta el mar.", 6)
    assert not f, f

    # banned everywhere, even in the last story
    f, _, _ = check("Ana era joven.", 10)
    assert any("imperfect" in x for x in f), f
    f, _, _ = check("¿Dónde estaba la carta?", 2)
    assert any("imperfect" in x and "estaba" in x for x in f), f

    # sequencing both ways
    f, _, _ = check("Mañana va a llegar el barco.", 2)
    assert any("ir_a_infinitive" in x for x in f), f
    f, _, _ = check("Mañana va a llegar el barco.", 5)
    assert not f, f

    # licensed vs unlicensed irregular preterite
    f, _, _ = check("Beto dijo la verdad.", 9)
    assert not f, f
    f, _, _ = check("Ana vio la luz.", 10)
    assert any("UNLICENSED" in x for x in f), f
    f, _, _ = check("Rosa leyó la lista.", 8)
    assert any("UNLICENSED" in x and "leer" in x for x in f), f

    # ordinary present-tense narration must stay quiet, or the gate is useless
    f, _, _ = check("Ana mira el mar. Beto toma su café y habla con ella.", 1)
    assert not f, f
    # `desaparecer` is -er, not -ar. Misfiling it once made `desaparece` (3sg present) read
    # as an usted imperative and fail story 07.
    f, _, _ = check("El ruido desaparece.", 7)
    assert not f, f

    # the accent carries the construct: subordinator vs question word
    f, _, _ = check("Cuando Ana vuelve, hay una carta.", 1)   # subordinator — not on the ladder
    assert not f, f
    f, _, _ = check("¿Desde cuándo trabaja aquí?", 1)          # question — introduced at story 02
    assert any("cuando" in x and "EARLY" in x for x in f), f

    # THE CEILING: real defects this script cannot see. If a future change makes either of
    # these fail, the docstring above has become a lie and must be rewritten.
    f, _, _ = check("Antes es de él.", 3)
    assert not f, "temporal misuse is NOT detectable by a form checker — see the docstring"
    f, _, _ = check("Mañana viene el barco.", 3)
    assert not f, "future-value present is NOT detectable by a form checker"

    print("selfcheck ok")


def main() -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    ap.add_argument("--text", help="chapter file, or a glob")
    ap.add_argument("--story", type=int, help="story number this text must satisfy")
    ap.add_argument("--inventory", help="frozen token inventory to guard against drift")
    ap.add_argument("--write-inventory", help="regenerate the inventory from --text and exit")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args()

    if args.selfcheck:
        selfcheck()
        return 0

    if not args.text:
        ap.error("--text is required")
    paths = sorted(glob.glob(args.text))
    if not paths:
        ap.error(f"no files matched {args.text!r}")

    if args.write_inventory:
        toks: set[str] = set()
        for p in paths:
            with open(p, encoding="utf-8") as fh:
                toks |= {normalize(t) for t in tokens(fh.read())}
        with open(args.write_inventory, "w", encoding="utf-8") as fh:
            fh.write("\n".join(sorted(toks)) + "\n")
        print(f"wrote {len(toks)} tokens to {args.write_inventory}")
        return 0

    if args.story is None:
        ap.error("--story is required (the ladder is per-story)")

    inventory: set[str] = set()
    if args.inventory:
        with open(args.inventory, encoding="utf-8") as fh:
            inventory = {line.strip() for line in fh if line.strip()}

    rc = 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        failures, notes, house = check(text, args.story)
        if inventory:
            unknown = inventory_guard(text, inventory)
            if unknown:
                failures.append("tokens not in the frozen inventory, classify them: "
                                + ", ".join(unknown[:12]))
        print(f"\n=== {p}  (story {args.story:02d}) ===")
        for n in notes:
            print(f"  ok    {n}")
        for h in house:
            print(f"  HOUSE {h}")
        for f in failures:
            print(f"  FAIL  {f}")
        print("  PASS" if not failures else "  FAIL")
        rc |= 1 if failures else 0

    print("\nNOTE: lint, not certification. Checks forms and patterns; cannot see temporal "
          "misuse (`Antes es de él`) or future-value present (`mañana viene`).")
    return rc


if __name__ == "__main__":
    sys.exit(main())
