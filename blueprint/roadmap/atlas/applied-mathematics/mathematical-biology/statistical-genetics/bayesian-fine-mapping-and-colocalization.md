---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF, MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF_eq, MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF_pos, MathlibExt.Biology.StatisticalGenetics.FineMapping.gaussianReal_eq_withDensity_wakefieldABF, MathlibExt.Biology.StatisticalGenetics.FineMapping.rnDeriv_map_add_ae_eq, MathlibExt.Biology.StatisticalGenetics.FineMapping.olsEffect, MathlibExt.Biology.StatisticalGenetics.FineMapping.olsVar, MathlibExt.Biology.StatisticalGenetics.FineMapping.serCov
statement: formalized
proof: formalized
---

# Bayesian fine-mapping and colocalization

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html).

## Wakefield's approximate Bayes factor

## Wakefield's approximate Bayes factor

Wakefield's approximate Bayes factor: the `N(0, V + W)` density of the estimate `b` (its
marginal law under the alternative `β ~ N(0, W)`) divided by its `N(0, V)` density (the null
`β = 0`). Wakefield (2009) reports the reciprocal, null over alternative; coloc and SuSiE use
this orientation, in which large values favor association. For `V = 0` the null density is
Mathlib's junk value `0` and so is the ratio; the theorems assume `V ≠ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#wakefield-abf).

## Wakefield's closed form

With `z = b / √V`,
`ABF = √(V / (V + W)) · exp (z² W / (2 (V + W)))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#wakefield-abf-eq).

## Positivity of Wakefield's approximate Bayes factor

Wakefield's ABF is strictly positive on its sampling-variance domain.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.wakefieldABF_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#wakefield-abf-pos).

## Wakefield's Bayes factor as a density ratio of Gaussians

The alternative marginal `N(0, V + W)` has density `wakefieldABF V W` with respect to the null
law `N(0, V)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.gaussianReal_eq_withDensity_wakefieldABF`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#gaussian-real-eq-with-density-wakefield).

## The ABF is the Bayes factor

If `β ~ N(0, W)` and the sampling error `ε ~ N(0, V)` are
independent, the law of the estimate `β + ε` (alternative) has density `wakefieldABF V W` with
respect to the law of `ε` (null).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.rnDeriv_map_add_ae_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#rn-deriv-map-add-ae-eq).

## Marginal least-squares effect estimate

The marginal least-squares effect estimate `xᵀ y / xᵀ x` of a variant with genotype vector
`x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.olsEffect`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ols-effect).

## Sampling variance of the least-squares effect estimate

The sampling variance `σ² / xᵀ x` of `olsEffect x y` for residual variance `σ²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.olsVar`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ols-var).

## Covariance of the single-effect regression model

The covariance `σ₀² x xᵀ + σ² I` of `y = x β + e` for `β ~ N(0, σ₀²)` and
`e ~ N(0, σ² I)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.serCov`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ser-cov).

## Single-effect regression covariance is positive definite

`serCov σ2 σ02 x` is positive definite for `σ² > 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.posDef_serCov`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#pos-def-ser-cov).

## The marginal law of the phenotype given the causal variant

If `y = x β + e` with
`β ~ N(0, σ₀²)` independent of `e ~ N(0, σ² I)`, then `y` has density
`multivariateGaussianPDFReal 0 (serCov σ2 σ02 x)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.map_ser_eq_withDensity`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#map-ser-eq-with-density).

## The regression Bayes factor is the Wakefield ABF

**The regression Bayes factor is the Wakefield ABF** (Wang et al. 2020): the
density of `y` when variant `x` carries an `N(0, σ₀²)` effect, divided by its density with no
effect, is the ABF of the summary statistics `olsEffect x y` and `olsVar σ2 x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.multivariateGaussianPDFReal_serCov_div`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#multivariate-gaussian-pdfreal-ser-cov-di).

## Prior weights over the causal variant

A finite probability distribution used as the prior over the single causal variant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.PriorWeights`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#prior-weights).

## A normalized prior gives some variant positive weight

A normalized non-negative finite prior assigns positive weight to some variant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.PriorWeights.exists_weight_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#exists-weight-pos).

## Positivity of the prior-weighted marginal likelihood

