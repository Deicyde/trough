---
catalog: module
lean: monadStateOf_get_eq_get, monadStateOf_modifyGet_eq_modifyGet, liftM_get, liftM_set, liftM_modify, liftM_modifyGet, liftM_getModify, LawfulMonadStateOf, LawfulMonadStateOf.get_seqRight, LawfulMonadStateOf.seqLeft_get, LawfulMonadStateOf.get_map_const, LawfulMonadStateOf.get_bind_get, LawfulMonadStateOf.get_bind_set, LawfulMonadStateOf.get_bind_map_set, LawfulMonadStateOf.set_bind_get_bind, LawfulMonadStateOf.set_bind_map_get, LawfulMonadStateOf.set_bind_set_bind, LawfulMonadStateOf.set_bind_map_set, LawfulMonadStateOf.modifyGetThe_eq, LawfulMonadStateOf.modify_eq, LawfulMonadStateOf.modifyThe_eq, LawfulMonadStateOf.getModify_eq, LawfulMonadStateOf.modifyGet_eq', LawfulMonadStateOf.modify_id, LawfulMonadStateOf.getModify_id, LawfulMonadStateOf.set_bind_modify, LawfulMonadStateOf.set_bind_modify_bind, LawfulMonadStateOf.set_bind_modifyGet, LawfulMonadStateOf.set_bind_modifyGet_bind, LawfulMonadStateOf.set_bind_getModify, LawfulMonadStateOf.set_bind_getModify_bind, LawfulMonadStateOf.modify_bind_modify, LawfulMonadStateOf.modify_bind_modifyGet, LawfulMonadStateOf.getModify_bind_modify, LawfulMonadStateOf.modify_comm_of_comp_comm, LawfulMonadStateOf.modify_bind_get
statement: formalized
proof: formalized
---

# Laws for Monads with State

`Batteries.Control.LawfulMonadState`, in [Batteries/Control/LawfulMonadState.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean), by Devon Tuma, Quang Dao.

> This file defines a typeclass for `MonadStateOf` with compatible `get` and `set` operations.
>
> Note that we use `MonadStateOf` over `MonadState` as the first induces the second,
> but we phrase things using `MonadStateOf.set` and `MonadState.get` as those are the
> versions that are available at the top level namespace.

`monadStateOf_get_eq_get` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L22))

> The namespaced `MonadStateOf.get` is equal to the `MonadState` provided `get`.

```lean
theorem monadStateOf_get_eq_get [MonadStateOf σ m] :
    (MonadStateOf.get : m σ) = get
```

`monadStateOf_modifyGet_eq_modifyGet` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L26))

> The namespaced `MonadStateOf.modifyGet` is equal to the `MonadState` provided `modifyGet`.

```lean
theorem monadStateOf_modifyGet_eq_modifyGet [MonadStateOf σ m]
    (f : σ → α × σ) : (MonadStateOf.modifyGet f : m α) = modifyGet f
```

`liftM_get` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L29))

```lean
theorem liftM_get {m n}  [MonadStateOf σ m] [MonadLift m n] :
    (liftM (get (m := m)) : n _) = get
```

`liftM_set` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L32))

```lean
theorem liftM_set {m n} [MonadStateOf σ m] [MonadLift m n]
    (s : σ) : (liftM (set (m := m) s) : n _) = set s
```

`liftM_modify` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L35))

```lean
theorem liftM_modify {m n} [MonadStateOf σ m] [MonadLift m n]
    (f : σ → σ) : (liftM (modify (m := m) f) : n _) = modify f
```

`liftM_modifyGet` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L38))

```lean
theorem liftM_modifyGet {m n} [MonadStateOf σ m] [MonadLift m n]
    (f : σ → α × σ) : (liftM (modifyGet (m := m) f) : n _) = modifyGet f
```

`liftM_getModify` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L41))

```lean
theorem liftM_getModify {m n} [MonadStateOf σ m] [MonadLift m n]
    (f : σ → σ) : (liftM (getModify (m := m) f) : n _) = getModify f
```

`LawfulMonadStateOf` (class, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L48))

