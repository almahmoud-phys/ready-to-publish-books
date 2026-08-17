# Wordlist provenance — read before trusting any coverage number

## Active list

`wordlist-es-opensubtitles-top2000.txt` — 2,000 surface forms.

- **Source:** [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords),
  `content/2018/es/es_50k.txt`, derived from the OpenSubtitles corpus.
- **License:** MIT (© 2016 Hermit Dave). Commercial use permitted. Attribution belongs in the
  book's back matter.
- **Derivation:** `tooling/scripts/build_wordlist.py --top 2000`. Lowercase Spanish alphabetic
  tokens only (drops the proper-noun tail, digits and crawl artifacts), ranked by frequency,
  ties broken alphabetically so the file is reproducible.

## Why this source and not the other one

Codex recommended OpenSLR SLR21 (CC BY-SA 3.0). It is properly licensed, and it was tested — but
it is a **news/web crawl**, and the register is wrong for fiction. Measured against the same
240-word sample story:

| Corpus | top-1000 | top-2000 | top-3000 | top-5000 |
|---|---:|---:|---:|---:|
| OpenSLR SLR21 (news) | 0.707 | 0.799 | — | 0.904 |
| OpenSubtitles (spoken) | 0.895 | **0.971** | 0.987 | — |

The news list's top-2000 is `crisis, guerra, mercado, muertos, proceso, miembros`. It does not
contain `ventana`, `silla`, `mira`, `vieja`, `cansada` — the basic furniture of a story. Even at
rank 5000 it never reaches threshold. **Register mattered more than list size.**

## The honest caveat, which must not be dropped

This is a **frequency proxy, not a CEFR A1 list.** High frequency correlates with early
acquisition; it does not certify a level. The charter already forbids claiming CEFR
certification, and nothing here changes that. A genuinely A1-graded list (ELELex) exists but is
noncommercially licensed and unusable without separate permission.

Subtitle register also skews conversational — good for dialogue, thin on descriptive prose.
Expect narration to need a slightly larger cutoff than dialogue.

## Superseded

`wordlist-a1-provisional.txt` was agent-assembled, 435 forms, no source, no license. It scored
the sample story at 0.979 — but that number was **inflated**, because the list was built around
that story and then had its exact missing inflections added. Grading your own homework. It is
retained only as a historical record of that error and MUST NOT be used for any coverage claim.
