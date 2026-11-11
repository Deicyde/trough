---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.DoublyLinkedList.Node, Cslib.Algorithms.Lean.DoublyLinkedList.Represents, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_head, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_time, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_ret, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_get, Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_frame
statement: formalized
proof: formalized
---

# Doubly linked list

62 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html).

## Doubly linked list node

A doubly linked list node with payloads in $\alpha$ and identities
in $\iota$ consists of a payload in $\alpha$ (the key together with any satellite data), a next
pointer and a previous pointer, each of which is either an identity in $\iota$ or NIL.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.Node`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#node).

## Store representing a doubly linked list

Let a store assign to each identity below $n$
either nothing or a doubly linked list node whose pointers are identities below $n$ or NIL, and
let the head be an identity below $n$ or NIL. The store and head represent the list of identities
$i_0, \dots, i_{k-1}$ when these identities are pairwise distinct, the head is $i_0$ (and NIL
when $k = 0$), and for each $j < k$ the store entry at $i_j$ is a node whose previous pointer is
NIL if $j = 0$ and $i_{j-1}$ otherwise, and whose next pointer is $i_{j+1}$ if $j + 1 < k$ and
NIL otherwise.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.Represents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#represents).

## Prepending a node to a doubly linked list

Let a store assign to each identity below $n$
either nothing or a doubly linked list node whose pointers are identities below $n$ or NIL, let
the head be an identity below $n$ or NIL, and let $x$ be an identity whose store entry is a node,
where the store entry of the head is also a node when the head is not NIL. The procedure sets the
next pointer of $x$ to the head, then sets the previous pointer of $x$ to NIL, then tests whether
the head is NIL; if it is not, it sets the previous pointer of the node at the head (read after
the two writes at $x$) to $x$. Finally it makes $x$ the new head and returns the updated store
together with the head $x$. One time unit is charged for each pointer assignment and for the NIL
test, so the cost is $4$ when the head is NIL and $5$ otherwise.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend).

## Prepending makes the supplied node the head

Fix a capacity $n$ and let $s$ be a store
assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Then the head returned by List Prepend on $s$,
$\mathrm{head}$ and $x$ is $x$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_head`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-head).

## Exact cost of doubly linked list prepend

Let a store assign to each identity below $n$
either nothing or a doubly linked list node, let the head be an identity below $n$ or NIL, and let
$x$ be an identity whose store entry is a node, where the store entry of the head is also a node
when the head is not NIL. Then prepending $x$ costs exactly $5$ time units if the head is not NIL
and exactly $4$ if it is NIL, counting one unit per pointer assignment and per NIL test of the
old head.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-time).

## Result of doubly-linked list prepend

Fix a capacity $n$ and let $s$ be a store assigning to
each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an identity, and let
$x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an identity,
$s(\mathrm{head})$ is a node. Let $u$ be $s$ with the cell at $x$ replaced by the node $s(x)$ with
next pointer $\mathrm{head}$ and previous pointer NIL. Then List Prepend on $s$, $\mathrm{head}$ and
$x$ returns the head $x$ together with the store $u$ when $\mathrm{head}$ is NIL, and, when
$\mathrm{head}$ is an identity $h$, together with the store obtained from $u$ by replacing its cell
at $h$ with the node $u(h)$ with previous pointer $x$ (leaving the cell empty if $u(h)$ is
nothing).

This holds also when $h = x$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-ret).

## Cells after doubly-linked list prepend

Fix a capacity $n$ and let $s$ be a store assigning
to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an identity, and
let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an identity,
$s(\mathrm{head})$ is a node. Let $s'$ be the store returned by List Prepend on $s$, $\mathrm{head}$
and $x$. For every identity $z$, let $c$ be the node $s(x)$ with next pointer $\mathrm{head}$ and
previous pointer NIL if $z = x$, and $c = s(z)$ otherwise. Then $s'(z)$ is $c$ with previous pointer
$x$ (nothing, if $c$ is nothing) when $\mathrm{head} = z$, and $s'(z) = c$ otherwise.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-get).

## Doubly-linked list prepend leaves other cells unchanged

Fix a capacity $n$ and let $s$ be a
store assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Let $s'$ be the store returned by List Prepend on $s$,
$\mathrm{head}$ and $x$. Then $s'(z) = s(z)$ for every identity $z$ with $z \ne x$ and
$\mathrm{head} \ne z$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-frame).

## Doubly-linked list prepend preserves allocation

