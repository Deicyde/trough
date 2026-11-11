---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Queue.Amortized.potential, Cslib.Algorithms.Lean.Queue.Amortized.dequeueCost, Cslib.Algorithms.Lean.Queue.Amortized.enqueue, Cslib.Algorithms.Lean.Queue.Amortized.enqueue_amortized, Cslib.Algorithms.Lean.Queue.Amortized.dequeue, Cslib.Algorithms.Lean.Queue.Amortized.dequeue_amortized, Cslib.Algorithms.Lean.Queue.Amortized.Operation, Cslib.Algorithms.Lean.Queue.Amortized.Operation.charge
statement: formalized
proof: formalized
---

# Two-list queue

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html).

## Potential of a two-list queue

For a queue stored as an enqueue list and a dequeue list, the
potential is the length of the enqueue list: the number of elements that will be reversed when
they are moved to the dequeue list.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.potential`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#potential).

## Modeled cost of a dequeue

For a queue stored as an enqueue list and a dequeue list, the
modeled cost of dequeueing is $1$ when the dequeue list is nonempty, and $m + 1$ when the dequeue
list is empty, where $m$ is the length of the enqueue list (the number of elements reversed when
they are moved to the dequeue list).

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.dequeueCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#dequeue-cost).

## Timed enqueue

Enqueueing a value $v$ onto a two-list queue $q$ returns the queue
obtained from $q$ by adding $v$ at the back, that is, by prepending $v$ to the enqueue list,
together with a recorded cost of $1$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.enqueue`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#enqueue).

## Amortized cost of enqueueing

For every two-list queue $q$ and every value $v$, the modeled
cost of enqueueing $v$ onto $q$ plus the potential of the resulting queue equals the potential of
$q$ plus $2$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.enqueue_amortized`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#enqueue-amortized).

## Timed dequeue

Dequeueing from a two-list queue $q$ returns the next element in first-in,
first-out order together with the remaining queue, or returns no element together with $q$ itself
when $q$ is empty. In both cases the recorded cost is the modeled dequeue cost of $q$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.dequeue`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#dequeue).

## Amortized cost of dequeueing

For every two-list queue $q$, the modeled cost of dequeueing
from $q$ plus the potential of the resulting queue equals the potential of $q$ plus $1$. This
includes the case where $q$ is empty.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.dequeue_amortized`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#dequeue-amortized).

## Queue operation

A queue operation over a type $\alpha$ is either a request to enqueue a
value $v \in \alpha$ or a request to dequeue. Sequences of such operations are used to state
aggregate cost bounds.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.Operation`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#operation).

## Amortized charge of a queue operation

The potential-method charge of a queue operation is
$2$ for an enqueue and $1$ for a dequeue.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.Operation.charge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#charge).

## One step of a queue operation

For a queue $q$, an enqueue operation with value $v$
performs the costed enqueue of $v$ onto $q$. A dequeue operation performs the costed dequeue
of $q$ and keeps the remaining queue and the cost, discarding the removed value; on an empty
queue the remaining queue is $q$ itself.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.step`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#step).

## Amortized cost of one queue operation

For every queue $q$ and every queue operation
$o$, the modeled cost of performing $o$ on $q$ plus the potential of the resulting queue equals
the potential of $q$ plus the charge of $o$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.step_amortized`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#step-amortized).

## Running a sequence of queue operations

Running a list of queue operations from a
queue $q$ performs the operations one step at a time from left to right, starting at $q$.
The result is the final queue, and the cost is the sum of the costs of the individual
steps; running the empty list returns $q$ at cost $0$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.run`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#run).

## Total charge of a sequence of queue operations

For a list of queue operations, the
total charge is the sum of the amortized charges of its operations, where an enqueue is charged
$2$ and a dequeue is charged $1$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.totalCharge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#total-charge).

## Amortized cost of a sequence of queue operations

For every list of queue operations and
every two-list queue $q$, the modeled cost of running the operations from left to right starting
at $q$, plus the potential of the final queue, equals the potential of $q$ plus the total charge
of the operations.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.run_amortized`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#run-amortized).

## Linear bound on the cost of queue operations

For every list of $n$ queue operations and
every two-list queue $q$, the modeled cost of running the operations from left to right starting
at $q$ is at most the potential of $q$ plus $2n$.

Formalized by `Cslib.Algorithms.Lean.Queue.Amortized.run_time_le_potential_add_twice_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Amortized.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#run-time-le-potential-add-twice-length).

## Contents of a two-list queue

A queue is stored as a dequeue list and an enqueue list
whose most recently enqueued element comes first. Its contents are its elements in FIFO
order: the dequeue list followed by the reverse of the enqueue list.

Formalized by `Cslib.Algorithms.Lean.Queue.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#contents).

## Array conversion lists the contents

For every queue $q$, the array obtained from $q$,
read as a list, equals the contents of $q$.

Formalized by `Cslib.Algorithms.Lean.Queue.toArray_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#to-array-to-list).

## Enqueueing appends to the contents

For every queue $q$ and value $v$, the contents of
the queue obtained by enqueueing $v$ onto $q$ are the contents of $q$ followed by $v$.

Formalized by `Cslib.Algorithms.Lean.Queue.contents_enqueue`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#contents-enqueue).

## The queue emptiness test matches the contents

For every queue $q$, the emptiness test
of $q$ returns true if and only if the contents of $q$ are empty.

Formalized by `Cslib.Algorithms.Lean.Queue.isEmpty_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#is-empty-eq-true-iff).

## Dequeueing fails exactly on empty queues

For every queue $q$, dequeueing $q$ returns
nothing if and only if the contents of $q$ are empty.

Formalized by `Cslib.Algorithms.Lean.Queue.dequeue?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#dequeue-eq-none-iff).

## A successful dequeue splits off the first element

If dequeueing a queue $q$ succeeds
and returns an element $a$ and a queue $r$, then the contents of $q$ are $a$ followed by the
contents of $r$.

Formalized by `Cslib.Algorithms.Lean.Queue.contents_eq_cons_of_dequeue?_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Queue/Semantics.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html#contents-eq-cons-of-dequeue-eq-some).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-list queue](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/two-list-queue)
