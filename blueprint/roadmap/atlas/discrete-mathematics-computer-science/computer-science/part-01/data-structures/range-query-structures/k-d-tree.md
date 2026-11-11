---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.KdTree, Cslib.Algorithms.Lean.KdTree.toListAux, Cslib.Algorithms.Lean.KdTree.toList, Cslib.Algorithms.Lean.KdTree.toListAux_eq, Cslib.Algorithms.Lean.KdTree.toList_node, Cslib.Algorithms.Lean.KdTree.size, Cslib.Algorithms.Lean.KdTree.length_toList, Cslib.Algorithms.Lean.KdTree.nextAxis
statement: formalized
proof: formalized
---

# k-d tree

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html).

## k-d tree

## Kd-trees

A kd-tree over points of $\mathbb{Z}^d$ is either empty, a leaf holding one
point of $\mathbb{Z}^d$, or a split node holding a split axis $a \in \{0, \dots, d-1\}$, a split
value $s \in \mathbb{Z}$ and two kd-trees, its left and right subtrees.

Formalized by `Cslib.Algorithms.Lean.KdTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#kd-tree).

## Kd-tree point traversal with an accumulator

For a kd-tree $t$ over points of
$\mathbb{Z}^d$ and a list $\mathit{acc}$ of such points, the accumulator traversal of $t$ onto
$\mathit{acc}$ is $\mathit{acc}$ when $t$ is empty, the point $p$ followed by $\mathit{acc}$ when
$t$ is a leaf holding $p$, and, when $t$ is a split node with left subtree $L$ and right subtree
$R$, the traversal of $L$ onto the traversal of $R$ onto $\mathit{acc}$.

Threading the output suffix avoids repeatedly appending (and copying) left-subtree results.

Formalized by `Cslib.Algorithms.Lean.KdTree.toListAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list-aux).

## Point list of a kd-tree

The point list of a kd-tree is the list of the points stored at
its leaves, from left to right.

Formalized by `Cslib.Algorithms.Lean.KdTree.toList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list).

## Accumulator traversal of a kd-tree

For every kd-tree $t$ over $\mathbb{Z}^d$ and
every list $acc$ of points, the accumulator traversal of $t$ onto $acc$ equals the list of
points of $t$ in left-to-right order followed by $acc$.

Formalized by `Cslib.Algorithms.Lean.KdTree.toListAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list-aux-eq).

## Point list of a kd-tree split node

For a split node with axis $a$, split value $s$, left
subtree $L$ and right subtree $R$, the point list of the node is the point list of $L$ followed
by the point list of $R$.

Formalized by `Cslib.Algorithms.Lean.KdTree.toList_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list-node).

## Size of a kd-tree

The size of a kd-tree is defined by recursion: the empty tree has
size $0$, a leaf has size $1$, and a split node has the sum of the sizes of its two
children. Since points are stored only at leaves, this is the number of points stored in the
tree, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.KdTree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#size).

## Length of the point list of a kd-tree

For every kd-tree $t$, the list of the points
stored in $t$, read from left to right, has length equal to the size of $t$, the number of
points stored in $t$.

Formalized by `Cslib.Algorithms.Lean.KdTree.length_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#length-to-list).

## Next split axis of a kd-tree

For a dimension $d \ge 1$ and an axis
$a \in \{0, \dots, d - 1\}$, the next split axis is $(a + 1) \bmod d$, so the axes are
visited cyclically.

Formalized by `Cslib.Algorithms.Lean.KdTree.nextAxis`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#next-axis).

## Membership in an axis-aligned box

For $lo, hi, p \in \mathbb{Z}^d$, the point $p$ lies
in the closed axis-aligned box $[lo, hi]$ when $lo_i \le p_i \le hi_i$ for every coordinate
$i \in \{0, \dots, d-1\}$.

Formalized by `Cslib.Algorithms.Lean.KdTree.inBox`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#in-box).

## Accumulator range report of a kd-tree

Points are vectors in $\mathbb{Z}^d$ with
coordinates $p_0, \dots, p_{d-1}$; the box $[lo, hi]$ consists of the points $p$ with
$lo_i \le p_i \le hi_i$ for every $i$. For a kd-tree $t$ and a list $acc$ of points, the
accumulator report of $t$ for $[lo, hi]$ onto $acc$ is defined by recursion on $t$. For the
empty tree it is $acc$. For a leaf $p$ it is $p$ followed by $acc$ if $p$ lies in the box,
and $acc$ otherwise. For a split node with axis $a$, split value $s$, left child $L$ and
right child $R$, let $acc'$ be $acc$ if $hi_a < s$ and the report of $R$ onto $acc$
otherwise; the result is $acc'$ if $s < lo_a$ and the report of $L$ onto $acc'$ otherwise.

