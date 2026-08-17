# Book Discovery Log

This is the pre-charter discovery inbox. An entry here is a lead, not an approved niche,
title, keyword, or permission to create a book workspace.

## Working agreement

- The owner is learning the market with the agent and will keep searching until the strongest
  defensible niche-and-book combination is found.
- Popularity identifies demand; it does not establish enterability.
- Major authors are ceiling benchmarks. A candidate also needs reachable mid-list/independent
  comps and evidence of an unmet reader need.
- Broad storefront and bestseller observations must be narrowed to a category, subcategory,
  reader promise, and provenance-backed phrase before Stage 0 begins.
- Bestseller pages are volatile and seasonal. Record the observation date and verify live data
  before using a title or rank as evidence.

## Discovery sources

| Added | Source | Role | Status |
|---|---|---|---|
| 2026-08-09 | [Amazon Books store](https://www.amazon.com/amz-books/store?ref=ebooks_dsk_sn_USF_sb&ccs_id=8c21bac5-528e-4338-845a-6781137a8389) | Broad merchandising and category discovery | Input only |
| 2026-08-09 | [Amazon Books Best Sellers](https://www.amazon.com/gp/bestsellers/books?ref=books_dsk_sn_amazon-best-s-c4fd0) | Cross-category demand, seasonality, formats and recurring authors | Input only |
| 2026-08-09 | [Amazon Books discover page](https://www.amazon.com/amz-books/discover?node=6&navStore=books&ref=books_dsk_sn_cookbooks-c6b18) | Category-branch exploration | Input only |
| 2026-08-09 | [Lucy Foley author store](https://www.amazon.com/stores/Lucy-Foley/author/B00LMBVZNC) | Major-author benchmark for closed-circle psychological mystery/thriller | Benchmark only |

## Current findings

- The overall bestseller list mixes fiction, nonfiction, children's books, licensed properties,
  workbooks, gift books and seasonal demand. It is a discovery surface, not a niche.
- Lucy Foley demonstrates demand for atmospheric, limited-suspect, secret-driven mysteries,
  but her publisher support, backlist and audience make her an unsuitable sole comp.
- No fiction or cookbook candidate had passed Stage 0 at this point. `ai-agent-testing` remained an
  incomplete, stopped research candidate and was later retired; its decision record is preserved in
  `research/archive/ai-agent-testing.md`.

## Provenance-backed phrases eligible for discovery probes

These phrases are copied verbatim from observed category paths or current comp titles. Their
presence here permits a bounded discovery probe; it does not approve a book.

| Phrase | Provenance | Why it is eligible | Probe status |
|---|---|---|---|
| `context engineering` | [Manning comp title](https://books.google.com/books/about/Context_Engineering.html?id=Vfcf0gEACAAJ) | Technical discipline with runnable, testable artifacts | Tested: 5 |
| `Model Context Protocol` | [Packt comp title](https://books.google.com/books?id=CNfEEQAAQBAJ) | Open protocol; examples can be reproduced and version-pinned | Tested: 4 |
| `Claude Code` | [KDP comp title](https://books.google.com/books/about/Claude_Code.html?id=etn60QEACAAJ) | Current developer-tool shelf with testable workflows | Tested: 22, noisy |
| `claude code harness engineering` | Amazon autocomplete from `Claude Code`, US, 2026-08-09 | Narrow workflow language; companion repository can test every claim | Tested: 2, thin |
| `Python Testing with pytest` | [Pragmatic Bookshelf comp title](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) | Established specialist shelf; every example can be executed in CI | Retired after thin parent probes |
| `pytest` | [Pragmatic Bookshelf comp title](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) | Verbatim framework name in the approved comp title; parent probe for buyer language | Tested: 1 |
| `Python testing` | [Pragmatic Bookshelf comp title](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) | Verbatim parent phrase from the same comp title; bounded follow-up after thin `pytest` harvest | Tested: 1 |
| `Practical SQL` | [No Starch Press comp title](https://nostarch.com/practical-sql-2nd-edition) | Best-selling evergreen technical shelf; outputs can be reproduced against frozen datasets | Next measured candidate |
| `SQL` | [No Starch Press comp title](https://nostarch.com/practical-sql-2nd-edition) | Verbatim parent term in an observed comp title; shared Trends anchor | Tested: 23; leading family |
| `GitHub Actions` | [Manning comp title](https://www.manning.com/books/github-actions-in-action) | Verbatim platform term in an observed comp title; workflows can run in CI | Trends watchlist |
| `Linux command line` | [No Starch Press comp title](https://nostarch.com/node/820) | Verbatim phrase in an observed comp title; labs can run in containers | Trends parked |
| `software testing` | [Manning comp title](https://www.manning.com/books/software-testing-with-generative-ai) | Verbatim parent phrase in an observed comp title; methods can be exercised against fixed code | Tested: 7; parked thin |
| `AI agents` | [Manning comp title](https://www.manning.com/books/ai-agents-in-action-second-edition) | Verbatim phrase in an observed comp title; broad attention benchmark, not an approved niche | Tested: 17; parked crowded |
| `SQL practice problems` | Amazon autocomplete from `SQL`, US, 2026-08-09 | Strong outcome language; exercises, datasets and answers can be tested automatically | Best candidate; exact comp title occupied |
| `SQL workbook practice` | Amazon autocomplete from `SQL`, US, 2026-08-09 | Substantive workbook format with automatically checkable outputs | Rejected: Trends 0 |
| `SQL tuning` | Amazon autocomplete from `SQL`, US, 2026-08-09 | Performance-oriented branch; technically testable but authority- and engine-sensitive | Rejected for Book 1 despite Trends 21 |
| `SQL certification study guide` | Amazon autocomplete from `SQL`, US, 2026-08-09 | Explicit purchase intent; vendor/exam dependency makes it a feasibility control | Trends unavailable |
| `guided journal` | Titles observed on Amazon Books Best Sellers | Strong gift format but weak Kindle fit and limited prose | Parked |
| `coloring book` | Titles observed on Amazon Books Best Sellers | Image-led/low-content production, outside first-book goal | Parked |
| `Cookbooks, Food & Wine` | Supplied Amazon category route | Requires recipe testing, food safety and original photography | Parked |
| `Mystery, Thriller & Suspense` | Amazon bestseller category path and Lucy Foley shelf | Human-taste validation burden; retain as later fiction research | Parked |

## Funnel for each promising lead

1. Record the observed category, title, author or exact buyer phrase.
2. Find at least three major demand comps and five reachable comps.
3. Check current rank/review velocity, autocomplete language and category rank-20 difficulty.
4. Mine low-star reviews for one repeated unmet need.
5. Only then ask the owner to approve a charter and create a fresh book workspace.

## Discovery run — 2026-08-09

### Instrument and measured phrases

The fresh US `historical fiction` control returned 28 suggestions, confirming collector health.

| Sourced seed | US suggestions | Five-year US Trends average in comparison | Editorial reading |
|---|---:|---:|---|
| `Claude Code` | 22 | 9 | Strongest raw signal, but mixed with merchandise and branded-tool noise. |
| `context engineering` | 5 | 0 | Emerging book language, still below broad public-search resolution. |
| `Model Context Protocol` | 4 | 1 | Real but thin specialist language. |
| `claude code harness engineering` | 2 | Not separately measured | Follow-up collapses to the phrase plus an author-name query; not a broad buyer-language cluster. |
| `Python Testing with pytest` | Not yet probed | 0 | Exact title phrase is too narrow for Trends; durable comp evidence makes `pytest` the next eligible parent probe. |

`Claude Code` reached a relative Trends peak of 100 in the week of 2026-03-29, then fell to
27 in the latest complete week (2026-08-02) on the shared scale. That is strong awareness but
currently declining momentum. A branded book would also carry rapid version decay and
trademark/dependency risk. Decision: do not create or write a Claude Code book from this run.

### Ranked candidate queue

1. **Intermediate SQL challenge workbook** — the completed adjudication below identifies this
   as the best candidate, with a review-derived gap and an executable evidence strategy.
2. **Home Assistant for non-technical households** — large ecosystem and a reachable direct
   shelf; hardware variation and truthful household testing make it less clean than pytest.
3. **Practical Obsidian knowledge system / tool-neutral family photo organization** — highly
   verifiable artifact design, but public demand remains less established.
4. **Context engineering / Model Context Protocol** — watchlist only until buyer language and
   repeated sales strengthen.

### Formats rejected for Book 1

- Psychological thriller: human beta readers are required to validate emotional engagement;
  the current pipeline's fiction scoring additions are deferred.
- Cookbook: recipes, food safety, nutrition claims and photography require real kitchen tests.
- Generic journal/coloring book: low-content/commodity economics and weak editorial moat.
- Medical, legal, financial, children's pedagogy and high-stakes cybersecurity promises:
  authority and harm risks exceed the first-book experiment.

### Current decision

No manuscript is authorized. The completed pytest run below retires that candidate and advances
`Practical SQL` to the next measured discovery pass; the AI-agent and Claude Code ideas do not.

## Discovery run — pytest — 2026-08-09

### Demand measurement

The fresh US control again returned 28 suggestions. `pytest` returned only `pytest` (1), and
the bounded `Python testing` follow-up returned only `python testing with pytest` (1). The exact
`Python Testing with pytest` phrase also rounded to zero in the prior five-year Trends comparison.
The collector was healthy; the buyer-language cluster is genuinely thin.

### Shelf and review evidence

| Comp | Date / size | Public signal | Competitive meaning |
|---|---|---|---|
| [Python Testing with pytest, 2e](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) — Brian Okken | 2022, 272 pp | $28.95 ebook; Goodreads 4.15/5, 59 ratings | Strong trusted incumbent; broad feature guide. |
| [Effective Testing: From Slop to Software](https://store.metasnake.com/testing) — Matt Harrison | 2026, 323 pp | $49 direct; named testimonials, no aggregate rating found | Current direct competitor already covering modern tooling, AI/TDD workflows and pytest. |
| [pytest Quick Start Guide](https://www.packtpub.com/en-us/product/pytest-quick-start-guide-9781789347562?type=print) — Bruno Oliveira | 2018, 160 pp | Packt 3.9/5 (7); Goodreads 4.06/5 (16) | Older but credible core-contributor comp. |

Thirteen attributable critical observations were accessible, but not the required 20 verified
low-star reviews. Repeated needs were test-design strategy (4 observations), advanced
mocking/monkeypatch behavior (3), and reproducible exercises/code transitions (4). Those needs
are real enough to describe a hypothesis, not enough to certify a differentiation contract.

The technical freshness gap is also real: Okken's examples target Python 3.10 and pytest 7,
while pytest 9.1.1 is current. But Harrison's 2026 book already occupies much of the obvious
modern-tooling position, and freshness alone decays too quickly to be a durable promise.

### Editorial decision

**STOP — do not create or write this book.** Content feasibility is excellent, but demand
language is too thin and the credible shelf already owns both the trusted fundamentals and
the modern angle. Publication would additionally require a named Python-testing practitioner
to review design judgment; CI can prove examples run, not that the testing strategy is wise.

`Practical SQL` becomes the next measured candidate.

## Trends-first discovery run — 2026-08-09

### Method

Two US five-year Google Trends comparisons used only provenance-backed phrases from observed
book titles. `SQL` was the shared anchor, so the two batches remain comparable. The first and
last columns below are averages across the first and most recent 52 complete weeks; the partial
current week is excluded. Trends measures general search attention, not book purchases.

| Topic | Five-year shared average | First 52 weeks | Latest 52 weeks | Reading |
|---|---:|---:|---:|---|
| `SQL` | 71 | 78.17 | 58.73 | By far the largest signal, but down about 25%; evergreen candidate, not a growth story. |
| `AI agents` | 4 | 0.00 | 18.40 | Strongest non-branded recent signal; broad and likely crowded, so Amazon must supply the niche. |
| `Claude Code` | 8 | 0.04 | 38.96 | Explosive branded attention, but volatile, dependency-heavy and already rejected on durability grounds. |
| `software testing` | 3 | 1.75 | 6.50 | Smaller but up about 271%; highly writable and testable. |
| `GitHub Actions` | 3 | 1.35 | 5.81 | Smaller but up about 332%; highly testable, with platform-dependency risk. |
| `Model Context Protocol` | 1 | 0.00 | 3.10 | Emerging, still below the current Amazon-validation cutoff. |
| `Linux command line` | 2 | 1.69 | 1.73 | Flat and evergreen; strong incumbent makes it a weak first entry. |
| `Python testing` | 1 | 0.17 | 1.35 | Rising from a tiny base; the completed pytest run already retired it. |
| `context engineering` | 0 | 0.00 | 1.50 | Emerging but below broad-search resolution. |

### Amazon handoff and circuit breaker

The writing-feasibility filter advanced `SQL`, `AI agents`, and `software testing` to the next
Amazon autocomplete batch. `GitHub Actions` remains the first watchlist candidate.

The required `historical fiction` control could not resolve `completion.amazon.com` in the
restricted environment. The wrapper exited 3, appended no cached rows, and triggered the
mandatory circuit breaker. Therefore no candidate Amazon request was made. Collector health is
unconfirmed, and this run makes no Amazon-demand, PIVOT, KILL, or GO claim.

This environment blocker was resolved by the next run below.

## Amazon discovery run — 2026-08-09

### Healthy autocomplete batch

The fresh `historical fiction` control returned 28 suggestions, confirming collector health.

| Seed | Suggestions | Buyer-language reading |
|---|---:|---|
| `SQL` | 23 | Strongest parent. Eighteen rows begin with SQL; useful branches include beginners, certification, Excel, practice problems, Server, tuning and workbook practice. Five `sal` rows plus a few lexical matches are noise. |
| `AI agents` | 17 | Real interest, but much of the harvest navigates to named books, authors or branded platforms. The reusable branches are MCP, design patterns, AWS, Python, RAG and step-by-step. |
| `software testing` | 7 | Thin. The useful branches are managers, pytest, Selenium, techniques and generative AI; the latter already names a strong direct comp. |
| `SQL practice problems` | 2 | The sole follow-up collapsed to the phrase itself and a query for Sylvia Moestl Vasilik's existing book. This is title-navigation, not a new buyer-language cluster. |

### Competition collection

The single low-volume Amazon search-results pass failed to parse all three shelves and exited 3.
The circuit breaker ended Amazon activity; no BSR, result count, category difficulty or live
top-10 verification was obtained. This run therefore cannot produce GO, PIVOT or KILL.

Degraded non-Amazon evidence still distinguishes the candidates:

- [Practical SQL, 2e](https://nostarch.com/practical-sql-2nd-edition) has a substantial,
  established shelf signal; Goodreads reports 4.25/5 from 242 ratings and 30 reviews.
- [SQL Practice Problems](https://www.goodreads.com/book/show/34863243-sql-practice-problems)
  reports 4.11/5 from 80 ratings and 13 reviews and already owns the generic real-world
  learn-by-doing promise.
- [Software Testing with Generative AI](https://www.manning.com/books/software-testing-with-generative-ai)
  is a 304-page 2024 Manning book by an experienced tester, rated 4.4/5 from 10 publisher-site
  reviews. A generic AI-for-testing book would enter behind a strong authority incumbent.
- Manning's current catalog contains numerous AI-agent books, confirming both demand and a
  crowded, fast-moving shelf. The broad AI-agent direction remains unsuitable for Book 1.

Public SQL reviews support only a provisional gap hypothesis: readers ask for more advanced
and common problem-solving patterns, realistic business use cases, and less setup friction.
That is not yet a differentiation contract because fewer than 20 attributable low-star reviews
were collected, and the existing practice-problems incumbent already addresses part of it.

### Recursive Trends check and decision

The Amazon-derived phrases `SQL workbook practice`, `SQL tuning`, and
`SQL certification study guide` were recorded before probing. Both a five-term Trends comparison
and a smaller three-term retry failed because Google Explore did not render its chart. This is
an unavailable measurement, not zero interest.

**Current leader: the SQL practice/workbook family, but still INCOMPLETE.** Do not create a
book workspace. `AI agents` is parked as broad/crowded; `software testing` is parked as thin
and authority-heavy. The next admissible action is to restore the Trends measurement for the
SQL subphrases, then run a new healthy Amazon shelf session and mine a full critical-review set.

## Autonomous candidate adjudication — 2026-08-09

The previously unavailable SQL subphrase comparison succeeded in a visible browser. US,
five-year Google Trends results exclude the partial current week:

| Phrase | Five-year average | First 52 weeks | Latest 52 weeks | Decision |
|---|---:|---:|---:|---|
| `SQL tuning` | 21 | 26.21 | 30.10 | Strong attention, but rejected for Book 1: performance claims depend on engine, statistics, hardware and specialist DBA judgment. |
| `SQL practice problems` | 1 | 0.25 | 4.67 | Small but sharply rising; advances because it also passes buyer-language, shelf, gap and production-feasibility filters. |
| `SQL workbook practice` | 0 | 0.00 | 0.00 | Amazon wording without broader search adoption; reject as keyword language, retain only as a possible internal format description. |

### Review-derived gap

Twenty attributable, dated critical observations were collected across `SQL Cookbook`,
`Learning SQL`, `Practical SQL`, `SQL Practice Problems`, and adjacent direct comps. Goodreads
usually hides each displayed review's individual star value and merges some editions, so this
is moderate-confidence differentiation evidence rather than a fully star-mapped GO sample.

Recurring needs:

1. A credible bridge from syntax basics to genuinely intermediate/advanced work — 8 reviewers.
2. Solutions that explain readability, parsimony, performance and best-practice tradeoffs —
   6 reviewers.
3. A reproducible bundled schema/data environment with immediate exercise feedback — 5 reviewers.
4. Explicit dialect scope instead of unclear or restrictive portability claims — 5 reviewers.

Only one strong review directly requested more realistic business scenarios, so business realism
is a supporting design requirement, not a standalone market claim.

### Nine-comp shelf conclusion

The shelf is established but provisionally enterable. Vasilik owns generic real-world SQL
practice; `Practical SQL` owns real datasets; `SQL Cookbook` owns advanced cross-dialect recipes;
and current Packt titles cover analytics exercises and design patterns. No inspected book combines
solve-first intermediate challenges, frictionless bundled setup, detailed alternative-solution
reasoning, and executable automated checks. Amazon BSR, result counts, review velocity, category
difficulty and live top-10 verification remain UNKNOWN because the search-results collector
triggered the circuit breaker.

### Best candidate

**An intermediate SQL challenge workbook for readers who know basic syntax but cannot yet solve
realistic data requests from scratch.** This is the strongest candidate found in the bounded hunt.
It is a product direction, not a final title; the exact incumbent title `SQL Practice Problems`
must not be copied.

Differentiation contract:

1. Every challenge ships with a visible, bundled schema and deterministic data; one command starts
   the environment and checks the learner's result.
2. Difficulty begins after syntax basics and progresses through genuinely intermediate analytical
   patterns, with adversarial cases for NULLs, duplicates, ties, missing relationships and dates.
3. Each solution explains correctness, readability/maintainability and performance tradeoffs,
   including a simpler or alternative correct query where useful.

Production contract: use one explicitly pinned SQL dialect and engine, likely DuckDB LTS, rather
than claiming false multi-dialect portability. Original synthetic datasets, solutions and prompts
feed an automated grader that compares result sets across adversarial fixtures. A named experienced
SQL/data practitioner must review scenario realism, solutions, edge cases and dialect claims before
publication. `SQL tuning` and certification preparation are excluded.

**Status: BEST CANDIDATE / FORMAL STAGE 0 STILL INCOMPLETE.** The candidate wins the discovery
comparison, but a fresh Amazon shelf pass, human top-10 verification, title-specific trademark
screen, and practitioner-review commitment are still required before a computed GO or workspace.

## Language direction

The catalog is not inherently English-only. English is the Book 1 strategy because the current
evidence is US-English, the style/scoring rules are English-first, and the owner can inspect the
result. A later language requires its own marketplace research and native-language editorial
gate; it is not a mechanical translation. The manifest already has a per-book `language` field,
but Pandoc metadata currently hardcodes `lang: en` and must be parameterized before a
non-English production run.

## Post-SQL pivot lead — data-intensive systems — 2026-08-09

Human-verified Amazon evidence identified *Designing Data-Intensive Applications: The Big Ideas
Behind Reliable, Scalable, and Maintainable Systems*, second edition, by Martin Kleppmann and Chris
Riccomini as a strong parent-market signal:

| Field | Observed value |
|---|---|
| Publisher / date | O'Reilly Media, March 24, 2026 |
| Edition / length | Second edition, 670 pages |
| Paperback price | $56.86 shown; $69.99 list |
| Paperback BSR | #1,864 in Books |
| Category ranks | #1 Data Mining; #1 Data Processing; #1 Data Warehousing (Books) |
| Rating / reviews | 3.6 / 206 |
| ISBN-10 / ISBN-13 | 1098119061 / 978-1098119065 |

This is materially stronger current-demand evidence than the SQL-practice shelf. It proves that
buyers spend money in the broader data-systems market. It does **not** prove that a direct competitor
to this 670-page O'Reilly flagship is enterable. The title has major-publisher distribution,
established authors, a successful first-edition foundation, and #1 placement in three categories.

Exact provenance-backed discovery language available from the page includes:

- `data-intensive applications` — comp title;
- `reliable, scalable, and maintainable systems` — comp subtitle;
- `Data Modeling & Design` — breadcrumb category;
- `Data Mining`, `Data Processing`, `Data Warehousing` — category/bestseller labels;
- `distributed systems`, `data stores`, `data warehouses`, and `data lakes` — listing description.

These may be used as parent seeds for Trends-first discovery. They are not approved book titles or
promises. The next admissible move is to compare their demand direction, then use Amazon
autocomplete to locate a narrower, executable buyer job with reachable comps and repeated review
gaps. A summary, workbook, unofficial companion, or close structural imitation of the O'Reilly book
is prohibited.

This lead is outside the current SQL-workbook charter: it changes the reader problem from solving
SQL requests to designing data systems. If it wins, it requires a fresh charter and workspace after
Stage-0 discovery rather than a cosmetic revival of the retired SQL candidate. Its decision record
is preserved in `research/archive/sql-challenge-workbook.md`.

### Captured parent-shelf audit

Four Amazon PDF captures under `research/` were audited on 2026-08-09. The full evidence inventory
and shelf notes are in `research/README.md`.

- `data modeling`: over 5,000 estimated results; contested, with strong incumbent and tool-specific
  books. Advance only as a parent discovery branch.
- `data warehousing`: over 6,000 estimated Books results; coherent, premium, and incumbent-heavy.
  Retain as the secondary branch.
- `distributed systems`: over 30,000 estimated Books results; generic query saturated and A-list
  heavy. Reject as a direct entry.
- `data modeling for the sciences`: over 5,000 estimated results but no coherent exact shelf; the
  exact title has six visible reviews. Reject as a seed.

The `data modeling` autocomplete screenshot was taken under Amazon **All**, not **Books**. Its
suggestions are allowed provenance leads, but they must be measured in Trends and recaptured under
Books before being treated as book-buyer language.

### Data-systems follow-up seeds — recorded before autocomplete probe

The following exact phrases are eligible for one bounded US Books autocomplete batch. They are
parent discovery terms only, not proposed titles or book promises:

- `dimensional modeling` — title phrase from *The Data Warehouse Toolkit: The Definitive Guide to
  Dimensional Modeling* (Kimball and Ross; Goodreads source recorded in this research pass).
- `data quality` — title phrase from *Practical Data Quality* (Packt) and *Data Quality Techniques*
  (Kogan Page).
- `data contracts` — title phrase from *Data Contracts* (O'Reilly) and *Driving Data Quality with
  Data Contracts* (Andrew Jones).

`data modeling` and `data warehousing` were already recorded above from the Amazon parent shelf.

### Autocomplete evidence — 2026-08-10

A fresh US Books `historical fiction` control returned 27 suggestions, so collector health was
confirmed. `data contracts` returned only two title-navigation suggestions (`data contracts book`
and `data contracts developing production-grade pipelines at scale`); it does not provide a
reusable buyer-language branch.

`data quality` returned five suggestions: `data quality automation`, `data quality book`, `data
quality etl`, `data quality fundamentals`, and `data quality the accuracy dimension`. The first
three are now provenance-backed follow-up candidates. Their next probe is bounded to this batch;
they are not book concepts yet.

The `data quality automation` and `data quality etl` follow-ups each returned only themselves.
Treat both as thin title-navigation signals, not as a market family.

The US Books `data modeling` parent returned nine suggestions: `data modeling and database design`,
`data modeling essentials`, `data modeling in snowflake`, `data modeling kimball`, `data modeling
made simple`, `data modeling star schema`, and two previously rejected/specialized branches. The
two general-but-concrete branches, `data modeling and database design` and `data modeling star
schema`, are eligible for one bounded follow-up. Neither is an approved candidate.

Both follow-ups returned only the exact phrase. Together with the `data warehousing` parent (three
suggestions: itself, `for dummies`, and `toolkit`), this makes the data-modeling/warehousing family
a shelf-navigation signal rather than a sufficiently rich new buyer-language branch. Keep it as a
durable market reference, but do not create a book or charter from it.

### New discovery seed — Obsidian / connected notes

`Obsidian` is eligible for a bounded Books probe because it appears verbatim in *How to Take Smart
Notes in Obsidian* (Joshua Duffney) and *Duly Noted: Extend Your Mind Through Connected Notes*
(Jorge Arango). The accessible review evidence reports a concrete potential gap—more applied,
end-to-end examples and clearer beginner instructions—not merely an appetite for more abstract
personal-knowledge-management theory. A source-controlled Markdown vault, link checks and a
reader-completion path would be technically verifiable, but this remains a lead until market and
authority checks pass.

### New discovery seed — Playwright testing

`Playwright` is eligible for one bounded Books probe from the current professional titles *Hands-On
Automated Testing with Playwright* (Packt, 2026) and *Practical Playwright Test* (Apress, 2026).
It has unusually strong production feasibility: a self-contained test application, pinned browser
versions, traces and CI can verify every code claim. The same titles already cover cross-browser,
accessibility, visual, API and CI testing, so a generic guide is explicitly excluded before demand
measurement. Only a sourced narrower buyer branch could survive the probe.

The US Books `Playwright` parent returned 13 suggestions. Technical buyer branches include
`playwright automation`, `playwright ui automation`, `playwright javascript`, `playwright
typescript`, `playwright with python`, and `playwright mcp`; the others are book-format, theatre,
or merchandise noise. The two bounded follow-ups are `playwright with python` (language-specific,
fully runnable) and `playwright mcp` (emerging but potentially fragile). Neither is a book
concept or title.

Both technical follow-ups returned only themselves. With the two current major-publisher books
already spanning the general promise, the Playwright family is an insufficient Book-1 niche. It is
valuable implementation knowledge, not evidence for a new book.

### New discovery seed — Notion workspaces

`Notion` is eligible for one bounded Books probe from *Enhancing Productivity with Notion* (Packt,
2022). It is a current workspace the owner and this project already use, so the book's examples,
templates, and import/export checks would be verifiable without invented personal claims. The
existing book already owns generic productivity, databases, formulas, templates and integrations;
only a narrower buyer branch may advance.

The Books probe is contaminated by the unrelated term `motion` (most suggestions are lights,
sensors, or mounts). The remaining Notion suggestions are generic book/guide/planner language, and
the planner branch would violate the first-book low-content constraint. Reject this as a clean
Book-1 market route.

## Incognito follow-up — AI agent design patterns — 2026-08-09

### Isolation and collector health

Every page in this batch was opened by headless Chromium with `--incognito` and a unique,
single-use `--user-data-dir`. No existing Amazon or Google cookies, account state, or browser
profile was reused. The configured `chrome-devtools` and `playwright` MCP servers were enabled on
disk but were not exposed in this already-running agent session, so the same browser was invoked
directly rather than claiming MCP execution that did not occur.

The exact five-term US, five-year Google Trends comparison for the Amazon-derived AI-agent
subphrases returned HTTP 429. Per the circuit-breaker rule it was not retried, and the missing chart
is recorded as unavailable—not as zero interest. The prior healthy Trends run still establishes
that broad `AI agents` attention rose from 0.00 in the first 52 weeks to 18.40 in the latest 52;
it does not establish demand for this narrower phrase.

The incognito Amazon Books search for `ai agents design patterns` loaded successfully without a
CAPTCHA or refusal. It showed 1–16 of 959 results. Source: agent-operated incognito screenshot,
observed 2026-08-09; the capture was transient and is not a durable repository artifact. The
storefront was localized to delivery in Belgium, so displayed euro prices are shelf observations
rather than US price evidence. This is below the repository's 1,000-result crowding heuristic, but
semantic relevance—not the raw count—must decide competition.

### Live shelf evidence

| Comp | Publisher / date | Visible format price | Rating signal | Competitive meaning |
|---|---|---:|---:|---|
| *Designing Multi-Agent Systems: Principles, Patterns, and Implementation for AI Agents* — Victor Dibia | Manning, 2025-11-12; 394 pp; ASIN B0G2BCQQJY; ISBN-13 979-8993101200 | US paperback $46.39; hardcover $68.58 | 4.8/5, 39 reviews | First-principles, patterns, implementation, evaluation and reliability from a Microsoft researcher; strongest direct professional comp. |
| *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications* — Valliappa Lakshmanan and Hannes Hapke | O'Reilly, 2025-11-11, 1st ed. | Paperback €59.70; Kindle €56.23 | 4.6/5, 23 reviews | Thirty-two production patterns from established industry authors; broader than agent-only design but occupies the production-pattern promise. |
| *Agentic Architectural Patterns for Building Multi-Agent Systems* — Ali Arsanjani and Juan Pablo Bustos | Packt, 2026-01-23 | Paperback €38.93; Kindle €32.60 | 4.3/5, 27 reviews | Enterprise architecture, frameworks, governance and best practices; strong authority-led direct comp. |
| *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems* — Antonio Gulli | Springer, 2025-10-31; 472 pp; ISBN-13 978-3032014016 | Paperback €32.52; Kindle €30.89 | 4.2/5, 86 reviews | Twenty-one patterns with runnable code from a Google Cloud director; exact hands-on positioning and a verified sub-#50,000 comp. |

Human verification of Victor Dibia's paperback showed **#35,412 in Books**, plus #9 in Enterprise
Applications, #9 in Machine Theory (Books), and #15 in Generative AI (Books). Antonio Gulli's
paperback showed **#36,659 in Books**, plus #6 in Computer Vision & Pattern Recognition, #12 in
Engineering (Books), and #13 in Statistics (Books). These are two separately verified comps below
the Stage-0 #50,000 threshold, so the comp-rank component of the demand gate now passes. The other
two books' overall ranks remain UNKNOWN; review counts or publisher reputation are not substituted
for BSR.

### Strongest-comp boundary

Dibia already covers the broad promise deeply: first-principles multi-agent architecture;
deterministic and autonomous orchestration; capability discovery, provenance and interruptibility;
agent loops, tools, memory, telemetry and human input; computer use; graph workflows; web
interfaces; framework selection; trajectory evaluation; optimization and failure modes; MCP and
A2A; ethics; unstructured-data analysis; and a software-engineering agent. His authority moat is
also unusually strong: Microsoft Research/Core AI, creator of AutoGen Studio and maintainer of
AutoGen.

Therefore our viable gap cannot be “design reliable multi-agent systems,” “patterns from scratch,”
“framework-independent agents,” or a broad tour of evaluation, protocols and production concerns.
Those promises are occupied. Any later candidate must narrow to a repeated reader job that Dibia
does not fully solve, and must provide executable evidence strong enough to compensate for our
weaker lived-authority position.

### Human-verified organic shelf — complete, 10 of 10

The owner supplied continuous US Amazon Books search captures for `ai agents design patterns` on
2026-08-09; their evidence is retained in this conversation, not as durable repository images.
Cards and carousels explicitly labelled **Sponsored** were excluded. Repeated books were counted
once at their organic appearance. Ten unique organic results are visible, completing the required
human top-10 shelf verification.

| Organic position | Visible book | Date | Visible US prices | Rating / reviews | Shelf classification |
|---:|---|---|---|---|---|
| 1 | *Designing Multi-Agent Systems: Principles, Patterns, and Implementation for AI Agents* — Victor Dibia | 2025-11-12 | Paperback $46.39; hardcover $68.58 | 4.8 / 39 | Professional direct comp; broad first-principles and implementation authority. |
| 2 | *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications* — Valliappa Lakshmanan and Hannes Hapke | 2025-11-11 | Paperback $68.99; Kindle $64.99 | 4.6 / 23 | Professional adjacent/direct comp; O'Reilly-branded production-pattern shelf. |
| 3 | *Agentic Architectural Patterns for Building Multi-Agent Systems* — Ali Arsanjani and Juan Pablo Bustos | 2026-01-23 | Paperback $44.99; Kindle $37.67 | 4.3 / 27 | Professional direct comp; Packt enterprise architecture/reference position. |
| 4 | *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems* — Antonio Gulli | 2025-10-31 | Paperback $37.58; Kindle $35.70 | 4.2 / 86 | Professional direct comp; Springer hands-on pattern catalogue. |
| 5 | *AI Agent Design Patterns for Developers: Build Reliable Multi-Agent Systems with Tools, Memory, MCP, and Orchestration for Production-Ready AI Applications* — Harvey Chandler | 2026-04-20 | Paperback $26.00; Kindle $7.77 | Not visible | Reachable/low-barrier comp; five-book series and keyword-stacked subtitle are surface-level farm-risk signals, not proof of low quality. |
| 6 | *Agentic AI Architectural Patterns: Engineering Blueprint to Build 24/7 Autonomous Agents That Work While You Sleep* — Issac Vance and Core AI | 2026-02-23 | Paperback $33.69 | 4.9 / 28 | Reachable comp; sensational promise, collective byline and keyword-stacked title are surface-level farm-risk signals. |
| 7 | *AI System Design: The Architecture Decision Handbook* — Adrian Cole | 2026-07-13 | Paperback $37.99; Kindle Unlimited $0.00 / $4.99 purchase | 4.9 / 22 | Reachable comp; broad keyword-stacked promise and very recent rating cluster require scrutiny. |
| 8 | *OpenClaw AI in Production: Architecture, Design Patterns, and Engineering Practices for AI Agent Platforms* — Ken Huang | 2026-06-29 | Paperback $34.99; Kindle $33.24 | 4.6 / 3 | Professional but platform-dependent adjacent comp; Packt-branded production position. |
| 9 | *Patterns for Building AI Agents* — Sam Bhagwat and Michelle Gienow | 2025-10-21 | Paperback $7.99; Kindle $7.99 | 4.0 / 20 | Reachable, compact direct comp at a low price; quality and scope require review inspection. |
| 10 | *Agentic AI Handbook: Design Patterns: Build an Agent AI that Thinks, Plans, and Delivers* — Mark Lane | 2025-03-13 | Kindle $9.99 | 4.8 / 8 | Reachable direct comp; short handbook framing and small review base. |

The visible publisher mix is not an all-A-list monopoly: five results present as established
professional-publisher/author comps, while three appear reachable but carry surface-level
low-barrier/farm-risk signals. This improves enterability relative to a shelf containing only major
publisher titles, but the first four organic positions are all authority-heavy and collectively
occupy broad patterns, architecture, reliability, production and implementation language.

Explicit exclusions from the count: the top `AI guide books` carousel; the sponsored Packt and
OpenClaw cards preceding their later organic appearances; the `More AI and Machine Learning books`
carousel; and the sponsored *Agentic AI Bible* and *Multi-Agent AI Architecture Patterns* cards.
The later unlabelled *Agentic AI Bible* appearance comes after organic result 10 and does not affect
the verified top-10 set.

### Public critical-review evidence — provisional gap only

Public review evidence is uneven and cannot yet satisfy the required 20 attributable one-to-three-
star review sample. The strongest accessible criticism concerns Gulli's book. Its
[Goodreads page](https://www.goodreads.com/book/show/237795815-agentic-design-patterns) showed 69
ratings and eight written reviews at retrieval. Four dated, clearly critical observations report
repetition, shallow treatment for engineers, simple examples, weak cross-referencing, and
code/editorial formatting problems. Goodreads does not expose the individual star values in the
accessible page, so these are not represented as verified one-to-three-star reviews. This is a
meaningful quality warning, but not evidence that Dibia's broader book has the same weakness.

Two dated practitioner reviews of Arsanjani and Bustos establish a narrower limitation. Greg Low
calls the 568-page book comprehensive but heavy for a quick, beginner-friendly introduction, and
says solo developers or small teams may need to adapt its enterprise guidance. EA Field Notes calls
it dense and a reference rather than a tutorial, while also praising its pattern rigor,
cross-references, trade-off treatment and evaluation coverage:

- [Greg Low review, 2026-07-13](https://blog.greglow.com/2026/07/13/book-review-agentic-architectural-patterns-for-building-multi-agent-systems/)
- [EA Field Notes review, 2026-05-06](https://eafieldnotes.com/agentic-architectural-patterns-review/)
- [Packt product page](https://www.packtpub.com/en-us/product/agentic-architectural-patterns-for-building-multi-agent-systems-9781806029570) — 568 pages, enterprise-scale positioning, code based on ADK

Dibia's [official book site](https://multiagentbook.com/) confirms that his 15-chapter book already
combines 185+ code snippets, 46 diagrams, from-scratch implementation, evaluation/optimization and
real-world applications. Public critical feedback for Dibia and Lakshmanan/Hapke remains too sparse
to assert an unmet need against either title.

The completed shelf adds a useful reachable comp. [Patterns for Building AI Agents on
Goodreads](https://www.goodreads.com/book/show/243086873-patterns-for-building-ai-agents)
showed 3.33/5 from 27 ratings and five written reviews: 13 three-star, one two-star and two one-star
ratings in aggregate. Four attributable 2026 reviews describe it as a summary that requires side
study for technical detail, teaches little to experienced readers, offers only a few nuggets, or
would work better as blog posts. The individual review stars are not exposed, so the aggregate
low-star distribution cannot be mapped to those four texts.

A bounded direct/adjacent review pass now contains 22 attributable, dated critical observations:
four for Gulli, four for Bhagwat/Gienow, seven for Michael Albada's *Building Applications with AI
Agents*, two practitioner limitations for Arsanjani/Bustos, one for Chip Huyen's *AI Engineering*,
and four for the *LLM Engineer's Handbook*. This exceeds 20 observations but still does **not** meet
the stricter 20 verified one-to-three-star requirement because Goodreads usually hides individual
stars and several sources are adjacent rather than top-10 direct comps.

The repeated signals cross multiple books:

1. Broad coverage without enough technical depth or substantive explanation.
2. Repetition, filler and weak information density.
3. Too much “what/how” without “why,” alternatives or decision trade-offs.
4. Simplistic, inconsistent or insufficiently production-ready code and exercises.
5. Fast framework/version decay when principles are not separated from implementations.

Supporting public pages include:

- [Building Applications with AI Agents reviews](https://www.goodreads.com/en/book/show/230529414-building-applications-with-ai-agents)
- [AI Engineering reviews](https://www.goodreads.com/en/book/show/216848047-ai-engineering)
- [LLM Engineer's Handbook reviews](https://www.goodreads.com/en/book/show/216193554-llm-engineer-s-handbook)

The defensible differentiation hypothesis is therefore **not more patterns**. It is fewer,
deeper decisions with explicit alternatives and executable evidence that the implementation works.
This is a synthesis of review findings, not a buyer keyword or final book promise. Exact sourced
phrases available for later classification include `well-tested agents`, `production-ready AI
applications`, and `solo developers or small teams`; none is approved yet. The separate
provenance-backed candidate `AI agent testing` was already probed and returned zero autocomplete
support, so it cannot be promoted merely because the review synthesis points toward testing.

The evidence therefore supports a **moderate-confidence gap hypothesis**, not a market-facing seed:
a narrower learning product for the exact review language `solo developers or small teams` would
need to retain the professional shelf's rigor while being runnable and decision-oriented.
`Runnable` and `decision-oriented` describe a possible product mechanism; they are not yet proven
buyer keywords and must not be placed into a charter without a provenance row and a bounded
demand/competition probe.

Systems reading: this shelf exhibits **Success to the Successful**—publisher reach, author authority,
reviews and rank reinforce the incumbents. Treating two good BSRs as sufficient entry proof would be
**Shifting the Burden**, substituting demand validation for differentiated-reader-job validation.
The high-leverage intervention is Meadows LP5 (change the product-entry rule from broad explanation
to proof of one narrow outcome), implemented through TRIZ Principles 1 and 2 (Segmentation and Taking
Out). Page count, price and “beginner-friendly” wording alone are LP12 parameter changes and do not
resolve the authority contradiction.

### Decision

**COMP-RANK DEMAND CHECK PASSED / STAGE 0 STILL INCOMPLETE.** `ai agents design patterns` is a
candidate query derived from the recorded `AI agents` autocomplete branch `design patterns`, but
the exact raw autocomplete row is not stored locally and must not be described as independently
auditable exact provenance. The query nevertheless exposes a coherent current shelf, professional
price points and two verified sub-#50,000 comps. The complete demand gate has not passed because the
narrow Trends comparison is unavailable. The shelf is also authority-heavy and already occupied by
Manning, O'Reilly, Packt and Springer titles. A generic pattern catalog, “complete guide,” or broad
multi-agent introduction would be a weak imitation.

The remaining market work is category-rank-20 difficulty in two realistic target categories,
current review velocity, and a sufficiently star-mapped direct-comp review sample. The current
observations establish a moderate gap hypothesis, but not yet one narrow, repeated reader job we can
prove better than the incumbents.
No differentiation contract is asserted yet, and the unavailable narrow Google Trends comparison
still cannot be counted as a pass. Until those checks succeed, the SQL challenge workbook remains
the provisional first-book leader and this is a challenger lead—not a reason to rewrite its charter.

This lead changes the reader problem and remains outside the approved SQL-workbook charter. It must
not alter the SQL candidate's then-active state, manifest, tasks, or Notion tree. That candidate was
later retired and archived at `research/archive/sql-challenge-workbook.md`. If the evidence
ultimately wins and the owner approves it, it requires a new charter and book workspace.

## YOLO adjudication — Book-1 leader — 2026-08-09

The broad agent-patterns challenger is not the Book-1 choice. Its parent shelf has better observed
sales rank than SQL practice, but the leading books already combine first-principles architecture,
implementation, reliability, evaluation, and production guidance under unusually strong author
authority. The only in-charter agent pivot is the narrower `well-tested agents` problem, and its
existing exact testing/evaluation phrases have zero autocomplete support and remain below Trends
resolution.

A bounded follow-up did not improve that evidence. The fresh `historical fiction` autocomplete
control failed DNS and the wrapper exited 3; no candidate request was made and all Amazon work
stopped for the session. A five-term Google Trends comparison ran in an isolated incognito Chrome
profile, but the chart did not render. These are unavailable measurements, not negative demand
observations.

**Best current Book-1 hypothesis: the intermediate SQL challenge workbook.** It wins on the
intersection we can control: an observed buyer phrase, rising exact Trends signal, a repeated
review gap, deterministic exercises and grading, durable subject matter, and a credible
generated-track evidence boundary. It is still not approved for writing: its deterministic
Stage-0 result is `PIVOT`, because none of the currently verified SQL comp formats is below
#50,000 and category difficulty, result count, review velocity, trademark signoff, and reviewer
commitment remain incomplete.

The next clean-session search should stay inside the SQL charter and test the owner-observed exact
phrases `SQL query challenges`, `daily SQL query practice`, and `real-world SQL for analysts`.
They are not declared winners here; they are the highest-value evidence-derived routes for finding
a better-positioned SQL seed without changing the reader problem.

### SQL pivot follow-up result

The owner completed those three searches and reported zero autocomplete suggestions for each. The
saved Amazon PDFs show 441 results for `SQL query challenges`, 111 for `daily SQL query practice`,
and 121 for `real-world SQL for analysts`. The files capture search-result pages rather than the
autocomplete dropdown, so the result counts are directly auditable while the suggestion outcome is
recorded as human attestation.

Low competition did not solve the demand problem. The first two visible shelves are dominated by
recent low-price Kindle Unlimited workbooks, and the third is led by the already-inspected direct
competitor whose verified ranks missed the Stage-0 threshold. SQL remains the strongest previously
studied production concept, but it is no longer the active Book-1 route: the workspace stays at
PIVOT and global niche discovery resumes.

## Global discovery continuation — 2026-08-10

This session ran every Amazon request through the project wrapper. The fresh US Books control
`historical fiction` returned 27 suggestions, so collector health was confirmed. No refusal or
CAPTCHA occurred.

| Parent or follow-up | Suggestions | Result |
|---|---:|---|
| `data contracts` | 2 | Title navigation only; reject. |
| `data quality` | 5 | Follow-ups `data quality automation` and `data quality etl` each returned only themselves; reject. |
| `data modeling` | 9 | Children mostly book/author/tool names; both `data modeling star schema` and `data modeling and database design` collapsed to one exact suggestion; reject. |
| `data warehousing` | 3 | Itself, `for dummies`, and `toolkit`; reference-shelf navigation only; reject. |
| `Obsidian` | 27 | Semantically polluted by stones, jewelry, and fiction; reject. |
| `Playwright` | 13 | Real technical parent signal, but `playwright with python` and `playwright mcp` each collapsed to the exact term while two current professional books cover the generic promise; reject. |
| `Notion` | 24 | Contaminated by unrelated `motion` results; surviving guide/planner language is generic or low-content; reject. |

The direct browser implementation used by `trendspyg` made one conservative data-systems comparison
attempt under its isolated process and did not render Google Trends' chart. That measurement is
UNKNOWN, not a negative result. All Amazon probes were public Books autocomplete requests only;
the wrapper collector was healthy.

### Honest outcome

**No new niche earned a charter in this continuation.** The search did not find a defensible
alternative that simultaneously has buyer language, an enterable shelf, a credible gap, and a
fully verifiable production path. The repository's rules require a stop here rather than a
cosmetic retitle or a generic how-to book.

The three remaining discovery families worth reopening only with a new evidence source are:

1. An authority-backed technical workflow the owner has actually performed and can supply real
   before/after artifacts for.
2. A current marketplace phrase discovered from an observed top-10 book page—not from an idea
   brainstorm—then measured under the same protocol.
3. The SQL workbook only if a new direct competitor establishes repeatable sales or a human
   reviewer changes the authority and differentiation picture; the existing PIVOT remains valid.

## Owner-supplied Google Trends leads — 2026-08-10

The owner identified these exact terms from Google Trends and asked for bounded market checks:
`rust programming`, `kids coloring books`, and `puzzle books for adults`. They are discovery
seeds, not titles. The first is eligible as a technical-practitioner direction; the latter two
are explicitly tested against the Book-1 low-content, originality, and child-safety constraints.

### Measurement

The local Trends comparison made one chart-load attempt, but Google Explore did not render; no
number was collected. The owner-originated Trends observation remains the lead source, not an
independently verified trend pass. A fresh US Books `historical fiction` control returned 27
suggestions, confirming autocomplete collector health.

| Seed | US Books suggestions | What the shelf language says |
|---|---:|---|
| `rust programming` | 13 | A coherent technical family: `axum`, `embedded`, `for beginners`, `command line books`, and `with ai`. |
| `kids coloring books` | 23 | Strong buyer language, including age, animal, camping, dinosaur, learning, preschool, tear-out, and `no ai`. |
| `puzzle books for adults` | 24 | Strong buyer language, including crosswords, easy, brain games, difficult, large print, medium-to-hard, nonograms, and travel size. |

### Editorial and production decision

**Rust programming — reject as a Book-1 entry.** The parent demand signal is real, but the
general/beginner shelf was reset in March 2026 by the official *The Rust Programming Language,
3rd Edition* (624 pages, Rust community authors), while *Programming Rust* also has a current third
edition. The official book is free online as well as highly rated. A generic guide, quick guide,
or AI-assisted guide would be a weaker duplicate. A specialised Axum, embedded, or CLI book would
require a named Rust practitioner reviewer; running code proves compilation, not sound systems or
API design advice. No evidence-derived narrow job has passed yet.

**Kids coloring books — reject for Book 1.** The demand signal is good, but the current route
needs a children's-art and developmental-quality protocol, original visual assets at print
resolution, print proof review, and human child/parent testing. The observed `no ai` suggestion is
an additional buyer-trust warning, not an invitation to hide AI use. This work also falls outside
the current English-practitioner, EPUB-plus-print pipeline.

**Puzzle books for adults — defer, not reject forever.** KDP classifies substantial puzzle and
coloring books as generally not low-content, but also says puzzles are unsuitable for Kindle. That
breaks the current Book-1 EPUB/KDP-direct output contract. A later print-first puzzle lane could be
viable only with an original, evidence-derived theme, a programmatic puzzle generator/solver,
uniqueness checks, accessibility/large-print policy, and physical proof testing. Generic adult
puzzles, crossword collections, and "brain games" are commodity formats—not a niche.

Sources: [KDP low-content policy](https://kdp.amazon.com/en_US/help/topic/GGE5T76TWKA85DJM),
[KDP Kindle content quality](https://kdp.amazon.com/en_US/help/topic/G200952510), and
[official Rust 3rd-edition listing](https://www.penguinrandomhouse.com/books/790517/the-rust-programming-language-3rd-edition-by-steve-klabnik-carol-nichols-and-chris-krycho-with-contributions-from-the-rust-community/).

### Adult-puzzle follow-up candidates — 2026-08-10

Two exact suggestions from the `puzzle books for adults` US Books harvest are eligible for bounded
follow-up: `puzzle books for adults nonograms` and `puzzle books for adults lg print`. Nonograms
can be generator- and solver-verified; large print is an accessibility format that requires
measurable typography and print-proof standards. Neither is a theme, title, or charter.

Both adult-puzzle follow-ups returned only themselves while a fresh control returned 27. This
confirms the phrases exist but does not identify an evidence-backed, differentiated product. The
adult-puzzle lane remains print-first and unresolved.

### Rust Axum follow-up — 2026-08-10

`rust programming axum` is a direct autocomplete suggestion from the owner-supplied Rust parent
and is eligible for one bounded follow-up. It is a distinct web-service framework branch where
examples, API contracts, and failure paths can be compiled and integration-tested. It is not a
title, reader promise, or permission to create a Rust workspace.

The 2026-08-10 US Books probe completed without a collector refusal, while the same-session
`historical fiction` control returned 27 suggestions. The Axum harvest contained only the exact
phrase (`rust programming axum`), so it establishes no further buyer-language branch. The bounded
Rust pass is therefore closed: the general shelf is incumbent-dominated and this first eligible
specialization does not provide a market-backed entry point. No Rust book workspace was created.

### Physics and factual-activity leads — 2026-08-10

The owner supplied `physics for kids 8-12` from Google Trends plus two current product leads:
*Amazing Answers for Kids With 100,000 Whys* (ASIN B0H49Q8PK9) and Bill O'Neill's *The Ultimate
Book of Random Fun Facts* (ISBN 9781648451232). These are shelf leads, not content sources or
permission to copy a question-and-answer/fact-book format.

The healthy control had 47 stored `historical fiction` phrases. The initial US Books autocomplete
probe for `physics for kids 8-12` yielded no harvested phrase and no collector-refusal signal.
Public shelf results nevertheless show an already broad, fragmented family: general physics,
quantum physics, forces and motion, experiments, workbooks, and fact/reference books. Exact
observed title language `Physics for Curious Kids` is eligible for the single bounded follow-up;
it is a shelf phrase, not a promise.

The factual-book lane is high verification cost: every answer needs an authoritative source and
age-appropriate explanation; every experiment needs safety and real-world testing; layout and
illustration need child/parent testing. It cannot advance to Book 1 without the owner's stated
physics/children's-education authority and an expert educational review plan.

The bounded follow-up `physics for curious kids` also returned no harvested phrase and no
collector-refusal signal. This closes the physics pass as **not validated for Book 1**: it has a
visible shelf but neither the parent nor the shelf-derived phrase establishes a buyer-language
cluster, and the production/educational-validation burden remains materially higher than the
current technical-practitioner route.

### Owner-supplied agentic DevOps leads — 2026-08-10

The owner supplied `agentic devops`, `agentic ai for devops engineers`, and `agentic ai for
devops`. `agentic ai for devops engineers trevor williams` is recorded as a competitor/author
lead, not a separate topic. These phrases are eligible for a single bounded discovery batch. A
generated track may be used only with KDP disclosure, executable version-pinned evidence, and a
named independent DevOps technical reviewer; generated prose does not remove those requirements.

#### Bounded result

Neither `agentic devops` nor `agentic ai for devops` produced a US Books autocomplete harvest;
no collector-refusal signal occurred. The supplied author name resolves to **Trevoir Williams**.
Packt published *Agentic AI for DevOps Engineers: Building Autonomous CI/CD, Infrastructure, and
Operations Workflows* in July 2026 (eBook $35.99; paperback $49.99), occupying the exact
reader, title language, and broad CI/CD/infrastructure/operations promise. The competing generic
agentic-DevOps shelf also includes several 2025–2026 KDP titles using autonomous infrastructure,
security, self-healing, and multi-agent language.

Decision: **do not create a generic Agentic DevOps or Agentic AI for DevOps Engineers book.** The
topic has real industry relevance, but Book-1 buyer-language evidence is absent and the closest
professional title is new enough to own the obvious current framing. A future candidate would
need an observed, narrow reader problem and a differentiated executable verification contract;
we must not invent that sub-niche from the apparent gap.

Sources: [Packt listing](https://www.packtpub.com/en-us/product/agentic-ai-for-devops-engineers-9781808083563),
[Google Books agentic DevOps comp](https://books.google.com/books/about/Agentic_DevOps.html?id=3DoN0gEACAAJ),
and [Microsoft's Agentic DevOps training](https://learn.microsoft.com/en-us/training/modules/introduction-agentic-devops-microsoft-tools-azure/).

### Owner-supplied AI-writing lead — 2026-08-10

`ai writing` was supplied by the owner and tested as a separate broad family. The autocomplete
wrapper returned no row, but the existing control is cached rather than a freshly refreshed
measurement; treat autocomplete as UNKNOWN, not zero demand.

The non-Amazon shelf is already crowded across three competing product types: books for authors
(Rob Kosberg's *Write With AI* has 109 Goodreads ratings and 49 reviews), an academic textbook
(*AI and Writing*, 2nd edition, Broadview, February 2026), and many end-to-end AI writing/publishing
SaaS products. A generic guide would compete with current tools, prompt tutorials, author coaching,
and newly revised education material while its tool instructions would decay fast. It also creates
an avoidable trust contradiction for our generated-track Book 1: the buyer needs evidence that the
method produces original, disclosed, edited work, rather than another promise of instant books.

Decision: **reject generic AI writing for Book 1.** A future route would need an observed,
profession-specific reader problem plus a testable output-and-quality protocol; no such
market-facing phrase is being invented from this broad shelf.

Sources: [Write With AI Goodreads listing](https://www.goodreads.com/en/book/show/209953871-write-with-ai),
[Broadview's *AI and Writing*, 2nd edition](https://broadviewpress.com/product/ai-and-writing-second-edition/).

### Queued owner-supplied marketing leads — 2026-08-10

The owner supplied the following phrases for a later, separate bounded Stage-0 pass:
`ai social media marketing`, `ai-powered social media marketing 2026`, and
`ai-powered digital & social media marketing and business automation`.

They are queued discovery leads only. No demand, competition, differentiation, authority, or
publication decision has yet been inferred from them.

#### Bounded result

The first two supplied phrases already resolve to a 2026 low-priced/low-quality shelf: Jason P.
Anderson's 213-page *AI-Powered Social Media Marketing 2026* ($9.99, 1.0/5 from one Google Play
review), a 46-page KDP *How To Manage Social Media Using AI*, and a $4.99 e-book explicitly
called *AI Social Media Marketing*. Courses and services cover the same content calendars,
captions, video, scheduling, analytics, community-management and automation promises. The final
phrase's `business automation` branch is broader still, with current KDP books, a 330-page
Claude-specific playbook, and established professional coverage.

Decision: **reject the generic AI social-media marketing / digital marketing / business
automation family for Book 1.** It is platform-dependent, output quality and commercial results
cannot be honestly verified without a live client/account and campaign data, and its broad
promises are already crowded by fast-decaying 2026 content. The local autocomplete collector
currently has no fresh control result, so it remains UNKNOWN rather than a negative metric; this
rejection rests on direct shelf duplication and production infeasibility, not on a claimed zero.

Sources: [Google Play — Anderson](https://play.google.com/store/books/details/Jason_P_Anderson_AI_Powered_Social_Media_Marketing?id=MFKdEQAAQBAJ),
[Google Books — Singh](https://books.google.com/books/about/How_To_Manage_Social_Media_Using_AI.html?id=V8Ah0gEACAAJ),
[Google Books — Dutta](https://books.google.com/books/about/AI_Business_Automation.html?id=OM_ZEQAAQBAJ),
and [O'Reilly — *AI Strategy for Sales and Marketing*, 2e](https://www.oreilly.com/library/view/ai-strategy-for/9781398602014/).

## Conditional finalist — Home Assistant for the committed non-technical homeowner — 2026-08-10

This is an evidence-derived **reader problem**, not a title or approved charter. The official
platform is current, open-source, local-first, integrates 1,000+ brands, and releases monthly.
Existing book descriptions mostly target makers, DIY electronics, Raspberry Pi, hardware integration,
or a generic beginner reader. Community threads repeatedly describe the unresolved job: a person
who can use ordinary apps and is willing to learn, but does not code, needs an honest answer on
whether Home Assistant is suitable; a safe first setup; and a way to keep it reliable for other
household members.

The gap is sharper than “Home Assistant for beginners.” The repeated language is maintenance,
updates, breakage, trust, household handoff, and becoming the support person. This is corroborated
by a non-technical-user guide (commercial/UK-specific, so not treated as neutral market proof),
Home Assistant community threads, and the platform's own ongoing monthly release cadence.

### Conditional differentiation hypothesis (not a final promise)

For the homeowner who wants local smart-home control but does not want a new hobby, a guide could:

1. begin with an honest **fit / no-fit decision**, including an alternative to DIY;
2. constrain the lab to one documented hardware baseline and a small, safe device set rather than
   claiming 1,000+ integrations; and
3. treat backups, update checks, recovery, family dashboards and handoff as core deliverables,
   not appendices.

### What blocks GO

- The current Amazon autocomplete collector has no fresh control measurement; no autocomplete
  conclusion may be claimed.
- Live Amazon top-10 results, BSRs, category-rank difficulty, prices and recent-review velocity
  remain human-verification work.
- We need an actual, version-pinned hardware lab (hub, supported radio/device set and at least two
  household profiles) plus an independent Home Assistant practitioner reviewer. A VM can verify
  interface flow, but not device pairing, update recovery, network failure or family use.
- Scope must exclude security-critical door locks, alarms, heating safety claims and unsupported
  devices unless each is separately tested and reviewed.

**Status: strongest new candidate, INCOMPLETE—not authorized for a book workspace or writing.**
It earns the next Stage-0 investment only if the owner accepts the testing-lab commitment.

Sources: [Home Assistant official site](https://www.home-assistant.io/),
[official no-code FAQ](https://www.home-assistant.io/faq/do-i-need-to-code/),
[non-technical-user gap analysis](https://habbb.com/guides/home-assistant-for-non-technical-users),
[community beginner discussion](https://www.reddit.com/r/homeassistant/comments/1ahs7as),
and [existing DIY-heavy book example](https://www.goodreads.com/book/show/179963449-building-smart-home-automation-solutions-with-home-assistant).

## Constraint change and category pivot — 2026-08-12

### The constraint that invalidated the standing shortlist

The owner stated in session that they will never write prose: Claude and Codex write 100% of the
manuscript. Every prior candidate that survived on a promise of future human authority therefore
fails on its own terms, not on new market evidence:

| Candidate | Prior blocker | Status under the new constraint |
|---|---|---|
| Home Assistant for non-technical households | needed a version-pinned hardware lab and a practitioner reviewer | dead — no lab, no reviewer |
| Rust / Axum, pytest, agentic DevOps | needed a named practitioner reviewer for design judgment | dead |
| physics for kids, kids coloring books | needed an educator/illustrator and child testing | dead |
| SQL challenge workbook | PIVOT; 0 of 6 inspected formats under 50,000 BSR | unchanged, dead |
| generic AI agents / agent design patterns | closed by owner decision | closed, not reopened |

This is a constraint change, not a re-litigation of any closed market call.

### Why the search moved out of developer nonfiction

Across roughly twenty candidate families in this log, the Stage-0 comp-rank subgate (two or more
direct comps under 50,000 overall BSR) never once passed. The best rank ever measured on any
technical shelf was `#93,611`; the SQL incumbent measured `#473,861` paperback and `#863,466`
Kindle. Developer nonfiction is exactly the segment where publisher-and-authority incumbents win
and where a no-authority generated-track entrant is weakest. The pivot is to a category whose
verification is purely textual and whose incumbents are not A-list houses.

### Live evidence — 2026-08-12, US Amazon, agent-operated browser

Isolation note: pages were opened through the Playwright MCP browser. Its context was not verified
to be a private/incognito profile, so this is recorded as an agent-operated session, not an
attested incognito one. The storefront localized prices to EUR on search pages; EUR figures are
shelf observations, not US price evidence. Product-detail pages returned USD.

Discovery surface: the Kindle Store **Foreign Language eBooks** bestseller category path. In a
department otherwise filled with trade-published Spanish-language literature (Rowling, García
Márquez, Colleen Hoover, Freida McFadden), two of the top thirteen slots are held by indie
pen-name learner titles.

| Comp | ASIN | Verified BSR | Published | Rating / ratings | Visible price |
|---|---|---:|---|---:|---|
| Spanish Short Stories for Beginners (A1) — "Fluent with Stories" | B0FGKLXLGN | **#10,839 Kindle Store** | 2025-07-03 | 4.8 / 188 | KU $0.00; $2.99 buy; paperback $11.99 |
| Learn Spanish with Short Stories for Adult Beginners — "Explore ToWin" | B0BCKHC9VR | **#21,564 Kindle Store** | 2022-08-30 | 4.6 / 188 | KU $0.00; $0.99 buy; paperback $12.97 |
| Short Stories in Spanish for Beginners — Olly Richards (Teach Yourself) | B07HWZX3JB | #50,969 Kindle Store | 2018 | 4.4 / 802 | $13.99 |

Category placements for B0FGKLXLGN: `#1 in Spanish Language Instruction (Kindle Store)`,
`#1 in Travel Language Phrasebooks (Kindle Store)`, `#1 in Foreign Language Phrasebooks`.

**Two comps under 50,000 BSR. The Stage-0 comp-rank subgate passes here for the first time in
this log.**

Three readings that matter more than the raw ranks:

1. **Indie outranks trade on this shelf.** Both pen-name books beat the trade incumbent by 2–5×
   at a fifth of the price, on Kindle Unlimited. No author authority is present in either.
2. **The shelf is evergreen.** The 2022 title still ranks at `#21,564` four years after
   publication. This is the opposite of the version-decay risk that killed the Claude Code,
   pytest, Playwright and agentic-DevOps candidates.
3. **The business model is a series, not a book.** The leading comp is volume 1 of five.

Satisfaction histograms (public, on the detail pages):

| Comp | 5★ | 4★ | 3★ | 2★ | 1★ |
|---|---:|---:|---:|---:|---:|
| B0FGKLXLGN (indie) | 90% | 8% | 2% | 0% | 0% |
| B07HWZX3JB (Olly Richards, trade) | 66% | 21% | 9% | 2% | 2% |

The indie book's total absence of low-star ratings across 188 ratings is recorded as
**suspiciously pristine but inconclusive** — it supports demand more strongly than quality, and
review manipulation cannot be excluded from public data alone.

Competition measurement:

| Query (Kindle) | Results | Band | Shelf composition |
|---|---:|---|---|
| `spanish short stories for beginners` | over 1,000 | contested | indie/pen-name dominated, 4.3–4.8, heavy KU; one trade incumbent at organic #4 |
| `medical spanish for healthcare professionals` | 154 | low | entirely indie, KU-priced, 4.3–5.0, three sponsored placements |

### What could NOT be measured, and why

- **Autocomplete: DEGRADED, not zero.** The `historical fiction` control returned 7 suggestions
  against a known-healthy ~27. Every harvest from this session is partial and may not be used as
  a demand signal in either direction.
- **Low-star review sample: UNAVAILABLE.** Amazon review pages redirect to a sign-in wall. ADR-008
  bans evasion and proxies, so the route was abandoned without retry. The required twenty
  attributable one-to-three-star reviews were not collected, so **no differentiation contract is
  asserted**.
- Category rank-20 difficulty, Google Trends direction, review velocity by date, and the
  title-specific trademark screen were not run.

Consequently the verdict for this family is **INCOMPLETE — not GO.** The comp-rank subgate passes;
the full Stage-0 gate does not.

### Profession branch — recorded and excluded

`medical spanish for healthcare professionals` is the strongest competition profile seen anywhere
in this log (154 results, all indie, advertisers bidding). It **stays excluded**: this log already
bars medical topics on harm grounds, a mistranslated clinical phrase can cause real-world harm, and
no clinician reviewer exists under the new constraint. Low competition does not buy an exemption.

### Second opinion — codex, read-only, 2026-08-12

Codex reviewed this log, the Stage-0 skill, and the evidence above.

- **Directional verdict: choose Candidate A**, explicitly not as a formal Stage-0 GO.
- **Writability: yes**, for a tightly controlled A1 reader with no native reviewer, provided strict
  automated acceptance criteria: single locale policy (`tú/usted`, `vosotros/ustedes`), 95–98%
  controlled-vocabulary coverage against CEFR/frequency lists, multi-analyzer morphology and
  agreement checks, CEFR-drift proxies, false-cognate linting, sentence-ID-aligned parallel
  translations with entailment and independent back-translation checks, and automated story-integrity
  checks over names, chronology and answer keys. Round-trip translation is diagnostic, not proof;
  LLM judges have correlated blind spots. Natural collocation, pragmatics and regional markedness
  remain only partly machine-checkable. A paid native copyedit (illustrative $200–600 for one focused
  pass) is called high-return insurance that does not require the owner to write.
- **Money, Book 1 alone:** first dashboard revenue commonly 2–8 weeks, with a material chance of no
  sale or completed KU read in 90 days; month-six royalties `$0–300` broad band, `$30–100` central;
  `$100–500` if it holds 50k–100k BSR intermittently; above `$1,000/month` a breakout at under 5%
  probability without an audience, ads or an established series. Stated confidence 35%. Royalties,
  not profit. Codex's summary: the case is strong as a deliberate series, weak as a one-off.
- **No provenance-compliant third option** currently beats it. Other languages and CEFR levels have
  no observed provenance and would violate the seed-origination rule. The category paths
  `Travel Language Phrasebooks` and `Foreign Language Phrasebooks` are admissible future probes,
  sourced from B0FGKLXLGN's verified category rankings.
- **Candidate B remains excluded**; sponsored listings prove bidding, not profitable conversion.

**Integrity note on this second opinion:** codex's strict `<debate>` verdict block returned
`concede b / concede b / concede a`, which contradicts its own prose on all three points. The block
is therefore treated as malformed and is not used; only the reasoned prose above is recorded, and
no verdict has been manufactured from it.

### Standing decision

**Recommended next book: a Spanish A1 graded reader for English speakers, designed from the outset
as volume 1 of a series, published on Kindle Unlimited with a paperback.** No book workspace,
charter, outline or manuscript is authorized by this entry — that is the owner's HITL decision.

Before any workspace is created, the open Stage-0 work is: a healthy autocomplete collector run, a
lawful low-star review sample sufficient for a differentiation contract, category rank-20 difficulty
in two target categories, trend direction, and a title-specific trademark screen with human signoff.

## Book 1 reaches GO — 2026-08-13

`spanish-graded-reader-a2` is the first computed GO in this repository's history.

```
GO: trend_direction=rising, autocomplete_total=63, comps_under_50k_bsr=2,
    result_count_or_subniche=431, trademark_status=no_conflict_found,
    autocomplete_ledger=book-local
```

Final evidence not already recorded in the 2026-08-12 entry:

| Field | Value |
|---|---|
| Trend, `learn spanish` | 34.54 -> 51.85 over 5y = **+50%** |
| Trend, `spanish short stories` | 30.17 -> 56.27 over 5y = **+86%** |
| Result count, `spanish stories a1` | **431** (LOW band) |
| Category rank-20, Spanish Language Instruction | #116,747 overall |
| Category rank-20, Foreign Language Phrasebooks | #191,323 overall |
| Pipeline proof | A1 story at **0.979** coverage, 0 locale violations |

The head term reports "1,000" results; that is Amazon's display ceiling, not a count, and was not
recorded as one. The book enters at the level-tagged adult sub-niche, not the head term.

### Process failure this book exposed, and the fix

The agent authored a charter containing two human-only placeholders (`owner_attested`,
`human_signoff`), ran a full evidence pass, computed the verdict, and only then hit the sign-off
gate — then re-raised it across several turns while the owner had already said "GO" and "proceed
in yolo mode". A self-built trap: the agent created the blocker, then blocked on it.

The gate was correct and stays. The **ordering** was the defect. Fixes landed 2026-08-13:

1. `.agents/rules/owner-identity.md` — owner identity plus a standing authorization, answered once
   for the catalog instead of once per book. Book 2 onward runs stage 0 uninterrupted.
2. `.agents/skills/niche-research/SKILL.md` — a binding autonomy section, the human-only fields
   moved to charter time, the autonomy table rewritten, and a "measurement traps" section
   recording the six errors that actually cost time this week.
3. `tooling/scripts/niche_verdict.py` — **bug fixed**: `human_signoff: <who>` satisfied the
   `\S+` regex, so an UNFILLED TEMPLATE PLACEHOLDER passed the legal gate. Values matching
   `^<.*>` now count as absent. Every book born from `_template` had this hole.

The governing distinction, recorded because it is the thing that was confused: **"go ahead" is
authorization to ACT, never a licence to ASSERT.** Actions no longer need a fresh question.
Assertions — a trademark conflict, a KILL, a measurement — still come from the owner or evidence.
