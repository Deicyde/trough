---
declaration: section
origin: cited
lean: ProbabilityTheory.negBinomialPMF, ProbabilityTheory.betaBinomialPMF, ProbabilityTheory.ascPochhammer_eval_add_eq_sum, ProbabilityTheory.sum_betaBinomialPMF, ProbabilityTheory.hasSum_negBinomialPMF, ProbabilityTheory.sum_negBinomialPMF_mul, ProbabilityTheory.negBinomialPMF_mul_div_eq_betaBinomialPMF, ProbabilityTheory.measure_cond_eq_betaBinomialPMF
statement: formalized
proof: formalized
---

# Negative binomial and beta-binomial distributions

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html).

## Negative binomial mass function with real shape

Negative binomial mass `P(X = k) = r^{(k)} / k! · p ^ r · (1 - p) ^ k` with real shape `r`
(rising factorial `r^{(k)} = (ascPochhammer ℝ k).eval r`) and success probability `p`, using the
real power `p ^ r`. A probability mass function for `r > 0` and `p ∈ (0, 1]`.

Formalized by `ProbabilityTheory.negBinomialPMF`, a definition declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-pmf).

## Beta-binomial mass function

Beta-binomial mass `C(n, k) α^{(k)} β^{(n - k)} / (α + β)^{(n)}` (zero for `k > n`, since
`C(n, k) = 0`). A probability mass function for `α, β > 0`.

Formalized by `ProbabilityTheory.betaBinomialPMF`, a definition declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#beta-binomial-pmf).

## Chu–Vandermonde identity for rising factorials

`(α + β)^{(n)} = ∑_{k ≤ n} C(n, k) α^{(k)} β^{(n - k)}`, for all real `α, β`.

Formalized by `ProbabilityTheory.ascPochhammer_eval_add_eq_sum`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#asc-pochhammer-eval-add-eq-sum).

## Beta-binomial masses sum to one

The beta-binomial masses sum to one for `α, β > 0`.

Formalized by `ProbabilityTheory.sum_betaBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#sum-beta-binomial-pmf).

## Negative binomial masses sum to one

The negative binomial masses sum to one for `r > 0` and `p ∈ (0, 1]` (the binomial series
`∑ₖ r^{(k)} xᵏ / k! = (1 - x)^{-r}` at `x = 1 - p`).

Formalized by `ProbabilityTheory.hasSum_negBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-neg-binomial-pmf).

## Convolution of negative binomial laws with a common `p`

`∑_{k ≤ n} NB(r₁, p)(k) NB(r₂, p)(n - k) = NB(r₁ + r₂, p)(n)` for `p > 0` and all real
shapes.

Formalized by `ProbabilityTheory.sum_negBinomialPMF_mul`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#sum-neg-binomial-pmf-mul).

## Negative binomial splitting

For `r₁, r₂ > 0`, `0 < p < 1` and `k ≤ n`,
`NB(r₁, p)(k) NB(r₂, p)(n - k) / NB(r₁ + r₂, p)(n) = BB(n; r₁, r₂)(k)`; the conditional law of
one component given the total is beta-binomial and does not depend on `p`.

Formalized by `ProbabilityTheory.negBinomialPMF_mul_div_eq_betaBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-pmf-mul-div-eq-beta-binomia).

## Negative binomial splitting for random variables

If `X` and `Y` are independent with
`P(X = j) = NB(r₁, p)(j)` and `P(Y = j) = NB(r₂, p)(j)` for all `j`, where `r₁, r₂ > 0` and
`0 < p < 1`, then `P(X = k ∣ X + Y = n) = BB(n; r₁, r₂)(k)` for `k ≤ n`.

Formalized by `ProbabilityTheory.measure_cond_eq_betaBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomialSplitting.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#measure-cond-eq-beta-binomial-pmf).

## Mean

For `α, β > 0`, `E M = n α / (α + β) = n π`.

