---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.MixedModel.phenCov, MathlibExt.Biology.StatisticalGenetics.MixedModel.IsMMESolution, MathlibExt.Biology.StatisticalGenetics.MixedModel.posDef_phenCov, MathlibExt.Biology.StatisticalGenetics.MixedModel.isMMESolution_iff, MathlibExt.Biology.StatisticalGenetics.MixedModel.isMMESolution_iff_gls, MathlibExt.Biology.StatisticalGenetics.MixedModel.condDistrib_mixedModel, MathlibExt.Biology.StatisticalGenetics.MixedModel.condExp_mixedModel, MathlibExt.Biology.StatisticalGenetics.MixedModel.condDistrib_ldpredInf
statement: formalized
proof: formalized
---

# Linear mixed models and BLUP

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html).

## Mixed-model equations

## Phenotypic covariance of a linear mixed model

The phenotypic covariance `V = Z G Zᵀ + R` of the linear mixed model
`y = X b + Z u + e` with `Cov u = G`, `Cov e = R`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.phenCov`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#phen-cov).

## Solution of Henderson's mixed-model equations

Henderson's mixed-model equations for `y = X b + Z u + e`, `Cov u = G`, `Cov e = R`:
`[Xᵀ R⁻¹ X, Xᵀ R⁻¹ Z; Zᵀ R⁻¹ X, Zᵀ R⁻¹ Z + G⁻¹] [b; u] = [Xᵀ R⁻¹ y; Zᵀ R⁻¹ y]`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.IsMMESolution`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#is-mmesolution).

## Positive definiteness of the phenotypic covariance

`V = Z G Zᵀ + R` is positive definite.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.posDef_phenCov`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#pos-def-phen-cov).

## Henderson's mixed-model equations

**Henderson's mixed-model equations** (Henderson 1975; Robinson 1991): for positive definite
`G` and `R` and `V = Z G Zᵀ + R`, `(b, u)` solves the mixed-model equations if and only if `b`
solves the generalized least-squares normal equations `Xᵀ V⁻¹ X b = Xᵀ V⁻¹ y` and
`u = G Zᵀ V⁻¹ (y - X b)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.isMMESolution_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#is-mmesolution-iff).

## The MME solution is the GLS estimate and the BLUP

**The MME solution is the GLS estimate and the BLUP** (Henderson 1975): if moreover
`Xᵀ V⁻¹ X` is invertible, the mixed-model equations have the unique solution
`b̂ = (Xᵀ V⁻¹ X)⁻¹ Xᵀ V⁻¹ y` (the GLS estimate) and `û = G Zᵀ V⁻¹ (y - X b̂)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.isMMESolution_iff_gls`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#is-mmesolution-iff-gls).

## BLUP as a conditional law

**BLUP as a conditional law** (Henderson 1975; Robinson 1991): in the Gaussian mixed model
`y = X b + Z u + e` with fixed effects `b`, random effects `u ~ N(0, G)` and residuals
`e ~ N(0, R)` independent, `G` and `R` positive definite, the conditional law of `u` given `y`
is `N(G Zᵀ V⁻¹ (y - X b), G - G Zᵀ V⁻¹ Z G)` with `V = Z G Zᵀ + R` (for almost every `y`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.condDistrib_mixedModel`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#cond-distrib-mixed-model).

## BLUP is the conditional expectation

**BLUP is the conditional expectation** in the Gaussian mixed model:
`𝔼[u | y] = G Zᵀ V⁻¹ (y - X b)` almost surely.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.condExp_mixedModel`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#cond-exp-mixed-model).

## The LDpred-inf posterior

**The LDpred-inf posterior** (Vilhjálmsson et al. 2015; the likelihood
`β̂ | β ~ N(R β, R / N)` of Zhu and Stephens 2017): with `M` markers, `N` individuals,
heritability `h² > 0`, effects `β ~ N(0, h² / M · I)`, an LD matrix `R` that is positive definite,
and marginal estimates `β̂ = R β + ε` with `ε ~ N(0, R / N)` independent of `β`, the posterior law
of `β` given `β̂` is `N((R + M / (N h²) · I)⁻¹ β̂, (1 / N) (R + M / (N h²) · I)⁻¹)`. In particular
`𝔼[β | β̂] = (R + M / (N h²) · I)⁻¹ β̂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.condDistrib_ldpredInf`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#cond-distrib-ldpred-inf).

## Marginal association estimate of a marker

The `N`-normalized marginal association estimate `β̂_j = X_jᵀ y / N` of marker `j` for the
phenotype `y = X β + ε` (fixed effects `β`, noise `ε`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.marginalEffect`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#marginal-effect).

## The mean of the marginal estimates

**The mean of the marginal estimates** (Zhu and Stephens 2017): for fixed effects `β` and
noise with mean zero, `𝔼[X_jᵀ y / N] = (R β)_j` with `R = Xᵀ X / N` (`ldCorr`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.integral_marginalEffect`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#integral-marginal-effect).

## The raw residual-product second moment of the marginal estimates

**The raw residual-product second moment of the marginal estimates** (Zhu and Stephens
2017): if `𝔼[ε_i ε_i'] = σ² [i = i']`, then
`𝔼[(β̂_j - (R β)_j)(β̂_k - (R β)_k)] = σ² / N · R_jk`.

This theorem deliberately assumes neither that `P` is a probability measure nor that the noise
has mean zero, so its conclusion is not by itself a covariance or a Gaussian likelihood. With a
probability measure and mean-zero noise, `integral_marginalEffect` identifies `R β` as the mean,
and this raw second moment is the corresponding covariance.

Formalized by `MathlibExt.Biology.StatisticalGenetics.MixedModel.integral_marginalEffect_sub_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/MixedModel.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/MixedModel.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html#integral-marginal-effect-sub-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear mixed models and BLUP](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/linear-mixed-models-and-blup)
