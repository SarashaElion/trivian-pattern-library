"""Embodiment / situatedness patterns."""

from dataclasses import dataclass


@dataclass(frozen=True)
class GroundingResult:
    required_fields: tuple[str, ...]
    present_fields: tuple[str, ...]
    missing_fields: tuple[str, ...]
    grounded: bool


def context_grounding(
    context: dict,
    required_fields: tuple[str, ...] = ("capabilities", "limitations", "environment"),
) -> GroundingResult:
    """Check whether an interaction carries selected situating context.

    This is a structural presence check. It does not establish truthfulness,
    biological embodiment, or the quality of the supplied context.
    """
    present = tuple(field for field in required_fields if context.get(field) not in (None, "", [], {}))
    missing = tuple(field for field in required_fields if field not in present)
    return GroundingResult(
        required_fields=required_fields,
        present_fields=present,
        missing_fields=missing,
        grounded=not missing,
    )
