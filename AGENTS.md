# AGENTS.md — harness-agnostic mirror

**Read `CLAUDE.md` first.** It is the single source of truth for pipeline, gates, and rules. This file only adds harness-neutral notes:

- Every skill is a plain markdown file at `.agents/skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`, `model_tier`, `stage`, `context_budget`, `outputs`). Any agent runtime can execute them by following the frontmatter.
- Tool names in skills are generic: `view_file`→Read, `grep_search`→search, `list_dir`→list, `notify_user`→present to user. Map them to your harness.
- Nothing in this repo may halt because a harness-specific file is missing (CEAD portability principle).
- State is files, not memory: `books/<slug>/state.json` is the ledger; `manifest.yaml` is the contract; `compliance_log.yaml` is append-only.
- Model choice is a repo rule, not a harness setting: `.agents/rules/model-routing.md` records which model drafts, which judges, and what each one gets wrong — measured in-repo. No model reviews its own draft; panels need independent model families with thresholds fixed before dispatch.
- If you are not Claude Code: ignore nothing in `CLAUDE.md` — it is harness-agnostic by design.
