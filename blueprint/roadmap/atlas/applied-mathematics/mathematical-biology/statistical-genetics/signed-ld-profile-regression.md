---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.ldMatrix, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.pheno, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.alphaHat, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_alphaHat, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_alphaHat_of_mean, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_gls_estimator, MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_gls_estimator_of_background
statement: formalized
proof: formalized
---

# Signed LD profile regression

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html).

## Signed LD profiles

## In-sample LD matrix

The in-sample LD matrix `R̂ = Xᵀ X / N`, with entries `ldCorr X j k`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.ldMatrix`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#ld-matrix).

## First-moment phenotype model of SLDP regression

The linear phenotype model of SLDP regression at the level of first moments: integrable
random effects `β` with means `meanBeta` and integrable noise `ε` of mean zero. (SLDP's model
takes `meanBeta = μ v` for a signed annotation `v`; second moments are not needed for the
first-moment identity.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#model).

## Phenotype in the SLDP regression model

The phenotype `y = X β + ε`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.pheno`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#pheno).

## Marginal marker-phenotype correlations in SLDP regression

The vector `α̂ = Xᵀ y / N` of marginal correlations between the (standardized) markers and
the phenotype.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.alphaHat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#alpha-hat).

## First-moment identity, exact in-sample form

Conditional on the genotype matrix,
`𝔼 α̂ = R̂ 𝔼 β` with `R̂ = Xᵀ X / N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_alphaHat`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#integral-alpha-hat).

## SLDP first-moment identity

**SLDP first-moment identity** (Reshef et al. 2018, Methods, Equation 5): if the true effects
have mean `μ v`, then `𝔼 α̂ = μ R̂ v`, a multiple of the signed LD profile `R̂ v` of `v`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_alphaHat_of_mean`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#integral-alpha-hat-of-mean).

## Unbiasedness of the weighted least-squares estimator

For any weight matrix `W` and
signed LD profile `s = R̂ v` with `⟪s, s⟫_W = sᵀ W s ≠ 0`, if `𝔼 β = μ v` then
`𝔼 [⟪s, α̂⟫_W / ⟪s, s⟫_W] = μ`, where `⟪a, b⟫_W = aᵀ W b`. SLDP uses the inverse of
`Ω = σ² R² + R / N` as `W`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_gls_estimator`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#integral-gls-estimator).

## Unbiasedness with covariates

**Unbiasedness with covariates** (the signed background model): suppose the true effects
have mean `μ v + U γ` for background annotations `U` (columns `u_b`) with arbitrary coefficients
`γ`, let `A = R̂ U` be their signed LD profiles, and let `z⊥ = R̂ v - A w` be the weighted residual
of the signed LD profile of `v` on `A` (`Aᵀ W z⊥ = 0`) for a symmetric weight matrix `W`. If
`⟪z⊥, z⊥⟫_W ≠ 0`, then `𝔼 [⟪z⊥, α̂⟫_W / ⟪z⊥, z⊥⟫_W] = μ`. By `Matrix.frischWaughLovell` this
estimator equals the coefficient of `R̂ v` in the joint weighted regression of `α̂` on
`[A | R̂ v]`, and the same as regressing the residualized `α̂` on `z⊥`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SignedLDProfile.Model.integral_gls_estimator_of_background`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/SignedLDProfile.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html#integral-gls-estimator-of-background).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Signed LD profile regression](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/signed-ld-profile-regression/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/signed-ld-profile-regression)
