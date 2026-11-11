---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix, MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix_mul_self, MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix_mul_mul_transpose, MathlibExt.Probability.Statistics.GeneralizedLeastSquares.aitken
statement: formalized
proof: formalized
---

# Generalized least squares

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html).

## Generalized least-squares matrix

The generalized least-squares matrix `(Xᵀ V⁻¹ X)⁻¹ Xᵀ V⁻¹`; `glsMatrix X V *ᵥ y` is the GLS
estimate of `b` in `y = X b + e` with `Cov e = V`.

Formalized by `MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix`, a definition declared in [MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html#gls-matrix).

## Unbiasedness of the generalized least-squares estimator

The GLS estimator is unbiased: `B X = 1` when `Xᵀ V⁻¹ X` is invertible.

Formalized by `MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix_mul_self`, a theorem declared in [MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html#gls-matrix-mul-self).

## Covariance of the generalized least-squares estimator

The covariance of the GLS estimator: `B V Bᵀ = (Xᵀ V⁻¹ X)⁻¹`.

Formalized by `MathlibExt.Probability.Statistics.GeneralizedLeastSquares.glsMatrix_mul_mul_transpose`, a theorem declared in [MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html#gls-matrix-mul-mul-transpose).

## Aitken's theorem

The GLS estimator has minimal covariance among linear unbiased
estimators: for every `A` with `A X = 1`, `A V Aᵀ - B V Bᵀ` is positive semidefinite, where
`B = glsMatrix X V`.

Formalized by `MathlibExt.Probability.Statistics.GeneralizedLeastSquares.aitken`, a theorem declared in [MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GeneralizedLeastSquares.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html#aitken).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized least squares](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/generalized-least-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/linear-models-multivariate/generalized-least-squares)
