---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.normalizedArity, Cslib.Algorithms.Lean.normalizedArity_valid, Cslib.Algorithms.Lean.normalizedArity_eq, Cslib.Algorithms.Lean.daryParent, Cslib.Algorithms.Lean.daryChild, Cslib.Algorithms.Lean.daryParent_child, Cslib.Algorithms.Lean.daryParent_lt, Cslib.Algorithms.Lean.daryParent_lt_size
statement: formalized
proof: formalized
---

# d-ary heap

55 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html).

## Normalized heap arity

The normalized arity of a requested arity $r \in \mathbb{N}$ is
$\max(2, r)$: the requested arities $0$ and $1$ become $2$ (the binary-heap policy), and every
$r \ge 2$ is left unchanged.

Formalized by `Cslib.Algorithms.Lean.normalizedArity`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#normalized-arity).

## Normalized arities are at least two

For every natural number $r$, the normalized arity
$\max(2, r)$ of $r$ is at least $2$.

Formalized by `Cslib.Algorithms.Lean.normalizedArity_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#normalized-arity-valid).

## Normalization leaves a valid arity unchanged

For every natural number $d \ge 2$, the
normalized arity $\max(2, d)$ of $d$ equals $d$.

Formalized by `Cslib.Algorithms.Lean.normalizedArity_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#normalized-arity-eq).

## Parent index in a $d$-ary tree

For natural numbers $d$ and $i$, the $d$-ary parent of $i$
is $\lfloor (i - 1)/d \rfloor$, computed in the natural numbers: $i - 1$ is truncated at $0$, so
the parent of $0$ is $0$, and division by $0$ gives $0$.

This is the parent index when a $d$-ary tree is stored in level order in an array with its root
at index $0$.

Formalized by `Cslib.Algorithms.Lean.daryParent`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-parent).

## Child index in a $d$-ary heap array

For natural numbers $d$, $i$ and $k$, the child of
index $i$ with zero-based offset $k$ in a contiguous level-order $d$-ary tree is the index
$d i + k + 1$.

Formalized by `Cslib.Algorithms.Lean.daryChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-child).

## The parent of a $d$-ary child

Let $d$, $i$ and $k$ be natural numbers with $d \ge 2$ and
$k < d$. Then the $d$-ary parent of the child of $i$ with zero-based offset $k$, that is, of the
index $di + k + 1$, is $i$.

Formalized by `Cslib.Algorithms.Lean.daryParent_child`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-parent-child).

## A $d$-ary parent has a smaller index

Let $d$ and $i$ be natural numbers with $d \ge 2$ and
$i > 0$. Then the $d$-ary parent of $i$ is strictly less than $i$.

Formalized by `Cslib.Algorithms.Lean.daryParent_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-parent-lt).

## The $d$-ary parent of a valid index is valid

Let $d \ge 2$ be a natural number, let $a$ be
an array over any type, write $|a|$ for its size, and let $i$ be an index with $0 < i < |a|$.
Then the $d$-ary parent of $i$ is also less than $|a|$.

Formalized by `Cslib.Algorithms.Lean.daryParent_lt_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-parent-lt-size).

## $d$-ary heap order

Let $d$ be a natural number and $a = (a_0, \dots, a_{n-1})$ an array
with entries in a type carrying a relation $\le$. The array $a$ is $d$-ary heap ordered when
$d \ge 2$ and every nonroot entry is at least the entry at its parent index:
$a_{\lfloor (i-1)/d \rfloor} \le a_i$ for every index $i$ with $0 < i < n$.

Formalized by `Cslib.Algorithms.Lean.DaryHeapOrdered`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-heap-ordered).

## Arrays ready for $d$-ary sift-up

Let $a = (a_0, \dots, a_{|a|-1})$ be an array over a
type with a relation $\le$, let $d$ and $i$ be natural numbers, and write
$p(j) = \lfloor (j-1)/d \rfloor$ for the parent of an index $j > 0$. The array $a$ is ready for
sift-up at $i$ when $d \ge 2$, $i < |a|$, $a_{p(j)} \le a_j$ for every $0 < j < |a|$ with
$j \ne i$, and, if $i > 0$, $a_{p(i)} \le a_j$ for every $0 < j < |a|$ with $p(j) = i$.

So the only edge that may violate heap order is the one entering $i$, and the parent of $i$ is
no greater than the children of $i$.

Formalized by `Cslib.Algorithms.Lean.DarySiftUpReady`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-up-ready).

## $d$-ary sift-up

Let $d \ge 2$, let $a$ be an array over a linearly ordered type, of length
$|a|$ with entries $a_0, \dots, a_{|a|-1}$, let $i$ be a natural number, and write
$p(i) = \lfloor (i-1)/d \rfloor$ for the parent of $i > 0$. The sift-up of $a$ from $i$ is defined
recursively: if $0 < i < |a|$ and $a_i < a_{p(i)}$, it is the sift-up from $p(i)$ of the array
obtained from $a$ by swapping the entries at positions $i$ and $p(i)$; otherwise it is $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftUp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-up).

## Sifting up permutes the array

Let $d \ge 2$, let $a$ be an array over a linearly ordered
type and let $i$ be a natural number. The array obtained from $a$ by $d$-ary sift-up from index $i$
is a permutation of $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftUp_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-up-perm).

## Sifting up preserves the multiset of entries

Let $d \ge 2$, let $a$ be an array over a
linearly ordered type and let $i$ be a natural number. The array obtained from $a$ by $d$-ary
sift-up from index $i$ has the same multiset of entries as $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftUp_multiset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-up-multiset).

## The root of a $d$-ary heap-ordered array is a minimum

Let $\alpha$ be a linearly ordered
type, let $d \ge 2$, and let $a$ be an array of elements of $\alpha$ that is $d$-ary
heap-ordered. Then $a_0 \le a_i$ for every index $i$ smaller than the size of $a$.

Formalized by `Cslib.Algorithms.Lean.DaryHeapOrdered.root_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#root-le).

