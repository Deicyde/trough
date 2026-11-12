---
catalog: module
lean: Cslib.DistributedConsistency.BaseHistory, Cslib.DistributedConsistency.BaseHistory.so, Cslib.DistributedConsistency.History, Cslib.DistributedConsistency.AbstractExecution, Cslib.DistributedConsistency.History.Satisfies, Cslib.DistributedConsistency.AbstractExecution.ReadMyWrites, Cslib.DistributedConsistency.AbstractExecution.MonotonicReads, Cslib.DistributedConsistency.AbstractExecution.ConsistentPrefix, Cslib.DistributedConsistency.AbstractExecution.hb, Cslib.DistributedConsistency.AbstractExecution.NoCircularCausality, Cslib.DistributedConsistency.AbstractExecution.CausalArbitration, Cslib.DistributedConsistency.AbstractExecution.CausalVisibility, Cslib.DistributedConsistency.AbstractExecution.Causality, Cslib.DistributedConsistency.AbstractExecution.SingleOrder, Cslib.DistributedConsistency.AbstractExecution.RealTime, Cslib.DistributedConsistency.AbstractExecution.nonVisibleEvents, Cslib.DistributedConsistency.AbstractExecution.EventualVisibility, Cslib.DistributedConsistency.OperationContext, Cslib.DistributedConsistency.OperationContext.Equiv, Cslib.DistributedConsistency.ReplicatedDataType, Cslib.DistributedConsistency.AbstractExecution.context, Cslib.DistributedConsistency.AbstractExecution.RVal, Cslib.DistributedConsistency.AbstractExecution.Linearizability, Cslib.DistributedConsistency.AbstractExecution.SequentialConsistency, Cslib.DistributedConsistency.AbstractExecution.CausalConsistency, Cslib.DistributedConsistency.AbstractExecution.BasicEventualConsistency
statement: formalized
proof: formalized
---

# Consistency specifications

`Cslib.Computability.Distributed.Consistency.Specification`, in [Cslib/Computability/Distributed/Consistency/Specification.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean), by Ching-Tsun Chou.

> We formalize several notions of consistency for replicated data types defined in [Burckhardt2014],
> listed below in decreasing order of strength:
> * Linearizability,
> * Sequential consistency.
> * Causal consistency,
> * Basic eventual consistency,
>
> We follow [Burckhardt2014] closely in the formalization except for one detail:
> instead of using an equivalence relation "same-session" to model the notion of sessions,
> we use a map `se : Event → Session` and regard two events `x` and `y` to belong to the
> same session iff `se x = se y`.  These two approaches are clearly equivalent and `se` is
> chosen because it is easier to work with.
>
> NOTE: We left out the definition of quiescent consistency, for two reasons:
> * Quiescent consistency is too weak a notion to be practically useful (see the remark
>   on page 44 of [Burckhardt2014]).
> * We found during the process of formalization that the only theoretic result about
>   quiescent consistency in [Burckhardt2014], that it is implied by causal consistency,
>   is incorrect given the definitions in [Burckhardt2014].
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Cslib.DistributedConsistency.BaseHistory` (structure, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L48))

> `BaseHistory` is an auxiliary definition containing all data fields of `History` below.

```lean
structure BaseHistory (Event Operation Value Session : Type*) where
  /-- `op` assigns each event its operation. -/
  op : Event → Operation
  /-- `se` assigns each event its session. -/
  se : Event → Session
  /-- `rval` assigns each event its return value, where `none` indicates that
  the event never returns. -/
  rval : Event → Option Value
  /-- `rb` is the "returns before" order on events. -/
  rb : Event → Event → Prop
```

`Cslib.DistributedConsistency.BaseHistory.so` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L60))

> `so` (for "session order") is `rb` restricted to a single session.

```lean
def BaseHistory.so (h : BaseHistory Event Operation Value Session) (s : Session)
```

`Cslib.DistributedConsistency.History` (structure, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L64))

> `History` extends `BaseHistory` with well-formedness conditions.

```lean
structure History (Event Operation Value Session : Type*)
    extends bh : BaseHistory Event Operation Value Session where
  /-- `rb` is a strict order on events (namely, it is irreflexive and transitive). -/
  rb_strict_order : IsStrictOrder Event rb
  /-- Each event has only a finite number of predecessors in the `rb` order. -/
  rb_pred_finite : ∀ x, (predecessors rb x).Finite
  /-- The `rb` order is an interval order. -/
  rb_interval_order : IsIntervalOrder rb
  /-- If an event `x` returns before another event `y`, then `x` cannot return `none`. -/
  rb_rval_ne_none : ∀ x y, rb x y → rval x ≠ none
  /-- The `so` order is a strict total order of the events of each session. -/
  so_strict_total_order : ∀ s, IsStrictTotalOrder {x | se x = s} (bh.so s)
