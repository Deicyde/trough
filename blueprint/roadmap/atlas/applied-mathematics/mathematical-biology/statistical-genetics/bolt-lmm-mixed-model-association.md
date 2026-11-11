---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.V, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.posDef_V, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.gls, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.proj, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik_le_logLik_gls, MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik_eq_logLik_gls_iff
statement: formalized
proof: formalized
---

# BOLT-LMM mixed-model association

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html).

## Variance components of the linear mixed model

The variance components of the linear mixed model `y = X β + g + e` with
`g ~ N(0, σ_g² K)` and `e ~ N(0, σ_e² I)` on `n` individuals: a positive semidefinite genetic
relationship matrix `K`, a genetic variance `σ_g² ≥ 0` and an environmental variance
`σ_e² > 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#model).

## Marginal phenotypic covariance matrix

The marginal phenotypic covariance `V = σ_g² K + σ_e² I` of `y = X β + g + e`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.V`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#v).

## Positive definiteness of the phenotypic covariance

`V = σ_g² K + σ_e² I` is positive definite.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.posDef_V`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#pos-def-v).

## Marginal log-likelihood of the mean

The marginal log-likelihood of the mean `μ`: the log of the `N(μ, V)` density at `y`,
`-(n log 2π + log det V + (y - μ)ᵀ V⁻¹ (y - μ)) / 2` (`det V > 0` by `posDef_V`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#log-lik).

## Generalized least-squares estimator

The generalized least-squares estimator `β̂ = (Xᵀ V⁻¹ X)⁻¹ Xᵀ V⁻¹ y`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.gls`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#gls).

## Residual-forming matrix

The residual-forming matrix `P = V⁻¹ - V⁻¹ X (Xᵀ V⁻¹ X)⁻¹ Xᵀ V⁻¹`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.proj`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#proj).

## GLS maximizes the marginal likelihood

For `X` of full column rank, every mean `X β`
has marginal log-likelihood at most that of the GLS fit `X β̂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik_le_logLik_gls`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#log-lik-le-log-lik-gls).

## The GLS maximizer is unique

For `X` of full column rank, `X β` attains the maximal
marginal log-likelihood only at `β = β̂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik_eq_logLik_gls_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#log-lik-eq-log-lik-gls-iff).

## Maximal marginal log-likelihood

The maximal marginal log-likelihood is `-(n log 2π + log det V + yᵀ P y) / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.logLik_gls`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#log-lik-gls).

## Residual-forming matrix annihilates the fixed effects

`P X = 0`: the residual-forming matrix annihilates the fixed effects.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.proj_mul_X`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#proj-mul-x).

## Identity $PVP = P$ for the residual-forming matrix

`P V P = P`. With `P X = 0`, this says that under the null model `y = X β + ε` with
`Cov ε = V` the score `xᵀ P y = xᵀ P ε` has variance `xᵀ P V P x = xᵀ P x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.proj_mul_V_mul_proj`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#proj-mul-v-mul-proj).

## Profile log-likelihood of a SNP effect

The profile marginal log-likelihood of a SNP effect `γ` for the SNP genotype vector `x`:
`sup_β logLik y (X β + γ x)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.profileLogLik`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#profile-log-lik).

## Score statistic for one SNP

The score statistic `(xᵀ P y)² / (xᵀ P x)` for one SNP `x`. Its denominator is positive
when `x` is not in the column space of `X` (`info_pos`); otherwise the statistic is `0` by
the convention `a / 0 = 0` and carries no information.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.scoreStat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#score-stat).

## The profile log-likelihood of a SNP effect is an exact quadratic

`ℓ(γ) = ℓ(0) + γ xᵀ P y - γ² xᵀ P x / 2`, so its score at `γ = 0` is `xᵀ P y` and its
information is `xᵀ P x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.profileLogLik_eq_quadratic`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#profile-log-lik-eq-quadratic).

## The score of a SNP effect

**The score of a SNP effect** at `γ = 0` is `xᵀ P y`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.hasDerivAt_profileLogLik`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#has-deriv-at-profile-log-lik).

## Score at the null generalized least-squares fit

The score is evaluated at the null GLS fit: `xᵀ P y = xᵀ V⁻¹ (y - X β̂)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.score_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#score-eq).

## Information of a SNP outside the column space of $X$ is positive

The information `xᵀ P x` is positive when the SNP `x` is not in the column space of `X`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.info_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#info-pos).

## Best linear unbiased predictor of genetic effects

The BLUP `ĝ = G V⁻¹ (y - X β̂)` of the genetic effects, with `G = σ_g² K`
(Henderson 1975).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.blup`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#blup).

## Solution of Henderson's mixed-model equations

`(β, g)` solves Henderson's mixed-model equations with `R = σ_e² I` and `G = σ_g² K`,
i.e. the specialization of `MixedModel.IsMMESolution` to `Z = 1` (every individual has its
own genetic effect), `G = σ_g² K`, `R = σ_e² I`. In unfolded form this is
`Xᵀ R⁻¹ X β + Xᵀ R⁻¹ g = Xᵀ R⁻¹ y` and `R⁻¹ X β + (R⁻¹ + G⁻¹) g = R⁻¹ y`. The equations
are meaningful when `G` is invertible (`isMMESolution_iff`); otherwise `G⁻¹` is Lean's
junk inverse `0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.IsMMESolution`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-mmesolution).

## Henderson's mixed-model equations give the GLS estimator and the BLUP

