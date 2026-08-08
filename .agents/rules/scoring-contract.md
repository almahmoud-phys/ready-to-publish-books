# Scoring Contract (harvested from Book Genesis v4, adapted)

> **The four laws**: (1) Draft BEFORE judgment. (2) Adversarial structural audit BEFORE scoring. (3) Every score cites the manuscript — no vibes. (4) **Floor principle**: book score = min(dimensions).

## Dimensions

### Universal (all books)
| Dimension | Question |
|---|---|
| Originality | Does this say something comps don't? Flag passages that could appear in any book on the topic |
| Prose | Sentence-level quality, rhythm, banlist compliance (`.agents/rules/style.md`) |
| Coherence | Do chapters honor outline contracts? Do promises made get kept? |
| Market | Would the target persona pay for this over the top 3 comps? Why? |
| Voice | Consistent, distinctive, matches style sheet |
| Opening | Do the first 3 pages earn page 4? |

### Non-fiction additions (default genre, ADR-001)
| Dimension | Question |
|---|---|
| Accuracy | Every claim verified/cited/experienced — cross-checked with fact-checker flags |
| Usefulness | Can the reader DO something after each chapter they couldn't before? |
| Structure | Information architecture: progression, chunking, reference-ability |

### Fiction additions (deferred until M5+, kept for completeness)
Theme · Characters · Pacing · Emotion

## Scorecard schema (`books/<slug>/scores/scorecard.json`)

```json
{
  "book": "<slug>",
  "timestamp": "<iso8601>",
  "model": "<judge-model-id>",
  "dimensions": {
    "<name>": {
      "score": 7,
      "citations": ["chapters/chapter_02.md:L40-L58 — reason"],
      "weakest_passage": "chapters/chapter_05.md:L12 — why"
    }
  },
  "book_score": 7,
  "floor_dimension": "<name>",
  "loopbacks_used": {"<dimension>": 1},
  "verdict": "PASS | LOOPBACK:<stage> | ESCALATE"
}
```

## Rules for the judge

1. Score **only** complete drafts (post stage 3 audit).
2. Every score < 9 requires ≥ 2 citations. Every score < floor requires a `weakest_passage`.
3. Judge reads: outline contracts, rolling summaries, targeted excerpts. Full read only at final pass (context discipline).
4. Independent judgments: multi-pass scoring with different excerpt seeds; disagreement > 1 point → third pass, take median.
5. Floor default: **7/10** per dimension (change control: `.agents/rules/quality-gates.md`).