Fix a capacity $n$ and let $s$ be a store
assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Let $s'$ be the store returned by List Prepend on $s$,
$\mathrm{head}$ and $x$. Then for every identity $z$, $s'(z)$ is a node if and only if $s(z)$ is a
node.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-allocated).

## Doubly-linked list prepend preserves payloads

Fix a capacity $n$ and let $s$ be a store
assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Let $s'$ be the store returned by List Prepend on $s$,
$\mathrm{head}$ and $x$. Then for every identity $z$, either $s(z)$ and $s'(z)$ are both nothing, or
both are nodes with the same payload.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-payload).

## Pointers of the node prepended to a doubly-linked list

Fix a capacity $n$ and let $s$ be a
store assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Suppose moreover that $\mathrm{head}$ is not $x$ (it may be
NIL). Let $s'$ be the store returned by List Prepend on $s$, $\mathrm{head}$ and $x$. Then $s'(x)$
is the node $s(x)$ with next pointer $\mathrm{head}$ and previous pointer NIL.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-node).

## Old head after doubly-linked list prepend

Fix a capacity $n$ and let $s$ be a store
assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Suppose moreover that $\mathrm{head}$ is an identity $h$
with $h \ne x$. Let $s'$ be the store returned by List Prepend on $s$, $\mathrm{head}$ and $x$.
Then $s'(h)$ is the node $s(h)$ with previous pointer $x$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_oldHead`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-old-head).

## Correctness of doubly-linked list prepend

Fix a capacity $n$ and let $s$ be a store
assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Suppose moreover that $s$ with head $\mathrm{head}$
represents a list $L = (\ell_1, \dots, \ell_k)$ of identities, that is, the $\ell_i$ are distinct,
$\mathrm{head}$ is $\ell_1$ (NIL if $k = 0$), and each $s(\ell_i)$ is a node with previous pointer
$\ell_{i-1}$ and next pointer $\ell_{i+1}$ (NIL past the ends of $L$), and that $x$ is not in $L$.
Let $s'$ and $h'$ be the store and head returned by List Prepend on $s$, $\mathrm{head}$ and $x$.
Then $s'$ with head $h'$ represents the list $(x, \ell_1, \dots, \ell_k)$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-represents).

## Doubly-linked list prepend preserves disjoint lists

Fix a capacity $n$ and let $s$ be a
store assigning to each identity $i < n$ either a node or nothing, let $\mathrm{head}$ be NIL or an
identity, and let $x$ be an identity such that $s(x)$ is a node and, when $\mathrm{head}$ is an
identity, $s(\mathrm{head})$ is a node. Suppose moreover that $s$ with some head $o$ represents a
list $L = (\ell_1, \dots, \ell_k)$ of identities, that is, the $\ell_i$ are distinct, $o$ is
$\ell_1$ (NIL if $k = 0$), and each $s(\ell_i)$ is a node with previous pointer $\ell_{i-1}$ and
next pointer $\ell_{i+1}$ (NIL past the ends of $L$), that $x$ is not in $L$, and that
$\mathrm{head}$ is NIL or an identity not in $L$. Let $s'$ be the store returned by List Prepend on
$s$, $\mathrm{head}$ and $x$. Then $s'$ with head $o$ also represents $L$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_disjoint_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-disjoint-represents).

## Uniform cost bound for doubly linked list prepend

Let a store assign to each identity
below $n$ either nothing or a doubly linked list node, let the head be an identity below $n$ or
NIL, and let $x$ be an identity whose store entry is a node, where the store entry of the head is
also a node when the head is not NIL. Then prepending $x$ costs at most $5$ time units, counting
one unit per pointer assignment and per NIL test of the old head.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listPrepend_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Basic.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-prepend-time-le).

## Deletion from a doubly linked list

Let the store be an array of cells, each either empty
or holding a node with a payload and optional next and previous pointers to cells, let $h$ be
the optional head pointer, and let $x$ be a cell holding a node such that each cell named by its
previous or next pointer also holds a node. Following CLRS `LIST-DELETE`, deleting $x$ returns a
new store and head as follows. If the node at $x$ has a previous pointer $p$, the next pointer of
the node at $p$ is set to the next pointer of $x$ and the head stays $h$; otherwise the head
becomes the next pointer of $x$. Then, if the node at $x$ has a next pointer $s$, the previous
pointer of the node at $s$ in the store from the first step is set to the previous pointer of $x$.
The computation is charged one unit for each of the two NIL tests and one unit for each executed
pointer or head assignment, so three or four units in total.

