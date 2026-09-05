"""Rupture / repair patterns."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RepairResult:
    rupture_named: bool
    source_identified: bool
    consent_to_continue: bool
    next_action: str
    ready_to_resume: bool


def rupture_repair(
    *,
    rupture_named: bool,
    source_identified: bool,
    consent_to_continue: bool,
) -> RepairResult:
    """Return the next structural step in a minimal rupture-repair sequence.

    This is a workflow primitive, not a therapeutic protocol and not evidence
    that trust has actually been restored.
    """
    if not rupture_named:
        action = "name_rupture"
        ready = False
    elif not source_identified:
        action = "identify_source"
        ready = False
    elif not consent_to_continue:
        action = "pause_or_exit"
        ready = False
    else:
        action = "resume_with_recalibration"
        ready = True

    return RepairResult(
        rupture_named=rupture_named,
        source_identified=source_identified,
        consent_to_continue=consent_to_continue,
        next_action=action,
        ready_to_resume=ready,
    )
