---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.map_withDensity_infinitePi_prod, MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInMeasure_logLikelihoodRatio_sub, MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInDistribution_two_mul_logLikelihood_sub_of_triangular, MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInDistribution_two_mul_logLikelihood_sub_local
statement: formalized
proof: formalized
---

# Local power of the likelihood-ratio test

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html).

## Reweighting an infinite product measure by a product density

If `μ.withDensity r` is a
probability measure, then reweighting the product measure `μ^ℕ` by `∏_{i<n} r (xᵢ)` and
projecting onto the first `n` coordinates gives the product measure `(μ.withDensity r)^n`.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.map_withDensity_infinitePi_prod`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html#map-with-density-infinite-pi-prod).

## Local asymptotic normality of the log-likelihood ratio

Suppose that on the ball of
radius `δ > 0` about `θ₀` the log-likelihood `log p θ x` is differentiable in `θ`, the score
`∂_θ log p θ x` is twice differentiable in `θ`, and `|∂³_θ log p θ x| ≤ M x`. Let `Y 0, Y 1, …`
be random variables such that `-(n⁻¹ ∑_{i<n} ∂²_θ log p θ₀ (Y i)) → I` and
`n⁻¹ ∑_{i<n} M (Y i) → c` in probability (laws of large numbers). Then, for the local
parameters `θₙ = θ₀ + h / √n`,
`∑_{i<n} (log p θₙ (Y i) - log p θ₀ (Y i)) - h n^{-1/2} ∑_{i<n} ∂_θ log p θ₀ (Y i)`
converges to `-h² I / 2` in probability.

## Sources

- van der Vaart (1998), Theorem 7.2 (local asymptotic normality), here under Cramér's third-derivative envelope instead of differentiability in quadratic mean.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInMeasure_logLikelihoodRatio_sub`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html#tendsto-in-measure-log-likelihood-ratio).

## Wilks' expansion for a triangular array

Let `X n i` be random variables (row `n` is the
sample of size `n`) and `θ̂ₙ` estimators that solve the likelihood equation
`∑_{i<n} ∂_θ log p θ (X n i) = 0` with probability tending to one and converge to `θ₀` in
probability. Suppose that on the ball of radius `δ > 0` about `θ₀` the log-likelihood is
differentiable in `θ`, the score is twice differentiable, and `|∂³_θ log p θ x| ≤ M x`. Assume
the laws of large numbers `-(n⁻¹ ∑_{i<n} ∂²_θ log p θ₀ (X n i)) → I` with `I > 0` and
`n⁻¹ ∑_{i<n} M (X n i) → c` in probability, and that the normalized score
`n^{-1/2} ∑_{i<n} ∂_θ log p θ₀ (X n i)` converges in distribution to `Y`. Then
`2 (ℓₙ(θ̂ₙ) - ℓₙ(θ₀)) → Y² / I` in distribution, where `ℓₙ θ = ∑_{i<n} log p θ (X n i)`.

No independence or distributional assumption on the rows is made: they enter only through the
three limit hypotheses. The positivity of `p` is not used either: the expansion holds for any
criterion `log p θ x` with these derivatives. For i.i.d. rows with law `p θ₀ ν` this is Wilks'
theorem; under local alternatives it gives the local power
(`tendstoInDistribution_two_mul_logLikelihood_sub_local`).

## Sources

- Wilks (1938); van der Vaart (1998), Theorem 5.41 and ch. 16.

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInDistribution_two_mul_logLikelihood_sub_of_triangular`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html#tendsto-in-distribution-two-mul-log-like).

## Local power of the likelihood-ratio test

Let row `n` of the triangular array
`X n 0, X n 1, …` be i.i.d. with law `p θₙ ν`, `θₙ = θ₀ + h / √n`, under the Cramér conditions
at `θ₀` of `LikelihoodRatioTests.tendstoInDistribution_two_mul_logLikelihood_sub` (all moment
and envelope conditions are under the null law `p θ₀ ν`). If `θ̂ₙ` solves the likelihood
equation for row `n` with probability tending to one and `θ̂ₙ → θ₀` in probability, then
`2 (ℓₙ(θ̂ₙ) - ℓₙ(θ₀))` converges in distribution to the law of `(Z + h √I(θ₀))²`,
`Z ~ N(0, 1)` (noncentral `χ²₁` with noncentrality `h² I(θ₀)`). For `h = 0` this is Wilks'
theorem for a triangular array.

The row `n = 0` is irrelevant for the limit; with Lean's `h / √0 = 0` its law is `p θ₀ ν`, which
makes `p θ₀ ν` a probability measure. No normalization `∫ p θ dν = 1` is assumed otherwise:
the laws `p θₙ ν` are probability measures because they are laws of random variables.

## Sources

- van der Vaart (1998), ch. 16 (local power), via local asymptotic normality (ch. 7) and Le Cam's first and third lemmas (ch. 6).

Formalized by `MathlibExt.Probability.Statistics.LikelihoodRatioLocalPower.tendstoInDistribution_two_mul_logLikelihood_sub_local`, a theorem declared in [MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LikelihoodRatioLocalPower.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html#tendsto-in-distribution-two-mul-log-like-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local power of the likelihood-ratio test](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing/local-power-of-the-likelihood-ratio-test)
