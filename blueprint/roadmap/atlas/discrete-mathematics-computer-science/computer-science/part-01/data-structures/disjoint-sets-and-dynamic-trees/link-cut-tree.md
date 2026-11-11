---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.LinkCutTree.spine, Cslib.Algorithms.Lean.LinkCutTree.ofVertexList, Cslib.Algorithms.Lean.LinkCutTree.findTree, Cslib.Algorithms.Lean.LinkCutTree.removeTree, Cslib.Algorithms.Lean.LinkCutTree.perm_flatMap_removeTree, Cslib.Algorithms.Lean.LinkCutTree.findSubtree, Cslib.Algorithms.Lean.LinkCutTree.Adjacent, Cslib.Algorithms.Lean.LinkCutTree.Adjacent.mem_left
statement: formalized
proof: formalized
---

# Link-cut tree

83 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html).

## Link Cut Tree

## Path tree on a vertex list

For a vertex $r$ and a list of vertices $c_1, \dots, c_k$, the
spine is the rooted tree $r \to c_1 \to \cdots \to c_k$: its root is $r$, each vertex has the next
one in the list as its only child, and the last vertex ($c_k$, or $r$ when $k = 0$) is a leaf.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.spine`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#spine).

## Forest from a vertex list

The forest built from the empty list is empty; the forest
built from a list $r, c_1, \dots, c_k$ consists of the single spine
$r \to c_1 \to \cdots \to c_k$, the rooted tree in which each vertex has the next one as
its only child.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.ofVertexList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#of-vertex-list).

## Tree of a forest containing a vertex

For a vertex $x$ and a forest given as a list of
trees, the first tree whose vertices contain $x$, or nothing when no tree contains $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.findTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#find-tree).

## Removing the trees that contain a vertex

Given a vertex $x$ and a forest, given as a list
of rooted ordered trees, removing the trees containing $x$ deletes from the list every tree that
has $x$ among its vertices and keeps the remaining trees in their original order.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.removeTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#remove-tree).

## Removing the tree containing a vertex splits the forest's vertices

Let $f$ be a forest of
rooted ordered trees whose concatenated vertex lists have no duplicates, let $x$ be a vertex, and
let $t$ be the first tree of $f$ containing $x$. Then the concatenated vertex list of the forest
obtained from $f$ by removing every tree containing $x$, followed by the vertex list of $t$, is a
permutation of the concatenated vertex list of $f$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.perm_flatMap_removeTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#perm-flat-map-remove-tree).

## Subtree rooted at a vertex

For a vertex $x$ and a tree $T$, the subtree of $T$ rooted at
the first occurrence of $x$ in preorder, or nothing when $x$ does not occur in $T$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.findSubtree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#find-subtree).

## Adjacency in a rooted tree

Two vertices $a$ and $b$ are adjacent in a rooted tree $t$
when they are joined by a parent-child edge of $t$ in either direction: some node of $t$
labelled $a$ has a child labelled $b$, or some node of $t$ labelled $b$ has a child labelled $a$.

This is the undirected edge relation that the structural operations of the link-cut tree are
specified against.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.Adjacent`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent).

## The first endpoint of a tree edge is a vertex

If $a$ and $b$ are adjacent in a tree
$t$, that is, joined by a parent-child edge in either direction, then $a$ is a vertex of
$t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.Adjacent.mem_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-left).

## Adjacency in a tree is symmetric

For every rooted ordered tree $T$ and vertices $a$ and
$b$, if $a$ and $b$ are adjacent in $T$ (joined by a parent-child edge in either direction), then
$b$ and $a$ are adjacent in $T$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.Adjacent.symm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#symm).

## The second endpoint of a tree edge is a vertex

If $a$ and $b$ are adjacent in a tree
$t$, that is, joined by a parent-child edge in either direction, then $b$ is a vertex of
$t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.Adjacent.mem_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-right).

## Adjacency test

For vertices $a$, $b$ and a rooted tree $t$ with root $r$ and child
subtrees $c_1, \dots, c_k$, the adjacency test of $a$ and $b$ in $t$ returns true exactly when
$r = a$ and some $c_i$ has root $b$, or $r = b$ and some $c_i$ has root $a$, or the adjacency test
of $a$ and $b$ returns true in some $c_i$.

It returns true exactly when $a$ and $b$ are adjacent in $t$, and it is the guard checked by the
edge cut before it cuts.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.adjacentB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-b).

