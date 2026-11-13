---
declaration: section
origin: cited
lean: Cslib.Algorithms.Concurrency.DiningPhilosophers.State, Cslib.Algorithms.Concurrency.DiningPhilosophers.phase, Cslib.Algorithms.Concurrency.DiningPhilosophers.setPhase, Cslib.Algorithms.Concurrency.DiningPhilosophers.Protocol, Cslib.Algorithms.Concurrency.DiningPhilosophers.held, Cslib.Algorithms.Concurrency.DiningPhilosophers.canMove, Cslib.Algorithms.Concurrency.DiningPhilosophers.move, Cslib.Algorithms.Concurrency.DiningPhilosophers.lts
statement: formalized
proof: formalized
---

# Dining philosophers problem

32 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html).

## Dining-philosophers state

A state of the three dining philosophers is a triple
$(s_0, s_1, s_2)$ with each $s_i \in \{0, 1, 2\}$ the phase of philosopher $i$: $0$ thinking,
$1$ holding the first fork, $2$ eating (holding both forks).

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.State`, an abbreviation declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#state).

## Phase of a philosopher

For a state $s = (s_0, s_1, s_2)$ of the three dining
philosophers and a philosopher $i \in \{0, 1, 2\}$, the phase of philosopher $i$ in $s$ is the
component $s_i$.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.phase`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#phase).

## Updating the phase of a philosopher

For a state $s = (s_0, s_1, s_2)$ of the three
dining philosophers, a philosopher $i \in \{0, 1, 2\}$ and a phase $p \in \{0, 1, 2\}$, setting
the phase of philosopher $i$ to $p$ gives the state obtained from $s$ by replacing the
component $s_i$ by $p$ and keeping the other two components.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.setPhase`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#set-phase).

## Dining-philosophers protocol

A protocol for three philosophers $i \in \{0, 1, 2\}$
sitting between forks $0, 1, 2$ consists of two maps $\mathrm{first}, \mathrm{second}$ from
$\{0, 1, 2\}$ to itself, the fork philosopher $i$ picks up first and the one it picks up
second, such that for every $i$ these are its two neighbouring forks $i$ and $i + 1$
(modulo $3$) in some order: either $\mathrm{first}(i) = i$ and $\mathrm{second}(i) = i + 1$,
or $\mathrm{first}(i) = i + 1$ and $\mathrm{second}(i) = i$.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.Protocol`, a structure declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#protocol).

## Held forks

Given a protocol and a state, fork $f$ is held exactly when some philosopher
$i$ either has $f$ as its first fork and is in phase $1$ or $2$, or has $f$ as its second fork
and is in phase $2$ (eating).

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.held`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#held).

## When a philosopher can move

Given a protocol and a state, philosopher $i$ can move
exactly when it is thinking (phase $0$) and its first fork is not held by any philosopher, or it
holds its first fork (phase $1$) and its second fork is not held by any philosopher, or it is
eating (phase $2$), in which case its move puts both forks down.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.canMove`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#can-move).

## Move of a philosopher

The state obtained from $s$ when philosopher $i$ moves: the phase
of $i$ advances from thinking ($0$) to holding its first fork ($1$), from $1$ to eating ($2$),
and from eating back to thinking; the phases of the other philosophers are unchanged. Whether
the move is allowed is not checked here.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.move`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#move).

## Transition system of a dining-philosophers protocol

For a protocol $P$, the labelled
transition system on the states whose labels are the philosophers: there is a transition from
$s$ to $t$ labelled $i$ exactly when philosopher $i$ can move in $s$ under $P$ and $t$ is the
state obtained from $s$ by the move of philosopher $i$.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.lts`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#lts).

## The eating valuation

The valuation of the atoms $i \in \{0, 1, 2\}$ on the states of the
dining philosophers: atom $i$ holds at a state exactly when philosopher $i$ is eating there, that
is, when its phase is $2$.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.eating`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#eating).

## Initial state of the dining philosophers

The state in which all three philosophers are
thinking, that is, every phase is $0$.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.initial`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#initial).

## Naive dining-philosophers protocol

