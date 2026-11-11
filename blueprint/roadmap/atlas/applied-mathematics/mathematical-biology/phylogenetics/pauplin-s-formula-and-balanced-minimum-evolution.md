---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.pauplinCoeff, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.length, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.leaves, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.pairs, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.kraft, MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.length
statement: formalized
proof: formalized
---

# Pauplin's formula and balanced minimum evolution

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html).

## Balanced Minimum Evolution

## Rooted binary tree with edge lengths

A rooted binary tree with leaf labels in `X`; `node a l b r` has the child `l` at the end of
an edge of length `a` and the child `r` at the end of an edge of length `b`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree`, an inductive type declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#rtree).

## Unrooted binary tree with edge lengths

An unrooted binary tree, rooted at its edge of length `len` that joins the roots of the
rooted binary trees `left` and `right`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree`, a structure declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#utree).

## Pauplin coefficient of a pair of leaves

The Pauplin coefficient `2 ^ (1 - τ)` of a pair of leaves at topological distance `τ`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.pauplinCoeff`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#pauplin-coeff).

## Total edge length of a rooted binary tree

The total length of the edges.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.length`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#length).

## Leaves of a rooted binary tree with root distances

The leaves, each with its label, its distance to the root and its number of edges to the
root.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.leaves`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#leaves).

## Leaf pairs of a rooted binary tree with path lengths

The unordered pairs of leaves, each with the two labels, the length of the path between the
two leaves and its number of edges.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.pairs`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#pairs).

## Kraft's equality

**Kraft's equality** for a rooted binary tree: `∑_{leaves} 2^{-depth} = 1`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.RTree.kraft`, a theorem declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#kraft).

## Total edge length of an unrooted binary tree

The total length of the edges.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.length`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#length-2).

## Leaf labels of an unrooted binary tree

The leaf labels (with multiplicity).

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.labels`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#labels).

## Leaf pairs of an unrooted binary tree with path lengths

The unordered pairs of leaves, each with the two labels, the length `d_T(i, j)` of the path
between the two leaves and its number of edges `τ_ij`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.pairs`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#pairs-2).

## Balanced minimum-evolution length

The **balanced minimum-evolution length** of the topology of `T` for a dissimilarity `d`
(Desper and Gascuel 2002): `∑_{i<j} 2^{1-τ_ij} (d(i, j) + d(j, i)) / 2`. It depends on `T`
only through the topological distances `τ_ij`. Each term is symmetrized, so the value does
not depend on the orientation `T.pairs` happens to assign to a pair: swapping the children of
a node, or the two sides of the root edge, leaves `bmeLength` unchanged.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.bmeLength`, a definition declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#bme-length).

## Pauplin's formula

**Pauplin's formula** (Pauplin 2000): the total edge length of a binary tree with real edge
lengths is `∑_{i<j} 2^{1-τ_ij} d_T(i, j)`, the sum over pairs of leaves of the path length
weighted by `2` to the power one minus the number of edges on the path.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.bmeLength_pathLength`, a theorem declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#bme-length-path-length).

## The balanced minimum-evolution length of a tree metric is the tree length

If `d` is the
path-length dissimilarity of `T` on its leaves and `d` is symmetric, `bmeLength T d = length T`.
Symmetry is needed because `bmeLength` averages the two orientations of each pair.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.bmeLength_eq_length`, a theorem declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#bme-length-eq-length).

## Kraft equality

**Kraft equality** for unrooted binary trees: for every leaf `i` of a tree with distinct leaf
labels, `∑_{j ≠ i} 2^{1-τ_ij} = 1`.

Formalized by `MathlibExt.Biology.Phylogenetics.BalancedMinimumEvolution.UTree.kraft_leaf`, a theorem declared in [MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/BalancedMinimumEvolution.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html#kraft-leaf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pauplin's formula and balanced minimum evolution](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/phylogenetics/pauplin-s-formula-and-balanced-minimum-evolution)