## Grafting a tree below a vertex

For a vertex $y$ and trees $N$ and $T$, grafting $N$ at
$y$ in $T$ attaches $N$ as a new last child of the first node of $T$ labelled $y$ in preorder,
keeping every existing node and edge; it returns nothing when $y$ does not occur in $T$. This is
the tree surgery behind linking two trees: it adds exactly the edge from $y$ to the root of $N$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.graftAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 852](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L852). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#graft-at).

## Vertices after grafting

Let $t$ and $C$ be trees and $y$ a vertex. If grafting $C$ at
$y$ in $t$, that is, attaching $C$ as a new last child of a node labelled $y$, produces the
tree $t'$, then for every $v$, $v$ is a vertex of $t'$ if and only if $v$ is a vertex of $t$ or
a vertex of $C$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.mem_vertices_graftAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 963](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L963). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-vertices-graft-at).

## Grafting keeps the root

Let $T$ and $N$ be rooted ordered trees and $y$ a vertex. If
grafting $N$ into $T$ at $y$ is defined and yields the tree $T'$, then the root of $T'$ equals the
root of $T$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.root_graftAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1006](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1006). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#root-graft-at).

## Edges after grafting

Let $t$ and $u$ be rooted trees and $y$ a vertex, and suppose that
grafting $u$ as a new child under $y$ in $t$ succeeds and yields the tree $t'$. Then for all
vertices $a$ and $b$, the vertices $a$ and $b$ are adjacent in $t'$ if and only if they are
adjacent in $t$, or adjacent in $u$, or $a = y$ and $b$ is the root of $u$, or $a$ is the root of
$u$ and $b = y$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.adjacent_graftAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-graft-at).

## Grafting adds the new subtree's vertices

Let $t$ and $s$ be rooted ordered trees and $y$
a vertex. If grafting $s$ as a new child at $y$ in $t$ succeeds and yields the tree $t'$, then the
vertex list of $t'$ is a permutation of the vertex list of $t$ followed by the vertex list of
$s$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.perm_vertices_graftAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#perm-vertices-graft-at).

## Rerooting a tree at a vertex

For a vertex $x$ and a rooted ordered tree $T$ with root $r$,
rerooting $T$ at $x$ is defined recursively. If $r = x$, the result is $T$ itself. Otherwise let
$C$ be the first child subtree of $r$ that contains $x$, let $p$ be the root of $C$, and let $C'$
be $C$ rerooted at $x$. The result is $C'$ with the tree formed by $r$ and its remaining
children (in their original order) attached as a new last child of the first node of $C'$, in
preorder, labelled $p$. If no child subtree of $r$ contains $x$, rerooting is undefined; thus
rerooting is defined exactly when $x$ is a vertex of $T$.

When the vertices of $T$ are distinct, this reverses the edges on the path from $r$ to $x$ and
keeps every other edge, so the undirected tree is unchanged and only the root moves to $x$. This
is the tree surgery behind making $x$ the root in a link-cut tree.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.rerootAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#reroot-at).

## Rerooting fails at an absent vertex

For every rooted ordered tree $T$ and every vertex $x$
that is not a vertex of $T$, rerooting $T$ at $x$ is undefined (it returns no tree).

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.rerootAt_eq_none_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#reroot-at-eq-none-of-not-mem).

## Rerooting preserves the vertex set

Let $t$ be a rooted tree and $x$ a vertex. If
rerooting $t$ at $x$ yields the tree $t'$, then a vertex lies in $t'$ if and only if it
lies in $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.mem_vertices_rerootAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-vertices-reroot-at).

## Rerooting keeps every edge

Let $t$ be a rooted tree with no repeated vertex, and suppose
that rerooting $t$ at a vertex $x$ yields the tree $t'$. Then for all vertices $a$ and $b$, the
vertices $a$ and $b$ are adjacent in $t'$ if and only if they are adjacent in $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.adjacent_rerootAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1618](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-reroot-at).

## Rerooting preserves the vertices

Let $t$ be a rooted ordered tree and $x$ a vertex. If
rerooting $t$ at $x$ yields the tree $t'$, then the vertex list of $t'$ is a permutation of the
vertex list of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.perm_vertices_rerootAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1758](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1758). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#perm-vertices-reroot-at).

## Pruning the subtrees rooted at a vertex

