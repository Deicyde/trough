---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree, MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.leaves, MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.leaves_ne_zero, MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.Swap, MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.On, MathlibExt.Biology.Phylogenetics.TreeCount.RootedBinaryTree, MathlibExt.Biology.Phylogenetics.TreeCount.nat_card_rootedBinaryTree, MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.UnrootedBinaryTree
statement: formalized
proof: formalized
---

# Counting binary phylogenetic trees

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html).

## Planar rooted binary tree with labeled leaves

A planar rooted binary tree with leaves labeled by `α`: a leaf `leaf a`, or an internal
vertex `node l r` with left subtree `l` and right subtree `r` (the children are ordered).

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree`, an inductive type declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#plane-tree).

## Leaf labels of a planar binary tree

The multiset of leaf labels.

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.leaves`, a definition declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#leaves).

## Every planar binary tree has a leaf

Every planar tree has at least one leaf.

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.leaves_ne_zero`, a theorem declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#leaves-ne-zero).

## Swap of the children of an internal vertex

One swap: exchange the two children of one internal vertex (anywhere in the tree).

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.Swap`, an inductive type declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#swap).

## Planar drawings of rooted binary trees on a taxon set

The planar drawings of rooted binary trees on the taxa `X`: planar trees whose leaves are
labeled by `X`, each taxon labeling exactly one leaf.

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.PlaneTree.On`, a definition declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#on).

## Rooted binary phylogenetic tree

The **rooted binary phylogenetic trees** on the taxa `X`: planar drawings with leaf set `X`
modulo exchanging the two children of internal vertices, i.e. rooted binary trees with
unordered children and leaves labeled bijectively by `X`, up to label-preserving isomorphism.

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.RootedBinaryTree`, a definition declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#rooted-binary-tree).

## Schröder's count of rooted binary phylogenetic trees

On `n ≥ 1` labeled taxa there are
`(2 n - 3)‼ = 1 · 3 · 5 ⋯ (2 n - 3)` rooted binary phylogenetic trees (`1` tree for `n = 1`
and `n = 2`, `3` for `n = 3`, `15` for `n = 4`). For `n = 1` the natural-number subtraction
gives `2 - 3 = 0` and `0‼ = 1`, the conventional value `(-1)‼ = 1` of the formula; the empty
set of taxa (excluded here) has no tree (`isEmpty_rootedBinaryTree_empty`).

## Sources

- Semple & Steel (2003), Proposition 2.1.4.

Formalized by `MathlibExt.Biology.Phylogenetics.TreeCount.nat_card_rootedBinaryTree`, a theorem declared in [MathlibExt/Biology/Phylogenetics/TreeCount.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/TreeCount.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#nat-card-rooted-binary-tree).

## Unrooted binary phylogenetic tree

An **unrooted binary phylogenetic tree** on the taxa `X`: a finite tree `G` on a vertex
type `V` whose degree-one vertices are labeled bijectively by `X` (`label`) and whose other
vertices all have degree three.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.UnrootedBinaryTree`, a structure declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#unrooted-binary-tree).

## Isomorphism of unrooted binary phylogenetic trees

Two unrooted binary phylogenetic trees are **isomorphic** when some graph isomorphism maps
the leaf with each label to the leaf with the same label.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.UnrootedBinaryTree.Iso`, a definition declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#iso).

## Binary hierarchy on a finite set

A **binary hierarchy** on a finite set `S`: a family of nonempty subsets of `S` containing
`S` and every singleton, any two members nested or disjoint, and every member with at least two
elements the disjoint union of two members. These are the cluster systems of the rooted binary
phylogenetic trees on `S` (Semple & Steel 2003, Section 3.1).

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.IsBinaryHierarchy`, a definition declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#is-binary-hierarchy).

## Binary hierarchy restricted below a member is a binary hierarchy

The members of a binary hierarchy below a member form a binary hierarchy.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.isBinaryHierarchy_filter`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#is-binary-hierarchy-filter).

## The number of binary hierarchies

On a nonempty finite set `S` there are
`(2 |S| - 3)‼` binary hierarchies, as many as rooted binary phylogenetic trees on `S`: a tree
corresponds to the leaf sets of its subtrees.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.nat_card_binaryHierarchy`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#nat-card-binary-hierarchy).

## Cluster of a vertex seen from a leaf

The **cluster** of a vertex `v` seen from the leaf labeled `a`: the taxa `x ≠ a` whose leaf
lies beyond `v`, i.e. `v` is on the path from the leaf `a` to the leaf `x`.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.cluster`, a definition declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#cluster).

## Cluster set of a tree seen from a leaf

The clusters of all vertices seen from the leaf labeled `a`. (The cluster of the leaf `a`
itself is the set of all other taxa, which is also the cluster of its neighbor.)

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.clusterSet`, a definition declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#cluster-set).

## Isomorphic trees have the same clusters

Isomorphic trees have the same clusters.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.clusterSet_eq_of_iso`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#cluster-set-eq-of-iso).

## Clusters of an unrooted tree form a binary hierarchy

The clusters of a tree seen from a leaf form a binary hierarchy on the other taxa
(Semple & Steel 2003, Section 3.1).

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.isBinaryHierarchy_clusterSet`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#is-binary-hierarchy-cluster-set).

## Clusters determine an unrooted binary tree

Two trees with the same clusters seen from the leaf `a` are isomorphic: the clusters
determine the tree.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.iso_of_clusterSet_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 1060](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L1060). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#iso-of-cluster-set-eq).

## Every binary hierarchy is a cluster set of a tree

Every binary hierarchy on the taxa other than `a` is the cluster set, seen from the leaf
`a`, of some unrooted binary phylogenetic tree (vertices: the leaf `a` and the members of the
hierarchy; each member is joined to the smallest member strictly containing it).

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.exists_clusterSet_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 1528](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L1528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#exists-cluster-set-eq).

## Unrooted binary trees correspond to binary hierarchies

Unrooted binary phylogenetic trees up to label-preserving isomorphism correspond to the
binary hierarchies on the taxa other than `a`, by their clusters seen from the leaf `a`.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.quotEquivHierarchy`, a definition declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 1609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L1609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#quot-equiv-hierarchy).

## Number of unrooted binary phylogenetic trees

The count `(2 n - 5)‼` of unrooted binary phylogenetic trees holds from `n = 2` taxa on:
for `n = 2` the single tree is one edge and `2 · 2 - 5 = 0` in `ℕ`, `0‼ = 1` (the conventional
value `(-1)‼ = 1`). For `n ≤ 1` there is no tree while the formula gives `1`.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.nat_card_unrootedBinaryTree_of_two_le`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 1628](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L1628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#nat-card-unrooted-binary-tree-of-two-le).

## The number of unrooted binary phylogenetic trees

On `n ≥ 3` labeled taxa there are
`(2 n - 5)‼ = 1 · 3 ⋯ (2 n - 5)` unrooted binary phylogenetic trees up to label-preserving
isomorphism.

## Sources

- Semple & Steel (2003), Proposition 2.1.4. Proves the deferred entry `nat_card_unrootedBinaryTree`.

Formalized by `MathlibExt.Biology.Phylogenetics.UnrootedTreeCount.nat_card_unrootedBinaryTree`, a theorem declared in [MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean, line 1642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Phylogenetics/UnrootedTreeCount.lean#L1642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html#nat-card-unrooted-binary-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting binary phylogenetic trees](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/phylogenetics/counting-binary-phylogenetic-trees)
