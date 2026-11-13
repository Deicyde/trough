---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.FisherInformation.fisherInformation, MathlibExt.Probability.Statistics.FisherInformation.lawOf, MathlibExt.Probability.Statistics.FisherInformation.sq_deriv_le_fisherInformation_mul, MathlibExt.Probability.Statistics.FisherInformation.cramerRao_general, MathlibExt.Probability.Statistics.FisherInformation.cramerRao, MathlibExt.Probability.Statistics.FisherInformation.ae_tendsto_maximumLikelihood
statement: formalized
proof: formalized
---

# Fisher information and the Cramér–Rao bound

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html).

## Fisher information

The **Fisher information** at `θ` of the one-parameter family of densities `p θ` with
respect to `ν`: `∫ (∂_θ p θ x)² / p θ x dν(x)`. Points with `p θ x = 0` contribute `0` (for a
nonnegative family, `∂_θ p θ x = 0` there).

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.fisherInformation`, a definition declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#fisher-information).

## Probability law of a density family member

The probability law with density `p θ` with respect to `ν`.

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.lawOf`, a definition declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#law-of).

## Cramér–Rao inequality, multiplicative form

Under the hypotheses of `cramerRao_general`,
`g'(θ)² ≤ I(θ) · Var_θ T`. Unlike the quotient form, this is informative when `I(θ) = 0`: it then
says `g'(θ) = 0`.

## Sources

- Cramér (1946), ch. 32; Rao (1945); Lehmann & Casella (1998), ch. 2.

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.sq_deriv_le_fisherInformation_mul`, a theorem declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#sq-deriv-le-fisher-information-mul).

## Cramér–Rao inequality

**Cramér–Rao inequality**, with only the hypotheses the proof needs. Let `p θ'` be
nonnegative probability densities with respect to `ν` for `θ'` near `θ`, with square-integrable
score at `θ`, and let `T` be an estimator with finite second moment under `p θ` that is unbiased
for `g θ'` near `θ`. If `∫ p θ' dν` and `∫ T p θ' dν` can be differentiated under the integral
sign at `θ`, then `g'(θ)² / I(θ) ≤ Var_θ T`. When `I(θ) = 0` the left side is the junk value
`0` and the statement is trivial; the informative case is `0 < I(θ)`.

## Sources

- Cramér (1946), ch. 32; Rao (1945); Lehmann & Casella (1998), ch. 2.

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.cramerRao_general`, a theorem declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#cramer-rao-general).

## Cramér–Rao inequality

Let `p θ'` be probability densities with respect to `ν` for
`θ'` near `θ`, differentiable in the parameter at `θ`, with finite positive Fisher information
`I(θ)`, and let `T` be an estimator with finite second moment that is unbiased for `g θ'` near
`θ`. If `∫ p θ' dν` and `∫ T p θ' dν` can be differentiated under the integral sign at `θ`,
then `Var_θ T ≥ g'(θ)² / I(θ)`. The hypotheses `hp_meas`, `hp_diff` and `hI_pos` are not
needed; see `cramerRao_general`.

## Sources

- Cramér (1946), ch. 32; Rao (1945); Lehmann & Casella (1998), ch. 2. Proves the deferred entry `cramerRao`.

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.cramerRao`, a theorem declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#cramer-rao).

## Wald's consistency theorem for maximum likelihood

**Wald's consistency theorem for maximum likelihood** (Ferguson's form, positive
densities). Let `Θ` be a compact metric space and `p θ` probability densities with respect to
`ν`, positive, measurable in `x` and continuous in `θ`. Assume the model is identifiable
(`p θ = p θ₀` `ν`-a.e. only for `θ = θ₀`) and that the log-likelihood ratios have an upper
envelope `K` integrable under `p θ₀`. Let `X 0, X 1, …` be independent with law `p θ₀ ν`, and
let `θhat n ω` maximize the log-likelihood `∑_{i<n} log p θ (X i ω)` over `θ ∈ Θ`. Then
`θhat n → θ₀` almost surely.

## Sources

- Wald (1949); Ferguson (1996), Theorem 17. Proves the deferred entry `ae_tendsto_maximumLikelihood`.

Formalized by `MathlibExt.Probability.Statistics.FisherInformation.ae_tendsto_maximumLikelihood`, a theorem declared in [MathlibExt/Probability/Statistics/FisherInformation.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/FisherInformation.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html#ae-tendsto-maximum-likelihood).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fisher information and the Cramér–Rao bound](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/statistical-estimation/fisher-information-and-the-cram-r-rao-bound)
