---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.LDScore.ldCorr, MathlibExt.Biology.StatisticalGenetics.LDScore.ldScore, MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized, MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized.ldCorr_self, MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized.ldCorr_sq_le_one, MathlibExt.Biology.StatisticalGenetics.LDScore.Model, MathlibExt.Biology.StatisticalGenetics.LDScore.Model.h2_nonneg, MathlibExt.Biology.StatisticalGenetics.LDScore.Model.h2_le_one
statement: formalized
proof: formalized
---

# LD-score regression

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html).

## Normalized cross product of genotype markers

The normalized cross product `r j k = X_jᵀ X_k / N` of markers `j` and `k`. For a
standardized genotype matrix (`IsStandardized`) it is the sample correlation of the two
markers; for other matrices it is only a scale-dependent dot product.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.ldCorr`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#ld-corr).

## LD score of a marker

The LD score `ℓ j = ∑ k, r j k ^ 2` of marker `j` (an LD score in the sense of the cited
paper for a standardized genotype matrix).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.ldScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#ld-score).

## Standardized genotype matrix

The genotype matrix is standardized: every marker column has mean `0` and sum of squares
`N` (unit sample variance).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#is-standardized).

## A standardized marker has correlation one with itself

For a standardized matrix each marker has correlation `1` with itself.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized.ldCorr_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#ld-corr-self).

## Correlations of standardized markers lie in (-1, 1)

For a standardized matrix the correlations lie in `[-1, 1]` (Cauchy–Schwarz).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.IsStandardized.ldCorr_sq_le_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#ld-corr-sq-le-one).

## Random-effects model of LD-score regression

The random-effects model of LD-score regression (Bulik-Sullivan et al. 2015), stated at
the level of raw second moments, for `N` individuals and `M` markers with heritability `h2`.

* `beta k` is the (random) effect of marker `k`, with `∫ β k * β l = h2 / M * [k = l]`;
* `eps i` is the environmental noise of individual `i`, with
  `∫ ε i * ε i' = (1 - h2) * [i = i']`;
* effects and noise are orthogonal in `L²`.

The measure is arbitrary and no means are assumed; for a probability measure and mean-zero
effects and noise these are the covariance conditions of the cited model. The genotype matrix is
not part of the model: all expectations are conditional on it.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#model).

## Nonnegativity of heritability in the LD-score model

The heritability is nonnegative when there is at least one marker.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.h2_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#h2-nonneg).

## Heritability is at most one in the LD-score model

The heritability is at most `1` when there is at least one individual.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.h2_le_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#h2-le-one).

## Phenotype in the LD-score model

The phenotype `y = X β + ε`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.pheno`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#pheno).

## Normalized marginal score in the LD-score model

The `N`-normalized score `β̂ j = X_jᵀ y / N` of marker `j`. For a standardized column
(`∑ i, X i j ^ 2 = N`) it is the marginal least-squares estimate of the effect of marker `j`;
in general that estimate has denominator `∑ i, X i j ^ 2` instead of `N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.betaHat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#beta-hat).

## Association statistic in the LD-score model

The association statistic `χ² j = N * β̂ j ^ 2` of marker `j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.chiSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#chi-sq).

## Expected association statistic for an arbitrary genotype matrix

The exact expectation of the association statistic built from the `N`-normalized score,
for an arbitrary genotype matrix:
`𝔼[χ² j] = N h² / M * ℓ j + (1 - h²) * (∑ i, X i j ^ 2) / N`. (For `N = 0` both sides are `0`
by the convention `x / 0 = 0`.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.integral_chiSq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#integral-chi-sq).

## LD-score regression

LD-score regression (Bulik-Sullivan et al. 2015): for a standardized genotype matrix
(`IsStandardized`, so that `ldCorr` is the sample correlation and `ldScore` the LD score) and
`N ≠ 0`, `𝔼[χ² j] = N h² / M * ℓ j + (1 - h²)`. The expected association statistic is affine in
the LD score, with slope `N h² / M` and intercept `1 - h²`. The proof uses only that column `j`
has sum of squares `N`; the rest of the standardization is what makes `ℓ j` an LD score.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScore.Model.integral_chiSq_of_standardized`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScore.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScore.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#integral-chi-sq-of-standardized).

## Mean LD score

The mean LD score `ℓ̄ = (1 / M) ∑ j, ℓ j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.meanLDScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#mean-ldscore).

## Polygenic inflation of the mean association statistic

Polygenic inflation: for a standardized genotype matrix with `N, M ≠ 0`, the mean expected
association statistic is `1 - h² + N h² ℓ̄ / M`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.mean_integral_chiSq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#mean-integral-chi-sq).

## Phenotype with population stratification

The phenotype with a stratification shift: `y i = (X β) i + ε i + s * c i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.phenoStrat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#pheno-strat).

## Normalized score under stratification

The `N`-normalized score of marker `j` under stratification, `X_jᵀ y / N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.betaHatStrat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#beta-hat-strat).

## Association statistic under stratification

The association statistic `N * β̂ j ^ 2` under stratification.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.chiSqStrat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#chi-sq-strat).

## Expected association statistic under stratification

Stratification inflation: for a probability measure and mean-zero effects and noise,
`𝔼[χ² j] = N h² / M * ℓ j + (1 - h²) (∑ i, X i j ^ 2) / N + N s² (X_jᵀ c / N)²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.integral_chiSqStrat`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#integral-chi-sq-strat).

## Expected statistic under stratification for standardized genotypes

Stratification inflation for a standardized genotype matrix and `N ≠ 0`:
`𝔼[χ² j] = N h² / M * ℓ j + (1 - h²) + N s² (X_jᵀ c / N)²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.integral_chiSqStrat_of_standardized`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#integral-chi-sq-strat-of-standardized).

## LD-score regression with constant stratification

With a constant stratification term (`s² (X_jᵀ c / N)² = a` for every marker), the expected
statistic is exactly affine in the LD score, with slope `N h² / M` and intercept
`1 - h² + N a`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.integral_chiSqStrat_of_const`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#integral-chi-sq-strat-of-const).

## Mean association statistic with constant stratification

With a constant stratification term `N a`, the mean expected statistic is
`N h² ℓ̄ / M + (1 - h² + N a)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.mean_integral_chiSqStrat_of_const`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#mean-integral-chi-sq-strat-of-const).

## Attenuation ratio

The attenuation ratio `(intercept - 1) / (mean χ² - 1)` of Loh et al. (2018).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.attenuationRatio`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#attenuation-ratio).

## Attenuation ratio under constant stratification

With a constant stratification term `N a`, the attenuation ratio of the exact intercept
`1 - h² + N a` and the mean expected statistic is `(N a - h²) / (N h² ℓ̄ / M + N a - h²)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.attenuationRatio_of_const`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#attenuation-ratio-of-const).

## Confounding share of inflation under constant stratification

With a constant stratification term `N a`, the share of the mean inflation above the exact
null level `1 - h²` that is due to stratification is `N a / (N a + N h² ℓ̄ / M)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.confoundingShare_of_const`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#confounding-share-of-const).

## Confounding share lies between 0 and 1

The confounding share `N a / (N a + N h² ℓ̄ / M)` lies in `[0, 1]` when `a`, `h²` and `ℓ̄`
are nonnegative (as they are in the model: `a` is a square, `h² ≥ 0` by `Model.h2_nonneg`,
LD scores are sums of squares).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LDScoreInflation.confoundingShare_mem_Icc`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/LDScoreInflation.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html#confounding-share-mem-icc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: LD-score regression](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/ld-score-regression/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/statistical-genetics/ld-score-regression)
