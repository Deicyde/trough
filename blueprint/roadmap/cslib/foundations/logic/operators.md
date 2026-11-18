---
catalog: module
lean: Cslib.Logic.HasAnd, Cslib.Logic.HasOr, Cslib.Logic.finiteAnd, Cslib.Logic.finiteAnd_nil, Cslib.Logic.finiteAnd_cons, Cslib.Logic.finiteOr, Cslib.Logic.finiteOr_nil, Cslib.Logic.finiteOr_cons, Cslib.Logic.HasImp, Cslib.Logic.HasIff, Cslib.Logic.HasNot, Cslib.Logic.HasTriangle, Cslib.Logic.HasNabla, Cslib.Logic.HasDynamicDiamond, Cslib.Logic.HasDynamicBox, Cslib.Logic.dynDiamond_eq_triangle, Cslib.Logic.dynBox_eq_nabla, Cslib.Logic.HasBox, Cslib.Logic.HasDiamond, Cslib.Logic.diamond_eq_dynDiamond, Cslib.Logic.box_eq_dynBox, Cslib.Logic.HasTensor
statement: formalized
proof: formalized
---

# Logical operators

`Cslib.Foundations.Logic.Operators`, in [Cslib/Foundations/Logic/Operators.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean), by Fabrizio Montesi, Thomas Waring.

> This module contains typeclasses and associated notation for common logical operators: propositional
> connectives (like `∧` and `→`), modalities (like `◇`, plain and indexed), linear connectives (like
> `⊗`), etc.

> ## Propositional connectives

`Cslib.Logic.HasAnd` (class, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L28))

> The type `α` has an and connective (`∧`).

```lean
class HasAnd (α : Type*) where
  /-- `a ∧ b` is the conjunction of `a` and `b`. -/
  and (a b : α) : α
```

`Cslib.Logic.HasOr` (class, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L35))

> The type `α` has an or connective (`∨`).

```lean
class HasOr (α : Type*) where
  /-- `a ∨ b` is the disjunction of `a` and `b`. -/
  or (a b : α) : α
```

`Cslib.Logic.finiteAnd` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L42))

> Finite conjunction, with empty conjunction equal to truth.

```lean
def finiteAnd [HasAnd α] [Top α] (as : List α) : α
```

`Cslib.Logic.finiteAnd_nil` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L47))

```lean
theorem finiteAnd_nil [HasAnd α] [Top α] : ⋀([] : List α) = ⊤
```

`Cslib.Logic.finiteAnd_cons` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L50))

```lean
theorem finiteAnd_cons [HasAnd α] [Top α] (a : α) (as : List α) :
    ⋀(a :: as) = (a ∧ ⋀as)
```

`Cslib.Logic.finiteOr` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L54))

> Finite disjunction, with empty disjunction equal to falsehood.

```lean
def finiteOr [HasOr α] [Bot α] (as : List α) : α
```

`Cslib.Logic.finiteOr_nil` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L59))

```lean
theorem finiteOr_nil [HasOr α] [Bot α] : ⋁([] : List α) = ⊥
```

`Cslib.Logic.finiteOr_cons` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L62))

```lean
theorem finiteOr_cons [HasOr α] [Bot α] (a : α) (as : List α) :
    ⋁(a :: as) = (a ∨ ⋁as)
```

`Cslib.Logic.HasImp` (class, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L66))

> The type `α` has an implication connective (`→`).

```lean
class HasImp (α : Type*) where
  /-- `a → b` denotes `a` implies `b`. -/
  imp (a b : α) : α
```

`Cslib.Logic.HasIff` (class, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L73))

> The type `α` has a bi-implication connective (`↔`).

```lean
class HasIff (α : Type*) where
  /-- `a ↔ b` denotes `a` implies `b` and vice-versa. -/
  iff (a b : α) : α
```

`Cslib.Logic.HasNot` (class, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L80))

> The type `α` has a negation connective (`¬`).

