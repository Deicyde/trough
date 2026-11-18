---
catalog: module
lean: Cslib.Logic.Modal.BTL.Direction, Cslib.Logic.Modal.BTL.τBTL, Cslib.Logic.Modal.BTL.Proposition, Cslib.Logic.Modal.BTL.Proposition.always_eq_not_future_not, Cslib.Logic.Modal.BTL.Proposition.hasAlwaysBeen_eq_not_past_not, Cslib.Logic.Modal.BTL.Model, Cslib.Logic.Modal.BTL.Model.toFrame, Cslib.Logic.Modal.BTL.Model.toModal, Cslib.Logic.Modal.BTL.Model.toModal_toFrame, Cslib.Logic.Modal.BTL.Model.toFrame_future_iff, Cslib.Logic.Modal.BTL.Model.toFrame_past_iff, Cslib.Logic.Modal.Satisfies.btl_atom_iff, Cslib.Logic.Modal.Satisfies.btl_future_sometime_iff, Cslib.Logic.Modal.Satisfies.btl_past_sometime_iff, Cslib.Logic.Modal.Satisfies.btl_future_always_iff, Cslib.Logic.Modal.Satisfies.btl_past_always_iff, Cslib.Logic.Modal.Satisfies.btl_future_sometime_intro, Cslib.Logic.Modal.Satisfies.btl_past_sometime_intro, Cslib.Logic.Modal.Satisfies.btl_future_always_elim, Cslib.Logic.Modal.Satisfies.btl_past_always_elim, Cslib.Logic.Modal.Satisfies.btl_future_past, Cslib.Logic.Modal.Satisfies.btl_past_future
statement: formalized
proof: formalized
---

# Basic Temporal Logic (BTL)

`Cslib.Logics.BTL.Basic`, in [Cslib/Logics/BTL/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean), by Fabrizio Montesi.

> The basic temporal language has two unary modalities: `F` (sometime in the future) and
> `P` (sometime in the past).
>
> ## Notation
>
> Open `Cslib.Logic.Modal.BTL` for the directions `F` and `P` and the judgement `BTL[m,w ⊨ φ]`.
> With `Cslib.Logic` open, use the standard dynamic modalities `d⟨F⟩φ` and `d⟨P⟩φ` for
> sometime in the future and past, and `d[F]φ` and `d[P]φ` for always in the future and past.
> Satisfaction is expressed by `⇓BTL[m,w ⊨ φ]`, using the modal inference system.
>
> ## References
>
> * [P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*][Blackburn2001]

`Cslib.Logic.Modal.BTL.Direction` (inductive type, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L35))

> The two directions of the basic temporal language.

```lean
inductive Direction where
  /-- Into the future. -/
  | F
  /-- Into the past. -/
  | P
  deriving DecidableEq
```

`Cslib.Logic.Modal.BTL.τBTL` (abbreviation, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L45))

> The modal signature of the basic temporal language.

```lean
abbrev τBTL : PFunctor
```

`Cslib.Logic.Modal.BTL.Proposition` (abbreviation, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L48))

> Temporal propositions, with a unary modality for each direction.

```lean
abbrev Proposition Atom
```

`Cslib.Logic.Modal.BTL.Proposition.always_eq_not_future_not` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L51))

```lean
theorem Proposition.always_eq_not_future_not (φ : Proposition Atom) :
    (d[F]φ) = ¬d⟨F⟩¬φ
```

`Cslib.Logic.Modal.BTL.Proposition.hasAlwaysBeen_eq_not_past_not` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L55))

```lean
theorem Proposition.hasAlwaysBeen_eq_not_past_not (φ : Proposition Atom) :
    (d[P]φ) = ¬d⟨P⟩¬φ
```

`Cslib.Logic.Modal.BTL.Model` (structure, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L64))

> A temporal model consists of an accessibility relation and a valuation at each world.
>
> No order properties are imposed on the relation. In particular, the modalities include
> the present only when the relation is reflexive at the current world, and the flow of time is
> modelled only when the relation is transitive.

```lean
structure Model World Atom where
  /-- The accessibility relation. -/
  r : World → World → Prop
  /-- Valuation of atoms at each world. -/
  v : World → Atom → Prop
```

`Cslib.Logic.Modal.BTL.Model.toFrame` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L76))

