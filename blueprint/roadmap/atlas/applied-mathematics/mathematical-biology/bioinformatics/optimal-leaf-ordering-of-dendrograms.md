---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.leaves, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.numInternal, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.orderings, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.adjScore, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optScore, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optEnds, Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.joinEnds
statement: formalized
proof: formalized
---

# Optimal leaf ordering of dendrograms

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html).

## Optimal Leaf Ordering

## Dendrogram as a leaf-labeled binary tree

A rooted binary tree whose leaves are labeled by `α`: the shape of a dendrogram
(merge heights are irrelevant for leaf ordering).

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram`, an inductive type declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#dendrogram).

## Leaves of a dendrogram

The leaves of a dendrogram, left to right.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.leaves`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#leaves).

## Number of internal nodes of a dendrogram

The number of internal (merge) nodes.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.numInternal`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#num-internal).

## Leaf orderings of a dendrogram

The leaf orders obtained by choosing, at each internal node, which child is drawn first.
Each choice pattern contributes one entry, so the list has `2 ^ numInternal t` entries.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.Dendrogram.orderings`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#orderings).

## Adjacent-similarity score of a leaf order

The score of a leaf order: the sum of the similarities of adjacent leaves.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.adjScore`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#adj-score).

## Optimal leaf-ordering score

The best score among the leaf orders of `t` (never `⊥`: `optScore_ne_bot`).

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optScore`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#opt-score).

## Optimal leaf-ordering score with fixed end leaves

The best score among the leaf orders of `t` that start with `i` and end with `j`
(`⊥` if there is none).

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optEnds`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#opt-ends).

## Joining two subtree orders at an adjacent leaf pair

One side of the recursion: the left part ranges over orders of a subtree with leaves `Ll`
and best-score table `Ml`, the right part over a subtree with leaves `Lr` and table `Mr`; the
two are joined at the adjacent pair `(k, l)`.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.joinEnds`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#join-ends).

## Bar-Joseph–Gifford–Jaakkola dynamic program for leaf ordering

The dynamic program of Bar-Joseph, Gifford and Jaakkola: `bestEnds S t i j` is computed
from the tables of the two children, trying both child orders.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.bestEnds`, a definition declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#best-ends).

## A dendrogram with m internal nodes has $2^m$ leaf orders

A dendrogram with `m` internal nodes has `2 ^ m` leaf orders (one per flip pattern).

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.length_orderings`, a theorem declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#length-orderings).

## Leaf orders are permutations of the leaves

Every leaf order of `t` is a permutation of its leaves.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.perm_of_mem_orderings`, a theorem declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#perm-of-mem-orderings).

## Correctness of the optimal leaf ordering recursion

**Correctness of the optimal leaf ordering recursion** (Bar-Joseph, Gifford and
Jaakkola 2001): the dynamic program computes, for every end pair `(i, j)`, the best score of
a leaf order of `t` starting at `i` and ending at `j`.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.bestEnds_eq_optEnds`, a theorem declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#best-ends-eq-opt-ends).

## Optimal leaf-ordering score via the dynamic program

The optimal leaf-ordering score is the best `bestEnds` value over end pairs of leaves.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optScore_eq_sup_bestEnds`, a theorem declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#opt-score-eq-sup-best-ends).

## Optimal leaf-ordering score is finite

Every dendrogram has a leaf order, so the optimal score is a real number.

Formalized by `Cslib.Bioinformatics.Clustering.OptimalLeafOrdering.optScore_ne_bot`, a theorem declared in [CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Clustering/OptimalLeafOrdering.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html#opt-score-ne-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Optimal leaf ordering of dendrograms](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/optimal-leaf-ordering-of-dendrograms)
