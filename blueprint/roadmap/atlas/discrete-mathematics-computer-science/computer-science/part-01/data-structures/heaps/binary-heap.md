---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.heapParent, Cslib.Algorithms.Lean.heapLeft, Cslib.Algorithms.Lean.heapRight, Cslib.Algorithms.Lean.heapParent_lt_size, Cslib.Algorithms.Lean.HeapOrdered, Cslib.Algorithms.Lean.SiftUpReady, Cslib.Algorithms.Lean.SiftDownReady, Cslib.Algorithms.Lean.smallerChild
statement: formalized
proof: formalized
---

# Binary heap

74 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html).

## Parent index in a level-order binary tree

In a binary tree stored in level order in an
array indexed from $0$, the parent index of a natural number $i$ is $\lfloor (i-1)/2 \rfloor$,
where $i - 1$ is truncated subtraction of natural numbers, so the root index $0$ is sent to $0$.

Formalized by `Cslib.Algorithms.Lean.heapParent`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#heap-parent).

## Left child index in a level-order binary tree

In a binary tree stored in level order in
an array indexed from $0$, the left child of the node at index $i$ has index $2i + 1$.

Formalized by `Cslib.Algorithms.Lean.heapLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#heap-left).

## Right child index in an array-backed binary tree

In the level-order layout of a binary
tree in an array indexed from $0$, the right child of the node at index $i$ is at index $2i + 2$.

Formalized by `Cslib.Algorithms.Lean.heapRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#heap-right).

## The parent of a valid nonroot index is valid

For an array $a$ of length $|a|$ and an index
$i$ with $0 < i < |a|$, the parent index $\lfloor (i-1)/2 \rfloor$ of $i$ is also less than
$|a|$.

Formalized by `Cslib.Algorithms.Lean.heapParent_lt_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#heap-parent-lt-size).

## Heap order on a level-order array

An array $a$ over a type with a relation $\le$, indexed
from $0$, is heap ordered when every entry other than the root is at least its parent entry:
for every index $i$ with $0 < i < |a|$, where $|a|$ is the length of $a$, we have
$a_{\lfloor (i-1)/2 \rfloor} \le a_i$.

Formalized by `Cslib.Algorithms.Lean.HeapOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#heap-ordered).

## Arrays ready for sift-up

Let $a$ be an array of length $|a|$ over a type with a relation
$\le$, indexed from $0$, and for $j > 0$ let $p(j) = \lfloor (j - 1)/2 \rfloor$ be the parent of
$j$. The array $a$ is ready for sift-up at an index $i$ when $i < |a|$, when $a_{p(j)} \le a_j$ for
every $j \ne i$ with $0 < j < |a|$, and when, if $i > 0$, also $a_{p(i)} \le a_j$ for every $j$
with $0 < j < |a|$ and $p(j) = i$.

Formalized by `Cslib.Algorithms.Lean.SiftUpReady`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up-ready).

## Sift-down precondition

For an array $a$ over a type ordered by $\le$, write
$p(j) = \lfloor (j-1)/2 \rfloor$ for the parent of index $j$. The array $a$ is ready for
sift-down at index $i$ when $i$ is a valid index of $a$; $a_{p(j)} \le a_j$ for every valid index
$j > 0$ with $p(j) \ne i$; and, if $i > 0$, $a_{p(i)} \le a_j$ for every valid index $j > 0$ with
$p(j) = i$.

Thus the only edges that may violate heap order are those leaving $i$, and moving either child
of $i$ up to position $i$ keeps the edge entering $i$ ordered.

Formalized by `Cslib.Algorithms.Lean.SiftDownReady`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-ready).

## Smaller child

Let $a$ be an array of length $|a|$ over a linearly ordered type, indexed
from $0$, and let $i$ be an index with children $\ell = 2i + 1$ and $r = 2i + 2$. If
$\ell \ge |a|$, then $i$ has no smaller child. Otherwise the smaller child of $i$ is $r$ when
$r < |a|$ and $a_r < a_\ell$, and $\ell$ in every other case, so ties go to the left child.

Formalized by `Cslib.Algorithms.Lean.smallerChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#smaller-child).

## The smaller child has a larger index

For every array $a$ over a linearly ordered type
and all indices $i$ and $c$, if $c$ is the smaller child of $i$ in $a$, then $i < c$.

Formalized by `Cslib.Algorithms.Lean.smallerChild_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#smaller-child-gt).

