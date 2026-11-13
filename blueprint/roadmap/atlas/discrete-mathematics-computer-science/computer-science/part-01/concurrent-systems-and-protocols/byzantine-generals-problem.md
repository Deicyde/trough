---
declaration: section
origin: cited
lean: Cslib.Distributed.Byzantine.Impossibility.OralProtocol, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.states_eq_of_inbox_eq, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState_self, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState_of_ne, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.inbox, Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state_zero
statement: formalized
proof: formalized
---

# Byzantine generals problem

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html).

## Oral-message protocol

A synchronous oral-message protocol for a set $G$ of generals, with
orders in $V$, local states in $\sigma$ and messages in $M$, consists of an initial state for
each general in $G$, used by the generals other than the commander; an initial state of the
commander for each order in $V$; a sending function giving, for each round $r$, each general $j$
in each state $s$ and each general $i$, the message in $M$ that $j$ sends to $i$ in round $r$; a
transition function giving, for each round $r$, each general $i$ in each state $s$ and each
assignment of a message to every sender $j$, the state of $i$ after round $r$; and a decision
function giving the value in $V$ that each general decides in each state.

The commander is not part of the protocol: it is chosen when the protocol is run. In each round
every general sends its messages from its current state and then moves to the state given by the
transition function on the messages it received. Only the commander's initial state depends on
the order.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol`, a structure declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#oral-protocol).

## Local views determine states

Let $P$ be an oral-message protocol for the generals $G$
with states $\sigma$ and messages $M$. Let $N$ be a type of nodes, node $k$ running the code of
the general $\rho(k) \in G$, and let $L$ be a property of nodes. For each round $r$ and node
$k$, let $s_r(k), s'_r(k) \in \sigma$ be two states and $\mu_r(k), \mu'_r(k) : G \to M$ two
families of received messages. Suppose that for every $r$ and every node $k$ satisfying $L$,
$s_{r+1}(k)$ is the state to which general $\rho(k)$ of $P$ moves in round $r$ from $s_r(k)$ on
the messages $\mu_r(k)$, and $s'_{r+1}(k)$ the one to which it moves from $s'_r(k)$ on
$\mu'_r(k)$; that $s_0(k) = s'_0(k)$ for every $k$ satisfying $L$; and that for every $r$, if
$s_r(k) = s'_r(k)$ for all $k$ satisfying $L$, then $\mu_r(k) = \mu'_r(k)$ for all $k$
satisfying $L$. Then $s_r(k) = s'_r(k)$ for every $r$ and every $k$ satisfying $L$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.states_eq_of_inbox_eq`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#states-eq-of-inbox-eq).

## Initial state of a general

When the commander $c$ has order $v$, the initial state of
general $i$ is the initial state that the protocol assigns to a commander with order $v$ if
$i = c$, and the initial state that the protocol assigns to $i$ as a general other than the
commander if $i \ne c$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#init-state).

## Initial state of the commander

When the commander $c$ has order $v$, the initial state of
$c$ is the initial state that the protocol assigns to a commander with order $v$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState_self`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#init-state-self).

## Initial state of a lieutenant

If general $i$ is not the commander $c$, then the initial
state of $i$ when $c$ has order $v$ is the initial state that the protocol assigns to $i$ as a
general other than the commander; in particular, it does not depend on $v$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.initState_of_ne`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#init-state-of-ne).

## Executions of an oral-message protocol

Let $P$ be an oral-message protocol for the
generals $G$, let $c \in G$ be the commander, $v$ its order and $S \subseteq G$ a finite set of
traitors, and let $a_r(j, i)$ be the message a traitor $j$ sends general $i$ in round $r$. The
state of general $i$ after $r$ rounds is defined by recursion on $r$. After $0$ rounds it is
the initial state of $i$ for commander $c$ and order $v$. After $r + 1$ rounds it is the state
to which $i$ moves by its code for round $r$ from its state after $r$ rounds, on receiving
$a_r(j, i)$ from each traitor $j \in S$ and, from each other general $j$, the message that $P$
has $j$ send to $i$ in round $r$ from the state of $j$ after $r$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#state).

## Messages received in a round

In the execution of a protocol $P$ with commander $c$,
order $v$, a set of traitors and a behaviour $\mathrm{adv}$ of the traitors, the messages that
general $i$ receives in round $r$ form the function of the sender $j$ whose value is
$\mathrm{adv}(r, j, i)$ if $j$ is a traitor, and otherwise the message that $P$ has $j$ send to
$i$ in round $r$ from the state of $j$ after $r$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.inbox`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#inbox).

## The start of an execution

In the execution of an oral-message protocol $P$ with
commander $c$, order $v$, any set of traitors and any traitor behaviour, every general is in
its initial state after $0$ rounds: the commander in the initial state given by the order $v$,
and every other general in its order-independent initial state.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state_zero`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#state-zero).

