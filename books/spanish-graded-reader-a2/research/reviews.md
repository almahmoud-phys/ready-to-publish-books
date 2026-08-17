# Differentiation review evidence (1–3 star)

Paste raw 1–3 star review text here, with source URLs, grouped by comp ASIN, so a
differentiation contract can be derived from negative signals only.

## ASIN:

- source: <url>
- source: <url>
- "review snippet..."

Bulk review scraping is banned (ADR-008 tier 3). This file is filled by hand.

# Critical review evidence — collected 2026-08-12

Amazon caps review display ("We're showing a limited selection of reviews") even when logged in,
so the 1-3 star sample is NOT obtainable there. Owner attempted and was blocked on all three comps.
Collected from Goodreads instead — public pages, low volume, no scraping tooling. Same fallback the
SQL and AI-agent passes used.

LIMITATION, stated up front: Goodreads hides individual star values on the displayed reviews and
merges editions. These are attributable, dated CRITICAL OBSERVATIONS, not verified 1-3 star reviews.
Moderate-confidence differentiation evidence. Do not describe it as a star-mapped sample.

## Short Stories in Spanish for Beginners — Olly Richards (trade incumbent)
https://www.goodreads.com/book/show/42175803-short-stories-in-spanish-for-beginners
Amazon: #50,969 Kindle, 4.4/802, histogram 66/21/9/2/2 (13% at 3-star or below)

| Reviewer | Date | Critical observation |
|---|---|---|
| Mikael | 2021-10-05 | "It's painfully obvious that the author is not a writer. The stories are dull and lack imagination. Thus, 'Learn Spanish the fun way' is most definitely an overstatement." Explicitly PRAISES the scaffolding: summaries, highlighted difficult vocabulary, in-context translation. |
| Shawn | 2019-08-05 | "Solamente problema es las historias fueran escriben en espanol de Espana. En el Estados Unidos mas los hispanicos de Mexico o Centro America." LOCALE MISMATCH: peninsular Spanish sold to a US market whose exposure is Latin American. |
| Ramona Mead | 2019-10-19 | "The big downside is the stories are silly and not as enjoyable as I'd hoped. They definitely feel like they're out of a kid's early reader, and this feels like a text book. I was looking for a more casual read." |
| soph | 2019-08-01 | "I found the stories hard to get through simply because for me they were awful and a little ridiculous in places. There were also a couple of ERRORS in there which won't really help your learning." |

## Convergent reading

Four independent reviewers, three distinct and repeated failures, and they are NOT about the
teaching method -- the method is praised. They are about the PROSE and the PRODUCTION:

1. **The stories are bad.** Dull, silly, childish, "author is not a writer", reads like a textbook.
   Three of four reviewers. This is the dominant complaint on the category's trade incumbent.
2. **Wrong locale for the buyer.** Peninsular Spanish sold into a US market whose real-world
   exposure is Mexican/Central American.
3. **Errors in the text.** Uncaught mistakes in a product whose entire value is being correct.

Strategic note: complaint 1 is the incumbent's structural weakness -- a language teacher writing
fiction. It is also the single thing a language model is genuinely good at. Complaints 2 and 3 are
not judgement calls at all; they are mechanically checkable, and the check suite already covers the
locale half (tooling/scripts/graded_reader_check.py).

## Not yet collected

- B0FGKLXLGN and B0BCKHC9VR: Goodreads pages not yet pulled. The Amazon-side histograms
  (90/8/2/0/0 and 79/11/8) show criticism exists for the second; it is simply not displayed.
- No sample yet reaches the skill's stricter "20 verified one-to-three-star reviews" bar.
