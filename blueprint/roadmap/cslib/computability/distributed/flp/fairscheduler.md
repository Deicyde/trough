---
catalog: module
lean: Cslib.FLP.DeliverMsg, Cslib.FLP.DeliverMsg.ForallActions, Cslib.FLP.DeliverMsg.foldList, Cslib.FLP.DeliverMsg.scheduleMsgs, Cslib.FLP.DeliverMsg.foldList_forallActions, Cslib.FLP.Algorithm.fairScheduler, Cslib.FLP.Algorithm.fairSegEnds, Cslib.FLP.Algorithm.fairSegActions, Cslib.FLP.Algorithm.FairDeliverMsg, Cslib.FLP.FairScheduler.fairScheduler_init, Cslib.FLP.FairScheduler.fairScheduler_step, Cslib.FLP.FairScheduler.fairSeg_forallActions, Cslib.FLP.FairScheduler.fairDeliverMsg_foldList, Cslib.FLP.FairScheduler.fairDeliverMsg_scheduleMsgs, Cslib.FLP.FairScheduler.fair_fairSegs, Cslib.FLP.FairScheduler.flatten_fairSegs, Cslib.FLP.FairScheduler.fair_omegaExecution, Cslib.FLP.FairScheduler.omega_forall_actions
statement: formalized
proof: formalized
---

# Machinery for constructing infinite fair executions

`Cslib.Computability.Distributed.FLP.FairScheduler`, in [Cslib/Computability/Distributed/FLP/FairScheduler.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean), by Ching-Tsun Chou.

> The main goal of this file is to define a `fairScheduler` that, given a function `d`
> of type `DeliverMsg`, a state predicate `q`, and a state `s0` of an algorithm `a`,
> constructs an infinite execution of `a` starting from state `s0` in which all processes
> from a set `ps` are fair and `q` is true infinitely often.  With additional assumptions,
> we may also want to require that all actions in the infinite execution satisfy an action
> predicate `r`.

`Cslib.FLP.DeliverMsg` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L32))

> Given a state `s` and a message `m`, a function `d` of type `DeliverMsg` is supposed to
> return `(xs, t)` where `xs` is a finite execution from `s` to `t` in which `m` is delivered.

```lean
def DeliverMsg P M S
```

`Cslib.FLP.DeliverMsg.ForallActions` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L35))

> `d.ForallActions r` requires that all actions returned by `d` satisfy `r`.

```lean
def DeliverMsg.ForallActions (d : DeliverMsg P M S) (r : Action P M → Prop) : Prop
```

`Cslib.FLP.DeliverMsg.foldList` (definition, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L41))

> `d.foldList s ml ms` uses `d` to deliver all messages that are in `ml` but not in `ms` from
> state `s`. Note that if a message `m` in `ml` is delivered during the delivery of an earlier
> message, `m` is added to `ms` so that it is not processed again.

```lean
def DeliverMsg.foldList (d : DeliverMsg P M S) (s : State P M S) :
    List (Message P M) → Finset (Message P M) → List (Action P M) × State P M S
```

`Cslib.FLP.DeliverMsg.scheduleMsgs` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L57))

> `d.scheduleMsgs ps s` schedules and delivers all messages which are in-flight in state `s`
> and have destinations in `ps` in some order (as determined by choice).  If no such message exists,
> then the the stuttering step is taken.

```lean
noncomputable def DeliverMsg.scheduleMsgs (d : DeliverMsg P M S) (ps : Set P)
    (s : State P M S) : List (Action P M) × State P M S
```

`Cslib.FLP.DeliverMsg.foldList_forallActions` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L70))

> If `d.ForallActions r`, then `d.foldList s ml ms` can only use actions satisfying `r`.

```lean
theorem foldList_forallActions {r : Action P M → Prop}
    (s : State P M S) (ml : List (Message P M)) (ms : Finset (Message P M))
    (h : d.ForallActions r) : (d.foldList s ml ms).fst.Forall r
```

`Cslib.FLP.Algorithm.fairScheduler` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L80))

> Starting from state `s0`, `a.fairScheduler d ps s0` constructs an infinite sequence of
> finite executions of `a` by repeatedly applying `d.scheduleMsgs ps`.

