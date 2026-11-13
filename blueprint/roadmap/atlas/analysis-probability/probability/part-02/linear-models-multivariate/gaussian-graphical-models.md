---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.GaussianGraphicalModel.inv_toBlocks₁₁_inv, MathlibExt.Probability.Statistics.GaussianGraphicalModel.partialCorrelation, MathlibExt.Probability.Statistics.GaussianGraphicalModel.partialCorrelation_eq, MathlibExt.Probability.Statistics.GaussianGraphicalModel.rest, MathlibExt.Probability.Statistics.GaussianGraphicalModel.measurable_rest, MathlibExt.Probability.Statistics.GaussianGraphicalModel.condIndepFun_iff_inv_apply_eq_zero, MathlibExt.Probability.Statistics.GaussianGraphicalModel.sampleCov, MathlibExt.Probability.Statistics.GaussianGraphicalModel.sum_dotProduct_mulVec_eq
statement: formalized
proof: formalized
---

# Gaussian graphical models

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html).

## Matrix

## The conditional covariance is the inverse of a precision block

For positive definite `S`
on `ι ⊕ κ`, `S₁₁ - S₁₂ S₂₂⁻¹ S₂₁ = ((S⁻¹)₁₁)⁻¹`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.inv_toBlocks₁₁_inv`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#inv-to-blocks-inv).

## Partial correlation from the conditional covariance

The partial correlation of coordinates `0` and `1` given the `κ`-block, computed from the
conditional covariance `C = S₁₁ - S₁₂ S₂₂⁻¹ S₂₁`: `C₀₁ / √(C₀₀ C₁₁)`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.partialCorrelation`, a definition declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#partial-correlation).

## Partial correlation from the precision matrix

The partial correlation from the precision matrix: `ρ₁₂·rest = -Ω₀₁ / √(Ω₀₀ Ω₁₁)`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.partialCorrelation_eq`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#partial-correlation-eq).

## Conditioning block of a vector

The `κ`-block (the conditioning coordinates) of a vector on `Fin 2 ⊕ κ`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.rest`, a definition declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#rest).

## Measurability of the conditioning block

The `κ`-block is a measurable function of the vector.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.measurable_rest`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#measurable-rest).

## Pairwise Markov property of Gaussian vectors

If `V = (X₀, X₁, Y) ~ N(μ, S)` with `S`
positive definite, then `X₀` and `X₁` are conditionally independent given `Y` iff
`(S⁻¹)₀₁ = 0`. (The standard Borel sample space is the setting of Mathlib's conditional
independence.)

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.condIndepFun_iff_inv_apply_eq_zero`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#cond-indep-fun-iff-inv-apply-eq-zero).

## Sample second-moment matrix

The sample second-moment matrix `m⁻¹ ∑ₛ xₛ xₛᵀ` of `m` observations in `ℝ^ι`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.sampleCov`, a definition declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#sample-cov).

## Sum of sample quadratic forms as a trace

The quadratic forms of a sample add up to `m · tr (S K)`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.sum_dotProduct_mulVec_eq`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#sum-dot-product-mul-vec-eq).

## Gaussian log-likelihood of a precision matrix

The Gaussian log-likelihood objective `log det K - tr (S K)` of a precision matrix `K`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.gaussLogLik`, a definition declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#gauss-log-lik).

## Matrix supported on the edges of a graph

A matrix vanishes off the edges of `G`: `K i j = 0` for distinct non-adjacent `i, j`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.IsSupportedOn`, a definition declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#is-supported-on).

## Dempster's covariance-selection MLE

**Dempster's covariance-selection MLE** (sufficiency): a positive definite `K̂` supported on
`G` whose inverse agrees with `S` on the diagonal and the edges maximizes `log det K - tr (S K)`
over positive definite `K` supported on `G`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.gaussLogLik_le_of_inv_eq_on_graph`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#gauss-log-lik-le-of-inv-eq-on-graph).

## Uniqueness of Dempster's MLE

Under the hypotheses of
`gaussLogLik_le_of_inv_eq_on_graph`, a positive definite `K` supported on `G` with the same
objective value is `K̂`.

Formalized by `MathlibExt.Probability.Statistics.GaussianGraphicalModel.eq_of_gaussLogLik_eq`, a theorem declared in [MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/GaussianGraphicalModel.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html#eq-of-gauss-log-lik-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian graphical models](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/linear-models-multivariate/gaussian-graphical-models)