> Class for well behaved state monads, extending the base `MonadState` type.
> Requires that `modifyGet` is equal to the same definition with only `get` and `set`,
> that `get` is idempotent if the result isn't used, and that `get` after `set` returns
> exactly the value that was previously `set`.

```lean
class LawfulMonadStateOf (σ : semiOutParam (Type _)) (m : Type _ → Type _)
    [Monad m] [MonadStateOf σ m] extends LawfulMonad m where
  /-- `modifyGet f` is equal to getting the state, modifying it, and returning a result. -/
  modifyGet_eq {α} (f : σ → α × σ) :
    modifyGet (m := m) f = do let z ← f <$> get; set z.2; return z.1
  /-- Discarding the result of `get` is the same as never getting the state. -/
  get_bind_const {α} (mx : m α) : (do let _ ← get; mx) = mx
  /-- Calling `get` twice is the same as just using the first retreived state value. -/
  get_bind_get_bind {α} (mx : σ → σ → m α) :
    (do let s ← get; let s' ← get; mx s s') = (do let s ← get; mx s s)
  /-- Setting the monad state to its current value has no effect. -/
  get_bind_set_bind {α} (mx : σ → PUnit → m α) :
    (do let s ← get; let u ← set s; mx s u) = (do let s ← get; mx s PUnit.unit)
  /-- Setting and then returning the monad state is the same as returning the set value. -/
  set_bind_get (s : σ) : (do set (m := m) s; get) = (do set s; return s)
  /-- Setting the monad twice is the same as just setting to the final state. -/
  set_bind_set (s s' : σ) : (do set (m := m) s; set s') = set s'
```

`LawfulMonadStateOf.get_seqRight` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L73))

```lean
theorem get_seqRight (mx : m α) : get *> mx = mx
```

`LawfulMonadStateOf.seqLeft_get` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L76))

```lean
theorem seqLeft_get (mx : m α) : mx <* get = mx
```

`LawfulMonadStateOf.get_map_const` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L79))

```lean
theorem get_map_const (x : α) :
    (fun _ => x) <$> get (m := m) = pure x
```

`LawfulMonadStateOf.get_bind_get` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L83))

```lean
theorem get_bind_get : (do let _ ← get (m := m); get) = get
```

`LawfulMonadStateOf.get_bind_set` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L85))

```lean
theorem get_bind_set :
    (do let s ← get (m := m); set s) = return PUnit.unit
```

`LawfulMonadStateOf.get_bind_map_set` (theorem, [line 90](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L90))

```lean
theorem get_bind_map_set (f : σ → PUnit → α) :
    (do let s ← get (m := m); f s <$> set s) = (do return f (← get) PUnit.unit)
```

`LawfulMonadStateOf.set_bind_get_bind` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L94))

```lean
theorem set_bind_get_bind (s : σ) (f : σ → m α) :
    (do set s; let s' ← get; f s') = (do set s; f s)
```

`LawfulMonadStateOf.set_bind_map_get` (theorem, [line 98](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L98))

```lean
theorem set_bind_map_get (f : σ → α) (s : σ) :
    (do set (m := m) s; f <$> get) = (do set (m := m) s; pure (f s))
```

`LawfulMonadStateOf.set_bind_set_bind` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L102))

```lean
theorem set_bind_set_bind (s s' : σ) (mx : m α) :
    (do set s; set s'; mx) = (do set s'; mx)
```

`LawfulMonadStateOf.set_bind_map_set` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L106))

```lean
theorem set_bind_map_set (s s' : σ) (f : PUnit → α) :
    (do set (m := m) s; f <$> set s') = (do f <$> set s')
```

`LawfulMonadStateOf.modifyGetThe_eq` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L112))

```lean
theorem modifyGetThe_eq (f : σ → α × σ) :
    modifyGetThe σ (m := m) f = do let z ← f <$> get; set z.2; return z.1 := modifyGet_eq f
```

`LawfulMonadStateOf.modify_eq` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L115))

```lean
theorem modify_eq (f : σ → σ) :
    modify (m := m) f = (do set (f (← get)))
```

`LawfulMonadStateOf.modifyThe_eq` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L118))

