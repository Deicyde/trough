---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SinglyLinkedList.Node, Cslib.Algorithms.Lean.SinglyLinkedList.Represents, Cslib.Algorithms.Lean.SinglyLinkedList.represents_nil, Cslib.Algorithms.Lean.SinglyLinkedList.represents_allocated, Cslib.Algorithms.Lean.SinglyLinkedList.contents, Cslib.Algorithms.Lean.SinglyLinkedList.contents_length, Cslib.Algorithms.Lean.SinglyLinkedList.contents_congr, Cslib.Algorithms.Lean.SinglyLinkedList.represents_contents_isSome
statement: formalized
proof: formalized
---

# Singly linked list

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html).

## Singly linked list node

A singly linked list node with payloads in $\alpha$ and identities
in $\iota$ consists of a payload in $\alpha$ (the key together with any satellite data) and a next
pointer, which is either an identity in $\iota$ or NIL.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.Node`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#node).

## Store representing a singly linked list

Fix a capacity $n$, let a store assign to each
identity below $n$ either nothing or a singly linked list node whose next pointer is an identity
below $n$ or NIL, and let the head be an identity below $n$ or NIL. The store and head represent
the list of identities $i_0, \dots, i_{k-1}$ when these identities are pairwise distinct, the head
is $i_0$ (and NIL when $k = 0$), and for each $j < k$ the store entry at $i_j$ is a node whose next
pointer is $i_{j+1}$ if $j + 1 < k$ and NIL otherwise.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.Represents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#represents).

## Representation of the empty singly linked list

Fix a capacity $n$ and let $s$ be any store
assigning to each identity below $n$ either nothing or a singly linked list node. Then $s$ with
head NIL represents the empty list of identities.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.represents_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#represents-nil).

## Represented identities hold nodes

Fix a capacity $n$, let $s$ be a store assigning to
each identity below $n$ either nothing or a singly linked list node, and let $\mathrm{head}$ be an
identity below $n$ or NIL. If $s$ and $\mathrm{head}$ represent the list of identities
$i_0, \dots, i_{k-1}$, then for every identity $i$ in this list the store entry $s(i)$ is a
node.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.represents_allocated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#represents-allocated).

## Payload list of a singly linked list store

Fix a capacity $n$ and let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node (a payload
together with a next pointer that is an identity below $n$ or NIL). For a list of identities
$i_0, \dots, i_{m-1}$ below $n$, the contents of $s$ at this list are the list
$c_0, \dots, c_{m-1}$, where $c_j$ is the payload of $s(i_j)$ when $s(i_j)$ is a node and $c_j$ is
nothing (marking an unallocated cell) when $s(i_j)$ is nothing.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#contents).

## The payload list has one entry per identity

Fix a capacity $n$ and let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node. For every list
$L$ of identities below $n$, the contents of $s$ at $L$ have the same length as $L$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.contents_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#contents-length).

## The payload list depends only on the listed cells

Fix a capacity $n$ and let $s$ and $s'$
be stores assigning to each identity below $n$ either nothing or a singly linked list node. If $L$
is a list of identities below $n$ and $s'(i) = s(i)$ for every $i$ in $L$, then the contents of
$s'$ at $L$ equal the contents of $s$ at $L$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.contents_congr`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#contents-congr).

## Represented lists have no missing contents

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, and let
$\mathrm{head}$ be an identity below $n$ or NIL. If $s$ and $\mathrm{head}$ represent the list of
identities $i_0, \dots, i_{k-1}$, then every entry of the contents of $s$ at $i_0, \dots, i_{k-1}$
is a payload rather than nothing.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.represents_contents_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#represents-contents-is-some).

## Prepending a node to a singly linked list

Fix a capacity $n$, let a store assign to each
identity below $n$ either nothing or a singly linked list node, let the head be an identity below
$n$ or NIL, and let $x$ be an identity whose store entry is a node. Prepending $x$ replaces the
store entry at $x$ by the same node with its next pointer set to the head, leaves every other entry
unchanged, and returns the updated store together with the new head $x$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend).

## Prepending makes the node the head

