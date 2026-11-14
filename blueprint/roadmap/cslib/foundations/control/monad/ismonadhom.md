---
catalog: module
lean: Id.pure_injective, Cslib.IsFunctorHom, Cslib.IsFunctorHom.mk', Cslib.IsFunctorHom.id, Cslib.IsFunctorHom.comp, Cslib.IsApplicativeHom, Cslib.IsApplicativeHom.mk', Cslib.IsApplicativeHom.id, Cslib.IsApplicativeHom.comp, Cslib.IsMonadHom, Cslib.IsMonadHom.mk', Cslib.IsMonadHom.id, Cslib.IsMonadHom.comp, Cslib.IsMonadHom.monadLift, Cslib.IsMonadHom.monadLiftT, Cslib.IsAlternativeHom, Cslib.IsAlternativeHom.mk', Cslib.IsAlternativeHom.id, Cslib.IsAlternativeHom.comp, Cslib.IsAlternativeMonadHom, Cslib.IsAlternativeMonadHom.mk', Cslib.IsAlternativeMonadHom.id, Cslib.IsAlternativeMonadHom.comp, Cslib.IsMonadHom.wp
statement: formalized
proof: formalized
---

# (unbundled) morphisms of monads

`Cslib.Foundations.Control.Monad.IsMonadHom`, in [Cslib/Foundations/Control/Monad/IsMonadHom.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean), by Eric Wieser.

> This file defines predicates on functions `f : ∀ {α}, m α → n α` that preserve functor, applicative,
> monadic, and alternative structure (`IsFunctorHom`, `IsApplicativeHom`, `IsMonadHom`,
> `IsAlternativeHom`, `IsAlternativeMonadHom`).
>
> Rather than assuming lawfulness, they explicitly require compatibility with every operator
> defined by the corresponding typeclasses, with helper constructors that dismiss the derived
> operators when the structures are lawful.

`Id.pure_injective` (theorem, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L29))

```lean
theorem _root_.Id.pure_injective : Function.Injective (pure : α → Id α)
```

> ### Functor Homomorphisms

`Cslib.IsFunctorHom` (structure, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L39))

> A function `f` is a morphism of functors if it preserves `<$>` and `Functor.mapConst`.

```lean
structure IsFunctorHom (m n) [Functor m] [Functor n] (f : ∀ {α}, m α → n α) : Prop where
  map_map {α β} (g : α → β) (x : m α) : f (g <$> x) = g <$> f x
  map_mapConst {α β} (a : α) (x : m β) : f (Functor.mapConst a x) = Functor.mapConst a (f x)
```

`Cslib.IsFunctorHom.mk'` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L56))

> Construct an `IsFunctorHom` for lawful functors from `map_map`.

```lean
theorem mk' [LawfulFunctor m] [LawfulFunctor n] {f : ∀ {α}, m α → n α}
    (map_map : ∀ {α β} (g : α → β) (x : m α), f (g <$> x) = g <$> f x) :
    IsFunctorHom m n f
```

`Cslib.IsFunctorHom.id` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L63))

```lean
protected theorem id : IsFunctorHom m m id
```

`Cslib.IsFunctorHom.comp` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L67))

```lean
protected theorem comp {f : ∀ {α}, n α → p α} {g : ∀ {α}, m α → n α}
    (hf : IsFunctorHom n p f) (hg : IsFunctorHom m n g) :
    IsFunctorHom m p (f ∘ g)
```

> ### Applicative Homomorphisms

`Cslib.IsApplicativeHom` (structure, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L81))

> A function `f` is a morphism of applicatives if it preserves `pure`, `<$>`, `<*>`, `<*`, and `*>`.

