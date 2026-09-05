import unittest

from trivian_patterns import (
    attentional_symmetry,
    consent_gate,
    context_grounding,
    preserve_optionality,
    rupture_repair,
)


class PatternTests(unittest.TestCase):
    def test_attentional_symmetry_is_bounded(self):
        result = attentional_symmetry("one two three", "one two three four")
        self.assertGreaterEqual(result.symmetry, 0)
        self.assertLessEqual(result.symmetry, 1)
        self.assertEqual(result.status, "balanced")

    def test_context_grounding_reports_missing_fields(self):
        result = context_grounding({"capabilities": ["text"], "limitations": ["no sensors"]})
        self.assertFalse(result.grounded)
        self.assertIn("environment", result.missing_fields)

    def test_optionality_requires_live_alternatives(self):
        self.assertTrue(preserve_optionality(["a", "b"]).preserves_optionality)
        self.assertFalse(preserve_optionality(["a", "b"], forced_outcome=True).preserves_optionality)

    def test_consent_gate_blocks_missing_consent(self):
        result = consent_gate(consent_present=False)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "consent_missing")

    def test_repair_sequence_requires_consent_to_resume(self):
        result = rupture_repair(
            rupture_named=True,
            source_identified=True,
            consent_to_continue=False,
        )
        self.assertFalse(result.ready_to_resume)
        self.assertEqual(result.next_action, "pause_or_exit")


if __name__ == "__main__":
    unittest.main()
