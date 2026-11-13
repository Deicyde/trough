---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.RangeTree, Cslib.Algorithms.Lean.RangeTree.toListAux, Cslib.Algorithms.Lean.RangeTree.toList, Cslib.Algorithms.Lean.RangeTree.toListAux_eq, Cslib.Algorithms.Lean.RangeTree.toList_node, Cslib.Algorithms.Lean.RangeTree.size, Cslib.Algorithms.Lean.RangeTree.length_toList, Cslib.Algorithms.Lean.RangeTree.tmin
statement: formalized
proof: formalized
---

# Range tree

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html).

## Range Tree

## Range tree

A one-dimensional range tree over the integers is either empty, a single leaf
holding an integer, or a binary node made of two integers $l$ and $h$ together with a left and a
right subtree. The integers $l$ and $h$ are meant to cache the interval $[l, h]$ spanned by the
leaf values of the node's subtree; the type does not enforce this, the bounds-correctness
predicate does.

Formalized by `Cslib.Algorithms.Lean.RangeTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#range-tree).

## Leaf traversal of a range tree with an accumulator

For a range tree $t$ and a list $a$
of integers, $\operatorname{aux}(t, a)$ is $a$ if $t$ is empty, the list $x$ followed by $a$ if
$t$ is a single leaf with value $x$, and $\operatorname{aux}(L, \operatorname{aux}(R, a))$ if $t$
is a node with left subtree $L$ and right subtree $R$.

Equivalently, $\operatorname{aux}(t, a)$ is the leaf list of $t$ followed by $a$, so the leaf list
is computed in linear time rather than by repeatedly appending left leaf lists.

Formalized by `Cslib.Algorithms.Lean.RangeTree.toListAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#to-list-aux).

## Leaf list of a range tree

The leaf list of a range tree $t$ is the list of the integers
stored at its leaves, read from left to right and with repetitions.

Formalized by `Cslib.Algorithms.Lean.RangeTree.toList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#to-list).

## Range-tree leaf traversal appends to its accumulator

For every range tree $t$ and every
list $a$ of integers, the accumulator leaf traversal of $t$ started from $a$ equals the leaf list
of $t$ followed by $a$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.toListAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#to-list-aux-eq).

## Leaf list of a range-tree node

For all integers $lo$, $hi$ and range trees $L$, $R$, the
leaf list of the node with stored bounds $lo$, $hi$, left subtree $L$ and right subtree $R$ is
the leaf list of $L$ followed by the leaf list of $R$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.toList_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#to-list-node).

## Number of leaves of a range tree

The size of a range tree is its number of leaves: $0$ for
the empty tree, $1$ for a leaf, and the sum of the sizes of the two children for a node.

Formalized by `Cslib.Algorithms.Lean.RangeTree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#size).

## Length of the leaf list of a range tree

For every range tree $t$, the list of leaf values
of $t$ read from left to right has length equal to the number of leaves of $t$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.length_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#length-to-list).

## Cached lower bound of a range tree

For a range tree $t$, $\operatorname{tmin}(t)$ is
$0$ if $t$ is empty, $x$ if $t$ is a single leaf with value $x$, and the stored lower bound
$lo$ if $t$ is a node with stored bounds $lo$, $hi$ and two subtrees.

The value $0$ for the empty tree is a sentinel without meaning. Computing
$\operatorname{tmin}(t)$ takes constant time: it reads the bound cached at the root and does not
traverse the tree.

