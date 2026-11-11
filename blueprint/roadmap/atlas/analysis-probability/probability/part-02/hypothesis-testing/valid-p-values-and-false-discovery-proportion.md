---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.IsValidPValue, MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_of_hasLaw_uniform, MathlibExt.Probability.Statistics.MultipleTesting.numBelow, MathlibExt.Probability.Statistics.MultipleTesting.numBelow_le, MathlibExt.Probability.Statistics.MultipleTesting.numBelow_mono, MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion, MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion_nonneg, MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion_le_one
statement: formalized
proof: formalized
---

# Valid p-values and false discovery proportion

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html).

## Valid p-value

A real random variable `X` is a *valid* (super-uniform) p-value under `μ` if
`μ {X ≤ t} ≤ t` for every level `t ∈ [0, 1]`. Uniform p-values are the equality case.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.IsValidPValue`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#is-valid-pvalue).

## Uniform p-values are valid

A p-value distributed uniformly on `[0, 1]` is valid.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_of_hasLaw_uniform`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#is-valid-pvalue-of-has-law-uniform).

## Number of p-values below a threshold

The number of p-values that are at most `t`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.numBelow`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#num-below).

## Number of p-values below a threshold is at most the total

At most `m` p-values lie below any threshold.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.numBelow_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#num-below-le).

## Number of p-values below a threshold is monotone

`numBelow p` is monotone in the threshold.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.numBelow_mono`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#num-below-mono).

## False discovery proportion

The false discovery proportion of a rejection set `R` when `H0` is the set of true nulls:
`|R ∩ H0| / max |R| 1` (zero when nothing is rejected).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#false-discovery-proportion).

## False discovery proportion is nonnegative

The false discovery proportion is nonnegative.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#false-discovery-proportion-nonneg).

## False discovery proportion is at most one

The false discovery proportion is at most one.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.falseDiscoveryProportion_le_one`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html#false-discovery-proportion-le-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Valid p-values and false discovery proportion](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/valid-p-values-and-false-discovery-proportion)
