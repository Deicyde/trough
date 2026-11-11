---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.PCA.colMean, MathlibExt.Probability.Statistics.PCA.center, MathlibExt.Probability.Statistics.PCA.sampleCov, MathlibExt.Probability.Statistics.PCA.scores, MathlibExt.Probability.Statistics.PCA.sum_center, MathlibExt.Probability.Statistics.PCA.sampleCov_apply, MathlibExt.Probability.Statistics.PCA.sampleCov_isHermitian, MathlibExt.Probability.Statistics.PCA.sampleCov_posSemidef
statement: formalized
proof: formalized
---

# Principal component analysis

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html).

## Sample covariance

## Sample mean of a data matrix column

The sample mean of column `j` of an `n × p` data matrix (rows are observations). For
`n = 0` it is the junk value `0`.

Formalized by `MathlibExt.Probability.Statistics.PCA.colMean`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#col-mean).

## Column-centered data matrix

The column-centered data matrix `X i j - x̄ⱼ`.

Formalized by `MathlibExt.Probability.Statistics.PCA.center`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#center).

## Unbiased sample covariance matrix

The unbiased sample covariance matrix `(n - 1)⁻¹ (X - x̄)ᵀ (X - x̄)` of an `n × p` data
matrix. The divisor needs `2 ≤ n`; for `n = 1` the factor is the junk value `(0 : ℝ)⁻¹ = 0`
(and for `n = 0` the product is the zero matrix).

Formalized by `MathlibExt.Probability.Statistics.PCA.sampleCov`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sample-cov).

## Principal component scores

The principal-component scores `(X - x̄) w` of the observations along a direction `w`.

Formalized by `MathlibExt.Probability.Statistics.PCA.scores`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#scores).

## Centered columns sum to zero

The centered columns sum to zero (for at least one observation).

Formalized by `MathlibExt.Probability.Statistics.PCA.sum_center`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sum-center).

## Entries of the sample covariance matrix

Entries of the sample covariance matrix:
`Sⱼₖ = (n - 1)⁻¹ ∑ᵢ (Xᵢⱼ - x̄ⱼ)(Xᵢₖ - x̄ₖ)`.

Formalized by `MathlibExt.Probability.Statistics.PCA.sampleCov_apply`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sample-cov-apply).

## Sample covariance matrix is symmetric

The sample covariance matrix is symmetric.

Formalized by `MathlibExt.Probability.Statistics.PCA.sampleCov_isHermitian`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sample-cov-is-hermitian).

## Sample covariance matrix is positive semidefinite

The sample covariance matrix is positive semidefinite (for every `n`).

Formalized by `MathlibExt.Probability.Statistics.PCA.sampleCov_posSemidef`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sample-cov-pos-semidef).

## Trace of the sample covariance is the total sample variance

The trace of the sample covariance matrix is the total sample variance, the sum of the
column sample variances.

Formalized by `MathlibExt.Probability.Statistics.PCA.trace_sampleCov`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#trace-sample-cov).

## Principal component scores have sample mean zero

The scores along any direction have sample mean zero.

Formalized by `MathlibExt.Probability.Statistics.PCA.sum_scores`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sum-scores).

## Sample variance of scores is a quadratic form

The sample variance of the scores along `w` is the quadratic form `wᵀ S w`.

Formalized by `MathlibExt.Probability.Statistics.PCA.sampleVar_scores`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sample-var-scores).

## Eigenvalues of a symmetric matrix in decreasing order

The eigenvalues `λ₀ ≥ λ₁ ≥ ⋯ ≥ λ_{p-1}` of a real symmetric `p × p` matrix, in decreasing
order (Mathlib's `LinearMap.IsSymmetric.eigenvalues` of `Matrix.toEuclideanLin S`).

Formalized by `MathlibExt.Probability.Statistics.PCA.orderedEigenvalues`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#ordered-eigenvalues).

## Ordered orthonormal eigenbasis of a symmetric matrix

An orthonormal eigenbasis of a real symmetric matrix, ordered to match
`orderedEigenvalues`; for a covariance matrix these are the principal axes.

Formalized by `MathlibExt.Probability.Statistics.PCA.orderedEigenbasis`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#ordered-eigenbasis).

## Rayleigh quotient of a matrix

The Rayleigh quotient `wᵀ S w / wᵀ w` of a real matrix (junk value `0` at `w = 0`).

Formalized by `MathlibExt.Probability.Statistics.PCA.rayleigh`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#rayleigh).

## Ordered eigenvalues are decreasing

The ordered eigenvalues are decreasing.

Formalized by `MathlibExt.Probability.Statistics.PCA.orderedEigenvalues_antitone`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#ordered-eigenvalues-antitone).

## Ordered eigenbasis vectors are eigenvectors

The `k`-th basis vector is an eigenvector for the `k`-th eigenvalue.

Formalized by `MathlibExt.Probability.Statistics.PCA.mulVec_orderedEigenbasis`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#mul-vec-ordered-eigenbasis).

## Quadratic form expanded in the ordered eigenbasis

The quadratic form expanded in the ordered eigenbasis: `xᵀ S x = ∑ λᵢ ⟪vᵢ, x⟫²`.

Formalized by `MathlibExt.Probability.Statistics.PCA.dotProduct_mulVec_eq_sum`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#dot-product-mul-vec-eq-sum).

## Ordered eigenvalues sum to the trace

The ordered eigenvalues sum to the trace.

Formalized by `MathlibExt.Probability.Statistics.PCA.sum_orderedEigenvalues`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sum-ordered-eigenvalues).

