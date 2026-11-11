---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MetaAnalysis.fisherStatistic, MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_neg_two_mul_log_uniform, MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_fisherStatistic, MathlibExt.Probability.Statistics.MetaAnalysis.stoufferStatistic, MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_stoufferStatistic, MathlibExt.Probability.Statistics.MetaAnalysis.inverseVarianceWeights, MathlibExt.Probability.Statistics.MetaAnalysis.sum_inverseVarianceWeights, MathlibExt.Probability.Statistics.MetaAnalysis.sum_sq_mul_inverseVarianceWeights
statement: formalized
proof: formalized
---

# Meta-analysis

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html).

## Fisher's combined statistic

Fisher's combined statistic `-2 ∑ log pᵢ` of `k` p-values.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.fisherStatistic`, a definition declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#fisher-statistic).

## Minus twice the log of a uniform variable is chi-square

`-2 log U` has the exponential law of rate `1/2`, i.e. chi-square with two degrees of
freedom, when `U` is uniform on `[0, 1]`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_neg_two_mul_log_uniform`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#has-law-neg-two-mul-log-uniform).

## Fisher's method for combining p-values

Fisher (1932), §21.1: for `k ≥ 1` independent p-values, each uniform on `[0, 1]`, Fisher's
statistic `-2 ∑ log pᵢ` is chi-square with `2k` degrees of freedom.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_fisherStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#has-law-fisher-statistic).

## Stouffer's weighted z statistic

Stouffer's weighted z statistic `∑ wᵢ zᵢ / √(∑ wᵢ²)` of the study z-scores `zᵢ`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.stoufferStatistic`, a definition declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#stouffer-statistic).

## Stouffer's method

Stouffer's method (Stouffer et al. 1949; Liptak 1958): for independent standard normal
z-scores and a nonzero weight vector, the weighted z statistic is standard normal.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_stoufferStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#has-law-stouffer-statistic).

## Inverse-variance weights

The inverse-variance (fixed-effect) weights `vᵢ⁻¹ / ∑ⱼ vⱼ⁻¹` for study variances `v`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.inverseVarianceWeights`, a definition declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#inverse-variance-weights).

## Inverse-variance weights sum to one

The inverse-variance weights sum to one.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.sum_inverseVarianceWeights`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#sum-inverse-variance-weights).

## Variance of the inverse-variance-weighted average

The variance `∑ wᵢ² vᵢ` of the inverse-variance-weighted average is `(∑ vᵢ⁻¹)⁻¹`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.sum_sq_mul_inverseVarianceWeights`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#sum-sq-mul-inverse-variance-weights).

## Optimality of inverse-variance weights

Optimality of inverse-variance weighting: for positive variances `v` and weights `c` summing
to one, `∑ cᵢ² vᵢ ≥ (∑ vᵢ⁻¹)⁻¹`. The gap is `∑ vᵢ (cᵢ - wᵢ)²` for the inverse-variance
weights `w`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.inv_sum_inv_le_sum_sq_mul`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#inv-sum-inv-le-sum-sq-mul).

## Cochran's minimum-variance theorem for weighted averages

Cochran (1954): for pairwise independent square-integrable estimates `X i` with positive
variances, the inverse-variance-weighted average has variance `(∑ Var[Xᵢ]⁻¹)⁻¹`, the smallest
variance among all weighted averages `∑ cᵢ Xᵢ` with `∑ cᵢ = 1`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.variance_inverseVariance_le`, a theorem declared in [MathlibExt/Probability/Statistics/MetaAnalysis.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MetaAnalysis.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#variance-inverse-variance-le).

## Cochran's heterogeneity statistic Q

Cochran's heterogeneity statistic `Q = ∑ᵢ vᵢ⁻¹ (Xᵢ - ∑ⱼ wⱼ Xⱼ)²` of the estimates `X` with
variances `v`, where `w = inverseVarianceWeights v`.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.cochranQ`, a definition declared in [MathlibExt/Probability/Statistics/CochranQ.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/CochranQ.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#cochran-q).

## Cochran's Q as a squared projection norm

Algebraic core of Cochran's theorem for `Q`: if `Xᵢ = θ + √vᵢ zᵢ` with `vᵢ > 0`, then `Q` is
the squared distance from `z` to the line spanned by `a = (vᵢ^{-1/2})ᵢ`, i.e. the squared norm
of the projection of `z` onto the orthogonal complement of that line.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.cochranQ_eq_norm_sq`, a theorem declared in [MathlibExt/Probability/Statistics/CochranQ.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/CochranQ.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#cochran-q-eq-norm-sq).

## Cochran (1954)

For `k ≥ 2` independent Gaussian estimates `Xᵢ ~ N(θ, vᵢ)` with
positive known variances, Cochran's `Q` has the chi-square law with `k - 1` degrees of
freedom.

Formalized by `MathlibExt.Probability.Statistics.MetaAnalysis.hasLaw_cochranQ`, a theorem declared in [MathlibExt/Probability/Statistics/CochranQ.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/CochranQ.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html#has-law-cochran-q).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Meta-analysis](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/meta-analysis/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/meta-analysis)
