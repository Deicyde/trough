---
catalog: module
lean: Cslib.FreeM.foldFreeM, Cslib.FreeM.foldFreeM_pure, Cslib.FreeM.foldFreeM_lift_bind, Cslib.FreeM.foldFreeM_lift_bind', Cslib.FreeM.foldFreeM_lift, Cslib.FreeM.foldFreeM_unique, Cslib.FreeM.foldFreeM_bind, Cslib.FreeM.foldFreeM_map, Cslib.FreeM.liftM_eq_foldFreeM
statement: formalized
proof: formalized
---

# Free Monad Catamorphism

`Cslib.Foundations.Control.Monad.Free.Fold`, in [Cslib/Foundations/Control/Monad/Free/Fold.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean), by Tanner Duve.

> This file defines the fold operation for free monads and proves its universal property.
>
> In computer science terms, `foldFreeM` provides **interpreters** for effectful syntax trees.
> Given any "target algebra" (a type with handlers for values and effects), `foldFreeM`
> constructs the unique interpreter that transforms `FreeM` programs into that target.
>
> The theory is based on the fact that `FreeM F α` is the initial algebra for a specific functor, and
> `foldFreeM` provides the unique way to eliminate free monad computations into any
> algebra of this functor.
>
> ## Main Definitions
>
> - `FreeM.foldFreeM`: Fold operation for free monads
> - `FreeM.foldFreeM_unique`: Universal property showing uniqueness of the fold
>
> ## Universal Property
>
> `FreeM F α` is the initial algebra of the functor `φ_F(β) = α ⊕ Σ_ι (F ι × (ι → β))`.
>
> An algebra of this functor consists of a type `β` and functions:
> - `onValue : α → β` (handles pure values)
> - `onEffect : {ι : Type u} → F ι → (ι → β) → β` (handles effects with continuations)
>
> For any such algebra, `foldFreeM onValue onEffect` is the unique algebra morphism
> from the initial algebra `FreeM F α` to `(β, onValue, onEffect)`.

`Cslib.FreeM.foldFreeM` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L51))

> Fold function for the `FreeM` monad

```lean
def foldFreeM
    (onValue : α → β)
    (onEffect : {ι : Type u} → F ι → (ι → β) → β) :
    FreeM F α → β
```

`Cslib.FreeM.foldFreeM_pure` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L59))

```lean
theorem foldFreeM_pure
    (onValue : α → β)
    (onEffect : {ι : Type u} → F ι → (ι → β) → β)
    (a : α) : foldFreeM onValue onEffect (pure a) = onValue a
```

`Cslib.FreeM.foldFreeM_lift_bind` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L65))

```lean
theorem foldFreeM_lift_bind
    (onValue : α → β)
    (onEffect : {ι : Type u} → F ι → (ι → β) → β)
    (op : F ι) (k : ι → FreeM F α) :
      foldFreeM onValue onEffect ((lift op).bind k)
      = onEffect op (fun x => foldFreeM onValue onEffect (k x))
```

`Cslib.FreeM.foldFreeM_lift_bind'` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L73))

```lean
theorem foldFreeM_lift_bind' {F : Type w → Type v} {ι : Type w}
    (onValue : α → β)
    (onEffect : {ι : Type w} → F ι → (ι → β) → β)
    (op : F ι) (k : ι → FreeM F α) :
      foldFreeM onValue onEffect (lift op >>= k)
      = onEffect op (fun x => foldFreeM onValue onEffect (k x))
```

`Cslib.FreeM.foldFreeM_lift` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L81))

```lean
theorem foldFreeM_lift
    (onValue : ι → β)
    (onEffect : {ι : Type u} → F ι → (ι → β) → β)
    (op : F ι) :
    foldFreeM onValue onEffect (lift op) = onEffect op onValue
```

`Cslib.FreeM.foldFreeM_unique` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L95))

> **Universal Property**: If `h : FreeM F α → β` satisfies:
> * `h (pure a) = onValue a`
> * `h ((lift op).bind k) = onEffect op (fun x => h (k x))`
>
> then `h` is equal to `foldFreeM onValue onEffect`.

```lean
theorem foldFreeM_unique
    (onValue : α → β)
    (onEffect : {ι : Type u} → F ι → (ι → β) → β)
    (h : FreeM F α → β)
    (h_pure : ∀ a, h (pure a) = onValue a)
    (h_liftBind : ∀ {ι} (op : F ι) (k : ι → FreeM F α),
      h ((lift op).bind k) = onEffect op (fun x => h (k x))) :
    h = foldFreeM onValue onEffect
```

`Cslib.FreeM.foldFreeM_bind` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L112))

> Sequencing substitutes the fold of the continuation for the value handler.

```lean
theorem foldFreeM_bind (onValue : β → γ)
    (onEffect : {ι : Type u} → F ι → (ι → γ) → γ)
    (x : FreeM F α) (k : α → FreeM F β) :
    foldFreeM onValue onEffect (x.bind k) =
      foldFreeM (fun a => foldFreeM onValue onEffect (k a)) onEffect x
```

`Cslib.FreeM.foldFreeM_map` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L121))

```lean
theorem foldFreeM_map (onValue : β → γ)
    (onEffect : {ι : Type u} → F ι → (ι → γ) → γ) (f : α → β) (x : FreeM F α) :
    foldFreeM onValue onEffect (map f x) = foldFreeM (onValue ∘ f) onEffect x
```

`Cslib.FreeM.liftM_eq_foldFreeM` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean#L128))

> Monadic interpretation is the fold whose effect handler uses `bind`.

```lean
theorem liftM_eq_foldFreeM {m : Type u → Type w} [Monad m] {α : Type u}
    (interp : {ι : Type u} → F ι → m ι) :
    FreeM.liftM interp (α := α) = foldFreeM pure (fun op k => interp op >>= k)
```

## Depends on

- [Free Monad (Free)](../free.md)

## Sources

- [Cslib/Foundations/Control/Monad/Free/Fold.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Fold.lean)
