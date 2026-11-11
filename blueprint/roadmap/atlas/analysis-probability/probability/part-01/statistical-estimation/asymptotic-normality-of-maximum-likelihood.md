---
declaration: section
origin: cited
lean: MeasureTheory.tendstoInMeasure_of_tendstoInDistribution_const, MeasureTheory.TendstoInDistribution.mul_tendstoInMeasure_zero, MeasureTheory.tendstoInMeasure_zero_of_abs_le, MathlibExt.Probability.Statistics.MLEAsymptoticNormality.score, MathlibExt.Probability.Statistics.MLEAsymptoticNormality.integral_score_sq, MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_score, MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_sqrt_mul_sub_of_estimatingEquation, MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_sqrt_mul_sub_of_likelihoodEquation
statement: formalized
proof: formalized
---

# Asymptotic normality of maximum likelihood

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html).

## Measure Theory

## Convergence in distribution to a constant implies convergence in probability

If the
random variables `X i` on one probability space converge in distribution to the constant `c`,
then they converge to `c` in probability.

Formalized by `MeasureTheory.tendstoInMeasure_of_tendstoInDistribution_const`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#tendsto-in-measure-of-tendsto-in-distrib).

## Product of a distributionally convergent and a vanishing sequence

A sequence `A i` converging in distribution, times a sequence `η i` converging in
probability to `0`, converges in probability to `0` (a consequence of Slutsky's theorem).

Formalized by `MeasureTheory.TendstoInDistribution.mul_tendstoInMeasure_zero`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#mul-tendsto-in-measure-zero).

## Convergence to zero in probability by domination on likely events

If `|W i| ≤ V i` on events `G i` whose complements have probability tending to `0`, and
`V i` tends to `0` in probability, then `W i` tends to `0` in probability.

Formalized by `MeasureTheory.tendstoInMeasure_zero_of_abs_le`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#tendsto-in-measure-zero-of-abs-le).

## Score function

The **score** `∂_θ log p θ x` of a one-parameter family of densities `p`.

Formalized by `MathlibExt.Probability.Statistics.MLEAsymptoticNormality.score`, a definition declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#score).

## Fisher information is the second moment of the score

For a positive density family, `E_θ [score²] = I(θ)`: the Fisher information of
`FisherInformation.fisherInformation` is the second moment of the score under `p θ ν`.

Formalized by `MathlibExt.Probability.Statistics.MLEAsymptoticNormality.integral_score_sq`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#integral-score-sq).

## Central limit theorem for the score

For i.i.d. observations with law `p θ₀ ν`, a
positive density family differentiable in `θ` at `θ₀`, a measurable score with mean zero and
`∫ score² d(p θ₀ ν) < ∞`, the normalized score `n^{-1/2} ∑_{i<n} score p θ₀ (X i)` converges in
distribution to `N(0, I(θ₀))`.

## Sources

- Lehmann & Casella (1998), §6.3; van der Vaart (1998), ch. 5.

Formalized by `MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_score`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#tendsto-in-distribution-score).

## Asymptotic normality of a consistent root of an estimating equation

**Asymptotic normality of a consistent root of an estimating equation** (one-dimensional
Z-estimator under Cramér-type conditions). Let `X 0, X 1, …` be i.i.d. with law `μX` and let
`ψ θ x` satisfy, for every `x` and every `θ` in the ball of radius `δ > 0` about `θ₀`: `ψ · x`
and `∂_θ ψ · x` are differentiable at `θ`, and `|∂²_θ ψ θ x| ≤ M x` with `M` integrable. Assume
`E ψ θ₀ = 0`, `E ψ θ₀² < ∞`, `∂_θ ψ θ₀` integrable with `E ∂_θ ψ θ₀ ≠ 0`. Let `θhat n` be
estimators that solve `∑_{i<n} ψ θ (X i) = 0` with probability tending to one and converge to
`θ₀` in probability. Then `√n (θhat n - θ₀)` converges in distribution to
`N(0, E ψ θ₀² / (E ∂_θ ψ θ₀)²)`.

## Sources

- van der Vaart (1998), Theorem 5.41 (one-dimensional case, with the third-derivative envelope of Cramér (1946), §33.3); Lehmann & Casella (1998), §6.3.

Formalized by `MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_sqrt_mul_sub_of_estimatingEquation`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#tendsto-in-distribution-sqrt-mul-sub-of).

## Asymptotic normality of consistent roots of the likelihood equation

**Asymptotic normality of consistent roots of the likelihood equation** (Cramér's
conditions). Let `p θ` be positive
densities with respect to `ν`, and on the ball of radius `δ > 0` about `θ₀` let each `p θ` be
measurable with `∫ p θ dν = 1`, so that the family is a statistical model there (as in
`FisherInformation.cramerRao`). The proof uses measurability only at `θ₀` and does not use the
normalization `_hp_int`: the limit theorem holds for roots of any criterion with these
derivatives.
Let `X 0, X 1, …` be i.i.d. with law `p θ₀ ν`. Assume that on the same ball the log-likelihood
`log p θ x` is differentiable in `θ` for every `x` (so that `score p θ x` is its true derivative
there, not Lean's junk value `0` of `deriv` at a nondifferentiable point) and the score
`∂_θ log p θ x` is twice differentiable in `θ` for every `x`, with `|∂³_θ log p θ x| ≤ M x`
for an integrable `M`; that the score `∂_θ log p θ₀` is measurable and square integrable with
mean zero; that `∂²_θ log p θ₀` is measurable and integrable with `E ∂²_θ log p θ₀ = -I(θ₀)`
(the information identity); and that `0 < I(θ₀)`. The two moment identities are what
differentiating `∫ p θ dν = 1` twice under the integral sign gives; they are assumed directly.
Let `θhat n` be estimators that solve the likelihood equation `∑_{i<n} ∂_θ log p θ (X i) = 0`
with probability tending to one and converge to `θ₀` in probability. Then
`√n (θhat n - θ₀) → N(0, 1 / I(θ₀))` in distribution. The roots need not maximize the
likelihood; for a maximum-likelihood estimator, consistency and the likelihood equation must
be established separately (for example, from an interior maximum of a differentiable
likelihood).

## Sources

- Cramér (1946), §33.3; Lehmann & Casella (1998), Theorem 6.3.10; van der Vaart (1998), Theorem 5.41.

Formalized by `MathlibExt.Probability.Statistics.MLEAsymptoticNormality.tendstoInDistribution_sqrt_mul_sub_of_likelihoodEquation`, a theorem declared in [MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MLEAsymptoticNormality.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html#tendsto-in-distribution-sqrt-mul-sub-of-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic normality of maximum likelihood](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/statistical-estimation/asymptotic-normality-of-maximum-likelihood)
