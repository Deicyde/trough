---
catalog: module
lean: Cslib.DistributedConsistency.Trajectory, Cslib.DistributedConsistency.Trajectory.op, Cslib.DistributedConsistency.Trajectory.rcv, Cslib.DistributedConsistency.Trajectory.proc, Cslib.DistributedConsistency.Trajectory.pre, Cslib.DistributedConsistency.Trajectory.post, Cslib.DistributedConsistency.Trajectory.snd, Cslib.DistributedConsistency.Trajectory.rval, Cslib.DistributedConsistency.Trajectory.isCall, Cslib.DistributedConsistency.Trajectory.isReturn, Cslib.DistributedConsistency.Trajectory.WellFormed, Cslib.DistributedConsistency.Trajectory.callsBefore, Cslib.DistributedConsistency.Trajectory.returnsBefore, Cslib.DistributedConsistency.Trajectory.ReturnWellFormed, Cslib.DistributedConsistency.Trajectory.isCall_eq_isReturn_returnWellFormed, Cslib.DistributedConsistency.Trajectory.returnsAfter, Cslib.DistributedConsistency.Trajectory.returnOf, Cslib.DistributedConsistency.Trajectory.self_le_returnOf, Cslib.DistributedConsistency.Trajectory.isReturn_returnOf, Cslib.DistributedConsistency.Trajectory.returnOf_isReturn, Cslib.DistributedConsistency.Trajectory.returnOf_le, Cslib.DistributedConsistency.Trajectory.callOf, Cslib.DistributedConsistency.Trajectory.callOf_le_self, Cslib.DistributedConsistency.Trajectory.callOf_isCall
statement: formalized
proof: formalized
---

# Trajectories

`Cslib.Computability.Distributed.Consistency.Trajectory`, in [Cslib/Computability/Distributed/Consistency/Trajectory.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean), by Ching-Tsun Chou.

> A trajectory is the sequence of events corresponding to the transitions executed by a role.
> Various well-formedness conditions are imposed on trajectories.
>
> This file formalizes section 7.2 of [Burckhardt2014].
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Cslib.DistributedConsistency.Trajectory` (structure, [line 35](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L35))

> Trajectory structure.

```lean
structure Trajectory (Event State Operation Value Message Process : Type*)
    [Enumeration Event] where
  /-- `tr` assigns each event its transition. -/
  tr : Event → Transition State Operation Value Message Process