Formalized by `ProbabilityTheory.sum_mul_betaBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/BetaBinomial.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaBinomial.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#sum-mul-beta-binomial-pmf).

## Second factorial moment

For `α, β > 0`,
`E[M (M - 1)] = n (n - 1) α (α + 1) / ((α + β) (α + β + 1))`.

Formalized by `ProbabilityTheory.sum_mul_sub_one_betaBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/BetaBinomial.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaBinomial.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#sum-mul-sub-one-beta-binomial-pmf).

## Variance

**Variance** (Dolzhenko–Smith parametrization). For `α, β > 0`, with `π = α / (α + β)` and
`γ = 1 / (α + β + 1)`, `Var M = E M² - (E M)² = n π (1 - π) (1 + (n - 1) γ)`.

Formalized by `ProbabilityTheory.variance_betaBinomial`, a theorem declared in [MathlibExt/Probability/Distributions/BetaBinomial.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaBinomial.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#variance-beta-binomial).

## Mixed Poisson mass function

The mixed Poisson mass function `p(k) = ∫ e^{-λ} λ^k / k! dν(λ)` for a mixing law `ν` of the
rate. It is a probability mass function when `ν` is a probability measure concentrated on
`[0, ∞)`, which the theorems below assume; for such `ν` the integrand lies in `[0, 1]`, so the
integral is never a junk value.

Formalized by `ProbabilityTheory.poissonMixtureReal`, a definition declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real).

## Zero class of a mixed Poisson law

The zero class of a mixed Poisson law is `E e^{-Λ}`.

Formalized by `ProbabilityTheory.poissonMixtureReal_zero`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real-zero).

## Nonnegativity of the mixed Poisson mass function

The mixed Poisson mass function is nonnegative when `ν` is concentrated on `[0, ∞)`.

Formalized by `ProbabilityTheory.poissonMixtureReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real-nonneg).

## Poisson mixture over a point mass is Poisson

The Poisson mixture over a point mass `δ_m` is the Poisson law with mean `m`.

Formalized by `ProbabilityTheory.poissonMixtureReal_dirac`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real-dirac).

## Normalization

For a probability measure `ν` concentrated on `[0, ∞)`, the mixed
Poisson masses sum to one.

Formalized by `ProbabilityTheory.hasSum_poissonMixtureReal`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-poisson-mixture-real).

## Zero inflation by mixing

**Zero inflation by mixing** (Jensen's inequality for `λ ↦ e^{-λ}`). For a probability
measure `ν` with integrable rate, `P(N = 0) = E e^{-Λ} ≥ e^{-E Λ}`, the zero class of the Poisson
law with the same mean.

Formalized by `ProbabilityTheory.exp_neg_integral_le_poissonMixtureReal_zero`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#exp-neg-integral-le-poisson-mixture-real).

## Mean

For a mixing measure `ν` on `[0, ∞)` with integrable rate, `E N = E Λ`
(finiteness of `ν` is not needed for this identity).

Formalized by `ProbabilityTheory.hasSum_mul_poissonMixtureReal`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-mul-poisson-mixture-real).

## Second factorial moment

For a mixing measure `ν` on `[0, ∞)` with square-integrable
rate, `E[N (N - 1)] = E Λ²` (finiteness of `ν` is not needed for this identity).

Formalized by `ProbabilityTheory.hasSum_mul_sub_one_poissonMixtureReal`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-mul-sub-one-poisson-mixture-real).

## Second moment

For a finite mixing measure `ν` on `[0, ∞)` with square-integrable rate,
`E N² = E Λ² + E Λ`.

Formalized by `ProbabilityTheory.hasSum_sq_poissonMixtureReal`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-sq-poisson-mixture-real).

## Variance decomposition

For a probability measure `ν` on `[0, ∞)` with square-integrable
rate, `Var N = E N² - (E N)² = E Λ + Var Λ`: Poisson noise plus the variance of the rate.

Formalized by `ProbabilityTheory.variance_poissonMixture`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#variance-poisson-mixture).

## Squared coefficient of variation

**Squared coefficient of variation** (Brennecke et al. 2013; Svensson 2020). For a
probability measure `ν` on `[0, ∞)` with square-integrable rate and `E Λ > 0`,
`CV²(N) = Var N / (E N)² = 1 / E Λ + Var Λ / (E Λ)² = 1 / E Λ + CV²(Λ)`.

Formalized by `ProbabilityTheory.cv_sq_poissonMixture`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonMixture.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonMixture.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#cv-sq-poisson-mixture).

## Negative binomial mass function with size and mean

The negative binomial mass function with size `θ` and mean `μ`:
`NB(k; θ, μ) = θ⁽ᵏ⁾ / k! · (θ / (θ + μ)) ^ θ · (μ / (θ + μ)) ^ k`, with the rising factorial
`θ⁽ᵏ⁾ = Γ(θ + k) / Γ(θ)` and a real power `(θ / (θ + μ)) ^ θ`. The parameter domain is `θ > 0`,
`μ ≥ 0`; at `μ = 0` it is the point mass at `0`. Outside the domain the formula is not a
probability mass function.

Formalized by `ProbabilityTheory.negBinomialReal`, a definition declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-real).

## Mean parametrization is the canonical `p`-parametrization

For `θ > 0` and `μ ≥ 0`,
`negBinomialReal θ μ` is `negBinomialPMF θ p` at `p = θ / (θ + μ)`, since
`1 - p = μ / (θ + μ)`. The two APIs are the same law; reuse the splitting and
conditioning results proved for `negBinomialPMF` through this equivalence.

Formalized by `ProbabilityTheory.negBinomialReal_eq_negBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-real-eq-neg-binomial-pmf).

