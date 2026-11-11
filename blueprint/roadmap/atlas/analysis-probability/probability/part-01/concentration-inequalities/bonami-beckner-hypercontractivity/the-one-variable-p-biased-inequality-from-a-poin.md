---
declaration: section
origin: cited
lean: StatMech.Probability.pih_m, StatMech.Probability.pih_V, StatMech.Probability.pih_KEY, StatMech.Probability.pih_core_of_KEY, StatMech.Probability.pih_two_point_value_of_KEY
statement: formalized
proof: formalized
---

# The one-variable p-biased inequality from a pointwise bound

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html).

## Mean of a p-biased two-valued function

The mean `(1-p) + p z` of the `p`-biased two-valued function with values `1` and `z`.

Formalized by `StatMech.Probability.pih_m`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html#pih-m).

## Variance term in the p-biased inequality

The variance term `4(q-1) p²(1-p)²(z - 1)²`.

Formalized by `StatMech.Probability.pih_V`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html#pih-v).

## Pointwise bound behind the p-biased inequality

The pointwise bound `(q/2) m^(q-2) V ≤ (1-p) + p z^q - m^q` for all `z ≥ 0`, with
`m = pih_m p z`, `V = pih_V p q z`.

Formalized by `StatMech.Probability.pih_KEY`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html#pih-key).

## Pointwise bound implies the one-variable p-biased inequality

The pointwise bound `pih_KEY p q` implies the one-variable inequality `pbt_OneVarCore p q`.

Formalized by `StatMech.Probability.pih_core_of_KEY`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html#pih-core-of-key).

## p-biased two-point inequality from the pointwise bound

The `p`-biased two-point inequality from `pih_KEY p q` and `pih_KEY (1 - p) q`.

Formalized by `StatMech.Probability.pih_two_point_value_of_KEY`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/PBiasedIntegralHC.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html#pih-two-point-value-of-key).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The one-variable p-biased inequality from a pointwise bound](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-one-variable-p-biased-inequality-from-a-poin)
