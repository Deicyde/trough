---
declaration: section
origin: cited
lean: Cslib.Databases.LockMode, Cslib.Databases.LockMode.Covers, Cslib.Databases.Access.mode, Cslib.Databases.Action, Cslib.Databases.ops, Cslib.Databases.HoldsBefore, Cslib.Databases.LocksCover, Cslib.Databases.ReleasesLocks
statement: formalized
proof: formalized
---

# Two-phase locking

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html).

## Lock mode

A lock is held in one of two modes: shared (a read lock) or exclusive (a write
lock).

Formalized by `Cslib.Databases.LockMode`, an inductive type declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#lock-mode).

## Lock mode coverage

A lock mode $m'$ covers a lock mode $m$ when a lock in mode $m'$
permits what a lock in mode $m$ permits: an exclusive lock covers both modes, and a shared lock
covers only the shared mode.

Formalized by `Cslib.Databases.LockMode.Covers`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#covers).

## Lock mode required by an access

The lock mode an access requires: shared for a read,
exclusive for a write.

Formalized by `Cslib.Databases.Access.mode`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#mode).

## Action of a locked schedule

For $n$ transactions, numbered $0, \dots, n-1$, and a type $X$
of data items, an action of a locked schedule is one of three kinds: a read or write operation; a
lock request, in which a transaction $t$ acquires a lock on an item $x \in X$ in a lock mode $m$
(shared or exclusive); or a release, in which a transaction $t$ releases its lock on an item
$x \in X$.

Formalized by `Cslib.Databases.Action`, an inductive type declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#action).

## Reads and writes of a locked schedule

For a locked schedule $s$, the schedule of reads and
writes of $s$: its reads and writes in order, with the lock requests and releases erased.

Formalized by `Cslib.Databases.ops`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#ops).

## Holding a lock

Let $s$ be a locked schedule, $t$ a transaction, $x$ a data item, $m$ a
lock mode and $p$ a natural number. Transaction $t$ holds a lock on $x$ covering mode $m$ just
before position $p$ of $s$ when there is a position $q < p$ at which $s$ has a lock request by $t$
on $x$ in some mode $m'$ that covers $m$, and for no position $r$ with $q < r < p$ is the action
of $s$ at $r$ a release of $x$ by $t$.

Formalized by `Cslib.Databases.HoldsBefore`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#holds-before).

## Schedules covered by locks

A locked schedule $s$ is covered by locks when every read or
write is protected by a lock of its transaction: whenever $s$ has at position $p$ a read or write
$o$ by transaction $t$ on item $x$, just before position $p$ transaction $t$ holds a lock on $x$
(acquired at an earlier position and not released since) whose mode covers the mode $o$ requires,
namely shared for a read and exclusive for a write; an exclusive lock covers both modes.

Formalized by `Cslib.Databases.LocksCover`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#locks-cover).

## Schedules that release every lock

A locked schedule $s$ releases its locks when every lock
request is followed by a matching release: whenever $s$ has at position $q$ a lock request (in
either mode) by transaction $t$ on item $x$, there is a position $r > q$ at which $s$ has a
release by $t$ of $x$.

In particular, transactions end holding no locks.

Formalized by `Cslib.Databases.ReleasesLocks`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#releases-locks).

## Well-formed locked schedules

A locked schedule $s$ (a list of reads, writes, lock
requests and lock releases of transactions) is well formed when its accesses are covered by
locks and it releases its locks: every read or write in $s$ is preceded by a lock request of its
own transaction on its item, in a mode covering the access (shared or exclusive for a read,
exclusive for a write), with no release of that item by that transaction in between; and every
lock request in $s$ by a transaction on an item is followed later in $s$ by a release of that
item by the same transaction.

Formalized by `Cslib.Databases.WellFormed`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#well-formed).

## Lock compatibility at a point

A locked schedule $s$ is legal just before position $p$
when, for every data item $x$, all distinct transactions $t \ne t'$ and all lock modes $m$, $m'$:
if $t$ holds a lock on $x$ covering $m$ and $t'$ holds a lock on $x$ covering $m'$ just before
position $p$ of $s$, then $m$ and $m'$ are both the shared mode. In words, two transactions do not
both hold locks on the same item unless both locks are shared.

Formalized by `Cslib.Databases.LegalAt`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#legal-at).

## Locked items