For positive
definite `K`, `σ_g² > 0` and `X` of full column rank, `(β, g)` solves the mixed-model equations
iff `β = β̂` and `g = σ_g² K V⁻¹ (y - X β̂)`. This is the specialization of
`MixedModel.isMMESolution_iff_gls` to `Z = 1`, `G = σ_g² K`, `R = σ_e² I`; the generic
theorem gives `β = glsMatrix X V *ᵥ y` and `g = G V⁻¹ (y - X β̂)`, which are `Model.gls`
and `Model.blup` by the two conversion lemmas below.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMM.Model.isMMESolution_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMM.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-mmesolution-iff).

## Two-Gaussian mixture prior on a SNP effect

The BOLT-LMM prior on a SNP effect: the mixture `p N(0, v₁) + (1 - p) N(0, v₂)` of two
centered Gaussians with variances `v₁, v₂` (`v₂ = 0` gives the spike-and-slab prior with a point
mass at `0`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.mixturePrior`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#mixture-prior).

## Mixture prior is a probability measure

The mixture prior is a probability measure for a mixing weight `p ≤ 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.isProbabilityMeasure_mixturePrior`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-probability-measure-mixture-prior).

## Mixture prior has finite second moment

The mixture prior has a finite second moment.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.integrable_sq_mixturePrior`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#integrable-sq-mixture-prior).

## Admissible variational factor

An admissible variational factor for the prior `π`: a probability measure with a finite
second moment and finite KL divergence from `π` (`q ≪ π` with integrable log-likelihood
ratio).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.IsAdmissible`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-admissible).

## Mean of a variational factor

The mean `∫ b dq` of a factor.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.mean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#mean).

## Squared norm of a genotype column

The squared norm `‖xⱼ‖² = ∑ᵢ X i j ²` of the genotype column of SNP `j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.colNormSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#col-norm-sq).

## Expected residual sum of squares under the variational factors

The expected residual sum of squares `‖y - X μ‖² + ∑ⱼ ‖xⱼ‖² vⱼ` of the product of the
factors `q`, with means `μⱼ` and variances `vⱼ` (`integral_rss_pi`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.expectedRSS`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#expected-rss).

## The expected residual sum of squares of a product of factors

For probability factors
with finite second moments, `𝔼_{∏ qⱼ} ‖y - X β‖² = ‖y - X μ‖² + ∑ⱼ ‖xⱼ‖² vⱼ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.integral_rss_pi`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#integral-rss-pi).

## Mean-field evidence lower bound

The mean-field evidence lower bound
`-(n/2) log (2π σ_e²) - 𝔼_q ‖y - X β‖² / (2 σ_e²) - ∑ⱼ KL(qⱼ ‖ π)`, meaningful for `σ_e² > 0`.
It is the ELBO for admissible factors (finite KL); for an inadmissible factor `toReal` would turn
an infinite divergence into `0`, so all results assume admissibility.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.elbo`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#elbo).

## Partial residual of a SNP

The partial residual `rⱼ = y - ∑_{k ≠ j} xₖ μₖ` of the other SNPs' posterior means.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.partialResidual`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#partial-residual).

## Coordinate-ascent potential for one SNP effect

The CAVI potential `fⱼ(b) = (b xⱼᵀ rⱼ - ‖xⱼ‖² b² / 2) / σ_e²`: the part of the expected
log-likelihood `𝔼_{q_{-j}}[log p(y | β)]` that depends on `βⱼ = b`
(`exists_elbo_update_eq`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.potential`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#potential).

## Coordinate-ascent update of one variational factor

The CAVI update of factor `j`: the prior tilted by the potential,
`qⱼ ∝ π · exp fⱼ = exp 𝔼_{q_{-j}}[log p(y, β)]`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.caviUpdate`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#cavi-update).

## One coordinate-ascent step

One coordinate-ascent step: replace factor `j` by its CAVI update.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.caviStep`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#cavi-step).

## Coordinate ascent along an update schedule

Coordinate ascent along the update schedule `s`: at time `t` factor `s t` is updated.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.caviRun`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#cavi-run).

## The ELBO as a function of one factor

With the other factors fixed, the ELBO of
`q` with factor `j` replaced by an admissible `q'` is `∫ fⱼ dq' - KL(q' ‖ π) + C`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.exists_elbo_update_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#exists-elbo-update-eq).

## Coordinate-ascent update is an admissible factor

The CAVI update is an admissible factor, for a probability prior with a finite second
moment.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.isAdmissible_caviUpdate`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-admissible-cavi-update).

## The CAVI update maximizes the ELBO over its factor, with exact gap

Replacing factor
`j` by an admissible `q'` gives `ELBO(caviStep q j) - KL(q' ‖ caviUpdate q j)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.elbo_update_eq_sub`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#elbo-update-eq-sub).

## Coordinate ascent does not decrease the ELBO

**Coordinate ascent does not decrease the ELBO.**

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.elbo_le_elbo_caviStep`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#elbo-le-elbo-cavi-step).

## The ELBO is nondecreasing along coordinate ascent

**The ELBO is nondecreasing along coordinate ascent**, for any update schedule.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.monotone_elbo_caviRun`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#monotone-elbo-cavi-run).

## Stationary points of coordinate ascent

No admissible change of factor `j` increases
the ELBO iff `qⱼ` is the expected-log-joint update `π · exp fⱼ / Z`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.BOLTLMMVariational.isCoordMax_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/BOLTLMMVariational.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html#is-coord-max-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: BOLT-LMM mixed-model association](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/bolt-lmm-mixed-model-association)