For a vertex $x$ and a rooted ordered tree $T$,
pruning $T$ at $x$ removes every subtree of $T$ whose root is labelled $x$, keeping every other
node and edge and the order of children. If the root of $T$ is $x$, nothing remains and pruning
is undefined. Otherwise the result is the tree with the same root whose children are, in their
original order, the pruned children of the root, with the children labelled $x$ dropped.

This is the tree surgery behind the remainder side of the cut operation of a link-cut tree.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.pruneAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#prune-at).

## Pruning at an absent vertex changes nothing

Let $t$ be a rooted ordered tree and $x$ a
vertex that does not occur in $t$. Then pruning the subtrees rooted at $x$ from $t$ succeeds and
returns $t$ itself.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.pruneAt_eq_self_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1811](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1811). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#prune-at-eq-self-of-not-mem).

## Vertices of a pruned tree

Let $t$ be a rooted tree and $x$ a vertex. If pruning
$t$ at $x$ leaves the tree $t'$, then every vertex of $t'$ is a vertex of $t$ and is
different from $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.mem_vertices_pruneAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-vertices-prune-at).

## Pruning keeps the vertices outside the detached subtree

Let $t$ be a rooted tree
whose preorder vertex list has no repeated vertex, and let $x$ be a vertex. Suppose the
subtree search finds the subtree $s$ of $t$ rooted at $x$, and pruning $t$ at $x$ leaves
the tree $t'$. Then every vertex of $t$ that is not a vertex of $s$ is a vertex of $t'$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.mem_vertices_pruneAt_of_mem_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 1944](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L1944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-vertices-prune-at-of-mem-not-mem).

## Pruning a subtree splits the vertex list

Let $t$ be a rooted ordered tree whose vertex
list has no duplicates and let $x$ be a vertex. If $x$ occurs in $t$, with $s$ the subtree of $t$
rooted at $x$, and pruning at $x$ leaves a tree $t'$ (that is, $x$ is not the root of $t$), then
the vertex list of $t$ is a permutation of the vertex list of $t'$ followed by the vertex list
of $s$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.perm_vertices_pruneAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#perm-vertices-prune-at).

## Pruning keeps the root

Let $T$ be a rooted ordered tree and $x$ a vertex. If pruning $T$ at
$x$ yields a tree $T'$ (that is, the root of $T$ is not $x$), then the root of $T'$ equals the root
of $T$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.root_pruneAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#root-prune-at).

## Pruning keeps surviving edges

Let $t$ be a rooted tree with no repeated vertex and $x$ a
vertex, and suppose that removing every subtree rooted at $x$ from $t$ leaves the tree $t'$ (that
is, the root of $t$ is not $x$). If $a$ and $b$ are adjacent in $t$ and both are vertices of
$t'$, then $a$ and $b$ are adjacent in $t'$.

Together with the fact that every vertex of $t'$ is a vertex of $t$ other than $x$, this
specifies pruning at the level of edges on the surviving vertices.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.adjacent_pruneAt_of_mem_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-prune-at-of-mem-mem).

## Root-to-vertex path

For a vertex $x$ and a rooted ordered tree $T$, the root path of $x$ is
defined exactly when $x$ is a vertex of $T$. It is then the list of vertices on the path from the
root of $T$ down to $x$, root first and ending with $x$; if $x$ occurs more than once, the path
leads to its first occurrence in preorder.