The record stored at $x$ is kept and no cell is freed; list consistency is needed only for
correctness, not to run the procedure.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete).

## Running time of doubly linked list deletion

Let the store be an array of cells, each
either empty or holding a node with optional next and previous pointers, let $h$ be the optional
head pointer, and let $x$ be a cell holding a node such that each cell named by its previous or
next pointer also holds a node. Counting one unit per NIL test and per executed pointer or head
assignment, deleting $x$ from the list with head $h$ costs exactly $4$ units if the node at $x$
has a next pointer, and exactly $3$ units otherwise.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-time).

## Header after doubly linked list deletion

Let $S$ be a store of $n$ cells, each empty or
holding a node (a payload with next and previous pointers, each an index or NIL), let $h$ be a
header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a node
$X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor $X.\mathrm{next}$
hold nodes whenever these pointers are not NIL. Let $h'$ be the header returned by List Delete on
$S$, $h$ and $x$. Then $h' = h$ if $X.\mathrm{prev}$ is not NIL, and $h' = X.\mathrm{next}$ if
$X.\mathrm{prev}$ is NIL.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_head`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-head).

## Result of doubly linked list deletion

Let $S$ be a store of $n$ cells, each empty or
holding a node (a payload with next and previous pointers, each an index or NIL), let $h$ be a
header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a node
$X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor $X.\mathrm{next}$
hold nodes whenever these pointers are not NIL. Let $T$ be $S$ if $X.\mathrm{prev}$ is NIL, and
otherwise $S$ with the next pointer of the node in cell $X.\mathrm{prev}$ set to
$X.\mathrm{next}$. Then List Delete on $S$, $h$ and $x$ returns the store equal to $T$ if
$X.\mathrm{next}$ is NIL, and otherwise to $T$ with the previous pointer of the node in cell
$X.\mathrm{next}$ of $T$ set to $X.\mathrm{prev}$, together with the header $h$ if
$X.\mathrm{prev}$ is not NIL and $X.\mathrm{next}$ if it is NIL. The successor's node is read
from $T$, so when $X.\mathrm{prev}$ and $X.\mathrm{next}$ are the same index (not NIL), both
pointer updates apply to its node.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-ret).

## Cellwise result of doubly linked list deletion

Let $S$ be a store of $n$ cells, each
empty or holding a node (a payload with next and previous pointers, each an index or NIL), let $h$
be a header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a
node $X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor
$X.\mathrm{next}$ hold nodes whenever these pointers are not NIL. Let $S'$ be the store returned
by List Delete on $S$, $h$ and $x$. For an index $z$, let $C$ be the cell $S(z)$ with the next
pointer of its node set to $X.\mathrm{next}$ if $X.\mathrm{prev} = z$, and $C = S(z)$ otherwise.
Then $S'(z)$ is $C$ with the previous pointer of its node set to $X.\mathrm{prev}$ if
$X.\mathrm{next} = z$, and $S'(z) = C$ otherwise; an empty cell stays empty. So the write at the
predecessor is applied before the write at the successor.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-get).

## Deletion changes only the cells of the neighbors

Let $S$ be a store of $n$ cells, each
empty or holding a node (a payload with next and previous pointers, each an index or NIL), let $h$
be a header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a
node $X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor
$X.\mathrm{next}$ hold nodes whenever these pointers are not NIL. Let $S'$ be the store returned
by List Delete on $S$, $h$ and $x$. Then $S'(z) = S(z)$ for every index $z$ with
$X.\mathrm{prev} \ne z$ and $X.\mathrm{next} \ne z$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-frame).

## Deletion from a doubly linked list allocates and frees nothing

Let $S$ be a store of $n$
cells, each empty or holding a node (a payload with next and previous pointers, each an index or
NIL), let $h$ be a header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose
cell holds a node $X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor
$X.\mathrm{next}$ hold nodes whenever these pointers are not NIL. Let $S'$ be the store returned
by List Delete on $S$, $h$ and $x$. Then for every index $z$, the cell $S'(z)$ holds a node if and
only if $S(z)$ does.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-allocated).

## Deletion preserves payloads

Let $S$ be a store of $n$ cells, each empty or holding a node
(a payload with next and previous pointers, each an index or NIL), let $h$ be a header (an index
in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a node $X$ such that the
cells at the predecessor $X.\mathrm{prev}$ and the successor $X.\mathrm{next}$ hold nodes
whenever these pointers are not NIL. Let $S'$ be the store returned by List Delete on $S$, $h$
and $x$. Then for every index $z$, either $S'(z)$ and $S(z)$ are both empty, or both hold nodes
and these two nodes have the same payload.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-payload).

## The deleted node keeps its record

Let $S$ be a store of $n$ cells, each empty or holding
a node (a payload with next and previous pointers, each an index or NIL), let $h$ be a header (an
index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a node $X$ such that
the cells at the predecessor $X.\mathrm{prev}$ and the successor $X.\mathrm{next}$ hold nodes
whenever these pointers are not NIL. Let $S'$ be the store returned by List Delete on $S$, $h$
and $x$. Then $S'(x) = S(x)$: the deleted node stays allocated with its payload and both of its
pointers unchanged.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_deleted_record`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-deleted-record).

