---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.IntervalTree.Interval, Cslib.Algorithms.Lean.IntervalTree.Interval.Valid, Cslib.Algorithms.Lean.IntervalTree.Interval.valid, Cslib.Algorithms.Lean.IntervalTree.Interval.Overlaps, Cslib.Algorithms.Lean.IntervalTree.Interval.overlaps, Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost, Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost_fst, Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost_snd
statement: formalized
proof: formalized
---

# Interval tree

84 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html).

## Interval Tree

## Interval

An interval is a pair of integers, its low endpoint and its high endpoint, read as
the closed interval from the low to the high endpoint. The structure itself imposes no order on the
endpoints; the public update operations accept an interval only when its low endpoint is at most
its high endpoint.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#interval).

## Valid interval

A closed interval with integer endpoints $a$ (low) and $b$ (high) is
valid when its low endpoint is at most its high endpoint, $a \le b$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid).

## Boolean interval validity test

For an interval $[a, b]$ with integer endpoints, the
Boolean validity test returns true exactly when $a \le b$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-2).

## Overlapping closed intervals

An interval $I$ with low endpoint $a$ and high endpoint $b$
overlaps an interval $J$ with low endpoint $c$ and high endpoint $d$ when $a \le d$ and $c \le b$;
in particular, intervals that share only an endpoint overlap.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.Overlaps`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#overlaps).

## Overlap test for closed intervals

For an interval $I$ with low endpoint $a$ and high
endpoint $b$ and an interval $J$ with low endpoint $c$ and high endpoint $d$, the overlap test of
$I$ against $J$ returns true exactly when $a \le d$ and $c \le b$; it compares $a$ with $d$ first
and returns false without the second comparison when $a > d$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.overlaps`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#overlaps-2).

## Overlap test with comparison count

For an interval $I$ with low endpoint $a$ and high
endpoint $b$ and an interval $J$ with low endpoint $c$ and high endpoint $d$, the instrumented
overlap test of $I$ against $J$ returns the pair (false, $1$) when $a > d$, the pair (false, $2$)
when $a \le d$ and $c > b$, and the pair (true, $2$) when $a \le d$ and $c \le b$; the number
is the count of endpoint comparisons evaluated.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#overlaps-with-cost).

## The instrumented overlap test returns the plain result

For intervals $I$ and $J$, the
Boolean component of the instrumented overlap test of $I$ against $J$ equals the overlap test of
$I$ against $J$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost_fst`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#overlaps-with-cost-fst).

## Comparison count of the overlap test

For intervals $I$ and $J$, the instrumented overlap
test of $I$ against $J$ reports $2$ endpoint comparisons when the low endpoint of $I$ is at most
the high endpoint of $J$, and $1$ comparison otherwise.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Interval.overlapsWithCost_snd`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#overlaps-with-cost-snd).

## Interval tree entry

An entry of the interval tree consists of an identifier, which is a
natural number, and an interval with integer low and high endpoints.

Identifiers, rather than endpoints, are meant to be unique among stored entries; this is required
by the indexed tree's representation invariant, not by the entry itself.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Entry`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#entry).

## Search key of an interval entry

The key of an entry is the pair
$(\ell, i) \in \mathbb{Z} \times \mathbb{N}$, where $\ell$ is the low endpoint of the entry's
interval and $i$ is the entry's identifier.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Entry.key`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key).

## Lexicographic comparison of keys

For keys $(a, i)$ and $(b, j)$ in
$\mathbb{Z} \times \mathbb{N}$ (a low endpoint and an occurrence identifier), the comparison
returns less-than if $a < b$, or if $a = b$ and $i < j$; greater-than if $a > b$, or if $a = b$
and $i > j$; and equal if $a = b$ and $i = j$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.compareKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#compare-key).

## Operation cost counters for interval trees

A cost record for the interval tree consists
of seven natural-number counters, each defaulting to $0$: node visits, key comparisons, endpoint
comparisons, cached-maximum reads, cache writes, rotations, and identifier-index operations.

The cached-maximum counter is deliberately narrow: it counts only the reads made by search
pruning, one per visited node where the left subtree's cached maximum decides the descent. Node
construction, rebalancing and the rotations read cached heights, sizes and maxima while rebuilding
nodes; those reads are not counted separately, and maintenance work is reported through the cache
write, rotation and remaining counters instead.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Cost`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cost).

## Interval tree

An interval tree is either empty or a node consisting of a left subtree,
an entry, a right subtree and three cached fields: a height and a size (natural numbers) and a
maximum high endpoint (an integer). The type imposes no balance or consistency condition on
these fields; it is the carrier on which the AVL interval-tree operations act.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#tree).

## Cached maximum of an interval tree

The cached maximum of an interval tree is no value
when the tree is empty, and when the tree is a node it is the integer stored in the node's cached
maximum-high-endpoint field.

It is read in constant time. The tree type itself does not require this field to equal the
largest high endpoint of an interval in the subtree.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cachedMax?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cached-max).

## Maximum with an optional value

For an integer $a$ and an optional integer $v$, the value
is $a$ when $v$ is absent and $\max(a, v)$ when $v$ is present. It combines a value with an
optional subtree maximum without using a sentinel value.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.maxWith`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#max-with).