This is the preferred path installed by the access operation of a link-cut tree.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.rootPath`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#root-path).

## A root path ends at its target

If $p$ is the path from the root of a tree $T$ down to a
vertex $x$ of $T$, then $p$ is nonempty and its last (deepest) vertex is $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.getLast?_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#get-last-root-path).

## The root path starts at the root

Let $t$ be a tree and $x$ a vertex. If the root path
of $x$ in $t$ (the path from the root of $t$ down to $x$) is defined and equals $p$, then $p$ is
nonempty and its first vertex is the root of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.head?_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#head-root-path).

## Root paths stay inside the tree

If $p$ is the path in a tree $t$ from the root down to
a vertex $x$, then every vertex of $p$ is a vertex of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.mem_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-root-path).

## Root paths have distinct vertices

If the preorder vertex list of a rooted tree $t$
has no repeated vertex and $p$ is the path from the root of $t$ down to a vertex $x$, then
$p$ has no repeated vertex.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.nodup_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#nodup-root-path).

## Consecutive vertices of a root path are adjacent

Let $t$ be a tree and $x$ a vertex. If
the root path of $x$ in $t$ is defined and equals $p = (p_0, \dots, p_k)$, then for every
$i < k$ the vertices $p_i$ and $p_{i+1}$ are adjacent in $t$, that is, joined by a parent-child
edge of $t$ in one direction or the other.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.isChain_adjacent_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#is-chain-adjacent-root-path).

## Parent-child relation in a rooted tree

For vertices $a$ and $b$ and a rooted ordered
tree $t$, $a$ is a parent of $b$ in $t$ when some node of $t$ labelled $a$ has a child subtree
whose root is $b$. Preferred edges of a link-cut tree are directed this way, from a node to its
preferred child.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.ParentChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#parent-child).

## Parent-child edges are edges

For every rooted tree $t$ and all vertices $a$ and $b$, if
$a$ is the parent of $b$ somewhere in $t$, then $a$ and $b$ are adjacent in $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.ParentChild.adjacent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-2).

## The parent endpoint of a tree edge is a vertex

If $a$ is the parent of $b$ somewhere
in a tree $t$, then $a$ is a vertex of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.ParentChild.mem_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2552](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-left-2).

## The child endpoint of a tree edge is a vertex

If $a$ is the parent of $b$ somewhere in
a tree $t$, then $b$ is a vertex of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.ParentChild.mem_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2558](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-right-2).

## A root path follows parent-child edges downward

Let $t$ be a tree and $x$ a vertex. If
the root path of $x$ in $t$ is defined and equals $p = (p_0, \dots, p_k)$, then for every
$i < k$ the vertex $p_i$ is the parent of $p_{i+1}$ somewhere in $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.isChain_parentChild_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2564](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#is-chain-parent-child-root-path).

## Consecutive edges of a vertex path

For a list of vertices $v_0, v_1, \dots, v_n$, its
path edges are the ordered pairs $(v_0, v_1), (v_1, v_2), \dots, (v_{n-1}, v_n)$ of consecutive
vertices, in this order; a list with at most one vertex has no path edges. For a path listed from
the root downward each pair is (parent, child), and the preferred edges installed by an access to
a vertex $x$ are the path edges of the root-to-$x$ path.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.pathEdges`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2592](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#path-edges).

## Preferred-path decomposition of a tree

Given a list $E$ of preferred edges, each a pair
(parent, preferred child), the decomposition of a tree $T$ is a pair (down, rest): down is the
preferred path that starts at the root of $T$ and follows edges of $E$ downward, and rest is the
list of all other preferred paths of $T$. When a node has several children joined to it by edges
of $E$ (excluded in valid states, where each vertex has at most one preferred child), the first
one in child order continues the path through that node and each of the others starts its own
path in rest.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.decomp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#decomp).

## Preferred paths of a tree

Let $t$ be a rooted ordered tree and let $E$ be a list of
preferred edges, each a pair (parent, child). The preferred paths of $t$ under $E$ are listed
as follows: first the downward path of the preferred-path decomposition of $t$ under $E$, which
starts at the root of $t$ and follows preferred edges downward, and then all other paths of
that decomposition, in the order the decomposition returns them.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.treePaths`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2748](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#tree-paths).

## The downward preferred path starts at the root

For every list of preferred edges, the
downward preferred path in the preferred-path decomposition of a tree is nonempty and its first
vertex is the root of the tree.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.decomp_fst_head?`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2752](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#decomp-fst-head).

## Preferred paths permute the vertex list

For every list of preferred edges, the downward
preferred path of a tree followed by the concatenation of the other paths of its preferred-path
decomposition is a permutation of the vertex list of the tree.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.decomp_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2977](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#decomp-perm).

## The preferred paths of a tree rearrange its vertex list

For every list $E$ of directed
edges and every rooted ordered tree $t$, the concatenation of the preferred paths of $t$ under
$E$ is a permutation of the preorder vertex list of $t$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.perm_treePaths_flatMap`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 2997](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L2997). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#perm-tree-paths-flat-map).

## Decomposition paths are paths of the tree

For every list of preferred edges, in the
preferred-path decomposition of a tree $T$, the downward preferred path and every other path are
paths of $T$: any two consecutive vertices are joined by a parent-child edge of $T$, in either
direction.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.decomp_isChain`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3012](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3012). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#decomp-is-chain).