## Deletion preserves lists avoiding the deleted node's neighbors

Let $S$ be a store of $n$
cells, each empty or holding a node (a payload with next and previous pointers, each an index or
NIL), let $h$ be a header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose
cell holds a node $X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor
$X.\mathrm{next}$ hold nodes whenever these pointers are not NIL. Let $S'$ be the store returned
by List Delete on $S$, $h$ and $x$. Let $h_0$ be a header and $L$ a list of indices such that $S$
with header $h_0$ represents $L$: the entries of $L$ are distinct, $h_0$ is the first entry of
$L$ (NIL if $L$ is empty), and the cell of each entry of $L$ holds a node whose previous and next
pointers are the adjacent entries of $L$, NIL at the ends. If neither $X.\mathrm{prev}$ nor
$X.\mathrm{next}$ is an entry of $L$, then $S'$ with header $h_0$ also represents $L$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_disjoint_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-disjoint-represents).

## Doubly linked list deletion costs at most four events

Let $S$ be a store of $n$ cells,
each empty or holding a node (a payload with next and previous pointers, each an index or NIL),
let $h$ be a header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell
holds a node $X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor
$X.\mathrm{next}$ hold nodes whenever these pointers are not NIL. Then List Delete on $S$, $h$
and $x$ costs at most $4$, counting NIL tests and executed pointer and header assignments.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-time-le).

## Correctness of doubly linked list deletion

Let $S$ be a store of $n$ cells, each empty or
holding a node (a payload with next and previous pointers, each an index or NIL), let $h$ be a
header (an index in $\{0, \dots, n-1\}$ or NIL), and let $x$ be an index whose cell holds a node
$X$ such that the cells at the predecessor $X.\mathrm{prev}$ and the successor $X.\mathrm{next}$
hold nodes whenever these pointers are not NIL. Let $S'$ and $h'$ be the store and header
returned by List Delete on $S$, $h$ and $x$. Let $L$ be a list of indices such that $S$ with
header $h$ represents $L$: the entries of $L$ are distinct, $h$ is the first entry of $L$ (NIL if
$L$ is empty), and the cell of each entry of $L$ holds a node whose previous and next pointers
are the adjacent entries of $L$, NIL at the ends. If $x$ is an entry of $L$, then $S'$ with
header $h'$ represents the list obtained from $L$ by removing $x$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listDelete_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Delete.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-delete-represents).

## Doubly-linked-list insertion (LIST-INSERT)

A store is an array of $n$ cells, each
either empty or holding a node with a payload and optional next and previous pointers to cells.
Given allocated cells $x$ and $y$ such that the successor of $y$, if any, is allocated,
inserting $x$ after $y$ performs the five lines of LIST-INSERT in order, each reading the store
as updated so far: set the next pointer of $x$ to the next pointer of $y$; set the previous
pointer of $x$ to $y$; test whether the next pointer of $y$ is NIL; if it is some cell $z$, set
the previous pointer of $z$ to $x$; set the next pointer of $y$ to $x$. The result is the
updated store, with cost one unit per pointer assignment and per NIL test.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert).

## Cost of doubly-linked-list insertion

For a store $S$ and allocated cells $x$ and $y$
such that the successor of $y$ in $S$, if any, is allocated, the cost of inserting $x$ after
$y$, counting one unit per pointer assignment and per NIL test, is $5$ if $y$ has a successor
in $S$ and $4$ if the next pointer of $y$ in $S$ is NIL.

No distinctness of $x$ and $y$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-time).

## Result of doubly-linked-list insertion

