---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistS, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistMean, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistVariance, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_standardized_eq_gaussianReal, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_dentistS_eq_map_sq, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_dentistS_eq_chiSquare, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistVariance_eq_one_iff, MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistMean_eq_zero_iff
statement: formalized
proof: formalized
---

# Testing LD consistency of association statistics

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html).

## DENTIST-S statistic

The DENTIST-S statistic `(z_i - r z_c) ^ 2 / (1 - r ^ 2)` of a variant with `z`-score `zi`,
given the `z`-score `zc` of the lead (putative causal) variant and the reference correlation `r`
between them (Kanai et al. 2022, Equation 1). Meaningful for `r ^ 2 < 1`; for `r ^ 2 = 1` it is
`0` by the convention `x / 0 = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistS`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#dentist-s).

## Mean of the standardized DENTIST difference

The mean `(ρ - r) λ / √(1 - r²)` of the standardized DENTIST difference when the true
correlation is `ρ`, the reference correlation is `r` and the lead variant has mean `λ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistMean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#dentist-mean).

## Variance of the standardized DENTIST difference

The variance `(1 - 2 r ρ + r²) / (1 - r²)` of the standardized DENTIST difference when the
true correlation is `ρ` and the reference correlation is `r`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistVariance`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#dentist-variance).

## Exact law of the standardized DENTIST difference

Let `(z_i, z_c)` be jointly Gaussian
with unit variances, correlation `ρ` (the covariance, as the variances are `1`), and means
`ρ λ` and `λ`. For a reference correlation `r` with `r ^ 2 < 1`, the standardized difference
`(z_i - r z_c) / √(1 - r²)` is Gaussian with mean `dentistMean ρ r λ` and variance
`dentistVariance ρ r`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_standardized_eq_gaussianReal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#map-standardized-eq-gaussian-real).

## DENTIST-S is chi-squared with one degree of freedom under correct LD

When the reference correlation equals the true correlation `ρ` (`ρ ^ 2 < 1`), the DENTIST-S
statistic has the law of the square of a standard normal variable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_dentistS_eq_map_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#map-dentist-s-eq-map-sq).

## DENTIST-S is exactly `χ²₁` when the reference LD is right

Under the model of
`map_standardized_eq_gaussianReal` with reference correlation equal to the true correlation
`ρ` (`ρ ^ 2 < 1`), the DENTIST-S statistic has the `chiSquareMeasure 1` law, for every value
`λ` of the lead variant's mean.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.map_dentistS_eq_chiSquare`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#map-dentist-s-eq-chi-square).

## Unit-variance criterion for the DENTIST difference

The standardized DENTIST difference has unit variance iff the reference correlation is `0`
or equals the true correlation (for `r ^ 2 < 1`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistVariance_eq_one_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#dentist-variance-eq-one-iff).

## Zero-mean criterion for the DENTIST difference

The standardized DENTIST difference has mean zero iff the reference correlation equals the
true correlation or the lead variant has mean zero (for `r ^ 2 < 1`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDOutlierTest.dentistMean_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LDOutlierTest.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html#dentist-mean-eq-zero-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Testing LD consistency of association statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/testing-ld-consistency-of-association-statistics)