## The smaller child is a valid index

For every array $a$ over a linearly ordered type and
all indices $i$ and $c$, if $c$ is the smaller child of $i$ in $a$, then $c$ is less than the
length $|a|$ of $a$.

Formalized by `Cslib.Algorithms.Lean.smallerChild_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#smaller-child-valid).

## Sift-up

Given an array $a$ of length $|a|$ over a linearly ordered type, indexed from $0$,
and an index $i$, the sift-up of $a$ from $i$ is defined by recursion on $i$. If $i = 0$ or
$i \ge |a|$, the result is $a$. Otherwise let $p = \lfloor (i - 1)/2 \rfloor$ be the parent of
$i$; if $a_i < a_p$, the result is the sift-up from $p$ of the array obtained from $a$ by
exchanging the entries at positions $i$ and $p$, and otherwise the result is $a$.

Formalized by `Cslib.Algorithms.Lean.siftUp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up).

## Sift-down

Sifting down an array $a$ over a linearly ordered type from index $i$ works as
follows. If $i$ has a child in $a$, that is, if $2i+1$ is a valid index, let $c$ be the child of
$i$ (among $2i+1$ and $2i+2$, if valid) holding the smaller value, preferring the left child
$2i+1$ on ties. If $a_c < a_i$, swap the entries at $i$ and $c$ and continue sifting down from
$c$; otherwise, or if $i$ has no child, return the array unchanged.

Formalized by `Cslib.Algorithms.Lean.siftDown`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down).

## Sift-up permutes the array

For every array $a$ over a linearly ordered type and every
index $i$, the array obtained by sifting up $a$ from $i$ is a permutation of $a$.

Formalized by `Cslib.Algorithms.Lean.siftUp_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up-perm).

## Binary-heap sift-down permutes the array

For every array $a$ over a linearly ordered
type and every index $i$, the array obtained by sifting down $a$ from $i$ is a permutation of
$a$.

Formalized by `Cslib.Algorithms.Lean.siftDown_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-perm).

## Binary-heap sift-up preserves the multiset of entries

For every array $a$ over a
linearly ordered type and every index $i$, the array obtained by sifting up $a$ from $i$ has the
same multiset of entries as $a$.

Formalized by `Cslib.Algorithms.Lean.siftUp_multiset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up-multiset).

## Binary-heap sift-down preserves the multiset of entries

For every array $a$ over a
linearly ordered type and every index $i$, the array obtained by sifting down $a$ from $i$ has
the same multiset of entries as $a$.

Formalized by `Cslib.Algorithms.Lean.siftDown_multiset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-multiset).

## The root of a heap-ordered binary-heap array is minimal

If an array $a$ over a linearly
ordered type is heap-ordered, then $a_0 \le a_i$ for every valid index $i$ of $a$.

Formalized by `Cslib.Algorithms.Lean.HeapOrdered.root_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#root-le).

## Sift-up restores heap order

Let $a$ be an array over a linearly ordered type and let
$i$ be an index such that $a$ is ready for sift-up at $i$. Then the array obtained by sifting
up $a$ from $i$ is heap ordered.

Formalized by `Cslib.Algorithms.Lean.siftUp_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up-ordered).

## Sift-down restores heap order

Let $a$ be an array over a linearly ordered type that
satisfies the sift-down precondition at a valid index $i$: the only edges that may violate heap
order are those leaving $i$, and moving either child of $i$ up to position $i$ keeps the edge
entering $i$ ordered. Then the array obtained by sifting down $a$ from $i$ is heap-ordered.