## Sift-up restores $d$-ary heap order

Let $a$ be an array over a linearly ordered type,
of length $|a|$ with entries $a_0, \dots, a_{|a|-1}$, let $d$ and $i$ be natural numbers, and
write $p(j) = \lfloor (j-1)/d \rfloor$ for the parent of an index $j > 0$. Suppose $a$ is ready
for sift-up at $i$: $d \ge 2$, $i < |a|$, $a_{p(j)} \le a_j$ for every $0 < j < |a|$ with
$j \ne i$, and, if $i > 0$, $a_{p(i)} \le a_j$ for every $0 < j < |a|$ with $p(j) = i$. Then the
array $b$, of length $|b|$ with entries $b_0, \dots, b_{|b|-1}$, obtained from $a$ by $d$-ary
sift-up from index $i$ is $d$-ary heap ordered: $b_{p(j)} \le b_j$ for every $0 < j < |b|$.

Formalized by `Cslib.Algorithms.Lean.darySiftUp_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-up-ordered).

## Pushing onto a $d$-ary heap leaves it ready for sifting up

Let $\alpha$ be a linearly
ordered type, let $d \ge 2$, and let $a$ be an array over $\alpha$ that is $d$-ary heap ordered,
with size $|a|$. Then for every $x \in \alpha$, the array obtained by appending $x$ to $a$ is
ready for $d$-ary sifting up at index $|a|$, the position of $x$; in particular every nonroot
entry other than $x$ is at least its $d$-ary parent.

Formalized by `Cslib.Algorithms.Lean.daryPush_siftUpReady`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-push-sift-up-ready).

## Readiness for $d$-ary sift-down

Let $a$ be an array over a type with a relation $\le$,
and let $d$ and $i$ be natural numbers. Write $|a|$ for the size of $a$ and $p(j)$ for the
$d$-ary parent of an index $j$. The array $a$ is ready for $d$-ary sifting down at $i$ when
$d \ge 2$, $i < |a|$, every index $j$ with $0 < j < |a|$ and $p(j) \ne i$ satisfies
$a_{p(j)} \le a_j$, and, if $i > 0$, every index $j$ with $0 < j < |a|$ and $p(j) = i$ satisfies
$a_{p(i)} \le a_j$.

Thus the only edges that may violate heap order leave $i$, and lifting a smallest child to $i$
keeps the edge entering $i$ ordered.

Formalized by `Cslib.Algorithms.Lean.DarySiftDownReady`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-down-ready).

## Smallest child among the offsets from $s$

Let $a$ be an array over a linearly ordered
type, of length $|a|$, let $d$, $i$ and $s$ be natural numbers, and call $d i + k + 1$ the child
of $i$ at offset $k$. Scanning the offsets $s, s + 1, \dots, d - 1$, this returns the index of a
scanned child of $i$ below $|a|$ whose entry in $a$ is least among those, taking the smallest
offset among ties, or nothing if no scanned child index is below $|a|$.

Formalized by `Cslib.Algorithms.Lean.darySmallestChildFrom`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-smallest-child-from).

## Smallest child in a $d$-ary heap array

Let $a$ be an array of length $|a|$ over a linearly
ordered type and let $d$ and $i$ be natural numbers. The children of $i$ are the indices
$d i + k + 1$ for $0 \le k < d$, and a child is valid when it is below $|a|$. The smallest child
of $i$ is the valid child of $i$ with the least entry, taking the smallest offset $k$ among ties,
or nothing if $i$ has no valid child.

Formalized by `Cslib.Algorithms.Lean.darySmallestChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-smallest-child).

