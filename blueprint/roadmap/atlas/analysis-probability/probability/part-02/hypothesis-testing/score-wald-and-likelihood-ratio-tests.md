---
declaration: section
origin: cited
lean: ProbabilityTheory.gaussianReal_map_sq_div, ProbabilityTheory.gaussianReal_map_max_zero_sq, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_scoreStatistic, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_scoreStatistic_of_estimator, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInMeasure_observedInformation, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_waldStatistic, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_waldStatistic_of_estimator, MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInMeasure_two_mul_logLikelihood_sub_sub
statement: formalized
proof: formalized
---

# Score, Wald and likelihood-ratio tests

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html).

## Probability Theory

## Squared normalized Gaussian is chi-square with one degree of freedom

If `Y ~ N(0, v)` with `v ≠ 0`, then `Y² / v ~ χ²₁`.

Formalized by `ProbabilityTheory.gaussianReal_map_sq_div`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#gaussian-real-map-sq-div).

## Law of the positive part squared of a standard normal variable

`max(Z, 0)²` has the
mixture law `½ δ₀ + ½ χ²₁` (chi-bar-square with weights `½, ½`).

Formalized by `ProbabilityTheory.gaussianReal_map_max_zero_sq`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#gaussian-real-map-max-zero-sq).

## Rao's score test, known information

Under the conditions of
`tendstoInDistribution_score` and `0 < I(θ₀)`, the score statistic
`(n^{-1/2} ∑_{i<n} score p θ₀ (X i))² / I(θ₀)` converges in distribution to `χ²₁`.

## Sources

- Rao (1948), one-parameter case; the central limit theorem for the score as in Lehmann & Casella (1998), §6.3.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_scoreStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-score-statistic).

## Rao's score test with an estimated information

As
`tendstoInDistribution_scoreStatistic`, with `I(θ₀)` replaced by any estimators `Î n`
converging to `I(θ₀)` in probability. Where `Î n ω = 0` the statistic takes Lean's value
`x / 0 = 0`; this event has probability tending to `0` because `0 < I(θ₀)`.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_scoreStatistic_of_estimator`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-score-statistic-2).

## Consistency of the observed information

For i.i.d. observations with law `p θ₀ ν`,
if `∂_θ score p θ₀` is measurable and integrable with `E ∂_θ score p θ₀ = -I(θ₀)` (the
information identity), then `-(1/n) ∑_{i<n} ∂_θ score p θ₀ (X i) → I(θ₀)` in probability.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInMeasure_observedInformation`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-measure-observed-information).

## Wald's test

Under the conditions of
`tendstoInDistribution_sqrt_mul_sub_of_likelihoodEquation` (without the normalization
`∫ p θ dν = 1`, which that proof does not use), the Wald statistic `n (θ̂ₙ - θ₀)² I(θ₀)` of a
consistent root `θ̂ₙ` of the likelihood equation converges in distribution to `χ²₁`.

## Sources

- Wald (1943), one-parameter case; the asymptotic normality of `θ̂ₙ` as in Lehmann & Casella (1998), §6.3.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_waldStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-wald-statistic).

## Wald's test with an estimated information

As `tendstoInDistribution_waldStatistic`,
with `I(θ₀)` replaced by any estimators `Î n → I(θ₀)` in probability (for example the observed
information of `tendstoInMeasure_observedInformation`; `I(θ̂ₙ)` also qualifies when
`θ ↦ I(θ)` is continuous at `θ₀`, by the continuous mapping theorem).

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_waldStatistic_of_estimator`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-wald-statistic-o).

## Quadratic expansion of the log-likelihood ratio

Let `θ̂ₙ` be `√n`-consistent
(`√n (θ̂ₙ - θ₀)` converges in distribution) and solve the likelihood equation with probability
tending to one. If on the ball of radius `δ > 0` about `θ₀` the log-likelihood is twice
differentiable in `θ` with `|∂³_θ log p θ x| ≤ M x` for an integrable `M`, and
`∂²_θ log p θ₀` is integrable with mean `-I(θ₀)`, then
`2 (ℓₙ(θ̂ₙ) - ℓₙ(θ₀)) - n (θ̂ₙ - θ₀)² I(θ₀) → 0` in probability, where
`ℓₙ θ = ∑_{i<n} log p θ (X i)`.

The positivity of `p` is not used: the expansion holds for any criterion `log p θ x` with these
derivatives, and the theorems below assume `0 < p θ x`.

## Sources

- the second-order expansion of Wilks (1938); van der Vaart (1998), ch. 16.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInMeasure_two_mul_logLikelihood_sub_sub`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-measure-two-mul-log-likelihoo).

## Wilks' theorem (simple null)

Under the conditions of `tendstoInDistribution_waldStatistic`
and joint measurability of `(θ, x) ↦ p θ x`, the log-likelihood-ratio statistic
`2 (ℓₙ(θ̂ₙ) - ℓₙ(θ₀))`, `ℓₙ θ = ∑_{i<n} log p θ (X i)`, of a consistent root `θ̂ₙ` of the
likelihood equation converges in distribution to `χ²₁`.

## Sources

- Wilks (1938), case of a one-dimensional parameter and a simple null hypothesis; van der Vaart (1998), ch. 16.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_two_mul_logLikelihood_sub`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-two-mul-log-like).

## Wilks' theorem, supremum form

If moreover `θ̂ₙ ω` maximizes the log-likelihood
`ℓₙ θ = ∑_{i<n} log p θ (X i ω)` over all `θ` for every `n` and `ω`, then the
likelihood-ratio statistic `2 (sup_θ ℓₙ θ - ℓₙ θ₀)` converges in distribution to `χ²₁`.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_two_mul_iSup_logLikelihood_sub`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 719](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L719). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-two-mul-i-sup-lo).

## Likelihood ratio on the boundary

**Likelihood ratio on the boundary** (one-sided parameter space `θ ∈ [0, ∞)`, true value
`θ₀ = 0`). Let the model be defined and regular on a ball about `0` as in
`tendstoInDistribution_two_mul_logLikelihood_sub` (so `0` is interior to the domain of the
family, though not to the parameter space), and let `θ̂ₙ` be a consistent root of the
likelihood equation. The statistic `2 (ℓₙ(max θ̂ₙ 0) - ℓₙ(0))` of the estimator projected onto
`[0, ∞)` converges in distribution to the mixture `½ δ₀ + ½ χ²₁`. The projection `max θ̂ₙ 0`
is the restricted maximizer when, for example, `ℓₙ` is concave; that is not assumed here.

## Sources

- Chernoff (1954); van der Vaart (1998), ch. 16.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioTests.tendstoInDistribution_two_mul_logLikelihood_max_zero_sub`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioTests.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html#tendsto-in-distribution-two-mul-log-like-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Score, Wald and likelihood-ratio tests](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing/score-wald-and-likelihood-ratio-tests)
