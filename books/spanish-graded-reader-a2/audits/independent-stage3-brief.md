<task>
  <goal>Independently adversarially audit the complete Spanish A2 graded-reader manuscript and return an evidence-bearing Gate B recommendation. You are the independent last reader: do not trust or copy prior audit conclusions.</goal>
  <current-state>
    Book: books/spanish-graded-reader-a2.
    Stage 2 is complete. A chronology repair changed Story 07's distracting light to an ordinary boat light and made Story 10 occur almost one year after Story 01. Targeted grammar and vocabulary/locale gates pass. Gate B is UNDECIDED because the repair model's own re-audit was invalidated.
  </current-state>
  <read-scope>
    Read CLAUDE.md; books/spanish-graded-reader-a2/constitution.md; manifest.yaml; research/niche.md; outline/outline.md and outline/chapter_01.md through chapter_10.md; all relevant bible files; summaries/chapter_01.summary.md through chapter_10.summary.md and summaries/continuity-report.md; chapters/01-la-carta-sin-dueno.md through chapters/10-la-luz-otra-vez.md; .agents/rules/quality-gates.md; .agents/rules/model-routing.md; .agents/skills/adversarial-editor/SKILL.md.
  </read-scope>
  <independence>
    Do NOT read audits/superseded/ or scores/superseded/. Do not rely on the placeholder audits/structural.md beyond knowing Gate B is currently undecided. Derive findings directly from manuscript and contracts.
  </independence>
  <passes>
    Run distinct passes for: (1) every chapter contract versus delivered content; (2) narrative spine, chapter order, and pacing; (3) redundancy across stories; (4) thin spots or asserted rather than demonstrated turns; (5) cold opening against the niche persona; (6) canon, physical causality, and chronology contradictions. Specifically recheck annual-light chronology across Stories 01, 07, 10 and bible/letters-causal-ledger.md, but do not limit the audit to that issue.
  </passes>
  <gate>Gate B passes only if there are zero open critical structural findings.</gate>
  <report>
    Return a complete proposed audits/structural.md in Markdown. Every finding must include severity critical|major|minor, exact file:line locations, quoted evidence, and a concrete directive plus responsible loopback stage. Include attack passes with no findings, an explicit Gate B PASS/FAIL recommendation, and the required verification block from quality-gates.md. Do not assign numeric scores; scoring is Stage 4.
  </report>
  <do-not-touch>Read-only. Do not edit any repository file. Do not create branches, worktrees, or commits. Do not produce translations, scoring, or packaging work.</do-not-touch>
</task>