Strictly positive evidence has a strictly positive prior-weighted marginal likelihood.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.PriorWeights.evidence_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#evidence-pos).

## Normalized weighted evidence

Algebraic normalization of arbitrary weights times evidence. This is useful even outside the
probability domain; it takes Lean's value `0` when the denominator vanishes.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.normalizedWeightedEvidence`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#normalized-weighted-evidence).

## Posterior inclusion probability

Posterior inclusion probability from a normalized non-negative prior and variant evidence.
When every evidence value is positive, `PriorWeights.evidence_pos` makes the denominator strictly
positive, and `pip_nonneg` and `sum_pip` prove that these values form a probability distribution.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.pip`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#pip).

## Nonnegativity of posterior inclusion probabilities

Posterior inclusion probabilities are non-negative when every evidence value is positive.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.pip_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#pip-nonneg).

## Posterior inclusion probabilities sum to one

Posterior inclusion probabilities normalize to one when every evidence value is positive.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sum_pip`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-pip).

## Single-effect likelihood-ratio identity

The unconditional algebraic single-effect likelihood-ratio identity for arbitrary real
weights. Its right side is accurately named algebraic normalization, not a posterior probability.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.serLikelihoodRatio_eq_normalizedWeightedEvidence`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ser-likelihood-ratio-eq-normalized-weigh).

## Positivity of the single-effect regression evidence

The prior-weighted single-effect evidence is strictly positive on the regression domain.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.serPosterior_evidence_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ser-posterior-evidence-pos).

## Posterior inclusion probabilities of the single-effect regression

**Posterior inclusion probabilities of the single-effect regression** (Wang et al. 2020):
Bayes' rule for the causal variant with a normalized non-negative prior equals `pip` applied to
the strictly positive Wakefield ABFs.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.serPosterior_eq_pip`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#ser-posterior-eq-pip).

## The effect posterior of the single-effect regression

**The effect posterior of the single-effect regression** (Wang et al. 2020): given
`y = x β + e` with `β ~ N(0, σ₀²)` independent of `e ~ N(0, σ² I)`, for almost every `y` the
effect is normal with mean `σ₀² / (σ₀² + s²) · β̂` and variance `σ₀² s² / (σ₀² + s²)`, where
`β̂ = olsEffect x y` and `s² = olsVar σ2 x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.condDistrib_ser_effect`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#cond-distrib-ser-effect).

## The five colocalization hypotheses

The five coloc hypotheses: no association (`h0`), trait 1 only (`h1`), trait 2 only (`h2`),
two distinct causal variants (`h3`), one shared causal variant (`h4`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocHypothesis`, an inductive type declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-hypothesis).

## Colocalization hypothesis of a causal configuration

The hypothesis of a configuration `(causal variant of trait 1, causal variant of trait 2)`,
`none` meaning no causal variant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocHypothesis`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-hypothesis-2).

## Colocalization prior parameters

Non-negative coloc configuration-weight parameters (Giambartolomei et al. 2014): `p1`, `p2`,
`p12` for a variant causal for trait 1 only, trait 2 only, and both. The cited hypothesis weights
use null weight `1`. The bound also supports a separate normalized categorical-prior model.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-prior).

## Null mass of the categorical colocalization prior

The remaining null mass in the optional normalized categorical-prior model.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.p0`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#p0).

## Normalized categorical colocalization prior

A normalized categorical prior, distinct from the cited coloc relative weights.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.categoricalPrior`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#categorical-prior).

## Unnormalized colocalization configuration weight

The cited coloc unnormalized configuration weight, whose H0 weight is `1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.weight`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#weight).

## Nonnegativity of categorical configuration priors

Categorical configuration priors are non-negative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.categoricalPrior_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#categorical-prior-nonneg).

## Nonnegativity of colocalization configuration weights

Cited coloc configuration weights are non-negative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.weight_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#weight-nonneg).

## Bayes factor of a colocalization configuration