Formalized by `Cslib.Algorithms.Lean.siftDown_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-ordered).

## Appending to a heap-ordered array prepares it for sift-up

If an array $a$ of length $n$
over a linearly ordered type is heap-ordered and $x$ is any value, then the array obtained by
appending $x$ to $a$ satisfies the sift-up precondition at index $n$, the position of $x$: the
only edge that may violate heap order is the one entering index $n$.

Formalized by `Cslib.Algorithms.Lean.push_siftUpReady`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#push-sift-up-ready).

## Binary min-heap

A binary min-heap over a linearly ordered type $\alpha$ is an array $a$
of elements of $\alpha$ (its level-order storage), of length $|a|$ and with entries
$a_0, \dots, a_{|a|-1}$, that is heap ordered: for every index $i$ with $0 < i < |a|$, the entry
$a_{\lfloor (i - 1)/2 \rfloor}$ at the parent index of $i$ is at most $a_i$.

Formalized by `Cslib.Algorithms.Lean.MinHeap`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min-heap).

## Elements of a binary min-heap

The multiset of elements of a binary min-heap is the
multiset of the entries of its level-order storage array, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.MinHeap.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#elements).

## Empty binary min-heap

The empty binary min-heap is the min-heap whose level-order storage
array has no entries.

Formalized by `Cslib.Algorithms.Lean.MinHeap.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#empty).

## Insertion into a binary min-heap

To insert a value $x$ into a binary min-heap $h$, append
$x$ at the end of the level-order array of $h$ and sift it up from its index (the old length of
the array), repeatedly swapping it with its parent while it is smaller. The result is again a
binary min-heap.

Formalized by `Cslib.Algorithms.Lean.MinHeap.push`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#push).

## Minimum lookup in a binary heap

For a binary min-heap $h$, the minimum lookup returns the
entry at index $0$ (the root) of the storage array of $h$ when that array is nonempty, and returns
no value when it is empty.

Formalized by `Cslib.Algorithms.Lean.MinHeap.min?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min).

## Binary heap minimum lookup fails exactly when empty

For a binary min-heap $h$ over a
linearly ordered type, looking up the minimum of $h$ returns no value if and only if the storage
array of $h$ has size $0$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.min?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min-eq-none-iff).

## Binary heap minimum lookup succeeds exactly when nonempty

For a binary min-heap $h$ over
a linearly ordered type, looking up the minimum of $h$ returns a value if and only if the storage
array of $h$ has positive size.

Formalized by `Cslib.Algorithms.Lean.MinHeap.min?_isSome_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min-is-some-iff).

## The binary heap minimum lookup returns a stored element

Let $h$ be a binary min-heap
over a linearly ordered type. If looking up the minimum of $h$ returns $x$, then $x$ belongs to
the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.min?_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min-mem).

## The binary heap minimum lookup is a lower bound

Let $h$ be a binary min-heap over a
linearly ordered type. If looking up the minimum of $h$ returns $x$, then $x \le y$ for every
element $y$ of the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.min?_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#min-le).

## Elements after binary heap insertion

Let $h$ be a binary min-heap over a linearly ordered
type and $x$ a value. The multiset of elements of the heap obtained by inserting $x$ into $h$ is
the multiset of elements of $h$ with one more copy of $x$ added.

Formalized by `Cslib.Algorithms.Lean.MinHeap.elements_push`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#elements-push).

## Binary heap insertion adds one copy of the inserted value

Let $h$ be a binary min-heap
over a linearly ordered type and $x$ a value. The multiplicity of $x$ in the multiset of elements
of the heap obtained by inserting $x$ into $h$ is one more than its multiplicity in the multiset
of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.count_push_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#count-push-self).

## Binary heap insertion leaves other multiplicities unchanged

Let $h$ be a binary min-heap
over a linearly ordered type, and let $x \ne y$ be values. Then $y$ occurs in the multiset of
elements of the heap obtained by inserting $x$ into $h$ exactly as many times as it occurs in the
multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.count_push_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#count-push-of-ne).

## Insertion into a binary min-heap preserves heap order