## Maximum high endpoint at a node

For subtrees $L$ and $R$ and an entry $e$, the node
maximum is the largest of the high endpoint of the interval of $e$, the cached maximum high
endpoint stored at the root of $L$, and the one stored at the root of $R$, where an empty subtree
stores no cached maximum and contributes nothing.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.nodeMax`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#node-max).

## Node construction with repaired metadata

For an interval tree $T$ write $h(T)$ and $|T|$
for its cached height and size, both $0$ for the empty tree. Given interval trees $L$ and $R$ and
an entry $e$, this builds the node with left subtree $L$, entry $e$ and right subtree $R$ whose
cached height is $\max(h(L), h(R)) + 1$, whose cached size is $|L| + |R| + 1$, and whose cached
maximum high endpoint is the largest of the high endpoint of $e$ and the cached maxima of the
nonempty subtrees among $L$ and $R$.

It is the sole ordinary node constructor.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.mkNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#mk-node).

## Cache invariant of an interval tree

An interval tree satisfies the cache invariant when
every cached field is exact, recursively. The empty tree satisfies it. A node with stored height
$h$, stored size $s$, stored maximum $m$, left subtree $L$, entry $e$ and right subtree $R$
satisfies it when $L$ and $R$ satisfy it, $m$ is at least the high endpoint of every entry of
$L$, of $e$ and of every entry of $R$, $m$ equals the high endpoint of one of these entries,
$h = \max(\operatorname{height} L, \operatorname{height} R) + 1$ and
$s = \operatorname{size} L + \operatorname{size} R + 1$. Here the height and size of a subtree
are its stored fields, and the empty tree has height and size $0$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.CacheInvariant`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant).

## Low-endpoint ordered interval tree

The empty tree is low-endpoint ordered, and a node is
low-endpoint ordered when both of its subtrees are low-endpoint ordered, every interval in the
left subtree has low endpoint at most the low endpoint of the node's interval, and the node's
low endpoint is at most the low endpoint of every interval in the right subtree.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.LowOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#low-ordered).

## Validity invariant of an interval tree