For a store $S$ and allocated cells $x$ and $y$
such that the successor of $y$ in $S$, if any, is allocated, let $s$ be the next pointer of $y$
in $S$. Let $S_1$ be $S$ with cell $x$ replaced by the node of $x$ with next pointer $s$ and
previous pointer $y$. Let $S_2 = S_1$ if $s$ is NIL; if $s$ is a cell $z$, let $S_2$ be $S_1$
with the previous pointer of the node in cell $z$ of $S_1$ replaced by $x$. Then the store
returned by inserting $x$ after $y$ is $S_2$ with the next pointer of the node in cell $y$ of
$S_2$ replaced by $x$.

No distinctness or representation hypothesis is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-ret).

## Cells after doubly-linked-list insertion

For a store $S$, allocated cells $x$ and $y$
such that the successor of $y$ in $S$, if any, is allocated, and any cell $z$, let $s$ be the
next pointer of $y$ in $S$. Let $c_1$ be the node of $x$ in $S$ with next pointer replaced by
$s$ and previous pointer replaced by $y$ if $z = x$, and the content of cell $z$ in $S$
otherwise. Let $c_2$ be $c_1$ with previous pointer replaced by $x$ if $s = z$, and $c_1$
otherwise. Then cell $z$ of the store returned by inserting $x$ after $y$ is $c_2$ with next
pointer replaced by $x$ if $z = y$, and $c_2$ otherwise (an empty cell stays empty).

No distinctness of $x$, $y$ and $s$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-get).

## Frame property of doubly-linked-list insertion

For a store $S$ and allocated cells $x$
and $y$ such that the successor of $y$ in $S$, if any, is allocated, let $z$ be a cell with
$z \ne x$, $z \ne y$, and $z$ not the successor of $y$ in $S$. Then cell $z$ of the store
returned by inserting $x$ after $y$ equals cell $z$ of $S$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-frame).

## Doubly-linked-list insertion neither allocates nor frees cells

For a store $S$ and
allocated cells $x$ and $y$ such that the successor of $y$ in $S$, if any, is allocated, every
cell $z$ of the store returned by inserting $x$ after $y$ is allocated if and only if cell $z$ of
$S$ is allocated. No distinctness of $x$, $y$ and the successor of $y$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-allocated).

## Doubly-linked-list insertion preserves payloads

For a store $S$ and allocated cells $x$
and $y$ such that the successor of $y$ in $S$, if any, is allocated, every cell $z$ of the store
returned by inserting $x$ after $y$ is empty exactly when cell $z$ of $S$ is empty, and
otherwise holds a node with the same payload as the node in cell $z$ of $S$.

No hypothesis on the payloads, such as distinct keys, is needed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-payload).

## Insertion into a represented doubly-linked list

Suppose the store $S$ with head $h$
represents the list of distinct cells $(i_0, \dots, i_{m-1})$. Let $k < m$, let $x$ be an
allocated cell not among $i_0, \dots, i_{m-1}$, and assume that cell $i_k$ and its successor in
$S$, if any, are allocated. Then the store returned by inserting $x$ after $i_k$, with the same
head $h$, represents the list $(i_0, \dots, i_k, x, i_{k+1}, \dots, i_{m-1})$.

The hypothesis that $x$ is not in the list is used only in the proof; the insertion itself runs
without it.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-represents).

## Doubly-linked-list insertion preserves disjoint lists

Suppose the store $S$ with head
$h$ represents the list of cells $(i_0, \dots, i_{m-1})$ and with head $h'$ represents a list
$L'$ of cells, and that the two lists have no cell in common. Let $k < m$, let $x$ be an
allocated cell not in $L'$, and assume that cell $i_k$ and its successor in $S$, if any, are
allocated. Then the store returned by inserting $x$ after $i_k$, with head $h'$, still
represents $L'$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listInsert_disjoint_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Insert.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-insert-disjoint-represents).

## Circular doubly linked list with a sentinel

Let $S$ be a store of $n$ slots indexed by
$\{0, \dots, n-1\}$, each either empty or holding a node with a payload and optional next and
previous indices. The store $S$ represents a circular list with sentinel $s$ and data nodes
$x_1, \dots, x_k$ (a list of indices) when the $x_i$ are pairwise distinct and all differ from
$s$; slot $s$ holds a node whose next index is $x_1$ and whose previous index is $x_k$ (both
are $s$ when $k = 0$); and for every $i$ with $1 \le i \le k$, slot $x_i$ holds a node whose
previous index is $x_{i-1}$ and whose next index is $x_{i+1}$, where $x_0 = x_{k+1} = s$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.CircularRepresents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Basic.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Basic.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#circular-represents).

