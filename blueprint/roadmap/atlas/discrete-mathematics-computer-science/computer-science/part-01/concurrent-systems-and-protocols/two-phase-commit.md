---
declaration: section
origin: cited
lean: Cslib.Distributed.TwoPhaseCommit.CoordState, Cslib.Distributed.TwoPhaseCommit.PartState, Cslib.Distributed.TwoPhaseCommit.State, Cslib.Distributed.TwoPhaseCommit.Action, Cslib.Distributed.TwoPhaseCommit.State.setPart, Cslib.Distributed.TwoPhaseCommit.Step, Cslib.Distributed.TwoPhaseCommit.lts, Cslib.Distributed.TwoPhaseCommit.initial
statement: formalized
proof: formalized
---

# Two-phase commit

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html).

## Coordinator states

In two-phase commit the coordinator is in one of three states:
waiting (collecting votes), committed (it has decided commit) or aborted (it has decided abort).

Formalized by `Cslib.Distributed.TwoPhaseCommit.CoordState`, an inductive type declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#coord-state).

## Participant states in two-phase commit

A participant is in one of four states: working
(it has not voted), prepared (it voted yes and waits for the decision), committed, or aborted
(it voted no, or learned of an abort).

Formalized by `Cslib.Distributed.TwoPhaseCommit.PartState`, an inductive type declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#part-state).

## Global states of two-phase commit

For a set $P$ of participants, a global state
consists of a coordinator state together with a participant state for each participant
$p \in P$.

Formalized by `Cslib.Distributed.TwoPhaseCommit.State`, a structure declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#state).

## Two-phase commit actions

The actions of the two-phase commit protocol over a set $P$ of
participants are: a participant $p \in P$ votes yes; a participant $p$ votes no; the coordinator
decides commit; the coordinator decides abort; a participant $p$ learns the commit decision; and a
participant $p$ learns the abort decision.

Formalized by `Cslib.Distributed.TwoPhaseCommit.Action`, an inductive type declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#action).

## Updating one participant's state

For a global state $s$, a participant $p$ and a
participant state $x$, the updated state has the same coordinator state as $s$, gives
participant $p$ the state $x$, and leaves the state of every other participant unchanged.

Formalized by `Cslib.Distributed.TwoPhaseCommit.State.setPart`, a definition declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#set-part).

## Transitions of two-phase commit

The protocol steps from a global state $s$ to a
global state $t$ by an action exactly in the following cases. A working participant $p$ may vote
yes, after which $p$ is prepared, or vote no, after which $p$ is aborted. If the coordinator is
waiting and every participant is prepared, the coordinator may decide commit, after which it is
committed. If the coordinator is waiting, it may decide abort, after which it is aborted. If the
coordinator has committed, a prepared participant $p$ may learn the commit, after which $p$ is
committed. If the coordinator has aborted, a prepared or working participant $p$ may learn the
abort, after which $p$ is aborted. In each step every other part of the state is unchanged.

Formalized by `Cslib.Distributed.TwoPhaseCommit.Step`, an inductive type declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#step).

## Two-phase commit as a transition system

For a set $P$ of participants, the labelled
transition system whose states are the global states of the protocol, whose labels are the
protocol actions, and whose transitions are the protocol steps.

Formalized by `Cslib.Distributed.TwoPhaseCommit.lts`, a definition declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#lts).

## Initial state of two-phase commit

The initial state of the two-phase commit protocol:
the coordinator is waiting and every participant is working.

Formalized by `Cslib.Distributed.TwoPhaseCommit.initial`, a definition declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#initial).

## Reachable states of two-phase commit

A global state $s$ is reachable when some finite
sequence of protocol actions leads by protocol steps from the initial state, in which the
coordinator is waiting and every participant is working, to $s$.

Formalized by `Cslib.Distributed.TwoPhaseCommit.Reachable`, a definition declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#reachable).

## Reachable states are closed under steps

If a global state $s$ of the two-phase commit
protocol is reachable and some action takes $s$ to $t$ in one protocol step, then $t$ is
reachable.

