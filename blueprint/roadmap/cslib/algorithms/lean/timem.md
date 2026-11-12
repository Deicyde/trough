---
catalog: module
lean: Cslib.Algorithms.Lean.TimeM, Cslib.Algorithms.Lean.TimeM.pure, Cslib.Algorithms.Lean.TimeM.bind, Cslib.Algorithms.Lean.TimeM.ret_pure, Cslib.Algorithms.Lean.TimeM.ret_bind, Cslib.Algorithms.Lean.TimeM.ret_map, Cslib.Algorithms.Lean.TimeM.ret_mapConst, Cslib.Algorithms.Lean.TimeM.ret_seqRight, Cslib.Algorithms.Lean.TimeM.ret_seqLeft, Cslib.Algorithms.Lean.TimeM.ret_seq, Cslib.Algorithms.Lean.TimeM.isMonadHom_pure_ret, Cslib.Algorithms.Lean.TimeM.time_bind, Cslib.Algorithms.Lean.TimeM.time_pure, Cslib.Algorithms.Lean.TimeM.time_map, Cslib.Algorithms.Lean.TimeM.time_seqRight, Cslib.Algorithms.Lean.TimeM.time_seqLeft, Cslib.Algorithms.Lean.TimeM.time_seq, Cslib.Algorithms.Lean.TimeM.tick, Cslib.Algorithms.Lean.TimeM.ret_tick, Cslib.Algorithms.Lean.TimeM.time_tick
statement: formalized
proof: formalized
---

# TimeM: Time Complexity Monad

`Cslib.Algorithms.Lean.TimeM`, in [Cslib/Algorithms/Lean/TimeM.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean), by Sorrachai Yingchareonthawornhcai, Eric Wieser.

> `TimeM T α` represents a computation that produces a value of type `α` and tracks its time cost.
>
> `T` is usually instantiated as `ℕ` to count operations, but can be instantiated as `ℝ` to count
> actual wall time, or as more complex types in order to model more general costs.
>
> ## Design Principles
> 1. **Pure inputs, timed outputs**: Functions take plain values and return `TimeM` results
> 2. **Time annotations are trusted**: The `time` field is NOT verified against actual cost.
>    You must manually ensure annotations match the algorithm's complexity in your cost model.
> 3. **Separation of concerns**: Prove correctness properties on `.ret`, prove complexity on `.time`
>
> ## Cost Model
> **Document your cost model explicitly** Decide and be consistent about:
> - **What costs 1 unit?** (comparison, arithmetic operation, etc.)
> - **What is free?** (variable lookup, pattern matching, etc.)
> - **Recursive calls:** Do you charge for the call itself?
>
> ## Notation
> - **`✓`** : A tick of time, see `tick`.
> - **`⟪tm⟫`** : Extract the pure value from a `TimeM` computation (notation for `tm.ret`)
>
> ## References
>
> See [Danielsson2008] for the discussion.

`Cslib.Algorithms.Lean.TimeM` (structure, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L50))

> A monad for tracking time complexity of computations.
> `TimeM T α` represents a computation that returns a value of type `α`
> and accumulates a time cost (represented as a type `T`, typically `ℕ`).

```lean
structure TimeM (T : Type*) (α : Type*) where
  /-- The return value of the computation -/
  ret : α
  /-- The accumulated time cost of the computation -/
  time : T
```

`Cslib.Algorithms.Lean.TimeM.pure` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L61))

> Lifts a pure value into a `TimeM` computation with zero time cost.
>
> Prefer to use `pure` instead of `TimeM.pure`.

```lean
protected def pure [Zero T] {α} (a : α) : TimeM T α
```

`Cslib.Algorithms.Lean.TimeM.bind` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L70))

> Sequentially composes two `TimeM` computations, summing their time costs.
>
> Prefer to use the `>>=` notation.

```lean
protected def bind {α β} [Add T] (m : TimeM T α) (f : α → TimeM T β) : TimeM T β
```

`Cslib.Algorithms.Lean.TimeM.ret_pure` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L97))

