---
catalog: module
lean: Cslib.DistributedConsistency.Transition, Cslib.DistributedConsistency.Transition.op, Cslib.DistributedConsistency.Transition.rcv, Cslib.DistributedConsistency.Transition.proc, Cslib.DistributedConsistency.Transition.pre, Cslib.DistributedConsistency.Transition.post, Cslib.DistributedConsistency.Transition.snd, Cslib.DistributedConsistency.Transition.rval
statement: formalized
proof: formalized
---

# Transitions

`Cslib.Computability.Distributed.Consistency.Transition`, in [Cslib/Computability/Distributed/Consistency/Transition.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean), by Ching-Tsun Chou.

> A transition models an atomic step in a concrete execution and has various attributes
> depending on its type.
>
> This file formalizes section 7.1 of [Burckhardt2014].
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Cslib.DistributedConsistency.Transition` (inductive type, [line 30](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L30))

> Transition datatype.

```lean
inductive Transition (State Operation Value Message Process : Type*)
  /-- Initialization transition. -/
  | init : State → Set Message → Transition State Operation Value Message Process
  /-- Operation call. -/
  | call : Operation → State → State → Set Message →
    Transition State Operation Value Message Process
  /-- Operation call + return transition. -/
  | callret : Operation → State → State → Set Message → Value →
    Transition State Operation Value Message Process
  /-- Message receive transition. -/
  | recv : Message → State → State → Set Message →
    Transition State Operation Value Message Process
  /-- Message receive + return transition. -/
  | recvret : Message → State → State → Set Message → Value →
    Transition State Operation Value Message Process
  /-- Process step transition. -/
  | step : Process → State → State → Set Message →
    Transition State Operation Value Message Process
  /-- Process step + return transition. -/
  | stepret : Process → State → State → Set Message → Value →
    Transition State Operation Value Message Process
```

> ### Partial functions for accessing the attributes of a transition.

`Cslib.DistributedConsistency.Transition.op` (definition, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L57))

> The operation of a transition.

```lean
def op : Transition State Operation Value Message Process → Option Operation
```

`Cslib.DistributedConsistency.Transition.rcv` (definition, [line 62](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L62))

> The received message of a transition.

```lean
def rcv : Transition State Operation Value Message Process → Option Message
```

`Cslib.DistributedConsistency.Transition.proc` (definition, [line 67](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L67))

> The process of a transition.

```lean
def proc : Transition State Operation Value Message Process → Option Process
```

`Cslib.DistributedConsistency.Transition.pre` (definition, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L72))

> The previous state of a transition.

```lean
def pre : Transition State Operation Value Message Process → Option State
```

`Cslib.DistributedConsistency.Transition.post` (definition, [line 79](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L79))

> The next state of a transition.

```lean
def post : Transition State Operation Value Message Process → Option State
```

`Cslib.DistributedConsistency.Transition.snd` (definition, [line 86](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L86))

> The set of messages sent by a transition.

```lean
def snd : Transition State Operation Value Message Process → Set Message
```

`Cslib.DistributedConsistency.Transition.rval` (definition, [line 93](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean#L93))

> The value returned by a transition.

```lean
def rval : Transition State Operation Value Message Process → Option Value
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Distributed/Consistency/Transition.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Distributed/Consistency/Transition.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Distributed.Consistency.Transition.json)
