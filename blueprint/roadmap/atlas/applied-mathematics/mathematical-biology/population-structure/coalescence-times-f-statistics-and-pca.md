---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.hetPair, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.sq_sub_eq_hetPair, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.meanHet, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.integrable_hetPair, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.f2_eq_meanHet, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel.f2_eq, MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel.f3_eq
statement: formalized
proof: formalized
---

# Coalescence times, f-statistics and PCA

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html).

## f-statistics from heterozygosities and coalescence times

## Probability that two genes differ at a biallelic site

The probability `a (1 - b) + b (1 - a)` that a gene from a population with allele frequency
`a` and a gene from a population with allele frequency `b` differ at a biallelic site.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.hetPair`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#het-pair).

## Squared frequency difference via pairwise heterozygosity

`(a - b) ^ 2 = hetPair a b - (hetPair a a + hetPair b b) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.sq_sub_eq_hetPair`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#sq-sub-eq-het-pair).

## Expected heterozygosity between populations

The expected heterozygosity `π X Y = 𝔼[hetPair (p X) (p Y)]` between populations `X` and
`Y` (within population `X` when `Y = X`).

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.meanHet`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#mean-het).

## Integrability of pairwise heterozygosity

`hetPair` of square-integrable frequencies is integrable on a finite measure space.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.integrable_hetPair`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#integrable-het-pair).

## Peter's formula for $f_2$ via expected heterozygosity

Peter (2016): `f2 A B = π A B - (π A A + π B B) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.f2_eq_meanHet`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#f2-eq-mean-het).

## Coalescent model linking heterozygosity and coalescence times

The relation between allele frequencies and coalescence times under neutral
infinite-sites mutation, taken as the model assumption: the expected heterozygosity between
populations `X` and `Y` is `θ` times the expected coalescence time `coalTime X Y` of a gene
from `X` and a gene from `Y` (two genes drawn independently, so with replacement, when
`X = Y`). Time is in units of `2N` generations and `θ = 4Nu`. The measure `μ` is finite: it
ranges over the evolutionary randomness and, in practice, over a finite set of loci. For
`θ = 0` the coalescence times are not determined by the frequencies, and the identities below
then say that the f-statistics vanish.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel`, a structure declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#coalescent-model).

## $f_2$ in terms of expected coalescence times

`f2 A B = θ (𝔼 T_AB - (𝔼 T_AA + 𝔼 T_BB) / 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel.f2_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#f2-eq).

## $f_3$ in terms of expected coalescence times

`f3 C A B = θ / 2 * (𝔼 T_CA + 𝔼 T_CB - 𝔼 T_AB - 𝔼 T_CC)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel.f3_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#f3-eq).

## $f_4$ in terms of expected coalescence times

`f4 A B C D = θ / 2 * (𝔼 T_AD + 𝔼 T_BC - 𝔼 T_AC - 𝔼 T_BD)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.CoalescentModel.f4_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#f4-eq).

## Column mean of a genotype matrix

The column mean `(1 / n) ∑ i, Z i s` of locus `s` over the `n` samples.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.colMean`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#col-mean).

## Column-centred genotype matrix

The genotype matrix with columns centred over the samples.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.centered`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#centered).

## Sample covariance of the centred genotype matrix

The sample covariance `C i j = (1 / L) ∑ s, X i s * X j s` of the centred genotype matrix
`X` over the `L` loci.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.genCov`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#gen-cov).

## Number of pairwise differences between samples

The number of pairwise differences `d i j = ∑ s, (Z i s - Z j s) ^ 2` (for `0`/`1`
haplotypes, the number of loci at which samples `i` and `j` differ).

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.pairDiff`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#pair-diff).

## Double centring of a square matrix

The double centring `t̄ i· + t̄ ·j - t i j - t̄ ··` of a square matrix `t` (row, column and
grand means over the `n` indices).

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.doubleCenter`, a definition declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#double-center).

## Genotype covariance as double-centred pairwise differences

McVean (2009), deterministic form: the covariance of the centred genotype matrix is the
double centring of the pairwise-difference matrix, divided by `2 L`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.genCov_eq_doubleCenter`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#gen-cov-eq-double-center).

## McVean's genealogical model for PCA

McVean's genealogical setting for PCA, taken as the model assumption: random genotypes
`Z i s` (sample `i`, locus `s`), square integrable, whose expected numbers of pairwise
differences are `θ` times the expected pairwise coalescence times `coalTime i j` (neutral
infinite sites, time in units of `2N` generations, `θ` the total scaled mutation rate of the
`L` loci). For `θ = 0` the coalescence times are not determined by the genotypes.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.McVeanModel`, a structure declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#mc-vean-model).

## McVean's theorem on expected genotype covariance

McVean (2009): the expected genotype covariance is `θ / (2 L)` times the double centring of
the expected pairwise coalescence times,
`𝔼[C i j] = θ / (2 L) * (t̄ i· + t̄ ·j - t i j - t̄ ··)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.CoalescentFStatistics.McVeanModel.integral_genCov`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/CoalescentFStatistics.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html#integral-gen-cov).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coalescence times, f-statistics and PCA](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/coalescence-times-f-statistics-and-pca)
