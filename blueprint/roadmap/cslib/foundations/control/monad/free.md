---
catalog: module
lean: Cslib.FreeM, Cslib.FreeM.pure_eq_pure, Cslib.FreeM.bind, Cslib.FreeM.bind_eq_bind, Cslib.FreeM.map, Cslib.FreeM.map_eq_map, Cslib.FreeM.lift, Cslib.FreeM.liftBind_eq, Cslib.FreeM.induction, Cslib.FreeM.bind_assoc, Cslib.FreeM.pure_bind, Cslib.FreeM.bind_pure, Cslib.FreeM.bind_pure_comp, Cslib.FreeM.map_pure, Cslib.FreeM.map_bind, Cslib.FreeM.id_map, Cslib.FreeM.comp_map, Cslib.FreeM.liftM, Cslib.FreeM.liftM_pure, Cslib.FreeM.liftM_lift_bind, Cslib.FreeM.liftM_lift, Cslib.FreeM.liftM_bind, Cslib.IsMonadHom.map_freeMLiftM, Cslib.FreeM.isMonadHom_liftM, Cslib.FreeM.liftM_map, Cslib.FreeM.liftM_seq, Cslib.FreeM.liftM_seqLeft, Cslib.FreeM.liftM_seqRight, Cslib.FreeM.Interprets, Cslib.FreeM.Interprets.eq, Cslib.FreeM.Interprets.liftM, Cslib.FreeM.Interprets.iff, Cslib.FreeM.liftM_lift_eq_self, Cslib.FreeM.liftM_comp
statement: formalized
proof: formalized
---

# Free Monad (Free)

`Cslib.Foundations.Control.Monad.Free`, in [Cslib/Foundations/Control/Monad/Free.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean), by Tanner Duve, Eric Wieser.

> This file defines a general `FreeM` monad construction for representing effectful programs
> as pure syntax trees, separate from their interpretation.
>
> The `FreeM` monad generates a free monad from any type constructor `f : Type → Type`, without
> requiring `f` to be a `Functor`. This implementation uses the "freer monad" approach as the
> traditional free monad is not safely definable in Lean due to termination checking.
>
> In this construction, **effectful programs are represented as trees of effects**.
> Each node (`FreeM.liftBind`) represents a request to perform an effect, accompanied by a
> continuation specifying how the computation proceeds after the effect.
> The leaves (`FreeM.pure`) represent completed computations with final results.
>
> This separation of syntax from semantics enables multiple interpretations of the same program:
> execution, static analysis, optimization, pretty-printing, verification, and more.
>
> A key insight is that `FreeM F` satisfies the **universal property of free monads**: for any monad
> `M` and effect handler `f : F → M`, there exists a unique way to interpret `FreeM F` computations
> in `M` that respects the effect semantics given by `f`.
> This unique interpreter is `FreeM.liftM f`
>
>
> ## Main Definitions
>
> - `FreeM`: The free monad construction
> - `FreeM.liftM`: The canonical interpreter satisfying the universal property
> - `FreeM.liftM_unique`: Proof of the universal property
>
> For elimination and interpretation theory, see `Free/Fold.lean`.
> For polynomial effect signatures with explicit operation shapes and positions, see
> `Cslib.Foundations.Data.PFunctor.Free`.
>
> See the Haskell [freer-simple](https://hackage.haskell.org/package/freer-simple) library for the
> Haskell implementation that inspired this approach.
>
> ## Implementation Notes
>
> The `FreeM` monad is defined using an inductive type with constructors `.pure` and `.liftBind`.
> We implement `Functor` and `Monad` instances, and prove the corresponding `LawfulFunctor`
> and `LawfulMonad` instances.
>
>
> The file `Free/Effects.lean` demonstrates practical applications by implementing State, Writer, and
> Continuations monads using `FreeM` with appropriate effect signatures.
>
> The file `Free/Fold.lean` provides the theory of the fold operation for free monads.
>
> ## References
>
> * [Oleg Kiselyov, Hiromi Ishii. *Freer Monads, More Extensible Effects*][Kiselyov2015]
> * [Bartosz Milewski. *The Dao of Functional Programming*][MilewskiDao]
>
> ## Tags
>
> Free monad, state monad

`Cslib.FreeM` (inductive type, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L87))