## One round of an execution

In the execution of an oral-message protocol $P$ with a given
commander, order, set of traitors and traitor behaviour, for every round $r$ and every general
$i$, the state of $i$ after $r + 1$ rounds is the state to which $i$ moves by its code for round
$r$ from its state after $r$ rounds on the messages it receives in round $r$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state_succ`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#state-succ).

## Decision of a general

In the execution of a protocol $P$ with commander $c$, order $v$, a
set of traitors and a behaviour of the traitors, the decision of general $i$ after $T$ rounds is
the value that the decision function of $P$ assigns to $i$ in its state after $T$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.decision`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#decision).

## Agreement condition (IC1)

Consider the execution of a protocol $P$ with commander $c$,
order $v$, a set of traitors and a behaviour of the traitors. Condition IC1 holds after $T$
rounds when any two generals $i$ and $j$, neither of which is the commander or a traitor, decide
the same value after $T$ rounds of this execution.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.Agreement`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#agreement).

## Validity in the Byzantine generals problem

In the execution of an oral-message protocol
with commander $c$, order $v$, a set of traitors and a traitor behaviour, condition IC2
(validity) holds after $T$ rounds if, provided the commander is loyal, every loyal general
other than the commander decides $v$ after $T$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.Validity`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#validity).

## Solving the Byzantine generals problem

An oral-message protocol $P$ for the generals
$G$ solves the Byzantine generals problem with commander $c \in G$ and at most $m$ traitors in
$T$ rounds if, for every order $v$, every set of at most $m$ traitors and every behaviour of
the traitors (the message each traitor sends to each general in each round), conditions IC1
(agreement) and IC2 (validity) hold after $T$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.Solves`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#solves).

## No protocol for three generals tolerates one traitor

Suppose there are at least two
possible orders. For every oral-message protocol for three generals $0$, $1$, $2$ with commander
$0$ and every number of rounds $T$, there are an order $v$, a general $t$ and a behaviour of $t$
such that, in the execution with order $v$ in which $t$ is the only traitor, the agreement
condition (IC1) or the validity condition (IC2) fails after $T$ rounds.

This is the theorem of Pease, Shostak and Lamport, proved here by a commander version of the
hexagon argument of Fischer, Lynch and Merritt.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.exists_violation_three`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#exists-violation-three).

## No protocol for three generals solves the Byzantine generals problem with one traitor

**No protocol for three generals solves the Byzantine generals problem with one
traitor.** Suppose there are at least two possible orders. For every oral-message protocol for
three generals $0$, $1$, $2$ with commander $0$ and every number of rounds $T$, the protocol does
not solve the Byzantine generals problem with commander $0$ and at most one traitor in $T$
rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.not_solves_three`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#not-solves-three).

## Three generals simulating a protocol

Let $P$ be an oral-message protocol for the
generals $G$ with orders in $V$, states $\sigma$ and messages $M$, let $c \in G$, let
$\mathrm{grp} : G \to \{0, 1, 2\}$ split the generals into three groups and let
$\mathrm{rep} : \{0, 1, 2\} \to G$. The simulation of $P$ with $c$, $\mathrm{grp}$ and
$\mathrm{rep}$ is the oral-message protocol for the generals $\{0, 1, 2\}$ with orders in $V$,
whose states are families $(s(i))_{i \in G}$ of states of $\sigma$ and whose messages are
families $(\mu(j, i))_{j, i \in G}$ of messages of $M$, defined as follows. A general other
than the commander starts from the family of the initial states that $P$ gives each general of
$G$ as a non-commander; the commander, with order $v$, starts from the family of the initial
states of the generals of $G$ in $P$ when $c$ is the commander with order $v$. In round $r$, a
general in state $s$ sends every general the family whose entry $(j, i)$ is the message that
general $j$ of $P$, in state $s(j)$, sends to general $i$ in round $r$. In round $r$, general
$g$ in state $s$, having received $\mu_h$ from each general $h$, moves to the family that keeps
$s(i)$ for each $i$ with $\mathrm{grp}(i) \ne g$ and, for each $i$ with $\mathrm{grp}(i) = g$,
holds the state to which general $i$ of $P$ moves in round $r$ from $s(i)$ on receiving
$\mu_{\mathrm{grp}(j)}(j, i)$ from each $j \in G$. General $g$ in final state $s$ decides
what general $\mathrm{rep}(g)$ of $P$ decides in state $s(\mathrm{rep}(g))$.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.simulate`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#simulate).

## The simulation is faithful