```lean
noncomputable def Algorithm.fairScheduler (a : Algorithm P M S) (d : DeliverMsg P M S) (ps : Set P)
    (s0 : State P M S) : ℕ → List (Action P M) × State P M S
```

`Cslib.FLP.Algorithm.fairSegEnds` (definition, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L87))

> The infinite sequence of states forming the end states of the finite executions constructed
> by `Algorithm.fairScheduler`.

```lean
noncomputable def Algorithm.fairSegEnds (a : Algorithm P M S) (d : DeliverMsg P M S)
    (ps : Set P) (s0 : State P M S) : ωSequence (State P M S)
```

`Cslib.FLP.Algorithm.fairSegActions` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L93))

> The infinite sequence of finite action sequences from the finite executions constructed
> by `Algorithm.fairScheduler`.

```lean
noncomputable def Algorithm.fairSegActions (a : Algorithm P M S) (d : DeliverMsg P M S)
    (ps : Set P) (s0 : State P M S) : ωSequence (List (Action P M))
```

`Cslib.FLP.Algorithm.FairDeliverMsg` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L101))

> `a.FairDeliverMsg d ps q` says that for any state `s` of `a` satisfying `q` and
> any message `m` which is in-flight in `s` and whose destination is in `ps`, `d s m`
> produces a legal finite execution of `a` in which `m` is delivered and which ends in
> a state satisfying `q` again.

```lean
def Algorithm.FairDeliverMsg (a : Algorithm P M S) (d : DeliverMsg P M S)
    (ps : Set P) (q : State P M S → Prop) : Prop
```

`Cslib.FLP.FairScheduler.fairScheduler_init` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L113))

> Re-stating the definition of `Algorithm.fairScheduler` as a mutual recursion of
> `Algorithm.fairSegEnds` and `Algorithm.fairSegActions`.

```lean
theorem fairScheduler_init {d : DeliverMsg P M S} (ps : Set P) (s0 : State P M S) :
    a.fairSegEnds d ps s0 0 = s0
```

`Cslib.FLP.FairScheduler.fairScheduler_step` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L119))

> Re-stating the definition of `Algorithm.fairScheduler` as a mutual recursion of
> `Algorithm.fairSegEnds` and `Algorithm.fairSegActions`.

```lean
theorem fairScheduler_step {d : DeliverMsg P M S} (ps : Set P) (s0 : State P M S) (k : ℕ) :
    d.scheduleMsgs ps (a.fairSegEnds d ps s0 k) =
    (a.fairSegActions d ps s0 k, a.fairSegEnds d ps s0 (k + 1))
```

`Cslib.FLP.FairScheduler.fairSeg_forallActions` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L125))

> If `d.ForallActions r`, then `a.fairSegActions d ps s0` can only use actions satisfying `r`.

```lean
theorem fairSeg_forallActions {d : DeliverMsg P M S} {r : Action P M → Prop}
    (ps : Set P) (s0 : State P M S) (k : ℕ) (ha : d.ForallActions r) (hn : r none) :
    (a.fairSegActions d ps s0 k).Forall r
```

`Cslib.FLP.FairScheduler.fairDeliverMsg_foldList` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L132))

> The correctness of `d.foldList s ml ms` under the assumption `a.FairDeliverMsg d ps q`.

```lean
theorem fairDeliverMsg_foldList {d : DeliverMsg P M S} {ps : Set P} {q : State P M S → Prop}
    (hd : a.FairDeliverMsg d ps q) (s : State P M S)
    (ml : List (Message P M)) (ms : Finset (Message P M))
    (hs : q s ∧ ∀ m, m ∈ ml → ¬ m ∈ ms → m ∈ s.msgs ∧ m.dest ∈ ps) :
    let (xl, t) := d.foldList s ml ms
    a.lts.MTr s xl t ∧ q t ∧ ∀ m, m ∈ ml → ¬ m ∈ ms → some m ∈ xl
```

`Cslib.FLP.FairScheduler.fairDeliverMsg_scheduleMsgs` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L153))

> The correctness of `d.scheduleMsgs ps s` under the assumption `a.FairDeliverMsg d ps q`.