The accumulator avoids repeatedly appending the results of left subtrees, so building the
output list costs work linear in the number of reported points; the traversal still visits
every node that pruning does not cut, which can be the whole tree even for an empty report.
No complexity bound is formalized.

Formalized by `Cslib.Algorithms.Lean.KdTree.reportAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report-aux).

## Orthogonal range report of a kd-tree

For a kd-tree $t$ over $\mathbb{Z}^d$ and
$lo, hi \in \mathbb{Z}^d$, the range report of $t$ for the box $[lo, hi]$ is the accumulator
range report of $t$ for $[lo, hi]$ onto the empty list.

Formalized by `Cslib.Algorithms.Lean.KdTree.report`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report).

## Kd invariant

A kd-tree satisfies the kd invariant when at every split node, with axis $a$
and split value $s$, every point of the left subtree has $a$-coordinate at most $s$ and every
point of the right subtree has $a$-coordinate at least $s$.

Formalized by `Cslib.Algorithms.Lean.KdTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#valid).

## Accumulator range report of a valid kd-tree

Let $t$ be a valid kd-tree over
$\mathbb{Z}^d$, let $lo, hi \in \mathbb{Z}^d$, and let $acc$ be a list of points. The
accumulator range report of $t$ for the box $[lo, hi]$ onto $acc$ equals the list of points
of $t$, in left-to-right order, that lie in the box (the points $p$ with
$lo_i \le p_i \le hi_i$ for every coordinate $i$), followed by $acc$.

Formalized by `Cslib.Algorithms.Lean.KdTree.reportAux_eq_filter_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report-aux-eq-filter-append).

## Correctness of the kd-tree range report

For every valid kd-tree $t$ over
$\mathbb{Z}^d$ and all $lo, hi \in \mathbb{Z}^d$, the range report of $t$ for the box
$[lo, hi]$ equals the list of points of $t$, in left-to-right order, that lie in the box,
that is, the points $p$ with $lo_i \le p_i \le hi_i$ for every coordinate $i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.report_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report-eq-filter).

## Range report of a valid kd-tree

Let $t$ be a kd-tree over $\mathbb{Z}^d$ that
satisfies the kd invariant, and let $lo, hi, p \in \mathbb{Z}^d$. Then $p$ occurs in the range
report of $t$ for the box $[lo, hi]$ if and only if $p$ is one of the points stored in $t$ and
$lo_i \le p_i \le hi_i$ for every coordinate $i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.mem_report_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#mem-report-iff).

## First-point coordinate

For an axis $a \in \{0, \dots, d-1\}$ and a list of points in
$\mathbb{Z}^d$, this is the $a$-coordinate of the first point of the list, or $0$ if the list
is empty.

Formalized by `Cslib.Algorithms.Lean.KdTree.headCoord`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#head-coord).

## Kd-tree construction by median splits

Let $d \ge 1$, let $a \in \{0, \dots, d-1\}$ be
an axis and let $P$ be a list of points in $\mathbb{Z}^d$. The kd-tree built from $P$ starting at
axis $a$ is the empty tree if $P$ is empty and the leaf holding $p$ if $P = [p]$. If $P$ has
$n \ge 2$ points, sort $P$ by $a$-coordinate with merge sort, let $L$ be the first
$\lfloor n/2 \rfloor$ points of the sorted list and $R$ the remaining ones. The result is the
split node with axis $a$ whose split value is the $a$-coordinate of the first point of $R$, whose
left subtree is built from $L$ and whose right subtree is built from $R$, both starting at the
next axis $(a + 1) \bmod d$.

Formalized by `Cslib.Algorithms.Lean.KdTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#build).

## Median-split kd-trees satisfy the kd invariant

For $d \ge 1$, every axis $a$ and every
list of points of $\mathbb{Z}^d$, the kd-tree built from the list by median splits starting at
axis $a$ satisfies the kd invariant.

