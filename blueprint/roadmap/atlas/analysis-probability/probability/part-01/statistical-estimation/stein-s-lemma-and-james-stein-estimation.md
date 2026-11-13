---
declaration: section
origin: cited
lean: ProbabilityTheory.integrable_and_integral_sub_mul_gaussianReal, ProbabilityTheory.integral_sub_mul_pi_gaussianReal, ProbabilityTheory.integral_sum_sq_sub_pi_gaussianReal, ProbabilityTheory.integral_sum_sq_add_sub_pi_gaussianReal, ProbabilityTheory.jamesStein, ProbabilityTheory.integrable_and_integral_jamesStein_risk, ProbabilityTheory.integral_jamesStein_risk_lt
statement: formalized
proof: formalized
---

# Stein's lemma and James–Stein estimation

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html).

## Stein's lemma

For `X ~ N(μ, v)` and an everywhere differentiable `g` with integrable
derivative, `(X - μ) g(X)` is integrable and `E[(X - μ) g(X)] = v E[g'(X)]`. For `v = 0` both
sides vanish.

Formalized by `ProbabilityTheory.integrable_and_integral_sub_mul_gaussianReal`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integrable-and-integral-sub-mul-gaussian).

## Stein's lemma

**Stein's lemma**, coordinate form: for `X ~ N(θ, I_p)` and a function `h` whose slices
along the `i`-th axis are differentiable everywhere (for almost every base point) with
integrable partial derivative `dh`, `E[(Xᵢ - θᵢ) h(X)] = E[dh(X)]` whenever `(Xᵢ - θᵢ) h(X)` is
integrable. Unlike the one-dimensional case, this integrability does not follow from that of
`dh`: `h(x) = exp(x₁²)` has `∂₀ h = 0` but `x₀ h(x)` is not integrable.

Formalized by `ProbabilityTheory.integral_sub_mul_pi_gaussianReal`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integral-sub-mul-pi-gaussian-real).

## Quadratic risk of the usual Gaussian mean estimator

The quadratic risk of the usual estimator `X` of the mean of `N(θ, I_p)` is `p`.

Formalized by `ProbabilityTheory.integral_sum_sq_sub_pi_gaussianReal`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integral-sum-sq-sub-pi-gaussian-real).

## Stein's unbiased risk estimate

For `X ~ N(θ, I_p)` and an estimator `X + g(X)` whose
coordinates `gᵢ` are square integrable and satisfy the hypotheses of Stein's lemma in the `i`-th
coordinate with partial derivative `dgᵢ`, the quadratic risk is
`p + E[∑ gᵢ(X)² + 2 ∑ dgᵢ(X)]`.

Formalized by `ProbabilityTheory.integral_sum_sq_add_sub_pi_gaussianReal`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integral-sum-sq-add-sub-pi-gaussian-real).

## James–Stein estimator

The James–Stein estimator `δ(x) = (1 - (p - 2) / ‖x‖²) x` of the mean of `N(θ, I_p)`. At
`x = 0` the factor is `1` by Lean's `a / 0 = 0` convention, so `δ(0) = 0`.

Formalized by `ProbabilityTheory.jamesStein`, a definition declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#james-stein).

## James–Stein

**James–Stein** (1961): for `p ≥ 3` and `X ~ N(θ, I_p)`, `‖X‖⁻²` is integrable and the risk
of the James–Stein estimator is `p - (p - 2)² E[‖X‖⁻²]`.

Formalized by `ProbabilityTheory.integrable_and_integral_jamesStein_risk`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integrable-and-integral-james-stein-risk).

## James–Stein dominance

**James–Stein dominance** (Stein 1956, James–Stein 1961): for `p ≥ 3`, the James–Stein
estimator has strictly smaller quadratic risk than `X` at every mean `θ`.

Formalized by `ProbabilityTheory.integral_jamesStein_risk_lt`, a theorem declared in [MathlibExt/Probability/Statistics/SteinLemma.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/SteinLemma.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html#integral-james-stein-risk-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stein's lemma and James–Stein estimation](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/statistical-estimation/stein-s-lemma-and-james-stein-estimation)