For every binary min-heap $h$
over a linearly ordered type and every value $x$, the level-order array of the heap obtained
by inserting $x$ into $h$ is heap-ordered: the entry at every nonroot index $i$ is at least
the entry at its parent index $\lfloor (i-1)/2 \rfloor$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.push_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 618](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#push-ordered).

## Moving the last entry to the root

For a nonempty array $a$ of length $n$, this operation
swaps the entries at indices $0$ and $n - 1$ and then deletes the final entry. The result has
length $n - 1$; when $n \ge 2$ its entry at index $0$ is $a_{n-1}$ and its entry at each index
$0 < i < n - 1$ is $a_i$.

Formalized by `Cslib.Algorithms.Lean.moveLastToRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#move-last-to-root).

## Moving the last entry to the root prepares a sift-down

Let $a$ be a heap-ordered array
over a linearly ordered type with at least two entries, and let $b$ be the array obtained from $a$
by moving its last entry to the root. Then $b$ is ready for sifting down at index $0$: index $0$ is
valid in $b$, and for every index $j > 0$ of $b$ whose parent index $\lfloor (j - 1)/2 \rfloor$ is
not $0$, the entry of $b$ at the parent index is at most $b_j$.

Formalized by `Cslib.Algorithms.Lean.moveLastToRoot_siftDownReady`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#move-last-to-root-sift-down-ready).

## Moving the last entry to the root removes the old root

For a nonempty array $a$ over a
linearly ordered type, the multiset of entries of the array obtained from $a$ by moving its last
entry to the root equals the multiset of entries of $a$ with one occurrence of $a_0$ removed.

Formalized by `Cslib.Algorithms.Lean.moveLastToRoot_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#move-last-to-root-elements).

## Removing the root of a nonempty binary min-heap

Let $h$ be a binary min-heap over a
linearly ordered type whose level-order array is nonempty. If the array has exactly one entry,
the result is the empty heap. Otherwise the last entry of the array replaces the root, the array
shrinks by one, and the result is the heap obtained by sifting this entry down from the root.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractTail`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-tail).

## Extracting the minimum of a binary min-heap

For a binary min-heap $h$ over a linearly
ordered type, extraction returns nothing when the level-order array of $h$ is empty. Otherwise it
returns the root entry (the first entry of the array) together with the heap obtained from $h$ by
removing its root and restoring heap order.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min).

## Extraction from a binary min-heap fails exactly when it is empty

For a binary min-heap
$h$ over a linearly ordered type, extracting the minimum of $h$ returns no result if and only if
the level-order storage array of $h$ has size $0$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-eq-none-iff).

## The value extracted from a binary min-heap is one of its elements

Let $h$ be a binary
min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds and returns a
value $x$ together with a heap $r$, then $x$ belongs to the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-mem).

## The value extracted from a binary min-heap is minimal

Let $h$ be a binary min-heap over
a linearly ordered type. If extracting the minimum from $h$ succeeds and returns a value $x$
together with a heap $r$, then $x \le y$ for every value $y$ in the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 771](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-le).

## Elements after binary heap extraction

Let $h$ be a binary min-heap over a linearly ordered
type. If extracting the minimum of $h$ succeeds and returns the value $x$ and the heap $h'$, then
the multiset of elements of $h'$ is obtained from the multiset of elements of $h$ by erasing one
occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 784](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L784). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-elements).

## Binary heap extraction splits off the minimum

Let $h$ be a binary min-heap over a linearly
ordered type. If extracting the minimum of $h$ succeeds and returns the value $x$ and the heap
$h'$, then the multiset of elements of $h$ equals the multiset of elements of $h'$ with one copy
of $x$ added.

The statement is phrased by adding $x$ back, not by erasing it from the multiset of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_cons_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 797](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L797). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-cons-elements).

## Binary heap extraction removes one copy of the minimum

Let $h$ be a binary min-heap over
a linearly ordered type. If extracting the minimum of $h$ succeeds and returns the value $x$ and
the heap $h'$, then the multiplicity of $x$ in the multiset of elements of $h'$ is its
multiplicity in the multiset of elements of $h$ minus one.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_count`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-count).

## Binary heap extraction leaves other multiplicities unchanged

Let $h$ be a binary min-heap
over a linearly ordered type. If extracting the minimum of $h$ succeeds and returns the value $x$
and the heap $h'$, then every value $y \ne x$ occurs in the multiset of elements of $h'$ exactly
as many times as in the multiset of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_count_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 819](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L819). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-count-of-ne).

## Membership after extraction from a binary min-heap

Let $h$ be a binary min-heap over a
linearly ordered type, and suppose extracting the minimum from $h$ succeeds and returns a value
$x$ together with a heap $r$. Then every value $y \ne x$ is an element of $r$ if and only if it
is an element of $h$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_mem_of_ne_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-mem-of-ne-iff).

## Extraction from a binary min-heap leaves a heap-ordered array