Formalized by `Cslib.Algorithms.Lean.RangeTree.tmin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#tmin).

## Cached upper bound of a range tree

For a range tree $t$, $\operatorname{tmax}(t)$ is
$0$ if $t$ is empty, $x$ if $t$ is a single leaf with value $x$, and the stored upper bound
$hi$ if $t$ is a node with stored bounds $lo$, $hi$ and two subtrees.

The value $0$ for the empty tree is a sentinel without meaning.

Formalized by `Cslib.Algorithms.Lean.RangeTree.tmax`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#tmax).

## Bounds-valid range trees

For a range tree $s$, write $s_{\min}$ and $s_{\max}$ for its
cached lower and upper bounds: the stored interval endpoints at a node, the value itself at a
leaf, and $0$ for the empty tree. Bounds-validity is defined inductively: the empty tree and every
leaf are bounds-valid, and a node with cached interval $[a, b]$, left child $\ell$ and right child
$r$ is bounds-valid when $\ell$ and $r$ are bounds-valid, each of them has at least one leaf,
$a = \min(\ell_{\min}, r_{\min})$ and $b = \max(\ell_{\max}, r_{\max})$.

The children must be nonempty because the empty tree has cached bounds $0$: with an empty child
the node cache would only enclose the leaves (a node over an empty child and the single leaf $5$
could cache $[0, 5]$), not equal their true interval. In a bounds-valid tree every leaf value lies
in the cached interval, and if the tree has a leaf, both cached bounds are leaf values.

Formalized by `Cslib.Algorithms.Lean.RangeTree.BoundsOk`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#bounds-ok).

## Valid range tree

A range tree $t$ is valid when it has correct cached bounds (every node
has two subtrees with nonempty leaf lists, and its stored lower and upper bounds are the minimum
of the lower bounds and the maximum of the upper bounds of its two subtrees, recursively) and
its leaf list is sorted in nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.RangeTree.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#valid).

## Valid range trees have sorted leaves

If a range tree $t$ is valid, then its list of leaf
values, read from left to right, is sorted in nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.RangeTree.Valid.pairwise_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#pairwise-to-list).

## Leaf values of a bounds-valid tree lie between the cached bounds

Let $t$ be a
bounds-valid range tree, and write $t_{\min}$ and $t_{\max}$ for its cached lower and upper
bounds. Then every leaf value $x$ of $t$ satisfies $t_{\min} \le x \le t_{\max}$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.bounds_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#bounds-of-mem).

## The cached bounds of a nonempty bounds-valid range tree are leaf values

Let $t$ be a
bounds-valid range tree with at least one leaf. Then the cached lower bound of $t$ and the cached
upper bound of $t$ are both leaf values of $t$.

Together with the fact that every leaf value lies between the cached bounds, this shows that the
cached interval is exactly the interval spanned by the leaves, not merely an enclosing one.

Formalized by `Cslib.Algorithms.Lean.RangeTree.bounds_mem_toList_of_ne_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#bounds-mem-to-list-of-ne-nil).

## Accumulator range report

For integers $a$, $b$ and a list $\mathit{acc}$ of integers, the
accumulator range report of a range tree for $[a, b]$ starting from $\mathit{acc}$ is defined by
recursion on the tree. The empty tree returns $\mathit{acc}$. A leaf with value $x$ returns $x$
followed by $\mathit{acc}$ if $a \le x \le b$, and $\mathit{acc}$ otherwise. A node with cached
interval $[l, h]$ returns $\mathit{acc}$ if $h < a$ or $b < l$; otherwise, if $a \le l$ and
$h \le b$, it returns the node's leaf values from left to right followed by $\mathit{acc}$;
otherwise it returns the report of the left child starting from the report of the right child
starting from $\mathit{acc}$.

The cached bounds make each pruning test constant-time.

Formalized by `Cslib.Algorithms.Lean.RangeTree.reportAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#report-aux).

## Range report

The range report of a range tree $t$ for integers $a$ and $b$ is the
accumulator range report of $t$ for $[a, b]$ starting from the empty list.

Formalized by `Cslib.Algorithms.Lean.RangeTree.report`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#report).

## Accumulator range report of a bounds-valid range tree

Let $t$ be a bounds-valid range
tree, let $a$ and $b$ be integers and let $\mathit{acc}$ be a list of integers. Then the
accumulator range report of $t$ for $[a, b]$ starting from $\mathit{acc}$ is the list of the leaf
values $x$ of $t$ with $a \le x \le b$, in left-to-right order and with repetitions, followed by
$\mathit{acc}$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.reportAux_eq_filter_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#report-aux-eq-filter-append).

## Correctness of the range report

Let $t$ be a range tree satisfying the bounds-correctness
predicate: every node has two subtrees with at least one leaf each and caches the least and the
greatest leaf value of its subtree. For all integers $a$ and $b$, the range report of $t$ for
$[a, b]$ equals the list of leaf values $x$ of $t$ with $a \le x \le b$, in left-to-right order.

Formalized by `Cslib.Algorithms.Lean.RangeTree.report_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#report-eq-filter).