```lean
class HasNot (α : Type*) where
  /-- `¬a` is the negation of `a`. -/
  not (a : α) : α
```

> ## General modalities from modal similarity types (polynomial functors)

`Cslib.Logic.HasTriangle` (class, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L93))

> The type `α` has a family of triangle operators (`Δ`).

```lean
class HasTriangle (α : Type*) (τ : outParam PFunctor) where
  /-- `Δ[op](φ₁, ..., φₙ)` means that `φ₁`, ..., `φₙ` are valid at some respective related states.
  -/
  triangle (op : τ.A) (arg : τ.B op → α) : α
```

`Cslib.Logic.HasNabla` (class, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L101))

> The type `α` has a family of nabla operators (`∇`).

```lean
class HasNabla (α : Type*) (τ : outParam PFunctor) where
  /-- `∇[op](φ₁, ..., φₙ)` means that `φ₁`, ..., `φₙ` are valid at all respective related states. -/
  nabla (op : τ.A) (arg : τ.B op → α) : α
```

> ## Dynamic modalities
>
> Here we need to use the prefix `d` to distinguish our notation from the normal `[·]` and `⟨·⟩`.
> …

`Cslib.Logic.HasDynamicDiamond` (class, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L118))

> The type `α` has a dynamic diamond modality with action type `β` (`d⟨a⟩φ`).

```lean
class HasDynamicDiamond (α : Type*) (β : outParam Type*) where
  /-- `b` is possibly valid after `a`. -/
  dynDiamond (a : β) (b : α) : α
```

`Cslib.Logic.HasDynamicBox` (class, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L125))

> The type `α` has a dynamic box modality with action type `β` (`d[a]φ`).

```lean
class HasDynamicBox (α : Type*) (β : outParam Type*) where
  /-- `b` is necessarily valid after `a`. -/
  dynBox (a : β) (b : α) : α
```

`Cslib.Logic.dynDiamond_eq_triangle` (theorem, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L137))

```lean
theorem dynDiamond_eq_triangle [HasTriangle α τ] (op : τ.A) (φ : α) :
    (d⟨op⟩φ) = (Δ[op](PFunctor.const op φ))
```

`Cslib.Logic.dynBox_eq_nabla` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L146))

```lean
theorem dynBox_eq_nabla [HasNabla α τ] (op : τ.A) (φ : α) :
    (d[op]φ) = (∇[op](PFunctor.const op φ))
```

> ## Basic modalities (Unimodal logic operators)

`Cslib.Logic.HasBox` (class, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L156))

> The type `α` has a box modality (`□`).

```lean
class HasBox (α : Type*) where
  /-- `a` is valid in all immediately reachable states. -/
  box (a : α) : α
```

`Cslib.Logic.HasDiamond` (class, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L163))

> The type `α` has a diamond modality (`◇`).

```lean
class HasDiamond (α : Type*) where
  /-- `a` is valid in a reachable state. -/
  diamond (a : α) : α
```

`Cslib.Logic.diamond_eq_dynDiamond` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L174))

```lean
theorem diamond_eq_dynDiamond [Unique β] [HasDynamicDiamond α β] {φ : α} :
    (◇φ) = (d⟨default⟩φ)
```

`Cslib.Logic.box_eq_dynBox` (theorem, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L182))

```lean
theorem box_eq_dynBox [Unique β] [HasDynamicBox α β] {φ : α} :
    (□φ) = (d[default]φ)
```

> ## Linear connectives

`Cslib.Logic.HasTensor` (class, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean#L192))

> The type `α` has a tensor connective (⊗).

```lean
class HasTensor (α : Type*) where
  /-- `a ⊗ b` is the multiplicative conjunction of `a` and `b`. -/
  tensor (a b : α) : α
```

## Depends on

- [Polynomial Functors](../data/pfunctor/basic.md)

## Sources

- [Cslib/Foundations/Logic/Operators.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/Operators.lean)