Fix a capacity $n$, let $s$ be a store assigning to
each identity below $n$ either nothing or a singly linked list node, let $\mathrm{head}$ be an
identity below $n$ or NIL, and let $x$ be an identity such that $s(x)$ is a node. Then the head
returned by Prepend on $s$, $\mathrm{head}$ and $x$ is $x$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_head`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-head).

## Store after prepending to a singly linked list

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, let
$\mathrm{head}$ be an identity below $n$ or NIL, and let $x$ be an identity such that $s(x)$ is a
node. Then for every identity $z$ below $n$, the entry at $z$ of the store returned by Prepend on
$s$, $\mathrm{head}$ and $x$ is the node $s(x)$ with its next pointer replaced by $\mathrm{head}$
when $z = x$, and is $s(z)$ when $z \ne x$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-get).

## Frame property of prepending to a singly linked list

Let $S$ be a store assigning to
each identity below $n$ either nothing or a singly linked list node, let $h$ be an identity below
$n$ or NIL, and let $x$ be an identity whose store entry is a node. For every identity
$z \ne x$, cell $z$ of the store obtained by prepending $x$ to the list with head $h$ equals
cell $z$ of $S$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-frame).

## The prepended node points at the old head

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, let
$\mathrm{head}$ be an identity below $n$ or NIL, and let $x$ be an identity such that $s(x)$ is a
node. Then the entry at $x$ of the store returned by Prepend on $s$, $\mathrm{head}$ and $x$ is the
node $s(x)$ with its payload kept and its next pointer replaced by $\mathrm{head}$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-node).

## Prepending conses onto the represented list

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, let
$\mathrm{head}$ be an identity below $n$ or NIL, and let $x$ be an identity such that $s(x)$ is a
node. If $s$ and $\mathrm{head}$ represent the list of identities $i_0, \dots, i_{k-1}$ and $x$ is
none of $i_0, \dots, i_{k-1}$, then the store and head returned by Prepend on $s$, $\mathrm{head}$
and $x$ represent the list $x, i_0, \dots, i_{k-1}$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-represents).

## Contents after prepending to a singly linked list

Let $S$ be a store assigning to each
identity below $n$ either nothing or a singly linked list node, let $h$ be an identity below $n$
or NIL, let $x$ be an identity whose store entry is a node with payload $a$, and let
$(i_0, \dots, i_{m-1})$ be a list of identities below $n$ not containing $x$. Then the contents,
at the list $(x, i_0, \dots, i_{m-1})$, of the store obtained by prepending $x$ to the list with
head $h$ are the present payload $a$ followed by the contents of $S$ at the list
$(i_0, \dots, i_{m-1})$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.prepend_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#prepend-contents).

## Inserting a node after another in a singly linked list

Let a store $S$ assign to each
identity below $n$ either nothing or a singly linked list node whose next pointer is an identity
below $n$ or NIL, and let $x$ and $y$ be identities whose store entries are nodes. Inserting $x$
after $y$ first replaces cell $x$ by the node of $x$ with next pointer replaced by the next
pointer of $y$ in $S$, then, in the store so obtained, replaces the next pointer of the node in
cell $y$ by $x$, and returns the resulting store.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after).

## Cells after singly-linked-list insertion

Let $S$ be a store assigning to each identity
below $n$ either nothing or a singly linked list node, let $x$ and $y$ be identities whose store
entries are nodes, and let $z$ be any identity. Let $c$ be the node of $x$ in $S$ with next
pointer replaced by the next pointer of $y$ in $S$ if $z = x$, and the content of cell $z$ in $S$
otherwise. Then cell $z$ of the store obtained by inserting $x$ after $y$ is $c$ with next pointer
replaced by $x$ if $z = y$, and $c$ otherwise.

No distinctness of $x$ and $y$ is assumed.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after-get).

## Frame property of singly-linked-list insertion

Let $S$ be a store assigning to each
identity below $n$ either nothing or a singly linked list node, and let $x$ and $y$ be identities
whose store entries are nodes. For every identity $z$ with $z \ne y$ and $z \ne x$, cell $z$ of
the store obtained by inserting $x$ after $y$ equals cell $z$ of $S$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after-frame).

## Singly-linked-list insertion preserves payloads

Let $S$ be a store assigning to each
identity below $n$ either nothing or a singly linked list node, and let $x$ and $y$ be identities
whose store entries are nodes. For every identity $z$, cell $z$ of the store obtained by inserting
$x$ after $y$ is empty exactly when cell $z$ of $S$ is empty, and otherwise holds a node with the
same payload as the node in cell $z$ of $S$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after-payload).

## Insertion into a represented singly linked list

Suppose the store $S$ with head $h$
represents the list of distinct identities $(i_0, \dots, i_{m-1})$. Let $k < m$, assume that the
store entry of $i_k$ is a node, and let $x$ be an identity whose store entry is a node and which
is not among $i_0, \dots, i_{m-1}$. Then the store obtained by inserting $x$ after $i_k$, with
the same head $h$, represents the list $(i_0, \dots, i_k, x, i_{k+1}, \dots, i_{m-1})$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after-represents).

## Contents after singly-linked-list insertion

Let $S$ be a store assigning to each identity
below $n$ either nothing or a singly linked list node, let $(i_0, \dots, i_{m-1})$ be a list of
identities below $n$, let $k < m$, and let $x$ be an identity such that the store entries of $x$
and $i_k$ are nodes, the node of $x$ having payload $a$. Then the contents of the store obtained
by inserting $x$ after $i_k$ at the list $(i_0, \dots, i_k, x, i_{k+1}, \dots, i_{m-1})$ equal
the contents of $S$ at $(i_0, \dots, i_{m-1})$ with the present payload $a$ inserted as entry
$k + 1$ (counting from $0$).

No representation or distinctness hypothesis is assumed.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.insertAfter_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#insert-after-contents).

## Deleting the head of a singly linked list

Let a store assign to each identity below $n$
either nothing or a singly linked list node whose next pointer is an identity below $n$ or NIL,
and let the head be an identity below $n$ or NIL. Deleting the head returns the store unchanged
together with a new head: NIL if the head is NIL or the store entry at the head is empty, and
otherwise the next pointer of the node stored at the head.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteHead`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-head).

