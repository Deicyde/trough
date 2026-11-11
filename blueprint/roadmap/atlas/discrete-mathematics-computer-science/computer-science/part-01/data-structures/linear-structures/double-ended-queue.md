---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Deque, Cslib.Algorithms.Lean.Deque.contents, Cslib.Algorithms.Lean.Deque.empty, Cslib.Algorithms.Lean.Deque.isEmpty, Cslib.Algorithms.Lean.Deque.isEmpty_eq_true_iff, Cslib.Algorithms.Lean.Deque.pushFront, Cslib.Algorithms.Lean.Deque.contents_pushFront, Cslib.Algorithms.Lean.Deque.pushBack
statement: formalized
proof: formalized
---

# Double-ended queue

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html).

## Deque

## Two-list deque

A deque with elements in a type $\alpha$ consists of two lists of elements
of $\alpha$, the front list and the back list. The front list holds the front part of the
sequence in order and the back list holds the back part in reverse order.

Formalized by `Cslib.Algorithms.Lean.Deque`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#deque).

## Represented sequence of a deque

The sequence represented by a deque with front list $f$
and back list $b$ is $f$ followed by the reverse of $b$; it lists the elements from front to
back.

Formalized by `Cslib.Algorithms.Lean.Deque.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#contents).

## The empty deque

The empty deque is the deque whose front list and back list are both
empty.

Formalized by `Cslib.Algorithms.Lean.Deque.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#empty).

## Emptiness test for a deque

The emptiness test of a deque returns true exactly when both
its front list and its back list are empty.

Formalized by `Cslib.Algorithms.Lean.Deque.isEmpty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#is-empty).

## Correctness of the deque emptiness test

For every deque $d$, the emptiness test of $d$
returns true if and only if the sequence represented by $d$ is empty.

Formalized by `Cslib.Algorithms.Lean.Deque.isEmpty_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#is-empty-eq-true-iff).

## Push at the front of a deque

Let $d$ be a deque with front list $f$ and back list $b$,
where $b$ is stored in reverse order. Pushing an element $x$ at the front of $d$ gives the deque
with front list consisting of $x$ followed by the entries of $f$, and back list $b$.

Formalized by `Cslib.Algorithms.Lean.Deque.pushFront`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#push-front).

## Pushing at the front of a deque

For every deque $d$ and element $x$, the sequence
represented by the deque obtained by pushing $x$ at the front of $d$ is $x$ followed by the
sequence represented by $d$.

Formalized by `Cslib.Algorithms.Lean.Deque.contents_pushFront`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#contents-push-front).

## Push at the back of a deque

Let $d$ be a deque with front list $f$ and back list $b$,
where $b$ is stored in reverse order. Pushing an element $x$ at the back of $d$ gives the deque
with front list $f$ and back list consisting of $x$ followed by the entries of $b$.

Formalized by `Cslib.Algorithms.Lean.Deque.pushBack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#push-back).

## Pushing at the back of a deque

For every deque $d$ and element $x$, the sequence
represented by the deque obtained by pushing $x$ at the back of $d$ is the sequence represented by
$d$ followed by $x$.

Formalized by `Cslib.Algorithms.Lean.Deque.contents_pushBack`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#contents-push-back).

## Peek at the front of a deque

Let $d$ be a deque with front list $f$ and back list $b$,
where $b$ is stored in reverse order. Peeking at the front of $d$ returns, without removing it,
the first element of $f$ when $f$ is nonempty, and otherwise the last element of $b$; when both
lists are empty it returns no element.

Formalized by `Cslib.Algorithms.Lean.Deque.peekFront`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#peek-front).

## Peeking at the front gives the first element

For every deque $d$, peeking at the front of
$d$ returns the first element of the sequence represented by $d$, and returns no element when
that sequence is empty.

Formalized by `Cslib.Algorithms.Lean.Deque.peekFront_eq_head`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#peek-front-eq-head).

## Peek at the back of a deque

Let $d$ be a deque with front list $f$ and back list $b$,
where $b$ is stored in reverse order. Peeking at the back of $d$ returns, without removing it,
the first element of $b$ when $b$ is nonempty, and otherwise the last element of $f$; when both
lists are empty it returns no element.

Formalized by `Cslib.Algorithms.Lean.Deque.peekBack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#peek-back).

## Peeking at the back of a deque

For every deque $d$, peeking at the back of $d$ returns
the last element of the sequence represented by $d$ when that sequence is nonempty, and returns
nothing when it is empty.

Formalized by `Cslib.Algorithms.Lean.Deque.peekBack_eq_getLast`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#peek-back-eq-get-last).

## Pop the front of a deque

Let $d$ be a deque with front list $f$ and back list $b$, where
$b$ is stored in reverse order. If $f$ has first element $v$ and remaining list $f'$, popping the
front of $d$ returns $v$ together with the deque with front list $f'$ and back list $b$. If $f$ is
empty and the reverse of $b$ has first element $v$ and remaining list $r$, it returns $v$ together
with the deque with front list $r$ and empty back list. If both lists are empty, it returns no
result.

Formalized by `Cslib.Algorithms.Lean.Deque.popFront`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#pop-front).

## Popping the front fails exactly on empty deques

For every deque $d$, popping the front of
$d$ returns no result if and only if the sequence represented by $d$ is empty.

Formalized by `Cslib.Algorithms.Lean.Deque.popFront_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#pop-front-eq-none-iff).

## Popping the front of a deque

If popping the front of a deque $d$ succeeds and returns an
element $x$ and a deque $d'$, then the sequence represented by $d$ is $x$ followed by the sequence
represented by $d'$.

Formalized by `Cslib.Algorithms.Lean.Deque.contents_eq_cons_of_popFront_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#contents-eq-cons-of-pop-front-eq-some).

## Pop the back of a deque

Let $d$ be a deque with front list $f$ and back list $b$, where
$b$ is stored in reverse order. If $b$ has first element $v$ and remaining list $b'$, popping the
back of $d$ returns $v$ together with the deque with front list $f$ and back list $b'$. If $b$ is
empty and the reverse of $f$ has first element $v$ and remaining list $r$, it returns $v$ together
with the deque with empty front list and back list $r$. If both lists are empty, it returns no
result.

Formalized by `Cslib.Algorithms.Lean.Deque.popBack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#pop-back).

## Popping the back fails exactly on empty deques

For every deque $d$, popping the back of
$d$ returns no result if and only if the sequence represented by $d$ is empty.

Formalized by `Cslib.Algorithms.Lean.Deque.popBack_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#pop-back-eq-none-iff).

## Popping the back of a deque

If popping the back of a deque $d$ succeeds and returns an
element $x$ and a deque $d'$, then the sequence represented by $d$ is the sequence represented by
$d'$ followed by $x$.

Formalized by `Cslib.Algorithms.Lean.Deque.contents_eq_append_of_popBack_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Deque.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Deque.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html#contents-eq-append-of-pop-back-eq-some).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Double-ended queue](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/double-ended-queue)