The list of data items locked in a locked schedule $s$: for each lock request
of $s$, in order, the item it locks, so an item appears once for each lock request on it.

Formalized by `Cslib.Databases.lockedItems`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#locked-items).

## Legal locked schedule

A locked schedule $s$ of length $\ell$ is legal when it satisfies
lock compatibility at every point $p \le \ell$: just before position $p$, no two distinct
transactions both hold locks on the same item unless both locks are shared.

After the last action the locks no longer change, so the points $p \le \ell$ are all the points.

Formalized by `Cslib.Databases.Legal`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#legal).

## Two-phase schedules

A locked schedule $s$ is two-phase when every lock request of a
transaction precedes every release of that transaction: whenever $s$ has at position $p$ a release
by transaction $t$ and at position $q$ a lock request by $t$ (on any items, in any mode), then
$q < p$.

Formalized by `Cslib.Databases.TwoPhase`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#two-phase).

## Strict two-phase schedules

A locked schedule $s$ is strict two-phase when it is two-phase
and every transaction releases its exclusive locks only after its last read or write: whenever
$s$ has at position $p$ a release by transaction $t$ of item $x$ and just before position $p$
transaction $t$ holds an exclusive lock on $x$, every read or write of $t$ in $s$ occurs at a
position before $p$.

Formalized by `Cslib.Databases.StrictTwoPhase`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#strict-two-phase).

## Lock coverage at a position

For a locked schedule $s$ and a position $p$: if $s$ has at
position $p$ a read or write $o$ by transaction $t$ on item $x$, then just before position $p$
transaction $t$ holds a lock on $x$ whose mode covers the mode $o$ requires (shared for a read,
exclusive for a write; an exclusive lock covers both modes). If position $p$ holds a lock request
or a release, or lies beyond the end of $s$, the condition holds trivially.

Formalized by `Cslib.Databases.LocksCoverAt`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#locks-cover-at).

## Release of the lock requested at a position

For a locked schedule $s$ and a position $q$:
if $s$ has at position $q$ a lock request (in either mode) by transaction $t$ on item $x$, then
there is a position $r$ with $q < r$ and $r$ less than the length of $s$ at which $s$ has a release
by $t$ of $x$. If position $q$ holds a read, a write or a release, or lies beyond the end of $s$,
the condition holds trivially.

Formalized by `Cslib.Databases.ReleasedAt`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#released-at).

## Two-phase condition at a pair of positions

For a locked schedule $s$ and positions $p$ and
$q$: if $s$ has at position $p$ a release by transaction $t$ and at position $q$ a lock request by
the same transaction $t$, then $q < p$. For every other pair of positions, including positions
beyond the end of $s$, the condition holds trivially.

Formalized by `Cslib.Databases.TwoPhaseAt`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#two-phase-at).

## Strictness at a pair of positions

For a locked schedule $s$ and positions $p$ and $q$: if
$s$ has at position $p$ a release by transaction $t$ of item $x$, just before position $p$
transaction $t$ holds an exclusive lock on $x$, and $s$ has at position $q$ a read or write by
$t$, then $q < p$. For every other pair of positions, including positions beyond the end of $s$,
the condition holds trivially.

Formalized by `Cslib.Databases.StrictAt`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#strict-at).

## Release test

For a transaction $t$, this Boolean test on the actions of a locked schedule
returns true exactly when the action is a release by $t$ of its lock on some item.

Formalized by `Cslib.Databases.Action.isUnlockBy`, a definition declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#is-unlock-by).

## The two-phase locking theorem

If the reads and writes of a locked schedule are distinct,
are covered by locks, and the schedule is legal and two-phase, then its reads and writes form a
conflict-serializable schedule.

Formalized by `Cslib.Databases.TwoPhase.conflictSerializable`, a theorem declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#conflict-serializable).

## Strict two-phase locking theorem

If the reads and writes of a locked schedule are
distinct, are covered by locks, and the schedule is legal and strict two-phase, then its reads and
writes form a conflict-serializable schedule.

Formalized by `Cslib.Databases.StrictTwoPhase.conflictSerializable`, a theorem declared in [CSLibExt/Databases/TwoPhaseLocking.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Databases/TwoPhaseLocking.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html#conflict-serializable-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-phase locking](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/two-phase-locking/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/databases/two-phase-locking)