```lean
theorem ret_pure {α} [Zero T] (a : α) : (pure a : TimeM T α).ret = a
```

`Cslib.Algorithms.Lean.TimeM.ret_bind` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L98))

```lean
theorem ret_bind {α β} [Add T] (m : TimeM T α) (f : α → TimeM T β) :
(m >>= f).ret = (f m.ret).ret
```

`Cslib.Algorithms.Lean.TimeM.ret_map` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L100))

```lean
theorem ret_map {α β} (f : α → β) (x : TimeM T α) : (f <$> x).ret = f x.ret
```

`Cslib.Algorithms.Lean.TimeM.ret_mapConst` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L101))

```lean
theorem ret_mapConst {α β} (a : α) (x : TimeM T β) :
(Functor.mapConst a x).ret = a
```

`Cslib.Algorithms.Lean.TimeM.ret_seqRight` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L103))

```lean
theorem ret_seqRight {α} (x : TimeM T α) (y : Unit → TimeM T β) [Add T] :
(SeqRight.seqRight x y).ret = (y ()).ret
```

`Cslib.Algorithms.Lean.TimeM.ret_seqLeft` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L105))

```lean
theorem ret_seqLeft {α} [Add T] (x : TimeM T α) (y : Unit → TimeM T β) :
(SeqLeft.seqLeft x y).ret = x.ret
```

`Cslib.Algorithms.Lean.TimeM.ret_seq` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L107))

```lean
theorem ret_seq {α β} [Add T] (f : TimeM T (α → β)) (x : Unit → TimeM T α) :
(Seq.seq f x).ret = f.ret (x ()).ret
```

`Cslib.Algorithms.Lean.TimeM.isMonadHom_pure_ret` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L110))

```lean
theorem isMonadHom_pure_ret [AddZero T] : Cslib.IsMonadHom (TimeM T) Id (fun x => pure x.ret)
```

`Cslib.Algorithms.Lean.TimeM.time_bind` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L119))

```lean
theorem time_bind {α β} [Add T] (m : TimeM T α) (f : α → TimeM T β) :
(m >>= f).time = m.time + (f m.ret).time
```

`Cslib.Algorithms.Lean.TimeM.time_pure` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L121))

```lean
theorem time_pure {α} [Zero T] (a : α) : (pure a : TimeM T α).time = 0
```

`Cslib.Algorithms.Lean.TimeM.time_map` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L122))

```lean
theorem time_map {α β} (f : α → β) (x : TimeM T α) : (f <$> x).time = x.time
```

`Cslib.Algorithms.Lean.TimeM.time_seqRight` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L123))

```lean
theorem time_seqRight {α} [Add T] (x : TimeM T α) (y : Unit → TimeM T β) :
(SeqRight.seqRight x y).time = x.time + (y ()).time
```

`Cslib.Algorithms.Lean.TimeM.time_seqLeft` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L125))

```lean
theorem time_seqLeft {α} [Add T] (x : TimeM T α) (y : Unit → TimeM T β) :
(SeqLeft.seqLeft x y).time = x.time + (y ()).time
```

`Cslib.Algorithms.Lean.TimeM.time_seq` (theorem, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L127))

```lean
theorem time_seq {α β} [Add T] (f : TimeM T (α → β)) (x : Unit → TimeM T α) :
(Seq.seq f x).time = f.time + (x ()).time
```

`Cslib.Algorithms.Lean.TimeM.tick` (definition, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L139))

> Creates a `TimeM` computation with a time cost.

```lean
def tick (c : T) : TimeM T PUnit
```

`Cslib.Algorithms.Lean.TimeM.ret_tick` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L141))

```lean
theorem ret_tick (c : T) : (tick c).ret = ()
```

`Cslib.Algorithms.Lean.TimeM.time_tick` (theorem, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean#L142))

```lean
theorem time_tick (c : T) : (tick c).time = c
```

## Depends on

- [(unbundled) morphisms of monads](../../foundations/control/monad/ismonadhom.md)

## Sources

- [Cslib/Algorithms/Lean/TimeM.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/TimeM.lean)