```lean
structure IsApplicativeHom (m n) [Applicative m] [Applicative n] (f : ∀ {α}, m α → n α) : Prop
    extends IsFunctorHom m n f where
  map_pure {α} (a : α) : f (pure a) = pure a
  map_seq {α β} (x : m (α → β)) (y : Unit → m α) :
      f (Seq.seq x y) = Seq.seq (f x) (f <| y ·)
  map_seqLeft {α β} (x : m α) (y : Unit → m β) :
      f (SeqLeft.seqLeft x y) = SeqLeft.seqLeft (f x) (f <| y ·)
  map_seqRight {α β} (x : m α) (y : Unit → m β) :
      f (SeqRight.seqRight x y) = SeqRight.seqRight (f x) (f <| y ·)
```

`Cslib.IsApplicativeHom.mk'` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L132))

> Construct an `IsApplicativeHom` for lawful applicatives from `map_pure` and `map_seq`.

```lean
theorem mk' [LawfulApplicative m] [LawfulApplicative n] {f : ∀ {α}, m α → n α}
    (map_pure : ∀ {α} (a : α), f (pure a) = pure a)
    (map_seq : ∀ {α β} (x : m (α → β)) (y : Unit → m α),
      f (Seq.seq x y) = Seq.seq (f x) (f <| y ·)) :
    IsApplicativeHom m n f
```

`Cslib.IsApplicativeHom.id` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L146))

```lean
protected theorem id : IsApplicativeHom m m id
```

`Cslib.IsApplicativeHom.comp` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L153))

```lean
protected theorem comp {f : ∀ {α}, n α → p α} {g : ∀ {α}, m α → n α}
    (hf : IsApplicativeHom n p f) (hg : IsApplicativeHom m n g) :
    IsApplicativeHom m p (f ∘ g)
```

> ### Monad Homomorphisms

`Cslib.IsMonadHom` (structure, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L170))

> A function `f` is a morphism of monads if it preserves `pure`, `>>=`, `<$>`, `<*>`, `<*`, and `*>`.

```lean
structure IsMonadHom (m n) [Monad m] [Monad n] (f : ∀ {α}, m α → n α) : Prop
    extends IsApplicativeHom m n f where
  map_bind {α β} (x : m α) (y : α → m β) : f (x >>= y) = f x >>= (f <| y ·)
```

`Cslib.IsMonadHom.mk'` (theorem, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L199))

> Construct an `IsMonadHom` for lawful monads from `map_pure` and `map_bind`.

```lean
theorem mk' [LawfulMonad m] [LawfulMonad n] {f : ∀ {α}, m α → n α}
    (map_pure : ∀ {α} (a : α), f (pure a) = pure a)
    (map_bind : ∀ {α β} (x : m α) (y : α → m β), f (x >>= y) = f x >>= (f <| y ·)) :
    IsMonadHom m n f
```

`Cslib.IsMonadHom.id` (theorem, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L207))

```lean
protected theorem id : IsMonadHom m m id
```

`Cslib.IsMonadHom.comp` (theorem, [line 211](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L211))

```lean
protected theorem comp {f : ∀ {α}, n α → p α} {g : ∀ {α}, m α → n α}
    (hf : IsMonadHom n p f) (hg : IsMonadHom m n g) :
    IsMonadHom m p (f ∘ g)
```

`Cslib.IsMonadHom.monadLift` (theorem, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L217))

```lean
protected theorem monadLift [LawfulMonad m] [LawfulMonad n]
    [MonadLift m n] [LawfulMonadLift m n] :
    IsMonadHom m n MonadLift.monadLift
```

`Cslib.IsMonadHom.monadLiftT` (theorem, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L222))

```lean
protected theorem monadLiftT [LawfulMonad m] [LawfulMonad n]
    [MonadLiftT m n] [LawfulMonadLiftT m n] :
    IsMonadHom m n monadLift
```

> ### Alternative Homomorphisms

`Cslib.IsAlternativeHom` (structure, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L235))

> A function `f` is a morphism of alternatives if it preserves `pure`, `<$>`, `<*>`, `<*`, `*>`,
> `failure`, and `orElse`.