> The bidirectional frame of a temporal model.
>
> This definition guarantees by construction that the future and past accessibility relations are
> inverse of each other. Modally, this is witnessed by `btl_future_past_prop` and
> `btl_past_future_prop`.

```lean
def Model.toFrame (m : Model World Atom) : Frame World τBTL
```

`Cslib.Logic.Modal.BTL.Model.toModal` (definition, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L82))

> Interprets a temporal model as a unary modal model.

```lean
def Model.toModal (m : Model World Atom) : Modal.Model World τBTL Atom
```

`Cslib.Logic.Modal.BTL.Model.toModal_toFrame` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L85))

```lean
theorem Model.toModal_toFrame (m : Model World Atom) : m.toModal.toFrame = m.toFrame
```

`Cslib.Logic.Modal.BTL.Model.toFrame_future_iff` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L88))

```lean
theorem Model.toFrame_future_iff (m : Model World Atom) (w w' : World) :
    m.toFrame.diagonal F w w' ↔ m.r w w'
```

`Cslib.Logic.Modal.BTL.Model.toFrame_past_iff` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L92))

```lean
theorem Model.toFrame_past_iff (m : Model World Atom) (w w' : World) :
    m.toFrame.diagonal P w w' ↔ m.r w' w
```

`Cslib.Logic.Modal.Satisfies.btl_atom_iff` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L110))

```lean
theorem Satisfies.btl_atom_iff {a : Atom} : ⇓BTL[m,w ⊨ a] ↔ m.v w a
```

`Cslib.Logic.Modal.Satisfies.btl_future_sometime_iff` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L113))

```lean
theorem Satisfies.btl_future_sometime_iff : ⇓BTL[m,w ⊨ d⟨F⟩φ] ↔ ∃ w', m.r w w' ∧ ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_past_sometime_iff` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L117))

```lean
theorem Satisfies.btl_past_sometime_iff : ⇓BTL[m,w ⊨ d⟨P⟩φ] ↔ ∃ w', m.r w' w ∧ ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_future_always_iff` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L121))

```lean
theorem Satisfies.btl_future_always_iff : ⇓BTL[m,w ⊨ d[F]φ] ↔ ∀ w', m.r w w' → ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_past_always_iff` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L125))

```lean
theorem Satisfies.btl_past_always_iff :
    ⇓BTL[m,w ⊨ d[P]φ] ↔ ∀ w', m.r w' w → ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_future_sometime_intro` (theorem, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L129))

```lean
theorem Satisfies.btl_future_sometime_intro (hr : m.r w w') (h : ⇓BTL[m,w' ⊨ φ]) :
    ⇓BTL[m,w ⊨ d⟨F⟩φ]
```

`Cslib.Logic.Modal.Satisfies.btl_past_sometime_intro` (theorem, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L133))

```lean
theorem Satisfies.btl_past_sometime_intro (hr : m.r w' w) (h : ⇓BTL[m,w' ⊨ φ]) :
    ⇓BTL[m,w ⊨ d⟨P⟩φ]
```

`Cslib.Logic.Modal.Satisfies.btl_future_always_elim` (theorem, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L137))

```lean
theorem Satisfies.btl_future_always_elim (h : ⇓BTL[m,w ⊨ d[F]φ]) (hr : m.r w w') : ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_past_always_elim` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L141))

```lean
theorem Satisfies.btl_past_always_elim (h : ⇓BTL[m,w ⊨ d[P]φ]) (hr : m.r w' w) : ⇓BTL[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.btl_future_past` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L145))

> If a proposition holds now, then it is always going to be the case that it was true.

```lean
theorem Satisfies.btl_future_past : ⇓BTL[m,w ⊨ φ → d[F](d⟨P⟩φ)]
```

`Cslib.Logic.Modal.Satisfies.btl_past_future` (theorem, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean#L149))

> If a proposition holds now, then it has always been the case that it will be true.

```lean
theorem Satisfies.btl_past_future : ⇓BTL[m,w ⊨ φ → d[P](d⟨F⟩φ)]
```

## Depends on

- [Semantics of Modal Logic](../modal/semantics.md)

## Proof depends on

- [Unary Modal Logic](../modal/unary/basic.md)

## Sources

- [Cslib/Logics/BTL/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/BTL/Basic.lean)
