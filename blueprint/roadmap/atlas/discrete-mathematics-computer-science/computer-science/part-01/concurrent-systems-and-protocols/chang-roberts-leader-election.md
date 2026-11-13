---
declaration: section
origin: cited
lean: Cslib.Distributed.ChangRoberts.State, Cslib.Distributed.ChangRoberts.succ, Cslib.Distributed.ChangRoberts.pred, Cslib.Distributed.ChangRoberts.deliver, Cslib.Distributed.ChangRoberts.lts, Cslib.Distributed.ChangRoberts.initial, Cslib.Distributed.ChangRoberts.Reachable, Cslib.Distributed.ChangRoberts.gap
statement: formalized
proof: formalized
---

# Chang–Roberts leader election

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html).

## Chang–Roberts global states

For a ring of $n + 1$ processes $0, \dots, n$, a global
state assigns to each process $k$ the FIFO channel of messages waiting at $k$, oldest first,
where each message is the index of the process whose identifier it carries, and records for
each process whether it has declared itself leader.

Formalized by `Cslib.Distributed.ChangRoberts.State`, a structure declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#state).

## Successor on the Chang–Roberts ring

On the ring of $n + 1$ processes $0, \dots, n$, the
successor of process $k$ is $k + 1$ when $k < n$, and $0$ when $k = n$.

Formalized by `Cslib.Distributed.ChangRoberts.succ`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#succ).

## Predecessor on the ring

On a ring of $n + 1$ processes numbered $0, \dots, n$, the
predecessor of $k$ is $k - 1$ if $k \ne 0$, and $n$ if $k = 0$.

Formalized by `Cslib.Distributed.ChangRoberts.pred`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#pred).

## Delivering a message in the Chang–Roberts ring

On a ring of $n + 1$ processes with
identifiers $\mathrm{id}$, process $k$ receives the oldest message in its channel in state $s$.
If the channel of $k$ is empty there is no step. Otherwise let $j$ be the origin of that message,
which is removed from the channel: if $\mathrm{id}(k) < \mathrm{id}(j)$, process $k$ forwards it
by appending $j$ to the end of the channel of its successor on the ring; otherwise, if $j = k$,
process $k$ declares itself leader; otherwise the message is discarded. Nothing else changes.

Formalized by `Cslib.Distributed.ChangRoberts.deliver`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#deliver).

## The Chang–Roberts transition system

For identifiers $\mathrm{id}$, the algorithm is the
labelled transition system whose states are the global states and whose labels are processes:
there is a transition from $s$ to $t$ labelled $k$ exactly when delivering the oldest message in
the channel of process $k$ in state $s$ gives $t$.

Formalized by `Cslib.Distributed.ChangRoberts.lts`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#lts).

## Initial state of the Chang–Roberts ring

In the initial state the channel into each
process $k$ holds exactly one message, whose origin is the predecessor of $k$ on the ring (so
every process has sent its identifier to its successor), and no process is leader.

Formalized by `Cslib.Distributed.ChangRoberts.initial`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#initial).

## Reachable states of Chang–Roberts

Given a natural-number identifier $\mathrm{id}(k)$ for
each process $k$ of the ring of $n + 1$ processes, a global state $s$ is reachable when the
Chang–Roberts transition system with these identifiers leads from the initial state to $s$ by a
multistep transition along some finite list of labels, that is, of receiving processes.

Formalized by `Cslib.Distributed.ChangRoberts.Reachable`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#reachable).

## Forward distance on the ring

For processes $j$ and $m$ on a ring of $n + 1$ processes
numbered $0, \dots, n$, the gap from $j$ to $m$ is the number of successor steps from $j$ to
$m$: it is $m - j$ if $j \le m$, and $m + (n + 1) - j$ otherwise. It lies in $[0, n]$.

Formalized by `Cslib.Distributed.ChangRoberts.gap`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#gap).

## Distance travelled by a message

For processes $j, k$ of the ring of $n + 1$ processes,
the distance travelled by a message from $j$ waiting at $k$ is $n + 1$, the whole ring, when
$k = j$, and otherwise the ring distance from $j$ to $k$, the number of links from $j$ forward
to $k$.

