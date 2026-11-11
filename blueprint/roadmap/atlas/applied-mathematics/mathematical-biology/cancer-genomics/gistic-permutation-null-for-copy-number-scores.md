---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.GisticNull.permutedScore, MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull, MathlibExt.Biology.CancerGenomics.GisticNull.scoreCount, MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_eq_count, MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_zero, MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_succ, MathlibExt.Biology.CancerGenomics.GisticNull.windowMin, MathlibExt.Biology.CancerGenomics.GisticNull.geneNull_eq_count
statement: formalized
proof: formalized
---

# GISTIC permutation null for copy-number scores

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html).

## Permuted GISTIC score at a marker

The permuted score at marker `m`: `∑ j, x j (σ j m)`.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.permutedScore`, a definition declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#permuted-score).

## GISTIC permutation null distribution

The GISTIC permutation null at marker `m`: the probability that `∑ j, x j (σ j m) = g`
when the permutations `σ j` of the markers are independent and uniform.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull`, a definition declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#permutation-null).

## Count of marker choices with a given score

The number of marker choices `u : Fin S → Fin M` (one marker per sample) with
`∑ j, x j (u j) = g`.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.scoreCount`, a definition declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#score-count).

## The GISTIC permutation null is the law of a sum of independent per-sample draws

(Mermel et al. 2011): the probability of the score `g` is the fraction of the `M ^ S` marker
choices with that score, whatever the marker `m`.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_eq_count`, a theorem declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#permutation-null-eq-count).

## GISTIC null with no samples is a point mass at zero

With no samples the null is the point mass at `0`.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_zero`, a theorem declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#permutation-null-zero).

## Convolution step

Adding sample `S` convolves the null of the first `S` samples with
the empirical law of the new sample, `P_{S+1}(g) = ∑_v (1 / M) P_S(g - x_S(v))`.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.permutationNull_succ`, a theorem declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#permutation-null-succ).

## Window minimum over consecutive markers

The minimum of `y` over the window of `n + 1` consecutive markers starting at `i`
(GeneGISTIC's per-sample gene-level value for a gene covering those markers).

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.windowMin`, a definition declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#window-min).

## GeneGISTIC null

**GeneGISTIC null** (Mermel et al. 2011): permuting the per-sample minima of all running
windows of `n + 1` markers gives, at every window `i`, the law of a sum of independent draws
of one window minimum per sample.

Formalized by `MathlibExt.Biology.CancerGenomics.GisticNull.geneNull_eq_count`, a theorem declared in [MathlibExt/Biology/CancerGenomics/GisticNull.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/GisticNull.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html#gene-null-eq-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: GISTIC permutation null for copy-number scores](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/gistic-permutation-null-for-copy-number-scores)