Let $P$ be an oral-message protocol for a finite set $G$ of
generals with messages $M$, let $c \in G$, and let $\mathrm{grp} : G \to \{0, 1, 2\}$ and
$\mathrm{rep} : \{0, 1, 2\} \to G$ with $\mathrm{grp}(c) = 0$. Fix an order $v$, a set
$S \subseteq \{0, 1, 2\}$ of traitors and a traitor behaviour $a$ for the simulation of $P$
with $c$, $\mathrm{grp}$ and $\mathrm{rep}$: in round $r$ a traitor $h$ sends general $g$ the
family $(a_r(h, g)(j, i))_{j, i \in G}$ of messages of $M$. Compare the execution of the
simulation with commander $0$, order $v$, traitors $S$ and behaviour $a$ with the execution of
$P$ with commander $c$, order $v$ and traitors $\{j \in G : \mathrm{grp}(j) \in S\}$, in which
a traitor $j$ sends general $i$ the message $a_r(\mathrm{grp}(j), \mathrm{grp}(i))(j, i)$ in
round $r$. Then for every $r \in \mathbb{N}$ and every $i \in G$ with $\mathrm{grp}(i) \notin S$,
the entry at $i$ of the state of general $\mathrm{grp}(i)$ after $r$ rounds of the first
execution equals the state of general $i$ after $r$ rounds of the second.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.state_simulate`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#state-simulate).

## Simulation reduces many generals to three

Let $P$ be an oral-message protocol for a
finite set $G$ of generals, let $c \in G$ and $m, T \in \mathbb{N}$, and suppose that $P$ solves
the Byzantine generals problem with commander $c$ and at most $m$ traitors in $T$ rounds. Let
$\mathrm{grp} : G \to \{0, 1, 2\}$ and $\mathrm{rep} : \{0, 1, 2\} \to G$ satisfy
$\mathrm{grp}(c) = 0$, $\mathrm{grp}(\mathrm{rep}(g)) = g$ for every $g \ne 0$, and
$|\{i \in G : \mathrm{grp}(i) = g\}| \le m$ for every $g$. Then the simulation of $P$ with $c$,
$\mathrm{grp}$ and $\mathrm{rep}$ solves the Byzantine generals problem for the generals
$\{0, 1, 2\}$ with commander $0$ and at most one traitor in $T$ rounds.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.solves_simulate`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#solves-simulate).

## No protocol for $n$ generals tolerates $m$ traitors when $3 \le n \le 3m$

Suppose there
are at least two possible orders and the set of generals is finite with $n$ elements, where
$3 \le n \le 3m$. Then for every oral-message protocol, every commander $c$ and every number of
rounds $T$, the protocol does not solve the Byzantine generals problem with commander $c$ and at
most $m$ traitors in $T$ rounds: there are an order, a set of at most $m$ traitors and a
behaviour of the traitors for which the agreement condition (IC1) or the validity condition
(IC2) fails after $T$ rounds.

This is the theorem of Lamport, Shostak and Pease, proved by reduction to three generals.

Formalized by `Cslib.Distributed.Byzantine.Impossibility.OralProtocol.not_solves_of_card_le_three_mul`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/Impossibility.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#not-solves-of-card-le-three-mul).

## Majority of a multiset

The majority of a finite multiset $s$ of values is the value $x$
such that more than half of the elements of $s$ are equal to $x$ (counted with multiplicity),
if there is one (there is at most one), and a fixed default value (retreat) otherwise.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.majority`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#majority).

## A value filling more than half of a multiset is its majority

If more than half of the
elements of a multiset $s$ of values are equal to $x$ (counted with multiplicity), then the
majority of $s$ is $x$.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.majority_eq_of_lt_count`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#majority-eq-of-lt-count).

## Majority falls back to the default value

If, for every value $x$, at most half of the
elements of a multiset $s$ of values are equal to $x$ (counted with multiplicity), then the
majority of $s$ is the default value (retreat).

Formalized by `Cslib.Distributed.Byzantine.OralMessages.majority_eq_default`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#majority-eq-default).

## Value received from a commander

