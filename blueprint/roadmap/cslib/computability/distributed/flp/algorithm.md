---
catalog: module
lean: Cslib.FLP.Message, Cslib.FLP.ProcState, Cslib.FLP.State, Cslib.FLP.Algorithm, Cslib.FLP.Action, Cslib.FLP.DestIn, Cslib.FLP.Algorithm.start, Cslib.FLP.Algorithm.recvMsg, Cslib.FLP.Algorithm.lts, Cslib.FLP.Algorithm.Reachable, Cslib.FLP.State.ProcDecided, Cslib.FLP.State.Decided, Cslib.FLP.State.Agreed, Cslib.FLP.Algorithm.SafeConsensus, Cslib.FLP.Algorithm.tr_none, Cslib.FLP.Algorithm.reachable_start, Cslib.FLP.Algorithm.reachable_stable, Cslib.FLP.Algorithm.procDecided_stable, Cslib.FLP.Algorithm.decided_stable, Cslib.FLP.Algorithm.recvMsg_comm, Cslib.FLP.Algorithm.tr_diamond, Cslib.FLP.Algorithm.mTr_notRcvd_enabled, Cslib.FLP.Algorithm.omega_notRcvd_enabled
statement: formalized
proof: formalized
---

# Distributed algorithms for solving the consensus problem

`Cslib.Computability.Distributed.FLP.Algorithm`, in [Cslib/Computability/Distributed/FLP/Algorithm.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean), by Ching-Tsun Chou.

> In the consensus problem, each process of a distributed algorithm is given a boolean value
> at the beginning.  Then by exchanging messages asynchronously, they are supposed to agree on
> one of the initial boolean values. This file contains a very general definition of such
> a distributed algorithm.
>
> Borrowing an idea from Leslie Lamport, we allow the LTS defined by such an algorithm to
> "stutter" at any time, in the sense of taking a dummy step without changing the
> global state of the distributed algorithm.  This idea enables us to focus on infinite
> executions alone without loss of generality, because an algorithm that has run out of
> useful steps to take can always take the stuttering step.  Pathological executions in which
> the stuttering step is taken forever when there is useful work to be done are outlawed by
> the fairness assumptions defined in `Consensus.lean`.
>
> The types `P`, `M`, and `S` below are the types of processes (more precisely, process identifiers),
> messages contents, and process states.  Eventually `P` will be assumed to be finite in the form of
> `[Fintype P]`, but that assumption will be added only where necessary.  No assumption whatsoever
> will be made about `M` and `S`.  In particular, they could be infinite.

`Cslib.FLP.Message` (structure, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L42))

> The type of messages that processes send to each other.

```lean
structure Message (P M : Type*) where
  /-- The destination of a message. -/
  dest : P
  /-- The content of the message, where the `Bool` option is used to carry to the
      initial boolean value to each process. -/
  msg : Bool ⊕ M
deriving DecidableEq
```

`Cslib.FLP.ProcState` (structure, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L51))

> The type of a process's local state.

```lean
structure ProcState (S : Type*) where
  /-- The internal state of a process. -/
  state : S
  /-- The state component used by a process to signal the boolean value it decides on. -/
  out : Option Bool
```

`Cslib.FLP.State` (structure, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L58))

> The global state of the distributed algorithm.

```lean
structure State (P M S : Type*) where
  /-- A multiset containing all messages that are in-flight (namely, they have been sent but
  not yet received). Note that being a multiset implies that the messages are not ordered. -/
  msgs : Multiset (Message P M)
  /-- A map giving the local states of all processes. -/
  proc : P → ProcState S
```

`Cslib.FLP.Algorithm` (structure, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L69))

> The specification of a distributed algorithm for solving the consensus problem.
> Note that each field below can depend on a process's identifier (recall that each `Message`
> contains its destination's identifier), so the algorithm is not required to be uniform
> across processes.