A tree satisfies the validity invariant when
every interval stored in it is valid, that is, its low endpoint is at most its high endpoint.
Recursively, the empty tree satisfies it, and a node satisfies it when its left subtree does,
the interval of its entry is valid, and its right subtree does.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.ValidInvariant`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant).

## Right rotation

Write $\langle L, x, R\rangle$ for a node with left subtree $L$, entry $x$
and right subtree $R$. The right rotation sends $\langle\langle a, x, b\rangle, y, c\rangle$ to
$\langle a, x, \langle b, y, c\rangle\rangle$, where both nodes of the result get freshly
recomputed height, size and maximum high endpoint. Every tree not of this shape is returned
unchanged.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.rotateRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#rotate-right).

## Left rotation

Write $\langle L, x, R\rangle$ for a node with left subtree $L$, entry $x$
and right subtree $R$. The left rotation sends $\langle a, x, \langle b, y, c\rangle\rangle$ to
$\langle\langle a, x, b\rangle, y, c\rangle$, where both nodes of the result get freshly
recomputed height, size and maximum high endpoint. Every tree not of this shape is returned
unchanged.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.rotateLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#rotate-left).

## Left-right double rotation

Write $\langle L, x, R\rangle$ for a node with left subtree
$L$, entry $x$ and right subtree $R$. The left-right rotation sends
$\langle\langle a, x, \langle b, y, c\rangle\rangle, z, d\rangle$ to
$\langle\langle a, x, b\rangle, y, \langle c, z, d\rangle\rangle$, where all three nodes of the
result get freshly recomputed height, size and maximum high endpoint. Every tree not of this
shape is returned unchanged.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.rotateLeftRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#rotate-left-right).

## Right-left double rotation

Write $\langle L, x, R\rangle$ for a node with left subtree
$L$, entry $x$ and right subtree $R$. The right-left rotation sends
$\langle a, x, \langle\langle b, y, c\rangle, z, d\rangle\rangle$ to
$\langle\langle a, x, b\rangle, y, \langle c, z, d\rangle\rangle$, where all three nodes of the
result get freshly recomputed height, size and maximum high endpoint. Every tree not of this
shape is returned unchanged.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.rotateRightLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#rotate-right-left).

## AVL rebalancing step with cost

Rebalancing a tree $T$ returns a tree and a cost, where
heights are the stored heights. If $T$ is empty, or neither subtree of its root is more than one
taller than the other, it returns $T$ unchanged with zero cost. If the left subtree $L$ is more
than one taller than the right subtree, it applies a right rotation, costing $2$ cache writes and
one rotation, when the left child of $L$ is at least as tall as the right child of $L$, and
otherwise a left-right double rotation, costing $3$ cache writes and two rotations. If the right
subtree $R$ is more than one taller than the left subtree, it applies a left rotation, costing
$2$ cache writes and one rotation, when the right child of $R$ is at least as tall as the left
child of $R$, and otherwise a right-left double rotation, costing $3$ cache writes and two
rotations. All other cost counters are zero.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.rebalanceWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#rebalance-with-cost).

## Keyed insertion with cost

Inserting an entry $x$ into a tree returns a new tree together
with an operation cost; keys (low endpoint, then identifier) are compared lexicographically. Into
the empty tree, $x$ is inserted as a single node, at a cost of one node visit and one cache write.
At a node with entry $y$: if the key of $x$ equals the key of $y$, then $y$ is replaced by $x$, at a
cost of one node visit, one key comparison and one cache write; if the key of $x$ is smaller
(respectively larger), then $x$ is inserted recursively into the left (respectively right)
subtree, the node is rebuilt with recomputed metadata and rebalanced, and the cost is the cost of
the recursive insertion, plus one node visit, one key comparison and one cache write, plus the
cost of rebalancing.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.insertKeyWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#insert-key-with-cost).

## Removing the leftmost entry, with its cost

Removing the leftmost entry of an interval
tree $T$ returns nothing when $T$ is empty. When the root's left subtree is empty, it returns the
root entry, the right subtree, and a cost of one node visit. Otherwise it removes the leftmost
entry $m$ of the left subtree recursively (returning nothing if that fails), rebuilds the root
node over the new left subtree with recomputed height, size and maximum high endpoint, and
rebalances that node; it returns $m$, the rebalanced tree, and the cost of the recursive call plus
one node visit and one cache write plus the cost of rebalancing.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.removeMinWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#remove-min-with-cost).

## Keyed erasure with cost

Erasing a key $k \in \mathbb{Z} \times \mathbb{N}$ from an
interval tree returns a new tree together with its cost; the key of an entry is the pair of its low
endpoint and identifier, and keys are compared lexicographically. The empty tree is returned
unchanged at a cost of one node visit. At a node with entry $x$, the key $k$ is compared with the
key of $x$. If $k$ is smaller, $k$ is erased from the left subtree; if it is larger, from the right
subtree; in both cases the node is rebuilt with the new subtree and rebalanced, and the cost is the
subtree's cost plus one node visit, one key comparison, one cache write and the rebalancing cost.
If $k$ equals the key of $x$ and the right subtree is empty (so it has no leftmost entry to
remove), the result is the left subtree at a cost of one node visit and one key comparison.
Otherwise the leftmost entry of the right subtree is removed and takes the place of $x$, the node
is rebuilt and rebalanced, and the cost is the removal's cost plus one node visit, one key
comparison, one cache write and the rebalancing cost.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.eraseKeyWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#erase-key-with-cost).

## Instrumented overlap search

Given a query interval $q = [c, d]$ and an interval tree
$T$, the instrumented overlap search returns an optional entry together with a cost record,
defined by recursion on $T$. On the empty tree it returns no entry and records one node visit.
At a node with left subtree $L$, entry $e$ with interval $[a, b]$ and right subtree $R$, it
first tests overlap by evaluating $a \le d$ and, only if that holds, $c \le b$; let
$k \in \{1, 2\}$ be the number of relations evaluated. If both hold, it returns $e$ and records
one node visit and $k$ endpoint comparisons. Otherwise, if $L$ is empty, it returns the result of
searching $R$, adding one node visit and $k$ endpoint comparisons to that search's cost. If $L$
is nonempty with cached maximum high endpoint $m$, it returns the result of searching $L$ when
$c \le m$ and of searching $R$ otherwise, adding one node visit, $k + 1$ endpoint comparisons and
one cached-maximum read to that search's cost. No other counter is ever incremented.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.searchWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-with-cost).

## Instrumented search in the empty tree

For every query interval $q$, the instrumented
overlap search of $q$ in the empty interval tree returns no entry, and its cost record counts
one node visit and zero for every other counter (key comparisons, endpoint comparisons,
cached-maximum reads, cache writes, rotations and index operations).

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.searchWithCost_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-with-cost-empty).

## Instrumented search in a one-entry tree

Let $e$ be an entry whose interval is $[a, b]$,
let $q = [c, d]$ be a query interval, and let $k = 2$ if $a \le d$ and $k = 1$ otherwise.
Consider the single-node tree built from $e$ with empty subtrees and exact cached fields. If
$[a, b]$ and $[c, d]$ overlap (that is, $a \le d$ and $c \le b$), the instrumented overlap search
of $q$ in this tree returns $e$ with a cost record of one node visit and $k$ endpoint
comparisons. Otherwise it returns no entry with a cost record of two node visits (the root and
its empty right subtree) and $k$ endpoint comparisons. All other counters are zero in both
cases.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.searchWithCost_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-with-cost-singleton).

## Interval-tree overlap search

The overlap search of a query interval $q$ in an interval
tree $T$ returns the optional entry produced by the instrumented overlap search of $q$ in $T$,
discarding its cost record.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.search`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search).

