---
catalog: module
lean: Except.emoji, Except.map_error, Except.map_ok, Except.map_eq_ok, Except.map_eq_error, Except.pmap, Except.pmap_error, Except.pmap_ok, Except.pmap_id, Except.map_pmap, ExceptT.mk_run, ExceptT.map_mk
statement: formalized
proof: formalized
---

# Except

`Batteries.Data.Except`, in [Batteries/Data/Except.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean), by Kim Morrison.

`Except.emoji` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L15))

> Visualize an `Except` using a checkmark or a cross.

```lean
def emoji : Except ε α → String
```

`Except.map_error` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L19))

```lean
theorem map_error {ε : Type u} (f : α → β) (e : ε) :
    f <$> (.error e : Except ε α) = .error e
```

`Except.map_ok` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L22))

```lean
theorem map_ok {ε : Type u} (f : α → β) (x : α) :
    f <$> (.ok x : Except ε α) = .ok (f x)
```

`Except.map_eq_ok` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L25))

```lean
theorem map_eq_ok {ε : Type u} {f : α → β} {x : Except ε α} {b : β} :
    f <$> x = .ok b ↔ ∃ a, x = .ok a ∧ b = f a
```

`Except.map_eq_error` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L29))

```lean
theorem map_eq_error {ε : Type u} (f : α → β) {x : Except ε α} {e : ε} :
    f <$> x = .error e ↔ x = .error e
```

`Except.pmap` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L35))

> Map a function over an `Except` value, using a proof that the value is `.ok`.

```lean
def pmap {ε : Type u} {α β : Type v} (x : Except ε α) (f : (a : α) → x = .ok a → β) : Except ε β
```

`Except.pmap_error` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L40))

```lean
theorem pmap_error {ε : Type u} {α β : Type v} (e : ε)
    (f : (a : α) → Except.error e = Except.ok a → β) :
    Except.pmap (.error e) f = .error e
```

`Except.pmap_ok` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L44))

```lean
theorem pmap_ok {ε : Type u} {α β : Type v} (a : α)
    (f : (a' : α) → (.ok a : Except ε α) = .ok a' → β) :
    Except.pmap (.ok a) f = .ok (f a rfl)
```

`Except.pmap_id` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L48))

```lean
theorem pmap_id {ε : Type u} {α : Type v} (x : Except ε α) :
    x.pmap (fun a _ => a) = x
```

`Except.map_pmap` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L51))

```lean
theorem map_pmap (g : β → γ) (x : Except ε α) (f : (a : α) → x = .ok a → β) :
    g <$> x.pmap f = x.pmap fun a h => g (f a h)
```

`ExceptT.mk_run` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L61))

```lean
theorem mk_run (x : ExceptT ε m α) : ExceptT.mk (ExceptT.run x) = x
```

`ExceptT.map_mk` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean#L64))

```lean
theorem map_mk [Monad m] [LawfulMonad m] (f : α → β) (x : m (Except ε α)) :
    f <$> ExceptT.mk x = ExceptT.mk ((f <$> · ) <$> x)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Except.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Except.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.Except.json)