```lean
structure Algorithm (P M S : Type*) where
  /-- A map specifying the initial state of each process. -/
  init : P → S
  /-- A map specifying how a process changes its internal state upon receiving a message. -/
  next : Message P M → ProcState S → S
  /-- A map specifying what messages a process sends out upon receiving a message. -/
  send : Message P M → ProcState S → Multiset (Message P M)
  /-- A map specifying the boolean decision a process makes upon receiving a message,
      where `none` means that no decision is made. -/
  out : Message P M → ProcState S → Option Bool
```

`Cslib.FLP.Action` (abbreviation, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L82))

> The type of labels of the LTS defined by an `Algorithm`, where `some m` denotes
> the reception of message `m` and `none` denotes a stuttering step.

```lean
abbrev Action (P M : Type*)
```

`Cslib.FLP.DestIn` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L85))

> `DestIn ps x` means that if `x ≠ none`, then `x = some m` with `m.dest ∈ ps`.

```lean
def DestIn (ps : Set P) : Action P M → Prop
```

`Cslib.FLP.Algorithm.start` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L93))

> Given `inp : P → Bool`, the initial state of the algorithm `a` contains a single message
> carrying the boolean value `inp p` to each process `p`, where the initial internal state is
> `a.init p` and no decision has been made.  The assumption `[Fintype P]` is made because
> a multiset may contain only finitely many elements.

```lean
def Algorithm.start [Fintype P] (a : Algorithm P M S) (inp : P → Bool) : State P M S
```

`Cslib.FLP.Algorithm.recvMsg` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L101))

> The specification of how the global state of the algorithm changes when a process `p`
> receives a message `m`.  (This function will be used only when such a message `m` exists.)
> Note that once `p` has made a boolean decision in its `out` field, it is not allowed to
> "change its mind" anymore.

```lean
def Algorithm.recvMsg (a : Algorithm P M S) (m : Message P M) (s : State P M S) : State P M S
```

`Cslib.FLP.Algorithm.lts` (definition, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L112))

> The transition relation of the LTS defined by the algorithm `a`.
> Note that the stuttering step is always allowed.

```lean
def Algorithm.lts (a : Algorithm P M S) : LTS (State P M S) (Action P M)
```

`Cslib.FLP.Algorithm.Reachable` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L118))

> `a.Reachable inp s` means that `s` is a reachable state of `a` given the initial `inp`.

```lean
def Algorithm.Reachable [Fintype P]
    (a : Algorithm P M S) (inp : P → Bool) (s : State P M S) : Prop
```

`Cslib.FLP.State.ProcDecided` (abbreviation, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L124))

> `s.ProcDecided p b` means that process `p` is decided on the boolean value `b`
> in the state `s`.

```lean
abbrev State.ProcDecided (s : State P M S) (p : P) (b : Bool) : Prop
```

`Cslib.FLP.State.Decided` (definition, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L129))

> `s.Decided b` means that at least one process is decided on the boolean value `b`
> in the state `s`.

```lean
def State.Decided (s : State P M S) (b : Bool) : Prop
```

`Cslib.FLP.State.Agreed` (definition, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L133))

> `s.Agreed` says that all boolean values decided on in state `s` must agree with each other.

```lean
def State.Agreed (s : State P M S) : Prop
```

`Cslib.FLP.Algorithm.SafeConsensus` (definition, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L140))

> `a.SafeConsensus` says that in any reachable state of `a`, (1) all boolean values decided on
> in that state must agree with each other and (2) that boolean value (if it exists) must be
> one of the boolean values given by `inp` at the beginning.  `a.SafeConsensus` is the minimal
> correctness requirement on `a` and is a safety property (hence its name).

```lean
def Algorithm.SafeConsensus [Fintype P] (a : Algorithm P M S) : Prop
```

`Cslib.FLP.Algorithm.tr_none` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L148))

> The stuttering step does not change the global state.

```lean
theorem tr_none {s s' : State P M S} (h : a.lts.Tr s none s') : s = s'
```

