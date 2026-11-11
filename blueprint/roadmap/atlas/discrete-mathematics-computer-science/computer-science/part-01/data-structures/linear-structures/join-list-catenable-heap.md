---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.CatenableHeap, Cslib.Algorithms.Lean.CatenableHeap.toListNaive, Cslib.Algorithms.Lean.CatenableHeap.toListAux, Cslib.Algorithms.Lean.CatenableHeap.toList, Cslib.Algorithms.Lean.CatenableHeap.toMultiset, Cslib.Algorithms.Lean.CatenableHeap.size, Cslib.Algorithms.Lean.CatenableHeap.toListAux_eq, Cslib.Algorithms.Lean.CatenableHeap.toList_eq_toListNaive
statement: formalized
proof: formalized
---

# Join list (catenable heap)

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html).

## Catenable heap

A catenable heap over a type $\alpha$ is a persistent unsorted heap,
represented as a join list (catenation tree): it is either the empty heap, an element of $\alpha$
added in front of a catenable heap, or the join of two catenable heaps.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#catenable-heap).

## Naive flattening of a catenable heap

The naive flattening of a catenable heap is defined
by recursion: the empty heap flattens to the empty list, the heap with an element $x$ added in
front of a heap $t$ flattens to $x$ followed by the naive flattening of $t$, and the join of
heaps $l$ and $r$ flattens to the naive flattening of $l$ followed by that of $r$.

It is the reference against which the accumulating flattening is checked.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toListNaive`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-naive).

## Accumulating flattening of a catenable heap

Given a catenable heap $h$ and a list $s$, the
accumulating flattening of $h$ onto $s$ is defined by recursion on $h$: for the empty heap it is
$s$; for the heap with an element $x$ added in front of a heap $t$ it is $x$ followed by the
accumulating flattening of $t$ onto $s$; for the join of heaps $l$ and $r$ it is the accumulating
flattening of $l$ onto the accumulating flattening of $r$ onto $s$.

Each node of $h$ is visited once.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toListAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-aux).

## Flattening of a catenable heap

The flattening of a catenable heap $h$ is the list of its
elements from left to right, computed as the accumulating flattening of $h$ onto the empty list.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list).

## Multiset of elements of a catenable heap

The multiset of elements of a catenable heap $h$
is the multiset of the entries of the left-to-right list of elements of $h$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset).

## Size of a catenable heap

The size of a catenable heap is the length of its left-to-right
list of elements, that is, the number of its elements counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size).

## Accumulator flattening of a catenable heap

For every catenable heap $h$ and list $a$,
flattening $h$ from left to right in front of the accumulator $a$ gives the naive left-to-right
flattening of $h$ followed by $a$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toListAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-aux-eq).

## Flattening of a catenable heap equals its naive flattening

For every catenable heap $h$,
the flattening of $h$ equals the naive flattening of $h$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_eq_toListNaive`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-eq-to-list-naive).

## Flattening the empty catenable heap

The flattening of the empty catenable heap is the
empty list.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-empty).

## Flattening a front node of a catenable heap

For an element $x$ and a catenable heap $t$,
the flattening of the heap with $x$ added in front of $t$ is $x$ followed by the flattening of
$t$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-cons).

## Flattening a join of catenable heaps

For catenable heaps $l$ and $r$, the flattening of
the join of $l$ and $r$ is the flattening of $l$ followed by the flattening of $r$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-join).

## The empty catenable heap has no elements

The multiset of elements of the empty catenable
heap is the empty multiset.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-empty).

## Multiset of a front node

For every element $a$ and every catenable heap $t$, the multiset
of elements of the heap obtained by adding $a$ in front of $t$ is the multiset of elements of $t$
with one more copy of $a$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-cons).

## Multiset of a join node

For all catenable heaps $L$ and $R$, the multiset of elements of
the join node with left child $L$ and right child $R$ is the multiset sum of the multisets of
elements of $L$ and $R$ (multiplicities add).

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-join).

## The empty catenable heap has size zero

The empty catenable heap has size $0$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-empty).

## Size of a heap with an element added in front

For every element $a$ and catenable heap
$t$, the size of the heap obtained by adding $a$ in front of $t$ is the size of $t$ plus one.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-cons).

## Size of a catenable heap join

For catenable heaps $\ell$ and $r$, the size of the join
node with left child $\ell$ and right child $r$ is the size of $\ell$ plus the size of $r$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-join).

## Size of a catenable heap as a multiset cardinality

