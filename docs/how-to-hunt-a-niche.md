# How to hunt a niche

A plain-English walkthrough of stage 0 — deciding whether a book is worth writing.

Written for a human, not an agent. The machine-readable contract is
`.agents/skills/niche-research/SKILL.md`; this file explains the same process in words, using
the real numbers from book 1 as worked examples. If the two ever disagree, **the SKILL.md wins**
— it is what actually runs.

---

## The idea in one line

**Find out if buyers exist BEFORE you write. Kill bad ideas in a day, not in three months.**

Writing a book costs weeks. Checking a niche costs an hour. So check first, always.

---

## Step 0 — The one thing only you decide

Before touching a tool: **what have you actually done?**

Not what interests you. What you have *done*. Ran LLM inference in production — real. Never
trained a model — not real. Write both into `books/<slug>/research/charter.md`: what you can
claim, and what you explicitly cannot.

This is your fence. Everything else in the charter can move; this cannot.

Why it matters: the research will happily find you an excellent niche you have no business
writing. The fence is what stops the search from wandering there. It is also the one field no
tool and no agent can fill for you — inventing it would mean inventing your own experience, and
every later stage would then treat the invention as established fact.

---

## Step 1 — Find the words buyers type

People do not search for what your book is *about*. They search using words they already know.

```bash
./tooling/scripts/niche_mine.sh "llm inference" -m us
```

This asks Amazon's own search box what people type after your phrase. About 40 seconds per seed.

| Result | Meaning |
|---|---|
| 15–30 keywords | Good. Real buyers, real language. |
| 1–5 keywords | Thin. Possibly too specific. |
| 0 keywords | Nobody searches this. Your phrase is wrong. |

**Always run a control seed first.** Mine `historical fiction` — it should return about 28. If
it returns 0 as well, Amazon is blocking you and *every* zero you collect is meaningless.

This is the single most important habit in the whole process. An empty result has two completely
different causes — "no demand" and "no data" — and they look identical.

> **Book 1:** `llm cost` = 0. `llm routing` = 0. Control `historical fiction` = 28, so the
> collector was healthy and those phrases really are dead. But the seed `llm` returned 23,
> including `llm inference`, `llm deployment`, `llm quantization`.
> The problem was real. The words were wrong.

### The provenance rule

Every phrase you test must come from somewhere real: the charter, an autocomplete harvest, a
competitor's title, or a line in a customer review. Record it in `research/candidates.csv`
(`candidate, parent_seed, source, evidence_location, relationship_to_problem, authority_fit,
status`) with its source.

Never test a phrase because it sounds plausible. That is exactly how book 1 got named around
`llm cost` — a phrase with zero buyers behind it.

---

## Step 2 — Is it growing or dying?

```bash
.kdp-research/kdp-scout/.venv/bin/trendspyg explore -k "llm inference" --timeframe "today 12-m"
```

Compare the first six months against the last six months.

| Pattern | Meaning |
|---|---|
| Last half higher | Rising. Good. |
| Roughly equal | Flat. Fine if the volume is decent. |
| Last half lower | Declining. Walk away. |
| Near zero all year | The word never caught on. |

Ignore week-to-week wiggles — they are noise. Compare halves.

> **Book 1:** `llm inference` went from 8.1 to 26.5 — rising about 3×. `llmops` sat at 1.2 out
> of 100 for the entire year, so that word never took and we removed it from consideration.

---

## Step 3 — Who is already there?

Search your keyword on Amazon. Look at the top 10 books. For each, record: **sales rank (BSR),
price, review count, and the date of the newest review.**

Sales rank converts roughly to sales:

| BSR | Copies/day |
|---|---|
| 10,000 | 10–20 |
| 50,000 | 3–8 |
| 100,000 | 1–3 |
| 1,000,000+ | approximately zero |

Reviews run about 1–2% of buyers, so 200 reviews suggests 10,000–20,000 copies sold.

**Review dates matter more than review counts.** 200 reviews whose newest is from 2023 is a dead
book. 30 reviews from last month is a live market.

### The three-book test

Name three books that would sit on the shelf beside yours.

- Cannot name three → no market exists.
- All three are major publishers with 500+ reviews → too crowded, go narrower.
- One big anchor plus several small ones → **this is the sweet spot.**

> **Book 1:** LLM Engineer's Handbook has 219 reviews. Around it sit books with 41, 35, 20 and
> 13. One giant, several beatable. A real shelf you can enter.

### Two safety rules while collecting

Product-page and search requests are the risky kind. The wrapper scripts stop themselves on the
first refusal and exit with code 3.

