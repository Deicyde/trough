---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.integral_score_mul_score, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.h2_nonneg, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.s2_nonneg, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.betaHat, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.accuracySq, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.integral_beta_mul_betaHat, MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.integral_beta_sq
statement: formalized
proof: formalized
---

# Genomic prediction from summary statistics

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html).

## Polygenic-score accuracy

## Cross moment of two polygenic scores

In a target population whose marker genotypes `x j` have raw second moments
`∫ x j * x k = [j = k]` (standardized, uncorrelated markers), the scores `xᵀ a` and `xᵀ b` of two
effect vectors have raw cross moment `aᵀ b`. With mean-zero genotypes and a probability measure
this is the covariance of the genetic value `xᵀ β` and the polygenic score `xᵀ β̂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.integral_score_mul_score`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-score-mul-score).

## Effect-estimate model for polygenic score accuracy

The effect-estimate model behind polygenic-score accuracy (Daetwyler et al. 2008;
Dudbridge 2013), at the level of raw second moments, for `M` independent markers: true effects
`beta k` with `∫ β k β l = (h² / M) [k = l]`, estimation errors `err k` with
`∫ e k e l = s² [k = l]`, orthogonal to the effects. The estimates are `β̂ = β + e`
(`betaHat`). For a probability measure and mean-zero effects and errors these are the
covariance conditions of the cited model; `s²` is the sampling variance of each estimate
(`1 / N` in the cited papers, `(1 - h²) / N` in `ofLDScore`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#prsmodel).

## Nonnegativity of heritability in the effect-estimate model

The model forces `h² ≥ 0` when there is at least one marker.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.h2_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#h2-nonneg).

## Nonnegativity of the sampling error variance of effect estimates

The model forces `s² ≥ 0` when there is at least one marker.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.s2_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#s2-nonneg).

## Estimated marker effects

The estimated effects `β̂ = β + e`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.betaHat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#beta-hat).

## Squared accuracy of a polygenic score

The squared correlation of the genetic value and the polygenic score as a ratio of
expectations, `𝔼[βᵀβ̂]² / (𝔼[βᵀβ] 𝔼[β̂ᵀβ̂])`: by `integral_score_mul_score`, `βᵀβ̂`, `βᵀβ` and
`β̂ᵀβ̂` are the covariance and variances of `xᵀβ` and `xᵀβ̂` over a target population of
standardized uncorrelated markers. It is not the expectation of a squared correlation.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.accuracySq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#accuracy-sq).

## Expected cross product of true and estimated effects

`𝔼[βᵀβ̂] = h²` (for at least one marker).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.integral_beta_mul_betaHat`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-beta-mul-beta-hat).

## Expected squared norm of the true effects

`𝔼[βᵀβ] = h²` (for at least one marker).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.integral_beta_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-beta-sq).

## Expected squared norm of the estimated effects

`𝔼[β̂ᵀβ̂] = h² + M s²` (for at least one marker).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.integral_betaHat_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-beta-hat-sq).

## Polygenic-score accuracy

**Polygenic-score accuracy** as a ratio of expectations: `r²_g = h² / (h² + M s²)`. (If
`h² = 0` both sides are `0`.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.accuracySq_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#accuracy-sq-eq).

## Daetwyler–Dudbridge formula

With sampling variance `s² = 1 / N`,
`r²_g = N h² / (N h² + M)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.accuracySq_eq_of_s2`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#accuracy-sq-eq-of-s2).

## Training genotype matrix with orthogonal standardized columns

The training genotype matrix has orthogonal columns with sum of squares `N`,
`∑ i, X i k * X i l = N [k = l]`; for centered columns this says that the markers are
uncorrelated, with unit sample variance, in the training sample.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.HasOrthogonalColumns`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#has-orthogonal-columns).

## Effect-estimate model derived from the LD-score model

The effect-estimate model obtained from the LD-score model when the effects are estimated by
the normalized scores `β̂ = Xᵀ y / N` on a training matrix with orthogonal standardized columns:
the error is `e k = ∑ i, X i k ε i / N` and its sampling variance is `(1 - h²) / N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.ofLDScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#of-ldscore).

## Estimates of the derived model are normalized scores

The estimates of `ofLDScore` are the normalized scores `Xᵀ y / N` of the LD-score model.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.ofLDScore_betaHat`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#of-ldscore-beta-hat).

## Polygenic-score accuracy in the LD-score model

With orthogonal standardized training
columns, `β̂ = Xᵀ y / N` and residual variance `1 - h²`,
`r²_g = N h² / (N h² + M (1 - h²))`. The cited `N h² / (N h² + M)` takes the residual variance to
be `1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.PRSModel.accuracySq_ofLDScore`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#accuracy-sq-of-ldscore).

## Marginal least-squares estimate of a marker effect

The marginal least-squares estimate `x_jᵀ y / x_jᵀ x_j` of marker `j` (single-marker
regression without intercept, on centered genotypes and phenotype as in Yang et al. 2012).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.marginalEstimate`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#marginal-estimate).

## Diagonal of the genotype Gram matrix

The diagonal `D = diag(XᵀX)` of the Gram matrix.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.gramDiag`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#gram-diag).

## Genotype-phenotype cross products from marginal estimates

`Xᵀ y = D β̂` for the marginal estimates `β̂` (Yang et al. 2012). This holds for every
genotype matrix: a column with `x_jᵀ x_j = 0` is zero, so both sides vanish there.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.transpose_mulVec_eq_gramDiag_mulVec`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#transpose-mul-vec-eq-gram-diag-mul-vec).

## COJO joint estimate

**COJO joint estimate** (Yang et al. 2012, eq. (5)): the joint least-squares estimate
`(XᵀX)⁻¹ Xᵀ y` equals `(XᵀX)⁻¹ D β̂` in terms of the marginal estimates `β̂`, so it can be
computed from summary statistics and `XᵀX`. (Stated for every `X`; it is the least-squares
estimate when `XᵀX` is invertible.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.cojo_joint`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#cojo-joint).

## Joint estimate equals marginal estimates for uncorrelated markers

For markers uncorrelated in the sample (`XᵀX` diagonal) without zero columns, the joint
estimate is the vector of marginal estimates.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.cojo_joint_of_diagonal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#cojo-joint-of-diagonal).

## Conditional estimate of second-block effects (COJO)

The unconditional algebraic formula from Yang et al. 2012, eq. (15):
`(X₂ᵀX₂)⁻¹ X₂ᵀ y - (X₂ᵀX₂)⁻¹ X₂ᵀX₁ (X₁ᵀX₁)⁻¹ X₁ᵀ y`. When both Gram determinants are units,
this has the usual interpretation as the block-2 fit conditional on the block-1 fit. For a
singular Gram matrix, Mathlib's nonsingular inverse is zero and the value can be a junk value.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.conditionalEstimate`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#conditional-estimate).

## COJO conditional algebraic formula from summary statistics

**COJO conditional algebraic formula from summary statistics** (Yang et al. 2012, eq. (17)):
`b̂₂|b̂₁ = (X₂ᵀX₂)⁻¹ D₂ β̂₂ - (X₂ᵀX₂)⁻¹ X₂ᵀX₁ (X₁ᵀX₁)⁻¹ D₁ β̂₁`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.conditionalEstimate_eq_summary`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#conditional-estimate-eq-summary).

## Conditional estimate as a fit to the first-block residual

Unconditionally, the conditional formula equals the nonsingular-inverse formula applied to
the algebraic residual `y - X₁ ((X₁ᵀX₁)⁻¹ X₁ᵀ y)`. If both Gram determinants are units, these
are the successive least-squares fits on blocks 1 and 2. With a singular Gram matrix they need
not minimize residual error. This is in general not the block-2 part of the joint formula on
both blocks (the formulas agree when `X₂ᵀX₁ = 0`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.conditionalEstimate_eq_residual`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#conditional-estimate-eq-residual).

## Stratified LD score

The stratified normalized-cross-product score
`ℓ(j, C) = ∑_{k ∈ C} (X_jᵀ X_k / N)²`. For a standardized genotype matrix this is the stratified
LD score of marker `j` with respect to annotation category `C` (Finucane et al. 2015).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.stratLDScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#strat-ldscore).

## Stratified LD-score model

The stratified LD-score model (Finucane et al. 2015), at the level of raw second moments:
annotation categories `cat c ⊆ {markers}` (possibly overlapping), per-category contributions
`tau c`, effects with `∫ β k β l = [k = l] ∑_c τ_c [k ∈ cat c]`, noise with
`∫ ε i ε i' = σ²_e [i = i']`, effects orthogonal to noise. The cited model normalizes the
phenotypic variance so that `σ²_e ≈ 1`; the confounding term `N a` is not modeled.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#stratified-model).

## Phenotype in the stratified LD-score model

The phenotype `y = X β + ε`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.pheno`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#pheno).

## Normalized score in the stratified LD-score model

The `N`-normalized score `β̂ j = X_jᵀ y / N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.betaHat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#beta-hat-2).

## Association statistic in the stratified LD-score model

The association statistic `χ² j = N β̂ j ²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.chiSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#chi-sq).

## Expected association statistic in the stratified LD-score model

The exact expectation of the association statistic in the stratified model, for any
genotype matrix: `𝔼[χ² j] = N ∑_c τ_c ℓ(j, cat c) + σ²_e (∑ i, X i j ²) / N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.integral_chiSq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-chi-sq).