For every catenable heap $h$, the size
of $h$ equals the cardinality of the multiset of its elements.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_eq_card_toMultiset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-eq-card-to-multiset).

## Creating an empty catenable heap

The operation that creates a catenable heap returns the
empty heap and charges cost $0$, since it allocates no node.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.make`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#make).

## Insertion into a catenable heap

For an element $x$ and a catenable heap $h$, inserting
$x$ into $h$ returns the heap with $x$ added in front of $h$ and charges cost $1$, for the one
front node it allocates.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#insert).

## Union of catenable heaps

The union of catenable heaps $h_1$ and $h_2$ allocates one join
node, at cost $1$, and returns that join node, whose left child is $h_1$ and whose right child is
$h_2$; neither operand is traversed or changed.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.union`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#union).

## Cost and result of creating a catenable heap

Creating a catenable heap returns the empty
heap, at cost $0$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.make_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#make-eq).

## Cost and result of insertion into a catenable heap

For every element $x$ and catenable
heap $h$, inserting $x$ into $h$ returns the heap with $x$ added in front of $h$, at cost
exactly $1$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.insert_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#insert-eq).

## Union allocates one join node

For all catenable heaps $h_1$ and $h_2$, the union of $h_1$
and $h_2$ returns the join node whose left child is $h_1$ and whose right child is $h_2$, at
cost $1$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.union_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#union-eq).

## Result of creating a catenable heap

The heap returned by the operation that creates a
catenable heap is the empty heap.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.ret_make`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#ret-make).

## Creating an empty catenable heap costs nothing

The operation that creates an empty
catenable heap has time cost $0$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.time_make`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#time-make).

## Result of insertion into a catenable heap

For every element $x$ and catenable heap $h$,
the heap returned by inserting $x$ into $h$ is the heap with $x$ added in front of $h$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.ret_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#ret-insert).

## Insertion into a catenable heap costs one

For every element $x$ and catenable heap $h$,
inserting $x$ into $h$ has time cost exactly $1$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.time_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#time-insert).

## Result of the union of catenable heaps

For all catenable heaps $h_1$ and $h_2$, the heap
returned by their union is the join of $h_1$ and $h_2$, with $h_1$ as left child and $h_2$ as
right child, both unchanged.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.ret_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#ret-union).

## Union of catenable heaps costs one

For all catenable heaps $h_1$ and $h_2$, the union of
$h_1$ and $h_2$ has time cost exactly $1$, independently of $h_1$ and $h_2$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.time_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#time-union).

## A newly created catenable heap flattens to the empty list

The flattening of the heap
returned by the operation that creates a catenable heap is the empty list.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_make`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-make).

## Flattening after insertion into a catenable heap

For an element $x$ and a catenable heap
$h$, the flattening of the heap returned by inserting $x$ into $h$ is $x$ followed by the
flattening of $h$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-insert).

## Flattening a union of catenable heaps

For catenable heaps $h_1$ and $h_2$, the flattening
of the heap returned by the union of $h_1$ and $h_2$ is the flattening of $h_1$ followed by the
flattening of $h_2$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toList_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-list-union).

## A newly made catenable heap has no elements

The multiset of elements of the heap returned
by the make operation is the empty multiset.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_make`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-make).

## Insertion adds one copy of the element

For every element $x$ and every catenable heap $h$,
the multiset of elements of the heap returned by inserting $x$ into $h$ is the multiset of
elements of $h$ with one more copy of $x$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-insert).

## Union adds the multisets of elements

For all catenable heaps $h_1$ and $h_2$, the multiset
of elements of the heap returned by the union of $h_1$ and $h_2$ is the multiset sum of the
multisets of elements of $h_1$ and $h_2$ (multiplicities add).

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.toMultiset_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#to-multiset-union).

## A newly made catenable heap has size zero

The heap returned by the operation that
creates an empty catenable heap has size $0$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_make`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-make).

## Insertion into a catenable heap increases its size by one

For every element $x$ and
catenable heap $h$, the heap returned by inserting $x$ into $h$ has size one more than the size
of $h$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-insert).

## Size of a catenable heap union

For catenable heaps $h_1$ and $h_2$, the heap returned by
the union of $h_1$ and $h_2$ has size equal to the size of $h_1$ plus the size of $h_2$.

Formalized by `Cslib.Algorithms.Lean.CatenableHeap.size_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/CatenableHeap.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html#size-union).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Join list (catenable heap)](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/join-list-catenable-heap)
