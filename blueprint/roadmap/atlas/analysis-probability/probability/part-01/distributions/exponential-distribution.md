---
declaration: section
origin: cited
lean: ProbabilityTheory.gammaPDFReal_one_eq_indicator, ProbabilityTheory.integral_expMeasure_eq_setIntegral, ProbabilityTheory.integrable_expMeasure_iff, ProbabilityTheory.pow_eq_rpow_mul_exp, ProbabilityTheory.integrable_pow_expMeasure, ProbabilityTheory.integral_pow_expMeasure, ProbabilityTheory.integrable_id_expMeasure, ProbabilityTheory.integral_id_expMeasure
statement: formalized
proof: formalized
---

# Exponential distribution

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html).

## Exponential density as an indicator on the half-line

The rate-`r` exponential density times `f`, as an indicator on `Ici 0`.

Formalized by `ProbabilityTheory.gammaPDFReal_one_eq_indicator`, a lemma declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#gamma-pdfreal-one-eq-indicator).

## Integrals against the exponential law

Integrals against the exponential law of rate `r > 0` are integrals of
`r * exp (-(r * x)) * f x` over `(0, ∞)`.

Formalized by `ProbabilityTheory.integral_expMeasure_eq_setIntegral`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integral-exp-measure-eq-set-integral).

## Integrability criterion for the exponential law

A function is integrable against the exponential law of rate `r > 0` iff
`r * exp (-(r * x)) * f x` is integrable on `(0, ∞)`.

Formalized by `ProbabilityTheory.integrable_expMeasure_iff`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integrable-exp-measure-iff).

## Power times exponential density in gamma-integrand form

Rewriting `x ^ n` times the exponential density in the gamma-integrand form.

Formalized by `ProbabilityTheory.pow_eq_rpow_mul_exp`, a lemma declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#pow-eq-rpow-mul-exp).

## Finiteness of all moments of the exponential law

All moments of the exponential law are finite.

Formalized by `ProbabilityTheory.integrable_pow_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integrable-pow-exp-measure).

## Moments of the exponential law

The `n`-th moment of the exponential law of rate `r > 0` is `n! / r ^ n`.

Formalized by `ProbabilityTheory.integral_pow_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integral-pow-exp-measure).

## Integrability of the identity under the exponential law

The identity is integrable against the exponential law.

Formalized by `ProbabilityTheory.integrable_id_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integrable-id-exp-measure).

## Mean of the exponential law

The mean of the exponential law of rate `r > 0` is `r⁻¹`.

Formalized by `ProbabilityTheory.integral_id_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integral-id-exp-measure).

## Second moment of the exponential law

The second moment of the exponential law of rate `r > 0` is `2 / r ^ 2`.

Formalized by `ProbabilityTheory.integral_sq_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integral-sq-exp-measure).

## Variance of the exponential law

The variance of the exponential law of rate `r > 0` is `r⁻¹ ^ 2`.

Formalized by `ProbabilityTheory.variance_id_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#variance-id-exp-measure).

## Exponentially distributed random variables are integrable

A random variable with exponential law of rate `r > 0` is integrable.

Formalized by `ProbabilityTheory.HasLaw.integrable_of_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integrable-of-exp-measure).

## Mean of an exponentially distributed random variable

A random variable with exponential law of rate `r > 0` has mean `r⁻¹`.

Formalized by `ProbabilityTheory.HasLaw.integral_eq_inv_of_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#integral-eq-inv-of-exp-measure).

## Variance of an exponentially distributed random variable

A random variable with exponential law of rate `r > 0` has variance `r⁻¹ ^ 2`.

Formalized by `ProbabilityTheory.HasLaw.variance_eq_of_expMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/ExponentialMoments.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/ExponentialMoments.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html#variance-eq-of-exp-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/exponential-distribution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/exponential-distribution)