Formalized by `Cslib.Algorithms.Lean.KdTree.valid_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#valid-build).

## Building a kd-tree preserves its points

For $d \ge 1$, every axis $a$ and every list of
points of $\mathbb{Z}^d$, the point list of the kd-tree built from the list by median splits
starting at axis $a$ is a permutation of the list.

Formalized by `Cslib.Algorithms.Lean.KdTree.toList_build_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list-build-perm).

## A built kd-tree holds the same points as its input

Let $d \ge 1$, let
$a \in \{0, \dots, d-1\}$ and let $P$ be a list of points in $\mathbb{Z}^d$. A point
$p \in \mathbb{Z}^d$ is stored in the kd-tree built from $P$ by median splits starting at axis
$a$ if and only if $p$ occurs in $P$.

Formalized by `Cslib.Algorithms.Lean.KdTree.mem_toList_build_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#mem-to-list-build-iff).

## Size of a built kd-tree

Let $d \ge 1$. For every starting axis $a$ and every list
$P$ of points of $\mathbb{Z}^d$, the size of the kd-tree built from $P$ starting at axis $a$
equals the length of $P$ (repeated points counted with multiplicity).

Formalized by `Cslib.Algorithms.Lean.KdTree.size_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#size-build).

## Kd-tree construction from the first axis

For $d \ge 1$ and a list of points in
$\mathbb{Z}^d$, this is the kd-tree built from the list by alternating-axis median splits,
starting with split axis $0$.

Formalized by `Cslib.Algorithms.Lean.KdTree.buildRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#build-root).

## Kd-trees built from axis 0 satisfy the kd invariant

For $d \ge 1$ and every list of
points of $\mathbb{Z}^d$, the kd-tree built from the list by median splits starting at axis $0$
satisfies the kd invariant.

Formalized by `Cslib.Algorithms.Lean.KdTree.valid_buildRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#valid-build-root).

## Building a kd-tree from axis 0 preserves its points

For $d \ge 1$ and every list of
points of $\mathbb{Z}^d$, the point list of the kd-tree built from the list by median splits
starting at axis $0$ is a permutation of the list.

Formalized by `Cslib.Algorithms.Lean.KdTree.toList_buildRoot_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#to-list-build-root-perm).

## Range report of a built kd-tree as a filter

Let $d \ge 1$. For every starting axis
$a$, every list $P$ of points of $\mathbb{Z}^d$ and all $lo, hi \in \mathbb{Z}^d$, let $T$ be
the kd-tree built from $P$ starting at axis $a$. The range report of $T$ for the box
$[lo, hi]$ equals the list of points of $T$, in left-to-right order, that lie in the box,
that is, the points $p$ with $lo_i \le p_i \le hi_i$ for every coordinate $i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.report_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report-build).

## Range report of a built kd-tree up to order

Let $d \ge 1$. For every starting axis $a$,
every list $P$ of points of $\mathbb{Z}^d$ and all $lo, hi \in \mathbb{Z}^d$, the range report
for the box $[lo, hi]$ of the kd-tree built from $P$ starting at axis $a$ is a permutation of
the list of entries of $P$ that lie in the box, that is, the points $p$ with
$lo_i \le p_i \le hi_i$ for every coordinate $i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.report_build_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#report-build-perm).

## Membership in the range report of a built kd-tree

Let $d \ge 1$, let
$a \in \{0, \dots, d-1\}$, let $P$ be a list of points in $\mathbb{Z}^d$ and let
$lo, hi, p \in \mathbb{Z}^d$. Then $p$ occurs in the range report, for the box $[lo, hi]$, of the
kd-tree built from $P$ by median splits starting at axis $a$ if and only if $p$ occurs in $P$ and
$lo_i \le p_i \le hi_i$ for every coordinate $i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.mem_report_build_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#mem-report-build-iff).

## Range report of a kd-tree built from the first axis

Let $d \ge 1$, let $P$ be a list
of points in $\mathbb{Z}^d$ and let $lo, hi, p \in \mathbb{Z}^d$. Then $p$ occurs in the range
report, for the box $[lo, hi]$, of the kd-tree built from $P$ by median splits starting at
axis $0$ if and only if $p$ occurs in $P$ and $lo_i \le p_i \le hi_i$ for every coordinate
$i$.

Formalized by `Cslib.Algorithms.Lean.KdTree.mem_report_buildRoot_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/KdTree.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html#mem-report-build-root-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-d tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/k-d-tree)