```lean
theorem modifyThe_eq (f : σ → σ) :
    modifyThe σ (m := m) f = (do set (f (← get)))
```

`LawfulMonadStateOf.getModify_eq` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L121))

```lean
theorem getModify_eq (f : σ → σ) :
    getModify (m := m) f = do let s ← get; set (f s); return s := by
  rw [getModify, modifyGet_eq, bind_map_left]
```

`LawfulMonadStateOf.modifyGet_eq'` (theorem, [line 126](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L126))

> Version of `modifyGet_eq` that preserves an call to `modify`.

```lean
theorem modifyGet_eq' (f : σ → α × σ) :
    modifyGet (m := m) f = do let s ← get; modify (Prod.snd ∘ f); return (f s).fst := by
  simp [modify_eq, modifyGet_eq]
```

`LawfulMonadStateOf.modify_id` (theorem, [line 130](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L130))

```lean
theorem modify_id : modify (m := m) id = pure PUnit.unit
```

`LawfulMonadStateOf.getModify_id` (theorem, [line 133](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L133))

```lean
theorem getModify_id : getModify (m := m) id = get
```

`LawfulMonadStateOf.set_bind_modify` (theorem, [line 136](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L136))

```lean
theorem set_bind_modify (s : σ) (f : σ → σ) :
    (do set (m := m) s; modify f) = set (f s)
```

`LawfulMonadStateOf.set_bind_modify_bind` (theorem, [line 139](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L139))

```lean
theorem set_bind_modify_bind (s : σ) (f : σ → σ) (mx : PUnit → m α) :
    (do set s; let u ← modify f; mx u) = (do set (f s); mx PUnit.unit)
```

`LawfulMonadStateOf.set_bind_modifyGet` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L143))

```lean
theorem set_bind_modifyGet (s : σ) (f : σ → α × σ) :
    (do set (m := m) s; modifyGet f) = (do set (f s).2; return (f s).1)
```

`LawfulMonadStateOf.set_bind_modifyGet_bind` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L146))

```lean
theorem set_bind_modifyGet_bind (s : σ) (f : σ → α × σ) (mx : α → m β) :
    (do set s; let x ← modifyGet f; mx x) = (do set (f s).2; mx (f s).1)
```

`LawfulMonadStateOf.set_bind_getModify` (theorem, [line 149](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L149))

```lean
theorem set_bind_getModify (s : σ) (f : σ → σ) :
    (do set (m := m) s; getModify f) = (do set (f s); return s)
```

`LawfulMonadStateOf.set_bind_getModify_bind` (theorem, [line 152](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L152))

```lean
theorem set_bind_getModify_bind (s : σ) (f : σ → σ) (mx : σ → m α) :
    (do set s; let x ← getModify f; mx x) = (do set (f s); mx s)
```

`LawfulMonadStateOf.modify_bind_modify` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L156))

```lean
theorem modify_bind_modify (f g : σ → σ) :
    (do modify (m := m) f; modify g) = modify (g ∘ f)
```

`LawfulMonadStateOf.modify_bind_modifyGet` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L159))

```lean
theorem modify_bind_modifyGet (f : σ → σ) (g : σ → α × σ) :
    (do modify (m := m) f; modifyGet g) = modifyGet (g ∘ f)
```

`LawfulMonadStateOf.getModify_bind_modify` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L163))

```lean
theorem getModify_bind_modify (f : σ → σ) (g : σ → σ → σ) :
    (do let s ← getModify (m := m) f; modify (g s)) =
      (do let s ← get; modify (g s ∘ f))
```

`LawfulMonadStateOf.modify_comm_of_comp_comm` (theorem, [line 168](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L168))

```lean
theorem modify_comm_of_comp_comm {f g : σ → σ} (h : f ∘ g = g ∘ f) :
    (do modify (m := m) f; modify g) = (do modify (m := m) g; modify f)
```

`LawfulMonadStateOf.modify_bind_get` (theorem, [line 172](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean#L172))

```lean
theorem modify_bind_get (f : σ → σ) :
    (do modify (m := m) f; get) = (do let s ← get; modify f; return (f s))
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Control/LawfulMonadState.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/LawfulMonadState.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Control.LawfulMonadState.json)
