"""Emergence / optionality-preservation patterns."""

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class OptionalityResult:
    option_count: int
    minimum_options: int
    forced_outcome: bool
    preserves_optionality: bool


def preserve_optionality(
    options: Sequence[object],
    *,
    minimum_options: int = 2,
    forced_outcome: bool = False,
) -> OptionalityResult:
    """Check whether a decision surface preserves more than one live option.

    This is a structural pattern for keeping alternatives available. It does
    not measure novelty, creativity, or emergence itself.
    """
    if minimum_options < 1:
        raise ValueError("minimum_options must be at least 1")
    count = len(options)
    preserved = count >= minimum_options and not forced_outcome
    return OptionalityResult(
        option_count=count,
        minimum_options=minimum_options,
        forced_outcome=forced_outcome,
        preserves_optionality=preserved,
    )
