---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.cellSum, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pairSum, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pairSum_eq_sum_cellSum, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pad, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.autocorrDFT, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.autocorrDFT_eq, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.meanGeno, Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.sampleCov
statement: formalized
proof: formalized
---

# Fourier computation of weighted linkage disequilibrium

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html).

## Binning by grid-cell offset

## Total of a per-SNP quantity over a grid cell

The total `U k = ∑_{x : c x = k} u x` of a per-SNP quantity `u` over grid cell `k`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.cellSum`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#cell-sum).

## Brute-force pair sum at a cell offset

The brute-force sum `∑_{x, y : c y = c x + j} u x v y` over ordered SNP pairs whose grid
cells differ by `j`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pairSum`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#pair-sum).

## Pair sum as cross-correlation of cell totals

Grouping pairs by cell offset: if every SNP lies in a cell `c x < K`, the pair sum at
offset `j` is the lag-`j` cross-correlation of the cell totals.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pairSum_eq_sum_cellSum`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#pair-sum-eq-sum-cell-sum).

## Zero padding of a sequence to $\mathbb{Z}/N\mathbb{Z}$

Zero padding: the sequence `U` read on `ZMod N` through `k ↦ U k.val`. When `U` vanishes
from `K` on and `K ≤ N`, this is `U` followed by `N - K` zeros.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pad`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#pad).

## Autocorrelation via the discrete Fourier transform

The transform computation of the lag-`j` autocorrelation: the inverse discrete Fourier
transform of the power spectrum `|𝓕 Ũ|^2` of the zero-padded sequence, read at `j`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.autocorrDFT`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#autocorr-dft).

## Zero-padded circular autocorrelation equals linear autocorrelation

Zero-padded circular autocorrelation equals the linear one: if `U k = 0` for `k ≥ K`,
`2 K ≤ N + 1` and `j < K`, then `𝓕⁻(|𝓕 Ũ|^2)(j) = ∑_{k < K} U k U (k + j)`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.autocorrDFT_eq`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#autocorr-dft-eq).

## Sample mean genotype at a SNP

The sample mean genotype `ḡ(x) = (1/m) ∑ i, g i x` at SNP `x` over `m` individuals.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.meanGeno`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#mean-geno).

## Unbiased sample covariance of genotypes

The unbiased sample covariance `ẑ(x, y) = (1/(m - 1)) ∑ i, (g i x - ḡ x) (g i y - ḡ y)`
of the genotypes at SNPs `x` and `y` (Loh et al. 2013, Eq. 5; meaningful for `m ≥ 2`).

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.sampleCov`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#sample-cov).

## Brute-force weighted linkage disequilibrium sum

The brute-force weighted-LD sum at cell offset `j`:
`∑_{x, y : c y = c x + j} ẑ(x, y) w(x) w(y)`, costing a pass over all pairs.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.bruteWeightedLD`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#brute-weighted-ld).

## Centred weighted genotype

The centred weighted genotype `(g i x - ḡ x) w x` of individual `i` at SNP `x`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.centredWeighted`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#centred-weighted).

## ALDER's Fourier-transform weighted LD computation

ALDER's transform algorithm: for each individual, the zero-padded autocorrelation of the
cell totals of its centred weighted genotypes, computed through `𝓕`; summed over individuals
and divided by `m - 1`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.dftWeightedLD`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#dft-weighted-ld).

## ALDER's transform algorithm equals the brute-force weighted LD

The transform algorithm computes the brute-force weighted-LD sum exactly, for every lag
`j < K`, when all SNPs lie in cells `c x < K` and the transform length satisfies
`2 K ≤ N + 1`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.dftWeightedLD_eq_bruteWeightedLD`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#dft-weighted-ld-eq-brute-weighted-ld).

## Number of SNP pairs at a cell offset

The number of ordered SNP pairs at cell offset `j`, by which ALDER divides the weighted
sum.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.pairCount`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#pair-count).

## Pair count as autocorrelation of cell occupancy counts

The pair count is the zero-padded autocorrelation of the cell occupancy counts.

Formalized by `Cslib.Bioinformatics.PopulationStructure.WeightedLDFFT.autocorrDFT_cellCount`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/WeightedLDFFT.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html#autocorr-dft-cell-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier computation of weighted linkage disequilibrium](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/fourier-computation-of-weighted-linkage-disequil)