> The Free monad over a type constructor `F`.
>
> A `FreeM F a` is a tree of operations from the type constructor `F`, with leaves of type `a`.
> It has two constructors: `pure` for wrapping a value of type `a`, and `liftBind` for
> representing an operation from `F` followed by a continuation.
>
> This construction provides a free monad for any type constructor `F`, allowing for composable
> effect descriptions that can be interpreted later. Unlike the traditional free monad,
> this does not require `F` to be a functor.

```lean
inductive FreeM.{u, v, w} (F : Type u → Type v) (α : Type w) where
  /-- The action that does nothing and returns `a`. -/
  | protected pure (a : α) : FreeM F α
  /-- Invoke the operation `op` with contuation `cont`.

  Note that Lean's inductive types prevent us splitting this into separate bind and lift
  constructors. -/
  | liftBind {ι : Type u} (op : F ι) (cont : ι → FreeM F α) : FreeM F α
```

`Cslib.FreeM.pure_eq_pure` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L106))

```lean
theorem pure_eq_pure : FreeM.pure = (pure : α → FreeM F α)
```

`Cslib.FreeM.bind` (definition, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L111))

> Bind operation for the `FreeM` monad.
>
> The builtin `>>=` notation should be preferred when `α` and `β` are in the same universe.

```lean
protected def bind (x : FreeM F α) (f : α → FreeM F β) : FreeM F β
```

`Cslib.FreeM.bind_eq_bind` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L120))

> Note that this lemma does not always apply, as it is universe-constrained by `Bind.bind`.

```lean
theorem bind_eq_bind {α β : Type w} : (FreeM.bind : FreeM F α → _ → FreeM F β) = Bind.bind
```

`Cslib.FreeM.map` (definition, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L125))

> Map a function over a `FreeM` monad.
>
> The builtin `<$>` notation should be preferred when `α` and `β` are in the same universe.

```lean
def map (f : α → β) : FreeM F α → FreeM F β
```

`Cslib.FreeM.map_eq_map` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L134))

> Note that this lemma does not always apply, as it is universe-constrained by `Functor.map`.

```lean
theorem map_eq_map {α β : Type w} : FreeM.map (F := F) (α := α) (β := β) = Functor.map
```

`Cslib.FreeM.lift` (definition, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L137))

> Lift an operation from the effect signature `F` into the `FreeM F` monad.

```lean
def lift (op : F ι) : FreeM F ι
```

`Cslib.FreeM.liftBind_eq` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L141))

```lean
lemma liftBind_eq (op : F ι) :
    liftBind op cont = (lift op : FreeM F ι).bind cont
```

`Cslib.FreeM.induction` (theorem, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L150))

> An override for the default induction principle that is in simp-normal form.
>
> Note that when `α` and `ι` are in the same universe, this simplifies slightly further.

```lean
protected theorem induction {motive : FreeM F α → Prop}
    (pure : ∀ a, motive (pure a))
    (lift_bind : ∀ {ι} (op : F ι) (cont : ι → FreeM F α) (ih : ∀ i, motive (cont i)),
      motive ((lift op).bind cont)) : ∀ x, motive x
```

`Cslib.FreeM.bind_assoc` (theorem, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L159))

```lean
protected theorem bind_assoc (x : FreeM F α) (f : α → FreeM F β) (g : β → FreeM F γ) :
    (x.bind f).bind g = x.bind (fun x => (f x).bind g)
```

`Cslib.FreeM.pure_bind` (lemma, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L167))

> `.pure a` followed by `bind` collapses immediately.

```lean
lemma pure_bind (a : α) (f : α → FreeM F β) : (pure a : FreeM F α).bind f = f a
```

