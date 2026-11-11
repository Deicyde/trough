---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_outcome, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_covariance, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_covariance_of_indepFun, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_variance_div, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_variance, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ratioEstimate, MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivwWeight
statement: formalized
proof: formalized
---

# Mendelian randomization

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html).

## Wald covariance identities in an observational linear moment model

## Linear moment model for instrumental variables

An observational linear moment model: variables `Z`, `X`, `Y` and `U` on a probability
space, all square integrable, with the algebraic decomposition `Y = α + β X + U`.
The residual `U` is an arbitrary observed-variable function. Consequently `outcome_eq` does not
exclude direct effects of `Z` under interventions, and `β` is only the coefficient in this
decomposition. Orthogonality (`Cov(Z, U) = 0`) and nonzero first stage (`Cov(Z, X) ≠ 0`) are
hypotheses of the covariance identities that use them.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#linear-moment-model).

## Covariance with the outcome in a linear moment model

The covariance of any square-integrable variable with the outcome splits along the
observational decomposition: `Cov(V, Y) = β Cov(V, X) + Cov(V, U)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_outcome`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#covariance-outcome).

## Wald ratio identity

The Wald covariance identity: if `Cov(Z, U) = 0` and `Cov(Z, X) ≠ 0`, then
`Cov(Z, Y) / Cov(Z, X) = β`. For a two-valued `Z` the ratio is the grouping estimator of Wald
(1940), the difference of the group means of `Y` over that of `X`. This is a moment-condition
identity, not a formal causal-identification result.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_covariance`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#covariance-div-covariance).

## Wald ratio identity for an instrument independent of the residual

The Wald covariance identity when the instrument is independent of the residual.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_covariance_of_indepFun`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#covariance-div-covariance-of-indep-fun).

## Wald ratio as a ratio of regression slopes

The Wald ratio as a ratio of regression slopes: the slope of `Y` on `Z` divided by the slope
of `X` on `Z` (the form used with SNP–outcome and SNP–exposure associations) is `β`. This is
again an observational moment identity.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_variance_div`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#covariance-div-variance-div).

## Bias of the ordinary least-squares coefficient under confounding

The ordinary least-squares coefficient identity for `Y` on `X` is
`β + Cov(X, U) / Var(X)`, which differs from `β` exactly when `Cov(X, U) ≠ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.LinearMomentModel.covariance_div_variance`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#covariance-div-variance).

## Ratio estimate of a single SNP

The ratio estimate `β̂_{Yj} / β̂_{Xj}` of SNP `j` (Lean's `x / 0 = 0` gives `0` when
`β̂_{Xj} = 0`; such SNPs carry weight `0` in `ivwWeight`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ratioEstimate`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ratio-estimate).

## Inverse-variance weight of a ratio estimate

The first-order inverse-variance weight `w_j = β̂_{Xj}² / σ_j²` of the ratio estimate of SNP
`j`, where `σ_j` is the standard error of `β̂_{Yj}` (Burgess, Butterworth & Thompson 2013).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivwWeight`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw-weight).

## Inverse-variance-weighted estimator

The inverse-variance-weighted (IVW) estimator
`∑ β̂_{Xj} β̂_{Yj} σ_j⁻² / ∑ β̂_{Xj}² σ_j⁻²` (Burgess, Butterworth & Thompson 2013). The
standard errors are positive in the model; it is the junk value `0` if every `β̂_{Xj} = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivw`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw).

## Weighted residual sum of squares through the origin

The weighted residual sum of squares `∑ (β̂_{Yj} - b β̂_{Xj})² / σ_j²` of the regression
through the origin with slope `b`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.weightedSSR`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#weighted-ssr).

## IVW estimator as a weighted mean of ratio estimates

The IVW estimator is the weighted mean of the ratio estimates with weights
`w_j = β̂_{Xj}² / σ_j²`. This holds for all data: a SNP with `β̂_{Xj} = 0` has weight `0` and
contributes nothing to either side.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivw_eq_weightedMean`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw-eq-weighted-mean).

## IVW estimator minimizes the weighted residual sum of squares

The IVW estimator is the weighted least-squares slope through the origin: it minimizes
the weighted residual sum of squares. This holds for all data: if every `β̂_{Xj} = 0` the sum
does not depend on the slope (and `ivw` is the junk value `0`), and a SNP with `σ_j = 0` has
weight `0` on both sides by Lean's `x / 0 = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivw_le_weightedSSR`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw-le-weighted-ssr).

## Positivity of the total IVW weight

The total weight is positive as soon as some SNP has `β̂_{Xj} ≠ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.sum_ivwWeight_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#sum-ivw-weight-pos).

## IVW recovers an exact proportionality coefficient

