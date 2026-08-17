# GTM series architecture decision

**Decision date:** 2026-08-14  
**Owner:** Mouhamad  
**Status:** adopted for the first KDP launch  
**Applies to:** reader-facing title, subtitle, cover, KDP series field, description, and launch roadmap

## Decision

Launch *The Letter at Puerto Lento* as a **standalone A2 entry point**, not as a visibly numbered volume and not as one installment of an implied complete A1–B1 curriculum.

Reader-facing launch identity:

- **Title:** *The Letter at Puerto Lento*
- **Subtitle:** *10 Linked Spanish Stories for Adult Learners (A2 Graded Reader)*
- **Level signal:** `A2 Spanish Graded Reader`
- **Volume/book number:** none on the cover, title, subtitle, or KDP description
- **KDP series field at initial setup:** `none`
- **Prospective umbrella name:** `Puerto Lento Spanish Readers`, reserved as a strategy candidate only; it is not approved marketplace metadata and must be screened before use.

The internal description of this manuscript as “Volume 1” may remain in historical, architectural, audit, and production records. It describes the intended catalog role and narrative scope; it must not leak into launch metadata or imply that other levels already exist.

## Rationale

1. The validated reader is an adult who has completed a beginner app or course, not an absolute beginner (`research/niche.md:24-33`). A2 is therefore the deliberate market-entry wedge, not a missing second rung.
2. The shelf evidence supports a series business model because unit prices are low, but it does not support pretending that a catalog already exists (`research/niche.md:55-56`).
3. Displaying both `A2` and `Volume 1` would create avoidable ambiguity: buyers could infer an unavailable A1 predecessor, an already-built B1 continuation, or a required reading order.
4. The narrative-first T1 title and category-first C1 cover can communicate story identity and level without numbering.
5. KDP series metadata can be added later after a second product is credible; launch does not need “series theater” to preserve future optionality.

## Launch positioning

Primary promise:

> You finished the beginner app. Now finish an actual Spanish story.

The KDP description must sell the reading experience rather than explain internal catalog architecture. Do not mention the absence of an earlier Puerto Lento book, the empty launch-series field, or the evidence-gated roadmap in customer-facing copy. The human explicitly rejected that framing on 2026-08-14; the locked description in `exports/blurbs.md` carries the standalone value proposition through audience and story positioning instead.

## Product-line sequence

The default roadmap is evidence-gated:

1. Launch this standalone A2 reader and observe market behavior.
2. If readers want more at the same level, default to a second standalone A2 reader in Puerto Lento for audience and setting continuity.
3. If two validated Puerto Lento books establish a real line, screen and consider the non-sequential umbrella `Puerto Lento Spanish Readers`; KDP series metadata may be added later.
4. Future Spanish graded readers do not all have to remain in Puerto Lento. Expand to another setting only when that concept passes its own niche, quality, and mark gates.
5. If readers demonstrate progression demand, consider a B1 Puerto Lento reader.
6. Produce an A1 product only if reviews, search evidence, or sales data show demand from a distinct lower-level audience.

No future volume is committed by this decision. Book 2 must pass its own niche and investment gate.

## Metadata and cover consequences

- Do not add `Volume 1`, `Book 1`, `Level 2`, or `A1–A2` to reader-facing metadata.
- Do not create or populate the KDP series field for the initial launch.
- Do not put a volume badge on Concept 1.
- Keep `A2 Spanish Graded Reader` prominent for category recognition.
- If a real series is established later, prefer the non-sequential endorsement `A Puerto Lento Spanish Reader` over a front-cover book number.
- `Puerto Lento Spanish Readers` requires a dated final-mark screen and human sign-off before use.

## Revisit gate

Revisit this decision only after one of these observable events:

- a second Puerto Lento book passes niche validation and enters production;
- launch reviews repeatedly ask for A1, another A2 volume, or B1 progression;
- marketplace/search evidence materially changes the target audience;
- KDP series configuration creates a demonstrated discoverability advantage worth the implied catalog commitment.

Until then, the launch remains standalone and unnumbered.