## Preferred paths of a tree follow tree edges

Let $t$ be a tree and $E$ any list of pairs
of vertices, read as preferred (parent, child) edges. For every path $p = (p_0, \dots, p_k)$ in
the preferred-path decomposition of $t$ under $E$ and every $i < k$, the vertices $p_i$ and
$p_{i+1}$ are adjacent in $t$, that is, joined by a parent-child edge of $t$ in one direction
or the other.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.isChain_of_mem_treePaths`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3063](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3063). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#is-chain-of-mem-tree-paths).

## Access edges make the root path the downward preferred path

Let $T$ be a tree whose
vertex list is duplicate-free, let $x$ be a vertex of $T$ with root path $p$ (the path from the
root of $T$ down to $x$), and let $E$ be a list of directed edges such that every consecutive
pair of $p$, parent first, lies in $E$, and every edge of $E$ whose first vertex lies on $p$ is
such a consecutive pair. Then the downward preferred path of the preferred-path decomposition of
$T$ under $E$ is $p$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.decomp_fst_eq_rootPath`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3076](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3076). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#decomp-fst-eq-root-path).

## Link-cut tree state

A state of a link-cut tree over a vertex type $V$ consists of the
represented forest, a list of rooted ordered trees with vertices in $V$, and a list of preferred
(solid) edges, each a pair $(u, v)$ of vertices meant as the edge from a node $u$ to its preferred
child $v$ in the represented forest; the structure itself does not require these pairs to be
edges of the forest. The preferred-path decomposition is derived from the preferred edges as the
maximal solid chains in each represented tree. With no preferred edges, every edge is dashed
and every vertex is its own singleton path.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#state).

## Vertex of a link-cut tree state

A vertex $x$ belongs to a link-cut tree state $s$
when $x$ is a vertex of some tree of the represented forest of $s$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem).

## Connectivity in a link-cut tree state

Two vertices $x$ and $y$ are connected in a
link-cut tree state $s$ when some tree of the represented forest of $s$ has both $x$ and $y$
among its vertices.

Connectivity is the abstraction against which the link-cut tree operations are specified.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Connected`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#connected).

## Connectivity via Euler tours

For a link-cut tree state $s$ and vertices $x$ and $y$,
$x$ and $y$ are connected in $s$ if and only if some tree of the represented forest of $s$
contains both $x$ and $y$ in its Euler tour.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.connected_iff_tour`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#connected-iff-tour).

## Valid link-cut tree states

A link-cut tree state $s$ is valid when four conditions
hold: the concatenation of the vertex lists of the trees of its represented forest has no
duplicates (so the trees are vertex-disjoint); its list of preferred edges has no duplicates;
every preferred edge $(a, b)$ is a parent-child edge of some tree of the represented forest,
with $a$ the parent of $b$; and any two preferred edges with the same parent are equal, so each
vertex has at most one preferred child.

The duplicate-free vertex condition also pins down the parent of each vertex, so the maximal
chains of preferred edges in each tree are genuine disjoint paths.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#valid).

## Validity of states with no preferred edges

Let $s$ be a link-cut tree state whose list
of preferred edges is empty. If the concatenation of the vertex lists of the trees of the
represented forest of $s$ has no duplicates, then $s$ is valid.

This is the situation after every structural operation, which resets all edges to dashed.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.valid_of_preferred_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#valid-of-preferred-nil).

## Preferred-path decomposition of a link-cut tree state

For a link-cut tree state $s$, its
preferred paths are obtained by taking, for each represented tree of $s$ in forest order, the
preferred paths of that tree under the preferred edges of $s$, and concatenating these lists.
Within a tree these are its maximal chains of preferred edges when each vertex has at most one
preferred child, each listed from its shallowest to its deepest vertex; a vertex incident to no
preferred edge forms a singleton path.

The decomposition keeps the preferred paths of every subtree, not one distinguished path, so an
access changes only the preferred edges leaving vertices of the accessed root path.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.paths`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#paths).

## Preferred paths cover exactly the vertices of the forest

For every link-cut tree state
$s$ and every vertex $v$, $v$ lies on some path of the preferred-path decomposition of $s$ if
and only if $v$ is a vertex of some tree of the represented forest of $s$. No validity
hypothesis on $s$ is needed.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.mem_paths_flatMap`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-paths-flat-map).