## Stratified LD-score regression

**Stratified LD-score regression** (Finucane et al. 2015): for a standardized genotype
matrix and `N ≠ 0`, `𝔼[χ² j] = N ∑_c τ_c ℓ(j, cat c) + σ²_e`. Full-matrix standardization makes
every normalized cross product in `stratLDScore` a sample correlation.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.integral_chiSq_of_standardized`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-chi-sq-of-standardized).

## One causal variant

**One causal variant** (the LD-proxy noncentrality; Pritchard & Przeworski 2001): if the
genotype matrix is standardized and the only category is the single causal marker `c` with
variance `τ`, then for a marker `m` and `N ≠ 0`, `𝔼[χ² m] = N τ r m c ² + σ²_e`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.StratifiedModel.integral_chiSq_single_causal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-chi-sq-single-causal).

## In-sample LD correlation

The in-sample normalized cross product `∑_{i ∈ S} X i j X i k / |S|` of markers `j`, `k` in
the sample `S` of a pool of individuals (the sample LD correlation for a matrix standardized
within `S`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.sampleCorr`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#sample-corr).

## Bivariate LD-score model

The bivariate LD-score model (Bulik-Sullivan et al. 2015b), at the level of the cross
second moments that enter `𝔼[z₁ z₂]`: a pool of `n` genotyped individuals with genotype matrix
`X`, two GWAS samples `S₁`, `S₂` of the pool (possibly overlapping), effects `β₁`, `β₂` with
`∫ β₁ k β₂ l = (ρ_g / M) [k = l]` (genetic covariance `ρ_g`), noises `ε₁`, `ε₂` with
`∫ ε₁ i ε₂ i' = ρ_e [i = i']` (residual cross-moment `ρ_e` within an individual), effects of
each trait orthogonal to the noise of the other. The structure intentionally does not impose
within-trait moments or phenotype normalization, so it does not identify `ρ_e` with phenotypic
correlation or establish that the scaled scores below are standardized z-scores.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.CrossTraitModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#cross-trait-model).