## Eigenvalues of a positive semidefinite matrix are nonnegative

The eigenvalues of a positive semidefinite matrix are nonnegative.

Formalized by `MathlibExt.Probability.Statistics.PCA.orderedEigenvalues_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#ordered-eigenvalues-nonneg).

## Rayleigh quotient of an eigenvector is its eigenvalue

The Rayleigh quotient of the `k`-th eigenvector is the `k`-th eigenvalue.

Formalized by `MathlibExt.Probability.Statistics.PCA.rayleigh_orderedEigenbasis`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#rayleigh-ordered-eigenbasis).

## Hotelling's characterization of the principal axes

On nonzero directions orthogonal
to the first `k` eigenvectors, the Rayleigh quotient is at most the `k`-th eigenvalue; the bound
is attained at the `k`-th eigenvector (`rayleigh_orderedEigenbasis`).

Formalized by `MathlibExt.Probability.Statistics.PCA.rayleigh_le_of_orthogonal`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#rayleigh-le-of-orthogonal).

## Lower bound on the Rayleigh quotient for orthogonal directions

Dual of `rayleigh_le_of_orthogonal`: on nonzero directions orthogonal to the eigenvectors
after index `k`, the Rayleigh quotient is at least the `k`-th eigenvalue.

Formalized by `MathlibExt.Probability.Statistics.PCA.le_rayleigh_of_orthogonal`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#le-rayleigh-of-orthogonal).

## Courant–Fischer min–max, matrix form

Every subspace of dimension `p - k` contains a
nonzero vector whose Rayleigh quotient is at least `λₖ`.

Formalized by `MathlibExt.Probability.Statistics.PCA.exists_le_rayleigh_of_finrank`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#exists-le-rayleigh-of-finrank).

## Courant–Fischer max–min, matrix form

Every subspace of dimension `k + 1` contains a
nonzero vector whose Rayleigh quotient is at most `λₖ`.

Formalized by `MathlibExt.Probability.Statistics.PCA.exists_rayleigh_le_of_finrank`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#exists-rayleigh-le-of-finrank).

## Proportion of variance explained by principal components

The proportion of total sample variance explained by the first `k` principal components:
`(λ₀ + ⋯ + λ_{k-1}) / tr S` for the sample covariance matrix `S`. The junk value `0` is
returned when the total variance `tr S` is `0` (constant data).

Formalized by `MathlibExt.Probability.Statistics.PCA.varianceExplained`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#variance-explained).

## Proportion of variance explained is nonnegative

The proportion of variance explained is nonnegative.

Formalized by `MathlibExt.Probability.Statistics.PCA.varianceExplained_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#variance-explained-nonneg).

## Proportion of variance explained is at most one

The proportion of variance explained is at most one.

Formalized by `MathlibExt.Probability.Statistics.PCA.varianceExplained_le_one`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#variance-explained-le-one).

## More components explain more variance

Keeping more components explains more variance.

Formalized by `MathlibExt.Probability.Statistics.PCA.varianceExplained_mono`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#variance-explained-mono).

## All components explain all of the variance

All `p` components explain all of the variance, when the total variance is positive.

Formalized by `MathlibExt.Probability.Statistics.PCA.varianceExplained_of_le`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#variance-explained-of-le).

## Right singular vectors of a matrix

Right singular vectors of `A`: an orthonormal eigenbasis of `Aᵀ A`, ordered so that the
`i`-th vector has eigenvalue `σᵢ²` with `σ₀ ≥ σ₁ ≥ ⋯` the singular values.

Formalized by `MathlibExt.Probability.Statistics.PCA.rightSingularBasis`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#right-singular-basis).

## Truncated singular value decomposition

The rank-`k` truncated singular value decomposition `A Vₖ Vₖᵀ = ∑_{i<k} σᵢ uᵢ vᵢᵀ`,
where `Vₖ` collects the first `k` right singular vectors.

Formalized by `MathlibExt.Probability.Statistics.PCA.truncSVD`, a definition declared in [MathlibExt/Probability/Statistics/PCA.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#trunc-svd).

## Rank of the truncated SVD is at most k

The truncated SVD has rank at most `k`.

Formalized by `MathlibExt.Probability.Statistics.PCA.rank_truncSVD_le`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#rank-trunc-svd-le).

## Frobenius error of the truncated SVD

The squared Frobenius error of the truncated SVD is the sum of the discarded squared
singular values.

Formalized by `MathlibExt.Probability.Statistics.PCA.frobenius_sub_truncSVD_sq`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#frobenius-sub-trunc-svd-sq).

## Eckart–Young (Frobenius norm)

Every matrix of rank at most `k` has squared Frobenius
distance from `A` at least the sum of the discarded squared singular values.

Formalized by `MathlibExt.Probability.Statistics.PCA.sum_sq_singularValues_le_frobenius_sub_sq`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#sum-sq-singular-values-le-frobenius-sub).

## Eckart–Young, best-approximation form

The truncated SVD is a best rank-`k` approximation
of `A` in the Frobenius norm: the least squared distance from `A` to a matrix of rank at most `k`
is `∑_{k ≤ i < n} σᵢ²`, attained by `truncSVD A k`.

Formalized by `MathlibExt.Probability.Statistics.PCA.isLeast_frobenius_sub_sq`, a theorem declared in [MathlibExt/Probability/Statistics/PCA.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/PCA.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html#is-least-frobenius-sub-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Principal component analysis](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/principal-component-analysis/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/linear-models-multivariate/principal-component-analysis)