Formalized by `Cslib.Distributed.ChangRoberts.travelled`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#travelled).

## The Chang–Roberts invariant

Given identifiers $\mathrm{id}$ on a ring of $n + 1$
processes, a state satisfies the invariant when two conditions hold. First, for every message
from origin $j$ waiting in the channel of process $k$, every process $m \ne j$ that the message
has already passed has a smaller identifier, $\mathrm{id}(m) < \mathrm{id}(j)$; here $m$ has been
passed when its forward distance from $j$ is less than the distance the message has travelled,
which is the forward distance from $j$ to $k$ if $k \ne j$, and $n + 1$ (the whole ring) if
$k = j$. Second, for every leader $i$ and every process $m \ne i$, we have
$\mathrm{id}(m) < \mathrm{id}(i)$.

Formalized by `Cslib.Distributed.ChangRoberts.Inv`, a structure declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#inv).

## Forwarding adds one link

For processes $j$ and $k$ of the ring with $k \ne j$, the
distance travelled by a message from $j$ waiting at the successor of $k$ is the number of links
from $j$ forward to $k$, plus one.

Formalized by `Cslib.Distributed.ChangRoberts.travelled_succ`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#travelled-succ).

## The initial messages have travelled one link

For every process $k$ of the ring, the
distance travelled by a message from the predecessor of $k$ waiting at $k$ is $1$.

Formalized by `Cslib.Distributed.ChangRoberts.travelled_pred`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#travelled-pred).

## The Chang–Roberts invariant is preserved along runs

For every assignment of identifiers,
if the invariant holds in a state $s$ and the state $t$ is reached from $s$ by delivering messages
along some schedule of receiving processes (a multistep transition of the algorithm's labelled
transition system), then the invariant holds in $t$.

Formalized by `Cslib.Distributed.ChangRoberts.inv_mtr`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#inv-mtr).

## The Chang–Roberts invariant holds in every reachable state

For every assignment of
identifiers, every state reachable from the initial state satisfies the invariant.

Formalized by `Cslib.Distributed.ChangRoberts.inv_reachable`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#inv-reachable).

## Only the maximum is elected

Let $\mathrm{id}$ assign a natural-number identifier, not
necessarily distinct, to each process $0, \dots, n$ of the Chang–Roberts ring. In every state
reachable with these identifiers, if process $i$ has declared itself leader, then
$\mathrm{id}(m) < \mathrm{id}(i)$ for every process $m \ne i$.

Formalized by `Cslib.Distributed.ChangRoberts.leader_max`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#leader-max).

## There is at most one leader

In every state of the Chang–Roberts algorithm reachable from
the initial state, any two processes that have declared themselves leader are equal.

Formalized by `Cslib.Distributed.ChangRoberts.leader_unique`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#leader-unique).

## Running a delivery schedule

Given a natural-number identifier $\mathrm{id}(k)$ for each
process $k$ of the ring, a global state $s$ and a list $k_1, \dots, k_r$ of processes, the run
applies the Chang–Roberts delivery step at $k_1$, then at $k_2$, and so on. It returns the final
state, or no state as soon as some $k_i$ has an empty channel at its turn; on the empty list it
returns $s$.

Formalized by `Cslib.Distributed.ChangRoberts.run`, a definition declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#run).

## Runs are multistep transitions

Given a natural-number identifier $\mathrm{id}(k)$ for
each process $k$ of the ring, for all global states $s, t$ and every list $\kappa$ of processes,
running the schedule $\kappa$ from $s$ returns $t$ if and only if the Chang–Roberts transition
system with identifiers $\mathrm{id}$ has a multistep transition from $s$ to $t$ labelled by
$\kappa$.

Formalized by `Cslib.Distributed.ChangRoberts.run_eq_some_iff`, a theorem declared in [CSLibExt/Computability/Distributed/ChangRoberts.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/ChangRoberts.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html#run-eq-some-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chang–Roberts leader election](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/chang-roberts-leader-election)
