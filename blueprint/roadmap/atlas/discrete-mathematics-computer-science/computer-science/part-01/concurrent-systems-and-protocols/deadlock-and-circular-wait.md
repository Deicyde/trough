---
declaration: section
origin: cited
lean: Cslib.Algorithms.Concurrency.Deadlock.AllocState, Cslib.Algorithms.Concurrency.Deadlock.AllocState.WaitsFor, Cslib.Algorithms.Concurrency.Deadlock.AllocState.Deadlocked, Cslib.Algorithms.Concurrency.Deadlock.AllocState.CircularWait, Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_waitsFor_self, Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_waitsFor_of_free, Cslib.Algorithms.Concurrency.Deadlock.AllocState.exists_deadlocked_of_circularWait, Cslib.Algorithms.Concurrency.Deadlock.AllocState.circularWait_of_deadlocked
statement: formalized
proof: formalized
---

# Deadlock and circular wait

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html).

## Deadlock

## Resource-allocation snapshot

A resource-allocation snapshot, for a type $P$ of
processes and a type $R$ of resources, records for each resource the process holding it, if
any (so each resource has at most one holder), and for each process $p$ and resource $r$
whether $p$ has an outstanding request for $r$. A process never requests a resource it holds.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState`, a structure declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#alloc-state).

## Wait-for relation

In a resource-allocation snapshot $s$, a process $p$ waits for a
process $q$ when there is a resource $r$ that $p$ requests in $s$ and that $q$ holds in $s$.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.WaitsFor`, a definition declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#waits-for).

## Deadlocked set of processes

In a resource-allocation snapshot $s$, a set $D$ of
processes is deadlocked when $D$ is nonempty and every process $p \in D$ waits in $s$ for some
process $q \in D$, that is, $p$ requests in $s$ a resource that $q$ holds in $s$.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.Deadlocked`, a definition declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#deadlocked).

## Circular wait

A resource-allocation snapshot $s$ has circular wait when some process $p$
waits for itself through a chain of one or more wait-for edges in $s$, that is, there are
processes $p = p_0, p_1, \dots, p_k = p$ with $k \ge 1$ such that $p_{i-1}$ waits for $p_i$ in
$s$ for each $1 \le i \le k$.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.CircularWait`, a definition declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#circular-wait).

## No process waits for itself directly

In a resource-allocation snapshot, no process $p$
waits for itself, that is, there is no resource that $p$ both requests and holds.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_waitsFor_self`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#not-waits-for-self).

## A process whose requests are all free waits for no one

In a resource-allocation
snapshot, if no resource requested by a process $p$ has a holder, then $p$ waits for no
process $q$.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_waitsFor_of_free`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#not-waits-for-of-free).

## Circular wait yields a deadlocked set

If a resource-allocation snapshot has
circular wait, that is, some process $p$ waits for itself through a chain of one or more
wait-for edges, then some set of processes is deadlocked.

One such set consists of the processes on a wait-for cycle through $p$.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.exists_deadlocked_of_circularWait`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#exists-deadlocked-of-circular-wait).

## A deadlocked set forces circular wait

In a resource-allocation snapshot with
finitely many processes, if some set of processes is deadlocked, then the snapshot has circular
wait: some process waits for itself through a chain of one or more wait-for edges.

The proof follows wait-for edges inside the deadlocked set; by finiteness it must revisit a
process.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.circularWait_of_deadlocked`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#circular-wait-of-deadlocked).

## Deadlock is circular wait

In a resource-allocation snapshot with finitely many
processes, some set of processes is deadlocked if and only if the snapshot has circular wait,
that is, some process waits for itself through a chain of one or more wait-for edges.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.deadlock_iff_circularWait`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#deadlock-iff-circular-wait).

## Havender's resource ordering

Let $s$ be a resource-allocation snapshot and let
$\mathrm{rank}$ assign a natural number to each resource. The snapshot $s$ is ordered by
$\mathrm{rank}$ when, for every process $p$, every resource $r$ that $p$ requests in $s$ and
every resource $r'$ that $p$ holds in $s$, we have $\mathrm{rank}(r') < \mathrm{rank}(r)$:
each process requests only resources ranked strictly above every resource it holds.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.Ordered`, a definition declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#ordered).

## Resource ordering prevents circular wait

Let $\mathrm{rank}$ assign a natural number
to each resource. If a resource-allocation snapshot is ordered by $\mathrm{rank}$ (Havender's
discipline), that is, $\mathrm{rank}(r') < \mathrm{rank}(r)$ whenever some process requests
$r$ and holds $r'$, then the snapshot has no circular wait: no process waits for itself
through a chain of one or more wait-for edges.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_circularWait_of_ordered`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#not-circular-wait-of-ordered).

## Resource ordering prevents deadlock

Let $\mathrm{rank}$ assign a natural number to
each resource. If a resource-allocation snapshot with finitely many processes is ordered by
$\mathrm{rank}$ (Havender's discipline), that is, $\mathrm{rank}(r') < \mathrm{rank}(r)$
whenever some process requests $r$ and holds $r'$, then no set of processes is deadlocked.

Formalized by `Cslib.Algorithms.Concurrency.Deadlock.AllocState.not_deadlocked_of_ordered`, a theorem declared in [CSLibExt/Algorithms/Concurrency/Deadlock.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/Deadlock.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html#not-deadlocked-of-ordered).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deadlock and circular wait](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/deadlock-and-circular-wait)
