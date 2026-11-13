---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.freqA, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.freqB, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.varA, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.varB, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.ldD, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.addA, MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.addB
statement: formalized
proof: formalized
---

# Dominance linkage disequilibrium

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html).

## Dominance LD

## Two-locus diploid genotype under random union of gametes

A diploid two-locus genotype under random union of gametes: the haplotypes
`(X₁, Y₁)` and `(X₂, Y₂)` are independent and identically distributed, with square-integrable
allele codings.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#random-union).

## Allele frequency at the first locus

The allele frequency (mean coding) `p = E X₁` at locus `A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.freqA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#freq-a).

## Allele frequency at the second locus

The allele frequency (mean coding) `q = E Y₁` at locus `B`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.freqB`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#freq-b).

## Haplotype variance at the first locus

The haplotype variance `V_A = E (X₁ - p)²` at locus `A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.varA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#var-a).

## Haplotype variance at the second locus

The haplotype variance `V_B = E (Y₁ - q)²` at locus `B`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.varB`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#var-b).

## Gametic linkage disequilibrium

The gametic linkage disequilibrium `D = E (X₁ - p) (Y₁ - q)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.ldD`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#ld-d).

## Additive coding at the first locus

The additive coding `a_A = (X₁ - p) + (X₂ - p)` (centred allele count) at locus `A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.addA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#add-a).

## Additive coding at the second locus

The additive coding `a_B = (Y₁ - q) + (Y₂ - q)` at locus `B`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.addB`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#add-b).

## Dominance coding at the first locus

The dominance coding `d_A = (X₁ - p) (X₂ - p)` at locus `A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.domA`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#dom-a).

## Dominance coding at the second locus

The dominance coding `d_B = (Y₁ - q) (Y₂ - q)` at locus `B`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.domB`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#dom-b).

## Additive linkage disequilibrium is twice the gametic one

Additive LD: `E(a_A a_B) = 2 D`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_addA_mul_addB`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-add-a-mul-add-b).

## Second moment of the additive coding at the first locus

The additive coding has second moment `E(a_A²) = 2 V_A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_addA_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-add-a-sq).

## Second moment of the additive coding at the second locus

The additive coding has second moment `E(a_B²) = 2 V_B`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_addB_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-add-b-sq).

## Dominance linkage disequilibrium is the square of the gametic one

Dominance LD: `E(d_A d_B) = D²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_domA_mul_domB`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-dom-a-mul-dom-b).

## Second moment of the dominance coding at the first locus

The dominance coding has second moment `E(d_A²) = V_A²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_domA_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-dom-a-sq).

## Second moment of the dominance coding at the second locus

The dominance coding has second moment `E(d_B²) = V_B²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_domB_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-dom-b-sq).

## Additive and dominance codings at different loci are uncorrelated

The additive coding at `A` and the dominance coding at `B` are uncorrelated:
`E(a_A d_B) = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.integral_addA_mul_domB`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#integral-add-a-mul-dom-b).

## Correlation of additive codings equals the gametic correlation

The correlation of the additive codings is the gametic correlation
`r = D / √(V_A V_B)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.addCorr_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#add-corr-eq).

## Dominance LD is the square of additive LD

**Dominance LD is the square of additive LD** (Palmer et al. 2023, graphical abstract): the
correlation of the dominance codings at two loci is the square of the correlation of their
additive codings.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.RandomUnion.domCorr_eq_addCorr_sq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#dom-corr-eq-add-corr-sq).

## Dominance encoding of a biallelic genotype

The dominance encoding of a biallelic genotype `g ∈ {0, 1, 2}` (count of the allele with
frequency `p`): `p²`, `-p (1 - p)`, `(1 - p)²`. Dividing by `-p (1 - p)` gives the encoding
`-p / (1 - p)`, `1`, `-(1 - p) / p` of Palmer et al. (2023).

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.dominanceEncoding`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#dominance-encoding).

## Dominance coding of allele indicators equals the dominance encoding

For `0`/`1` allele indicators the dominance coding `(X₁ - p) (X₂ - p)` depends only on the
genotype `X₁ + X₂` and equals its dominance encoding.

Formalized by `MathlibExt.Biology.StatisticalGenetics.DominanceLD.domCode_eq_dominanceEncoding`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/DominanceLD.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html#dom-code-eq-dominance-encoding).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dominance linkage disequilibrium](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/dominance-linkage-disequilibrium)
