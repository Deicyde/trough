---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BallTree, Cslib.Algorithms.Lean.BallTree.toListAux, Cslib.Algorithms.Lean.BallTree.toList, Cslib.Algorithms.Lean.BallTree.size, Cslib.Algorithms.Lean.BallTree.length_toList, Cslib.Algorithms.Lean.BallTree.distSq, Cslib.Algorithms.Lean.BallTree.distSq_comm, Cslib.Algorithms.Lean.BallTree.distSq_le_two_mul
statement: formalized
proof: formalized
---

# Ball tree

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html).

## Ball Tree

## Ball tree

For a dimension $d$, a ball tree over the integer points $\mathbb{Z}^d$
(functions $\{0, \dots, d-1\} \to \mathbb{Z}$) is either empty, a leaf holding one point,
or a node holding a center point $c \in \mathbb{Z}^d$, a natural number $b$ (the squared-radius
bound of the node's sphere) and two child ball trees.

That the sphere around $c$ actually contains the points below the node is a separate validity
invariant, not part of this definition.

Formalized by `Cslib.Algorithms.Lean.BallTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#ball-tree).

## Accumulating traversal of a ball tree

For a ball tree $T$ and a list $A$ of points, the
accumulating traversal returns $A$ when $T$ is empty, the point $p$ followed by $A$ when $T$ is a
leaf holding $p$, and, when $T$ is a node with children $L$ and $R$, the accumulating traversal of
$L$ whose accumulator is the accumulating traversal of $R$ with accumulator $A$.

The result is the leaf points of $T$, from left to right, followed by $A$.

Formalized by `Cslib.Algorithms.Lean.BallTree.toListAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#to-list-aux).

## Point list of a ball tree

The point list of a ball tree is the list of the points held
at its leaves, from left to right: the empty tree gives the empty list, a leaf holding $p$ gives
the list $[p]$, and a node gives the point list of its left subtree followed by the point list of
its right subtree. The centers stored at nodes are not included.

Formalized by `Cslib.Algorithms.Lean.BallTree.toList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#to-list).

## Size of a ball tree

The size of a ball tree is the number of points held in its leaves:
it is $0$ for the empty tree, $1$ for a leaf, and the sum of the sizes of the two children for a
node; the center of a node is not counted.

Formalized by `Cslib.Algorithms.Lean.BallTree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#size).

## Number of points of a ball tree

For every ball tree $t$, the list of points stored in
$t$, read from left to right, has length equal to the size of $t$.

Formalized by `Cslib.Algorithms.Lean.BallTree.length_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#length-to-list).

## Squared Euclidean distance

For points $p, q \in \mathbb{Z}^d$, the squared distance
from $p$ to $q$ is the natural number $\sum_{i=0}^{d-1} (p_i - q_i)^2$, computed in
$\mathbb{Z}$ and then converted to $\mathbb{N}$.

Formalized by `Cslib.Algorithms.Lean.BallTree.distSq`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#dist-sq).

## Symmetry of squared distance

For all points $p, q \in \mathbb{Z}^d$, the squared
distance from $p$ to $q$ equals the squared distance from $q$ to $p$.

Formalized by `Cslib.Algorithms.Lean.BallTree.distSq_comm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#dist-sq-comm).

## Relaxed triangle inequality for squared distance

For all points
$a, b, c \in \mathbb{Z}^d$, writing $\delta(x, y)$ for the squared distance from $x$ to $y$,
we have $\delta(a, c) \le 2\,(\delta(a, b) + \delta(b, c))$.

The factor $2$ comes from $(x + y)^2 \le 2(x^2 + y^2)$ applied coordinatewise. This is the
estimate that makes bounding-sphere pruning sound without square roots.

Formalized by `Cslib.Algorithms.Lean.BallTree.distSq_le_two_mul`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#dist-sq-le-two-mul).

## Squared covering radius

For a center $c \in \mathbb{Z}^d$ and a list $P$ of points of
$\mathbb{Z}^d$, the squared covering radius of $P$ about $c$ is the largest squared distance from
$c$ to a point of $P$, or $0$ if $P$ is empty.

Formalized by `Cslib.Algorithms.Lean.BallTree.radiusSq`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#radius-sq).

## Points lie within the squared radius

Let $c \in \mathbb{Z}^d$ and let $L$ be a list
of points of $\mathbb{Z}^d$. For every point $p$ of $L$, the squared distance from $c$ to $p$
is at most the squared radius of $L$ around $c$, the largest squared distance from $c$ to a
point of $L$.

Formalized by `Cslib.Algorithms.Lean.BallTree.distSq_le_radiusSq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#dist-sq-le-radius-sq).

## Accumulating ball-tree search

Let $d$ be a dimension and write $\delta(x, y)$ for the
squared distance from $x$ to $y$ in $\mathbb{Z}^d$. For a ball tree $T$ over $\mathbb{Z}^d$, a
query point $q \in \mathbb{Z}^d$, a squared radius $r \in \mathbb{N}$ and a list $A$ of points,
the accumulating search of $T$ for $q$ and $r$ with accumulator $A$ is $A$ when $T$ is empty;
when $T$ is a leaf holding $p$, it is $p$ followed by $A$ if $\delta(q, p) \le r$ and $A$
otherwise; when $T$ is a node with center $c$, squared-radius bound $b$ and children $L$ and $R$,
it is $A$ if $2(b + r) < \delta(c, q)$, and otherwise the accumulating search of $L$ for $q$ and
$r$ whose accumulator is the accumulating search of $R$ for $q$ and $r$ with accumulator $A$.

When $T$ satisfies the bounding-sphere invariant, this pruning is sound by the relaxed triangle
inequality $\delta(x, z) \le 2(\delta(x, y) + \delta(y, z))$ for all $x, y, z \in \mathbb{Z}^d$,
and the result is the points of $T$ within squared distance $r$ of $q$, from left to right,
followed by $A$.

Formalized by `Cslib.Algorithms.Lean.BallTree.searchAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#search-aux).

## Ball-tree similarity search

The search of a ball tree $T$ for a query point
$q \in \mathbb{Z}^d$ and a squared radius $r \in \mathbb{N}$ is the accumulating search of $T$ for
$q$ and $r$ started with the empty accumulator.

When $T$ satisfies the bounding-sphere invariant, the search lists exactly the points of $T$
within squared distance $r$ of $q$, from left to right.

Formalized by `Cslib.Algorithms.Lean.BallTree.search`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#search).

## Bounding-sphere invariant of a ball tree

Validity of a ball tree is defined inductively:
the empty tree and every leaf are valid, and a node with center $c$ and squared-radius bound $b$
is valid when both of its subtrees are valid and every point in the point list of either subtree
lies within squared Euclidean distance $b$ of $c$.

Formalized by `Cslib.Algorithms.Lean.BallTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#valid).

## Ball-tree search is exact

For every ball tree $T$ over $\mathbb{Z}^d$ satisfying the
bounding-sphere invariant, every query point $q \in \mathbb{Z}^d$ and every $r \in \mathbb{N}$, the
search of $T$ for $q$ and $r$ equals the list of points of $T$, from left to right, filtered to
the points $p$ whose squared distance from $q$ is at most $r$, in their order. Pruning against
the bounding spheres loses no point.

Formalized by `Cslib.Algorithms.Lean.BallTree.search_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#search-eq-filter).

## Search of a valid ball tree

Let $t$ be a ball tree satisfying the bounding-sphere
invariant. For all $q, p \in \mathbb{Z}^d$ and every natural number $r$, $p$ is returned by the
similarity search of $t$ with query $q$ and squared radius $r$ if and only if $p$ is one of the
points stored in $t$ and the squared distance from $q$ to $p$ is at most $r$.

Formalized by `Cslib.Algorithms.Lean.BallTree.mem_search_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#mem-search-iff).

## Building a ball tree by halving

The ball tree built from a list of points of
$\mathbb{Z}^d$ is defined by recursion on the list. The empty list gives the empty tree and a
one-point list $[p]$ gives the leaf $p$. A list $L = [x_1, \dots, x_n]$ with $n \ge 2$ gives a
node whose center is $x_1$, whose bound is the squared radius of $L$ around $x_1$ (the largest
squared distance from $x_1$ to a point of $L$), whose left child is the tree built from the
first $\lfloor n/2 \rfloor$ points of $L$, and whose right child is the tree built from the
remaining points of $L$.

Formalized by `Cslib.Algorithms.Lean.BallTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#build).

## Ball trees built by halving are valid

For every list of points in $\mathbb{Z}^d$, the
ball tree built from it by recursive halving satisfies the bounding-sphere invariant.

Formalized by `Cslib.Algorithms.Lean.BallTree.valid_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#valid-build).

## A built ball tree stores a permutation of its input

For every list $P$ of points of
$\mathbb{Z}^d$, the list of points of the ball tree built from $P$, from left to right, is a
permutation of $P$.

Formalized by `Cslib.Algorithms.Lean.BallTree.toList_build_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#to-list-build-perm).

## Points of a built ball tree

For every list $L$ of points of $\mathbb{Z}^d$ and every
point $p \in \mathbb{Z}^d$, $p$ is one of the points stored in the ball tree built from $L$ if
and only if $p$ occurs in $L$.

Formalized by `Cslib.Algorithms.Lean.BallTree.mem_toList_build_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#mem-to-list-build-iff).

## Size of a built ball tree

For every list $P$ of points of $\mathbb{Z}^d$, the size of
the ball tree built from $P$ equals the length of $P$, that is, the number of entries of $P$
counted with repetition.

Formalized by `Cslib.Algorithms.Lean.BallTree.size_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#size-build).

## Ball-tree search of a built tree

For every list $P$ of points of $\mathbb{Z}^d$, every
query point $q \in \mathbb{Z}^d$ and every $r \in \mathbb{N}$, let $T$ be the ball tree built from
$P$. The search of $T$ for $q$ and $r$ equals the list of points of $T$, from left to right,
filtered to the points $p$ whose squared distance from $q$ is at most $r$, in their order.

Formalized by `Cslib.Algorithms.Lean.BallTree.search_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#search-build).

## Ball-tree search of a built tree, up to order

For every list $P$ of points of
$\mathbb{Z}^d$, every query point $q \in \mathbb{Z}^d$ and every $r \in \mathbb{N}$, the search of
the ball tree built from $P$ for $q$ and $r$ is a permutation of the sublist of $P$ consisting of
the points $p$ whose squared distance from $q$ is at most $r$, kept with their multiplicities.

Formalized by `Cslib.Algorithms.Lean.BallTree.search_build_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#search-build-perm).

## Search of a built ball tree

Let $L$ be a list of points of $\mathbb{Z}^d$, let
$q, p \in \mathbb{Z}^d$ and let $r$ be a natural number. Then $p$ is returned by the similarity
search with query $q$ and squared radius $r$ on the ball tree built from $L$ if and only if $p$
occurs in $L$ and the squared distance from $q$ to $p$ is at most $r$.

Formalized by `Cslib.Algorithms.Lean.BallTree.mem_search_build_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/BallTree.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html#mem-search-build-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ball tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/ball-tree)