## Linear-scan overlap search

For a tree $T$ and a query interval $q$, the oracle search
returns the first entry, in the in-order list of entries of $T$, whose interval overlaps $q$ as
closed intervals, and returns nothing when no entry's interval overlaps $q$.

It is a separate full-traversal oracle used only by specifications and tests.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.oracleSearch`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#oracle-search).

## Completeness of interval-tree search

Let $T$ be an interval tree whose cached height, size
and maximum high endpoint are exact at every node, and whose low endpoints respect the search
order (at every node, low endpoints in the left subtree are at most the node's, and those in the
right subtree at least the node's). If some entry stored in $T$ has an interval that overlaps the
query interval $Q$ (each interval's low endpoint is at most the other's high endpoint), then
searching $T$ for $Q$ returns some entry.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.search_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-complete).

## Interval-tree search fails exactly when nothing overlaps

Let $T$ be an interval tree
whose cached height, size and maximum high endpoint are exact at every node, and whose low
endpoints respect the search order (at every node, low endpoints in the left subtree are at most
the node's, and those in the right subtree at least the node's). Then searching $T$ for a query
interval $Q$ returns nothing if and only if no entry stored in $T$ has an interval that overlaps
$Q$ (each interval's low endpoint is at most the other's high endpoint).

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.search_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-eq-none-iff).

## Executable cache check for interval trees

The Boolean cache check returns true on the
empty tree. On a node with stored height $h$, stored size $s$, stored maximum $m$, left subtree
$L$, entry $e$ and right subtree $R$ it returns true exactly when
$h = \max(\operatorname{height} L, \operatorname{height} R) + 1$,
$s = \operatorname{size} L + \operatorname{size} R + 1$, $m$ is the largest of the high endpoint
of $e$ and the cached maxima of those of $L$ and $R$ that are nonempty, and the check returns
true on both $L$ and $R$. Here the height and size of a subtree are its stored fields, and the
empty tree has height and size $0$.

It is used only by the executable invariant checker.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheOK`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-ok).

## Key between optional bounds

Given an optional lower bound, an optional upper bound and a
key $k$ (a pair of an integer and a natural number), this test returns true exactly when the lower
bound is absent or strictly below $k$, and the upper bound is absent or strictly above $k$. Keys
are compared lexicographically: first by the integer, then by the natural number.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyBetween`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-between).

## Ordered-and-valid check for interval trees

Keys of entries are pairs (low endpoint,
identifier), ordered lexicographically. Given optional lower and upper key bounds $\ell$ and $u$,
the check accepts the empty tree, and accepts a node with left subtree $L$, entry $e$ and right
subtree $R$ exactly when the key $k$ of $e$ is strictly greater than $\ell$ if $\ell$ is present
and strictly less than $u$ if $u$ is present, the interval of $e$ has low endpoint at most its
high endpoint, $L$ is accepted with bounds $\ell$ and $k$, and $R$ is accepted with bounds $k$
and $u$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.orderedValid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#ordered-valid).

## Boolean AVL balance check for interval trees

The balance check returns true on the empty
tree. On a node whose left and right subtrees have stored heights $h_L$ and $h_R$ (the empty tree
has height $0$), it returns true exactly when the node's stored height equals
$\max(h_L, h_R) + 1$, $h_L \le h_R + 1$, $h_R \le h_L + 1$, and the check returns true on both
subtrees.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balanced`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced).

## AVL balance of an interval tree

An interval tree is AVL balanced with exact stored heights
when it is empty, or when it is a node such that, writing $h_L$ and $h_R$ for the stored heights
of its left and right subtrees (the empty tree has height $0$), the node's stored height equals
$\max(h_L, h_R) + 1$, $h_L \le h_R + 1$, $h_R \le h_L + 1$, and both subtrees are again AVL
balanced with exact stored heights.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.BalancedProp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop).

## Key-ordered interval tree