`Cslib.FreeM.bind_pure` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L170))

```lean
lemma bind_pure : ∀ x : FreeM F α, x.bind pure = x
```

`Cslib.FreeM.bind_pure_comp` (lemma, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L175))

```lean
lemma bind_pure_comp (f : α → β) : ∀ x : FreeM F α, x.bind (pure ∘ f) = map f x
```

`Cslib.FreeM.map_pure` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L180))

```lean
theorem map_pure (f : α → β) (x : α) : map f (pure x : FreeM F α) = pure (f x)
```

`Cslib.FreeM.map_bind` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L183))

```lean
theorem map_bind (f : β → γ) (x : FreeM F α) (c : α → FreeM F β) :
    map f (x.bind c) = x.bind fun a => (c a).map f
```

`Cslib.FreeM.id_map` (theorem, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L188))

```lean
theorem id_map : ∀ x : FreeM F α, map id x = x
```

`Cslib.FreeM.comp_map` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L192))

```lean
theorem comp_map (h : β → γ) (g : α → β) : ∀ x : FreeM F α, map (h ∘ g) x = map h (map g x)
```

`Cslib.FreeM.liftM` (definition, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L220))

> Interpret a `FreeM F` computation into any monad `m` by providing an interpretation
> function for the effect signature `F`.
>
> This function defines the *canonical interpreter* from the free monad `FreeM F` into the target
> monad `m`. It is the unique monad morphism that extends the effect handler
> `interp : ∀ {β}, F β → m β` via the universal property of `FreeM`.

```lean
protected def liftM (interp : {ι : Type u} → F ι → m ι) : FreeM F α → m α
```

`Cslib.FreeM.liftM_pure` (lemma, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L225))

```lean
lemma liftM_pure (interp : {ι : Type u} → F ι → m ι) (a : α) :
    (pure a : FreeM F α).liftM interp = pure a
```

`Cslib.FreeM.liftM_lift_bind` (lemma, [line 229](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L229))

```lean
lemma liftM_lift_bind (interp : {ι : Type u} → F ι → m ι) (op : F β) (cont : β → FreeM F α) :
    ((lift op) >>= cont).liftM interp = (do let b ← interp op; (cont b).liftM interp)
```

`Cslib.FreeM.liftM_lift` (lemma, [line 234](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L234))

```lean
lemma liftM_lift [LawfulMonad m] (interp : {ι : Type u} → F ι → m ι) (op : F β) :
    (lift op).liftM interp = interp op
```

`Cslib.FreeM.liftM_bind` (lemma, [line 240](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L240))

```lean
lemma liftM_bind [LawfulMonad m]
    (interp : {ι : Type u} → F ι → m ι) (x : FreeM F α) (f : α → FreeM F β) :
    (x >>= f).liftM interp = (do let a ← x.liftM interp; (f a).liftM interp)
```

`Cslib.IsMonadHom.map_freeMLiftM` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L248))

> A morphism of monads moves inside `FreeM.liftM`.

```lean
theorem _root_.Cslib.IsMonadHom.map_freeMLiftM [Monad n]
    {f : ∀ {α}, m α → n α} (hf : IsMonadHom m n f)
    (interp : {ι : Type u} → F ι → m ι) (x : FreeM F α) :
    f (x.liftM interp) = x.liftM (fun op => f (interp op))
```

`Cslib.FreeM.isMonadHom_liftM` (theorem, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L258))

> `FreeM.liftM interp` is a morphism of monads.

```lean
theorem isMonadHom_liftM [LawfulMonad m] (interp : {ι : Type u} → F ι → m ι) :
    IsMonadHom (FreeM F) m (FreeM.liftM interp)
```

`Cslib.FreeM.liftM_map` (lemma, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L263))

```lean
lemma liftM_map [LawfulMonad m]
    (interp : {ι : Type u} → F ι → m ι) (f : α → β) (x : FreeM F α) :
    (f <$> x).liftM @interp = f <$> x.liftM @interp
```

