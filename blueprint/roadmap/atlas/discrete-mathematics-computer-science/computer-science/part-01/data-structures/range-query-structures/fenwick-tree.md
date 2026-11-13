---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FenwickTree, Cslib.Algorithms.Lean.FenwickTree.lowbit, Cslib.Algorithms.Lean.FenwickTree.lowbit_zero, Cslib.Algorithms.Lean.FenwickTree.lowbit_pos, Cslib.Algorithms.Lean.FenwickTree.lowbit_le, Cslib.Algorithms.Lean.FenwickTree.lowbit_dvd, Cslib.Algorithms.Lean.FenwickTree.lowbit_two_pow, Cslib.Algorithms.Lean.FenwickTree.lowbit_div_odd
statement: formalized
proof: formalized
---

# Fenwick tree

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html).

## Fenwick Tree

## Fenwick tree

A Fenwick tree (binary indexed tree) over a commutative additive monoid
$\alpha$ is an array of elements of $\alpha$, read as one-indexed interval sums with an unused
dummy entry at index $0$. The structure itself imposes no condition on the entries, and the
underlying array it represents is not stored; the relation saying that a tree represents a
given array is defined separately.

Formalized by `Cslib.Algorithms.Lean.FenwickTree`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#fenwick-tree).

## Lowest set bit

For a natural number $n > 0$, $\operatorname{lowbit}(n)$ is the largest
power of two dividing $n$; for $n = 0$ it is defined as $\operatorname{lowbit}(0) = 0$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit).

## Lowbit of zero

By convention, $\operatorname{lowbit}(0) = 0$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-zero).

## The lowest set bit of a positive number is positive

For every natural number $n > 0$,
$\operatorname{lowbit}(n) > 0$, where $\operatorname{lowbit}(n)$ is the value of the lowest set
bit of $n$ in binary.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_pos`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-pos).

## The lowest set bit is at most the number

For every natural number $n$,
$\operatorname{lowbit}(n) \le n$, where $\operatorname{lowbit}(n)$ is the value of the lowest
set bit of $n$ in binary (with $\operatorname{lowbit}(0) = 0$).

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-le).

## The lowest set bit divides the number

For every natural number $n > 0$,
$\operatorname{lowbit}(n)$ divides $n$, where $\operatorname{lowbit}(n)$ is the value of the
lowest set bit of $n$ in binary.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_dvd`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-dvd).

## The lowest set bit is a power of two

For every natural number $n > 0$,
$\operatorname{lowbit}(n)$ is a power of two: $\operatorname{lowbit}(n) = 2^k$ for some natural
number $k$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_two_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-two-pow).

## Dividing out the lowest set bit leaves an odd number

For every natural number $n > 0$,
the quotient $n / \operatorname{lowbit}(n)$ is odd, where $\operatorname{lowbit}(n)$ is the
value of the lowest set bit of $n$ in binary.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.lowbit_div_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#lowbit-div-odd).

## Fenwick-tree interval sum of a list

For a list $a$ of elements of a commutative additive
monoid $\alpha$ and a natural number $j$, the interval sum at the one-indexed position $j$ is
the sum of the $\operatorname{lowbit}(j)$ entries of $a$ ending at zero-indexed position
$j - 1$, where $\operatorname{lowbit}(j)$ is the largest power of two dividing $j$ (with
$\operatorname{lowbit}(0) = 0$) and entries past the end of $a$ count as $0$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.blockSum`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#block-sum).

## Interval sum read from an array

For an array $a$ of elements of a commutative additive
monoid $\alpha$ and a natural number $j$, this is the sum of the $\operatorname{lowbit}(j)$
entries of $a$ ending at zero-indexed position $j - 1$, where $\operatorname{lowbit}(j)$ is the
largest power of two dividing $j$ (with $\operatorname{lowbit}(0) = 0$) and entries past the
end of $a$ count as $0$.

It has the same value as the list-based interval sum but reads each entry in constant time;
Fenwick-tree construction uses it, so building takes $O(n \log n)$ reads rather than quadratic
list indexing.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.blockSumArray`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#block-sum-array).

## Fenwick tree representing a list

A Fenwick tree $t$ over an additive commutative monoid
represents a list $a$ of length $n$ when its stored array has length $n + 1$ (a dummy entry at
index $0$ plus one entry per element of $a$) and, for every $j$ with $1 \le j \le n$, the stored
entry at index $j$ equals the block sum of $a$ at $j$: the sum of the $\operatorname{lowbit}(j)$
entries of $a$ ending at position $j - 1$ (positions counted from $0$), where
$\operatorname{lowbit}(j)$ is the largest power of two dividing $j$.

The underlying list itself is not stored at runtime; it appears only in this specification
relation.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#valid).

## Size of a Fenwick tree

The size of a Fenwick tree is the length of its stored array
minus one, truncated at $0$; the one accounts for the dummy entry at index $0$. It is read off
the stored array in constant time.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#size).

## A Fenwick tree has the length of the list it represents

If a Fenwick tree $t$ over an
additive commutative monoid represents a list $a$, then the size of $t$ equals the length of
$a$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.size_eq_length_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#size-eq-length-of-valid).

## Building a Fenwick tree from a list

For a list $a$ of length $n$ over a commutative
additive monoid $\alpha$, the Fenwick tree built from $a$ stores the array of length $n + 1$
whose entry at index $0$ is $0$ and whose entry at each one-indexed position $j$ with
$1 \le j \le n$ is the sum of the $\operatorname{lowbit}(j)$ entries of $a$ ending at
zero-indexed position $j - 1$, where $\operatorname{lowbit}(j)$ is the largest power of two
dividing $j$.

