---
declaration: section
origin: cited
lean: Cslib.Algorithms.Concurrency.Banker.System, Cslib.Algorithms.Concurrency.Banker.System.need, Cslib.Algorithms.Concurrency.Banker.System.SafeSeq, Cslib.Algorithms.Concurrency.Banker.System.Safe, Cslib.Algorithms.Concurrency.Banker.System.SafeSeq.mono, Cslib.Algorithms.Concurrency.Banker.System.SafeSeq.erase, Cslib.Algorithms.Concurrency.Banker.System.Safe.exists_runnable, Cslib.Algorithms.Concurrency.Banker.System.safe_iff_safe_erase
statement: formalized
proof: formalized
---

# Banker's algorithm

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html).

## Banker

## Claims and allocations of processes

A system with processes $P$ and resource types
$R$ consists of two maps $\mathrm{claim}, \mathrm{alloc} : P \to (R \to \mathbb{N})$, where
$\mathrm{claim}(p)$ is the maximum demand of process $p$ for each resource type and
$\mathrm{alloc}(p)$ is the amount of each resource type currently allocated to $p$. No
inequality between the two is required.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System`, a structure declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#system).

## Remaining need

The remaining need of a process $p$ in a system $S$ is the resource
vector $\mathrm{claim}(p) - \mathrm{alloc}(p)$: the maximum claim of $p$ minus its current
allocation, computed for each resource type by truncated subtraction of natural numbers, so it
is $0$ for every resource type where the allocation exceeds the claim.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.need`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#need).

## Safe sequence

Let $S$ be a system with processes $P$ and resource types $R$, where
process $p$ has maximum claim $\mathrm{claim}(p)$ and allocation $\mathrm{alloc}(p)$ in
$R \to \mathbb{N}$. A list $p_1, \dots, p_k$ of processes is a safe sequence from the free
resource vector $w : R \to \mathbb{N}$ when, for each $i$, the remaining need
$\mathrm{claim}(p_i) - \mathrm{alloc}(p_i)$ (truncated at zero) is at most
$w + \mathrm{alloc}(p_1) + \cdots + \mathrm{alloc}(p_{i-1})$ componentwise. In particular
the empty list is a safe sequence from every $w$.

Thus each process in turn can be given its remaining need from what is free, finish, and
release its allocation.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.SafeSeq`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safe-seq).

## Safe state

Let $S$ be a system of claims and allocations with processes $P$ and
resource types $R$. A list of pending processes is safe from the free resource vector
$w : R \to \mathbb{N}$ when it has no repetitions and some permutation of it is a safe sequence
from $w$: the pending processes can all finish, one after another, in some order.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.Safe`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safe).

## Safe sequences are monotone in the free resources

Let $S$ be a system of processes with
maximum claims and current allocations, and let $\sigma$ be a list of processes. If $\sigma$ is a
safe sequence for $S$ from a vector $w$ of free resources (a natural number for each resource
type), and $w \le w'$ componentwise, then $\sigma$ is also a safe sequence for $S$ from $w'$.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.SafeSeq.mono`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#mono).

## Removing a process from a safe sequence

Let $S$ be a system of processes with maximum
claims and current allocations, let $w$ be a vector of free resources (a natural number for
each resource type), and let $\sigma$ be a list of processes that is a safe sequence for $S$
from $w$. If $p$ occurs in $\sigma$, then the list obtained from $\sigma$ by deleting the first
occurrence of $p$ is a safe sequence for $S$ from $w + \mathrm{alloc}(p)$, where
$\mathrm{alloc}(p)$ is the current allocation of $p$ and the sum is taken componentwise.

In other words, letting a member of a safe sequence finish first and release its allocation
leaves the rest of the sequence safe. This is why the greedy safety check is complete.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.SafeSeq.erase`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#erase).

## A safe state is not deadlocked

Let $S$ be a system of processes with maximum claims and
current allocations, let $w$ be a vector of free resources (a natural number for each resource
type), and let $L$ be a nonempty list of pending processes. If $S$ is safe from $w$ for $L$, then
some process $p$ in $L$ has remaining need $\mathrm{need}(p) \le w$ componentwise, so it can be
given its whole remaining need.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.Safe.exists_runnable`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#exists-runnable).

## Letting a process that fits finish preserves safety

Let $S$ be a system of processes
with maximum claims and current allocations, $w$ a vector of free resources (a natural number
for each resource type) and $L$ a list of pending processes without repetitions. If $p$ occurs in
$L$ and its remaining need $\mathrm{need}(p)$ in $S$ satisfies $\mathrm{need}(p) \le w$
componentwise, then $S$ is safe from $w$ for $L$ if and only if $S$ is safe from
$w + \mathrm{alloc}(p)$ for the list obtained from $L$ by removing $p$, where
$\mathrm{alloc}(p)$ is the current allocation of $p$ and the sum is taken componentwise.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.safe_iff_safe_erase`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safe-iff-safe-erase).

## Banker's safety algorithm with fuel

