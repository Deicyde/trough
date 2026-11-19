---
catalog: module
lean: Except.bind_ok_T, Except.bind_ok, Except.bind_err, bind_ne_error, Option.bind_some_T, Option.bind_some_fun, Option.bind_none_fun, do_some, do_error, do_ok_eq_ok, do_eq_ok, do_eq_ok₂, to_option_some, to_option_none, to_option_left_ok, to_option_right_ok, to_option_right_ok', to_option_left_ok', to_option_left_err, to_option_right_err, do_error_to_option, do_to_option_none, do_to_option_some, to_option_eq_do₁, to_option_eq_do₂, to_option_distr_map, to_option_distr_fmap
statement: formalized
proof: formalized
---

# Data/Control

`Cedar.Thm.Data.Control`, in [Cedar/Thm/Data/Control.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean).

> This file contains `simp` lemmas for proofs about code that uses the `do`
> notation together with `Except` and `Option`.

`Except.bind_ok_T` (theorem, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L25))

```lean
public theorem Except.bind_ok_T (a : α) (f : α → ExceptT ε Id β) :
  (bind (Except.ok a) f : ExceptT ε Id β) = f a
```

`Except.bind_ok` (theorem, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L29))

```lean
public theorem Except.bind_ok (a : α) (f : α → Except ε β) :
  (bind (Except.ok a) f : Except ε β) = f a
```

`Except.bind_err` (theorem, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L33))

```lean
public theorem Except.bind_err (e : ε) (f : α → Except ε β) :
  (bind (Except.error e) f : Except ε β) = (Except.error e)
```

`bind_ne_error` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L41))

> Monadic bind preserves "not this error": if neither the first computation nor
> the continuation (on success) yields error `e`, the bind does not either.

```lean
public theorem bind_ne_error {α β ε} {r : Except ε α} {f : α → Except ε β} {e : ε}
  (hr : r ≠ .error e)
  (hf : ∀ a, r = .ok a → f a ≠ .error e) :
  (r >>= f) ≠ .error e
```

`Option.bind_some_T` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L57))

```lean
public theorem Option.bind_some_T (a : α) (f : α → OptionT Id β) :
  (bind (Option.some a) f : OptionT Id β) = f a
```

`Option.bind_some_fun` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L61))

```lean
public theorem Option.bind_some_fun (a : α) (f : α → Option β) :
  (bind (Option.some a) f : Option β) = f a
```

`Option.bind_none_fun` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L65))

```lean
public theorem Option.bind_none_fun (f : α → Option β) :
  (bind Option.none f : Option β) = Option.none
```

`do_some` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L69))

```lean
public theorem do_some {opt : Option α} {f : α → β} :
  (do let v ← opt ; some (f v)) = some b ↔
  ∃ a, opt = some a ∧ f a = b
```

`do_error` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L74))

```lean
public theorem do_error {res : Except ε α} {e : ε} {f : α → β} :
  (do let v ← res ; .ok (f v)) = .error e ↔
  res = .error e
```

`do_ok_eq_ok` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L79))

```lean
public theorem do_ok_eq_ok {res : Except ε α} {f : α → β} :
  (do let v ← res ; .ok (f v)) = .ok b ↔
  ∃ a, res = .ok a ∧ f a = b
```

`do_eq_ok` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L84))

```lean
public theorem do_eq_ok {res : Except ε α} {f : α → Except ε β} :
  (do let v ← res ; f v) = .ok b ↔
  ∃ a, res = .ok a ∧ f a = .ok b
```

`do_eq_ok₂` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L89))

```lean
public theorem do_eq_ok₂ {res₁ res₂: Except ε PUnit} :
  (do res₁ ; res₂) = .ok () → res₁ = .ok () ∧ res₂ = .ok ()
```

`to_option_some` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L94))

```lean
public theorem to_option_some {v : α} {res: Except ε α} :
  res.toOption = .some v ↔ res = .ok v
```

