---
declaration: section
origin: cited
lean: ProbabilityTheory.HasMonotoneLikelihoodRatioOn, ProbabilityTheory.HasAntitoneLikelihoodRatioOn, ProbabilityTheory.setIntegral_Ioi_mul_integral_le_of_hasMLR, ProbabilityTheory.setIntegral_Ioi_mul_integral_le_of_hasAntitoneLR, ProbabilityTheory.posteriorTail, ProbabilityTheory.posteriorTail_mono_of_hasMLR, ProbabilityTheory.posteriorTail_anti_of_hasAntitoneLR, ProbabilityTheory.poissonLik
statement: formalized
proof: formalized
---

# Monotone likelihood ratio

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html).

## Monotone likelihood ratio

The likelihood family `L : ℕ → ℝ → ℝ` (observation, parameter) has a **monotone
likelihood ratio** on the parameter set `S`: `L` is nonnegative on `S`, and for
observations `n ≤ m` and parameters `θ ≤ θ'` in `S`,
`L m θ * L n θ' ≤ L n θ * L m θ'` (total positivity of order two). For positive
likelihoods this is monotonicity of `θ ↦ L m θ / L n θ`. The nonnegativity is part of
the predicate: without it the downstream `posteriorTail` would not be a posterior
probability (a signed `L` can give `posteriorTail > 1`).

Formalized by `ProbabilityTheory.HasMonotoneLikelihoodRatioOn`, a definition declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#has-monotone-likelihood-ratio-on).

## Antitone likelihood ratio

The likelihood family has an **antitone likelihood ratio** on `S`: `L` is nonnegative
on `S`, and for `n ≤ m` and `θ ≤ θ'` in `S`, `L n θ * L m θ' ≤ L m θ * L n θ'`.
For positive likelihoods this says `θ ↦ L m θ / L n θ` is nonincreasing (larger counts
favor smaller parameters).

Formalized by `ProbabilityTheory.HasAntitoneLikelihoodRatioOn`, a definition declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#has-antitone-likelihood-ratio-on).

## Posterior stochastic ordering, cross-multiplied form

**Posterior stochastic ordering, cross-multiplied form** (Milgrom 1981, Prop. 1). If the
family `L` has a monotone likelihood ratio on a set `S` carrying the prior `μ`
(`μ Sᶜ = 0`), and every `L n` is `μ`-integrable, then for `n ≤ m` and every threshold `t`,
`(∫_{θ > t} L n dμ) (∫ L m dμ) ≤ (∫_{θ > t} L m dμ) (∫ L n dμ)`.

Formalized by `ProbabilityTheory.setIntegral_Ioi_mul_integral_le_of_hasMLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#set-integral-ioi-mul-integral-le-of-has).

## Posterior stochastic ordering for an antitone likelihood ratio, cross-multiplied form

Under the hypotheses of `setIntegral_Ioi_mul_integral_le_of_hasMLR` with the reversed ratio
condition, for `n ≤ m`:
`(∫_{θ > t} L m dμ) (∫ L n dμ) ≤ (∫_{θ > t} L n dμ) (∫ L m dμ)`.

Formalized by `ProbabilityTheory.setIntegral_Ioi_mul_integral_le_of_hasAntitoneLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#set-integral-ioi-mul-integral-le-of-has-2).

## Posterior tail probability

Posterior probability of `{θ > t}` after observing `n`, by Bayes' formula for the prior
`μ` and likelihood `L`: `(∫_{θ > t} L n θ dμ) / ∫ L n θ dμ`. Meaningful when the marginal
likelihood `∫ L n dμ` is positive (otherwise the division returns the junk value `0`), and a
genuine posterior probability only when `L` is nonnegative (as in the MLR predicates:
a signed `L` can give a value outside `[0, 1]`).

Formalized by `ProbabilityTheory.posteriorTail`, a definition declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#posterior-tail).

## The posterior is stochastically nondecreasing in the observation

**The posterior is stochastically nondecreasing in the observation** for an MLR family and
every prior (Milgrom 1981, Prop. 2): if `n ≤ m` and both marginal likelihoods are positive, then
`P(θ > t ∣ n) ≤ P(θ > t ∣ m)` for every `t`.

Formalized by `ProbabilityTheory.posteriorTail_mono_of_hasMLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#posterior-tail-mono-of-has-mlr).

## The posterior is stochastically nonincreasing in the observation

**The posterior is stochastically nonincreasing in the observation** for a family with an
antitone likelihood ratio and every prior: if `n ≤ m` and both marginal likelihoods are
positive, then `P(θ > t ∣ m) ≤ P(θ > t ∣ n)` for every `t`.

Formalized by `ProbabilityTheory.posteriorTail_anti_of_hasAntitoneLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#posterior-tail-anti-of-has-antitone-lr).

## Poisson likelihood

Poisson likelihood with parameter-dependent mean `λ θ`:
`L n θ = e^{-λ θ} λ θ ^ n / (n !)`.

Formalized by `ProbabilityTheory.poissonLik`, a definition declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#poisson-lik).

## Poisson family with monotone mean has monotone likelihood ratio

A Poisson family whose mean is nonnegative and monotone on `S` has a monotone likelihood
ratio on `S`.

Formalized by `ProbabilityTheory.poissonLik_hasMLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#poisson-lik-has-mlr).

## Poisson family with antitone mean has antitone likelihood ratio

A Poisson family whose mean is nonnegative and antitone on `S` has an antitone likelihood
ratio on `S`.

Formalized by `ProbabilityTheory.poissonLik_hasAntitoneLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#poisson-lik-has-antitone-lr).

## Binomial likelihood

Binomial likelihood with `N` trials and parameter-dependent success probability `p θ`:
`L n θ = C(N, n) p θ ^ n (1 - p θ) ^ (N - n)` (zero for `n > N`, since `C(N, n) = 0`).

Formalized by `ProbabilityTheory.binomialLik`, a definition declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#binomial-lik).

## Binomial family has monotone likelihood ratio

A binomial family whose success probability lies in `[0, 1]` and is monotone on `S` has a
monotone likelihood ratio on `S`.

Formalized by `ProbabilityTheory.binomialLik_hasMLR`, a theorem declared in [MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MonotoneLikelihoodRatio.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html#binomial-lik-has-mlr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone likelihood ratio](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/monotone-likelihood-ratio)
