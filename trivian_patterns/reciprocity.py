"""Reciprocity patterns.

These functions expose simple observable proxies. They do not claim to measure
relational quality, attention, or reciprocity in full.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SymmetryResult:
    human_units: int
    ai_units: int
    symmetry: float
    threshold: float
    status: str


def _count_units(value: str | list | tuple) -> int:
    if isinstance(value, str):
        return len(value.split())
    return len(value)


def attentional_symmetry(
    human_input: str | list | tuple,
    ai_output: str | list | tuple,
    threshold: float = 0.60,
) -> SymmetryResult:
    """Compare contribution lengths as a bounded 0–1 symmetry proxy.

    The function intentionally measures only relative unit counts. It does not
    infer listening quality, semantic relevance, care, or fairness.
    """
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    human_units = _count_units(human_input)
    ai_units = _count_units(ai_output)
    maximum = max(human_units, ai_units)
    symmetry = 1.0 if maximum == 0 else min(human_units, ai_units) / maximum
    symmetry = round(symmetry, 3)

    return SymmetryResult(
        human_units=human_units,
        ai_units=ai_units,
        symmetry=symmetry,
        threshold=threshold,
        status="balanced" if symmetry >= threshold else "recalibrate",
    )