## Nonnegativity of the negative binomial mass function

The negative binomial mass function is nonnegative on the parameter domain.

Formalized by `ProbabilityTheory.negBinomialReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-real-nonneg).

## Zero class of the negative binomial law

The zero class of the negative binomial law is `(θ / (θ + μ)) ^ θ`.

Formalized by `ProbabilityTheory.negBinomialReal_zero`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-real-zero).

## Negative binomial law with mean zero is a point mass

With mean `0` the negative binomial law is the point mass at `0`.

Formalized by `ProbabilityTheory.negBinomialReal_mean_zero`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#neg-binomial-real-mean-zero).

## Zero class versus the Poisson law

For `θ > 0` and `μ ≥ 0`,
`P(0) = (θ / (θ + μ)) ^ θ ≥ e^{-μ}`: a negative binomial law puts at least as much mass at zero
as the Poisson law with the same mean.

Formalized by `ProbabilityTheory.exp_neg_le_negBinomialReal_zero`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#exp-neg-le-neg-binomial-real-zero).

## Greenwood–Yule

The Poisson mixture over a Gamma rate of shape `a > 0` and rate `b > 0`
is negative binomial with size `a` and mean `a / b`.

Formalized by `ProbabilityTheory.poissonMixtureReal_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real-gamma-measure).

## Greenwood–Yule, mean form

For `θ, μ > 0`, the Poisson mixture over `Gamma(θ, θ / μ)`
(mean `μ`, variance `μ² / θ`) is `NB(θ, μ)`.

Formalized by `ProbabilityTheory.poissonMixtureReal_gammaMeasure_mean`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#poisson-mixture-real-gamma-measure-mean).

## Normalization

For `θ > 0` and `μ ≥ 0` the negative binomial masses sum to one.
For `μ > 0` this is `hasSum_negBinomialPMF` transported along
`negBinomialReal_eq_negBinomialPMF`, so the mean parametrization shares the canonical
law's normalization instead of re-proving it.

Formalized by `ProbabilityTheory.hasSum_negBinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-neg-binomial-real).

## Mean

For `θ > 0` and `μ ≥ 0` the negative binomial law has mean `μ`.

Formalized by `ProbabilityTheory.hasSum_mul_negBinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-mul-neg-binomial-real).

## Second moment

For `θ > 0` and `μ ≥ 0`, `E N² = μ + μ² / θ + μ²`.

