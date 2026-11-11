---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.meanValue, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.avgEffect, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domDev, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.genVar, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.addVar, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domVar, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.genotypicValue_eq, MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.sum_mul_avgEffect
statement: formalized
proof: formalized
---

# Fisher's decomposition of genetic variance

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html).

## Mean genotypic value under Hardy–Weinberg proportions

The mean genotypic value `μ = ∑ i ∑ j p i p j G i j` under Hardy–Weinberg proportions.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.meanValue`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#mean-value).

## Average effect of an allele

The average effect of allele `i`, `α i = ∑ j p j G i j - μ`: the mean value of the genotypes
carrying `i` (the other gene drawn from the population) minus the population mean. This is the
average excess; under Hardy–Weinberg proportions it is Fisher's average effect, the coefficient
of the least-squares additive fit (`domVar_le_sum_sq`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.avgEffect`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#avg-effect).

## Dominance deviation of a genotype

The dominance deviation `δ i j = G i j - μ - α i - α j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domDev`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#dom-dev).

## Genetic variance under Hardy–Weinberg proportions

The genetic variance `V_G = ∑ i ∑ j p i p j (G i j - μ) ²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.genVar`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#gen-var).

## Additive genetic variance

The additive genetic variance `V_A = 2 ∑ i p i α i ²`, the variance of the breeding value
`α i + α j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.addVar`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#add-var).

## Dominance variance

The dominance variance `V_D = ∑ i ∑ j p i p j δ i j ²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domVar`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#dom-var).

## Decomposition of the genotypic value

The decomposition `G i j = μ + α i + α j + δ i j` (an identity by definition of `δ`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.genotypicValue_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#genotypic-value-eq).

## Average effects have mean zero

The average effects have mean zero: `∑ i p i α i = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.sum_mul_avgEffect`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#sum-mul-avg-effect).

## Orthogonality of dominance deviations in the second allele

Orthogonality of the dominance deviations: `∑ j p j δ i j = 0` for every `i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.sum_mul_domDev_right`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#sum-mul-dom-dev-right).

## Orthogonality of dominance deviations in the first allele

Orthogonality of the dominance deviations for a symmetric genotypic value:
`∑ i p i δ i j = 0` for every `j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.sum_mul_domDev_left`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#sum-mul-dom-dev-left).

## Least squares (Fisher 1918)

Among all fits `c + a i + a j` of the genotypic value by
a function additive over the two genes, the additive fitted genotypic value `μ + α i + α j`
minimizes the weighted squared error `∑ p i p j (G i j - c - a i - a j) ²`; its error is `V_D`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domVar_le_sum_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#dom-var-le-sum-sq).

## Fisher's variance decomposition

`V_G = V_A + V_D`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.genVar_eq_addVar_add_domVar`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#gen-var-eq-add-var-add-dom-var).

## Parent–offspring covariance of genotypic values

The covariance of the genotypic values of a parent and its offspring: the parent has
genotype `(i, j)` (frequency `p i p j`) and transmits `cond b i j` (each with probability
`1/2`), and the offspring's other gene `k` comes from an unrelated mate (frequency `p k`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covParentOffspring`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-parent-offspring).

## Half-sib covariance of genotypic values

The covariance of the genotypic values of half sibs: the common parent has genotype
`(i, j)` and transmits `cond b i j` to one offspring and, independently, `cond b' i j` to the
other; the second genes `k`, `l` come from two unrelated mates.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covHalfSibs`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-half-sibs).

## Full-sib covariance of genotypic values

The covariance of the genotypic values of full sibs: the sire `(i, j)` and the dam
`(k, l)` are unrelated; the first offspring receives `cond b i j` and `cond e k l`, the second,
independently, `cond b' i j` and `cond e' k l`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covFullSibs`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-full-sibs).

## Parent and offspring (Fisher 1918)

`Cov(P, O) = V_A / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covParentOffspring_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-parent-offspring-eq).

## Half sibs (Fisher 1918)

`Cov(HS) = V_A / 4`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covHalfSibs_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-half-sibs-eq).

## Full sibs (Fisher 1918)

`Cov(FS) = V_A / 2 + V_D / 4`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.covFullSibs_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#cov-full-sibs-eq).

## Allele frequencies at a biallelic locus

Allele frequencies at a biallelic locus: `A₁` (`true`) has frequency `q₁` and `A₂`
(`false`) has frequency `1 - q₁`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.biallelicFreq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#biallelic-freq).

## Genotypic values at a biallelic locus on Falconer's scale

Genotypic values at a biallelic locus on Falconer's scale: `A₁A₁ ↦ a`, `A₁A₂ ↦ d`,
`A₂A₂ ↦ -a` (the origin is the midpoint of the homozygotes).

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.biallelicValue`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#biallelic-value).

## Additive variance at a biallelic locus (Falconer & Mackay 1996, ch. 8)

With
`p = q₁` and `q = 1 - q₁`, `V_A = 2pq (a + d (q - p)) ²`. An algebraic identity, valid for every
real `q₁`; it is a variance for `0 ≤ q₁ ≤ 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.addVar_biallelic`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#add-var-biallelic).

## Dominance variance at a biallelic locus (Falconer & Mackay 1996, ch. 8)

`V_D = (2pqd) ²`, for every real `q₁`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.FisherDecomposition.domVar_biallelic`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/FisherDecomposition.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html#dom-var-biallelic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fisher's decomposition of genetic variance](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/quantitative-genetics/fisher-s-decomposition-of-genetic-variance)