## Empty circular list with a sentinel

Let $S$ be a store of $n$ slots indexed by
$\{0, \dots, n-1\}$, each either empty or holding a node with a payload and optional next and
previous indices, and let $s$ be an index. Then $S$ represents the empty circular list with
sentinel $s$ if and only if slot $s$ holds a node whose next index and previous index are both
$s$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.CircularRepresents_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Basic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Basic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#circular-represents-nil).

## Deletion from a circular list with a sentinel

Let $S$ be a node store with $c$ cells,
each either empty or holding a node (a payload, an optional next address and an optional
previous address in $\{0, \dots, c-1\}$). Let $x$ be an address whose cell holds a node $\nu$
with previous address $p$ and next address $n$, where the cells at $p$ and $n$ are nonempty.
Sentinel deletion of $x$ from $S$ is the timed computation that first sets the next address of
the node at $p$ to $n$, at cost $1$, then sets the previous address of the node at $n$ in the
resulting store to $p$, at cost $1$, and returns the store obtained.

These dereferences are its only preconditions: it does not check that $x$ is not the sentinel
or that $x$ lies on a represented list.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete).

## Sentinel deletion takes two pointer assignments

Let $S$ be a node store and $x$ an
address whose cell holds a node with previous address $p$ and next address $n$, where the cells
at $p$ and $n$ are nonempty. Then sentinel deletion of $x$ from $S$ has cost exactly $2$, one
for each pointer assignment.

This includes the alias cases in which $p$, $n$ and $x$ are not pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-time).

## The store returned by sentinel deletion

Let $S$ be a node store and $x$ an address
whose cell holds a node with previous address $p$ and next address $n$, where the cells at $p$
and $n$ are nonempty. Let $S_1$ be $S$ with the node at $p$ replaced by a copy whose next
address is $n$. Then sentinel deletion of $x$ from $S$ returns $S_1$ with the node of $S_1$ at
$n$ replaced by a copy whose previous address is $p$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-ret).

## Cells after sentinel deletion

Let $S$ be a node store and $x$ an address whose cell
holds a node with previous address $p$ and next address $n$, where the cells at $p$ and $n$ are
nonempty. For every address $z$, let $C$ be the cell of $S$ at $z$ if $z \ne p$, and that cell
with its next address set to $n$ if $z = p$. Then after sentinel deletion of $x$ from $S$ the
cell at $z$ is $C$ if $z \ne n$, and $C$ with its previous address set to $p$ if $z = n$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-get).

## Sentinel deletion changes only the two neighbours

Let $S$ be a node store and $x$ an
address whose cell holds a node with previous address $p$ and next address $n$, where the cells
at $p$ and $n$ are nonempty. For every address $z$ with $z \ne p$ and $z \ne n$, the cell at $z$
after sentinel deletion of $x$ from $S$ equals the cell of $S$ at $z$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-frame).

## Sentinel deletion preserves allocation

Let $S$ be a node store and $x$ an address whose
cell holds a node with previous address $p$ and next address $n$, where the cells at $p$ and $n$
are nonempty. For every address $z$, the cell at $z$ after sentinel deletion of $x$ from $S$ is
nonempty if and only if the cell of $S$ at $z$ is nonempty.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-allocated).

## Sentinel deletion preserves payloads

Let $S$ be a node store and $x$ an address whose
cell holds a node with previous address $p$ and next address $n$, where the cells at $p$ and $n$
are nonempty. For every address $z$, the cell at $z$ after sentinel deletion of $x$ from $S$
and the cell of $S$ at $z$ are either both empty or both hold nodes with the same payload.

The payload includes any key and satellite data.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-payload).

## Sentinel deletion keeps the deleted node

Let $S$ be a node store and $x$ an address
whose cell holds a node with previous address $p$ and next address $n$, where the cells at $p$
and $n$ are nonempty. The cell at $x$ after sentinel deletion of $x$ from $S$ equals the cell of
$S$ at $x$, so the deleted node stays allocated and unchanged.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_deleted_record`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-deleted-record).

## Sentinel deletion removes a node from its circular list

Let $S$ be a node store and $x$
an address whose cell holds a node with previous address $p$ and next address $n$, where the
cells at $p$ and $n$ are nonempty. If $S$ represents a circular doubly linked list with sentinel
$s$ and data addresses $\ell$, and $x$ occurs in $\ell$, then the store returned by sentinel
deletion of $x$ from $S$ represents a circular doubly linked list with sentinel $s$ and the
list of data addresses obtained from $\ell$ by removing the first occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_circular`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-circular).

