---
catalog: module
lean: PFunctor.FreeM, PFunctor.FreeM.pure_eq_pure, PFunctor.FreeM.lift, PFunctor.FreeM.lift_ne_pure, PFunctor.FreeM.pure_ne_lift, PFunctor.FreeM.bind, PFunctor.FreeM.bind_eq_bind, PFunctor.FreeM.map, PFunctor.FreeM.map_eq_map, PFunctor.FreeM.liftBind_eq, PFunctor.FreeM.liftObj, PFunctor.FreeM.liftObj_ne_pure, PFunctor.FreeM.pure_ne_liftObj, PFunctor.FreeM.monadLift_eq_liftObj, PFunctor.FreeM.induction, PFunctor.FreeM.bind_assoc, PFunctor.FreeM.pure_bind, PFunctor.FreeM.bind_pure, PFunctor.FreeM.bind_pure_comp, PFunctor.FreeM.map_pure, PFunctor.FreeM.map_bind, PFunctor.FreeM.liftBind_bind, PFunctor.FreeM.liftObj_bind, PFunctor.FreeM.bind_eq_pure_iff, PFunctor.FreeM.pure_eq_bind_iff, PFunctor.FreeM.id_map, PFunctor.FreeM.comp_map, PFunctor.FreeM.pure_inj, PFunctor.FreeM.liftBind_inj, PFunctor.FreeM.liftM, PFunctor.FreeM.liftM_pure, PFunctor.FreeM.liftM_lift_bind, PFunctor.FreeM.Interprets, PFunctor.FreeM.Interprets.eq, PFunctor.FreeM.Interprets.liftM, PFunctor.FreeM.Interprets.iff, Cslib.IsMonadHom.map_pfunctorFreeMLiftM, PFunctor.FreeM.liftM_bind, PFunctor.FreeM.isMonadHom_liftM, PFunctor.FreeM.liftM_map, PFunctor.FreeM.liftM_seq, PFunctor.FreeM.liftM_seqLeft, PFunctor.FreeM.liftM_seqRight, PFunctor.FreeM.liftM_lift, PFunctor.FreeM.liftM_liftObj, PFunctor.FreeM.liftM_lift_eq_self, PFunctor.FreeM.liftM_comp
statement: formalized
proof: formalized
---

# Free Monad of a Polynomial Functor

`Cslib.Foundations.Data.PFunctor.Free`, in [Cslib/Foundations/Data/PFunctor/Free.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean), by Quang Dao.

> We define the free monad on a **polynomial functor** (`PFunctor`), and prove some basic properties.
>
> The free monad `PFunctor.FreeM P` extends the W-type construction with an extra `pure`
> constructor, yielding a monad that is free over the polynomial functor `P`.
>
> ## Comparison with `Cslib.FreeM`
>
> `Cslib.FreeM F` (in `Cslib/Foundations/Control/Monad/Free.lean`) builds a free monad over an
> arbitrary type constructor `F : Type u → Type v`, which need not be functorial.
> Its `liftBind` constructor abstracts over the intermediate type `ι`:
> ```
> | liftBind {ι : Type u} (op : F ι) (cont : ι → FreeM F α) : FreeM F α
> ```
>
> `PFunctor.FreeM P` instead takes a polynomial functor `P : PFunctor`, where the shapes
> `P.A` and positions `P.B a` are given explicitly.
> Its `liftBind` constructor uses the shape and continuation directly:
> ```
> | liftBind (a : P.A) (cont : P.B a → P.FreeM α) : P.FreeM α
> ```
>
> When the effect signature is naturally polynomial (a fixed set of operations, each with a
> known return type), `PFunctor.FreeM` avoids the universe bump that the abstract `ι` in
> `Cslib.FreeM` introduces.
> Concretely, `PFunctor.FreeM P` is a genuine endofunctor on a single universe: for a ground
> `P`, `P.FreeM α : Type` whenever `α : Type`, whereas `Cslib.FreeM F α : Type 1` for
> `F : Type → Type`, since `liftBind` stores the intermediate type `ι : Type`.
>
> This matters when a program must itself be a first-class value of the same kind, i.e. for
> higher-order effects whose operations consume or return computations of the same monad
> (schedulers, exception handlers, staged interpreters, higher-order oracles).
> Such an effect's response type can be another `P.FreeM` computation, staying in one universe:
> ```
> def coin : PFunctor.{0,0} := ⟨Bool, fun b => if b then Bool else Nat⟩
> -- a `coin`-program is itself `Type 0`, so it can be another effect's response type:
> def scheduler : PFunctor.{0,0} := ⟨Unit, fun _ => coin.FreeM Bool⟩  -- `Type 0`
> ```
> With the abstract `ι`, the analogous program lives in `Type 1`, so an effect `Type → Type`
> cannot return it; bumping the effect to `Type 1 → Type 1` pushes its programs to `Type 2`,
> and so on without bound.
>
> This construction is ported from the [VCV-io](https://github.com/dtumad/VCV-io) library.
>
> ## Main Definitions
>
> - `PFunctor.FreeM`: The free monad on a polynomial functor.
> - `PFunctor.FreeM.lift`: Lift a shape of the base polynomial functor into the free monad.
> - `PFunctor.FreeM.liftObj`: Lift an object of the base polynomial functor into the free monad.
> - `PFunctor.FreeM.liftM`: Interpret `FreeM P` into any other monad.

`PFunctor.FreeM` (inductive type, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L78))

