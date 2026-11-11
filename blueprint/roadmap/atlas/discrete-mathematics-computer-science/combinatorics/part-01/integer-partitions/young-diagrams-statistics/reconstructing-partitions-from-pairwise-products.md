---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.pairwiseProducts, MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.partition_eq_of_pairwiseProducts_eq_of_max_eq, MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.partition_pairwiseProducts_eq_iff
statement: formalized
---

# Reconstructing partitions from pairwise products

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products/index.html).

## Pairwise products of a multiset

If a multiset $s$ of natural numbers consists of
$x_1, \dots, x_k$, listed with multiplicity, then the pairwise products of $s$ form the multiset
of the products $x_i x_j$ over all pairs of indices $1 \le i < j \le k$; equal elements at
different positions give separate products, and the result is empty when $k < 2$.

Applied to the parts of a partition $\lambda$, this gives the parts of the partition
$\mathrm{pre}_2(\lambda)$ of Li's note on multiset reconstruction.

Formalized by `MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.pairwiseProducts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products/index.html#pairwise-products).

## Li's lemma: reconstruction from the largest part and pairwise products

Let $n$ be a
positive integer and let $\lambda$ and $\mu$ be partitions of $n$ with a common largest part,
that is, some $a$ is a part of both $\lambda$ and $\mu$ and no part of either exceeds $a$. If the
pairwise products of the parts of $\lambda$ and the pairwise products of the parts of $\mu$ form
the same multiset, then $\lambda = \mu$.

## Sources

- Stella Jiahui Li, "A Note on Multiset Reconstruction from Pairwise Products and Total Sum", Lemma 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.partition_eq_of_pairwiseProducts_eq_of_max_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products/index.html#partition-eq-of-pairwise-products-eq-of).

## Li's theorem: partitions are determined by their pairwise products

Let $n$ be a positive
integer and let $\lambda$ and $\mu$ be partitions of $n$. The pairwise products of the parts of
$\lambda$ and the pairwise products of the parts of $\mu$ form the same multiset if and only if
$\lambda = \mu$.

## Sources

- Stella Jiahui Li, "A Note on Multiset Reconstruction from Pairwise Products and Total Sum", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.Partition.MultisetReconstructionPairwiseProductsWanted.partition_pairwiseProducts_eq_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/MultisetReconstructionPairwiseProductsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products/index.html#partition-pairwise-products-eq-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reconstructing partitions from pairwise products](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/reconstructing-partitions-from-pairwise-products)