## Sentinel deletion preserves disjoint circular lists

Let $S$ be a node store and $x$ an
address whose cell holds a node with previous address $p$ and next address $n$, where the cells
at $p$ and $n$ are nonempty. Suppose $S$ represents a circular doubly linked list with sentinel
$s$ and data addresses $\ell$, with $x$ in $\ell$, and also one with sentinel $t$ and data
addresses $m$, such that no address occurs both among $s$ and $\ell$ and among $t$ and $m$.
Then the store returned by sentinel deletion of $x$ from $S$ still represents the circular
doubly linked list with sentinel $t$ and data addresses $m$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelDelete_disjoint_circular`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Delete.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-delete-disjoint-circular).

## Sentinel list insertion (LIST-INSERT′)

Let $S$ be a store of $n$ cells, each empty or
holding a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not
NIL, and the cell $w$ it points to is allocated. Sentinel insertion of $x$ after $y$ performs four
pointer assignments in order, each costing one time unit, and returns the resulting store: set
the next pointer of $x$ to the next pointer of $y$; set the previous pointer of $x$ to $y$; set
the previous pointer of the successor $w$ of $y$ to $x$; set the next pointer of $y$ to $x$.

Each assignment reads the store left by the previous ones, so aliased cells see earlier writes.
Unlike LIST-INSERT, there is no NIL test.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert).

## Sentinel insertion takes four steps

Let $S$ be a store of $n$ cells, each empty or holding
a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not NIL, and the
cell it points to is allocated. Then sentinel insertion of $x$ after $y$ in $S$ costs exactly $4$
time units, one per pointer assignment.

This counts logical pointer assignments, not full RAM cost.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-time).

## The store after sentinel insertion

Let $S$ be a store of $n$ cells, each empty or holding
a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not NIL, and the
cell $w$ it points to is allocated; write $S[c]$ for the node at an allocated cell $c$. Then the
store returned by sentinel insertion of $x$ after $y$ is obtained from $S$ by three updates, each
applied to the result of the previous one: replace the content of $x$ by the node $S[x]$ with next
pointer equal to the next pointer of $S[y]$ and previous pointer $y$; set the previous pointer of
the node at $w$ to $x$; set the next pointer of the node at $y$ to $x$.

No freshness or distinctness of $x$, $y$ and $w$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-ret).

## Sentinel insertion, cell by cell

Let $S$ be a store of $n$ cells, each empty or holding a
node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not NIL, and the
cell it points to is allocated; write $S[c]$ for the node at an allocated cell $c$. Let $S'$ be
the store returned by sentinel insertion of $x$ after $y$. Then for every cell $z$, the content of
$z$ in $S'$ is obtained from its content in $S$ by three steps in order: if $z = x$, replace the
content by the node $S[x]$ with next pointer equal to the next pointer of $S[y]$ and previous
pointer $y$; if the next pointer of $S[y]$ is $z$, set the previous pointer to $x$; if $z = y$,
set the next pointer to $x$. The last two steps leave an empty cell empty.

No distinctness of $x$, $y$, $z$ and the successor of $y$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-get).

## Sentinel insertion leaves other cells unchanged

Let $S$ be a store of $n$ cells, each
empty or holding a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is
not NIL, and the cell it points to is allocated. Let $S'$ be the store returned by sentinel
insertion of $x$ after $y$. If a cell $z$ differs from $x$ and from $y$, and the next pointer of
$y$ in $S$ is not $z$, then $z$ has the same content in $S'$ as in $S$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-frame).

## Sentinel insertion preserves allocation

Let $S$ be a store of $n$ cells, each empty or
holding a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not NIL,
and the cell it points to is allocated. Let $S'$ be the store returned by sentinel insertion of
$x$ after $y$. Then every cell $z$ is allocated in $S'$ if and only if it is allocated in $S$.

No distinctness of $x$, $y$, $z$ and the successor of $y$ is assumed.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-allocated).

## Sentinel insertion preserves payloads

Let $S$ be a store of $n$ cells, each empty or
holding a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is not NIL,
and the cell it points to is allocated. Let $S'$ be the store returned by sentinel insertion of
$x$ after $y$. Then for every cell $z$, either $z$ is empty in both $S$ and $S'$, or it holds a
node in both and the two nodes have the same payload, including keys and satellite data.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-payload).

## Sentinel insertion preserves the circular list

Let $S$ be a store of $n$ cells, each
empty or holding a node, in which the cells $x$ and $y$ are allocated, the next pointer of $y$ is
not NIL, and the cell it points to is allocated. Suppose $S$ circularly represents the list $L$
of cells with sentinel $s$, that $L$ is the concatenation of lists $B$ and $A$, and that $y$ is
the last element of $B$, or $y = s$ if $B$ is empty. If $x \ne s$ and $x$ does not occur in $L$,
then the store returned by sentinel insertion of $x$ after $y$ circularly represents, with
sentinel $s$, the list consisting of the elements of $B$, then $x$, then the elements of $A$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_circular`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-circular).

