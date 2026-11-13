---
declaration: section
origin: cited
lean: Matrix.cochran_rank_criterion, ProbabilityTheory.iIndepFun_starProjection_stdGaussian, ProbabilityTheory.iIndepFun_norm_sq_starProjection_stdGaussian, ProbabilityTheory.groupMean, ProbabilityTheory.indepFun_groupMean_residual, ProbabilityTheory.indepFun_sumSqBetween_sumSqWithin, ProbabilityTheory.hasLaw_sampleMean, ProbabilityTheory.iIndepFun_dotProduct_mulVec_pi_gaussianReal
statement: formalized
proof: formalized
---

# Cochran's theorem

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html).

## Rank criterion

**Rank criterion** (Cochran 1934): square matrices `A k` over a field that sum to
the identity have ranks adding up to the size iff they are idempotent and pairwise
annihilating.

Formalized by `Matrix.cochran_rank_criterion`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#cochran-rank-criterion).

## Independence of orthogonal projections of a standard Gaussian

Under the standard Gaussian law, orthogonal projections onto pairwise orthogonal subspaces are
mutually independent.

Formalized by `ProbabilityTheory.iIndepFun_starProjection_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#i-indep-fun-star-projection-std-gaussian).

## Independence of squared lengths of orthogonal Gaussian projections

Under the standard Gaussian law, the squared lengths `‖P_{K k} Z‖²` of the projections onto
pairwise orthogonal subspaces are mutually independent.

Formalized by `ProbabilityTheory.iIndepFun_norm_sq_starProjection_stdGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#i-indep-fun-norm-sq-star-projection-std).

## Group mean of observations

The mean of the observations `x i` with `grp i = g` (`0` for an empty group).

Formalized by `ProbabilityTheory.groupMean`, a definition declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#group-mean).

## Gaussian one-way layout

For i.i.d. `N(μ, v)` observations `xᵢ` labelled by groups
`grp i`, the vector of group means is independent of the vector of within-group residuals
`xᵢ - x̄_{grp i}`.

Formalized by `ProbabilityTheory.indepFun_groupMean_residual`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#indep-fun-group-mean-residual).

## One-way analysis of variance

For i.i.d. `N(μ, v)` observations labelled by groups, the
between-group sum of squares `∑ᵢ (x̄_{grp i} - x̄)²` is independent of the within-group sum of
squares `∑ᵢ (xᵢ - x̄_{grp i})²`.

Formalized by `ProbabilityTheory.indepFun_sumSqBetween_sumSqWithin`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#indep-fun-sum-sq-between-sum-sq-within).

## Law of the Gaussian sample mean

For an i.i.d. sample `X₁, …, Xₙ ~ N(μ, v)` with `n ≥ 1`, the sample mean has the law
`N(μ, v / n)`.

Formalized by `ProbabilityTheory.hasLaw_sampleMean`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#has-law-sample-mean).

## Cochran's theorem

**Cochran's theorem**, independence part: if `Z` has independent standard normal coordinates
and symmetric matrices `A k` sum to the identity with ranks adding up to the dimension, the
quadratic forms `Zᵀ (A k) Z` are mutually independent.

Formalized by `ProbabilityTheory.iIndepFun_dotProduct_mulVec_pi_gaussianReal`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#i-indep-fun-dot-product-mul-vec-pi-gauss).

## Independence of the Gaussian sample mean and residuals

For an i.i.d. sample `X₁, …, Xₙ ~ N(μ, v)`, the sample mean is independent of the residual
vector `(Xᵢ - X̄)ᵢ`.

Formalized by `ProbabilityTheory.indepFun_sampleMean_residual`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#indep-fun-sample-mean-residual).

## Independence of the Gaussian sample mean and sum of squared deviations

For an i.i.d. sample `X₁, …, Xₙ ~ N(μ, v)`, the sample mean `X̄` is independent of the sum of
squared deviations `∑ (Xᵢ - X̄)² = (n - 1) S²`.

Formalized by `ProbabilityTheory.indepFun_sampleMean_sumSqDev`, a theorem declared in [MathlibExt/Probability/Distributions/CochranIndependence.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranIndependence.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#indep-fun-sample-mean-sum-sq-dev).

## Sum of squares of independent standard normals is chi-square

For independent standard normal coordinates, the sum of the squares of the coordinates in a
nonempty finite set `s` has the chi-square law with `|s|` degrees of freedom.

Formalized by `ProbabilityTheory.pi_gaussianReal_map_sum_sq`, a theorem declared in [MathlibExt/Probability/Distributions/CochranTheorem.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranTheorem.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#pi-gaussian-real-map-sum-sq).

## Squared orthonormal coordinates of a standard Gaussian are chi-square

Coordinates of the standard Gaussian law in an orthonormal basis `b`: the sum of the squared
coordinates `⟪b i, x⟫` over a nonempty set `s` of indices is chi-square with `|s|` degrees of
freedom.

Formalized by `ProbabilityTheory.stdGaussian_map_sum_sq_inner`, a theorem declared in [MathlibExt/Probability/Distributions/CochranTheorem.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranTheorem.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#std-gaussian-map-sum-sq-inner).

## Cochran's theorem

**Cochran's theorem**, projection form: for the standard Gaussian law on a
finite-dimensional real inner product space `E` and a subspace `K` of positive dimension, the
squared norm of the orthogonal projection onto `K` is chi-square with `dim K` degrees of
freedom.

Formalized by `ProbabilityTheory.stdGaussian_map_norm_sq_starProjection`, a theorem declared in [MathlibExt/Probability/Distributions/CochranTheorem.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranTheorem.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#std-gaussian-map-norm-sq-star-projection).

## Cochran's theorem

**Cochran's theorem**, matrix form: if `Z` has independent standard normal coordinates and
`A` is a symmetric idempotent matrix of positive rank, the quadratic form `Zᵀ A Z` is
chi-square with `rank A` degrees of freedom.

Formalized by `ProbabilityTheory.pi_gaussianReal_map_dotProduct_mulVec`, a theorem declared in [MathlibExt/Probability/Distributions/CochranTheorem.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/CochranTheorem.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html#pi-gaussian-real-map-dot-product-mul-vec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cochran's theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/cochran-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/linear-models-multivariate/cochran-s-theorem)