> The free monad on a polynomial functor.
> This extends `WType` with an extra `pure` constructor.

```lean
inductive FreeM (P : PFunctor.{uA, uB}) : Type v → Type (max uA uB v)
  /-- A leaf node wrapping a pure value. -/
  | protected pure {α} (a : α) : P.FreeM α
  /-- Invoke the operation `a : P.A` with continuation `cont : P.B a → P.FreeM α`. -/
  | liftBind {α} (a : P.A) (cont : P.B a → P.FreeM α) : P.FreeM α
deriving Inhabited
```

`PFunctor.FreeM.pure_eq_pure` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L92))

```lean
theorem pure_eq_pure : (FreeM.pure : α → P.FreeM α) = pure
```

`PFunctor.FreeM.lift` (definition, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L95))

> Lift a shape of the base polynomial functor into the free monad.

```lean
def lift (a : P.A) : P.FreeM (P.B a)
```

`PFunctor.FreeM.lift_ne_pure` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L97))

```lean
lemma lift_ne_pure (a : P.A) (y : P.B a) :
    (lift a : P.FreeM (P.B a)) ≠ pure y
```

`PFunctor.FreeM.pure_ne_lift` (lemma, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L100))

```lean
lemma pure_ne_lift (a : P.A) (y : P.B a) :
    pure y ≠ (lift a : P.FreeM (P.B a))
```

`PFunctor.FreeM.bind` (definition, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L106))

> Bind operation for the `FreeM` monad.
>
> The builtin `>>=` notation should be preferred when `α` and `β` are in the same universe.

```lean
protected def bind : P.FreeM α → (α → P.FreeM β) → P.FreeM β
```

`PFunctor.FreeM.bind_eq_bind` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L114))

> Note that this lemma does not always apply, as it is universe-constrained by `Bind.bind`.

```lean
theorem bind_eq_bind {α β : Type v} :
    (FreeM.bind : P.FreeM α → _ → P.FreeM β) = Bind.bind
```

`PFunctor.FreeM.map` (definition, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L120))

> Map a function over a `FreeM` computation.
>
> The builtin `<$>` notation should be preferred when `α` and `β` are in the same universe.

```lean
def map (f : α → β) : P.FreeM α → P.FreeM β
```

`PFunctor.FreeM.map_eq_map` (theorem, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L129))

> Note that this lemma does not always apply, as it is universe-constrained by `Functor.map`.

```lean
theorem map_eq_map {α β : Type v} :
    FreeM.map (P := P) (α := α) (β := β) = Functor.map
```

`PFunctor.FreeM.liftBind_eq` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L133))