## The smallest child is a valid index

Let $a$ be an array of length $|a|$ over a linearly
ordered type and let $d$, $i$ and $c$ be natural numbers. If the smallest valid child of $i$ in
the $d$-ary heap array $a$ is $c$, then $c < |a|$.

Formalized by `Cslib.Algorithms.Lean.darySmallestChild_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-smallest-child-valid).

## The smallest child lies after its parent

Let $d \ge 2$, let $a$ be an array over a
linearly ordered type and let $i$ and $c$ be natural numbers. If the smallest valid child of $i$
in the $d$-ary heap array $a$ is $c$, then $i < c$.

Formalized by `Cslib.Algorithms.Lean.darySmallestChild_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-smallest-child-gt).

## $d$-ary sift-down

Let $\alpha$ be a linearly ordered type, let $a$ be an array over
$\alpha$, and let $i$ and $d$ be natural numbers with $d \ge 2$. Sifting down from $i$ in $a$
returns $a$ if $i$ has no valid $d$-ary child in $a$. Otherwise let $c$ be the smallest valid
$d$-ary child of $i$, with ties broken toward the lowest child offset: if $a_c < a_i$, swap the
entries at $i$ and $c$ and sift down from $c$ in the resulting array; otherwise return $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftDown`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-down).

## Sifting down in a $d$-ary heap permutes the array

Let $\alpha$ be a linearly ordered type,
let $a$ be an array over $\alpha$, and let $i$ and $d$ be natural numbers with $d \ge 2$. The
array produced by $d$-ary sifting down from index $i$ in $a$ is a permutation of $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftDown_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-down-perm).

## Sifting down in a $d$-ary heap preserves the multiset of entries

Let $\alpha$ be a
linearly ordered type, let $a$ be an array over $\alpha$, and let $i$ and $d$ be natural numbers
with $d \ge 2$. The array produced by $d$-ary sifting down from index $i$ in $a$ has the same
multiset of entries as $a$.

Formalized by `Cslib.Algorithms.Lean.darySiftDown_multiset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-down-multiset).

## Sifting down restores $d$-ary heap order

Let $\alpha$ be a linearly ordered type, let
$d \ge 2$, and let $a$ be an array over $\alpha$ that is ready for $d$-ary sifting down at an
index $i$. Then the array produced by $d$-ary sifting down from index $i$ in $a$ is $d$-ary heap
ordered.

Formalized by `Cslib.Algorithms.Lean.darySiftDown_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-sift-down-ordered).

## Last-to-root move on an array

For a nonempty array $a = (a_0, \dots, a_{n-1})$, the
last-to-root move swaps $a_0$ and $a_{n-1}$ and then deletes the last entry, producing an array
$b = (b_0, \dots, b_{n-2})$ of length $n - 1$: when $n \ge 2$, $b_0 = a_{n-1}$ and
$b_i = a_i$ for $0 < i < n - 1$, and $b$ is empty when $n = 1$.

Formalized by `Cslib.Algorithms.Lean.daryMoveLastToRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-move-last-to-root).

## Last-to-root move in a $d$-ary heap is ready for sift-down

Let $d$ be a natural number,
let $a$ be a $d$-ary heap ordered array with at least two entries over a linearly ordered type,
and let $b = (b_0, \dots, b_{m-1})$ be the array obtained from $a$ by the last-to-root move.
Then $b$ is ready for a $d$-ary sift-down at index $0$: $d \ge 2$, $0 < m$, and
$b_{\lfloor (j-1)/d \rfloor} \le b_j$ for every index $j$ with $0 < j < m$ whose parent index
$\lfloor (j-1)/d \rfloor$ is not $0$.

Formalized by `Cslib.Algorithms.Lean.daryMoveLastToRoot_siftDownReady`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-move-last-to-root-sift-down-ready).

## Last-to-root move in a $d$-ary heap removes one copy of the root

For every nonempty
array $a = (a_0, \dots, a_{n-1})$ over a linearly ordered type, the multiset of entries of the
array obtained from $a$ by the last-to-root move equals the multiset of entries of $a$ with one
occurrence of $a_0$ removed.