`Cslib.FLP.Algorithm.reachable_start` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L152))

> The initial state is reachable.

```lean
theorem reachable_start [Fintype P] :
    a.Reachable inp (a.start inp)
```

`Cslib.FLP.Algorithm.reachable_stable` (theorem, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L158))

> If `s` is reachable from the initial state and `s'` is reachable from `s`,
> then `s'` is reachable from the initial state.

```lean
theorem reachable_stable [Fintype P] {s s' : State P M S}
    (hr : a.Reachable inp s) (hc : a.lts.CanReach s s') : a.Reachable inp s'
```

`Cslib.FLP.Algorithm.procDecided_stable` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L167))

> If `p` is decided on the boolean value `b` in `s` and `s'` is reachable from `s`,
> then `p` is still decided on `b` in `s'`.

```lean
theorem procDecided_stable {s s' : State P M S} {p : P} {b : Bool}
    (hd : s.ProcDecided p b) (hc : a.lts.CanReach s s') : s'.ProcDecided p b
```

`Cslib.FLP.Algorithm.decided_stable` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L174))

> If at least one process is decided on the boolean value `b` in `s` and `s'` is reachable
> from `s`, then at least one process is still decided on `b` in `s'`.

```lean
theorem decided_stable {s s' : State P M S} {b : Bool}
    (hd : s.Decided b) (hc : a.lts.CanReach s s') : s'.Decided b
```

`Cslib.FLP.Algorithm.recvMsg_comm` (theorem, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L182))

> If `m1` and `m2` are both inflight and they have different destinations,
> then receiving them in either order produces the same end state.

```lean
theorem recvMsg_comm {m1 m2 : Message P M} {s : State P M S}
    (hd : m1.dest ≠ m2.dest) (h1 : m1 ∈ s.msgs) (h2 : m2 ∈ s.msgs) :
    m2 ∈ (a.recvMsg m1 s).msgs ∧ m1 ∈ (a.recvMsg m2 s).msgs ∧
    a.recvMsg m2 (a.recvMsg m1 s) = a.recvMsg m1 (a.recvMsg m2 s)
```

`Cslib.FLP.Algorithm.tr_diamond` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L201))

> A diamond property for the transition relation `a.lts.Tr`.

```lean
theorem tr_diamond {ps : Set P} {x1 x2 : Action P M} {s s1 s2 : State P M S}
    (hx1 : DestIn ps x1) (hs1 : a.lts.Tr s x1 s1)
    (hx2 : DestIn psᶜ x2) (hs2 : a.lts.Tr s x2 s2) :
    ∃ s', a.lts.Tr s1 x2 s' ∧ a.lts.Tr s2 x1 s'
```

`Cslib.FLP.Algorithm.mTr_notRcvd_enabled` (theorem, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L218))

> A message that is in-flight stays in-flight as long as it is not received
> (finite execution version).

```lean
theorem mTr_notRcvd_enabled {s t : State P M S} {xl : List (Action P M)} {m : Message P M}
    (hst : a.lts.MTr s xl t) (hs : m ∈ s.msgs) (hxl : ¬ some m ∈ xl) : m ∈ t.msgs
```

`Cslib.FLP.Algorithm.omega_notRcvd_enabled` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean#L228))

> A message that is in-flight stays in-flight as long as it is not received
> (infinite execution version).

```lean
theorem omega_notRcvd_enabled
    {ss : ωSequence (State P M S)} {xs : ωSequence (Action P M)} {k : ℕ} {m : Message P M}
    (he : a.lts.OmegaExecution ss xs) (hm : m ∈ (ss k).msgs) (hn : ∀ j, k ≤ j → xs j ≠ some m) :
    ∀ j, k ≤ j → m ∈ (ss j).msgs
```

## Depends on

- [Infinite executions of LTS](../../../foundations/semantics/lts/omegaexecution.md)

## Sources

- [Cslib/Computability/Distributed/FLP/Algorithm.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Algorithm.lean)
