---
declaration: section
origin: cited
lean: Cslib.Algorithms.Concurrency.DeadlockDetection.State, Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces, Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces.erase, Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces.eq_nil, Cslib.Algorithms.Concurrency.DeadlockDetection.State.reduceAux, Cslib.Algorithms.Concurrency.DeadlockDetection.State.finished, Cslib.Algorithms.Concurrency.DeadlockDetection.State.detect, Cslib.Algorithms.Concurrency.DeadlockDetection.State.reduceAux_disjoint
statement: formalized
proof: formalized
---

# Deadlock detection

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html).

## Deadlock Detection

## Resource-allocation state

For a type $P$ of processes and a type $R$ of resource types,
a state consists of two functions $\mathrm{alloc}, \mathrm{request} : P \to R \to \mathbb{N}$:
$\mathrm{alloc}(p)(r)$ is the number of instances of resource type $r$ that process $p$ holds,
and $\mathrm{request}(p)(r)$ is the number of instances of $r$ that $p$ is waiting for.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State`, a structure declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#state).

## Reduction sequences

Let $P$ be a type of processes and $R$ a type of resource types, and
let $S$ be a state that gives each process $p$ an allocation $\mathrm{alloc}(p)$ and a request
$\mathrm{request}(p)$, both functions $R \to \mathbb{N}$ ordered componentwise. A list of
processes $p_1, \dots, p_k$ is a reduction sequence of $S$ from the free vector
$w : R \to \mathbb{N}$ when, for every $1 \le i \le k$, we have
$\mathrm{request}(p_i) \le w + \mathrm{alloc}(p_1) + \dots + \mathrm{alloc}(p_{i-1})$. In
particular the empty list is a reduction sequence from every $w$.

Informally: starting with $w$ free, each process in turn gets its request, finishes, and
releases its allocation.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces`, a definition declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#reduces).

## Letting a process that fits finish first preserves reduction sequences

Let $w$ be a
resource vector and $p$ a process whose request is at most $w$. If $\sigma$ is a reduction sequence
from $w$, then the list obtained from $\sigma$ by removing the first occurrence of $p$, if any, is a
reduction sequence from $w$ plus the allocation of $p$.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces.erase`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#erase).

## A reduction sequence in which no process fits is empty

Let $w$ be a resource vector. If
$\sigma$ is a reduction sequence from $w$ and no process of $\sigma$ has a request at most $w$,
then $\sigma$ is empty.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.Reduces.eq_nil`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#eq-nil).

## The detection algorithm with fuel

Given the fuel, a number of steps, together with the free
resource vector $w$ and a list of pending processes, the algorithm returns two lists: the processes
that finished, in order, and the processes left over. With fuel $0$, or when no pending process has
a request at most $w$, no process finishes and all the pending processes are left over. Otherwise
the fuel is $n + 1$ for some $n$; take the first pending process $p$ whose request is at most $w$
and run the algorithm with fuel $n$, free vector $w$ plus the allocation of $p$, and the list with
that entry of $p$ removed. The result is $p$ followed by the processes that finished there,
together with the processes left over there.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.reduceAux`, a definition declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#reduce-aux).

## The processes the detection algorithm lets finish

Given the free resource vector $w$ and a
list of pending processes, run the detection algorithm: repeatedly take the first pending process
whose request is at most what is free, let it finish, remove that entry from the list and add its
allocation to what is free, until no pending process has a request at most what is free. This is
the list of the processes taken, in the order they were taken.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.finished`, a definition declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#finished).

## The detection algorithm

Given the free resource vector $w$ and a list of pending
processes, repeatedly take the first pending process whose request is at most what is free, let it
finish, remove that entry from the list and add its allocation to what is free, until no pending
process has a request at most what is free. The processes still pending then are the ones reported
as deadlocked.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.detect`, a definition declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#detect).

## The algorithm with fuel leaves over no process of a reduction sequence

Let $w$ be the free
resource vector, let the list of pending processes contain no duplicates, and let the fuel be at
least the number of pending processes. If $\sigma$ is a duplicate-free reduction sequence from $w$
all of whose processes are pending, then no process of $\sigma$ is among the processes that the
detection algorithm with that fuel leaves over.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.reduceAux_disjoint`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#reduce-aux-disjoint).

## Every reported process is stuck

Let $w$ be the free resource vector. For every process $q$
that the detection algorithm reports, the request of $q$ is not at most $w$ plus the sum of the
allocations of the processes that the algorithm lets finish: for at least one resource type, $q$
requests more than is free even after all those processes have released their allocations.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.detect_stuck`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#detect-stuck).

## The processes the algorithm lets finish form a reduction sequence

For every free resource
vector $w$ and every list of pending processes, the processes that the detection algorithm lets
finish, in the order it lets them finish, form a reduction sequence from $w$.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.finished_reduces`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#finished-reduces).

## Correctness of deadlock detection

Let $w$ be the free resource vector and let the list of
pending processes contain no duplicates. A process $p$ is reported by the detection algorithm if
and only if $p$ is pending and no duplicate-free reduction sequence $\sigma$ from $w$ made of
pending processes contains $p$.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.mem_detect_iff`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#mem-detect-iff).

## No deadlock is reported exactly when all the processes can finish

Let $w$ be the free
resource vector and let the list of pending processes contain no duplicates. The detection
algorithm, started with $w$ free, reports no process if and only if some reordering of the pending
processes is a reduction sequence from $w$.

Formalized by `Cslib.Algorithms.Concurrency.DeadlockDetection.State.detect_eq_nil_iff`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/DeadlockDetection.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html#detect-eq-nil-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deadlock detection](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-detection)