```lean
theorem fairDeliverMsg_scheduleMsgs {d : DeliverMsg P M S} {ps : Set P} {q : State P M S → Prop}
    (hd : a.FairDeliverMsg d ps q) (s : State P M S) (hs : q s) :
    let xl := (d.scheduleMsgs ps s).fst
    let t := (d.scheduleMsgs ps s).snd
    q t ∧ a.lts.MTr s xl t ∧ 0 < xl.length ∧ ∀ m, m ∈ s.msgs → m.dest ∈ ps → some m ∈ xl
```

`Cslib.FLP.FairScheduler.fair_fairSegs` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L177))

> The correctness of `a.fairSegEnds d ps s0` and `a.fairSegActions d ps s0`
> under the assumption `a.FairDeliverMsg d ps q`.

```lean
theorem fair_fairSegs {d : DeliverMsg P M S} {ps : Set P} {q : State P M S → Prop}
    (hd : a.FairDeliverMsg d ps q) (s0 : State P M S) (hs0 : q s0) :
    let ts := a.fairSegEnds d ps s0
    let xls := a.fairSegActions d ps s0
    ∀ k, q (ts k) ∧ a.lts.MTr (ts k) (xls k) (ts (k + 1)) ∧ 0 < (xls k).length ∧
      ∀ m, m ∈ (ts k).msgs → m.dest ∈ ps → some m ∈ xls k
```

`Cslib.FLP.FairScheduler.flatten_fairSegs` (theorem, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L190))

> Given an infinite sequence of non-empty finite executions of algorithm `a`,
> if all messages with destinations in `ps` that are in-flight at the beginning of each
> finite execution are delivered in that finite execution, then those finite executions can
> be concatenated into an infinite execution of `a` in which every process in `ps` is fair.

```lean
theorem flatten_fairSegs {ps : Set P}
    {ts : ωSequence (State P M S)} {xls : ωSequence (List (Action P M))}
    (hmtr : ∀ k, a.lts.MTr (ts k) (xls k) (ts (k + 1)))
    (hpos : ∀ k, 0 < (xls k).length)
    (hsch : ∀ k m, m ∈ (ts k).msgs → m.dest ∈ ps → some m ∈ xls k) :
    ∃ ss, a.lts.OmegaExecution ss xls.flatten ∧ (∀ k, ss (xls.cumLen k) = ts k) ∧
      ∀ p, p ∈ ps → ProcFair p ss xls.flatten
```

`Cslib.FLP.FairScheduler.fair_omegaExecution` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L212))

> Under the assumption `a.FairDeliverMsg d ps q`, the infinite sequence of finite executions
> of `a` represented by `a.fairSegEnds d ps s0` and `a.fairSegActions d ps s0` can be concatenated
> into an infinite execution of `a` in which every process in `ps` is fair and `q` is true at
> the ends of all those finite executions.

```lean
theorem fair_omegaExecution {d : DeliverMsg P M S} {ps : Set P} {q : State P M S → Prop}
    (hd : a.FairDeliverMsg d ps q) (s0 : State P M S) (hs0 : q s0) :
    let ts := a.fairSegEnds d ps s0
    let xls := a.fairSegActions d ps s0
    ∃ ss, a.lts.OmegaExecution ss xls.flatten ∧
      ss 0 = s0 ∧ (∀ k, ss (xls.cumLen k) = ts k) ∧
      (∀ k, q (ss (xls.cumLen k))) ∧ (∀ k, 0 < (xls k).length) ∧
      ∀ p, p ∈ ps → ProcFair p ss xls.flatten
```

`Cslib.FLP.FairScheduler.omega_forall_actions` (theorem, [line 233](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean#L233))

> If `d.ForallActions r`, then the concatenation of all `a.fairSegActions d ps s0` segments
> can only use actions satisfying `r`.

```lean
theorem omega_forall_actions {d : DeliverMsg P M S} {ps : Set P}
    {q : State P M S → Prop} {r : Action P M → Prop}
    (hd : a.FairDeliverMsg d ps q) (s0 : State P M S) (hs0 : q s0)
    (ha : d.ForallActions r) (hn : r none) :
    ∀ k, r ((a.fairSegActions d ps s0).flatten k)
```

## Depends on

- [Fault-tolerant consensus](consensus.md)

## Sources

- [Cslib/Computability/Distributed/FLP/FairScheduler.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/FairScheduler.lean)