```

`Cslib.DistributedConsistency.AbstractExecution` (structure, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L79))

> `AbstractExecution` extends `History` with two more orders and additional
> well-formedness conditions.

```lean
structure AbstractExecution (Event Operation Value Session : Type*)
    extends History Event Operation Value Session where
  /-- `vis x y` means that `x` is visible to `y`. -/
  vis : Event → Event → Prop
  /-- `ar` is the arbitration order of the whole system. -/
  ar : Event → Event → Prop
  /-- The visibility order `vis` is acyclic. -/
  vis_acyclic : Acyclic vis
  /-- Each event has only a finite number of predecessors in the `vis` order. -/
  vis_pred_finite : ∀ x, (predecessors vis x).Finite
  /-- The arbitration order is a strict total order of all events. -/
  ar_strict_total_order : IsStrictTotalOrder Event ar
```

`Cslib.DistributedConsistency.History.Satisfies` (definition, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L94))

> A history satisfies a predicte `p` on abstract executions iff it can be extended
> to an abstract execution satisfying `p`.

```lean
def History.Satisfies (h : History Event Operation Value Session)
    (p : AbstractExecution Event Operation Value Session → Prop) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.ReadMyWrites` (definition, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L102))

> `ReadMyWrites` says that if two events are ordered by `so`,
> then they are also ordered by `vis`.

```lean
def ReadMyWrites (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.MonotonicReads` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L107))

> `MonotonicReads` says that if `x` is visible to `y`, then `x` is also visible to all
> successors of `y` under the `so` order.

```lean
def MonotonicReads (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.ConsistentPrefix` (definition, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L112))

> `ConsistentPrefix` says that if `x` is visible to `y` in a different session,
> then all predecessors of `x` in the arbitration order are also visible to `y`.

```lean
def ConsistentPrefix (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.hb` (definition, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L117))

> The `happens before` order is transitive closure of the union of the `vis` order
> and the `so s` orders for all sessions `s`.

```lean
def hb (a : AbstractExecution Event Operation Value Session) : Event → Event → Prop
```

`Cslib.DistributedConsistency.AbstractExecution.NoCircularCausality` (definition, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L121))

> `NoCircularCausality` says that the `hb` order is acyclic.

```lean
def NoCircularCausality (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.CausalArbitration` (definition, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L126))

> `CausalArbitration` says that if two events are ordered by `hb`,
> then they are also ordered by `ar`.

```lean
def CausalArbitration (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.CausalVisibility` (definition, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L131))

> `CausalVisibility` says that if two events are ordered by `hb`,
> then they are also ordered by `vis`.

```lean
def CausalVisibility (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.Causality` (definition, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L135))

> `Causality` is the conjunction of `CausalArbitration` and `CausalVisibility`.

```lean
def Causality (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.SingleOrder` (definition, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L140))

> `SingleOrder` says that `vis` and `ar` are the same order except that there may be
> a set of events which never returns and are not visible.

```lean
def SingleOrder (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.RealTime` (definition, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L145))

> `RealTime` says that if two events are ordered by `rb`, then they are also ordered by `ar`.

```lean
def RealTime (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.nonVisibleEvents` (definition, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L150))

> `a.nonVisibleEvents x s` is the set of events in session `s` which returns after `x`
> but does not see `x`.

```lean
def nonVisibleEvents (a : AbstractExecution Event Operation Value Session)
    (x : Event) (s : Session) : Set Event
```

`Cslib.DistributedConsistency.AbstractExecution.EventualVisibility` (definition, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L157))

> `EventualVisibility` says that for any event `x` and any session `s`, there can be at most
> finitely many events in `s` that return after `x` and do not see `x`.

```lean
def EventualVisibility (a : AbstractExecution Event Operation Value Session) : Prop
```

`Cslib.DistributedConsistency.OperationContext` (structure, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L164))

> An `OperationContext` is the data used by a replicated data type to determine the
> return value of an operation.  It is an abstraction of the notion of states.

```lean
structure OperationContext (Event Operation : Type*) where
  /-- The set of events in the operation context. -/
  events : Set Event
  /-- Operation labeling of events. -/
  op : Event → Operation
  /-- Visibility order. -/
  vis : Event → Event → Prop
  /-- Arbitration order. -/
  ar : Event → Event → Prop
```

`Cslib.DistributedConsistency.OperationContext.Equiv` (structure, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L177))

> The notion of equivalence on `OperationContext`, which is essentially an isomorphism
> that ignores the identities of events and the behavior of `op`, `vis`, and `ar` outside
> the set of events in the operation context.

```lean
structure OperationContext.Equiv (c1 c2 : OperationContext Event Operation) where
  /-- A bijection from `c1`'s events to `c2`'s events. -/
  equiv : { x // x ∈ c1.events } ≃ { x // x ∈ c2.events }
  /-- `op` is preserved by the bijection. -/
  op_equiv : ∀ x, c1.op x.val = c2.op (equiv x).val
  /-- `vis` is preserved by the bijection. -/
  vis_equiv : ∀ x y, c1.vis x.val y.val ↔ c2.vis (equiv x).val (equiv y).val
  /-- `ar` is preserved by the bijection. -/
  ar_equiv : ∀ x y, c1.ar x.val y.val ↔ c2.ar (equiv x).val (equiv y).val
```

`Cslib.DistributedConsistency.ReplicatedDataType` (structure, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L188))

> The notion of a replicated data type.

```lean
structure ReplicatedDataType (Event Operation Value : Type*) where
  /-- `rval` takes an operation and an operation context and returns a value. -/
  rval : Operation → OperationContext Event Operation → Option Value
  /-- For any operation, `rval` must returns the same value on equivalent operation contexts. -/
  rval_equiv : ∀ o c1 c2, ∀ _ : c1.Equiv c2, rval o c1 = rval o c2
```

`Cslib.DistributedConsistency.AbstractExecution.context` (definition, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L197))

> `a.context xs` is the operation context obtained by restricting `a` to `xs`.

```lean
def context (a : AbstractExecution Event Operation Value Session)
    (xs : Set Event) : OperationContext Event Operation
```

`Cslib.DistributedConsistency.AbstractExecution.RVal` (definition, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L207))

> `a.RVal d` says that the return value of any event in the abstract execution `a` is
> the same as the value returned by the replicated data type `d` in the context consisting of
> the predecessors of the event.

```lean
def RVal (a : AbstractExecution Event Operation Value Session)
    (d : ReplicatedDataType Event Operation Value) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.Linearizability` (definition, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L212))

> `Linearizability` is the conjunction of `SingleOrder`, `RealTime`, and `RVal`.

```lean
def Linearizability (a : AbstractExecution Event Operation Value Session)
    (d : ReplicatedDataType Event Operation Value) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.SequentialConsistency` (definition, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L217))

> `SequentialConsistency` is the conjunction of `SingleOrder`, `ReadMyWrites`, and `RVal`.

```lean
def SequentialConsistency (a : AbstractExecution Event Operation Value Session)
    (d : ReplicatedDataType Event Operation Value) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.CausalConsistency` (definition, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L222))

> `CausalConsistency` is the conjunction of `EventualVisibility`, `Causality`, and `RVal`.

```lean
def CausalConsistency (a : AbstractExecution Event Operation Value Session)
    (d : ReplicatedDataType Event Operation Value) : Prop
```

`Cslib.DistributedConsistency.AbstractExecution.BasicEventualConsistency` (definition, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean#L228))

> `BasicEventualConsistency` is the conjunction of `EventualVisibility`, `NoCircularCausality`,
> and `RVal`.

```lean
def BasicEventualConsistency (a : AbstractExecution Event Operation Value Session)
    (d : ReplicatedDataType Event Operation Value) : Prop
```

## Depends on

- [Relations: Definitions](../../../foundations/relation/defs.md)

## Sources

- [Cslib/Computability/Distributed/Consistency/Specification.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Specification.lean)