Formalized by `ProbabilityTheory.hasSum_sq_negBinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#has-sum-sq-neg-binomial-real).

## Variance

For `θ > 0` and `μ ≥ 0` the negative binomial law has variance
`μ + μ² / θ`.

Formalized by `ProbabilityTheory.variance_negBinomial`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#variance-neg-binomial).

## Gamma–Poisson conjugacy, posterior

With prior `Λ ~ Gamma(a, b)` (`a, b > 0`) and one
observation `N = k` from `Po(Λ)`, the posterior density (likelihood times prior over the
marginal `NB(k; a, a / b)`) is the `Gamma(a + k, b + 1)` density.

Formalized by `ProbabilityTheory.gammaPDFReal_posterior`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#gamma-pdfreal-posterior).

## Gamma–Poisson conjugacy, posterior predictive

With prior `Λ ~ Gamma(a, b)`
(`a, b > 0`) and counts `N, N'` that are independent `Po(Λ)` given `Λ`,
`P(N' = j | N = k) = P(N = k, N' = j) / P(N = k) = NB(j; a + k, (a + k) / (b + 1))`.

Formalized by `ProbabilityTheory.posterior_predictive_gammaPoisson`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#posterior-predictive-gamma-poisson).

## Net probability flow of the immigration–death chain

The net probability flow into state `n` of the immigration–death chain on `ℕ`, in which
molecules are made at rate `κ` (`n → n + 1`) and each decays at rate `γ` (`n → n - 1` at rate
`γ n`): `(κ p(n - 1) + γ (n + 1) p(n + 1)) - (κ + γ n) p(n)`, with no inflow from below at
`n = 0`. A law `p` is stationary (global balance) iff this flow vanishes for every `n`.

Formalized by `ProbabilityTheory.immigrationDeathFlow`, a definition declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#immigration-death-flow).

## Immigration–death stationary law

For `γ ≠ 0` the Poisson law with mean `κ / γ`
satisfies global balance for the immigration–death chain. The identity holds for all real `κ`;
the chain is meaningful for `κ ≥ 0`, `γ > 0`.

Formalized by `ProbabilityTheory.immigrationDeathFlow_poisson`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#immigration-death-flow-poisson).

## Fano factor of the Poisson law

For mean `m > 0`, `Var N / E N = 1`; in particular the
stationary law of the immigration–death chain has Fano factor `1`.

Formalized by `ProbabilityTheory.fano_poisson`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#fano-poisson).

## Net probability flow of the bursty production–degradation chain

The net probability flow into state `n` of the bursty production–degradation chain:
bursts arrive at rate `κ` and add `B` molecules, `B` geometric with mean `b`,
`P(B = j) = b ^ j / (1 + b) ^ (j + 1)` for `j ≥ 0`; each molecule decays at rate `γ`. A burst
of size `0` changes nothing, so state `n` is left by a burst at rate `κ P(B ≥ 1) = κ b / (1 + b)`.
The flow is `κ ∑_{m < n} p(m) P(B = n - m) + γ (n + 1) p(n + 1) - (κ b / (1 + b) + γ n) p(n)`.

Formalized by `ProbabilityTheory.burstDeathFlow`, a definition declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#burst-death-flow).

## Bursty expression stationary law

**Bursty expression stationary law** (Shahrezaei–Swain). For burst rate `κ > 0`, decay rate
`γ > 0` and mean burst size `b ≥ 0`, the negative binomial law with size `a = κ / γ` (bursts per
lifetime) and mean `a b` satisfies global balance for the bursty production–degradation
chain.

Formalized by `ProbabilityTheory.burstDeathFlow_negBinomial`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#burst-death-flow-neg-binomial).

## Fano factor of bursty expression

For `a > 0` and `b > 0`, the negative binomial law with
size `a` and mean `a b` has `Var N / E N = 1 + b`.

Formalized by `ProbabilityTheory.fano_negBinomial`, a theorem declared in [MathlibExt/Probability/Distributions/NegativeBinomial.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/NegativeBinomial.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html#fano-neg-binomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Negative binomial and beta-binomial distributions](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/discrete/negative-binomial-and-beta-binomial-distribution)