## Preferred paths cover each vertex at most once

In a valid link-cut tree state, the
concatenation of all preferred paths of the decomposition has no repeated vertex: no vertex
occurs twice on one path or on two different paths.

Together with the fact that every vertex of the represented forest lies on some preferred
path, the preferred paths partition the vertex set.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.nodup_paths_flatMap`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#nodup-paths-flat-map).

## Preferred paths are pairwise vertex-disjoint

In a valid link-cut tree state, any two
preferred paths at different positions of the preferred-path decomposition have no vertex in
common.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.pairwise_disjoint_paths`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#pairwise-disjoint-paths).

## Preferred paths have distinct vertices

Every preferred path of a valid state has
distinct vertices.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.nodup_of_mem_paths`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#nodup-of-mem-paths).

## Preferred paths of a link-cut tree state follow represented edges

Let $s$ be a link-cut
tree state. For every path $p = (p_0, \dots, p_k)$ in the preferred-path decomposition of $s$
and every $i < k$, some represented tree of $s$ has $p_i$ and $p_{i+1}$ adjacent, that is,
joined by a parent-child edge in one direction or the other.

This holds for every state, with no validity hypothesis.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.isChain_of_mem_paths`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#is-chain-of-mem-paths).

## Access in a link-cut tree

Let $s$ be a link-cut tree state and $x$ a vertex. If $x$ is a
vertex of some tree of the represented forest of $s$, let $T$ be the first such tree and let $p$
be the path in $T$ from its root down to $x$. Accessing $x$ keeps the represented forest and
replaces the preferred edges by those preferred edges of $s$ whose parent endpoint is not on $p$,
followed by the edges of $p$, each directed from parent to child. If $x$ is not a vertex of the
represented forest, accessing $x$ leaves $s$ unchanged.

Thus every edge of the root-to-$x$ path becomes preferred, the previously preferred child edges
of the vertices on that path are dropped, and preferred edges hanging off the path survive: in
the tree with root $1$, whose children are $2$ and $3$, where $4$ is a child of $2$ and $5$ a
child of $3$, accessing $5$ after accessing $4$ keeps the preferred path $[2, 4]$, since the edge
from $2$ to $4$ has its parent endpoint off the path $1, 3, 5$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.access`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#access).

## Access keeps off-path preferred edges

Let $s$ be a link-cut tree state, $x$ a vertex,
and $(u, w)$ a preferred edge of $s$, directed from the parent $u$ to the child $w$. Suppose
that, if some tree of the represented forest of $s$ contains $x$, then $u$ does not lie on the
path in the first such tree from its root down to the first occurrence of $x$ in preorder. Then
$(u, w)$ is still a preferred edge after accessing $x$.

This is the edge-level fact behind the persistence of off-path preferred paths across
accesses.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.mem_preferred_access`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-preferred-access).

## Access makes the root path preferred

Let $s$ be a link-cut tree state and $x$ a
vertex, let $t$ be the first tree of the represented forest of $s$ that contains $x$, and let
$p$ be the path in $t$ from the root down to the first occurrence of $x$ in preorder. Then every
edge of $p$, taken as the pair (parent, child) of consecutive vertices of $p$, is a preferred
edge of the state obtained from $s$ by accessing $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.mem_preferred_access_of_mem_pathEdges`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-preferred-access-of-mem-path-edges).

## Access leaves the represented forest unchanged

For every link-cut tree state $s$ and
every vertex $x$, accessing $x$ changes only the preferred edges: the represented forest of the
resulting state equals the represented forest of $s$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.access_forest`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#access-forest).

## After access, the accessed vertex ends its preferred path

Let $s$ be a valid link-cut
tree state and let $x$ be a vertex of its represented forest. Then, after accessing $x$, the
preferred-path decomposition of the new state contains a path $p$ whose last vertex is $x$, and
$p$ is the path from the root down to $x$ in some tree of the represented forest of $s$.

Paths are listed from the root downward, so $x$ is the deepest vertex of $p$. No auxiliary splay
tree is modeled, so this is only the endpoint property of the accessed preferred path.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.access_last`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#access-last).

## Access preserves validity

If a link-cut tree state $s$ is valid, then for every vertex
$x$ the state obtained from $s$ by accessing $x$ is again valid.

The new preferred edges are the retained off-path edges together with the edges of the accessed
root path; the two groups have disjoint parent endpoints (off versus on the path), so
duplicate-freeness and the at-most-one-preferred-child condition carry over.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid.access`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#access-2).

