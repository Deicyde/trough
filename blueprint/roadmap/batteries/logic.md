---
catalog: module
lean: Function.id_def, heq_iff_eq, eq_rec_constant, congrArg₂, congrFun₂, congrFun₃, funext₂, funext₃, Eq.congr, Eq.congr_left, Eq.congr_right, congr_arg, congr_arg₂, congr_fun, congr_fun₂, congr_fun₃, heq_of_cast_eq, cast_eq_iff_heq, eqRec_eq_cast, eqRec_heq_self, eqRec_heq_iff_heq, heq_eqRec_iff_heq, not_nonempty_empty, not_nonempty_pempty, subsingleton_of_forall_eq, subsingleton_iff_forall_eq, congr_eqRec
statement: formalized
proof: formalized
---

# Logic

`Batteries.Logic`, in [Batteries/Logic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean), by Leonardo de Moura, Jeremy Avigad, Floris van Doorn, Mario Carneiro.

> ## id

`Function.id_def` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L17))

```lean
theorem Function.id_def : @id α = fun x => x
```

> ## decidable

> ## classical logic

> ## equality

`heq_iff_eq` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L33))

```lean
theorem heq_iff_eq {a b : α} : a ≍ b ↔ a = b
```

`eq_rec_constant` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L35))

```lean
theorem eq_rec_constant {α : Sort _} {a a' : α} {β : Sort _} (y : β) (h : a = a') :
    (@Eq.rec α a (fun _ _ => β) y a' h) = y
```

`congrArg₂` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L38))

```lean
theorem congrArg₂ (f : α → β → γ) {x x' : α} {y y' : β}
    (hx : x = x') (hy : y = y') : f x y = f x' y'
```

`congrFun₂` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L41))

```lean
theorem congrFun₂ {β : α → Sort _} {γ : ∀ a, β a → Sort _}
    {f g : ∀ a b, γ a b} (h : f = g) (a : α) (b : β a) :
    f a b = g a b
```

`congrFun₃` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L46))

```lean
theorem congrFun₃ {β : α → Sort _} {γ : ∀ a, β a → Sort _} {δ : ∀ a b, γ a b → Sort _}
      {f g : ∀ a b c, δ a b c} (h : f = g) (a : α) (b : β a) (c : γ a b) :
    f a b c = g a b c
```

`funext₂` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L51))

```lean
theorem funext₂ {β : α → Sort _} {γ : ∀ a, β a → Sort _}
    {f g : ∀ a b, γ a b} (h : ∀ a b, f a b = g a b) : f = g
```

`funext₃` (theorem, [line 55](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L55))

```lean
theorem funext₃ {β : α → Sort _} {γ : ∀ a, β a → Sort _} {δ : ∀ a b, γ a b → Sort _}
    {f g : ∀ a b c, δ a b c} (h : ∀ a b c, f a b c = g a b c) : f = g
```

`Eq.congr` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L59))

```lean
protected theorem Eq.congr (h₁ : x₁ = y₁) (h₂ : x₂ = y₂) : x₁ = x₂ ↔ y₁ = y₂
```

`Eq.congr_left` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L62))

```lean
theorem Eq.congr_left {x y z : α} (h : x = y) : x = z ↔ y = z
```

`Eq.congr_right` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L64))

```lean
theorem Eq.congr_right {x y z : α} (h : x = y) : z = x ↔ z = y
```

`congr_arg` (alias, [line 66](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L66))

```lean
alias congr_arg
```

`congr_arg₂` (alias, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L67))

```lean
alias congr_arg₂
```

`congr_fun` (alias, [line 68](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L68))

```lean
alias congr_fun
```

`congr_fun₂` (alias, [line 69](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L69))

```lean
alias congr_fun₂
```

`congr_fun₃` (alias, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L70))

```lean
alias congr_fun₃
```

`heq_of_cast_eq` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L72))

```lean
theorem heq_of_cast_eq : ∀ (e : α = β) (_ : cast e a = a'), a ≍ a'
```

`cast_eq_iff_heq` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L75))

```lean
theorem cast_eq_iff_heq : cast e a = a' ↔ a ≍ a'
```

`eqRec_eq_cast` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L78))

```lean
theorem eqRec_eq_cast {α : Sort _} {a : α} {motive : (a' : α) → a = a' → Sort _}
    (x : motive a rfl) {a' : α} (e : a = a') :
    @Eq.rec α a motive x a' e = cast (e ▸ rfl) x
```

`eqRec_heq_self` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L84))

```lean
theorem eqRec_heq_self {α : Sort _} {a : α} {motive : (a' : α) → a = a' → Sort _}
    (x : motive a rfl) {a' : α} (e : a = a') : @Eq.rec α a motive x a' e ≍ x
```

`eqRec_heq_iff_heq` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L89))

```lean
theorem eqRec_heq_iff_heq {α : Sort _} {a : α} {motive : (a' : α) → a = a' → Sort _}
    {x : motive a rfl} {a' : α} {e : a = a'} {β : Sort _} {y : β} :
    @Eq.rec α a motive x a' e ≍ y ↔ x ≍ y
```

`heq_eqRec_iff_heq` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L96))

```lean
theorem heq_eqRec_iff_heq {α : Sort _} {a : α} {motive : (a' : α) → a = a' → Sort _}
    {x : motive a rfl} {a' : α} {e : a = a'} {β : Sort _} {y : β} :
    y ≍ @Eq.rec α a motive x a' e ↔ y ≍ x
```

> ## miscellaneous

`not_nonempty_empty` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L103))

```lean
theorem not_nonempty_empty  : ¬Nonempty Empty
```

`not_nonempty_pempty` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L104))

```lean
theorem not_nonempty_pempty : ¬Nonempty PEmpty
```

`subsingleton_of_forall_eq` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L113))

> If all points are equal to a given point `x`, then `α` is a subsingleton.

```lean
theorem subsingleton_of_forall_eq (x : α) (h : ∀ y, y = x) : Subsingleton α
```

`subsingleton_iff_forall_eq` (theorem, [line 116](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L116))

```lean
theorem subsingleton_iff_forall_eq (x : α) : Subsingleton α ↔ ∀ y, y = x
```

`congr_eqRec` (theorem, [line 119](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean#L119))

```lean
theorem congr_eqRec {β : α → Sort _} (f : (x : α) → β x → γ) (h : x = x') (y : β x) :
  f x' (Eq.rec y h) = f x y
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Logic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Logic.lean)
- [Declaration ledger](../../sources/batteries/Batteries.Logic.json)
