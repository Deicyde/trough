---
declaration: section
origin: cited
lean: Cslib.Distributed.VectorClock.stamp, Cslib.Distributed.VectorClock.clockStep, Cslib.Distributed.VectorClock.run, Cslib.Distributed.VectorClock.timestamps, Cslib.Distributed.VectorClock.run_getD, Cslib.Distributed.VectorClock.timestamps_getD_eq_stamp, Cslib.Distributed.VectorClock.timestamp_le_vector, Cslib.Distributed.VectorClock.vector_eq
statement: formalized
proof: formalized
---

# Vector clocks

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html).

## Vector clock stamp of an event

Let $P$ be the set of processes. Given the current
vectors $V_q \in \mathbb{N}^P$ of the processes $q$ and the timestamps $T_0, T_1, \dots$ assigned
so far, the vector clock algorithm stamps an event $e$ of process $p$ as follows. Let $m = T_i$
if $e$ receives the message sent by the event at position $i$ and $T_i$ has been assigned, and
$m = 0$ otherwise. The stamp of $e$ is the pointwise maximum of $V_p$ and $m$, with its $p$-entry
increased by $1$.

Formalized by `Cslib.Distributed.VectorClock.stamp`, a definition declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#stamp).

## One step of the vector clock algorithm

The state of the algorithm holds a vector
$V_q \in \mathbb{N}^P$ for each process $q$, where $P$ is the set of processes, and the
timestamps assigned so far, kept in an array for constant-time append and lookup. On an event $e$
of process $p$, the step replaces $V_p$ by the stamp $s$ of $e$ computed from the current state,
leaves the other vectors unchanged, and appends $s$ to the timestamps.

Formalized by `Cslib.Distributed.VectorClock.clockStep`, a definition declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#clock-step).

## Running the vector clock algorithm

The state of the vector clock algorithm after an
execution is obtained by starting from the state in which every process's vector is $0$ and no
timestamps have been assigned, and applying one step of the algorithm to each event of the
execution in order.

Formalized by `Cslib.Distributed.VectorClock.run`, a definition declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#run).

## Vector timestamps of an execution

The vector timestamps of an execution are the list of
vectors that the vector clock algorithm, run over the execution, assigns to its events, in
order.

Formalized by `Cslib.Distributed.VectorClock.timestamps`, a definition declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#timestamps).

## Array lookup agrees with the timestamp list

For every execution and every natural
number $i$, the entry at index $i$ of the array of timestamps built by the vector clock algorithm
on the execution equals the $i$-th vector timestamp of the execution, where an index out of range
gives the zero vector in both lookups.

Formalized by `Cslib.Distributed.VectorClock.run_getD`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#run-get-d).

## Timestamps are stamps from the preceding state

For every execution and every position
$j$ of an event $e$ of it, the vector timestamp of $j$ equals the stamp of $e$ computed from the
state of the vector clock algorithm after the first $j$ events of the execution.

Formalized by `Cslib.Distributed.VectorClock.timestamps_getD_eq_stamp`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#timestamps-get-d-eq-stamp).

## Each process's vector dominates its events' timestamps

For every execution and every
position $i$ of an event of it, the vector timestamp of $i$ is pointwise at most the vector of
that event's process in the state of the vector clock algorithm after the whole execution.

Formalized by `Cslib.Distributed.VectorClock.timestamp_le_vector`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#timestamp-le-vector).

## A process's final vector is zero or one of its timestamps

Run the vector clock
algorithm over an execution, starting from all vectors $0$. For every process $p$, the vector
held by $p$ at the end is either the zero vector or the vector timestamp of some event of $p$
in the execution.

Formalized by `Cslib.Distributed.VectorClock.vector_eq`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#vector-eq).

## An event's own entry is positive

For every position $j$ of an event of an execution, if
$p$ is the process of that event, then the $p$-entry of the vector timestamp of $j$ is at least
$1$.

Formalized by `Cslib.Distributed.VectorClock.one_le_own`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#one-le-own).

## Vector timestamps are monotone along one step of happened-before

In an execution,
write $V_i$ for the vector timestamp that the vector clock algorithm gives to the event at
position $i$. If the event at position $j$ follows the event at position $i$ by one step of
happened-before, then $V_i(q) \le V_j(q)$ for every process $q$.

Formalized by `Cslib.Distributed.VectorClock.vectorClock_le_of_step`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#vector-clock-le-of-step).

## Vector timestamps are monotone along happened-before

In an execution, write $V_i$ for
the vector timestamp that the vector clock algorithm gives to the event at position $i$. If the
event at position $a$ happened before the event at position $b$, then $V_a(q) \le V_b(q)$ for
every process $q$.

Formalized by `Cslib.Distributed.VectorClock.vectorClock_le_of_happensBefore`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#vector-clock-le-of-happens-before).

## Own-entry comparison detects happened-before

Let $a$ and $b$ be positions of events of
an execution, and let $p$ be the process of the event at $a$. If the $p$-entry of the vector
timestamp of $a$ is at most the $p$-entry of the vector timestamp of $b$, then $a = b$ or $a$
happened before $b$.

Formalized by `Cslib.Distributed.VectorClock.eq_or_happensBefore_of_le`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#eq-or-happens-before-of-le).

## Vector clocks characterize happened-before

For two events of an
execution, `a` happened before `b` exactly when `a`'s timestamp is smaller than
`b`'s in the pointwise order.

Formalized by `Cslib.Distributed.VectorClock.happensBefore_iff_lt`, a theorem declared in [CSLibExt/Computability/Distributed/VectorClock.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/VectorClock.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html#happens-before-iff-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vector clocks](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/vector-clocks)