**When that happens, stop for the session.** Do not retry, do not wait ten minutes and try
again, do not use a proxy — even though the tool itself suggests one. Repeated probing is what
turns a temporary refusal into a lasting block, and the publishing account is worth more than
any single data point.

---

## Step 4 — Read the negative reviews

Open the 1–3 star reviews of those competitors. Read about twenty.

You are hunting one sentence: *"I wish this book had…"*

That complaint is your book. It is the only thing you can promise that the shelf does not
already deliver.

Paste them into `research/reviews.md` with their links. From them, write **three promises no
competitor keeps.** Each promise must trace back to a real complaint — not to a good idea you
had in the shower. A promise you invented is one you may not be able to keep.

---

## Step 5 — Decide

Do not decide by feel. Run:

```bash
python3 tooling/scripts/niche_verdict.py <book-slug>
```

It reads `research/evidence.yaml`, checks your claims against the files behind them, and prints
one of four things:

| Verdict | Meaning | What to do |
|---|---|---|
| **GO** | Demand + enterable shelf + real gap + safe name | Start writing |
| **PIVOT** | Buyers exist; your angle is wrong | Change the angle, run again |
| **KILL** | No buyers, or you cannot credibly write it | Drop it — it cost you a day |
| **INCOMPLETE** | Something is not measured yet | Go measure it |

The script will not say GO while any field is `UNKNOWN`, and it will not accept a number that
disagrees with the file behind it. Claim 30 keywords when the ledger holds 2 and it refuses.
That is deliberate: it exists so enthusiasm cannot overrule evidence — including yours.

**PIVOT versus KILL.** PIVOT means the right problem in the wrong words. KILL means the wrong
problem. Book 1 was a PIVOT: the cost problem is real, but "cost" is not what buyers type.

**A missing field never causes a KILL.** "Nobody measured this" is not "there is nothing here."
The script enforces that, and it is the difference between a gate and a shredder.

You may **veto** a GO — your judgement outranks the script. You may **not** promote a PIVOT or
KILL into a GO without new evidence. The ratchet turns one way only.

---

## Step 6 — Check the name is legal

Search your title on Justia Trademarks, Trademarkia and uspto.report. The classes that matter
for books: **9** (ebooks), **16** (print), **41** (publishing services).

The official portals (WIPO, TMview, USPTO search) block automated access, so an agent cannot
read them — but the mirrors above are searchable and carry the full records.

An agent may write `no_conflict_found`, meaning *"I searched N sources and saw nothing."* Only
**you** write `human_signoff: <who> <date>` in `research/trademark.md`, meaning *"I accept
this."* The verdict script requires that line before it will say GO.

A search is not clearance. A real conflict goes to a lawyer, not to another search.

---

## Then you write

Only after a GO:

1. **Outline** — every chapter gets a promise and a word budget. **You approve it.** ← *checkpoint 1*
2. **Style bible** — terms, voice, examples, locked. This is what makes twelve chapters sound like one book.
3. **Chapters** — written one at a time, in parallel. Nobody grades them yet: judging while drafting produces cautious, boring prose.
4. **Attack** — one pass whose only job is to prove the book is bad. Not to improve it. Separating those two jobs is what keeps the criticism honest.
5. **Score** — ten dimensions. **Your book's score is its worst dimension, not the average.** Nine 9s and one 3 is a 3, because that is where readers quit.
6. **Proofread and fact-check** — every checkable claim is verified, rewritten, or cut. Invented numbers die here.
7. **Package** — cover, blurb, keywords, EPUB, print PDF.
8. **Publish** ← *checkpoint 2*

Two places where you are required. Everything else runs itself.

---

## The five rules underneath all of it

1. **Check the instrument before believing it.** A zero means nothing until the control seed proves the tool works.
2. **Research first, write second.** Never write prose to "test" an idea.
3. **Missing is not zero.** Never kill a book over a field nobody measured.
4. **Your worst dimension is your score.** A book is not an average.
5. **Never invent a number.** Stage 5 removes it, and a reader who catches one stops believing all of them.

---

## When you are stuck

| Symptom | Likely cause | Do this |
|---|---|---|
| Every seed returns 0 | Amazon is blocking you | Run the control seed. If it also returns 0, stop for the session. |
| Script exits with code 3 | Refusal detected | Stop all Amazon work for the session. No retry, no proxy. |
| Verdict says INCOMPLETE | Fields still `UNKNOWN` | It prints exactly which. Go and measure those. |
| INCOMPLETE, "claimed X but ledger has Y" | A number does not match its file | Fix the number, not the file. |
| INCOMPLETE, "charter placeholder" | The charter is not filled | Fill it. Nothing runs without a goal. |
| Third PIVOT in a row | The angle is not the problem | Stop. The charter itself may be wrong — that is your call, not the loop's. |