## Sentinel insertion preserves a disjoint circular list

Let $S$ be a store of $n$
cells, each empty or holding a node, in which the cells $x$ and $y$ are allocated, the next
pointer of $y$ is not NIL, and the cell it points to is allocated. Suppose $S$ circularly
represents the list $L$ with sentinel $s$, that $L$ is the concatenation of lists $B$ and $A$,
and that $y$ is the last element of $B$, or $y = s$ if $B$ is empty. Suppose $S$ also circularly
represents the list $M$ with sentinel $t$, that no cell among $s$ and the elements of $L$ equals
$t$ or an element of $M$, and that $x \ne t$ and $x$ does not occur in $M$. Then the store
returned by sentinel insertion of $x$ after $y$ still circularly represents $M$ with sentinel
$t$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.sentinelInsert_disjoint_circular`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Insert.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#sentinel-insert-disjoint-circular).

## Search in a circular list with a sentinel

Let a store have cells indexed by
$\{0, \dots, m-1\}$, each empty or holding a node that carries a key, satellite data and optional
next and prev links, and let the cell $s$ be the sentinel of some list of data nodes that the
store circularly represents. Sentinel search for a key $k$ first overwrites the key of the
sentinel with $k$, keeping its satellite data and links, then starts at the successor of $s$ and
follows next links until it reaches a node whose key is $k$. It returns the modified store
together with that node, or no node if the scan stopped at $s$.

Only the sentinel key is overwritten, and its old key is not restored. The cost charges one unit
for the key write, one for initializing the cursor, one for each key comparison, one for each
advance past a mismatching node and one for the final test against $s$; reads and result
construction are free, and physical storage or bit operations are not counted.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listSearchSentinel`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-search-sentinel).

## Sentinel search returns the first matching node

If a store circularly represents the list
$L$ of data nodes with sentinel $s$, then sentinel search for a key $k$ returns the first node of
$L$ (in list order, which starts at the successor of $s$) whose key in the input store is $k$, and
returns no node if no node of $L$ has key $k$. In particular, the sentinel is never returned.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listSearchSentinel_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-search-sentinel-ret).

## Cost of sentinel search

If a store circularly represents the list $L$ of $n$ data nodes
with sentinel $s$, then sentinel search for a key $k$ costs exactly $2i + 4$, where $i$ is the
position, counting from $0$, of the first node of $L$ whose key is $k$, and $i = n$ if no node of
$L$ has key $k$.

That is, two units for each mismatching data node before the match plus four fixed units; an
unsuccessful search scans all $n$ data nodes.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listSearchSentinel_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-search-sentinel-time).

## Sentinel search changes only the sentinel's key

Let $s$ be the sentinel of some list of
data nodes that a store circularly represents, and let $k$ be a key. In the store returned by
sentinel search for $k$, the cell $s$ holds the original sentinel node with its key replaced by
$k$ and its satellite data and next and prev links unchanged, and every cell $z \ne s$ holds
exactly what it held in the input store.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listSearchSentinel_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-search-sentinel-get).

## Sentinel search preserves the circular list

If a store circularly represents the list $L$
of data nodes with sentinel $s$, then for every key $k$ the store returned by sentinel search for
$k$ still circularly represents $L$ with sentinel $s$.

Formalized by `Cslib.Algorithms.Lean.DoublyLinkedList.listSearchSentinel_circular`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/DoublyLinkedList/Sentinel/Search.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html#list-search-sentinel-circular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Doubly linked list](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/doubly-linked-list)