Let $h$ be a binary
min-heap over a linearly ordered type. If extracting the minimum from $h$ succeeds and returns a
value $x$ together with a heap $r$, then the level-order array of $r$ is heap ordered: every
entry other than the root is at least its parent entry.

Formalized by `Cslib.Algorithms.Lean.MinHeap.extractMin_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#extract-min-ordered).

## The heap parent is one level up

For every natural number $i > 0$, the parent index
$p = \lfloor (i-1)/2 \rfloor$ satisfies
$\lfloor \log_2(p+1) \rfloor + 1 = \lfloor \log_2(i+1) \rfloor$; that is, in the level-order
binary tree the parent of a nonroot index lies one level above it.

Formalized by `Cslib.Algorithms.Lean.log2_heapParent_add_one`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#log2-heap-parent-add-one).

## Sift-up with comparison and swap counts

Given an array $a$ of length $|a|$ over a
linearly ordered type and an index $i$, this computes the sift-up of $a$ at $i$ together
with a cost $(c, s) \in \mathbb{N} \times \mathbb{N}$, where $c$ counts value comparisons
and $s$ counts swaps. If $i \ge |a|$ or $i = 0$, the result is $a$ with cost $(0, 0)$.
Otherwise let $p = \lfloor (i - 1)/2 \rfloor$ be the parent of $i$. If $a_i < a_p$, the
result is this sift-up at $p$ of the array obtained from $a$ by exchanging the entries at
positions $i$ and $p$, with cost $(1, 1)$ plus the cost of that recursive sift-up;
otherwise the result is $a$ with cost $(1, 0)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.siftUp`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-up-2).

## Counting does not change the result of sift-up

For every array $a$ over a linearly
ordered type and every natural number $i$, the array returned by sift-up with comparison and
swap counts on $a$ at index $i$ equals the array returned by the plain sift-up of $a$ at $i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_siftUp`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#ret-sift-up).

## Comparison bound for sift-up

For every array $a$ over a linearly ordered type and
every natural number $i$, the number of value comparisons counted by sift-up with comparison
and swap counts on $a$ at index $i$ is at most $\lfloor \log_2(i+1) \rfloor$, the depth of
index $i$ in the level-order binary tree.

Formalized by `Cslib.Algorithms.Lean.TimeM.comparisons_siftUp_le_log2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#comparisons-sift-up-le-log2).

## Swap bound for sift-up

For every array $a$ over a linearly ordered type and every
natural number $i$, the number of swaps counted by sift-up with comparison and swap counts
on $a$ at index $i$ is at most $\lfloor \log_2(i+1) \rfloor$, the depth of index $i$ in the
level-order binary tree.

Formalized by `Cslib.Algorithms.Lean.TimeM.swaps_siftUp_le_log2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#swaps-sift-up-le-log2).

## Combined comparison and swap bound for sift-up

For every array $a$ over a linearly
ordered type and every natural number $i$, if sift-up with comparison and swap counts on $a$
at index $i$ counts $c$ comparisons and $s$ swaps, then
$c + s \le 2 \lfloor \log_2(i+1) \rfloor$.

Formalized by `Cslib.Algorithms.Lean.TimeM.events_siftUp_le_log2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#events-sift-up-le-log2).

## Sift-up at the root costs nothing

For every array $a$ over a linearly ordered type,
sift-up with comparison and swap counts on $a$ at index $0$ has cost $(0, 0)$: it counts no
comparisons and no swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_siftUp_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-sift-up-zero).

## Sift-up at an out-of-range index costs nothing

For every array $a$ of length $|a|$
over a linearly ordered type and every natural number $i$ with $i \ge |a|$, sift-up with
comparison and swap counts on $a$ at index $i$ has cost $(0, 0)$: it counts no comparisons
and no swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_siftUp_of_size_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/Cost.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-sift-up-of-size-le).

## Decrease-key in a binary min-heap

Given a binary min-heap $h$ over a linearly ordered
type, with level-order array $a$, an index $i < |a|$ and a value $x \le a_i$, decrease-key returns
the heap whose array is obtained from $a$ by replacing the entry at position $i$ with $x$ and then
sifting position $i$ up, repeatedly swapping the entry with its parent while it is strictly
smaller than the parent.

