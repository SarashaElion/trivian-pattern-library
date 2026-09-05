"""Small, reusable relational-AI design patterns from the Trivian lineage."""

from .embodiment import GroundingResult, context_grounding
from .emergence import OptionalityResult, preserve_optionality
from .non_domination import ConsentGateResult, consent_gate
from .reciprocity import SymmetryResult, attentional_symmetry
from .repair import RepairResult, rupture_repair

__all__ = [
    "SymmetryResult",
    "attentional_symmetry",
    "GroundingResult",
    "context_grounding",
    "OptionalityResult",
    "preserve_optionality",
    "ConsentGateResult",
    "consent_gate",
    "RepairResult",
    "rupture_repair",
]
