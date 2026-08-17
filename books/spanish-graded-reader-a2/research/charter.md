# This file is for stage-0 only.
# Charter used only while running niche-research.
#
# PROVENANCE OF THIS CHARTER — read before trusting any field.
# The template says "Filled by: human". These fields were drafted by the agent on
# 2026-08-12 under an explicit owner delegation: the owner said "GO. you MUST fill the
# charter instead of me." That is authorization to draft, and it is recorded here rather
# than hidden, because a charter is the one artifact the niche-research loop may not edit
# and must not silently author for itself.
#
# The owner still owns two things no delegation can transfer:
#   1. attesting that the authority envelope below is one they are willing to publish under;
#   2. the trademark human_signoff line, which niche_verdict.py checks separately.
# Until line `owner_attested` below reads a name and date, this charter is DRAFTED, NOT ATTESTED.
owner_attested: Mouhamad 2026-08-13   # Filled by: human only. Blank = drafted, not attested.
# Attested by the owner in session across 2026-08-12/13: "GO. you MUST fill the charter instead of
# me", "proceed in yolo mode", and "it is me:: Mouhamad. sign it". The agent drafted every field
# below; the owner adopted them. Recorded this way so a later reader can tell authorship (agent)
# from accountability (owner) — they are different, and only the second is a signature.

reader_problem: "An adult English speaker who has finished a beginner app or course knows isolated Spanish words and rules but cannot read continuous Spanish for meaning: they stop to translate every sentence, lose the thread, and abandon real Spanish text."

useful_outcome: "The reader finishes a sequence of vocabulary-controlled Spanish stories reading for meaning rather than decoding, inside a declared and bounded vocabulary they can check they have actually acquired, and can move on to longer or less-controlled material without a confidence collapse."  # [OWNER 2026-08-13] was 'A1-controlled ... move on to A2 material'. The volume is A2 (constitution amendment log), so that sentence promised a step the book itself now occupies. The control this book actually enforces is LEXICAL and machine-measured (Gate L); grammar is classified against PCIC, and the wordlist is a frequency proxy, not a CEFR list. 'Vocabulary-controlled' is the claim the evidence supports, and no exit level is promised.

authority_envelope: "Generated track, machine-verified. Claims are limited to (a) Spanish text that passes a version-pinned, reproducible check suite in a companion repository — controlled-vocabulary coverage against a published CEFR/frequency wordlist, morphological and agreement analysis, single-locale consistency, sentence-ID-aligned parallel translation with entailment and independent back-translation checks, and story-integrity checks over names, chronology and answer keys — and (b) pedagogy statements cited to public primary sources (CEFR descriptors, published extensive-reading/graded-reader research). No claim of personal fluency, teaching practice, or lived language-learning experience."

authority_exclusions: "No claim of native or near-native fluency. No teaching credential, certification, or classroom experience. No personal fluency-timeline, learner-outcome, or 'how I learned Spanish' narrative. No promise of a fluency level or timeframe. No medical, clinical, legal, financial, or emergency Spanish. No children's pedagogy or classroom-use claims. No claim of regional authenticity beyond the one declared locale. No pronunciation or audio authority. No claim that any exercise is exam-equivalent or CEFR-certified — the check suite measures conformance to a published wordlist and to level proxies, which is not certification."

allowed_adjacency: [retitle, sub-niche, persona, marketplace]
max_pivot_cycles: 3

# Scope decisions the owner delegated, recorded so a later stage cannot quietly reinterpret them:
# - Locale: exactly one, declared on the cover and enforced by the check suite. Not yet chosen;
#   it is a Stage-0/1 decision and must cite observed shelf evidence, not preference.
# - Series: this book is designed as volume 1. The evidence for entering this shelf at all
#   (docs/discovery-log.md, 2026-08-12) is a series-economics case; a one-off is a weaker bet.
# - Title: copying an occupied incumbent title is banned, exactly as it was for the SQL candidate.
#   "Spanish Short Stories for Beginners" is an occupied incumbent title and must not be copied.

INVARIANT:
A pivot must preserve reader_problem and authority_envelope and must cite evidence for its new angle.
Failing either means it is not a pivot, it is a different book — stop and hand back to the human.