`Cslib.FreeM.liftM_seq` (lemma, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L269))

```lean
lemma liftM_seq [LawfulMonad m]
    (interp : {ι : Type u} → F ι → m ι) (x : FreeM F (α → β)) (y : FreeM F α) :
    (x <*> y).liftM interp = x.liftM interp <*> y.liftM interp
```

`Cslib.FreeM.liftM_seqLeft` (lemma, [line 275](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L275))

```lean
lemma liftM_seqLeft [LawfulMonad m]
    (interp : {ι : Type u} → F ι → m ι) (x : FreeM F α) (y : FreeM F β) :
    (x <* y).liftM interp = x.liftM interp <* y.liftM interp
```

`Cslib.FreeM.liftM_seqRight` (lemma, [line 281](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L281))

```lean
lemma liftM_seqRight [LawfulMonad m]
    (interp : {ι : Type u} → F ι → m ι) (x : FreeM F α) (y : FreeM F β) :
    (x *> y).liftM interp = x.liftM interp *> y.liftM interp
```

`Cslib.FreeM.Interprets` (structure, [line 298](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L298))

> A predicate stating that `interp : FreeM F α → m α` is an interpreter for the effect
> handler `handler : ∀ {α}, F α → m α`.
>
> This means that `interp` is a monad morphism from the free monad `FreeM F` to the
> monad `m`, and that it extends the interpretation of individual operations
> given by `f`.
>
> Formally, `interp` satisfies the two equations:
> - `interp (pure a) = pure a`
> - `interp (liftBind op k) = handler op >>= fun x => interp (k x)`

```lean
structure Interprets (handler : {ι : Type u} → F ι → m ι) (interp : FreeM F α → m α) : Prop where
  apply_pure (a : α) : interp (.pure a) = pure a
  apply_lift_bind {ι : Type u} (op : F ι) (cont : ι → FreeM F α) :
    interp (lift op >>= cont) = handler op >>= fun x => interp (cont x)
```

`Cslib.FreeM.Interprets.eq` (theorem, [line 303](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L303))

```lean
theorem Interprets.eq {handler : {ι : Type u} → F ι → m ι} {interp : FreeM F α → m α}
    (h : Interprets handler interp) :
    interp = (·.liftM @handler)
```

`Cslib.FreeM.Interprets.liftM` (theorem, [line 312](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L312))

```lean
theorem Interprets.liftM (handler : {ι : Type u} → F ι → m ι) :
    Interprets handler (·.liftM handler : FreeM F α → _)
```

`Cslib.FreeM.Interprets.iff` (theorem, [line 323](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L323))

> The universal property of the free monad `FreeM`.
>
> That is, `liftM handler` is the unique interpreter that extends the effect handler `handler` to
> interpret `FreeM F` computations in a monad `m`.

```lean
theorem Interprets.iff (handler : {ι : Type u} → F ι → m ι) (interp : FreeM F α → m α) :
    Interprets handler interp ↔ interp = (·.liftM handler)
```

`Cslib.FreeM.liftM_lift_eq_self` (theorem, [line 331](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L331))

> Interpreting each operation by its lift into the free monad is the identity.

```lean
theorem liftM_lift_eq_self {α : Type u} (x : FreeM F α) : FreeM.liftM lift x = x
```

`Cslib.FreeM.liftM_comp` (theorem, [line 337](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean#L337))

> Interpreting into a free monad and then into `m` composes the two handlers.

```lean
theorem liftM_comp {m : Type u → Type w} [Monad m] [LawfulMonad m]
    {G : Type u → Type w'} {α : Type u} (x : FreeM F α)
    (first : {ι : Type u} → F ι → FreeM G ι) (second : {ι : Type u} → G ι → m ι) :
    (x.liftM first).liftM second = x.liftM fun op => (first op).liftM second
```

## Depends on

- [(unbundled) morphisms of monads](ismonadhom.md)

## Sources

- [Cslib/Foundations/Control/Monad/Free.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free.lean)