The empty tree is key-ordered, and a node is key-ordered when
both of its subtrees are key-ordered, the key of every entry in the left subtree is strictly less
than the key of the node's entry, and the key of the node's entry is strictly less than the key of
every entry in the right subtree. Keys are compared lexicographically: low endpoint first, then
identifier.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.KeyOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-ordered).

## The executable ordering check implies key ordering

Let $t$ be an interval tree and let
$\ell$ and $u$ be optional keys in $\mathbb{Z} \times \mathbb{N}$. If the executable ordering check
of $t$ with lower bound $\ell$ and upper bound $u$ succeeds, then $t$ is key-ordered, and every
entry $e$ stored in $t$ satisfies $\ell < \operatorname{key}(e)$ when $\ell$ is present and
$\operatorname{key}(e) < u$ when $u$ is present, where $<$ is the lexicographic order on keys
(low endpoint first, then identifier).

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyOrdered_of_orderedValid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-ordered-of-ordered-valid).

## The executable ordering check implies low-endpoint ordering

Let $t$ be an interval tree
and let $\ell$ and $u$ be optional keys in $\mathbb{Z} \times \mathbb{N}$. If the executable
ordering check of $t$ with lower bound $\ell$ and upper bound $u$ succeeds, then $t$ is
low-endpoint ordered, and every entry $e$ stored in $t$ satisfies $\ell < \operatorname{key}(e)$
when $\ell$ is present and $\operatorname{key}(e) < u$ when $u$ is present, where $<$ is the
lexicographic order on keys (low endpoint first, then identifier).

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.lowOrdered_of_orderedValid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#low-ordered-of-ordered-valid).

## The ordering check implies interval validity

Let $T$ be an interval tree and let
$\ell$ and $u$ be optional lower and upper key bounds. If the executable check of $T$ with
bounds $\ell$ and $u$, which tests that every key lies strictly between its bounds and that every
stored interval passes the Boolean validity test, returns true, then every interval stored in
$T$ is valid, that is, its low endpoint is at most its high endpoint.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_of_orderedValid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-of-ordered-valid).

## Removing the minimum preserves the other entries

If removing the leftmost entry of a tree
$T$ returns an entry $m$, a tree $T'$ and a cost, then the list consisting of $m$ followed by the
in-order entries of $T'$ is a permutation of the in-order entries of $T$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.removeMinWithCost_entries_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#remove-min-with-cost-entries-perm).

## Entries after keyed insertion

Let $t$ be a tree whose entries are strictly ordered by key,
and let $x$ be an entry. The in-order list of entries of the tree obtained by inserting $x$ into $t$
by key is a permutation of the list consisting of $x$ followed by those entries of $t$ whose key
differs from the key of $x$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.insertKeyWithCost_entries_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#insert-key-with-cost-entries-perm).

## Keyed erasure removes exactly the entries with that key

The key of an entry is the pair
$(\ell, i) \in \mathbb{Z} \times \mathbb{N}$ of its low endpoint $\ell$ and identifier $i$; keys are
compared lexicographically. Let $T$ be an interval tree whose keys are strictly ordered (every key
in a left subtree is lexicographically below its node's key and every key in a right subtree is
above it), and let $k \in \mathbb{Z} \times \mathbb{N}$ be a key. Then the in-order list of entries
of the tree obtained by erasing $k$ from $T$ is a permutation of the in-order list of entries of $T$
with every entry of key $k$ removed.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.eraseKeyWithCost_entries_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#erase-key-with-cost-entries-perm).

## Strictly key-ordered trees have distinct keys

If a tree is strictly ordered by key, then
the keys of its stored entries are pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyNodup_of_keyOrdered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-nodup-of-key-ordered).

## The removed minimum has the least key

Let $T$ be a key-ordered interval tree: at every
node, the keys in the left subtree are strictly smaller and those in the right subtree strictly
larger than the node's key, where the key of an entry is the pair (low endpoint, identifier)
compared lexicographically. If removing the leftmost entry of $T$ returns the entry $m$ (together
with the remaining tree and a cost record), then every entry $e$ stored in $T$ is either $m$
itself or has a key strictly larger than the key of $m$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.removeMinWithCost_min_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#remove-min-with-cost-min-le).

## Insertion into an interval tree preserves key ordering

Let $t$ be a key-ordered interval
tree and let $e$ be an entry. Then the tree returned by the cost-instrumented keyed insertion of
$e$ into $t$ (which replaces the entry with the same key, if there is one; the reported cost is
discarded) is again key-ordered.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyOrdered_insertKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1667](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-ordered-insert-key-with-cost).

## Removing the minimum from an interval tree preserves key ordering

Let $t$ be a
key-ordered interval tree. If the cost-instrumented removal of the leftmost entry of $t$ succeeds,
returning that entry, a remaining tree $t'$ and a cost, then $t'$ is key-ordered.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyOrdered_removeMinWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1706](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-ordered-remove-min-with-cost).