```lean
lemma liftBind_eq (a : P.A) (cont : P.B a → P.FreeM α) :
    FreeM.liftBind a cont = (FreeM.lift a).bind cont
```

`PFunctor.FreeM.liftObj` (abbreviation, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L141))

> Lift an object of the base polynomial functor into the free monad.
>
> This lifts the shape `x.1` with `lift` and relabels the responses with `x.2`. We use the
> universe-polymorphic `FreeM.map` rather than `<$>`, since the response type `P.B x.1` and the
> target `α` need not lie in the same universe.

```lean
abbrev liftObj (x : P.Obj α) : P.FreeM α
```

`PFunctor.FreeM.liftObj_ne_pure` (lemma, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L146))

```lean
lemma liftObj_ne_pure (x : P.Obj α) (y : α) :
    (liftObj x : P.FreeM α) ≠ pure y
```

`PFunctor.FreeM.pure_ne_liftObj` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L149))

```lean
lemma pure_ne_liftObj (x : P.Obj α) (y : α) :
    pure y ≠ (liftObj x : P.FreeM α)
```

`PFunctor.FreeM.monadLift_eq_liftObj` (lemma, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L152))

```lean
lemma monadLift_eq_liftObj (x : P.Obj α) : (x : P.FreeM α) = FreeM.liftObj x
```

`PFunctor.FreeM.induction` (theorem, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L159))

> An override for the default induction principle that is in simp-normal form.
>
> Note that when `α` and `P.B a` are in the same universe, this simplifies slightly further.

```lean
protected theorem induction {motive : P.FreeM α → Prop}
    (pure : ∀ a, motive (pure a))
    (lift_bind : ∀ (a : P.A) (cont : P.B a → P.FreeM α) (ih : ∀ i, motive (cont i)),
      motive ((FreeM.lift a).bind cont)) : ∀ x, motive x
```

`PFunctor.FreeM.bind_assoc` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L166))

```lean
protected theorem bind_assoc (x : P.FreeM α) (f : α → P.FreeM β) (g : β → P.FreeM γ) :
    (x.bind f).bind g = x.bind (fun a => (f a).bind g)
```

`PFunctor.FreeM.pure_bind` (lemma, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L174))

> `.pure a` followed by `bind` collapses immediately.

```lean
lemma pure_bind (a : α) (f : α → P.FreeM β) :
    (pure a : P.FreeM α).bind f = f a
```

`PFunctor.FreeM.bind_pure` (lemma, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L178))

```lean
lemma bind_pure : ∀ x : P.FreeM α, x.bind pure = x
```

`PFunctor.FreeM.bind_pure_comp` (lemma, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L184))

```lean
lemma bind_pure_comp (f : α → β) : ∀ x : P.FreeM α, x.bind (pure ∘ f) = map f x
```

`PFunctor.FreeM.map_pure` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L189))

```lean
theorem map_pure (f : α → β) (x : α) : map f (pure x : P.FreeM α) = pure (f x)
```

`PFunctor.FreeM.map_bind` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L192))

```lean
theorem map_bind (f : β → γ) (x : P.FreeM α) (cont : α → P.FreeM β) :
    map f (x.bind cont) = x.bind fun a => (cont a).map f
```

`PFunctor.FreeM.liftBind_bind` (lemma, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L197))

```lean
lemma liftBind_bind (a : P.A) (cont : P.B a → P.FreeM β) (f : β → P.FreeM γ) :
    ((FreeM.lift a).bind cont).bind f = (FreeM.lift a).bind (fun u ↦ (cont u).bind f)
```

`PFunctor.FreeM.liftObj_bind` (lemma, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L203))

```lean
lemma liftObj_bind (x : P.Obj α) (f : α → P.FreeM β) :
    (FreeM.liftObj x).bind f = FreeM.liftBind x.1 (fun a ↦ f (x.2 a))
```

`PFunctor.FreeM.bind_eq_pure_iff` (lemma, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L206))

```lean
lemma bind_eq_pure_iff (x : P.FreeM α) (f : α → P.FreeM β) (b : β) :
    x.bind f = pure b ↔ ∃ a, x = pure a ∧ f a = pure b
```