```

`Cslib.DistributedConsistency.Trajectory.op` (abbreviation, [line 45](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L45))

> The operation of an event.

```lean
abbrev op (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.rcv` (abbreviation, [line 48](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L48))

> The received message of an event.

```lean
abbrev rcv (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.proc` (abbreviation, [line 51](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L51))

> The process of an event.

```lean
abbrev proc (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.pre` (abbreviation, [line 54](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L54))

> The previous state of an event.

```lean
abbrev pre (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.post` (abbreviation, [line 57](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L57))

> The next state of an event.

```lean
abbrev post (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.snd` (abbreviation, [line 60](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L60))

> The set of messages sent by an event.

```lean
abbrev snd (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.rval` (abbreviation, [line 63](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L63))

> The value returned by an event.

```lean
abbrev rval (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.isCall` (abbreviation, [line 66](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L66))

> An event is considered a call iff it has an operation.

```lean
abbrev isCall (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.isReturn` (abbreviation, [line 69](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L69))

> An event is considered a return iff it has a return value.

```lean
abbrev isReturn (x : Event)
```

`Cslib.DistributedConsistency.Trajectory.WellFormed` (structure, [line 73](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L73))

> The well-formedness conditions on a trajectory.
> NOTE: In [Burckhardt2014], this is conditions "t3" and "t4" in the definition of a trajectory.

```lean
structure WellFormed : Prop where
  /-- The first event has no previous state.  Every subsequent event has its previous state
  matching the next state of its predecessor event. -/
  state_sequence (x : Event) :
    (pred x = x ∧ traj.pre x = none) ∨
    (pred x < x ∧ traj.pre x = traj.post (pred x))
  /-- Between any two calls there must be a return, which may be the same event as
  the first call. -/
  call_return_call (x y : Event) :
    x < y → traj.isCall x → traj.isCall y → ∃ z, traj.isReturn z ∧ x ≤ z ∧ z < y
```

`Cslib.DistributedConsistency.Trajectory.callsBefore` (definition, [line 85](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L85))

> The finite set of calls preceding an event (in the non-strict execution order).

```lean
def callsBefore (x : Event) : Finset Event
```

`Cslib.DistributedConsistency.Trajectory.returnsBefore` (definition, [line 88](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L88))

> The finite set of returns preceding an event (in the non-strict execution order).

```lean
def returnsBefore (x : Event) : Finset Event
```

`Cslib.DistributedConsistency.Trajectory.ReturnWellFormed` (definition, [line 93](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L93))

> The return well-formedness condition on a trajectory, which says that
> each event is preceded by no more returns than calls.
> NOTE: In [Burckhardt2014], this is called the well-formedness condition of a trajectory.

```lean
def ReturnWellFormed : Prop
```

`Cslib.DistributedConsistency.Trajectory.isCall_eq_isReturn_returnWellFormed` (theorem, [line 97](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L97))

> Lemma 7.1 of [Burckhardt2014]: if all calls return immediately,
> then the trajectory is return well-formed.

```lean
theorem isCall_eq_isReturn_returnWellFormed
    (h : traj.isCall = traj.isReturn) : traj.ReturnWellFormed
```

`Cslib.DistributedConsistency.Trajectory.returnsAfter` (definition, [line 103](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L103))

> The set of returns succeeding an event (in the non-strict execution order).

```lean
def returnsAfter (x : Event) : Set Event
```

`Cslib.DistributedConsistency.Trajectory.returnOf` (definition, [line 107](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L107))

> The return event of an event is the least return event succeeding it, if it exists.

```lean
noncomputable def returnOf (x : Event) : Option Event
```

`Cslib.DistributedConsistency.Trajectory.self_le_returnOf` (theorem, [line 112](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L112))

```lean
theorem self_le_returnOf {x y : Event} (h : traj.returnOf x = some y) : x ≤ y
```

`Cslib.DistributedConsistency.Trajectory.isReturn_returnOf` (theorem, [line 118](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L118))

```lean
theorem isReturn_returnOf {x y : Event} (h : traj.returnOf x = some y) : traj.isReturn y
```

`Cslib.DistributedConsistency.Trajectory.returnOf_isReturn` (theorem, [line 124](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L124))

```lean
theorem returnOf_isReturn {x : Event} (h : traj.isReturn x) : traj.returnOf x = some x
```

`Cslib.DistributedConsistency.Trajectory.returnOf_le` (theorem, [line 131](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L131))

> Every event preceding a return event has its return event.

```lean
theorem returnOf_le {x z : Event} (hz : traj.isReturn z) (hxz : x ≤ z) :
    ∃ y, traj.returnOf x = some y ∧ y ≤ z
```

`Cslib.DistributedConsistency.Trajectory.callOf` (definition, [line 139](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L139))

> The call event of an event is the greatest call event preceding it, if it exists.

```lean
def callOf (x : Event) : Option Event
```

`Cslib.DistributedConsistency.Trajectory.callOf_le_self` (theorem, [line 144](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L144))

```lean
theorem callOf_le_self {x y : Event} (h : traj.callOf x = some y) : y ≤ x
```

`Cslib.DistributedConsistency.Trajectory.callOf_isCall` (theorem, [line 150](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean#L150))

```lean
theorem callOf_isCall {x : Event} (h : traj.isCall x) : traj.callOf x = some x
```

## Depends on

- [Enumeration](enumeration.md)
- [Transitions](transition.md)

## Sources

- [Cslib/Computability/Distributed/Consistency/Trajectory.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Trajectory.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Distributed.Consistency.Trajectory.json)
