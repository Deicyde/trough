---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.genotype, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.kinship, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.inbreeding, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.grm, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.grmDiag, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_allele, MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_allele_mul
statement: formalized
proof: formalized
---

# Genomic relationship matrices

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html).

## Relatedness

## Malécot's identity-by-descent model

Malécot's identity-by-descent model at one biallelic locus, at the level of second
moments. The individuals are `ι`; individual `i` carries the gene copies `(i, 0)` (paternal) and
`(i, 1)` (maternal), and `allele c ∈ {0, 1}` indicates the reference allele on copy `c`. The
reference allele has frequency `p ∈ (0, 1)` (a polymorphic locus), and `ibd c d` is the
probability that the copies `c` and `d` are identical by descent: IBD copies carry the same
allele and non-IBD copies are independent draws with frequency `p` (Malécot 1948), which gives
the second moments `𝔼[a_c a_d] = p² + p (1 - p) ibd c d`. Only these first and second moments
are assumed. `ibd` is determined by the moments (`p (1 - p) ≠ 0`), and `ibd c c = 1`
(`IBDModel.ibd_self`). In Malécot's model `ibd c d ∈ [0, 1]`; the structure does not require
this, and the identities below hold for any real `ibd` (for example a correlation relative to a
reference population, which can be negative). A monomorphic locus (`p ∈ {0, 1}`) is excluded:
there the GRM denominator `2p(1 - p)` vanishes.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#ibdmodel).

## Genotype of an individual at a biallelic locus

The genotype (reference-allele count) `x_i ∈ {0, 1, 2}` of individual `i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.genotype`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#genotype).

## Kinship coefficient

The kinship coefficient `φ_ij`: the probability that a copy drawn at random from `i` and a
copy drawn at random from `j` are identical by descent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.kinship`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#kinship).

## Inbreeding coefficient

The inbreeding coefficient `F_i`: the probability that the two copies of `i` are identical
by descent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.inbreeding`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#inbreeding).

## Genetic relationship matrix entry

The genetic relationship matrix entry of Yang et al. (2010) at one locus,
`A_ij = (x_i - 2p)(x_j - 2p) / (2p(1 - p))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.grm`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#grm).

## GCTA diagonal relationship estimator

The diagonal estimator of GCTA (Yang et al. 2011) at one locus,
`A_ii = 1 + (x_i² - (1 + 2p) x_i + 2p²) / (2p(1 - p))`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.grmDiag`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#grm-diag).

## Integrability of allele indicators

The allele indicators are integrable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_allele`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integrable-allele).

## Integrability of products of allele indicators

Products of allele indicators are integrable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_allele_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integrable-allele-mul).

## A gene copy is identical by descent with itself

A gene copy is identical by descent with itself: `ibd c c = 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.ibd_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#ibd-self).

## Symmetry of identity by descent

Identity by descent is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.ibd_comm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#ibd-comm).

## Self-kinship equals $(1 + F_i)/2$

`φ_ii = (1 + F_i) / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.kinship_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#kinship-self).

## Symmetry of kinship

Kinship is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.kinship_comm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#kinship-comm).

## Integrability of genotypes

Genotypes are integrable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_genotype`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integrable-genotype).

## Integrability of products of genotypes

Products of genotypes are integrable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integrable_genotype_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integrable-genotype-mul).

## Expected genotype equals $2p$

`𝔼[x_i] = 2p`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_genotype`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-genotype).

## Second moment of genotypes in terms of kinship

`𝔼[x_i x_j] = 4p² + 4p(1 - p) φ_ij`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_genotype_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-genotype-mul).

## The genetic relationship covariance

**The genetic relationship covariance** (Yang et al. 2010):
`𝔼[(x_i - 2p)(x_j - 2p)] = 2p(1 - p) · 2 φ_ij`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_centered_mul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-centered-mul).

## The GRM is unbiased for twice the kinship

**The GRM is unbiased for twice the kinship** (Yang et al. 2010):
`𝔼[A_ij] = 2 φ_ij`, for every pair `i, j` (including `i = j`, where `2 φ_ii = 1 + F_i`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_grm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-grm).

## Diagonal GRM entry is unbiased for $1 + F_i$

The diagonal GRM entry is unbiased for `1 + F_i`: `𝔼[A_ii] = 1 + F_i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_grm_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-grm-self).

## The KING moment

**The KING moment** (Manichaikul et al. 2010), general form:
`𝔼[(x_i - x_j)²] = 2p(1 - p)(1 + F_i) + 2p(1 - p)(1 + F_j) - 8p(1 - p) φ_ij`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_sub_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-sub-sq).

## The KING moment

**The KING moment** (Manichaikul et al. 2010) for two non-inbred individuals:
`𝔼[(x_i - x_j)²] = 4p(1 - p)(1 - 2φ_ij)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_sub_sq_of_inbreeding_eq_zero`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-sub-sq-of-inbreeding-eq-zero).

## The GCTA diagonal estimator is unbiased for `1 + F_i`

**The GCTA diagonal estimator is unbiased for `1 + F_i`** (Yang et al. 2011):
`𝔼[1 + (x_i² - (1 + 2p) x_i + 2p²) / (2p(1 - p))] = 1 + F_i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Relatedness.IBDModel.integral_grmDiag`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Relatedness.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Relatedness.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html#integral-grm-diag).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Genomic relationship matrices](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/quantitative-genetics/genomic-relationship-matrices)