## Scaled marginal score for the first trait

The scaled marginal score `z₁ j = √N₁ X_jᵀ y₁ / N₁` of marker `j` for trait 1, computed on
`S₁` with `y₁ = X β₁ + ε₁`. The model does not assert the normalization needed for a z-score.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.CrossTraitModel.z1`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#z1).

## Scaled marginal score for the second trait

The analogous scaled marginal score `z₂ j` of marker `j` for trait 2, computed on `S₂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.CrossTraitModel.z2`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#z2).

## Cross-trait scaled-score identity, exact form

With `N₁ = |S₁|`, `N₂ = |S₂|`,
`𝔼[z₁ j z₂ j] = √(N₁ N₂) (ρ_g / M) ∑_k r¹ j k r² j k + ρ_e (∑_{i ∈ S₁ ∩ S₂} X i j ²) / √(N₁ N₂)`,
with the in-sample normalized cross products `r¹`, `r²` (`sampleCorr`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.CrossTraitModel.integral_z_mul_z`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-z-mul-z).

## Equal normalized-cross-product specialization of the residual cross-moment identity

If
the two samples have the same normalized cross products with marker `j` and the overlap marker
is standardized at `j`
(`∑_{i ∈ S₁ ∩ S₂} X i j ² = N_s`), then
`𝔼[z₁ j z₂ j] = √(N₁ N₂) ρ_g ℓ_j / M + ρ_e N_s / √(N₁ N₂)`. Here `ρ_e` is only the residual
cross-moment specified by `CrossTraitModel`; this theorem does not state the Bulik-Sullivan
phenotypic-correlation overlap formula or establish z-score normalization.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.CrossTraitModel.integral_z_mul_z_of_sameLD`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#integral-z-mul-z-of-same-ld).

## Number of individuals in a case-control genotype table

The number of individuals `N = ∑ (r i + s i)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.total`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#total).

## Numerator of the Cochran–Armitage trend statistic

The trend numerator `U = ∑ i, i (r i S - s i R)` with `R = ∑ r`, `S = ∑ s`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.numer`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 733](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L733). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#numer).

