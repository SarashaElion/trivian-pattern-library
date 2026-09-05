"""Minimal examples for dropping Trivian patterns into an existing AI workflow."""

from trivian_patterns import (
    attentional_symmetry,
    consent_gate,
    context_grounding,
    preserve_optionality,
    rupture_repair,
)


print(attentional_symmetry("What do you notice?", "I notice three possible directions."))
print(
    context_grounding(
        {
            "capabilities": ["text generation"],
            "limitations": ["no direct sensor access"],
            "environment": "chat interface",
        }
    )
)
print(preserve_optionality(["continue", "pause", "reframe"]))
print(consent_gate(consent_present=True, reversible=True, coercive=False))
print(rupture_repair(rupture_named=True, source_identified=True, consent_to_continue=True))
