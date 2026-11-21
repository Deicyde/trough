---
catalog: module
lean: EStateM.Result.map, EStateM.Result.map_ok, EStateM.Result.map_error, EStateM.Result.map_eq_ok, EStateM.Result.map_eq_error, EStateM.dummySave_apply, EStateM.dummyRestore_apply, EStateM.run'_pure, EStateM.run'_bind, EStateM.run_map, EStateM.run'_map, EStateM.run_seq, EStateM.run'_seq, EStateM.run_seqLeft, EStateM.run'_seqLeft, EStateM.run_seqRight, EStateM.run'_seqRight, EStateM.run'_get, EStateM.run'_set, EStateM.run'_modify, EStateM.run'_modifyGet, EStateM.run_getModify, EStateM.run'_getModify, EStateM.run'_throw, EStateM.run_orElse, EStateM.run'_orElse, EStateM.run_tryCatch, EStateM.run'_tryCatch, EStateM.run'_adaptExcept, EStateM.run_tryFinally', EStateM.run'_tryFinally', EStateM.run_fromStateM, EStateM.run'_fromStateM, EStateM.ext
statement: formalized
proof: formalized
---

# EStateM

`Batteries.Lean.EStateM`, in [Batteries/Lean/EStateM.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean), by Kim Morrison.

`EStateM.Result.map` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L18))

> Map a function over an `EStateM.Result`, preserving states and errors.

```lean
def map {ε σ α β} (f : α → β) (x : Result ε σ α) : Result ε σ β
```

`EStateM.Result.map_ok` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L23))

```lean
theorem map_ok {ε σ α β} (f : α → β) (a : α) (s : σ) :
    (Result.ok a s : Result ε σ α).map f = .ok (f a) s
```

`EStateM.Result.map_error` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L26))

```lean
theorem map_error {ε σ α β} (f : α → β) (e : ε) (s : σ) :
    (Result.error e s : Result ε σ α).map f = .error e s
```

`EStateM.Result.map_eq_ok` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L29))

```lean
theorem map_eq_ok {ε σ α β} {f : α → β} {x : Result ε σ α} {b : β} {s : σ} :
    x.map f = .ok b s ↔ ∃ a, x = .ok a s ∧ b = f a
```

`EStateM.Result.map_eq_error` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L33))

```lean
theorem map_eq_error {ε σ α β} (f : α → β) {x : Result ε σ α} {e : ε} {s : σ} :
    x.map f = .error e s ↔ x = .error e s
```

`EStateM.dummySave_apply` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L39))

```lean
theorem dummySave_apply (s : σ) : EStateM.dummySave s = PUnit.unit
```

`EStateM.dummyRestore_apply` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L41))

```lean
theorem dummyRestore_apply (s : σ) : EStateM.dummyRestore s = Function.const _ s
```

`EStateM.run'_pure` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L43))

```lean
theorem run'_pure (x : α) (s : σ) :
    (pure x : EStateM ε σ α).run' s = some x
```

`EStateM.run'_bind` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L46))

```lean
theorem run'_bind (x : EStateM ε σ α) (f : α → EStateM ε σ β) (s : σ) :
    (x >>= f).run' s = match x.run s with
    | .ok a s => (f a).run' s
    | .error _ _ => none
```

`EStateM.run_map` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L53))

```lean
theorem run_map (f : α → β) (x : EStateM ε σ α) (s : σ) :
    (f <$> x).run s = (x.run s).map f
```

`EStateM.run'_map` (theorem, [line 56](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L56))

```lean
theorem run'_map (f : α → β) (x : EStateM ε σ α) (s : σ) :
    (f <$> x).run' s = Option.map f (x.run' s)
```

`EStateM.run_seq` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L61))

```lean
theorem run_seq (f : EStateM ε σ (α → β)) (x : EStateM ε σ α) (s : σ) :
    (f <*> x).run s = match f.run s with
    | .ok g s => Result.map g (x.run s)
    | .error e s => .error e s
```

`EStateM.run'_seq` (theorem, [line 68](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L68))

```lean
theorem run'_seq (f : EStateM ε σ (α → β)) (x : EStateM ε σ α) (s : σ) :
    (f <*> x).run' s = match f.run s with
    | .ok g s => Option.map g (x.run' s)
    | .error _ _ => none
```

`EStateM.run_seqLeft` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L75))

```lean
theorem run_seqLeft (x : EStateM ε σ α) (y : EStateM ε σ β) (s : σ) :
    (x <* y).run s = match x.run s with
    | .ok v s => Result.map (fun _ => v) (y.run s)
    | .error e s => .error e s
```

`EStateM.run'_seqLeft` (theorem, [line 82](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L82))

```lean
theorem run'_seqLeft (x : EStateM ε σ α) (y : EStateM ε σ β) (s : σ) :
    (x <* y).run' s = match x.run s with
    | .ok v s => Option.map (fun _ => v) (y.run' s)
    | .error _ _ => none
```

`EStateM.run_seqRight` (theorem, [line 88](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L88))

```lean
theorem run_seqRight (x : EStateM ε σ α) (y : EStateM ε σ β) (s : σ) :
    (x *> y).run s = match x.run s with
    | .ok _ s => y.run s
    | .error e s => .error e s
```

