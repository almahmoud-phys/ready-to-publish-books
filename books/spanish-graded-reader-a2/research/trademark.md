# Trademark screen — spanish-graded-reader-a2

**Searched:** 2026-08-12
**Method:** web search over indexed USPTO mirrors (Justia Trademarks, Trademarkia, uspto.report),
per `.agents/skills/niche-research/SKILL.md` Step 3. The official portals (WIPO, EUIPO TMview,
USPTO tmsearch) are JavaScript + CAPTCHA and return nothing to an agent; they were **not** scraped,
and no trademark library was installed (ADR-008 tier-3).
**Classes searched:** 9 (downloadable e-books), 16 (printed matter), 41 (publishing/education services).

## Status

verdict: no_conflict_found
trademark_status: no_conflict_found

Read that literally: **no conflict found across the sources listed below, in classes 9/16/41,
searched 2026-08-12.** It is an absence of evidence with its scope stated. It is **not** `clear`.
Only the owner converts this to clear at sign-off, and a real conflict goes to a lawyer, not to a
re-run.

## What was screened

| Term | Role | Result |
|---|---|---|
| `graded reader` | descriptive category term in the working title | No USPTO record surfaced for a registered mark consisting of this term in class 16 or 41. Results returned only general class guidance and unrelated marks (STEP-UP BOOKS, BROOKE'S BOOKS). |
| `Spanish A1 Graded Reader — Volume 1` | working title as screened, 2026-08-12 | Not screened as a whole mark — see limitation 1. |
| `Spanish A2 Graded Reader — Volume 1` | current working title from 2026-08-13 | **Not re-screened.** The retitle changed one token, `A1`→`A2`, and a CEFR level designator is descriptive of the goods in the same way `graded reader` is — so the finding below does not turn on it. Recorded rather than silently overwritten: the mark actually searched was the A1 string. Limitation 1 applies to both. |

## Finding

`graded reader` is the standard pedagogical term for a book written to a controlled vocabulary and
grammar level. That makes it **generic for the goods themselves** in class 16 and highly descriptive
of class 41 services, so it is not registrable as-is and would normally be disclaimed apart from the
mark in any series registration. This cuts both ways, and both ways are fine for us: we are unlikely
to infringe by using it descriptively, and we cannot own it.

What *is* registrable in this space is the **series brand** — the publisher-style name sitting above
the descriptive words (the Penguin Readers / Oxford Bookworms / Cambridge English Readers pattern).
That is precisely the asset this book does not have yet.

## Limitations — read before treating this as done

1. **The real screen has not happened yet.** The final title, subtitle, series name and pen name are
   all still unchosen; `metadata-seo` (stage 6) sets them. A trademark screen is only meaningful
   against the marks actually used, so **this file must be re-run at stage 6** against the final
   title, series name, imprint and pen name.
2. **The pen name is itself a mark surface.** Both verified comps publish under invented brand-style
   names ("Fluent with Stories", "Explore ToWin"). Whatever we choose needs its own class-9/16/41
   screen, not just a domain check.
3. Search coverage is indexed mirrors, not the live USPTO register. Mirrors lag.
4. EU/EUIPO not searched. Only relevant if we sell beyond amazon.com.

## Sources

- [Trademarkia — Trademark Class 16](https://go.trademarkia.com/trademark-class-16)
- [Trademarkia — Trademark Class 41](https://go.trademarkia.com/trademark-class-41)
- [Trademarkia — How to Trademark a Book Title](https://www.trademarkia.com/news/trademarks/how-to-trademark-book-title)
- [Justia — Browsing Trademarks with International Class Code 41](https://trademarks.justia.com/international-class-code/41/page3)
- [uspto.report — STEP-UP BOOKS (Random House)](https://uspto.report/TM/72213888)

## Human sign-off

human_signoff: Mouhamad 2026-08-13

Recorded from the owner's explicit instruction in session on 2026-08-13: "human_signoff: <who> :
it is me:: Mouhamad. sign it". The agent transcribed the owner's own words; it did not originate
the clearance.

Scope of what the owner signed off, stated so it cannot be over-read later: the search result
above — no conflict found across indexed USPTO mirrors, classes 9/16/41, on the descriptive term
`graded reader`. The final title, subtitle, series name, imprint and pen name did not exist when
this was signed, so **this sign-off does not cover them**, and stage 6 must re-run the screen and
obtain a second sign-off against the actual marks used.

---

## Stage 6 final-mark screen — preliminary, incomplete

**Screen date:** 2026-08-14  
**Status:** `INCOMPLETE — do not treat as clearance`  
**Initial KDP series:** none  
**Initial bespoke imprint:** none

### Exact marks and identity checks

| Mark | Role | Observed result |
|---|---|---|
| `The Letter at Puerto Lento` | selected title | Exact-name indexed web search surfaced no clear competing book title in the accessible results. Justia mirror search was blocked by Cloudflare and was not bypassed. No legal clearance claimed. |
| `10 Linked Spanish Stories for Adult Learners (A2 Graded Reader)` | selected subtitle | Predominantly descriptive wording. No separate conflict surfaced in the limited accessible checks. No legal clearance claimed. |
| `Avery Calder` | owner-proposed pen name | **REJECTED.** Both final Luna and Terra reviews independently found an active author identity, books, and author pages under the exact name, creating retail-search and attribution collision risk. |
| `Mara Ellison` | backup pen-name candidate | **REJECTED.** Accessible search surfaced active Amazon, Goodreads, retail, and other author footprints under the exact name. |
| `Julian Mercer` | backup pen-name candidate | **REJECTED.** Open Library surfaced active exact-name author records. |
| `Nina Marlow` | current replacement screening candidate | Accessible Open Library, Goodreads, and exact-name web checks surfaced no clear exact author collision. Google Books API returned shared-quota `429`; Justia returned Cloudflare `403`; those failures are limitations, not clean results. |
| `Puerto Lento Spanish Readers` | prospective future umbrella only | Not launch metadata. Exact-name indexed search produced no useful competing result, but Justia was blocked. Must be screened again if and when a second validated title makes the umbrella real. |

### Coverage limitations

- Justia exact-mark searches returned Cloudflare `403`; no challenge was bypassed.
- Google Books API returned shared-project quota `429`; no result was inferred.
- Bing exact-match quality was inconsistent and sometimes returned irrelevant localized results.
- Goodreads author search pages exposed no clear `Nina Marlow` result, but logged-out rendering is limited.
- Open Library is a catalog signal, not a trademark register or complete marketplace index.
- No official live USPTO, WIPO, EUIPO, or Amazon catalog clearance was obtained.

### Required second sign-off

`Nina Marlow` is a **candidate**, not a cleared mark. Before `manifest.yaml.pen_name` changes, the owner must either:

1. accept the documented limited screen and sign the exact selected marks; or
2. provide a stronger human/browser-assisted search result; or
3. select another name and repeat the screen.

human_signoff_stage6: PENDING

## Exact approved pen-name addendum — 2026-08-15

The owner approved the exact spelling **`Nina Marlo`**. Fresh quoted-name web, Amazon-books,
Goodreads-author, and general author/writer searches found no clear active publishing identity under
that exact name in accessible results. One historical bookseller result credits a `Nina Marlo` in a
1951 Spanish theatre programme; this is not an active contemporary author collision. Search-index
coverage remains incomplete, so this is practical collision screening rather than legal clearance.

human_signoff_stage6: APPROVED_NINA_MARLO_2026-08-15

## Comparative pen-name re-screen — 2026-08-15

**Decision:** retain **`Nina Marlo`**; reject **`Nina Marlow`** for this publishing identity.

The owner requested a second comparison after observing that `Nina Marlo` has fewer Google results
and that `Nina Marlow` has several social profiles. Terra, Luna, and the primary reviewer ran
independent exact-name screens and reached the same recommendation: **`Nina Marlo`**.

### Evidence considered

| Surface | `Nina Marlo` | `Nina Marlow` | Decision impact |
|---|---|---|---|
| Book and author catalogs | No clear exact active author identity surfaced in accessible Amazon, Open Library, Google Books, or Goodreads author checks. A Goodreads reader/reviewer uses the exact name; that is not an author brand. | No clear exact book-author identity surfaced in the same accessible catalog checks. | Neither name receives legal or catalog clearance from an absence of results. |
| Public identity footprint | No corroborated exact-name professional or educational brand surfaced. | Exact-name professional records and a durable `Nina Marlow School of Ballet` / `Nina Marlow Ballet School` footprint surfaced across independent institutional sources. | Material attribution and entity-confusion risk for `Marlow`, especially beside an educational product. |
| Entertainment/search noise | No verified exact-name entertainment identity surfaced. | A *Starfield* character preset and an erotic audiobook character both use the exact name `Nina Marlow`. These are fictional and do not describe any real profile holder. | `Marlow` has denser and less useful search-result competition. |
| Social profiles | No verified exact-name author/social brand surfaced. | Exact-name professional and social profiles surfaced. | Existing real-person profiles increase misattribution risk; their authenticity or content origin was not inferred from appearance. |
| Domain | `ninamarlo.com` is registered and resolved during the check, but returned no useful live page. | `ninamarlow.com` did not resolve during the check; this does not prove availability. | A different owned domain will be needed for `Marlo`; this does not outweigh the identity-collision advantage. |

### Reconciliation

Raw result count is not a quality score. For a new author identity, fewer relevant exact-name results
are useful when they mean less competition for entity recognition. The extra `Nina Marlow` results
belong to unrelated people, organisations, and fictional uses; they do not create transferable
discoverability for this book.

No evidence obtained in this screen establishes that any Instagram account or depicted person is
AI-generated, that its name came from ChatGPT, or that it publishes adult content. Those impressions
are excluded from the decision. The rejection of `Nina Marlow` rests on independently verifiable
identity and brand crowding.

### Practical disposition

- **Use:** `Nina Marlo`, exactly and consistently across cover, interior, EPUB/PDF metadata, and KDP.
- **Do not use:** `Nina Marlow` for this series.
- **Before public launch:** check and reserve a suitable domain and matching social handles; the exact
  `.com` is not assumed available.
- **Boundary:** practical publishing collision screen only; not trademark or legal clearance.

`final_owner_lock: NINA_MARLO_2026-08-15`

The owner explicitly confirmed “I choose Nina Marlo. lock it.” after receiving the reconciled
Terra/Luna/primary recommendation. Reopen the spelling only for a concrete legal, marketplace, or
identity-conflict defect—not for another preference loop.

Sources: [Goodreads exact-name reviewer](https://www.goodreads.com/book/show/242534608-bella-barks-letztes-like);
[Nexus Mods `Nina Marlow` fictional character](https://www.nexusmods.com/starfield/mods/1077);
[Ballet Arizona institutional programme](https://balletaz.org/wp-content/uploads/2025/10/BAZ_Turning-Point-Fall-2025_Web.pdf);
[Master Ballet Academy registration](https://www.masterballetacademy.com/_files/ugd/0a88a0_9d12830c1e5b4bde8545e83145ece509.pdf);
[LinkedIn exact-name profile](https://www.linkedin.com/in/nina-marlow-87437a88);
[Phoenix public campaign record](https://apps-secure.phoenix.gov/CampaignFinance/Reports/RegDocs/a66c31e8-677d-4bb3-8821-16171733aeb5);
[Audible fictional-character listing](https://www.audible.com/es_US/ac/His-Best-Friends-Hot-Mom-Audiolibro/B0F8HYB9V9);
[Verisign RDAP for `ninamarlo.com`](https://rdap.verisign.com/com/v1/domain/ninamarlo.com).
