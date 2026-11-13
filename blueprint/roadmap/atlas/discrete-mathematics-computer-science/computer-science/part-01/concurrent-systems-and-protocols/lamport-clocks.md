---
declaration: section
origin: cited
lean: Cslib.Distributed.LamportClock.Event, Cslib.Distributed.LamportClock.WellFormed, Cslib.Distributed.LamportClock.Step, Cslib.Distributed.LamportClock.HappensBefore, Cslib.Distributed.LamportClock.HappensBefore.lt, Cslib.Distributed.LamportClock.clockStep, Cslib.Distributed.LamportClock.run, Cslib.Distributed.LamportClock.timestamps
statement: formalized
proof: formalized
---

# Lamport clocks

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html).

## Event

An event of an execution, for a type $P$ of processes, consists of the process
in $P$ it belongs to and, if it is a receipt, a natural number: the position in the execution
of the event whose message it receives. The structure does not require that position to be
earlier than the event itself.

Formalized by `Cslib.Distributed.LamportClock.Event`, a structure declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#event).

## Well-formed executions

An execution $e_0, \dots, e_{n-1}$ is well formed when every
receipt names an earlier event: whenever $e_j$ receives the message sent by the event at
position $i$, then $i < j$.

Formalized by `Cslib.Distributed.LamportClock.WellFormed`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#well-formed).

## One step of happened-before

In an execution, position $i$ precedes position $j$ by one
step when $i < j$, both positions hold events, and either the two events belong to the same
process or the event at $j$ receives the message of the event at $i$.

Formalized by `Cslib.Distributed.LamportClock.Step`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#step).

## Happened-before

Lamport's happened-before relation on the positions of an execution is
the transitive closure of one step of happened-before: $a$ happened before $b$ when there is a
chain $a = i_0, i_1, \dots, i_k = b$ with $k \ge 1$ in which each $i_m$ precedes $i_{m+1}$ by
one step.

Formalized by `Cslib.Distributed.LamportClock.HappensBefore`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#happens-before).

## Happened-before goes forward in the execution

If position $a$ happened before position
$b$ in an execution, then $a < b$.

Formalized by `Cslib.Distributed.LamportClock.HappensBefore.lt`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#lt).

## One step of the Lamport clock algorithm

The state is a counter $c(p) \in \mathbb{N}$
for each process $p$ together with the timestamps assigned so far. An event $e$ of process
$p$ gets the timestamp $t = \max(c(p), s) + 1$, where $s$ is the timestamp already assigned
at the position that $e$ receives from; $s = 0$ if $e$ is not a receipt or if no timestamp
has been assigned at that position. The step sets $c(p)$ to $t$ and appends $t$ to the
timestamps.

The timestamps are kept in an array, for constant-time append and lookup.

Formalized by `Cslib.Distributed.LamportClock.clockStep`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#clock-step).

## Running the Lamport clock algorithm

The clock algorithm over an execution applies one
step of the algorithm to each event in order, starting from all process counters $0$ and no
timestamps. The result is the final counters together with the timestamps assigned to the
events, in order.

Formalized by `Cslib.Distributed.LamportClock.run`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#run).

## Lamport timestamps

The Lamport timestamps $t_0, \dots, t_{n-1}$ of an execution
$e_0, \dots, e_{n-1}$ are computed by Lamport's clock algorithm. Every process keeps a
counter, initially $0$. For $k = 0, \dots, n-1$ in turn, let $c$ be the current counter of
the process of $e_k$, and let $m = t_i$ if $e_k$ receives the message sent by the event at
position $i$ with $i < k$, and $m = 0$ otherwise. Then $t_k = \max(c, m) + 1$, and the
counter of the process of $e_k$ is set to $t_k$.

Formalized by `Cslib.Distributed.LamportClock.timestamps`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamps).

## Appending events does not change earlier timestamps

Let $e_0, \dots, e_{n-1}$ be an
execution, and extend it by appending further events. For every $i < n$, the Lamport timestamp
of the event at position $i$ is the same in the extended execution as in the original one.

