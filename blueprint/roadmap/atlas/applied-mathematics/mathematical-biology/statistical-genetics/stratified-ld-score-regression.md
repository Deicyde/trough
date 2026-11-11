---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.pheno, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.betaHat, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.chiSq, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.ofLDScore, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.chiSq_ofLDScore, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq, MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq_of_standardized
statement: formalized
proof: formalized
---

# Stratified LD-score regression

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html).

## Random-effects model of stratified LD-score regression

The random-effects model of stratified LD-score regression at the level of raw second
moments: marker `k` has effect variance `sigma2 k`, the noise has variance `sigmaE2`, and
effects and noise are orthogonal in `L²`. As in `LDScore.Model`, the measure is arbitrary, no
means are assumed, and all statements are conditional on the genotype matrix.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#model).

## Phenotype in the stratified LD-score model

The phenotype `y = X β + ε`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.pheno`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#pheno).

## Normalized marker score in stratified LD-score regression

The `N`-normalized score `β̂ j = X_jᵀ y / N` of marker `j` (as in `LDScore.Model.betaHat`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.betaHat`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#beta-hat).

## Association chi-squared statistic in stratified LD-score regression

The association statistic `χ² j = N * β̂ j ^ 2` of marker `j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.chiSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#chi-sq).

## LD-score regression model as a stratified model

The LD-score regression model of `LDScore` is the stratified model with equal per-marker
variances `h² / M` and noise variance `1 - h²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.ofLDScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#of-ldscore).

## Stratified statistic agrees with the LD-score statistic

The stratified statistic of `ofLDScore D` is the statistic of `LDScore`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.chiSq_ofLDScore`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#chi-sq-of-ldscore).

## Expected statistic with per-marker variances

**Expected statistic with per-marker variances**, for an arbitrary genotype matrix:
`𝔼[χ² j] = N ∑_k r_jk² σ²_k + σ²_e (∑_i X_ij²) / N`. (For `N = 0` both sides are `0`.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#integral-chi-sq).

## Expected chi-squared statistic of a standardized marker

For a column with sum of squares `N` (a standardized marker) and `N ≠ 0`:
`𝔼[χ² j] = N ∑_k r_jk² σ²_k + σ²_e`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq_of_standardized`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#integral-chi-sq-of-standardized).

## Annotation LD score of a marker

The LD score of marker `j` with respect to annotation `C`:
`ℓ(j, C) = ∑_k a_{kC} r_jk²` (Finucane et al. 2015 for binary annotations; Gazal et al. 2017 for
continuous ones).

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.annotLDScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#annot-ldscore).

## Stratified LD-score regression

**Stratified LD-score regression** (Finucane et al. 2015; continuous annotations, Gazal et
al. 2017): if the per-marker variances are linear in the annotations, `σ²_k = ∑_C τ_C a_{kC}`,
then for a standardized genotype matrix and `N ≠ 0`,
`𝔼[χ² j] = N ∑_C τ_C ℓ(j, C) + σ²_e`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq_of_annot`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#integral-chi-sq-of-annot).

## Frequency-dependent architecture

**Frequency-dependent architecture** (the α model of Schoech et al. 2019): if the per-allele
effect variance of marker `k` with allele frequency `p_k` is proportional to `[p_k (1 - p_k)]^α`,
the variance of the effect of the standardized genotype is `σ²_k = c [p_k (1 - p_k)]^(1 + α)`,
and then, for a standardized genotype matrix and `N ≠ 0`,
`𝔼[χ² j] = N c ∑_k [p_k (1 - p_k)]^(1 + α) r_jk² + σ²_e`. (The real power is meaningful for
`0 < p_k < 1`.)

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq_of_alpha`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#integral-chi-sq-of-alpha).

## Heritability of a marker category

The heritability `h²(C) = ∑_{k ∈ C} σ²_k` of category `C`, for a labeling `cat` of the
markers by categories.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.catH2`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#cat-h2).

## Number of markers in a category

The number `M_C` of markers in category `C`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.catSize`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#cat-size).

## Heritability enrichment of a category

The enrichment of category `C`: its proportion of heritability divided by its proportion of
markers, `(h²(C) / h²) / (M_C / M)` with `h² = ∑_k σ²_k` (Finucane et al. 2015).

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.enrichment`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#enrichment).

## Marker-proportion-weighted enrichments sum to one

For a partition of the markers into categories (a labeling `cat`) and nonzero total
heritability, the marker-proportion-weighted enrichments sum to one:
`∑_C (M_C / M) * Enrichment(C) = 1`. Empty categories contribute `0` on both sides of each
term.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.sum_size_mul_enrichment`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#sum-size-mul-enrichment).

## Design matrix of stratified LD-score regression

The design matrix `[1 | N ℓ(·, C)]` of stratified LD-score regression with a free intercept;
column `none` is the intercept and column `some C` the scaled annotation LD score.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.design`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#design).

## Injective matrix action iff full column rank

A real matrix has injective `mulVec` iff it has full column rank.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.injective_mulVec_iff_rank_eq_card`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#injective-mul-vec-iff-rank-eq-card).

## Expected statistics are the design matrix times the parameters

Under the annotation model, the vector of expected statistics is the design matrix applied
to the parameter vector `(σ²_e, τ)` (intercept first). Hence the parameters are determined by
the expected statistics of all markers, whatever their values, iff
`(design X a).rank = Fintype.card (Option ι)` (`injective_mulVec_iff_rank_eq_card`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.Model.integral_chiSq_eq_design_mulVec`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#integral-chi-sq-eq-design-mul-vec).

## LDSC-SEG contrast

**LDSC-SEG contrast** (Finucane et al. 2018): for per-SNP variances
`σ²_k = ∑_C τ_C a_{kC}`, two SNPs `k`, `k'` whose annotations agree except on annotation `cS`
differ in per-SNP variance by `τ_{cS} (a_{k cS} - a_{k' cS})`. With `cS` the indicator of a gene
set `S` contained in the control gene set `G` (whose indicator is one of the other annotations),
`k ∈ S` and `k' ∈ G ∖ S` with equal values of all other annotations give
`σ²_k - σ²_{k'} = τ_S`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.StratifiedLDScore.sigma2_sub_sigma2_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/StratifiedLDScore.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html#sigma2-sub-sigma2-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stratified LD-score regression](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/stratified-ld-score-regression/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/stratified-ld-score-regression)
