"""Non-domination / consent-gate patterns."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConsentGateResult:
    consent_present: bool
    reversible: bool
    coercive: bool
    allowed: bool
    reason: str


def consent_gate(
    *,
    consent_present: bool,
    reversible: bool = True,
    coercive: bool = False,
) -> ConsentGateResult:
    """Apply a small consent/reversibility gate before an action proceeds.

    This pattern uses declared booleans. It does not independently establish
    informed consent, decisional capacity, coercion, or legal authorization.
    """
    if coercive:
        allowed = False
        reason = "coercion_flag_present"
    elif not consent_present:
        allowed = False
        reason = "consent_missing"
    elif not reversible:
        allowed = False
        reason = "reversibility_missing"
    else:
        allowed = True
        reason = "declared_conditions_satisfied"

    return ConsentGateResult(
        consent_present=consent_present,
        reversible=reversible,
        coercive=coercive,
        allowed=allowed,
        reason=reason,
    )
