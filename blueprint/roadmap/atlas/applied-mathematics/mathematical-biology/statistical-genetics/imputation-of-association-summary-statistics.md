---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.imputed, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_sq, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_mul, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_sq_of_normal, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq_of_normal, MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.sigmaOO_transpose
statement: formalized
proof: formalized
---

# Imputation of association summary statistics

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html).

## Summary Imputation

## Second-moment model for summary-statistic imputation

Square-integrable statistics `z_t` (untyped marker) and `z_o` (typed markers) with raw second
moments `𝔼 z_o z_oᵀ = Σ_oo`, `𝔼 z_t z_o = Σ_ot`, `𝔼 z_t² = Σ_tt`. These are the covariances of
the ImpG null model when the statistics are centred.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#model).

## Imputed summary statistic

The imputed statistic `ẑ = wᵀ z_o` with weights `w`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.imputed`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#imputed).

## Second moment of the imputed statistic

`𝔼 ẑ² = wᵀ Σ_oo w`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-imputed-sq).

## Cross moment of the imputed and untyped statistics

`𝔼 ẑ z_t = wᵀ Σ_ot`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-imputed-mul).

## Mean squared imputation error

The mean squared imputation error: `𝔼 (z_t - ẑ)² = Σ_tt - 2 wᵀ Σ_ot + wᵀ Σ_oo w`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-error-sq).

## Second moment of the statistic imputed with ImpG weights

For the ImpG weights (`Σ_oo w = Σ_ot`, i.e. `w = Σ_oo⁻¹ Σ_ot` when `Σ_oo` is invertible) the
imputed statistic has second moment `wᵀ Σ_ot = Σ_to Σ_oo⁻¹ Σ_ot`; for `Σ_tt = 1` this is
`1 -` the linear-prediction residual variance, ImpG's `r²_pred`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_imputed_sq_of_normal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-imputed-sq-of-normal).

## Mean squared error of imputation with ImpG weights

For the ImpG weights (`Σ_oo w = Σ_ot`) the mean squared imputation error is
`Σ_tt - wᵀ Σ_ot = Σ_tt - Σ_to Σ_oo⁻¹ Σ_ot`, the linear-prediction residual variance
(the conditional variance only under the Gaussian ImpG model).

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq_of_normal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-error-sq-of-normal).

## Symmetry of the typed-marker moment matrix

The moment matrix `Σ_oo` is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.sigmaOO_transpose`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#sigma-oo-transpose).

## Excess error of a linear imputation

If `Σ_oo w = Σ_ot`, then for any weights `w'`,
`𝔼 (z_t - w'ᵀ z_o)² = 𝔼 (z_t - wᵀ z_o)² + (w' - w)ᵀ Σ_oo (w' - w)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-error-sq-eq).

## ImpG is the best linear imputation

The weights solving `Σ_oo w = Σ_ot` minimize the mean
squared error `𝔼 (z_t - w'ᵀ z_o)²` over all weights `w'`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_error_sq_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-error-sq-le).

## Normalized imputed statistic

For any weights `w` with `wᵀ Σ_oo w > 0` (for example the
ridge weights solving `(Σ_oo + λ I) w = Σ_ot`), the statistic `ẑ / √(wᵀ Σ_oo w)` has second
moment `1`, so it has unit variance under the centred null.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SummaryImputation.Model.integral_normalized_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SummaryImputation.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html#integral-normalized-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Imputation of association summary statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/imputation-of-association-summary-statistics)