## Membership in a range report

Let $t$ be a range tree satisfying the bounds-correctness
predicate: every node has two subtrees with at least one leaf each and caches the least and the
greatest leaf value of its subtree. For all integers $a$, $b$ and $x$, the value $x$ occurs in the
range report of $t$ for $[a, b]$ if and only if $x$ is a leaf value of $t$ and $a \le x \le b$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.mem_report_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#mem-report-iff).

## Range count

For a range tree $t$ and integers $a$ and $b$, the range count of $t$ over
$[a, b]$ is the length of the range report of $t$ for $[a, b]$.

On a bounds-valid tree this is the number of leaves whose value lies in $[a, b]$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.count`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#count).

## Range count of a bounds-valid tree

Let $t$ be a bounds-valid range tree and let $a$ and
$b$ be integers. Then the range count of $t$ over $[a, b]$ equals the number of leaves of $t$
whose value lies in $[a, b]$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.count_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#count-eq).

## Building a range tree from a list

For a range tree $s$, write $s_{\min}$ and $s_{\max}$
for its cached lower and upper bounds. The range tree built from a list $L$ of integers of length
$n$ is defined by recursion on $n$: the empty list gives the empty tree, a one-element list $[x]$
gives the leaf $x$, and for $n \ge 2$ it is the node whose left child $\ell$ is the tree built from
the first $\lfloor n/2 \rfloor$ entries of $L$, whose right child $r$ is the tree built from the
remaining entries, and whose cached interval is
$[\min(\ell_{\min}, r_{\min}), \max(\ell_{\max}, r_{\max})]$.

The entries of $L$ are kept in their given order; $L$ is not sorted first.

Formalized by `Cslib.Algorithms.Lean.RangeTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#build).

## Building a range tree preserves the list

For every list $xs$ of integers, the leaf list
of the range tree built from $xs$ is $xs$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.toList_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#to-list-build).

## Size of a built range tree

For every list $\mathit{xs}$ of integers, the range tree built
from $\mathit{xs}$ has exactly as many leaves as $\mathit{xs}$ has elements.

Formalized by `Cslib.Algorithms.Lean.RangeTree.size_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#size-build).

## Built range trees are bounds-valid

For every list $L$ of integers, the range tree built
from $L$ by recursive halving is bounds-valid.

Formalized by `Cslib.Algorithms.Lean.RangeTree.boundsOk_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#bounds-ok-build).

## Building from a sorted list gives a valid range tree

For every list $xs$ of integers that
is sorted in nondecreasing order, the range tree built from $xs$ is valid.

Without the sortedness hypothesis the built tree still has correct cached bounds, but it need not
be valid.

Formalized by `Cslib.Algorithms.Lean.RangeTree.valid_build_of_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#valid-build-of-sorted).

## Range report on a built tree

For every list $\mathit{xs}$ of integers and all integers $a$
and $b$, the range report for $[a, b]$ on the range tree built from $\mathit{xs}$ equals the list
of elements $x$ of $\mathit{xs}$ with $a \le x \le b$, in their original order.

Formalized by `Cslib.Algorithms.Lean.RangeTree.report_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#report-build).

## Range counting on a built tree

For every list $L$ of integers and all integers $a$ and
$b$, the range count over $[a, b]$ of the range tree built from $L$ equals the number of entries
of $L$, counted with multiplicity, that lie in $[a, b]$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.count_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#count-build).

## Range report membership on a built tree

For every list $L$ of integers and all integers
$a$, $b$ and $x$, the value $x$ occurs in the range report for $[a, b]$ on the range tree built
from $L$ if and only if $x$ is an entry of $L$ and $a \le x \le b$.

Formalized by `Cslib.Algorithms.Lean.RangeTree.mem_report_build_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RangeTree.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html#mem-report-build-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Range tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/range-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/range-tree)
