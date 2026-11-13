---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.mean, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.alpha, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.delta, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varG, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varA, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varD, MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.sum_p_alpha
statement: formalized
proof: formalized
---

# Covariance between relatives

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html).

## Covariance Relatives

## Single-locus model under random union of gametes

A single locus under random union of gametes: allele frequencies `p` on a finite allele
set and symmetric genotypic values `g a b` (the mean phenotype of genotype `{a, b}`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#locus-model).

## Population mean genotypic value at a single locus

The population mean genotypic value `μ = ∑ p_a p_b g(a, b)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.mean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#mean).

## Fisher's average effect of an allele at a single locus

Fisher's average effect of allele `a`: `α a = ∑_b p_b g(a, b) - μ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.alpha`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#alpha).

## Dominance deviation at a single locus

The dominance deviation `δ a b = g(a, b) - μ - α a - α b`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.delta`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#delta).

## Genetic variance at a single locus

The genetic variance `V_G = ∑ p_a p_b (g(a, b) - μ)²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varG`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-g).

## Additive variance at a single locus

The additive variance `V_A = 2 ∑ p_a α_a²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-a).

## Dominance variance at a single locus

The dominance variance `V_D = ∑ p_a p_b δ_{ab}²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varD`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-d).

## Average effects are centred

Average effects are centred: `∑ p_a α_a = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.sum_p_alpha`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#sum-p-alpha).

## Dominance deviations are orthogonal to every allele

Dominance deviations are orthogonal to every allele: `∑_b p_b δ_{ab} = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.sum_p_delta`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#sum-p-delta).

## Fisher decomposition

**Fisher decomposition** of the genetic variance: `V_G = V_A + V_D`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varG_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-g-eq).

## Nonnegativity of the single-locus additive variance

The additive variance is nonnegative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varA_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-a-nonneg).

## Nonnegativity of the single-locus dominance variance

The dominance variance is nonnegative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varD_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-d-nonneg).

## The additive fit is least squares

**The additive fit is least squares** (Fisher definition of average effects): every
additive fit `c + h a + h b` has mean squared error at least `V_D`, the error of
`μ + α a + α b`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.varD_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-d-le).

## Mean product of genotypic values of two relatives

The mean product of genotypic values of two non-inbred relatives that share `0`, `1`, `2`
alleles identical by descent with probabilities `k₀, k₁, k₂`: given the IBD state, the
non-shared alleles are independent draws from `p`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.relProd`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#rel-prod).

## Covariance between relatives

**Covariance between relatives** at one locus (Fisher 1918; in the IBD form of Falconer and
Mackay ch. 9): for IBD probabilities summing to one,
`E[G_X G_Y] - μ² = (k₁ / 2 + k₂) V_A + k₂ V_D`, i.e. `2φ V_A + Δ V_D` with kinship
`φ = k₁ / 4 + k₂ / 2` and `Δ = k₂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.relCov_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#rel-cov-eq).

## Cockerham–Kempthorne variance components

Cockerham–Kempthorne variance components up to order `n`: `V i j = V_{A^i D^j}` is the
component of `i` additive and `j` dominance factors (`V 1 0 = V_A`, `V 0 1 = V_D`,
`V 2 0 = V_AA`, …). They are nonnegative, there is no `(0, 0)` component, and the genetic
covariance of relatives with `2φ` and `Δ` is `∑_{i, j ≤ n} (2φ)^i Δ^j V i j`. This structure
is the stated representation; it is proved for one locus by `LocusModel.relCov_eq`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#cockerham-components).

## Genetic covariance of relatives in Cockerham form

The genetic covariance of relatives with coefficients `2φ = twoPhi` and `Δ = Δ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.cov`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#cov).

## Additive variance of the Cockerham components

The additive variance `V_A = V 1 0` (zero if `n = 0`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.varA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-a-2).

## Falconer's estimator

**Falconer's estimator** under the ACE model, in covariance form: monozygotic twins have
`2φ = Δ = 1`, dizygotic twins (full sibs) `2φ = 1/2`, `Δ = 1/4`, and both share the same
common-environment covariance `C`; the estimator is `2 (Cov_MZ - Cov_DZ)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.falconer`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#falconer).

## Falconer's estimator in terms of Cockerham components

Falconer's estimator is `V_A` plus the non-additive components weighted by
`2 (1 - 2^{-i} 4^{-j})` (derived from Cockerham's coefficients).

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.falconer_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#falconer-eq).

## Phantom heritability inequality

The phantom-heritability inequality in covariance form: `V_A ≤ 2 (Cov_MZ - Cov_DZ)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.varA_le_falconer`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#var-a-le-falconer).

## Equality case of the phantom heritability inequality

Equality holds iff every non-additive component of order `≤ n` vanishes.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.falconer_eq_varA_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#falconer-eq-var-a-iff).

## Phantom heritability

**Phantom heritability** on the correlation scale (Zuk et al. 2012): with phenotypic
variance `V_P > 0`, the narrow-sense heritability `V_A / V_P` is at most the ACE estimate
`2 (r_MZ - r_DZ)`, where `r = Cov / V_P`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.CockerhamComponents.narrow_le_falconerHeritability`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#narrow-le-falconer-heritability).

## Single-locus model as Cockerham components

The one-locus model as Cockerham components of order `1`: `V 1 0 = V_A`, `V 0 1 = V_D`,
`V 1 1 = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.toComponents`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#to-components).

## Single-locus covariance between relatives in Cockerham form

The one-locus covariance between relatives is the Cockerham form of `toComponents`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.relCov_eq_cov`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#rel-cov-eq-cov).

## One-locus phantom heritability, unconditional

With monozygotic twins
(`k₂ = 1`), dizygotic twins (`k = (1/4, 1/2, 1/4)`) and a common environment `C`,
`2 (Cov_MZ - Cov_DZ) = V_A + (3/2) V_D`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.CovarianceRelatives.LocusModel.falconer_eq_of_locus`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/CovarianceRelatives.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html#falconer-eq-of-locus).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Covariance between relatives](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/covariance-between-relatives/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/covariance-between-relatives)
