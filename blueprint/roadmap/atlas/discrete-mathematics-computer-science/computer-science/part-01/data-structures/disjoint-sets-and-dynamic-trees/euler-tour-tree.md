---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.EulerTourTree.Tree, Cslib.Algorithms.Lean.EulerTourTree.Tree.children_ind, Cslib.Algorithms.Lean.EulerTourTree.Tree.root, Cslib.Algorithms.Lean.EulerTourTree.Tree.children, Cslib.Algorithms.Lean.EulerTourTree.Tree.size, Cslib.Algorithms.Lean.EulerTourTree.Tree.verticesAux, Cslib.Algorithms.Lean.EulerTourTree.Tree.vertices, Cslib.Algorithms.Lean.EulerTourTree.Tree.verticesAux_eq
statement: formalized
proof: formalized
---

# Euler tour tree

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html).

## Euler Tour Tree

## Rooted ordered tree

A rooted ordered tree with vertices in a type $V$ consists of a root
vertex in $V$ together with an ordered list of child subtrees, each a rooted ordered tree with
vertices in $V$.

Vertex labels need not be distinct.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tree).

## Induction principle for rooted trees

Let $P$ be a property of trees. Suppose that for
every vertex $r$ and all trees $c_1, \dots, c_k$ (with $k \ge 0$), if $P$ holds for each $c_i$, then
$P$ holds for the tree with root $r$ and child subtrees $c_1, \dots, c_k$. Then $P$ holds for every
tree.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.children_ind`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#children-ind).

## Root of a rooted tree

The root of the tree with root vertex $r$ and child subtrees
$c_1, \dots, c_k$ is the vertex $r$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.root`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#root).

## Children of a rooted tree

The children of a tree are the child subtrees of its root, as a
list in their given order.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.children`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#children).

## Size of a rooted tree

The size of a tree is its number of nodes, counting repeated vertex
labels with multiplicity: the tree with root $r$ and child subtrees $c_1, \dots, c_k$ has size
$1 + \sum_{i=1}^{k} \operatorname{size}(c_i)$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#size).

## Accumulator preorder traversal

For a rooted ordered tree $t$ with root $r$ and child
subtrees $c_1, \dots, c_k$ (in order) and a list $a$, the accumulator traversal $T(t, a)$ is
the list whose first entry is $r$ and whose remaining entries are
$T(c_1, T(c_2, \dots, T(c_k, a) \dots))$; when $k = 0$ the remaining entries are $a$.

The list $T(t, a)$ equals the preorder vertex list of $t$ followed by $a$, so the preorder list
is computed in linear time rather than by repeatedly appending child lists.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.verticesAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#vertices-aux).

## Preorder vertex list of a rooted tree

The preorder vertex list of a rooted ordered tree
$t$ is the accumulator preorder traversal of $t$ started from the empty list.

Equivalently, it is the root of $t$ followed by the preorder vertex lists of its child subtrees
in order; repeated vertex labels appear with multiplicity.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.vertices`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#vertices).

## Accumulator preorder traversal is append

For every rooted ordered tree $t$ and every
list $a$, the accumulator preorder traversal of $t$ started from $a$ equals the preorder vertex
list of $t$ followed by $a$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.verticesAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#vertices-aux-eq).

## Preorder vertex list of a node

For a vertex $r$ and rooted ordered trees
$c_1, \dots, c_k$, the preorder vertex list of the tree with root $r$ and child subtrees
$c_1, \dots, c_k$ (in order) is $r$ followed by the concatenation of the preorder vertex lists
of $c_1, \dots, c_k$, in this order.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.vertices_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#vertices-node).

## Euler tour with an accumulator

Let $t$ be a tree with root $r$ and child subtrees
$c_1, \dots, c_k$ in order, and let $a$ be a list of vertices. For a list $L$ of vertices, write
$r \cdot L$ for the list $L$ with $r$ put in front. The Euler tour of $t$ with accumulator $a$,
written $T(t, a)$, is $r \cdot L_1$, where $L_{k+1} = a$ and $L_i = T(c_i, r \cdot L_{i+1})$ for
$i = k, \dots, 1$.

It equals the Euler tour of $t$ followed by $a$, and computes the Euler tour without repeatedly
concatenating the tours of the child subtrees.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.tourAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tour-aux).

## Euler tour