```lean
structure IsAlternativeHom (m n) [Alternative m] [Alternative n] (f : ∀ {α}, m α → n α) : Prop
    extends IsApplicativeHom m n f where
  map_failure {α} : f (Alternative.failure : m α) = Alternative.failure
  map_orElse {α} (x : m α) (y : Unit → m α) :
    f (HOrElse.hOrElse x y) = HOrElse.hOrElse (f x) (f <| y ·)
```

`Cslib.IsAlternativeHom.mk'` (theorem, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L249))

> Construct an `IsAlternativeHom` for lawful applicatives from `map_pure`, `map_seq`,
> `map_failure`, and `map_orElse`.

```lean
theorem mk' [LawfulApplicative m] [LawfulApplicative n] {f : ∀ {α}, m α → n α}
    (map_pure : ∀ {α} (a : α), f (pure a) = pure a)
    (map_seq : ∀ {α β} (x : m (α → β)) (y : Unit → m α),
      f (Seq.seq x y) = Seq.seq (f x) (f <| y ·))
    (map_failure : ∀ {α}, f (Alternative.failure : m α) = Alternative.failure)
    (map_orElse : ∀ {α} (x : m α) (y : Unit → m α),
      f (HOrElse.hOrElse x y) = HOrElse.hOrElse (f x) (f <| y ·)) :
    IsAlternativeHom m n f
```

`Cslib.IsAlternativeHom.id` (theorem, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L262))

```lean
protected theorem id : IsAlternativeHom m m id
```

`Cslib.IsAlternativeHom.comp` (theorem, [line 267](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L267))

```lean
protected theorem comp {f : ∀ {α}, n α → p α} {g : ∀ {α}, m α → n α}
    (hf : IsAlternativeHom n p f) (hg : IsAlternativeHom m n g) :
    IsAlternativeHom m p (f ∘ g)
```

> ### Alternative Monad Homomorphisms

`Cslib.IsAlternativeMonadHom` (structure, [line 282](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L282))

> A function `f` is a morphism of alternative monads if it preserves monadic and alternative
> structure.

```lean
structure IsAlternativeMonadHom (m n) [AlternativeMonad m] [AlternativeMonad n]
    (f : ∀ {α}, m α → n α) : Prop
    extends IsMonadHom m n f, IsAlternativeHom m n f
```

`Cslib.IsAlternativeMonadHom.mk'` (theorem, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L293))

> Construct an `IsAlternativeMonadHom` for lawful monads from `map_pure`, `map_bind`,
> `map_failure`, and `map_orElse`.

```lean
theorem mk' [LawfulMonad m] [LawfulMonad n] {f : ∀ {α}, m α → n α}
    (map_pure : ∀ {α} (a : α), f (pure a) = pure a)
    (map_bind : ∀ {α β} (x : m α) (y : α → m β), f (x >>= y) = f x >>= (f <| y ·))
    (map_failure : ∀ {α}, f (Alternative.failure : m α) = Alternative.failure)
    (map_orElse : ∀ {α} (x : m α) (y : Unit → m α),
      f (HOrElse.hOrElse x y) = HOrElse.hOrElse (f x) (f <| y ·)) :
    IsAlternativeMonadHom m n f
```

`Cslib.IsAlternativeMonadHom.id` (theorem, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L305))

```lean
protected theorem id : IsAlternativeMonadHom m m id
```

`Cslib.IsAlternativeMonadHom.comp` (theorem, [line 310](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L310))

```lean
protected theorem comp {f : ∀ {α}, n α → p α} {g : ∀ {α}, m α → n α}
    (hf : IsAlternativeMonadHom n p f) (hg : IsAlternativeMonadHom m n g) :
    IsAlternativeMonadHom m p (f ∘ g)
```

`Cslib.IsMonadHom.wp` (theorem, [line 320](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean#L320))

```lean
theorem IsMonadHom.wp [Monad m] [WPMonad m ps] : IsMonadHom m (PredTrans ps) WP.wp
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Control/Monad/IsMonadHom.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom.lean)
