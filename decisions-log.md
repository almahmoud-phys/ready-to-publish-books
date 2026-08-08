# Decisions Log — Ready To Publish Books

*Architecture Decision Records. Each entry: decision, contradiction analysis (TRIZ), leverage check (Meadows), rationale, consequences. Status: LOCKED unless noted. Full ADR-001…009 text: see git history (commit d0b21cc) or the Notion Decisions page. Newest entries below.*

---

## ADR-010 — Work environment: self-reconstituting research workspace + book factory + catalog registry

**Status**: ✅ LOCKED (2026-08-08)

**Context**: The repo is for ALL books, not one. We need: where niche tools live, what scripts run them, and how each book is born as a uniform subproject — portable across machines.

**Decision**:

1. **Research workspace lives at `{repo}/.kdp-research/`** — INSIDE the repo root, **git-ignored**. Bootstrapped by `tooling/scripts/research-init.sh` (idempotent): clones/updates KDP Scout, creates an isolated venv, installs the tool + trendspyg, inits config, writes the ledger header. Rationale (founder caveat, accepted): an external `~/kdp-research/` dies when changing machines; the in-repo workspace + init script makes the repo a **self-reconstituting system** — clone on any PC, run one script, the whole research layer rebuilds itself (Meadows LP4 self-organization; TRIZ P25 Self-Service: the system carries its own environment). Only the script + structure contract are committed; the DB/exports/venv are data, never committed. `RTPB_RESEARCH_DIR` remains as an override for exotic setups.

2. **Thin wrapper scripts own the interface** (`tooling/scripts/`): `niche_mine.sh` (autocomplete → ledger, rate-limited), `niche_snapshot.sh` (ASIN snapshot, low-volume tier), `niche_report.sh` (ledger → per-book projection into `books/<slug>/research/`). **Skills never call KDP Scout directly** — they call wrappers (TRIZ P24 Intermediary: swap tools without touching skills).

3. **Every book is born by `tooling/scripts/new-book.sh <slug> "<title>"`** — validates kebab-case + uniqueness, copies `books/_template/`, fills manifest/state/compliance_log, creates the 10 stage dirs (research, outline, bible, chapters, summaries, audits, scores, edits, exports, assets), registers the book in **`books/registry.yaml`**, prints the stage-0 checklist.

4. **`books/registry.yaml` = the catalog ledger** — one entry per book: slug, title, track, stage, verdict (GO/PIVOT/KILL), created, published, book_score, cost_usd. The single glance-view of the whole catalog (LP6 at catalog level — without it, multi-book state lives in the founder's head).

**TRIZ read**: P1 Segmentation (each book an independent subproject) + P6 Universality (one template serves all) + P10 Preliminary Action (the factory builds compliance structure before any content exists) + P24 Intermediary (wrappers decouple skills from tools) + P25 Self-Service (the repo rebuilds its own tooling layer).

**Meadows read**: registry.yaml closes the catalog-level information gap; the git-ignored workspace keeps the market-knowledge stock (ledger) inside the system's boundary but outside its versioned surface — portable because structure is code, data is regenerate-able.

**Uniform book workflow**: `research-init.sh` (once per machine) → `new-book.sh` (once per book) → stage 0 niche-research (wrappers → ledger → niche.md) → HITL gate → stages 1–7 → publish → retrospective → registry updated.
