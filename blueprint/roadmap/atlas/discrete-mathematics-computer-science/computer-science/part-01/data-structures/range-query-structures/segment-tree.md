---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SegmentTree, Cslib.Algorithms.Lean.SegmentTree.agg, Cslib.Algorithms.Lean.SegmentTree.size, Cslib.Algorithms.Lean.SegmentTree.toListAux, Cslib.Algorithms.Lean.SegmentTree.toList, Cslib.Algorithms.Lean.SegmentTree.toListAux_eq, Cslib.Algorithms.Lean.SegmentTree.toList_node, Cslib.Algorithms.Lean.SegmentTree.Valid
statement: formalized
proof: formalized
---

# Segment tree

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html).

## Segment Tree

## Segment tree

A segment tree with values in $\alpha$ is either empty, a leaf holding a
value in $\alpha$, or an internal node holding a cached segment aggregate in $\alpha$, a cached
segment length in $\mathbb{N}$, a left child and a right child, both segment trees.

Formalized by `Cslib.Algorithms.Lean.SegmentTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#segment-tree).

## Aggregate of a segment tree

The aggregate of a segment tree with values in an additive
monoid is $0$ for the empty tree, $x$ for a single leaf with value $x$, and the aggregate cached at
the root for an internal node.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.agg`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#agg).

## Size of a segment tree

The size of a segment tree is $0$ for the empty tree, $1$ for a
leaf, and, for an internal node, the segment length cached at that node.

When every cached length is the sum of the sizes of the node's children, this is the number of
leaves, and internal nodes answer in constant time.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#size).

## Accumulator traversal of a segment tree

Given a segment tree and a list $acc$, the
accumulator traversal returns $acc$ for the empty tree, the list $acc$ with $x$ prepended for a
leaf with value $x$, and, for an internal node with left child $L$ and right child $R$, the
traversal of $L$ starting from the result of the traversal of $R$ starting from $acc$.

Threading the output suffix this way collects the leaves of an $n$-leaf tree in linear time
instead of repeatedly appending (and copying) left-subtree results.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toListAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-aux).

## Leaf list of a segment tree

The leaf list of a segment tree is the list of its leaf
values from left to right: the empty list for the empty tree, $[x]$ for a leaf with value $x$,
and the leaf list of the left child followed by the leaf list of the right child for an
internal node.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list).

## Accumulator traversal prepends the leaf list

For every segment tree $t$ and every list
$acc$, the accumulator traversal of $t$ starting from $acc$ returns the leaf list of $t$ followed
by $acc$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toListAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-aux-eq).

## Leaf list of an internal node

For every internal node of a segment tree, with any cached
aggregate, any cached length, left child $L$ and right child $R$, its leaf list is the leaf list
of $L$ followed by the leaf list of $R$.

With the accumulator definition of the leaf list this is a theorem, not a definitional
unfolding.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-node).

## Valid segment trees

Validity of a segment tree over an additive monoid is defined
inductively: the empty tree and every leaf are valid, and an internal node with valid left child
$L$ and valid right child $R$ is valid when its cached aggregate is the aggregate of $L$ plus
the aggregate of $R$ and its cached length is the size of $L$ plus the size of $R$. Here the
aggregate and size of the empty tree are $0$ and $0$, of a leaf with value $x$ are $x$ and $1$,
and of an internal node are its cached aggregate and cached length.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#valid).

## Size of a valid segment tree

If $t$ is a valid segment tree with values in an additive
monoid, then the length of the list of leaf values of $t$, read from left to right, equals the
size of $t$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.length_toList_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#length-to-list-of-valid).

## Aggregate of a valid segment tree

If $t$ is a valid segment tree with values in an
additive monoid, then the aggregate of $t$ equals the sum of the leaf values of $t$, taken from
left to right.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.agg_eq_sum_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#agg-eq-sum-to-list).

## Building a segment tree from a list

The segment tree built from a list $L$ with entries
in an additive monoid is the empty tree if $L$ is empty, and a single leaf with value $x$ if
$L = (x)$. If $L$ has length $n \ge 2$, it is the internal node whose left child is the tree built
from the first $\lfloor n/2 \rfloor$ entries of $L$, whose right child is the tree built from the
remaining entries, and which caches the aggregate of the left child plus the aggregate of the
right child, in that order, and the sum of the sizes of its children.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#build).

## Built segment trees are valid

For every list $xs$ over an additive monoid, the segment
tree built from $xs$ is valid.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.valid_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#valid-build).

## Building a segment tree preserves the list

For every list $xs$ with entries in an
additive monoid, the leaf list of the segment tree built from $xs$ is $xs$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-build).

## Size of a built segment tree

For every list $xs$ with entries in an additive monoid, the
segment tree built from $xs$ has size equal to the length of $xs$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.size_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#size-build).

## Aggregate of a built segment tree

For every list $L$ with entries in an additive
monoid, the aggregate of the segment tree built from $L$ equals the sum of the entries of $L$,
taken from left to right.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.agg_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#agg-build).

## Range query on a segment tree