## Deleting the head removes the first identity

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, and suppose that
$s$ with head $h$ represents the list of identities $L$, where $h$ is an identity below $n$ or NIL.
Let $(s', h')$ be the store and head returned by deleting the head of $s$ with head $h$. Then $s'$
with head $h'$ represents $L$ with its first entry removed, which is the empty list when $L$ is
empty.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteHead_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-head-represents).

## Deleting the successor in a singly linked list

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node whose next
pointer is an identity below $n$ or NIL, and let $y$ be an identity such that $s(y)$ is a node.
Deleting after $y$ returns the store that agrees with $s$ except at $y$, where it holds the node
$s(y)$ with its next pointer replaced as follows: if the next pointer of $s(y)$ is an identity $m$
and $s(m)$ is a node, the new next pointer is the next pointer of $s(m)$; otherwise it is NIL.

The removed node stays allocated in the store; at the tail the links are unchanged.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after).

## Cells after deleting a successor

Fix a capacity $n$, let $s$ be a store assigning to each
identity below $n$ either nothing or a singly linked list node, let $y$ be an identity such that
$s(y)$ is a node, and let $s'$ be the store obtained from $s$ by deleting the successor of $y$.
Let $c$ be the node $s(y)$ with its next pointer replaced by the next pointer of $s(m)$ if the
next pointer of $s(y)$ is an identity $m$ such that $s(m)$ is a node, and by NIL otherwise. Then
for every identity $z$, $s'(z)$ is the node $c$ if $z = y$, and $s'(z) = s(z)$ if $z \ne y$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter_get`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after-get).

## Deleting a successor leaves other cells unchanged

Fix a capacity $n$, let $s$ be a store
assigning to each identity below $n$ either nothing or a singly linked list node, let $y$ be an
identity such that $s(y)$ is a node, and let $s'$ be the store obtained from $s$ by deleting the
successor of $y$. Then $s'(z) = s(z)$ for every identity $z \ne y$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter_frame`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after-frame).

## Deleting a successor preserves payloads