`PFunctor.FreeM.pure_eq_bind_iff` (lemma, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L217))

```lean
lemma pure_eq_bind_iff (x : P.FreeM α) (f : α → P.FreeM β) (b : β) :
    pure b = x.bind f ↔ ∃ a, x = pure a ∧ pure b = f a
```

`PFunctor.FreeM.id_map` (theorem, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L231))

```lean
theorem id_map : ∀ x : P.FreeM α, map id x = x
```

`PFunctor.FreeM.comp_map` (theorem, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L239))

```lean
theorem comp_map (h : β → γ) (g : α → β) :
    ∀ x : P.FreeM α, map (h ∘ g) x = map h (map g x)
```

`PFunctor.FreeM.pure_inj` (lemma, [line 255](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L255))

```lean
lemma pure_inj (a b : α) : (pure a : P.FreeM α) = pure b ↔ a = b
```

`PFunctor.FreeM.liftBind_inj` (lemma, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L262))

```lean
lemma liftBind_inj (a a' : P.A)
    (cont : P.B a → P.FreeM α) (cont' : P.B a' → P.FreeM α) :
    FreeM.liftBind a cont = FreeM.liftBind a' cont' ↔ ∃ h : a = a', h ▸ cont = cont'
```

`PFunctor.FreeM.liftM` (definition, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L278))

> Interpret a `FreeM P` computation into any monad `m` by providing an interpretation
> `interp : (a : P.A) → m (P.B a)` for each operation.

```lean
protected def liftM [Pure m] [Bind m] (interp : (a : P.A) → m (P.B a)) : P.FreeM α → m α
```

`PFunctor.FreeM.liftM_pure` (lemma, [line 285](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L285))

```lean
lemma liftM_pure (a : α) : (Pure.pure a : P.FreeM α).liftM interp = Pure.pure a
```

`PFunctor.FreeM.liftM_lift_bind` (lemma, [line 288](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L288))

```lean
lemma liftM_lift_bind (a : P.A) (cont : P.B a → P.FreeM α) :
    FreeM.liftM interp (FreeM.lift a >>= cont) =
      (do let u ← interp a; (cont u).liftM interp)
```

`PFunctor.FreeM.Interprets` (structure, [line 302](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L302))

> A predicate stating that `eval : P.FreeM α → m α` is an interpreter for the polynomial
> effect handler `handler : (a : P.A) → m (P.B a)`.
>
> This means that `eval` is a monad morphism from the free monad `P.FreeM` to the
> monad `m`, and that it extends the interpretation of individual operations given by
> `handler`.

```lean
structure Interprets (handler : (a : P.A) → m (P.B a)) (eval : P.FreeM α → m α) : Prop where
  apply_pure (a : α) : eval (.pure a) = pure a
  apply_lift_bind (a : P.A) (cont : P.B a → P.FreeM α) :
    eval ((FreeM.lift a).bind cont) = handler a >>= fun x => eval (cont x)
```

`PFunctor.FreeM.Interprets.eq` (theorem, [line 307](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L307))

```lean
theorem Interprets.eq {handler : (a : P.A) → m (P.B a)} {eval : P.FreeM α → m α}
    (h : Interprets handler eval) :
    eval = (·.liftM handler)
```

`PFunctor.FreeM.Interprets.liftM` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L318))

```lean
theorem Interprets.liftM (handler : (a : P.A) → m (P.B a)) :
    Interprets handler (·.liftM handler : P.FreeM α → _)
```

`PFunctor.FreeM.Interprets.iff` (theorem, [line 329](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L329))

> The universal property of the free monad `P.FreeM`.
>
> That is, `liftM handler` is the unique interpreter that extends the effect handler `handler` to
> interpret `P.FreeM` computations in a monad `m`.

```lean
theorem Interprets.iff (handler : (a : P.A) → m (P.B a)) (eval : P.FreeM α → m α) :
    Interprets handler eval ↔ eval = (·.liftM handler)
```

