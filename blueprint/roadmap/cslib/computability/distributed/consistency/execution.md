---
catalog: module
lean: Cslib.DistributedConsistency.ConcreteExecution, Cslib.DistributedConsistency.ConcreteExecution.op, Cslib.DistributedConsistency.ConcreteExecution.rcv, Cslib.DistributedConsistency.ConcreteExecution.proc, Cslib.DistributedConsistency.ConcreteExecution.pre, Cslib.DistributedConsistency.ConcreteExecution.post, Cslib.DistributedConsistency.ConcreteExecution.snd, Cslib.DistributedConsistency.ConcreteExecution.rval, Cslib.DistributedConsistency.ConcreteExecution.isCall, Cslib.DistributedConsistency.ConcreteExecution.isReturn, Cslib.DistributedConsistency.ConcreteExecution.trajectory, Cslib.DistributedConsistency.ConcreteExecution.returnOf, Cslib.DistributedConsistency.ConcreteExecution.callOf, Cslib.DistributedConsistency.ConcreteExecution.WellFormed, Cslib.DistributedConsistency.ConcreteExecution.isCall_eq_isReturn_returnWellFormed, Cslib.DistributedConsistency.ConcreteExecution.HistoryEvent, Cslib.DistributedConsistency.ConcreteExecution.baseHistory, Cslib.DistributedConsistency.ConcreteExecution.self_le_returnOf, Cslib.DistributedConsistency.ConcreteExecution.isReturn_returnOf, Cslib.DistributedConsistency.ConcreteExecution.rb_strict_order, Cslib.DistributedConsistency.ConcreteExecution.rb_pred_finite, Cslib.DistributedConsistency.ConcreteExecution.not_rb, Cslib.DistributedConsistency.ConcreteExecution.rb_interval_order, Cslib.DistributedConsistency.ConcreteExecution.rb_rval_ne_none, Cslib.DistributedConsistency.ConcreteExecution.rb_of_lt, Cslib.DistributedConsistency.ConcreteExecution.so_strict_total_order, Cslib.DistributedConsistency.ConcreteExecution.history
statement: formalized
proof: formalized
---

# Concrete executions

`Cslib.Computability.Distributed.Consistency.Execution`, in [Cslib/Computability/Distributed/Consistency/Execution.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean), by Ching-Tsun Chou.

> A concrete execution is the sequence of events corresponding to the transitions executed
> by a distributed system containing (potentially) multiple roles.
> Various well-formedness conditions are imposed on concrete executions.
> We also show that a history (defined in `Specification.lean`) can be extracted from
> a concrete execution by restriction to call events
>
> This file formalizes sections 7.3 and 7.4 of [Burckhardt2014].
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Cslib.DistributedConsistency.ConcreteExecution` (structure, [line 35](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L35))

> Concrete execution structure.

```lean
structure ConcreteExecution (Event State Operation Value Message Process Role : Type*)
    [Enumeration Event] where
  /-- `tr` assigns each event its transition. -/
  tr : Event → Transition State Operation Value Message Process
  /-- `role` assigns each event its role id. -/
  role : Event → Role
  /-- `del` is the message delivery relation. -/
  del : Event → Event → Prop