The protocol in which every philosopher
$i \in \{0, 1, 2\}$ picks up fork $i$ (its left fork) first and fork $i + 1$ (modulo $3$) second.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.naive`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#naive).

## Resource-ordered dining-philosophers protocol

The protocol in which every philosopher
$i \in \{0, 1, 2\}$ picks up the lower-numbered of its two forks $i$ and $i + 1$ (modulo $3$)
first and the higher-numbered one second: philosophers $0$ and $1$ take fork $i$ first, and
philosopher $2$ takes fork $0$ first and fork $2$ second.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.ordered`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#ordered).

## The deadlock formula

The CTL formula $\neg\,\mathsf{EX}\,\top$ over the philosophers as
atoms. It holds at a state exactly when the state has no successor; in the transition system of
a protocol, exactly when no philosopher can move.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.deadlock`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#deadlock).

## Neighbours-apart formula

For a philosopher $i \in \{0, 1, 2\}$, the CTL formula
$\neg(p_i \wedge p_{i+1})$ over the atoms $p_0, p_1, p_2$ (one per philosopher), with indices
modulo $3$. Under the valuation in which $p_j$ holds when philosopher $j$ eats, it says that the
neighbouring philosophers $i$ and $i + 1$ do not eat at the same time.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.neighboursApart`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#neighbours-apart).

## The naive protocol can deadlock

Consider the transition system of the naive protocol, in
which every philosopher $i$ picks up fork $i$ first and fork $i + 1$ second (indices modulo $3$),
with atom $i$ read as "philosopher $i$ is eating". Its initial state, where all philosophers are
thinking, satisfies the CTL formula $\mathsf{EF}$ applied to the deadlock formula: from it, a
state in which no philosopher can move is reachable.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.naive_deadlock_reachable`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#naive-deadlock-reachable).

## A deadlock state of the naive protocol

In the transition system of the naive protocol,
with atom $i$ read as "philosopher $i$ is eating", the state in which every philosopher holds its
first fork (every phase is $1$) satisfies the deadlock formula: no philosopher can move there.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.naive_deadlock_state`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#naive-deadlock-state).

## Resource ordering prevents deadlock for the dining philosophers

In the transition
system of the three dining philosophers under the resource-ordered protocol, the initial state,
in which everybody thinks, satisfies the CTL formula $\mathrm{AG}\,\mathrm{EX}\,\top$: every
state reachable from it has a successor, that is, some philosopher can move.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.ordered_deadlock_free`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#ordered-deadlock-free).

## Every philosopher can still eat under resource ordering

In the transition system of
the three dining philosophers under the resource-ordered protocol, with the atom $p_j$ holding
when philosopher $j$ eats, the initial state, in which everybody thinks, satisfies the CTL
formula $\mathrm{AG}\,\mathrm{EF}\,p_i$ for every philosopher $i \in \{0, 1, 2\}$: from every
state reachable from the initial state, some state in which philosopher $i$ eats is reachable.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.ordered_can_eat`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#ordered-can-eat).

## Mutual exclusion under the naive protocol

For every philosopher $i$, in the transition
system of the naive protocol, with atom $j$ read as "philosopher $j$ is eating", the initial
state satisfies $\mathsf{AG}$ applied to the formula that philosophers $i$ and $i + 1$ (indices
modulo $3$) do not both eat: in no state reachable from the initial state, where all
philosophers are thinking, are philosophers $i$ and $i + 1$ both eating.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.naive_mutex`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#naive-mutex).

## Neighbours never eat together under resource ordering

In the transition system of the
three dining philosophers under the resource-ordered protocol, with the atom $p_j$ holding when
philosopher $j$ eats, the initial state, in which everybody thinks, satisfies the CTL formula
$\mathrm{AG}\,\neg(p_i \wedge p_{i+1})$ for every philosopher $i \in \{0, 1, 2\}$, with indices
modulo $3$: in no state reachable from the initial state do philosophers $i$ and $i + 1$ both
eat.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.ordered_mutex`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophers.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#ordered-mutex).

## Enabled moves under atomic acquisition

Philosopher $i$ can move in state $s$ when it
thinks and neither of its forks $i$ and $i + 1$ (modulo $3$) is held in $s$, or when it eats
(it then puts both forks down); a philosopher holding only its first fork cannot move. A fork
is held as in the naive protocol: philosopher $j$ holds fork $j$ when it holds its first fork
or eats, and holds fork $j + 1$ when it eats.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.canMoveAtomic`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#can-move-atomic).

## Move of a philosopher under atomic acquisition

In a state $s$ (the phases of the three
philosophers), the move of philosopher $i$ changes only the phase of $i$: if $i$ is thinking, it
starts eating, picking up both forks at once; otherwise it goes back to thinking. The phases of
the other two philosophers are unchanged.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.moveAtomic`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#move-atomic).