Formalized by `Cslib.Distributed.TwoPhaseCommit.Reachable.step`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#step-2).

## Two-phase commit invariant

A global state $s$ of the two-phase commit protocol
satisfies the invariant when two conditions hold: if the coordinator has committed, then every
participant is prepared or committed; and every committed participant has a committed
coordinator.

Formalized by `Cslib.Distributed.TwoPhaseCommit.Inv`, a structure declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#inv).

## Multistep transitions preserve the two-phase commit invariant

If a state $s$ of the
two-phase commit protocol satisfies the inductive invariant and a state $t$ is reached from $s$
by a finite sequence of transitions, then $t$ satisfies the invariant.

Formalized by `Cslib.Distributed.TwoPhaseCommit.inv_mtr`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#inv-mtr).

## The two-phase commit invariant holds in reachable states

For every set $P$ of
participants, every global state of the two-phase commit protocol that is reachable from the
initial state satisfies the inductive invariant, that is, both of the following hold: if the
coordinator has committed, then every participant is prepared or committed; and every committed
participant has a committed coordinator.

Formalized by `Cslib.Distributed.TwoPhaseCommit.inv_reachable`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#inv-reachable).

## Atomicity between participants

For every set $P$ of participants, in every reachable
state of the two-phase commit protocol, if some participant $p$ has committed, then no
participant $q$ has aborted.

This is the participant part of condition AC1 of Bernstein, Hadzilacos and Goodman.

Formalized by `Cslib.Distributed.TwoPhaseCommit.atomicity`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#atomicity).

## Validity for the coordinator

In every reachable state of the two-phase commit protocol,
if the coordinator has decided commit, then every participant voted yes, that is, every
participant is prepared or committed.

This is the coordinator form of condition AC3 of Bernstein, Hadzilacos and Goodman.

Formalized by `Cslib.Distributed.TwoPhaseCommit.coord_committed_imp_all_voted_yes`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#coord-committed-imp-all-voted-yes).

## Validity for participants

In every reachable state of the two-phase commit protocol, if
some participant has committed, then every participant voted yes, that is, every participant is
prepared or committed.

This is the participant form of condition AC3 of Bernstein, Hadzilacos and Goodman; that the
coordinator has then decided commit is the separate result that a committed participant has a
committed coordinator.

Formalized by `Cslib.Distributed.TwoPhaseCommit.committed_imp_all_voted_yes`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#committed-imp-all-voted-yes).

## An aborted participant rules out a coordinator commit

In every reachable state of the
two-phase commit protocol, if some participant has aborted, then the coordinator has not decided
commit.

Formalized by `Cslib.Distributed.TwoPhaseCommit.aborted_imp_not_committed`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#aborted-imp-not-committed).

## A committed participant has a committed coordinator

In every reachable state of the
two-phase commit protocol, if some participant has committed, then the coordinator has
committed.

This is the atomicity condition AC1 of Bernstein, Hadzilacos and Goodman between a participant
and the coordinator.

Formalized by `Cslib.Distributed.TwoPhaseCommit.part_committed_coord_committed`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#part-committed-coord-committed).

## A committed coordinator has no aborted participant

In every reachable state of the
two-phase commit protocol, if the coordinator has decided commit, then no participant has
aborted.

This is the coordinator–participant part of condition AC1 of Bernstein, Hadzilacos and
Goodman.

Formalized by `Cslib.Distributed.TwoPhaseCommit.coord_committed_part_not_aborted`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#coord-committed-part-not-aborted).

## An aborted coordinator has no committed participant

In every reachable state of the
two-phase commit protocol, if the coordinator has decided abort, then no participant has
committed.

This is the coordinator–participant part of condition AC1 of Bernstein, Hadzilacos and
Goodman.

Formalized by `Cslib.Distributed.TwoPhaseCommit.coord_aborted_part_not_committed`, a theorem declared in [CSLibExt/Computability/Distributed/TwoPhaseCommit.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Distributed/TwoPhaseCommit.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html#coord-aborted-part-not-committed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-phase commit](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/concurrent-systems-and-protocols/two-phase-commit)