```

`Cslib.DistributedConsistency.ConcreteExecution.op` (abbreviation, [line 49](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L49))

> The operation of an event.

```lean
abbrev op (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.rcv` (abbreviation, [line 52](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L52))

> The received message of an event.

```lean
abbrev rcv (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.proc` (abbreviation, [line 55](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L55))

> The process of an event.

```lean
abbrev proc (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.pre` (abbreviation, [line 58](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L58))

> The previous state of an event.

```lean
abbrev pre (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.post` (abbreviation, [line 61](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L61))

> The next state of an event.

```lean
abbrev post (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.snd` (abbreviation, [line 64](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L64))

> The set of messages sent by an event.

```lean
abbrev snd (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.rval` (abbreviation, [line 67](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L67))

> The value returned by an event.

```lean
abbrev rval (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.isCall` (abbreviation, [line 70](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L70))

> An event is considered a call iff it has an operation.

```lean
abbrev isCall (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.isReturn` (abbreviation, [line 73](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L73))

> An event is considered a return iff it has a return value.

```lean
abbrev isReturn (x : Event)
```

`Cslib.DistributedConsistency.ConcreteExecution.trajectory` (definition, [line 77](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L77))

> Projecting a concrete execution on a role to obtain a trajectory.

```lean
noncomputable def trajectory (r : Role) :
    Trajectory {x : Event // exec.role x = r} State Operation Value Message Process
```

`Cslib.DistributedConsistency.ConcreteExecution.returnOf` (definition, [line 82](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L82))

> The return event of an event according to its role's trajectory.

```lean
noncomputable def returnOf (x : Event) : Option Event
```

`Cslib.DistributedConsistency.ConcreteExecution.callOf` (definition, [line 86](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L86))

> The call event of an event according to its role's trajectory.

```lean
noncomputable def callOf (x : Event) : Option Event
```

`Cslib.DistributedConsistency.ConcreteExecution.WellFormed` (structure, [line 90](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L90))

> The well-formedness conditions on a concrete execution.

```lean
structure WellFormed : Prop where
  /-- Projecting the concrete execution on each role produces a well-formed trajectory. -/
  trajectory_wellFormed (r : Role) : (exec.trajectory r).WellFormed
  /-- If a message from event `x` is delivered to event `y`, then `x` strictly precedes `y`
  and the message received by `y` is sent by `x`. -/
  del_snd_lt_rcv (x y : Event) : exec.del x y → x < y ∧
    ∃ m, exec.rcv y = some m ∧ m ∈ exec.snd x
  /-- An event can be delivered a message from at most one other event. -/
  del_sender_unique (x1 x2 y : Event) : exec.del x1 y → exec.del x2 y → x1 = x2
```

`Cslib.DistributedConsistency.ConcreteExecution.isCall_eq_isReturn_returnWellFormed` (theorem, [line 102](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L102))

> Lemma 7.1 of [Burckhardt2014]: if all calls return immediately,
> then the concrete execution is return well-formed.

```lean
theorem isCall_eq_isReturn_returnWellFormed (h : exec.isCall = exec.isReturn) (r : Role) :
    (exec.trajectory r).ReturnWellFormed
```

`Cslib.DistributedConsistency.ConcreteExecution.HistoryEvent` (abbreviation, [line 107](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L107))

> A history contains only call events.

```lean
abbrev HistoryEvent
```

`Cslib.DistributedConsistency.ConcreteExecution.baseHistory` (definition, [line 110](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L110))

> Extracting a history from a concrete execution by restriction to call events.

```lean
noncomputable def baseHistory : BaseHistory exec.HistoryEvent Operation Value Role
```

`Cslib.DistributedConsistency.ConcreteExecution.self_le_returnOf` (theorem, [line 116](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L116))

```lean
theorem self_le_returnOf {x z : Event} (h : exec.returnOf x = some z) : x ≤ z
```

`Cslib.DistributedConsistency.ConcreteExecution.isReturn_returnOf` (theorem, [line 125](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L125))

```lean
theorem isReturn_returnOf {x z : Event} (h : exec.returnOf x = some z) : exec.isReturn z
```

`Cslib.DistributedConsistency.ConcreteExecution.rb_strict_order` (theorem, [line 134](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L134))

```lean
theorem rb_strict_order : IsStrictOrder exec.HistoryEvent exec.baseHistory.rb
```

`Cslib.DistributedConsistency.ConcreteExecution.rb_pred_finite` (theorem, [line 141](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L141))

```lean
theorem rb_pred_finite (x : exec.HistoryEvent) : (predecessors exec.baseHistory.rb x).Finite
```

`Cslib.DistributedConsistency.ConcreteExecution.not_rb` (theorem, [line 147](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L147))

```lean
theorem not_rb {x y : exec.HistoryEvent} {z : Event}
    (hxy : ¬ exec.baseHistory.rb x y) (hx : exec.returnOf x.val = some z) : y ≤ z
```

`Cslib.DistributedConsistency.ConcreteExecution.rb_interval_order` (theorem, [line 151](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L151))

```lean
theorem rb_interval_order : IsIntervalOrder exec.baseHistory.rb
```

`Cslib.DistributedConsistency.ConcreteExecution.rb_rval_ne_none` (theorem, [line 160](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L160))

```lean
theorem rb_rval_ne_none {x y : exec.HistoryEvent}
    (h : exec.baseHistory.rb x y) : exec.baseHistory.rval x ≠ none
```

`Cslib.DistributedConsistency.ConcreteExecution.rb_of_lt` (theorem, [line 166](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L166))

```lean
theorem rb_of_lt (hwf : exec.WellFormed) {x y : exec.HistoryEvent}
    (hr : exec.role x.val = exec.role y.val) (hlt : x.val < y.val) : exec.baseHistory.rb x y
```

`Cslib.DistributedConsistency.ConcreteExecution.so_strict_total_order` (theorem, [line 174](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L174))

```lean
theorem so_strict_total_order (hwf : exec.WellFormed) (r : Role) :
    IsStrictTotalOrder {x : exec.HistoryEvent | exec.baseHistory.se x = r}
      (exec.baseHistory.so r)
```

`Cslib.DistributedConsistency.ConcreteExecution.history` (definition, [line 191](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean#L191))

> The history extracted from a concrete execution by restriction to call events
> is a well-defined history.

```lean
noncomputable def history (hwf : exec.WellFormed) :
    History exec.HistoryEvent Operation Value Role
```

## Depends on

- [Consistency specifications](specification.md)
- [Trajectories](trajectory.md)

## Sources

- [Cslib/Computability/Distributed/Consistency/Execution.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Execution.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Distributed.Consistency.Execution.json)