Formalized by `Cslib.Algorithms.Lean.daryMoveLastToRoot_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 749](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L749). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-move-last-to-root-elements).

## $d$-ary min-heap

A $d$-ary min-heap over a linearly ordered type $\alpha$ consists of a
natural number $d \ge 2$, its arity, and an array $a = (a_0, \dots, a_{n-1})$ of elements of
$\alpha$, stored in level order, that is $d$-ary heap ordered:
$a_{\lfloor (i-1)/d \rfloor} \le a_i$ for every index $i$ with $0 < i < n$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#dary-min-heap).

## Elements of a d-ary heap

The multiset of elements of a $d$-ary min-heap $h$ over a
linearly ordered type is the multiset of the entries of its level-order storage array, counted
with multiplicity.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#elements).

## Empty d-ary heap

For a natural number $r$ (the requested arity), the empty heap is the
$d$-ary min-heap over a linearly ordered type with arity $d = \max(2, r)$ and an empty storage
array; a requested arity below two is thus normalized to two.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#empty).

## Insertion into a $d$-ary heap

Inserting a value $x$ into a $d$-ary min-heap $h$ of arity
$d$ gives the heap of the same arity $d$ whose array is obtained by appending $x$ at the end of
the level-order array of $h$ and sifting it up from that last index: while the current index
$i > 0$ holds an entry strictly smaller than the entry at its parent index
$\lfloor (i-1)/d \rfloor$, the two entries are swapped and the process continues from the
parent. Only the ancestor path of the new entry is changed.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.push`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#push).

## Minimum query on a $d$-ary min-heap

The minimum query on a $d$-ary min-heap $h$
returns the entry at index $0$ (the root) of the storage array of $h$, or nothing if the array
is empty.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.min?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#min).

## The minimum query on a $d$-ary heap fails exactly when it is empty

For a $d$-ary
min-heap $h$, the minimum query on $h$ (which returns the entry at index $0$ of the storage
array, if any) returns nothing if and only if the storage array of $h$ is empty.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.min?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 796](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L796). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#min-eq-none-iff).

## The minimum query on a $d$-ary heap returns an element of the heap

Let $h$ be a
$d$-ary min-heap. If the minimum query on $h$ returns $x$, then $x$ belongs to the multiset of
elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.min?_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#min-mem).

## The minimum query on a $d$-ary heap returns a least element

Let $h$ be a $d$-ary
min-heap. If the minimum query on $h$ returns $x$, then $x \le y$ for every element $y$ of the
multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.min?_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#min-le).

## Insertion into a d-ary heap adds one occurrence

For a $d$-ary min-heap $h$ over a
linearly ordered type and a value $x$, the multiset of elements of the heap obtained by inserting
$x$ into $h$ is the multiset of elements of $h$ with one more occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.elements_push`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 826](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L826). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#elements-push).

## Insertion keeps a $d$-ary heap ordered

Let $h$ be a $d$-ary min-heap of arity $d$ and let
$x$ be a value. Then the level-order array of the heap obtained by inserting $x$ into $h$ is
$d$-ary heap-ordered for the same arity $d$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.push_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 835](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#push-ordered).

## Insertion into a $d$-ary heap raises the multiplicity by one

For every $d$-ary min-heap
$h$ over a linearly ordered type and every value $x$, the multiplicity of $x$ among the elements
of the heap obtained by inserting $x$ into $h$ is one more than its multiplicity among the
elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.count_push_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#count-push-self).

## Insertion into a $d$-ary heap preserves other multiplicities

For every $d$-ary min-heap
$h$ over a linearly ordered type and all values $x \ne y$, the multiplicity of $y$ among the
elements of the heap obtained by inserting $x$ into $h$ equals the multiplicity of $y$ among the
elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.count_push_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#count-push-of-ne).

## Removing the root of a $d$-ary min-heap

Let $h$ be a $d$-ary min-heap whose storage
array $a$ is nonempty. Removing the root of $h$ gives the heap of arity $d$ whose storage array
is empty if $a$ has one entry. Otherwise the last entry of $a$ replaces the root, the last
position is dropped, and the new root is repeatedly swapped with its smallest $d$-ary child
while that child is smaller.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractTail`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-tail).

## Removing the root of a $d$-ary heap preserves its arity

