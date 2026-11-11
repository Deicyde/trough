---
declaration: section
origin: cited
lean: StatMech.Probability.pbt_g, StatMech.Probability.pbt_OneVarCore, StatMech.Probability.pbt_lhs, StatMech.Probability.pbt_two_point_value_of_core
statement: formalized
proof: formalized
---

# The p-biased two-point inequality, reduced to one variable

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html).

## Left side of the one-variable p-biased inequality

`((1-p) + p z)² + 4(q-1) p²(1-p)²(z - 1)²`: the left side of the `p`-biased two-point
inequality at `u = 1`, `v = z`.

Formalized by `StatMech.Probability.pbt_g`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html#pbt-g).

## Statement of the one-variable p-biased inequality

The one-variable `p`-biased inequality: `pbt_g p q z ≤ ((1-p) + p z^q)^(2/q)` for `z ≥ 0`.

Formalized by `StatMech.Probability.pbt_OneVarCore`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html#pbt-one-var-core).

## Left side of the p-biased two-point inequality

The left side `((1-p) u + p v)² + 4(q-1) p²(1-p)²(u - v)²` of the `p`-biased two-point
inequality.

Formalized by `StatMech.Probability.pbt_lhs`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html#pbt-lhs).

## Reduction of the p-biased two-point inequality to one variable

The `p`-biased two-point inequality, assuming the one-variable inequality for `p` and
`1 - p`.

Formalized by `StatMech.Probability.pbt_two_point_value_of_core`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedTwoPoint.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html#pbt-two-point-value-of-core).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The p-biased two-point inequality, reduced to one variable](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality-reduced-to-one)
