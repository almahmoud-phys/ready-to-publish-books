# This file is for stage-0 only.
# Human-authored charter used only while running niche-research.

reader_problem: <reader_problem>               # Filled by: human
useful_outcome: <useful_outcome>               # Filled by: human
authority_envelope: <authority_envelope>       # Filled by: human, list what the author has already done and owns
authority_exclusions: <authority_exclusions>   # Filled by: human, explicit topics the author cannot credibly write
allowed_adjacency: [retitle, sub-niche, persona, marketplace]  # Filled by: human during pivot planning
max_pivot_cycles: 3

INVARIANT:
A pivot must preserve reader_problem and authority_envelope and must cite evidence for its new angle.
Failing either means it is not a pivot, it is a different book — stop and hand back to the human.