The input is converted to an array once, so each entry read is constant-time and construction
is $O(n \log n)$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#build).

## Size of a built Fenwick tree

For every list $a$ over an additive commutative monoid,
the Fenwick tree built from $a$ has size equal to the length of $a$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.size_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#size-build).

## Building a Fenwick tree yields a valid representation

For every list $a$ over an
additive commutative monoid, the Fenwick tree built from $a$ represents $a$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.valid_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#valid-build).

## Fenwick tree prefix sum

Let $t$ be a Fenwick tree over an additive commutative monoid
with $n$ underlying entries, let $k$ be a natural number and let $m = \min(k, n)$. The prefix sum
of length $k$ of $t$ is the sum of the stored entries of $t$ at the positions $j_0 = m$,
$j_{r+1} = j_r - \operatorname{lowbit}(j_r)$, taken for as long as $j_r > 0$.

When $t$ represents a list, this is the sum of its first $m$ entries, so queries past the end
are clamped.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.prefixSum`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#prefix-sum).

## The empty prefix sum is zero

For every Fenwick tree $t$ over an additive commutative
monoid, the prefix sum of length $0$ of $t$ is $0$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.prefixSum_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#prefix-sum-zero).

## Correctness of Fenwick tree prefix sums

Let $t$ be a Fenwick tree representing a list $a$
of elements of an additive commutative monoid. Then for every natural number $k$, including
$k > |a|$, the prefix sum of length $k$ of $t$ equals the sum of the first $\min(k, |a|)$ entries
of $a$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.prefixSum_eq_take_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#prefix-sum-eq-take-sum).

## Prefix sums of a built Fenwick tree

For every list $a$ of elements of an additive
commutative monoid and every natural number $k$, the prefix sum of length $k$ of the Fenwick tree
built from $a$ equals the sum of the first $\min(k, |a|)$ entries of $a$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.prefixSum_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 560](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L560). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#prefix-sum-build).

## Point update of a Fenwick tree

Let $t$ be a Fenwick tree over a commutative additive
monoid $\alpha$, let $n$ be its size (the length of its stored array minus one), let $i$ be a
natural number and let $\delta \in \alpha$. Adding $\delta$ at underlying position $i$ adds
$\delta$ to the stored entries at the one-indexed positions $j_1 = i + 1$ and
$j_{k+1} = j_k + \operatorname{lowbit}(j_k)$, for as long as $j_k \le n$, where
$\operatorname{lowbit}(j)$ is the largest power of two dividing $j$; every other stored entry
is left unchanged. In particular, if $i \ge n$ the tree is unchanged.

Each write is constant-time only when the stored array is uniquely referenced, since a shared
array is copied by the first persistent write. The walk is fuelled by the size, which always
suffices because the visited positions strictly increase.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.add`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#add).

## Out-of-range point updates leave a Fenwick tree unchanged

Let $t$ be a Fenwick tree
over a commutative additive monoid $\alpha$, and let $n$ be its size (the length of its stored
array minus one). For every natural number $i \ge n$ and every $\delta \in \alpha$, the point
update of $t$ adding $\delta$ at position $i$ returns $t$ itself.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.add_eq_self_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#add-eq-self-of-le).

## Point update preserves representation

Let $t$ be a Fenwick tree over an additive
commutative monoid that represents a list $a$ of length $n$. For every index $i < n$ (counting
from $0$) and every element $\delta$, the tree obtained from $t$ by adding $\delta$ at position
$i$ represents the list obtained from $a$ by replacing its entry $a_i$ with $a_i + \delta$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.valid_add`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#valid-add).

## Prefix sums after a point update

Let $t$ be a Fenwick tree representing a list $a$ of
elements of an additive commutative monoid, let $i < |a|$ be a position, let $\delta$ be an
element of the monoid, and let $k$ be any natural number, possibly larger than $|a|$. Then the
prefix sum of length $k$ of the tree obtained from $t$ by adding $\delta$ at position $i$ equals
the prefix sum of length $k$ of $t$ plus $\delta$ if $i < k$, and equals the prefix sum of
length $k$ of $t$ if $k \le i$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.prefixSum_add`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#prefix-sum-add).

## Fenwick tree range sum

For a Fenwick tree $t$ over an additive commutative group and
natural numbers $\mathit{lo}$ and $\mathit{hi}$, the range sum of $t$ over
$[\mathit{lo}, \mathit{hi})$ is $0$ if $\mathit{hi} \le \mathit{lo}$, and otherwise the prefix sum
of length $\mathit{hi}$ of $t$ minus the prefix sum of length $\mathit{lo}$ of $t$.

When $t$ represents a list, this is the sum of its entries with indices in
$[\mathit{lo}, \mathit{hi})$. This is the only Fenwick tree operation that needs additive
inverses.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.rangeSum`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 771](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#range-sum).

## Correctness of Fenwick tree range sums

Let $t$ be a Fenwick tree representing a list
$a = (a_0, \dots, a_{n-1})$ of elements of an additive commutative group. Then for all natural
numbers $\mathit{lo}$ and $\mathit{hi}$, the range sum of $t$ over $[\mathit{lo}, \mathit{hi})$
equals $\sum_{\mathit{lo} \le i < \min(\mathit{hi}, n)} a_i$; in particular it is $0$ when
$\mathit{hi} \le \mathit{lo}$.

Formalized by `Cslib.Algorithms.Lean.FenwickTree.rangeSum_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean, line 778](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/FenwickTree.lean#L778). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html#range-sum-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fenwick tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/fenwick-tree)