Fix a predicate saying which generals are loyal and an
adversary $\mathrm{adv}$ that assigns a value to each pair of a finite sequence of generals and a
recipient. The value that lieutenant $p$ receives from commander $c$, who holds the value $v$ and
whose superiors form the sequence $\sigma$, is $v$ if $c$ is loyal, and is
$\mathrm{adv}(\sigma c, p)$ if $c$ is a traitor, where $\sigma c$ is $\sigma$ followed by $c$.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.received`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#received).

## The oral messages algorithm

Fix which generals are loyal and a strategy for the traitors,
which assigns a value to each list of generals and each recipient. Let $c$ be a commander holding
the value $v$, let $\sigma$ be the list of the commanders above $c$, and let $S$ be a finite set
of lieutenants. For a general $q$, let $r_q$ be the value $q$ receives from $c$: $v$ if $c$ is
loyal, and otherwise the value the strategy assigns to the list $\sigma c$ ($\sigma$ followed by
$c$) and the recipient $q$. The value that a general $p$ decides under $\mathrm{OM}(m)$ is defined
by recursion on $m$. Under $\mathrm{OM}(0)$, $p$ decides $r_p$. Under $\mathrm{OM}(m + 1)$, $p$
decides the majority of the multiset of values $w_q$ for $q \in S$, where $w_p = r_p$ and, for
$q \ne p$, $w_q$ is the value $p$ decides under $\mathrm{OM}(m)$ when $q$, holding $r_q$ with the
superiors $\sigma c$, sends it to the lieutenants $S \setminus \{q\}$.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.om`, a definition declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#om).

## A loyal commander sends its value

If the commander $c$ is loyal, then for every value $v$,
every list of superiors of $c$ and every general $p$, the value $p$ receives from $c$ is $v$.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.received_of_loyal`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#received-of-loyal).

## A traitorous commander sends the adversary's value

Fix which generals are loyal and an
adversary $\mathrm{adv}$ that assigns a value to each pair of a list of generals and a recipient.
If the commander $c$ is a traitor, then for every value $v$, every list $\sigma$ of superiors of
$c$ and every general $p$, the value $p$ receives from $c$ is $\mathrm{adv}(\sigma c, p)$, where
$\sigma c$ is $\sigma$ followed by $c$.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.received_of_not_loyal`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#received-of-not-loyal).

## A loyal commander is obeyed under oral messages

Let $m$ and $k$ be natural numbers, and
let a loyal commander $c$ run $\mathrm{OM}(m)$ with a value $v$ and any list of superiors, sending
to a finite set $S$ of lieutenants. If $2k + m < |S| + 1$ (more than $2k + m$ generals when
$c \notin S$) and at most $k$ of the generals in $S \cup \{c\}$ are traitors, then, whatever the
traitors send, every loyal lieutenant $p \in S$ decides $v$.

This is Lemma 1 of Lamport–Shostak–Pease.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.om_eq_of_loyal`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#om-eq-of-loyal).

## Validity under oral messages (IC2)

Let a loyal commander $c$ run $\mathrm{OM}(m)$ with a
value $v$ and any list of superiors, sending to a finite set $S$ of lieutenants. If
$3m < |S| + 1$ (more than $3m$ generals when $c \notin S$) and at most $m$ of the generals in
$S \cup \{c\}$ are traitors, then, whatever the traitors send, every loyal lieutenant $p \in S$
decides $v$.

This is condition IC2 of Theorem 1 of Lamport–Shostak–Pease.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.om_valid`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#om-valid).

## Agreement under oral messages (IC1)

Let a commander $c$ run $\mathrm{OM}(m)$ with a value
$v$ and any list of superiors, sending to a finite set $S$ of lieutenants with $c \notin S$. If
there are more than $3m$ generals, that is $3m < |S| + 1$, and at most $m$ of the generals in
$S \cup \{c\}$ are traitors, then, whatever the traitors send, any two loyal lieutenants
$p, p' \in S$ decide the same value.

This is condition IC1 of Theorem 1 of Lamport–Shostak–Pease.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.om_agree`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#om-agree).

## Oral messages achieve interactive consistency

Let a commander $c$ run $\mathrm{OM}(m)$
with a value $v$ and any list of superiors, sending to a finite set $S$ of lieutenants with
$c \notin S$. If there are more than $3m$ generals, that is $3m < |S| + 1$, and at most $m$ of
the generals in $S \cup \{c\}$ are traitors, then, whatever the traitors send, any two loyal
lieutenants in $S$ decide the same value (IC1), and if $c$ is loyal, every loyal lieutenant in
$S$ decides $v$ (IC2).

This is Theorem 1 of Lamport–Shostak–Pease.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.om_interactive_consistency`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#om-interactive-consistency).

## The oral messages algorithm solves the Byzantine generals problem

Let $G$ be a finite set
of more than $3m$ generals, at most $m$ of whom are traitors, and let the commander $c \in G$ run
$\mathrm{OM}(m)$ with the value $v$, with no superiors and with all the other generals as
lieutenants. Then, whatever the traitors send, any two loyal lieutenants decide the same value,
and if $c$ is loyal, every loyal lieutenant decides $v$.

This is Theorem 1 of Lamport–Shostak–Pease, applied to all the generals.

Formalized by `Cslib.Distributed.Byzantine.OralMessages.byzantine_generals`, a theorem declared in [CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/Byzantine/OralMessages.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html#byzantine-generals).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Byzantine generals problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/byzantine-generals-problem)