## Deletion from an interval tree preserves key ordering

Let $t$ be a key-ordered interval
tree and let $k \in \mathbb{Z} \times \mathbb{N}$ be a key. Then the tree returned by the
cost-instrumented keyed deletion of $k$ from $t$ (the reported cost is discarded) is again
key-ordered.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.keyOrdered_eraseKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#key-ordered-erase-key-with-cost).

## Rebalancing an interval-tree node with exact stored height restores AVL balance

Let $L$
and $R$ be interval trees that are AVL balanced with exact stored heights, with heights $h_L$ and
$h_R$ satisfying $h_L \le h_R + 2$ and $h_R \le h_L + 2$. Let $N$ be a node with left subtree $L$,
entry $e$ and right subtree $R$ whose stored height is $\max(h_L, h_R) + 1$ (its stored size and
stored maximum are arbitrary), and let $B$ be the tree obtained by rebalancing $N$ (the tree
component of the result; the cost is ignored). Then $B$ is AVL balanced with exact stored heights,
the height of $B$ is $\max(h_L, h_R) + 1$ or $\max(h_L, h_R)$, and it is $\max(h_L, h_R)$ only if
$h_L = h_R + 2$ or $h_R = h_L + 2$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balancedProp_rebalance_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop-rebalance-node).

## Rebalancing a rebuilt interval-tree node restores AVL balance

Let $L$ and $R$ be interval
trees that are AVL balanced with exact stored heights, with heights $h_L$ and $h_R$ satisfying
$h_L \le h_R + 2$ and $h_R \le h_L + 2$, and let $e$ be an entry. Let $B$ be the tree obtained by
rebalancing the node that the smart constructor builds from $L$, $e$ and $R$ (the tree component
of the result; the cost is ignored). Then $B$ is AVL balanced with exact stored heights, the
height of $B$ is $\max(h_L, h_R) + 1$ or $\max(h_L, h_R)$, and it is $\max(h_L, h_R)$ only if
$h_L = h_R + 2$ or $h_R = h_L + 2$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balancedProp_rebalance_mkNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1900](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1900). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop-rebalance-mk-node).

## Keyed insertion preserves AVL balance in an interval tree

Let $T$ be an interval tree that
is AVL balanced with exact stored heights, and let $e$ be an entry. The tree $T'$ returned by keyed
insertion of $e$ into $T$ (which replaces an entry with the same key, if there is one; we take the
tree component of the result and ignore the cost) is again AVL balanced with exact stored heights,
and the height of $T'$ is either the height of $T$ or one more.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balancedProp_insertKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1914](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1914). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop-insert-key-with-cost).

## Removing the minimum preserves AVL balance in an interval tree

Let $T$ be an interval tree
that is AVL balanced with exact stored heights. If removing the leftmost entry of $T$ succeeds and
returns an entry $m$, a remaining tree $R$ and a cost $c$, then $R$ is AVL balanced with exact
stored heights, and the height of $R$ is either the height of $T$ or one less.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balancedProp_removeMinWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1962](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop-remove-min-with-cost).

## Keyed deletion preserves AVL balance in an interval tree

Let $T$ be an interval tree that
is AVL balanced with exact stored heights, and let $k$ be a key (a pair of an integer low endpoint
and a natural-number identifier). The tree $T'$ returned by keyed deletion of $k$ from $T$ (the
tree component of the result; the cost is ignored) is again AVL balanced with exact stored
heights, and the height of $T'$ is either the height of $T$ or one less.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.balancedProp_eraseKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 1997](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L1997). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#balanced-prop-erase-key-with-cost).

## Node construction preserves interval validity

If $L$ and $R$ are interval trees
satisfying the validity invariant and $e$ is an entry whose interval $[a, b]$ satisfies
$a \le b$, then the node with left subtree $L$, entry $e$ and right subtree $R$, built by the
node constructor that recomputes the cached fields, satisfies the validity invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_mkNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2066](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-mk-node).

## Stored intervals of a valid tree are valid

If an interval tree $T$ satisfies the validity
invariant, then every entry stored in $T$ has an interval $[a, b]$ with $a \le b$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-mem).

## Keyed insertion preserves interval validity

Let $T$ be an interval tree in which every
stored interval $[a, b]$ satisfies $a \le b$, and let $e$ be an entry whose interval $[a, b]$
satisfies $a \le b$. Then the tree returned by keyed insertion of $e$ into $T$ also has every
stored interval $[a, b]$ satisfying $a \le b$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_insertKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-insert-key-with-cost).

## Removing the minimum preserves interval validity

