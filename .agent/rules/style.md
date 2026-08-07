# House Style Sheet (defaults — per-book overrides go in bible/style-sheet.md)

## Voice (practitioner non-fiction default)

- Second person ("you") for instruction; first person ("I/we") only for hard-won experience.
- Practitioner-to-practitioner register: direct, concrete, zero fluff. The reader is smart and busy.
- Present tense, active voice. Short paragraphs (≤ 4 sentences). Sentence length varies — rhythm matters.
- Every claim is either: demonstrated (code/steps/example), experienced (first-person anecdote), or cited. Nothing floats.

## Structure conventions

- Chapter = one promise made in the opening paragraph, kept by the end.
- Headings are assertions, not labels ("Cache invalidation kills more launches than traffic" — not "Caching").
- Code/commands in fenced blocks with language tags. Every block must be runnable as written.
- Each chapter ends with: "Try this" (one action) — no summaries that repeat the chapter.

## LLM-tic banlist (proofreader enforces mechanically)

- Words: delve, tapestry, landscape (metaphorical), realm, foster, underscore, pivotal, crucial, embark, journey (metaphorical), navigate (metaphorical), unleash, unlock, elevate, seamless(ly), robust, leverage (as verb, unless literal), utilize, furthermore, moreover.
- Patterns: "It's not X, it's Y" more than once per book; triads of adjectives; "In today's fast-paced world"; rhetorical question openings; em-dash overuse (max 1 per 500 words); "Let that sink in"; "game-changer".
- No filler openers ("In this chapter, we will..."). Start in motion.

## Formatting

- Markdown source, Pandoc-flavored. H1 = chapter, H2 = section, H3 max depth.
- Numbers under 10 spelled out; units with non-breaking space; code identifiers in backticks.
- Figures/tables numbered per chapter (Fig 3.2). Alt text mandatory (accessibility + EPUB validity).

## Readability targets

- Grade level: 8–10 (Hemingway-ish). Jargon allowed only after definition.
- Chapter length: per outline word budget ±10%.