Formalized by `Cslib.Algorithms.Lean.MinHeap.decreaseKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#decrease-key).

## Array of a binary heap after decrease-key

Let $h$ be a binary min-heap over a linearly
ordered type, with level-order array $a$, let $i < |a|$ and let $x \le a_i$. The array of the heap
obtained by decreasing the key at position $i$ to $x$ equals the result of sifting up position $i$
in the array obtained from $a$ by replacing its entry at position $i$ with $x$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.decreaseKey_data`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#decrease-key-data).

## Decrease-key yields a heap-ordered array

Let $h$ be a binary min-heap over a linearly
ordered type, with level-order array $a$, let $i < |a|$ and let $x \le a_i$. The array of the heap
obtained by decreasing the key at position $i$ to $x$ is heap-ordered: the entry at every nonroot
position is at least the entry at its parent position.

Formalized by `Cslib.Algorithms.Lean.MinHeap.decreaseKey_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#decrease-key-ordered).

## Decrease-key preserves the heap size

Let $h$ be a binary min-heap over a linearly ordered
type, with level-order array $a$, let $i < |a|$ and let $x \le a_i$. The array of the heap obtained
by decreasing the key at position $i$ to $x$ has the same length as $a$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.decreaseKey_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#decrease-key-size).

## Multiset of a binary heap after decrease-key

Let $h$ be a binary min-heap over a
linearly ordered type, with level-order array $a$, let $i < |a|$ and let $x \le a_i$. The
multiset of elements of the heap obtained by decreasing the key at position $i$ to $x$ is
obtained from the multiset of elements of $h$ by removing one occurrence of $a_i$ and adding one
occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.MinHeap.decreaseKey_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/DecreaseKey.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#decrease-key-elements).

## The smaller child lies one level below its parent

Let $a$ be an array over a linearly
ordered type and let $i$ and $c$ be natural numbers. If $c$ is the smaller child of $i$ in $a$,
then $\lfloor \log_2 (c+1) \rfloor = \lfloor \log_2 (i+1) \rfloor + 1$; that is, in the
level-order binary tree stored in $a$, the node $c$ lies exactly one level below $i$.

Formalized by `Cslib.Algorithms.Lean.log2_smallerChild_add_one`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#log2-smaller-child-add-one).

## The smaller child's level is bounded by the array size

Let $a$ be an array over a
linearly ordered type, of size $|a|$, and let $i$ and $c$ be natural numbers. If $c$ is the
smaller child of $i$ in $a$, then $\lfloor \log_2 (c+1) \rfloor \le \lfloor \log_2 |a| \rfloor$.

Formalized by `Cslib.Algorithms.Lean.log2_smallerChild_le_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#log2-smaller-child-le-size).

## Timed smaller-child selection

Let $a$ be an array over a linearly ordered type and $i$
an index, with left child $2i + 1$ and right child $2i + 2$; cost is counted as the pair
(value comparisons, array swaps). If both children are valid indices of $a$, the selection costs
$(1, 0)$ and returns the right child when its value is strictly less than the value at the left
child, and the left child otherwise. If only the left child is a valid index, it returns the
left child at cost $(0, 0)$. If the left child is not a valid index, it returns no child at cost
$(0, 0)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.timedSmallerChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#timed-smaller-child).

## Timed child selection returns the smaller child

For every array $a$ over a linearly
ordered type and every index $i$, the value returned by timed child selection at $i$, with its
cost discarded, is the smaller child of $i$ in $a$ (an optional index, absent when $i$ has no
valid child).

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_timedSmallerChild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#ret-timed-smaller-child).

## Sift-down with comparison and swap counts

For an array $a$ over a linearly ordered
type and an index $i$, timed sift-down returns an array together with a cost pair
(value comparisons, array swaps), where costs add componentwise. If the left child index
$2i+1$ is not a valid index of $a$, it returns $a$ at cost $(0, 0)$. Otherwise let $c$ be the
smaller child of $i$: the left child $2i+1$, unless the right child $2i+2$ is a valid index
and $a_{2i+2} < a_{2i+1}$, in which case $c = 2i+2$. Selecting $c$ costs one comparison when
$2i+2$ is a valid index and nothing otherwise. Comparing $a_c$ with $a_i$ costs one more
comparison. If $a_c < a_i$, the entries at $i$ and $c$ are swapped at the cost of one swap,
and the result and remaining cost are those of timed sift-down from $c$ in the swapped array;
otherwise the result is $a$.