Without error, IVW recovers the proportionality coefficient: if
`β̂_{Yj} = β β̂_{Xj}` for all `j` and some `β̂_{Xj} ≠ 0`, then the IVW estimate is `β`.
This algebraic statement does not itself give `β` a causal interpretation.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivw_of_proportional`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw-of-proportional).

## Unbiasedness of the IVW estimator

Unbiasedness of IVW (Burgess, Butterworth & Thompson 2013), with the SNP–exposure
associations `β̂_{Xj}` treated as fixed: if `β̂_{Yj} = β β̂_{Xj} + ε_j` with integrable
mean-zero errors, the IVW estimator has mean `β`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.integral_ivw`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#integral-ivw).

## Variance of the IVW estimator

The first-order variance of IVW (Burgess, Butterworth & Thompson 2013): with the
`β̂_{Xj}` fixed and `β̂_{Yj} = β β̂_{Xj} + ε_j`, where the errors are square integrable,
pairwise uncorrelated (for instance independent) and `Var(ε_j) = σ_j²`, the IVW estimator has
variance `(∑ w_j)⁻¹ = (∑ β̂_{Xj}² / σ_j²)⁻¹`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.variance_ivw`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#variance-ivw).

## Weighted mean

The weighted mean `∑ v_j a_j / ∑ v_j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.weightedMean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#weighted-mean).

## Weighted covariance

The weighted covariance `∑ v_j (a_j - ā_v)(b_j - b̄_v) / ∑ v_j`, where `ā_v` and `b̄_v` are
weighted means.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.weightedCov`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#weighted-cov).

## MR-Egger slope

The MR-Egger slope (Bowden, Davey Smith & Burgess 2015): the slope of the weighted linear
regression of `β̂_{Yj}` on `β̂_{Xj}` with an intercept, `Cov_v(β̂_X, β̂_Y) / Var_v(β̂_X)`. The
paper's weights are `v_j = σ_j⁻²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerSlope`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-slope).

## MR-Egger intercept

The MR-Egger intercept `β̂̄_Y - slope · β̂̄_X` (weighted means).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerIntercept`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-intercept).

## Weighted residual sum of squares of a line

The weighted residual sum of squares `∑ v_j (β̂_{Yj} - a - b β̂_{Xj})²` of the line with
intercept `a` and slope `b`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerSSR`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-ssr).

## MR-Egger line is the weighted least-squares line

The MR-Egger line is the weighted least-squares line: for nonnegative weights and `β̂_X`
of nonzero weighted variance (so the total weight is positive and `β̂_X` is not constant on the
support of the weights), it minimizes the weighted residual sum of squares.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerSSR_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-ssr-le).

## MR-Egger slope under pleiotropy

The MR-Egger slope under pleiotropy (Bowden, Davey Smith & Burgess 2015): if the SNP–outcome
associations are `Γ_j = α_j + β γ_j`, with pleiotropic terms `α_j` and SNP–exposure
associations `γ_j`, the Egger slope of `Γ` on `γ` is `β + Cov_v(γ, α) / Var_v(γ)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerSlope_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-slope-eq).

## MR-Egger intercept under pleiotropy

The MR-Egger intercept under pleiotropy: it is the weighted mean pleiotropic effect
`ᾱ_v` minus `Cov_v(γ, α) / Var_v(γ) · γ̄_v`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerIntercept_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-intercept-eq).

## InSIDE identity for MR-Egger

The finite-sample InSIDE identity (Bowden, Davey Smith & Burgess 2015): if the pleiotropic
terms are uncorrelated with the instrument strengths in the weighted sense,
`Cov_v(α, γ) = 0`, the MR-Egger slope is the coefficient `β` and the intercept is the weighted
mean pleiotropic term `ᾱ_v`. This identity alone does not encode a causal interpretation.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.eggerSlope_eq_of_inside`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#egger-slope-eq-of-inside).

## Directional pleiotropy biases the IVW estimator

Directional pleiotropy biases IVW: if `Γ_j = α_j + β γ_j`, the IVW estimate is
`β + ∑ γ_j α_j σ_j⁻² / ∑ γ_j² σ_j⁻²`. For example a common pleiotropic term `α_j = α ≠ 0`
biases IVW whenever `∑ γ_j σ_j⁻² ≠ 0`, whereas a constant `α` satisfies InSIDE, so
`eggerSlope_eq_of_inside` gives MR-Egger slope `β` and intercept `α`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ivw_of_pleiotropy`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#ivw-of-pleiotropy).

## Ratio with a Gaussian denominator has infinite first moment

A ratio with a Gaussian denominator has no first moment (a classical fact, recalled in the
weak-instrument analysis of Burgess & Thompson 2011): if `D ~ N(m, v)` with `v > 0` and `N` is
independent of `D` and not almost surely `0`, then `𝔼|N / D| = ∞`. Applied to the ratio
estimator `β̂_Y / β̂_X` with a normally distributed SNP–exposure estimate `β̂_X`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.lintegral_enorm_div_eq_top`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#lintegral-enorm-div-eq-top).

## Ratio of independent normal variables is not integrable

The ratio of two independent normal variables, the denominator with positive variance and
the numerator not almost surely zero (`(mN, vN) ≠ (0, 0)`), is not integrable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.not_integrable_div_gaussian`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#not-integrable-div-gaussian).

