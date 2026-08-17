# Stage 6 keyword and category evidence

**Collected:** 2026-08-14  
**Scope:** Candidate marketplace metadata for *The Letter at Puerto Lento*. This is not search-volume research: autocomplete, result counts, category ranks, and BSR are different proxies and are kept separate below.

## Rules verified against current KDP guidance

Sources accessed 2026-08-14:

- [Make Your Book More Discoverable with Keywords](https://kdp.amazon.com/en_US/help/topic/G201298500): KDP allows up to seven keywords or short phrases; recommends reader language, live suggestion/result checks, and accurate setting/character/plot/tone descriptors; advises against repeating information already in metadata or categories, competitor names, brands, promotions, Amazon program names, and misleading terms.
- [Metadata Guidelines for Books](https://kdp.amazon.com/en_US/help/topic/G201953870): keywords must accurately describe the central content; title/subtitle together must be under 200 characters and match the cover; categories must be relevant.
- [KDP Categories](https://kdp.amazon.com/en_US/help/topic/G200652170): up to three categories may be selected, but relevance takes priority; availability varies by format, marketplace, and time.

## Local demand evidence

### Observed buyer-language signals

| Observed phrase | Evidence | Use decision |
|---|---|---|
| `spanish stories a2` | `research/niche-ledger.csv`; interpreted in `research/niche.md:60-69,85-91` | Strong level/format signal, but already represented by the T1 subtitle. Do not spend a keyword slot repeating it. |
| `spanish stories easy` | `research/niche-ledger.csv`; clean `spanish stories` seed summarized in `research/evidence.yaml` | Relevant but broad; `easy` may underspecify the evidence-backed A2 level. Not selected. |
| `spanish stories for intermediate` | Same sources | Relevant reading intent, but `intermediate` risks overstating A2. Not selected. |
| `spanish stories for learners` | Same sources | Relevant, but `stories` and `learners` are already in the subtitle. Not selected. |
| `learn spanish for adult beginners` / `spanish for beginners adult` | `research/niche-ledger.csv`; persona in `research/niche.md:24-33` | Adult self-study intent is real, but T1 already contains Spanish/adult/learners and the product explicitly excludes absolute beginners. Not selected. |
| `spanish reading and comprehension` | `research/niche-ledger.csv`; `research/evidence.yaml` | Relevant to the exercise blocks, but `reader` is already in the subtitle and the KDP description already names comprehension prompts. Not selected. |
| `spanish stories with english translation` | `research/niche.md:85-91` | Strong feature request but prohibited now: `PIPE-001` has no translation owner or verification method. Excluded from metadata until that changes. |
| `spanish short stories for beginners with audio` | `research/niche-ledger.csv`; audio boundary in `research/niche.md:128-136` | Excluded because no audio exists. |

### Noise and prohibited uses

- About 12 of 63 autocomplete rows describe the adult self-study reader; classroom supplies, children, workbooks, cards, and decor dominate the `spanish reading` seed (`research/niche.md:85-91`).
- Competitor/author navigation terms are not open-category intent and are prohibited metadata.
- Amazon result counts in `research/niche.md:60-69` measure competition, not demand. The `1,000` head-term value is a display cap.
- Google Trends in `research/niche.md:51-53` measures broad attention, not purchases or keyword-level volume.
- The demand case rests primarily on two verified sub-50k Kindle competitors and category-rank evidence (`research/niche.md:35-46,75-78`), not on fabricated search-volume claims.

## Recommended seven slots for T1

Candidate metadata being tested:

- **Title:** *The Letter at Puerto Lento*
- **Subtitle:** *10 Linked Spanish Stories for Adult Learners (A2 Graded Reader)*

The slots add accurate tone, character, plot, setting, theme, and audience descriptors not stated in the candidate title/subtitle or used as feature bullets in the KDP description. They are not claimed as observed search phrases.

| Slot | Phrase | Evidence class | Basis and boundary |
|---:|---|---|---|
| 1 | `quiet suspense` | Untested tone descriptor | The linked mystery is restrained rather than action-driven (`outline/outline.md:35-40,60-79`). |
| 2 | `female protagonist` | Untested character descriptor | Ana is the viewpoint and decision-making lead (`bible/cast.md`; `outline/outline.md:60-79`). |
| 3 | `reluctant witnesses` | Untested character/plot descriptor | Residents evade Ana's questions while revealing pieces of the past (`outline/outline.md:68-79`). |
| 4 | `community secrets` | Untested plot descriptor | The plot concerns what Puerto Lento will and will not say about Tomás and the letters (`outline/outline.md:68-79`). |
| 5 | `harbor night setting` | Untested setting descriptor | Ana works nights in a coastal harbor town and the recurring light is central (`outline/outline.md:60-79`). |
| 6 | `family separation` | Untested theme descriptor | Tomás's long absence and its effects on Lucía, Rosa, and the town drive the emotional history (`outline/outline.md:68-79`). |
| 7 | `post beginner fiction` | Untested audience/form descriptor | The A2 starting state assumes prior beginner study and excludes absolute beginners (`research/niche.md:24-33`; `edits/fact-report.md:F-001`). |

### Slot checks

- Exactly seven phrases.
- No title/subtitle words are repeated: `the`, `letter`, `at`, `Puerto`, `Lento`, `10`, `linked`, `Spanish`, `stories`, `for`, `adult`, `learners`, `A2`, `graded`, `reader`.
- The selected phrases add tone, character, plot, setting, and audience information rather than restating the KDP description's feature bullets. If the final description changes, rerun this comparison against the complete marketplace metadata.
- No stem is intentionally repeated across the seven slots.
- No competitor name, author, trademark, promotion, `free`, `bestseller`, KDP/KU term, audio, translation, certification, or guaranteed outcome appears.
- None of the selected slots is claimed as observed or high-volume buyer language. They are accurate KDP-permitted descriptors chosen after the observed phrases were either already present in title/subtitle or prohibited by missing translation/audio features.

## Category recommendation

1. **Spanish Language Instruction** — supported and measured. The Stage-0 snapshot placed its rank-20 book at overall BSR `#116,747` (`research/niche.md:75-78`). Confirm the current ebook and print path during KDP setup.
2. **Fiction → Short Stories (Single Author), or the closest current equivalent** — content-accurate but conditionally named. Competitive difficulty was not measured for this shelf, and KDP paths vary by marketplace and format. Confirm the exact current path during setup.

### Rejected category

**Foreign Language Phrasebooks** is rejected. Its Stage-0 rank-20 benchmark was measurable, but a phrasebook is a different product from ten linked stories. KDP’s current guidance prioritizes accurate categorization over an easier rank threshold.

## Could not verify

- No direct search volume exists for any proposed phrase.
- Autocomplete was collected on 2026-08-12 and was not re-harvested in this pass.
- Exact category-picker paths cannot be confirmed outside an account-specific KDP title setup and may differ between ebook and print.
- T1 is not a selected final mark. It still needs human selection, a final title/subtitle/pen-name/series/imprint screen, and owner sign-off.
- English translation remains the strongest unavailable feature phrase and stays excluded while `PIPE-001` is open.
