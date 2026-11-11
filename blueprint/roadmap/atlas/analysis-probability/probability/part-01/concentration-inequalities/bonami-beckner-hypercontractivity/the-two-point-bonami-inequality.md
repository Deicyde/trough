---
declaration: section
origin: cited
lean: StatMech.Probability.bts_taylor_lower, StatMech.Probability.bts_twoPointScalar
statement: formalized
proof: formalized
---

# The two-point Bonami inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-two-point-bonami-inequality/index.html).

## Taylor lower bound for $(1+t)^q + (1-t)^q$

For `1 ≤ q ≤ 2` and `|t| ≤ 1`, `2 + q(q-1) t² ≤ (1 + t)^q + (1 - t)^q`.

Formalized by `StatMech.Probability.bts_taylor_lower`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTwoPoint.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTwoPoint.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-two-point-bonami-inequality/index.html#bts-taylor-lower).

## Two-point Bonami inequality

The **two-point Bonami inequality** (Bonami 1970; Beckner 1975): for `0 ≤ ρ ≤ 1` and real
`a, b`, with `q = 1 + ρ²`, `a² + ρ² b² ≤ ((|a + b|^q + |a - b|^q) / 2)^(2/q)`, i.e.
`‖a + ρ b x‖₂ ≤ ‖a + b x‖_q` for a uniform random sign `x`.

Formalized by `StatMech.Probability.bts_twoPointScalar`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTwoPoint.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTwoPoint.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-two-point-bonami-inequality/index.html#bts-two-point-scalar).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The two-point Bonami inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-two-point-bonami-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-two-point-bonami-inequality)