`EStateM.run'_seqRight` (theorem, [line 93](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L93))

```lean
theorem run'_seqRight (x : EStateM ε σ α) (y : EStateM ε σ β) (s : σ) :
    (x *> y).run' s = match x.run s with
    | .ok _ s => y.run' s
    | .error _ _ => none
```

`EStateM.run'_get` (theorem, [line 100](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L100))

```lean
theorem run'_get (s : σ) :
    (get : EStateM ε σ σ).run' s = some s
```

`EStateM.run'_set` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L103))

```lean
theorem run'_set (v s : σ) :
    (set v : EStateM ε σ PUnit).run' s = some PUnit.unit
```

`EStateM.run'_modify` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L106))

```lean
theorem run'_modify (f : σ → σ) (s : σ) :
    (modify f : EStateM ε σ PUnit).run' s = some PUnit.unit
```

`EStateM.run'_modifyGet` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L109))

```lean
theorem run'_modifyGet (f : σ → α × σ) (s : σ) :
    (modifyGet f : EStateM ε σ α).run' s = some (f s).1
```

`EStateM.run_getModify` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L112))

```lean
theorem run_getModify (f : σ → σ) :
    (getModify f : EStateM ε σ σ).run s = Result.ok s (f s)
```

`EStateM.run'_getModify` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L115))

```lean
theorem run'_getModify (f : σ → σ) (s : σ) :
    (getModify f : EStateM ε σ σ).run' s = some s
```

`EStateM.run'_throw` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L118))

```lean
theorem run'_throw (e : ε) (s : σ) :
    (throw e : EStateM ε σ α).run' s = none
```

`EStateM.run_orElse` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L121))

```lean
theorem run_orElse {δ} [h : Backtrackable δ σ] (x₁ x₂ : EStateM ε σ α) (s : σ) :
    (x₁ <|> x₂).run s = match x₁.run s with
    | .ok x s => .ok x s
    | .error _ s' => x₂.run (restore s' (save s))
```

`EStateM.run'_orElse` (theorem, [line 130](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L130))

```lean
theorem run'_orElse {δ} [h : Backtrackable δ σ] (x₁ x₂ : EStateM ε σ α) (s : σ) :
    (x₁ <|> x₂).run' s = match x₁.run s with
    | .ok x _ => some x
    | .error _ s' => x₂.run' (restore s' (save s))
```

`EStateM.run_tryCatch` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L137))

```lean
theorem run_tryCatch {δ} [h : Backtrackable δ σ]
    (body : EStateM ε σ α) (handler : ε → EStateM ε σ α) (s : σ) :
    (tryCatch body handler).run s = match body.run s with
    | .ok x s => .ok x s
    | .error e s' => (handler e).run (restore s' (save s))
```

`EStateM.run'_tryCatch` (theorem, [line 147](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L147))

```lean
theorem run'_tryCatch {δ} [h : Backtrackable δ σ]
    (body : EStateM ε σ α) (handler : ε → EStateM ε σ α) (s : σ) :
    (tryCatch body handler).run' s = match body.run s with
    | .ok x _ => some x
    | .error e s' => (handler e).run' (restore s' (save s))
```

`EStateM.run'_adaptExcept` (theorem, [line 155](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L155))

```lean
theorem run'_adaptExcept (f : ε → ε) (x : EStateM ε σ α) (s : σ) :
    (adaptExcept f x).run' s = x.run' s
```

`EStateM.run_tryFinally'` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L160))

```lean
theorem run_tryFinally' (x : EStateM ε σ α)
    (h : Option α → EStateM ε σ β) (s : σ) : (tryFinally' x h).run s = match x.run s with
    | .ok a s => match (h (some a)).run s with
      | .ok b s => Result.ok (a, b) s
      | .error e s => Result.error e s
    | .error e₁ s => match (h none).run s with
      | .ok _ s => Result.error e₁ s
      | .error e₂ s => Result.error e₂ s
```

`EStateM.run'_tryFinally'` (theorem, [line 169](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L169))

```lean
theorem run'_tryFinally' (x : EStateM ε σ α)
    (h : Option α → EStateM ε σ β) (s : σ) :
    (tryFinally' x h).run' s = match x.run s with
    | .ok a s => Option.map (a, ·) ((h (some a)).run' s)
    | .error _ _ => none
```

`EStateM.run_fromStateM` (theorem, [line 179](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L179))

```lean
theorem run_fromStateM (x : StateM σ α) (s : σ) :
    (fromStateM x : EStateM ε σ α).run s =
    Result.ok (x.run s).1 (x.run s).2
```

`EStateM.run'_fromStateM` (theorem, [line 183](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L183))

```lean
theorem run'_fromStateM (x : StateM σ α) (s : σ) :
    (fromStateM x : EStateM ε σ α).run' s = some (x.run' s)
```

`EStateM.ext` (theorem, [line 186](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean#L186))

```lean
theorem ext {ε σ α} {x y : EStateM ε σ α} (h : ∀ s, x.run s = y.run s) : x = y
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/EStateM.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/EStateM.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.EStateM.json)