Let $T$ be an interval tree in which
every stored interval is valid (its low endpoint is at most its high endpoint). If the
instrumented removal of the leftmost entry of $T$ succeeds, returning that entry $m$, the
remaining tree $T'$ and a cost record $c$, then every interval stored in $T'$ is valid.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_removeMinWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-remove-min-with-cost).

## Keyed erasure preserves interval validity

Let $T$ be an interval tree in which every
stored interval $[a, b]$ satisfies $a \le b$. Then for every key $(\ell, i)$ with $\ell$ an
integer and $i$ a natural number, the tree returned by keyed erasure of $(\ell, i)$ from $T$ also
has every stored interval $[a, b]$ satisfying $a \le b$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.validInvariant_eraseKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#valid-invariant-erase-key-with-cost).

## Indexed interval tree

An indexed interval tree consists of a root interval tree together
with an identifier index: a finite map, implemented as a balanced search tree, from natural-number
identifiers to integer low endpoints.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#indexed-interval-tree).

## Insertion by identifier with cost

Let $T$ be an indexed interval tree and let $e$ be an
entry with identifier $i$ and interval $[a, b]$. Inserting $e$ into $T$ first tests $a \le b$. If
$a > b$, it returns no tree, at a cost of one endpoint comparison. Otherwise, if the identifier
index of $T$ maps $i$ to a low endpoint $\ell$, the entry with key $(\ell, i)$ is erased from the
root tree of $T$ by keyed erasure; if $i$ is not in the index, the root tree is kept, at zero
cost. Then $e$ is inserted into the resulting tree by keyed insertion. The result is the indexed
interval tree with this new root tree and with the index updated to map $i$ to $a$, and the cost
is the cost of the erasure plus the cost of the insertion plus one endpoint comparison and two
index operations.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.insertWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#insert-with-cost).

## Erasure by identifier with cost

To erase identifier $i$ from an indexed interval tree,
look $i$ up in the identifier index. If it is absent, the tree is returned unchanged at a cost of
one index operation. If the index maps $i$ to a low endpoint $\ell$, the entry with key
$(\ell, i)$ is erased from the underlying interval tree, $i$ is removed from the index, and the
cost is the cost of the keyed erasure plus two index operations.

When the representation invariant holds, this deletes exactly the stored entry with identifier
$i$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.eraseWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#erase-with-cost).

## Forward identifier-index check

For an indexed interval tree, the forward index check
returns true exactly when the identifier index maps the identifier of every stored entry to the low
endpoint of that entry's interval.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.indexForwardOK`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#index-forward-ok).

## Backward identifier-index check

For an indexed interval tree, the backward index check
returns true exactly when, for every identifier $i$ that the identifier index maps to a low endpoint
$\ell$, some stored entry has identifier $i$ and an interval with low endpoint $\ell$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.indexBackwardOK`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#index-backward-ok).

## Representation check for the indexed interval tree

For an indexed interval tree, the
check returns true exactly when all of the following hold: at every node the cached height and size
agree with the values recomputed from its children's cached heights and sizes, and the cached
maximum high endpoint equals the largest of the node's own high endpoint and its children's cached
maxima; the tree is AVL-balanced (sibling heights differ by at most one) with exact stored heights;
the entry keys (low endpoint, identifier), ordered lexicographically, are strictly ordered as a
binary search tree and every stored interval has low endpoint at most its high endpoint; the
identifiers of the stored entries are pairwise distinct; the identifier index maps the identifier of
every stored entry to that entry's low endpoint; and every identifier and low endpoint paired by the
index belong to some stored entry.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.check`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#check).

## Representation invariant of an indexed interval tree

An indexed interval tree $T$
satisfies the representation invariant when its root tree has exact cached metadata (heights,
sizes, and attained maximum high endpoints), is strictly ordered by the composite key (low
endpoint, then identifier), is AVL balanced with exact stored heights, and stores only valid
intervals; the identifiers of the stored entries are pairwise distinct; the identifier index maps
the identifier of every stored entry to that entry's low endpoint; and every pair $(i, \ell)$ in
the identifier index is the identifier and low endpoint of some stored entry.

The ordering of low endpoints used by search follows from the strict key ordering.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.Invariant`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#invariant).

## The interval-tree smart constructor preserves the cache invariant

If interval trees $L$
and $R$ satisfy the cache invariant (every cached maximum high endpoint, height and size is
exact), then for every entry $e$ the node that the smart constructor builds from $L$, $e$ and $R$
also satisfies the cache invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_mkNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-mk-node).

## The executable cache check implies the cache invariant

If the executable cache check
returns true on an interval tree $t$, then $t$ satisfies the cache invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_of_cacheOK`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-of-cache-ok).

## Right rotation preserves the interval-tree cache invariant