## Compliance types of Angrist, Imbens and Rubin

The four compliance types of Angrist, Imbens & Rubin (1996), determined by the pair of
potential treatments `(D(0), D(1))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.ComplianceType`, an inductive type declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#compliance-type).

## Compliance type of a pair of potential treatments

The compliance type of the potential treatments `(D(0), D(1)) = (d₀, d₁)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.complianceType`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#compliance-type-2).

## Potential-outcomes model with binary instrument and treatment

A potential-outcomes model with a binary instrument and a binary treatment (Imbens &
Angrist 1994; Angrist, Imbens & Rubin 1996): the assigned instrument `Z`, the potential
treatments `D(z)` and the potential outcomes `Y(z, d)`, all measurable. The observed treatment
is `D(Z)` and the observed outcome `Y(Z, D(Z))`. The identifying assumptions (independence,
exclusion, monotonicity, relevance) are separate predicates.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#potential-outcomes).

## Observed treatment in a potential-outcomes model

The observed treatment `D = D(Z)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.observedTreatment`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#observed-treatment).

## Observed outcome in a potential-outcomes model

The observed outcome `Y = Y(Z, D(Z))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.observedOutcome`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#observed-outcome).

## Compliance type of a unit

The compliance type of a unit.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.type`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#type).

## Compliers in a potential-outcomes model

The compliers, `D(0) = 0` and `D(1) = 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.compliers`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 690](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L690). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#compliers).

## Independence assumption for an instrument

Independence (random assignment): the instrument is independent of the vector of all
potential treatments and potential outcomes.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.Independence`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#independence).

## Exclusion restriction for an instrument

Exclusion: the instrument affects the outcome only through the treatment,
`Y(0, d) = Y(1, d)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.Exclusion`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#exclusion).

## Monotonicity assumption (no defiers)

Monotonicity: assignment never decreases the treatment, `D(0) ≤ D(1)`; there are no
defiers.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.Monotonicity`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#monotonicity).

## Mean of a variable within an instrument arm

The mean of `f` in the arm `Z = z`, `𝔼[f | Z = z]`, the expectation under the conditional
measure. It is the junk value `0` when `P(Z = z) = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.armMean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#arm-mean).

## Observed treatment as a 0-1 real variable

The observed treatment as a `0`/`1` real variable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.treated`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#treated).

## Wald instrumental-variable estimand

The Wald (instrumental-variable) estimand
`(𝔼[Y | Z = 1] - 𝔼[Y | Z = 0]) / (𝔼[D | Z = 1] - 𝔼[D | Z = 0])`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.waldEstimand`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#wald-estimand).

## First stage: treatment-rate difference equals complier share

The first stage (Imbens & Angrist 1994): under independence and monotonicity, with both
arms of positive probability, the difference in treatment rates between the arms is the
proportion of compliers.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.armMean_treated_sub`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 795](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L795). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#arm-mean-treated-sub).

## Reduced form: outcome difference is the complier-weighted effect

The reduced form (Imbens & Angrist 1994): under independence, exclusion and monotonicity,
with integrable potential outcomes and both arms of positive probability, the difference in
mean outcomes between the arms is `𝔼[(Y(z, 1) - Y(z, 0)) 1_complier]`, for either `z`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.armMean_outcome_sub`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#arm-mean-outcome-sub).

## Unrestricted algebraic identity behind the LATE theorem

The unrestricted algebraic identity behind LATE. If the complier set has measure zero, both
sides totalize to `0`; therefore this theorem is not an identification or complier-average claim
at that boundary. Use `waldEstimand_eq_late` for the source-faithful result with relevance.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.waldEstimand_eq_late_totalized`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 837](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L837). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#wald-estimand-eq-late-totalized).

## Local average treatment effect theorem

The local average treatment effect theorem (Imbens & Angrist 1994, Theorem 1; Angrist,
Imbens & Rubin 1996): under independence, exclusion, monotonicity and relevance, with integrable
potential outcomes and both arms of positive probability, the Wald estimand is the average
treatment effect among compliers, `𝔼[Y(1) - Y(0) | complier]` (read at either instrument value
`z`, which exclusion makes irrelevant). Relevance is the nonzero complier mass hypothesis; by
`armMean_treated_sub`, it is equivalent here to a nonzero Wald denominator.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MendelianRandomization.PotentialOutcomes.waldEstimand_eq_late`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean, line 852](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/MendelianRandomization.lean#L852). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html#wald-estimand-eq-late).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mendelian randomization](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/mendelian-randomization/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/mendelian-randomization)