## Making a vertex the root in a link-cut tree state

Given a vertex $x$ and a state $s$,
the state $\operatorname{makeRoot}(x, s)$ has no preferred edges (all edges dashed), and its
forest is defined as follows. If $x$ is not a vertex of the forest, the forest is unchanged.
Otherwise the first represented tree containing $x$ is rerooted at $x$: the edges on the path
from its old root to $x$ are reversed, and when the tree has distinct vertices every undirected
edge is kept. The rerooted tree replaces every tree containing $x$ and is placed at the end of
the forest.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.makeRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3528](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#make-root).

## Making a vertex the root installs a tree rooted there

Let $s$ be a link-cut tree state
and $x$ a vertex of its represented forest. After making $x$ the root, some represented tree
has root $x$ and contains $x$ as a vertex.

That tree is the rerooted old tree of $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.makeRoot_root`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3549](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#make-root-root).

## Making a vertex the root keeps its connections

Let $s$ be a valid link-cut tree state
and let $x$ and $y$ be connected in $s$. Then $x$ and $y$ are still connected in the state
obtained from $s$ by making $x$ the root of its represented tree.

Rerooting spans the same vertex set as the old tree and keeps every undirected edge; vertex
disjointness of the represented trees pins down which tree contains $x$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.connected_makeRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#connected-make-root).

## Rerooting a link-cut tree state preserves validity

For every valid link-cut tree state
$s$ and every vertex $x$, the state obtained from $s$ by making $x$ the root of its represented
tree is valid.

The new forest has the same flat vertex list as the old one up to permutation (the rerooted tree
replaces its original), and the preferred edges are reset.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid.makeRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#make-root-2).

## Linking two trees of a link-cut tree state

Given vertices $x$ and $y$ and a state $s$,
the state $\operatorname{link}(x, y, s)$ has no preferred edges (all edges dashed), and its
forest is defined as follows. If $x$ or $y$ is not a vertex of the forest, the forest is
unchanged. Otherwise let $t_x$ and $t_y$ be the first represented trees containing $x$ and $y$.
If $x$ is a vertex of $t_y$, the forest is unchanged. Otherwise $t_x$ is rerooted at $x$ (the
edges on its old root-to-$x$ path are reversed, so $x$ becomes its root), the result is
attached as a new last child subtree of the first node labelled $y$ in $t_y$, which adds the
edge from $y$ to $x$, and this joined tree replaces every tree containing $x$ or $y$, placed at
the end of the forest.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.link`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3619](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#link).

## Linking connects the endpoints

Let $s$ be a link-cut tree state and let $x$ and $y$ be
vertices of its represented forest. Then in the state obtained from $s$ by linking $x$ to $y$,
the vertices $x$ and $y$ are connected, that is, some represented tree contains both. No
invariant on the state is needed.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.connected_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#connected-link).

## Linking in a link-cut tree preserves validity

For every valid link-cut tree state $s$
and all vertices $x$ and $y$, the state obtained from $s$ by linking $x$ and $y$ is valid.

The joined tree has the union of the two old vertex lists up to permutation (rerooting and
grafting both permute), the rest of the forest is untouched, and the preferred edges are
reset.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid.link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3674](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#link-2).

## Cutting off the subtree at a vertex

Cutting at a vertex $x$ resets the preferred edges
of the state to the empty list and changes its forest as follows. If no tree of the forest
contains $x$, the forest is unchanged. Otherwise let $T$ be the first tree containing $x$ and
$S$ the first subtree of $T$ rooted at $x$ in preorder. Every tree containing $x$ is removed from
the forest, and two trees are appended at the end: first the remainder of $T$ with every subtree
rooted at $x$ pruned off, then $S$. When $x$ is the root of $T$ nothing remains, and only $S$ is
appended.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.cut`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3769](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut).

## A cut disconnects a vertex from everything outside its subtree

Let $s$ be a
link-cut tree state, let $t$ be the first tree of its represented forest containing the
vertex $x$, and let $u$ be the first subtree of $t$ in preorder whose root is $x$. After
cutting $s$ at $x$, the vertex $x$ is not connected to any vertex $y$ that is not a vertex
of $u$.

No invariant on the state is needed.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.not_connected_cut`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3802](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3802). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#not-connected-cut).

