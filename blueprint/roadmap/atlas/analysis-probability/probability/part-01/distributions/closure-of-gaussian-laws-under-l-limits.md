---
declaration: section
origin: cited
lean: ProbabilityTheory.HasGaussianLaw.of_tendsto_eLpNorm_real, ProbabilityTheory.HasGaussianLaw.of_tendsto_eLpNorm, ProbabilityTheory.IsGaussianProcess.of_tendsto_eLpNorm, ProbabilityTheory.tendsto_integral_mul_of_tendsto_eLpNorm
statement: formalized
proof: formalized
---

# Closure of Gaussian laws under L² limits

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html).

## Closure of real Gaussian laws under `L²` limits

If each `X n` is a real Gaussian random
variable and `X n → Y` in `L²(P)`, then `Y` is Gaussian.

Formalized by `ProbabilityTheory.HasGaussianLaw.of_tendsto_eLpNorm_real`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianL2Limit.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianL2Limit.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html#of-tendsto-e-lp-norm-real).

## Closure of Gaussian laws under `L²` limits

If each `X n` is a Gaussian random vector in
a separable Banach space `E` and `X n → Y` in `L²(P)`, then `Y` is Gaussian.

Formalized by `ProbabilityTheory.HasGaussianLaw.of_tendsto_eLpNorm`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianL2Limit.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianL2Limit.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html#of-tendsto-e-lp-norm).

## Closure of Gaussian processes under `L²` limits

If each `X n` is a real Gaussian
process and `X n t → Y t` in `L²(P)` for every `t`, then `Y` is a Gaussian process.

Formalized by `ProbabilityTheory.IsGaussianProcess.of_tendsto_eLpNorm`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianL2Limit.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianL2Limit.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html#of-tendsto-e-lp-norm-2).

## Continuity of the second moment pairing in `L²`

If `X n → Y` and `Z n → W` in `L²(P)`
(all square integrable), then `E[X n Z n] → E[Y W]`.

Formalized by `ProbabilityTheory.tendsto_integral_mul_of_tendsto_eLpNorm`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianL2Limit.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianL2Limit.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html#tendsto-integral-mul-of-tendsto-e-lp-nor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closure of Gaussian laws under L² limits](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/closure-of-gaussian-laws-under-l-limits)
