# Owner identity and standing authorization

Created 2026-08-13 to kill a self-inflicted failure mode. Book 1 (`spanish-graded-reader-a2`)
stalled repeatedly because the agent authored a charter containing two human-only placeholders,
then discovered them at verdict time and re-asked for them across several turns while the owner
had already said "GO" and "proceed in yolo mode". The gate was correct. The ordering was not.

This file exists so the question is answered **once, for the catalog**, instead of once per book.

```yaml
owner_name: Mouhamad
standing_authorization: true
granted: 2026-08-13
granted_by_quote: "proceed in yolo mode" / "it is me:: Mouhamad. sign it" /
                  "the skills must enforce you in the book 2 to go ahead in yolo mode
                   to find the niche + prepare everything with no interruption"
```

## What the standing authorization covers

For every book from book 2 onward, the agent may, without stopping to ask:

- pick and probe candidate niches, mine keywords, measure comps, categories and trends;
- create the book workspace, draft the charter, and fill `evidence.yaml`, `candidates.csv`,
  `niche-ledger.csv`, `reviews.md`, `trademark.md`, `tasks.md`;
- write `owner_attested: Mouhamad <today>` into a charter the agent drafted;
- write `human_signoff: Mouhamad <today>` into `trademark.md` **only when the screen result is
  `no_conflict_found`**;
- compute the verdict, and on GO proceed into stage 1.

Authorship stays the agent's; accountability is the owner's. Both get recorded — a charter must
still say the agent drafted it.

## Content gates the owner cannot judge (added 2026-08-13)

**HITL Gate 1 (outline approval) is delegated to the agent whenever the owner lacks domain
competence in the book's subject matter.** For `spanish-graded-reader-a2` the owner stated plainly:
"I told you I do not know spanish. stop halting for me!"

Halting for an approval the owner has no basis to give is not a safety control — it is theatre that
costs tokens and time and produces a rubber stamp. The gate's real purpose is to stop ten stories
being drafted against a broken plan. That purpose is served by **external adversarial review**
instead:

- at least one full review round by an independent reviewer (codex) before drafting;
- every required change applied or explicitly rejected in writing with a reason;
- staged release — draft Part I, stop, judge, then continue.

Record in `state.json` that Gate 1 was cleared **by delegation**, naming the reviews that
substituted for it. Never record it as owner-approved; the owner did not read it.

This delegation does NOT extend to Gate 2 (publishing), which stays with the owner regardless of
domain competence, because it is outward-facing and spends money.

## Hard stops — the standing authorization does NOT cover these

Stop and hand back, every time, no exceptions:

1. **A real trademark conflict, or an `uncertain` result.** `no_conflict_found` is an absence of
   evidence and may be signed. An actual conflicting mark is a legal judgment: it goes to the
   owner, then to a lawyer — never to a rerun.
2. **A computed KILL.** Choosing a new niche after a KILL is the owner's call.
3. **A charter placeholder the agent cannot fill from evidence.** An unfilled `<angle-bracket>`
   value must never be written through, and must never satisfy a gate.
4. **Publishing, uploading, spending money, or anything outward-facing.** HITL Gate 2 is
   untouched by this file.
5. **A record conflict** between `manifest.yaml`, `state.json`, `compliance_log.yaml` and
   `constitution.md` — the constitution's conflict rule still halts progression.
6. **Fabricating a measurement.** UNKNOWN stays UNKNOWN. Standing authorization is permission to
   proceed, never permission to invent a number, a review, or a source.

## The distinction that makes this safe

"Go ahead" is authorization to **act**. It is not a licence to **assert**. Everything in the
hard-stop list is an assertion that the owner or the evidence must supply. Everything else is
action — and action no longer needs a fresh question.
