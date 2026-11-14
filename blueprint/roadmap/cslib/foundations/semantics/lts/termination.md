---
catalog: module
lean: Cslib.LTS.Bounded.toTerminating, Cslib.LTS.bounded_terminating, Cslib.LTS.Terminating.toAcyclic, Cslib.LTS.terminating_acyclic, Cslib.LTS.Acyclic.toBoundedUpTo, Cslib.LTS.Acyclic.toBounded, Cslib.LTS.Acyclic.toTerminating, Cslib.LTS.MayTerminate, Cslib.LTS.Stuck
statement: formalized
proof: formalized
---

# Termination of LTS

`Cslib.Foundations.Semantics.LTS.Termination`, in [Cslib/Foundations/Semantics/LTS/Termination.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean), by Fabrizio Montesi.

> This module relates global execution bounds, well-founded termination, and acyclicity.

`Cslib.LTS.Bounded.toTerminating` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L30))

> Bounded LTSs are terminating.

```lean
theorem Bounded.toTerminating (h : lts.Bounded) : lts.Terminating
```

`Cslib.LTS.bounded_terminating` (instance, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L50))

> A bounded LTS is available as a terminating LTS through typeclass inference.

```lean
instance bounded_terminating [lts.Bounded] : lts.Terminating
```

`Cslib.LTS.Terminating.toAcyclic` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L54))

> Terminating LTSs are acyclic.

```lean
theorem Terminating.toAcyclic (h : lts.Terminating) : lts.Acyclic
```

`Cslib.LTS.terminating_acyclic` (instance, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L58))

> A terminating LTS is available as an acyclic LTS through typeclass inference.

```lean
instance terminating_acyclic [lts.Terminating] : lts.Acyclic
```

`Cslib.LTS.Acyclic.toBoundedUpTo` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L63))

> On a finite state space, an acyclic LTS has execution length strictly less than the number of
> states.

```lean
theorem Acyclic.toBoundedUpTo [Finite State] (h : lts.Acyclic) :
    lts.BoundedUpTo (Nat.card State)
```

`Cslib.LTS.Acyclic.toBounded` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L76))

> On a finite state space, acyclic LTSs are bounded.

```lean
theorem Acyclic.toBounded [Finite State] (h : lts.Acyclic) : lts.Bounded
```

`Cslib.LTS.Acyclic.toTerminating` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L80))

> On a finite state space, acyclic LTSs are terminating.

```lean
theorem Acyclic.toTerminating [Finite State] (h : lts.Acyclic) : lts.Terminating
```

`Cslib.LTS.MayTerminate` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L85))

> A state 'may terminate' if it can reach a terminated state. The definition of `Terminated`
> is a parameter.

```lean
def MayTerminate (s : State) : Prop
```

`Cslib.LTS.Stuck` (definition, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean#L89))

> A state 'is stuck' if it is not terminated and cannot go forward. The definition of `Terminated`
> is a parameter.

```lean
def Stuck (s : State) : Prop
```

## Depends on

- [Labelled Transition System (LTS)](basic.md)

## Proof depends on

- [Termination (well-foundedness) properties of relations](../../relation/termination.md)
- [Finite executions of LTS](execution.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Termination.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Termination.lean)