## Both sides of a cut remain in the forest

Let $s$ be a link-cut tree state, let $x$ and
$y$ be vertices, and let $t$ be the first tree of the represented forest of $s$ that contains
$x$. Suppose no vertex occurs twice in $t$, and let $T_x$ be the subtree of $t$ rooted at $x$.
If $y$ is a vertex of $t$ but not of $T_x$, then after cutting $s$ at $x$ both $x$ and $y$ are
vertices of the represented forest.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.mem_cut`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3836](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#mem-cut).

## Cutting preserves validity

If $s$ is a valid link-cut tree state, then for every vertex
$x$ the state obtained from $s$ by cutting off the subtree rooted at $x$ is again valid.

Pruning splits the vertices of the cut tree into those of the remainder and those of the
detached subtree, the rest of the forest is untouched, and the preferred edges are reset.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid.cut`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3883](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3883). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut-2).

## Cutting an edge of a link-cut tree

For vertices $x$ and $y$ and a link-cut tree state
$s$, cutting the edge between $x$ and $y$ works as follows. If $x$ and $y$ are adjacent in some
tree of the represented forest of $s$, the result is obtained from $s$ by first making $x$ the
root of its represented tree and then cutting off the subtree rooted at $y$. Otherwise the
represented forest is left unchanged. In both cases the list of preferred edges becomes empty.

When $x$ and $y$ are joined by an edge of a valid state, making $x$ the root turns $y$ into the
root of a child subtree of $x$, so the cut separates the two sides of the edge between $x$ and
$y$ and keeps every other edge.

The adjacency test is necessary: without it the composite would cut at $y$ regardless of $x$.
For instance, on the chain $1 \to 2$ it would detach $2$ when asked to cut the edge between
$99$ and $2$, although there is no such edge.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.cutEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3964](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut-edge).

## Edge cut on an adjacent pair

Let $s$ be a link-cut tree state and let $x$ and $y$ be
adjacent in some tree of the represented forest of $s$. Then cutting the edge between $x$ and
$y$ in $s$ gives the same state as first making $x$ the root of its represented tree and then
cutting off the subtree rooted at $y$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.cutEdge_eq_cut_makeRoot_of_adjacent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3987](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut-edge-eq-cut-make-root-of-adjacent).

## Edge cut on a non-adjacent pair

Let $s$ be a link-cut tree state and let $x$ and $y$ be
adjacent in no tree of the represented forest of $s$. Then cutting the edge between $x$ and $y$
in $s$ leaves the represented forest unchanged and makes the list of preferred edges empty.

In particular, no other edge at $y$ is cut.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.cutEdge_eq_of_not_adjacent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 3996](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L3996). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut-edge-eq-of-not-adjacent).

## Edge cutting preserves validity

If $s$ is a valid link-cut tree state, then for all
vertices $x$ and $y$ the state obtained from $s$ by cutting the edge between $x$ and $y$ is
again valid.

On an adjacent pair the edge cut makes $x$ the root of its tree and then cuts off the subtree
rooted at $y$; otherwise it only resets the preferred edges.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.Valid.cutEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 4007](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L4007). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#cut-edge-2).

## Cutting an edge separates its endpoints

Let $s$ be a valid link-cut tree state and
let $x$ and $y$ be adjacent in some tree of the represented forest of $s$. After the edge
cut of $x$ and $y$ in $s$, the vertices $x$ and $y$ are not connected: no represented tree
contains both.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.not_connected_cutEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 4042](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L4042). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#not-connected-cut-edge).

## An edge cut keeps every other edge

Let $s$ be a valid link-cut tree state and let $x$ and
$y$ be adjacent in some tree of its represented forest. If $a$ and $b$ are adjacent in some tree
of the represented forest of $s$, and neither $a = x$ and $b = y$ nor $a = y$ and $b = x$, then
$a$ and $b$ are adjacent in some tree of the represented forest obtained from $s$ by cutting the
edge between $x$ and $y$.

Edges of other trees pass through untouched; edges of the cut tree survive the rerooting at $x$
and then lie on one side of the prune at $y$, and the only edge crossing the prune is the edge
between $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.LinkCutTree.State.adjacent_cutEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean, line 4090](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LinkCutTree.lean#L4090). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html#adjacent-cut-edge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Link-cut tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/link-cut-tree)
