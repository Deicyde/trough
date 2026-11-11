---
declaration: section
origin: cited
lean: StatMech.Probability.vtp_vectorTwoPoint, StatMech.Probability.vtp_hypercontractivity
statement: formalized
proof: formalized
---

# Bonami–Beckner hypercontractivity on the uniform cube

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/bonami-beckner-hypercontractivity-on-the-uniform/index.html).

## Vector two-point inequality for nonnegative noise

The vector two-point inequality holds for `0 ≤ ρ ≤ 1`.

Formalized by `StatMech.Probability.vtp_vectorTwoPoint`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/VectorTwoPoint.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/VectorTwoPoint.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/bonami-beckner-hypercontractivity-on-the-uniform/index.html#vtp-vector-two-point).

## Bonami–Beckner hypercontractive inequality

The **Bonami–Beckner hypercontractive inequality** (Bonami 1970; Beckner 1975): for
`0 ≤ ρ ≤ 1` and `f : (Fin n → Bool) → ℝ`, `‖T_ρ f‖₂ ≤ ‖f‖_(1 + ρ²)` under the uniform measure.

Formalized by `StatMech.Probability.vtp_hypercontractivity`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/VectorTwoPoint.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/VectorTwoPoint.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/bonami-beckner-hypercontractivity-on-the-uniform/index.html#vtp-hypercontractivity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bonami–Beckner hypercontractivity on the uniform cube](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/bonami-beckner-hypercontractivity-on-the-uniform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/bonami-beckner-hypercontractivity-on-the-uniform)