The Euler tour of a tree $t$ with root $r$ and child subtrees
$c_1, \dots, c_k$ in order is the list of vertices consisting of $r$, followed, for each
$i = 1, \dots, k$ in turn, by the Euler tour of $c_i$ and then $r$. It is the vertex sequence of
the depth-first walk that returns to the parent vertex after each child subtree.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.tour`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tour).

## Accumulator lemma for the Euler tour

For every tree $t$ and every list $a$ of vertices,
the Euler tour of $t$ with accumulator $a$ equals the Euler tour of $t$ followed by $a$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.tourAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tour-aux-eq).

## Recursive formula for the Euler tour

For a vertex $r$ and a list of trees
$c_1, \dots, c_k$, the Euler tour of the tree with root $r$ and child subtrees $c_1, \dots, c_k$
in order is $r$, followed, for each $i = 1, \dots, k$ in turn, by the Euler tour of $c_i$ and
then $r$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.tour_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tour-node).

## Arc sequence of the Euler tour

The arc sequence of a tree $t$ is the list of consecutive
pairs of its Euler tour: if the Euler tour of $t$ is $v_0, v_1, \dots, v_k$, then the arc sequence
of $t$ is $(v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k)$.

Each tree edge occurs once in each direction.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.arcTour`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#arc-tour).

## Arc sequence as the zipped Euler tour

For every tree $t$, the arc sequence of $t$ is
the Euler tour of $t$ zipped with its own tail: if the Euler tour of $t$ is $v_0, v_1, \dots, v_k$,
then the arc sequence of $t$ is $(v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k)$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.arcTour_eq_zip`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#arc-tour-eq-zip).

## The Euler tour visits exactly the vertices of the tree

For every tree $t$ and every $v$,
$v$ occurs in the Euler tour of $t$ if and only if $v$ is a vertex of $t$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.mem_tour_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#mem-tour-iff).

## Valid Euler-tour tree

A rooted ordered tree is valid when its list of vertices in
preorder has no duplicates, that is, every vertex label occurs at most once in the tree.

Raw trees may repeat vertex labels; reading the linking of two trees as a link in a dynamic
forest requires valid trees with disjoint vertex sets.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#valid).

## Valid trees have distinct vertices

A tree $t$ is valid if and only if its list of
vertices in preorder has no repeated entries.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.valid_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#valid-iff).

## A single-vertex tree is valid

For every vertex $r$, the tree with root $r$ and no child
subtrees is valid.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.valid_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#valid-singleton).

## Linking two rooted trees

Let $t_1$ be a tree with root $r$ and child subtrees
$c_1, \dots, c_k$, and let $t_2$ be a tree. The link of $t_1$ and $t_2$ is the tree with root $r$
and child subtrees $c_1, \dots, c_k, t_2$, so $t_2$ becomes the new last child subtree of the root
of $t_1$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.link`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#link).

## Linking valid trees with disjoint vertices gives a valid tree

Let $t_1$ and $t_2$ be
valid trees such that no vertex of $t_1$ is a vertex of $t_2$. Then the link of $t_1$ and $t_2$,
that is, $t_1$ with $t_2$ added as the last child subtree of its root, is valid.

This is the forest precondition for reading the link as a link of two trees in a dynamic
forest.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.valid_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#valid-link).

## Linking two copies of a single vertex is not valid

For every vertex $r$, the link of the
single-vertex tree with root $r$ and another single-vertex tree with root $r$ is not valid, since
the vertex $r$ occurs twice in it. Hence the link of two valid trees need not be valid when their
vertex sets are not disjoint.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.not_valid_link_same_root`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#not-valid-link-same-root).

## Splicing two Euler tours

For lists $\tau_1$ and $\tau_2$ of vertices and a vertex $r$,
the splice of $\tau_1$ and $\tau_2$ at $r$ is the list consisting of the entries of $\tau_1$,
followed by the entries of $\tau_2$, followed by $r$.

It is used with $\tau_1$ and $\tau_2$ the Euler tours of two trees and $r$ the root of the first
tree: walk the first tour, then the second tour, then return to $r$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.spliceLink`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#splice-link).

## Euler tour of a linked tree

For trees $t_1$ and $t_2$, let $t$ be the link of $t_1$ and
$t_2$, that is, $t_1$ with $t_2$ added as the last child subtree of its root. The Euler tour of
$t$ is the Euler tour of $t_1$, followed by the Euler tour of $t_2$, followed by the root of
$t_1$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.tour_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#tour-link).

## Cutting the last child subtree

Let $t$ be a tree with root $r$ and child subtrees
$c_1, \dots, c_k$. Cutting the last child subtree of $t$ gives no result when $k = 0$; when
$k \ge 1$ it gives the pair consisting of the tree with root $r$ and child subtrees
$c_1, \dots, c_{k-1}$, together with the removed subtree $c_k$.

Formalized by `Cslib.Algorithms.Lean.EulerTourTree.Tree.cutLast`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/EulerTourTree.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html#cut-last).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler tour tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/euler-tour-tree)