`Cslib.IsMonadHom.map_pfunctorFreeMLiftM` (theorem, [line 334](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L334))

> A morphism of monads moves inside `FreeM.liftM`.

```lean
theorem _root_.Cslib.IsMonadHom.map_pfunctorFreeMLiftM [Monad n]
    {f : ∀ {α}, m α → n α} (hf : Cslib.IsMonadHom m n f) (interp : (a : P.A) → m (P.B a))
    (x : P.FreeM α) :
    f (x.liftM interp) = x.liftM (fun op => f (interp op))
```

`PFunctor.FreeM.liftM_bind` (lemma, [line 346](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L346))

```lean
lemma liftM_bind {α β : Type uB} (x : P.FreeM α) (f : α → P.FreeM β) :
    (x >>= f).liftM interp = (do let u ← x.liftM interp; (f u).liftM interp)
```

`PFunctor.FreeM.isMonadHom_liftM` (theorem, [line 359](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L359))

> `FreeM.liftM interp` is a morphism of monads.

```lean
theorem isMonadHom_liftM : Cslib.IsMonadHom P.FreeM m (FreeM.liftM interp)
```

`PFunctor.FreeM.liftM_map` (lemma, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L363))

```lean
lemma liftM_map {α β : Type uB} (f : α → β) (interp : (a : P.A) → m (P.B a)) (x : P.FreeM α) :
    (f <$> x).liftM interp = f <$> x.liftM interp
```

`PFunctor.FreeM.liftM_seq` (lemma, [line 368](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L368))

```lean
lemma liftM_seq {α β : Type uB}
    (interp : (a : P.A) → m (P.B a)) (x : P.FreeM (α → β)) (y : P.FreeM α) :
    (x <*> y).liftM interp = x.liftM interp <*> y.liftM interp
```

`PFunctor.FreeM.liftM_seqLeft` (lemma, [line 374](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L374))

```lean
lemma liftM_seqLeft {α β : Type uB}
    (interp : (a : P.A) → m (P.B a)) (x : P.FreeM α) (y : P.FreeM β) :
    (x <* y).liftM interp = x.liftM interp <* y.liftM interp
```

`PFunctor.FreeM.liftM_seqRight` (lemma, [line 380](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L380))

```lean
lemma liftM_seqRight {α β : Type uB}
    (interp : (a : P.A) → m (P.B a)) (x : P.FreeM α) (y : P.FreeM β) :
    (x *> y).liftM interp = x.liftM interp *> y.liftM interp
```

`PFunctor.FreeM.liftM_lift` (lemma, [line 386](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L386))

```lean
lemma liftM_lift (interp : (a : P.A) → m (P.B a)) (a : P.A) :
    (FreeM.lift a).liftM interp = interp a
```

`PFunctor.FreeM.liftM_liftObj` (lemma, [line 392](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L392))

```lean
lemma liftM_liftObj (interp : (a : P.A) → m (P.B a)) (x : P.Obj α) :
    (FreeM.liftObj x).liftM interp = x.2 <$> interp x.1
```

`PFunctor.FreeM.liftM_lift_eq_self` (theorem, [line 400](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L400))

> Interpreting each operation by its lift into the free monad is the identity.

```lean
theorem liftM_lift_eq_self {α : Type uB} (x : P.FreeM α) : FreeM.liftM FreeM.lift x = x
```

`PFunctor.FreeM.liftM_comp` (theorem, [line 406](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean#L406))

> Interpreting into a free monad and then into `m` composes the two handlers.

```lean
theorem liftM_comp {m : Type uB → Type v} [Monad m] [LawfulMonad m]
    {Q : PFunctor.{u, uB}} {α : Type uB} (x : P.FreeM α)
    (first : (a : P.A) → Q.FreeM (P.B a)) (second : (a : Q.A) → m (Q.B a)) :
    (x.liftM first).liftM second = x.liftM fun a => (first a).liftM second
```

## Depends on

- [(unbundled) morphisms of monads](../../control/monad/ismonadhom.md)

## Sources

- [Cslib/Foundations/Data/PFunctor/Free.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free.lean)