Fix a capacity $n$, let $s$ be a store assigning
to each identity below $n$ either nothing or a singly linked list node, let $y$ be an identity
such that $s(y)$ is a node, and let $s'$ be the store obtained from $s$ by deleting the successor
of $y$. Then for every identity $z$, either $s(z)$ and $s'(z)$ are both nothing, or both are nodes
with the same payload.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter_payload`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after-payload).

## Deleting a successor removes it from the represented list

Fix a capacity $n$, let $s$ be a
store assigning to each identity below $n$ either nothing or a singly linked list node, and
suppose that $s$ with head $h$ represents the list of identities $L = (i_0, \dots, i_{m-1})$. Let
$k < m$ be such that $s(i_k)$ is a node, and let $s'$ be the store obtained from $s$ by deleting
the successor of $i_k$. Then $s'$ with the same head $h$ represents the list obtained from $L$ by
removing the entry at position $k + 1$. Positions count from $0$, and at the tail ($k + 1 = m$)
the list is unchanged.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter_represents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after-represents).

## Contents after deleting a successor

Fix a capacity $n$, let $s$ be a store assigning to
each identity below $n$ either nothing or a singly linked list node, let
$L = (i_0, \dots, i_{m-1})$ be a list of identities below $n$, and let $k < m$ be such that
$s(i_k)$ is a node. Let $s'$ be the store obtained from $s$ by deleting the successor of $i_k$.
Then the contents of $s'$ at the list obtained from $L$ by removing the entry at position $k + 1$
equal the list obtained from the contents of $s$ at $L$ by removing the entry at position $k + 1$.
Positions count from $0$, and nothing is removed when $k + 1 = m$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.deleteAfter_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#delete-after-contents).

## Fuel-bounded search in a singly-linked list

Given a node pool with $n$ cells, a target
payload $t$, a fuel $f \in \mathbb{N}$ and a start $h$ that is either an identity in
$\{0, \dots, n-1\}$ or NIL, fuel-bounded search for $t$ from $h$ with fuel $f$ returns nothing
if $f = 0$ or $h$ is NIL. Otherwise $h$ is an identity $i$: the search returns nothing if cell
$i$ is unallocated, returns $i$ if the node in cell $i$ has payload $t$, and otherwise continues
from the next pointer of that node with fuel $f - 1$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.searchAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 625](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L625). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search-aux).

## Search in a singly-linked list

Given a node pool with $n$ cells, a head $h$ that is
either an identity in $\{0, \dots, n-1\}$ or NIL, and a target payload $t$, the search for $t$
from $h$ is fuel-bounded search for $t$ from $h$ with fuel $n$. It follows next pointers from
$h$ and returns the first visited identity whose node has payload $t$, returning nothing if it
reaches NIL or an unallocated cell first, or if $n$ steps run out.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.search`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search).

## Fuel-bounded search finds the first matching represented identity

Suppose a node pool
represents, from the head $h$, the list of distinct identities $\ell$. Then for every target
payload $t$ and every fuel $f$ with $f \ge |\ell|$, fuel-bounded search for $t$ from $h$ with
fuel $f$ returns the first identity in $\ell$ whose cell holds a node with payload $t$, and
returns nothing if no identity in $\ell$ has this property.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.searchAux_eq_find?`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search-aux-eq-find).

## Represented lists fit in the store

Fix a capacity $n$, let $s$ be a store assigning to
each identity below $n$ either nothing or a singly linked list node, and let $\mathrm{head}$ be an
identity below $n$ or NIL. If $s$ and $\mathrm{head}$ represent the list of identities
$i_0, \dots, i_{k-1}$, then $k \le n$.

The identities are pairwise distinct and there are only $n$ of them.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.represents_length_le_capacity`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#represents-length-le-capacity).

## Search finds the first matching represented identity

If a node pool represents, from the
head $h$, the list of distinct identities $\ell$, then for every target payload $t$ the search
for $t$ from $h$ returns the first identity in $\ell$ whose cell holds a node with payload $t$,
and returns nothing if no identity in $\ell$ has this property.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.search_eq_find?`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search-eq-find).

## A successful search returns a matching represented identity

If a node pool represents,
from the head $h$, the list of distinct identities $\ell$, and the search for a target payload
$t$ from $h$ returns an identity $x$, then $x$ belongs to $\ell$ and cell $x$ holds a node with
payload $t$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.search_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search-eq-some).

## Search fails exactly when no represented node has the target payload

If a node pool
represents, from the head $h$, the list of distinct identities $\ell$, then for every target
payload $t$ the search for $t$ from $h$ returns nothing if and only if no identity in $\ell$ has
a cell holding a node with payload $t$.

Formalized by `Cslib.Algorithms.Lean.SinglyLinkedList.search_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SinglyLinkedList.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html#search-eq-none-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Singly linked list](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/singly-linked-list)