`to_option_none` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L108))

```lean
public theorem to_option_none {res: Except ε α} :
  res.toOption = .none ↔ (∃ err, res = .error err)
```

`to_option_left_ok` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L114))

```lean
public theorem to_option_left_ok {α ε₁ ε₂} {v : α} {res₁ : Except ε₁ α} {res₂ : Except ε₂ α} :
  res₁.toOption = res₂.toOption → res₁ = .ok v → res₂ = .ok v
```

`to_option_right_ok` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L127))

```lean
public theorem to_option_right_ok {α ε₁ ε₂} {v : α} {res₁ : Except ε₁ α} {res₂ : Except ε₂ α} :
  res₁.toOption = res₂.toOption → res₂ = .ok v → res₁ = .ok v
```

`to_option_right_ok'` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L134))

```lean
public theorem to_option_right_ok' {α ε₁ ε₂} {v : α} {res₁ : Except ε₁ α} :
  res₁.toOption = ((.ok v) : Except ε₂ α).toOption → res₁ = Except.ok v
```

`to_option_left_ok'` (theorem, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L142))

```lean
public theorem to_option_left_ok' {α ε₁ ε₂} {v : α} {res₂ : Except ε₂ α} :
  ((.ok v) : Except ε₁ α).toOption = res₂.toOption → res₂ = Except.ok v
```

`to_option_left_err` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L149))

```lean
public theorem to_option_left_err {ε₁ ε₂ α} {err₁: ε₁} {res₂ : Except ε₂ α} :
  (Except.error err₁).toOption = res₂.toOption → ∃ err₂, res₂ = .error err₂
```

`to_option_right_err` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L158))

```lean
public theorem to_option_right_err {ε₂ ε₁ α} {err₂: ε₂} {res₁ : Except ε₁ α} :
  res₁.toOption = (Except.error err₂).toOption → ∃ err₁, res₁ = .error err₁
```

`do_error_to_option` (theorem, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L165))

```lean
public theorem do_error_to_option {res : Except ε α} {e : ε} :
  (do let (_ : α) ← res ; (.error e : Except ε α)).toOption = .none
```

`do_to_option_none` (theorem, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L170))

```lean
public theorem do_to_option_none {ε α β} {res : Except ε α} {f : α → Except ε β} :
  res.toOption = none → (do let x ← res; f x).toOption = none
```

`do_to_option_some` (theorem, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L177))

```lean
public theorem do_to_option_some {ε α β} {res : Except ε α} {v : α} {f : α → Except ε β} :
  res.toOption = .some v → (do let x ← res; f x) = f v
```

`to_option_eq_do₁` (theorem, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L183))

```lean
public theorem to_option_eq_do₁ {α β ε} {res₁ res₂: Except ε α} (f : α → Except ε β) :
  res₁.toOption = res₂.toOption →
  (do let x ← res₁; f x).toOption = (do let x ← res₂; f x).toOption
```

`to_option_eq_do₂` (theorem, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L193))

```lean
public theorem to_option_eq_do₂ {α ε} {res₁ res₂ res₃ res₄: Except ε α} (f : α → α → Except ε α) :
  res₁.toOption = res₃.toOption →
  res₂.toOption = res₄.toOption →
  (do let x ← res₁; let y ← res₂; f x y).toOption = (do let x ← res₃; let y ← res₄; f x y).toOption
```

`to_option_distr_map` (theorem, [line 209](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L209))

```lean
public theorem to_option_distr_map {ε α β} {x : Except ε α} {f : α → β} :
  (x.map f).toOption = x.toOption.map f
```

`to_option_distr_fmap` (theorem, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean#L216))

```lean
public theorem to_option_distr_fmap {ε α β} {x : Except ε α} {f : α → β} :
  (f <$> x).toOption = f <$> x.toOption
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Thm/Data/Control.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Control.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Control.json)