If an interval tree $t$
satisfies the cache invariant, then so does the right rotation of $t$, which leaves $t$ unchanged
when $t$ is empty or has an empty left subtree.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_rotateRight`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-rotate-right).

## Left rotation preserves the interval-tree cache invariant

If an interval tree $t$
satisfies the cache invariant, then so does the left rotation of $t$, which leaves $t$ unchanged
when $t$ is empty or has an empty right subtree.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_rotateLeft`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-rotate-left).

## Left-right rotation preserves the interval-tree cache invariant

If an interval tree $t$
satisfies the cache invariant, then so does the left-right double rotation of $t$, which leaves
$t$ unchanged unless $t$ has a nonempty left subtree whose right subtree is nonempty.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_rotateLeftRight`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-rotate-left-right).

## Right-left rotation preserves the interval-tree cache invariant

If an interval tree $t$
satisfies the cache invariant, then so does the right-left double rotation of $t$, which leaves
$t$ unchanged unless $t$ has a nonempty right subtree whose left subtree is nonempty.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_rotateRightLeft`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-rotate-right-left).

## Rebalancing preserves the interval-tree cache invariant

If an interval tree $t$
satisfies the cache invariant, then the tree returned by the rebalancing step at the root of $t$
also satisfies the cache invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_rebalanceWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-rebalance-with-cost).

## Keyed insertion preserves the interval-tree cache invariant

Let $T$ be an interval tree
satisfying the cache invariant (every cached maximum high endpoint, height and size is exact), and
let $e$ be an entry. The tree returned by keyed insertion of $e$ into $T$ (the tree component of
the result; the cost is ignored) also satisfies the cache invariant. This includes the case where
an entry with the same key is replaced.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_insertKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-insert-key-with-cost).

## Removing the minimum preserves the interval-tree cache invariant

Let $t$ be an interval
tree that satisfies the cache invariant. If removing the leftmost entry of $t$ succeeds and
returns an entry, a tree $t'$ and an operation cost, then $t'$ satisfies the cache invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_removeMinWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-remove-min-with-cost).

## Keyed deletion preserves the interval-tree cache invariant

Let $T$ be an interval tree
satisfying the cache invariant (every cached maximum high endpoint, height and size is exact), and
let $k$ be a key (a pair of an integer low endpoint and a natural-number identifier). The tree
returned by keyed deletion of $k$ from $T$ (the tree component of the result; the cost is
ignored) also satisfies the cache invariant. This includes keys that do not occur in $T$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.Tree.cacheInvariant_eraseKeyWithCost`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#cache-invariant-erase-key-with-cost).

## Soundness of the invariant checker

If the executable checker returns true on an indexed
interval tree $T$, then $T$ satisfies the representation invariant.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.invariant_of_check`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#invariant-of-check).

## Soundness of indexed interval-tree search

The search of an indexed interval tree $T$ for
a query interval $q = [c, d]$ returns nothing when $c > d$, and otherwise returns the entry, if
any, found by the instrumented overlap search of $q$ in the root tree of $T$. For every indexed
interval tree $T$, every query interval $q$ and every entry $e$, if this search returns $e$, then
$e$ is one of the entries stored in the root tree of $T$ and the interval of $e$ overlaps $q$.

The representation invariant of $T$ is not needed.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.search_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-sound).

## Completeness of indexed interval search

Let $T$ be an indexed interval tree satisfying
its representation invariant, and let $Q$ be a valid query interval (low endpoint at most high
endpoint). If some entry stored in $T$ has an interval that overlaps $Q$ (each interval's low
endpoint is at most the other's high endpoint), then searching $T$ for $Q$ returns some entry.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.search_complete_of_invariant`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#search-complete-of-invariant).

## Correctness of insertion into an indexed interval tree

Let $T$ be an indexed interval tree
satisfying the representation invariant, and let $x$ be an entry whose interval is valid (its low
endpoint is at most its high endpoint). If inserting $x$ into $T$ succeeds with result $T'$, then
$T'$ satisfies the representation invariant, $x$ is stored in the root tree of $T'$, and an entry
$e$ is stored in the root tree of $T'$ if and only if either $e = x$, or $e$ is stored in the root
tree of $T$ and the identifier of $e$ differs from the identifier of $x$.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.insert_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#insert-spec).

## Correctness of erasure from the indexed interval tree

Let $T$ be an indexed interval tree
satisfying the representation invariant, and let $i$ be a natural number. Then the tree obtained by
erasing identifier $i$ from $T$ again satisfies the invariant, and an entry is stored in it if and
only if it is stored in $T$ and its identifier differs from $i$.

In particular, if no stored entry has identifier $i$, the stored entries are unchanged.

Formalized by `Cslib.Algorithms.Lean.IntervalTree.IndexedIntervalTree.erase_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean, line 2792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IntervalTree.lean#L2792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html#erase-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Interval tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/interval-tree)