## Dining philosophers with atomic fork acquisition

The labelled transition system on the
states of the three philosophers, labelled by the philosopher that moves: there is a step
labelled $i$ from $s$ to $t$ exactly when either philosopher $i$ thinks in $s$, neither of its
forks $i$ and $i + 1$ (modulo $3$) is held in $s$, and $t$ is $s$ with philosopher $i$ eating;
or philosopher $i$ eats in $s$ and $t$ is $s$ with philosopher $i$ thinking. A fork is held as
in the naive protocol: philosopher $j$ holds fork $j$ when it holds its first fork or eats, and
holds fork $j + 1$ when it eats.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.atomicLts`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#atomic-lts).

## Number of seated philosophers

The number of seated philosophers in a state $s$ is the
number of philosophers that hold at least one fork in $s$, that is, whose phase is either holding
the first fork or eating.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.seated`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#seated).

## Enabled moves under a butler

Philosopher $i$ can move in state $s$ when it can move in
$s$ under the naive protocol and, if it is thinking, fewer than two philosophers hold at least
one fork in $s$. Under the naive protocol each philosopher $i$ picks up the left fork $i$ first
and then the right fork $i + 1$ (modulo $3$), each only when no philosopher holds it, and an
eating philosopher can always put both forks down.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.canMoveButler`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#can-move-butler).

## Dining philosophers with a butler

The labelled transition system on the states of the
three philosophers, labelled by the philosopher that moves: there is a step labelled $i$ from
$s$ to $t$ exactly when philosopher $i$ can move in $s$ under the naive protocol, if
philosopher $i$ is thinking then fewer than two philosophers hold a fork in $s$, and $t$ is $s$
with philosopher $i$ advanced one phase (thinking to holding its first fork, to eating, to
thinking). Under the naive protocol each philosopher $i$ picks up the left fork $i$ first and
then the right fork $i + 1$ (modulo $3$), each only when no philosopher holds it, and an eating
philosopher can always put both forks down.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.butlerLts`, a definition declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#butler-lts).

## Atomic acquisition prevents deadlock

In the dining philosophers transition system with
atomic acquisition of both forks, every state reachable from the initial state (all three
philosophers thinking) has a successor: some philosopher can move.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.atomic_deadlock_free`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#atomic-deadlock-free).

## Under atomic acquisition every philosopher can always still eat

In the dining
philosophers transition system with atomic acquisition of both forks, for each philosopher
$i \in \{0, 1, 2\}$, from every state reachable from the initial state (all three philosophers
thinking) a state in which philosopher $i$ eats is reachable, in zero or more steps.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.atomic_can_eat`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#atomic-can-eat).

## Mutual exclusion under atomic acquisition

In the dining philosophers transition system
with atomic acquisition of both forks, for each philosopher $i \in \{0, 1, 2\}$, in no state
reachable from the initial state (all three philosophers thinking) do philosopher $i$ and its
neighbour $i + 1$ (modulo $3$) both eat.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.atomic_mutex`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#atomic-mutex).

## A butler prevents deadlock

In the dining philosophers transition system of the naive
protocol under a butler, every state reachable from the initial state (all three philosophers
thinking) has a successor: some philosopher can move.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.butler_deadlock_free`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#butler-deadlock-free).

## Under a butler every philosopher can always still eat

In the dining philosophers
transition system of the naive protocol under a butler, for each philosopher
$i \in \{0, 1, 2\}$, from every state reachable from the initial state (all three philosophers
thinking) a state in which philosopher $i$ eats is reachable, in zero or more steps.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.butler_can_eat`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#butler-can-eat).

## Mutual exclusion under a butler

In the dining philosophers transition system of the
naive protocol under a butler, for each philosopher $i \in \{0, 1, 2\}$, in no state reachable
from the initial state (all three philosophers thinking) do philosopher $i$ and its neighbour
$i + 1$ (modulo $3$) both eat.

Formalized by `Cslib.Algorithms.Concurrency.DiningPhilosophers.butler_mutex`, a theorem declared in [CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Concurrency/DiningPhilosophersVariants.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html#butler-mutex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dining philosophers problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/dining-philosophers-problem)