Formalized by `Cslib.Distributed.LamportClock.timestamps_append`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamps-append).

## Process counters dominate their timestamps

After the Lamport clock algorithm has run
over an execution, the counter of each process is at least the timestamp of every event of that
process in the execution.

Formalized by `Cslib.Distributed.LamportClock.timestamp_le_clock`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamp-le-clock).

## A timestamp depends only on a prefix containing its event

Let $e_0, \dots, e_{n-1}$ be
an execution and let $i < k \le n$. The Lamport timestamp of $e_i$ in the whole execution equals
its Lamport timestamp in the prefix $e_0, \dots, e_{k-1}$.

Formalized by `Cslib.Distributed.LamportClock.timestamps_getD_take`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamps-get-d-take).

## One step of happened-before raises the timestamp

If position $i$ precedes position $j$
by one step of happened-before in an execution, then the Lamport timestamp of $i$ is smaller
than the Lamport timestamp of $j$.

Formalized by `Cslib.Distributed.LamportClock.step_lt`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#step-lt).

## A receipt is stamped later than its send

Let $e_0, \dots, e_{n-1}$ be a well-formed
execution and let $t_k$ be the Lamport timestamp of $e_k$. If $j < n$ and $e_j$ receives the
message sent by the event at position $i$, then $t_i < t_j$.

This is Lamport's clock condition C2, which his implementation rule IR2 guarantees.

Formalized by `Cslib.Distributed.LamportClock.timestamp_lt_of_recv`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamp-lt-of-recv).

## Lamport timestamps increase along each process

Let $e_0, \dots, e_{n-1}$ be an
execution and let $t_k$ be the Lamport timestamp of $e_k$. If $i < j < n$ and $e_i$ and $e_j$
belong to the same process, then $t_i < t_j$.

This is Lamport's clock condition C1, which his implementation rule IR1 guarantees.

Formalized by `Cslib.Distributed.LamportClock.timestamp_lt_of_proc`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#timestamp-lt-of-proc).

## The clock condition

In every execution, if the event at position $a$ happened before
the event at position $b$, then the Lamport timestamp of $a$ is smaller than the Lamport
timestamp of $b$ (Lamport 1978).

Formalized by `Cslib.Distributed.LamportClock.clock_condition`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#clock-condition).

## Happened-before relates positions of the execution

If position $a$ happened before
position $b$ in an execution, then the execution has an event at position $a$ and an event at
position $b$.

Formalized by `Cslib.Distributed.LamportClock.HappensBefore.exists_events`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#exists-events).

## Lamport's total order

Fix a linear order on the processes. In an execution
$e_0, \dots, e_{n-1}$ with Lamport timestamps $t_0, \dots, t_{n-1}$, position $a$ precedes
position $b$ when $a < n$, $b < n$, and either $t_a < t_b$, or $t_a = t_b$ and the process of
$e_a$ is smaller than the process of $e_b$.

Formalized by `Cslib.Distributed.LamportClock.TotalBefore`, a definition declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#total-before).

## Lamport's total order extends happened-before

In every execution, if the event at
position $a$ happened before the event at position $b$, then position $a$ precedes position $b$
in Lamport's total order.

Formalized by `Cslib.Distributed.LamportClock.totalBefore_of_happensBefore`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#total-before-of-happens-before).

## Lamport's order is total

In every execution, for any two distinct positions $a \ne b$
that both hold events, $a$ precedes $b$ or $b$ precedes $a$ in Lamport's total order.

Two events of the same process have different timestamps (an earlier event of a process has
a smaller timestamp), so ties only occur between different processes, which the order on
processes breaks.

Formalized by `Cslib.Distributed.LamportClock.totalBefore_total`, a theorem declared in [CSLibExt/Computability/Distributed/LamportClock.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/LamportClock.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html#total-before-total).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lamport clocks](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/lamport-clocks)