Let $S$ be a system with processes $P$ and a
finite set $R$ of resource types, where process $p$ has maximum claim $\mathrm{claim}(p)$ and
allocation $\mathrm{alloc}(p)$ in $R \to \mathbb{N}$. Given a fuel $n \in \mathbb{N}$, a free
resource vector $w : R \to \mathbb{N}$ and a list of pending processes, the algorithm succeeds
if the list is empty. Otherwise, if $n > 0$ and some pending process $q$ has remaining need
$\mathrm{claim}(q) - \mathrm{alloc}(q)$ (truncated at zero) at most $w$ componentwise, it takes
the first such process $p$ in the list, removes that occurrence of $p$ from the list, adds
$\mathrm{alloc}(p)$ to $w$ and continues with fuel $n - 1$; if $n = 0$ or no pending process
fits, it fails.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.safetyCheckAux`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safety-check-aux).

## Banker's safety algorithm

Let $S$ be a system of claims and allocations with processes
$P$ and a finite set $R$ of resource types. Given a free resource vector $w : R \to \mathbb{N}$
and a list of pending processes, the algorithm fails if the list has a repetition. Otherwise it
runs the safety algorithm with fuel equal to the length of the list: it repeatedly lets the
first pending process whose remaining need (claim minus allocation, truncated at zero) is at
most the free resources componentwise finish and adds its allocation to the free resources,
for at most one round per pending process, and it succeeds exactly when no pending process is
left at the end.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.safetyCheck`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safety-check).

## Correctness of the safety algorithm

For every system $S$ of claims and allocations over
a finite set $R$ of resource types, every free resource vector $w : R \to \mathbb{N}$ and every
list of pending processes, the banker's safety algorithm succeeds on $w$ and the list if and
only if the list is a safe state from $w$.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.safetyCheck_iff`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#safety-check-iff).

## Granting a request

For a system $S$ of processes with maximum claims and current
allocations, a process $p$ and a resource vector $r$ (a natural number for each resource type),
the system obtained by granting $r$ to $p$ has the same maximum claims as $S$, gives $p$ the
allocation $\mathrm{alloc}(p) + r$ (componentwise sum, where $\mathrm{alloc}(p)$ is the current
allocation of $p$ in $S$), and leaves the allocation of every other process unchanged.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.grant`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#grant).

## Remaining need after a grant

For a system $S$ of processes with maximum claims and
current allocations, a process $p$ and a resource vector $r$ (a natural number for each resource
type), the remaining need of $p$ in the system obtained by granting $r$ to $p$ equals
$\mathrm{need}(p) - r$, where $\mathrm{need}(p)$ is the remaining need of $p$ in $S$ and the
subtraction is truncated subtraction of natural numbers, taken componentwise.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.need_grant_self`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#need-grant-self).

## Resource-request algorithm

Let $S$ be a system of claims and allocations with processes
$P$ and a finite set $R$ of resource types, let $a : R \to \mathbb{N}$ be the vector of free
resources, $L$ a list of pending processes, $p$ a process and $r : R \to \mathbb{N}$ the
resources that $p$ requests. The request is granted when $p$ occurs in $L$, $L$ has no
repetitions, $r \le \mathrm{need}(p)$ and $r \le a$ componentwise, where $\mathrm{need}(p)$ is
the remaining need of $p$ in $S$, and the banker's safety algorithm succeeds for the system
obtained from $S$ by granting $r$ to $p$, from the free vector $a - r$ (componentwise truncated
subtraction) and the list $L$. A granted request returns the free vector $a - r$ and that
system; otherwise the algorithm returns no result.

No result covers the error case of the textbook algorithm (a request beyond the remaining
claim), the cases where the process must wait, and malformed input (a requester that is not
pending, or a pending list with repetitions).

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.request`, a definition declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#request).

## The request algorithm grants exactly the safe requests within the claim and the free resources

**The request algorithm grants exactly the safe requests within the claim
and the free resources.** Let $S$ be a system of claims and allocations with processes $P$ and a
finite set $R$ of resource types, let $a : R \to \mathbb{N}$ be the vector of free resources, $L$
a list of pending processes, $p$ a process and $r : R \to \mathbb{N}$ the resources that $p$
requests. Write $\mathrm{need}(p)$ for the remaining need of $p$ in $S$, $T$ for the system
obtained from $S$ by granting $r$ to $p$, and $a - r$ for componentwise truncated subtraction.
The resource-request algorithm grants the request and returns the free vector $a'$ and the
system $S'$ if and only if $p$ occurs in $L$, $L$ has no repetitions, both
$r \le \mathrm{need}(p)$ and $r \le a$ hold componentwise, $T$ is safe from $a - r$ for $L$,
$a' = a - r$, and $S' = T$.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.request_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#request-eq-some-iff).

## Granted requests lead to safe states

Let $S$ be a system of processes with maximum
claims and current allocations, $a$ the vector of free resources, $L$ the list of pending
processes, $p$ a process and $r$ a resource vector. If the resource-request algorithm grants the
request of $r$ by $p$, returning the free vector $a'$ and the system $S'$, then $S'$ is safe from
$a'$ for $L$.

Formalized by `Cslib.Algorithms.Concurrency.Banker.System.request_safe`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Banker.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Concurrency/Banker.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html#request-safe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banker's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/banker-s-algorithm)
