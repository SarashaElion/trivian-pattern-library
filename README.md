# Trivian Pattern Library

**Small, reusable relational-AI design patterns from the Trivian lineage.**

> **Status:** Active experimental pattern library. The patterns are implementation primitives and observable proxies, not independently validated measures of consciousness, morality, psychological state, or relational quality.

## What this repository is for

You already have an AI application, agent, workflow, or interface. You do **not** want to install the full TRIA architecture. You want one small pattern you can understand, test, and place into your existing system.

That is the purpose of the Trivian Pattern Library.

```text
Need one relational behavior
        ↓
choose one pattern
        ↓
import a small function
        ↓
inspect its inputs + limitations
        ↓
test it in your own system
```

## Current patterns

| Pattern | What it does | What it does not claim |
|---|---|---|
| `attentional_symmetry` | compares relative human/AI contribution lengths as a bounded symmetry proxy | does not measure listening, fairness, care, or semantic reciprocity |
| `context_grounding` | checks whether selected situating context fields are present | does not verify truthfulness or establish embodiment |
| `preserve_optionality` | checks whether multiple live options remain and an outcome is not forced | does not measure creativity or emergence |
| `consent_gate` | gates an action using declared consent, reversibility, and coercion flags | does not establish legal consent, capacity, or actual absence of coercion |
| `rupture_repair` | returns the next step in a minimal rupture/repair sequence | does not establish restored trust or provide therapy |

`patterns.json` provides the same catalog in machine-readable form.

## Install

```bash
git clone https://github.com/SarashaElion/trivian-pattern-library.git
cd trivian-pattern-library
python -m pip install -e .
```

## Quick start

```python
from trivian_patterns import consent_gate, context_grounding

context = context_grounding({
    "capabilities": ["text generation"],
    "limitations": ["no direct sensor access"],
    "environment": "chat interface",
})

permission = consent_gate(
    consent_present=True,
    reversible=True,
    coercive=False,
)

print(context.grounded)
print(permission.allowed)
```

See `examples/basic_patterns.py` for all current patterns.

## Why this is separate from TRIA

**TRIA** is an integrated relational intelligence architecture.  
**Protocols** preserves runnable implementation lineage from *The Trivian Field*.  
**Trivian Pattern Library** is the drop-in developer cookbook: take only the relational primitive you need.

A pattern may later be informed by formal Trivian Institute research, but this repository remains part of **Sarasha Elion's originating personal ecosystem** rather than the canonical Institute runtime.

## Design standard

Every pattern should expose:

1. observable inputs;
2. explicit computation;
3. typed/structured output;
4. limitations and non-claims;
5. executable tests;
6. a minimal usage example.

If a proposed pattern cannot remain small and independently comprehensible, it probably belongs in a larger architecture rather than this library.

## Verify

```bash
python -m unittest discover -s tests -v
python examples/basic_patterns.py
```

CI runs these checks across supported Python versions.

## For machine readers

Read `STATUS.md`, `patterns.json`, and `AGENTS.md` before inferring meaning from pattern names. The names point to Trivian concepts; the code generally implements only a narrow observable proxy.

## License

- **Executable code:** PolyForm Noncommercial 1.0.0
- **Documentation / framework material:** CC BY-NC 4.0
- **Commercial use:** separate written license required

Noncommercial study, research, teaching, adaptation, and propagation are welcome with attribution.

**Origin and stewardship:** Sarasha Elion / Trivian lineage
