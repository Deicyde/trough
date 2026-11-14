---
catalog: module
lean: PFunctor.FreeM.foldFreeM, PFunctor.FreeM.foldFreeM_pure, PFunctor.FreeM.foldFreeM_lift_bind, PFunctor.FreeM.foldFreeM_lift_bind', PFunctor.FreeM.foldFreeM_lift, PFunctor.FreeM.foldFreeM_unique, PFunctor.FreeM.foldFreeM_bind, PFunctor.FreeM.foldFreeM_map, PFunctor.FreeM.liftM_eq_foldFreeM
statement: formalized
proof: formalized
---

# Folding polynomial free monads

`Cslib.Foundations.Data.PFunctor.Free.Fold`, in [Cslib/Foundations/Data/PFunctor/Free/Fold.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean), by Devon Tuma, Quang Dao.

> `PFunctor.FreeM.foldFreeM` evaluates a free polynomial tree in an algebra given by handlers
> for values and operations. It satisfies the same universal property and substitution laws
> as `Cslib.FreeM.foldFreeM`.

`PFunctor.FreeM.foldFreeM` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L28))

> Fold a free polynomial tree into an algebra of its signature.

```lean
def foldFreeM (onValue : α → β) (onEffect : (a : P.A) → (P.B a → β) → β) : P.FreeM α → β
```

`PFunctor.FreeM.foldFreeM_pure` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L33))

```lean
theorem foldFreeM_pure (onValue : α → β) (onEffect : (a : P.A) → (P.B a → β) → β) (a : α) :
    foldFreeM onValue onEffect (pure a) = onValue a
```

`PFunctor.FreeM.foldFreeM_lift_bind` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L37))

```lean
theorem foldFreeM_lift_bind (onValue : α → β) (onEffect : (a : P.A) → (P.B a → β) → β)
    (a : P.A) (cont : P.B a → P.FreeM α) :
    foldFreeM onValue onEffect ((lift a).bind (α := no_index (P.B a)) cont) =
      onEffect a (fun b => foldFreeM onValue onEffect (cont b))
```

`PFunctor.FreeM.foldFreeM_lift_bind'` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L44))

```lean
theorem foldFreeM_lift_bind' {α : Type uB} (onValue : α → β)
    (onEffect : (a : P.A) → (P.B a → β) → β) (a : P.A) (cont : P.B a → P.FreeM α) :
    foldFreeM onValue onEffect (Bind.bind (α := no_index (P.B a)) (lift a) cont) =
      onEffect a (fun b => foldFreeM onValue onEffect (cont b))
```

`PFunctor.FreeM.foldFreeM_lift` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L50))

```lean
theorem foldFreeM_lift (a : P.A) (onValue : P.B a → β)
    (onEffect : (a : P.A) → (P.B a → β) → β) :
    foldFreeM (α := no_index (P.B a)) onValue onEffect (lift a) = onEffect a onValue
```

`PFunctor.FreeM.foldFreeM_unique` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L55))

> A function agreeing with the algebra on values and operations is the fold.

```lean
theorem foldFreeM_unique (onValue : α → β) (onEffect : (a : P.A) → (P.B a → β) → β)
    (h : P.FreeM α → β) (h_pure : ∀ a, h (pure a) = onValue a)
    (h_lift_bind : ∀ (a : P.A) (cont : P.B a → P.FreeM α),
      h ((lift a).bind cont) = onEffect a (fun b => h (cont b))) :
    h = foldFreeM onValue onEffect
```

`PFunctor.FreeM.foldFreeM_bind` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L67))

> Sequencing substitutes the fold of the continuation for the value handler.

```lean
theorem foldFreeM_bind (onValue : β → γ) (onEffect : (a : P.A) → (P.B a → γ) → γ)
    (x : P.FreeM α) (k : α → P.FreeM β) :
    foldFreeM onValue onEffect (x.bind k) =
      foldFreeM (fun a => foldFreeM onValue onEffect (k a)) onEffect x
```

`PFunctor.FreeM.foldFreeM_map` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L75))

```lean
theorem foldFreeM_map (onValue : β → γ) (onEffect : (a : P.A) → (P.B a → γ) → γ)
    (f : α → β) (x : P.FreeM α) :
    foldFreeM onValue onEffect (map f x) = foldFreeM (onValue ∘ f) onEffect x
```

`PFunctor.FreeM.liftM_eq_foldFreeM` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean#L82))

> Monadic interpretation is the fold whose effect handler uses `bind`.

```lean
theorem liftM_eq_foldFreeM {m : Type uB → Type v} [Monad m] {α : Type uB}
    (interp : (a : P.A) → m (P.B a)) :
    FreeM.liftM interp (α := α) = foldFreeM pure (fun a k => interp a >>= k)
```

## Depends on

- [Free Monad of a Polynomial Functor](../free.md)

## Sources

- [Cslib/Foundations/Data/PFunctor/Free/Fold.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/Fold.lean)