For a segment tree $t$ with values in an additive monoid
and natural numbers $l, r$, the range query over $[l, r)$, with positions counted from the start
of the segment of $t$, is defined recursively. On the empty tree it is $0$. On a leaf with value
$x$ it is $x$ if $l = 0 < r$, and $0$ otherwise. On an internal node with cached aggregate $a$,
cached size $s$ and children $t_1, t_2$, it is $0$ if $r \le l$ or $s \le l$; otherwise it is $a$
if $l = 0$ and $s \le r$; and in all remaining cases it is the query over $[l, r)$ on $t_1$ plus
the query over $[l - m, r - m)$ on $t_2$, where $m$ is the size of $t_1$ and subtraction is
truncated at $0$.

An empty range and a node disjoint from the range contribute $0$ without descending, and a fully
covered node contributes its cached aggregate.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.query`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#query).

## Correctness of range queries on a valid segment tree

Let $t$ be a valid segment tree with
values in an additive monoid, let $(x_0, \dots, x_{n-1})$ be its leaf values from left to right,
and let $l, r$ be natural numbers. The range query over $[l, r)$ on $t$ returns
$\sum_{l \le k < \min(r, n)} x_k$, the sum taken in increasing order of $k$; it is $0$ when
$\min(r, n) \le l$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.query_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#query-eq).

## Range queries on a built segment tree

Let $L = (x_0, \dots, x_{n-1})$ be a list with
entries in an additive monoid and let $l, r$ be natural numbers. The range query over $[l, r)$ on
the segment tree built from $L$ returns $\sum_{l \le k < \min(r, n)} x_k$, the sum taken in
increasing order of $k$; it is $0$ when $\min(r, n) \le l$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.query_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#query-build).

## Point update of a segment tree

The point update of a segment tree over an additive
monoid at an index $i \in \mathbb{N}$, relative to the tree's segment, with a value $y$ is
defined recursively. The empty tree stays empty. A leaf becomes a leaf with value $y$ if $i = 0$
and is unchanged otherwise. At an internal node with left child $L$ and right child $R$: if $i$
is less than the size of $L$, then $L$ is replaced by its point update at $i$ with $y$, and
otherwise $R$ is replaced by its point update at $i$ minus the size of $L$ with $y$; the node
keeps its cached length, and its cached aggregate becomes the aggregate of the new left child
plus the aggregate of the new right child.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.update`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#update).

## Point update preserves the size of a segment tree

For every segment tree $t$ over an
additive monoid, every index $i$ and every value $y$, the point update of $t$ at $i$ with $y$
has the same size as $t$.

Every node on the update path keeps its cached segment length.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.size_update`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#size-update).

## Point update preserves validity

If $t$ is a valid segment tree over an additive monoid,
then for every natural number $i$ and every value $y$, the point update of $t$ at $i$ with $y$ is
valid.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.Valid.update`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#update-2).

## Leaf list after an in-range point update

Let $t$ be a valid segment tree over an
additive monoid and let $i$ be a natural number less than the size of $t$. Then for every value
$y$, the leaf list of the point update of $t$ at $i$ with $y$ is the leaf list of $t$ with its
entry at position $i$ (counting from $0$) replaced by $y$.

Validity is what ties the cached sizes used for routing to the leaf list.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList_update_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-update-of-lt).

## Out-of-range point update leaves the leaf list unchanged

For every valid segment tree $t$
over an additive monoid, every index $i$ at least the size of $t$ and every value $y$, the point
update of $t$ at $i$ with $y$ has the same leaf list as $t$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList_update_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-update-of-le).

## Point update of a built segment tree

For every list $xs$ with entries in an additive
monoid, every index $i$ smaller than the length of $xs$ and every value $y$, the leaf list of the
segment tree built from $xs$, after the point update at $i$ with $y$, is $xs$ with its entry at
position $i$ (counting from $0$) replaced by $y$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.toList_update_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#to-list-update-build).

## Aggregate after a point update of a built segment tree

Let $L = (x_0, \dots, x_{n-1})$
be a list with entries in an additive monoid, let $i < n$, and let $y$ be an element of the
monoid. Applying the point update at index $i$ with value $y$ to the segment tree built from $L$
gives a tree whose aggregate is the sum, taken from left to right, of the list obtained from $L$
by replacing $x_i$ with $y$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.agg_update_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#agg-update-build).

## Range queries after a point update of a built segment tree

Let $L = (x_0, \dots, x_{n-1})$
be a list with entries in an additive monoid, let $i < n$, let $y$ be an element of the monoid,
and let $L'$ be the list obtained from $L$ by replacing $x_i$ with $y$, with entries
$x'_0, \dots, x'_{n-1}$. Apply the point update at index $i$ with value $y$ to the segment tree
built from $L$. For all natural numbers $l, r$, the range query over $[l, r)$ on the result
returns $\sum_{l \le k < \min(r, n)} x'_k$, the sum taken in increasing order of $k$; it is $0$
when $\min(r, n) \le l$.

Formalized by `Cslib.Algorithms.Lean.SegmentTree.query_update_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SegmentTree.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html#query-update-build).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Segment tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/segment-tree)