Index arithmetic, bounds checks, pattern matching and recursive calls are free.

Formalized by `Cslib.Algorithms.Lean.TimeM.siftDown`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-2).

## Timed sift-down returns the sift-down result

For every array $a$ over a linearly
ordered type and every index $i$, the array returned by timed sift-down from $i$, with its
cost discarded, equals the array returned by sift-down from $i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_siftDown`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#ret-sift-down).

## Cost of child selection

Let $a$ be an array over a linearly ordered type and $i$ an
index, and count cost as the pair (value comparisons, array swaps). The timed child selection at
$i$ in $a$ has cost $(1, 0)$ if the right child index $2i + 2$ is less than the size of $a$, and
cost $(0, 0)$ otherwise.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_timedSmallerChild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-timed-smaller-child).

## Child selection at a node without children costs nothing

Let $a$ be an array over a
linearly ordered type and $i$ an index. If the smaller-child selection at $i$ in $a$ returns no
child, then the timed child selection at $i$, with cost counted as the pair (value comparisons,
array swaps), has cost $(0, 0)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_timedSmallerChild_of_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-timed-smaller-child-of-none).

## Sift-down performs at most one swap per remaining level

Write $|a|$ for the size of an
array $a$, and let $\ell(n) = \lfloor \log_2 n \rfloor$ for $n \ge 1$ and $\ell(0) = 0$. For
every array $a$ over a linearly ordered type and every index $i$, the number of array swaps
counted by timed sift-down from $i$ is at most $\max(0, \ell(|a|) - \ell(i+1))$.

Formalized by `Cslib.Algorithms.Lean.TimeM.siftDown_swaps_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-swaps-le).

## Sift-down makes at most two comparisons per remaining level

Write $|a|$ for the size
of an array $a$, and let $\ell(n) = \lfloor \log_2 n \rfloor$ for $n \ge 1$ and $\ell(0) = 0$.
For every array $a$ over a linearly ordered type and every index $i$, the number of value
comparisons counted by timed sift-down from $i$ is at most $2 \max(0, \ell(|a|) - \ell(i+1))$.

Formalized by `Cslib.Algorithms.Lean.TimeM.siftDown_comparisons_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-comparisons-le).

## Total sift-down cost is at most three per remaining level

Write $|a|$ for the size of
an array $a$, and let $\ell(n) = \lfloor \log_2 n \rfloor$ for $n \ge 1$ and $\ell(0) = 0$.
For every array $a$ over a linearly ordered type and every index $i$, the number of value
comparisons plus the number of array swaps counted by timed sift-down from $i$ is at most
$3 \max(0, \ell(|a|) - \ell(i+1))$.

Formalized by `Cslib.Algorithms.Lean.TimeM.siftDown_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#sift-down-time-le).

## Sift-down from a node without children costs nothing

Let $a$ be an array over a
linearly ordered type and $i$ an index. If the smaller-child selection at $i$ in $a$ returns no
child, then sift-down from $i$, with cost counted as the pair (value comparisons, array swaps),
has cost $(0, 0)$: it makes no value comparisons and no array swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_siftDown_of_smallerChild_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-sift-down-of-smaller-child-none).

## Sift-down from a leaf costs nothing

Let $a$ be an array over a linearly ordered type,
of size $|a|$, and let $i$ be an index with $|a| \le 2i+1$, so that the left child of $i$ is not
a valid index (this includes invalid indices $i$). Then timed sift-down from $i$ has cost pair
$(0, 0)$: it counts no comparisons and no swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_siftDown_of_heapLeft_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-sift-down-of-heap-left-ge).

## Sift-down from an invalid index costs nothing

Let $a$ be an array over a linearly
ordered type, of size $|a|$, and let $i$ be a natural number with $|a| \le i$. Then timed
sift-down from $i$ has cost pair $(0, 0)$: it counts no comparisons and no swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.time_siftDown_of_size_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryHeap/SiftDownCost.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html#time-sift-down-of-size-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary heap](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binary-heap/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/heaps/binary-heap)