The Bayes factor of a configuration against the null: the product of the two traits' Bayes
factors, `1` for a trait without a causal variant (the two studies are independent).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocBF`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-bf).

## Nonnegativity of configuration Bayes factors

A configuration Bayes factor is non-negative when both traits' Bayes factors are.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocBF_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-bf-nonneg).

## Closed-form colocalization hypothesis scores

The cited coloc closed-form algebraic scores. H0 has score `1`; H1--H4 retain the
per-configuration coefficients of Giambartolomei et al. (2014). They are unnormalized hypothesis
weights, and hence have a probability interpretation, when the Bayes factors are non-negative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocClosedForm`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 640](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L640). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-closed-form).

## Closed-form scores for the categorical colocalization prior

Closed forms for the optional normalized categorical-prior model. This differs from the cited
coloc formula only in using its remaining null mass rather than the cited H0 weight `1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocCategoricalClosedForm`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-categorical-closed-form).

## The coloc closed forms

**The coloc closed forms** (Giambartolomei et al. 2014): the sum of unnormalized configuration
weight times Bayes factor over each hypothesis equals its closed form.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sum_colocWeight_mul_colocBF`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 659](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-coloc-weight-mul-coloc-bf).

## Nonnegativity of closed-form colocalization scores

Cited coloc closed-form scores are non-negative on the Bayes-factor domain.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocClosedForm_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-closed-form-nonneg).

## Positivity of colocalization evidence

Cited coloc evidence is strictly positive for non-negative Bayes factors because H0 has
unnormalized weight `1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocEvidence_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-evidence-pos).

## Categorical-prior hypothesis scores equal their closed forms

The corresponding closed forms for the optional normalized categorical-prior model.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sum_categoricalPrior_mul_colocBF`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-categorical-prior-mul-coloc-bf).

## Categorical colocalization priors sum to one

The optional categorical configuration priors sum to one.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.ColocPrior.sum_categoricalPrior`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-categorical-prior).

## Colocalization normalization identity

The unconditional algebraic coloc normalization identity: each hypothesis's configuration
score divided by the total score equals its closed-form score divided by the closed-form total.
For arbitrary real `bf1` and `bf2` these ratios need not be probabilities. See
`colocPosterior_nonneg` and `sum_colocPosterior_eq_one` for the probability-domain results.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocPosterior_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-posterior-eq).

## Nonnegativity of colocalization posteriors

Normalized cited coloc hypothesis weights are non-negative for non-negative Bayes factors.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocPosterior_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-posterior-nonneg).

## Colocalization posteriors sum to one

Normalized cited coloc hypothesis weights sum to one for non-negative Bayes factors.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sum_colocPosterior_eq_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-coloc-posterior-eq-one).

## Posterior identity for the categorical colocalization prior

The normalized posterior identity for the separate categorical-prior model.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.colocCategoricalPosterior_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#coloc-categorical-posterior-eq).

## Credible set of variants

A `ρ`-credible set: its total posterior inclusion probability is at least `ρ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.IsCredibleSet`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#is-credible-set).

## Prefix of variants in a given order

The first `k` variants in the order `σ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sortedPrefix`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sorted-prefix).

## Cardinality of a sorted prefix

A prefix of length `k ≤ card ι` has `k` elements.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.card_sortedPrefix`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#card-sorted-prefix).

## Sorted prefix carries the most posterior mass

The `k` largest values carry the most mass: if `σ` sorts `α` in decreasing order, no set of
`S.card` variants has more mass than the prefix of that length.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.sum_le_sum_sortedPrefix`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 811](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L811). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#sum-le-sum-sorted-prefix).

## The shortest credible prefix has minimum size

**The shortest credible prefix has minimum size** (Maller et al. 2012; Wang et al. 2020): if
`σ` sorts `α` in decreasing order and no prefix shorter than `k` is `ρ`-credible, every
`ρ`-credible set has at least `k` elements.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.le_card_of_isCredibleSet`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 861](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L861). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#le-card-of-is-credible-set).

## A minimum-size credible set exists and is a sorted prefix

If the total mass is at least
`ρ`, some prefix of length `k` is `ρ`-credible, has `k` elements, and every `ρ`-credible set has
at least `k` elements.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FineMapping.exists_minimal_credible_prefix`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FineMapping.lean, line 871](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/FineMapping.lean#L871). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html#exists-minimal-credible-prefix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayesian fine-mapping and colocalization](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/statistical-genetics/bayesian-fine-mapping-and-colocalization)