For a $d$-ary min-heap $h$
with nonempty storage array, the heap obtained from $h$ by removing its root has the same
arity $d$ as $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractTail_arity`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 871](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L871). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-tail-arity).

## Building a $d$-ary min-heap from a list

Let $\alpha$ be a linearly ordered type, let
$r \in \mathbb{N}$ be a requested arity, and let $d = \max(2, r)$. The min-heap built from the
empty list is the empty min-heap of arity $d$, and the min-heap built from a list with head $x$
and tail $xs$ of elements of $\alpha$ is obtained by inserting $x$ into the min-heap built from
$xs$. Thus the min-heap built from $[x_1, \dots, x_n]$ starts from the empty min-heap of arity
$d$ and inserts $x_n$, then $x_{n-1}$, and so on, ending with $x_1$, each by $d$-ary
insertion.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.ofList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 934](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L934). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#of-list).

## Building a heap from a list keeps its elements

For every requested arity $r$ and every
list $xs$ over a linearly ordered type, the multiset of elements of the min-heap of arity
$\max(2, r)$ built from $xs$ by successive insertions equals the multiset of entries of $xs$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.elements_ofList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 940](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L940). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#elements-of-list).

## Arity of a $d$-ary heap built from a list

For every requested arity $r \in \mathbb{N}$
and every list $xs$ over a linearly ordered type, the $d$-ary min-heap built from $xs$ with
requested arity $r$ has arity equal to the normalized arity of $r$, namely $\max(2, r)$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.arity_ofList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 950](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L950). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#arity-of-list).

## Extracting the minimum of a $d$-ary min-heap

For a $d$-ary min-heap $h$,
extracting the minimum returns nothing if the storage array of $h$ is empty. Otherwise it
returns the root entry (the entry at index $0$) together with the heap obtained from $h$ by
removing its root: the last entry moves to the root and sifts down along a single $d$-ary
child path.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 959](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L959). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min).

## Extracting the minimum of a d-ary heap fails exactly on the empty heap

For a $d$-ary
min-heap $h$ over a linearly ordered type, extracting the minimum from $h$ returns no result if
and only if the storage array of $h$ is empty.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 967](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L967). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-eq-none-iff).

## Extracted minimum and remaining d-ary heap recover the original elements

Let $h$ be a
$d$-ary min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds,
returning a value $x$ and a heap $h'$, then the multiset of elements of $h$ is the multiset of
elements of $h'$ with one more occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_cons_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 972](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L972). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-cons-elements).

## Extracting the minimum of a d-ary heap removes one occurrence

Let $h$ be a $d$-ary
min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds, returning a
value $x$ and a heap $h'$, then the multiset of elements of $h'$ is obtained from the multiset of
elements of $h$ by removing one occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 984](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L984). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-elements).

## Extracting the minimum of a d-ary heap lowers its multiplicity by one

Let $h$ be a
$d$-ary min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds,
returning a value $x$ and a heap $h'$, then the multiplicity of $x$ in the multiset of elements
of $h'$ is its multiplicity in the multiset of elements of $h$ minus one.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_count`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 991](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L991). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-count).

## The extracted minimum of a d-ary heap is one of its elements

Let $h$ be a $d$-ary
min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds, returning a
value $x$ and a heap $h'$, then $x$ belongs to the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 1001](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L1001). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-mem).

## The extracted minimum of a d-ary heap is a lower bound

Let $h$ be a $d$-ary min-heap
over a linearly ordered type. If extracting the minimum from $h$ succeeds, returning a value $x$
and a heap $h'$, then $x \le y$ for every element $y$ of the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-le).

## Extracting the minimum preserves the arity of a d-ary heap

Let $h$ be a $d$-ary min-heap
over a linearly ordered type. If extracting the minimum from $h$ succeeds, returning a value $x$
and a heap $h'$, then $h'$ has the same arity as $h$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_arity`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 1021](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L1021). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-arity).

## Extracting the minimum leaves a heap-ordered $d$-ary heap

Let $h$ be a $d$-ary
min-heap. If extracting the minimum of $h$ returns a value $x$ and a heap $h'$ of arity $d'$,
then $d' \ge 2$ and the storage array $a$ of $h'$ is heap-ordered: for every index $i$ with
$0 < i < |a|$, the entry $a_{\lfloor (i-1)/d' \rfloor}$ is at most $a_i$.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.extractMin_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 1032](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L1032). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#extract-min-ordered).

## Size of a $d$-ary min-heap

For every $d$-ary min-heap $h$ over a linearly ordered type,
the number of elements of $h$, counted with multiplicity, equals the length of its backing
array.

Formalized by `Cslib.Algorithms.Lean.DaryMinHeap.card_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/DaryHeap.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html#card-elements).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: d-ary heap](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/d-ary-heap/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/heaps/d-ary-heap)