## Pooled genotype-score variance

The pooled genotype-score variance `∑ i² n_i / N - (∑ i n_i / N)²`, `n_i = r i + s i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.scoreVar`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#score-var).

## Cochran–Armitage trend statistic

The **Cochran–Armitage trend statistic** with scores `0, 1, 2` (Armitage 1955):
`N U² / (R S (N ∑ i² n_i - (∑ i n_i)²))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.trendStat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#trend-stat).

## Squared correlation of case status and genotype score

The squared sample correlation of case status (`1` for cases, `0` for controls) and the
genotype score over the `N` individuals of the table.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.corrSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 749](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L749). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#corr-sq).

## Pooled allele frequency

The pooled frequency `p = ∑ i n_i / (2 N)` of the counted allele.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.alleleFreq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#allele-freq).

## Pearson's chi-squared statistic of a 2 × 2 table

Pearson's statistic `n (a d - b c)² / ((a + b)(c + d)(a + c)(b + d))` of a `2 × 2` table
`[[a, b], [c, d]]` with `n = a + b + c + d`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.pearson2x2`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#pearson2x2).

## Allelic test statistic

The **allelic test**: Pearson's statistic of the `2 × 2` table of case and control allele
counts (`2N` alleles).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.allelicStat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#allelic-stat).

## The trend test is `N r²`

**The trend test is `N r²`** (Armitage 1955): the Cochran–Armitage statistic is `N` times
the squared sample correlation of case status and genotype score. (In degenerate tables, where a
denominator vanishes, both sides are `0` by the convention `x / 0 = 0`.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.trendStat_eq_total_mul_corrSq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 784](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L784). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#trend-stat-eq-total-mul-corr-sq).

## Departure of the genotype-score variance from Hardy–Weinberg

The observed score variance minus the Hardy–Weinberg score variance `2 p q`:
`Var - 2 p (1 - p) = (4 n₀ n₂ - n₁²) / (2 N²)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.scoreVar_sub_hweVar`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 808](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L808). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#score-var-sub-hwe-var).

## Allelic versus trend test

**Allelic versus trend test** (Sasieni 1997): with cases and controls present, a pooled
allele frequency strictly between `0` and `1` and a positive score variance,
`allelic · 2 p q = trend · Var`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.allelicStat_mul_hweVar`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 822](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L822). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#allelic-stat-mul-hwe-var).

## The allelic test equals the trend test iff the pooled sample is in Hardy–Weinberg proportions

**The allelic test equals the trend test iff the pooled sample is in Hardy–Weinberg
proportions** (`n₁² = 4 n₀ n₂`; Sasieni 1997), whenever the trend numerator is nonzero.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GenomicPrediction.ArmitageTrend.allelicStat_eq_trendStat_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean, line 858](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/GenomicPrediction.lean#L858). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html#allelic-stat-eq-trend-stat-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Genomic prediction from summary statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/genomic-prediction-from-summary-statistics)
