---
catalog: module
lean: Cslib.Frame.rel, Cslib.Frame.rel_iff_diagonal, Cslib.Frame.ofRelation, Cslib.Frame.ofRelation_rel, Cslib.Frame.ofRelation_rel_iff, Cslib.Frame.ofRelation_rel_of, Cslib.Frame.preservesMap_const_iff_preserves, Cslib.Logic.Modal.Satisfies.diamond_iff_exists, Cslib.Logic.Modal.Satisfies.diamond_of, Cslib.Logic.Modal.Satisfies.box_iff_forall, Cslib.Logic.Modal.Satisfies.unimodal_k, Cslib.Logic.Modal.Satisfies.unimodal_dual, Cslib.Logic.Modal.Satisfies.diamond_and, Cslib.Logic.Modal.Satisfies.diamond_and_box, Cslib.Logic.Modal.Satisfies.diamond_of_box, Cslib.Logic.Modal.Satisfies.unimodal_t, Cslib.Logic.Modal.Satisfies.unimodal_t_refl, Cslib.Logic.Modal.Satisfies.t_box_diamond, Cslib.Logic.Modal.Satisfies.unimodal_b, Cslib.Logic.Modal.Satisfies.unimodal_b_symm, Cslib.Logic.Modal.Satisfies.unimodal_four, Cslib.Logic.Modal.Satisfies.unimodal_four_trans, Cslib.Logic.Modal.Satisfies.unimodal_five, Cslib.Logic.Modal.Satisfies.unimodal_five_rightEuclidean, Cslib.Logic.Modal.Satisfies.d, Cslib.Logic.Modal.Satisfies.d_serial, Cslib.Logic.Modal.Satisfies.l, Cslib.Logic.Modal.Satisfies.l_induction, Cslib.Logic.Modal.Satisfies.pointTwo, Cslib.Logic.Modal.Satisfies.pointTwo_diamond, Cslib.Logic.Modal.Proposition.diamond_and_equiv_of_preserves, Cslib.Logic.Modal.Proposition.diamond_diamond_equiv, Cslib.Logic.Modal.Proposition.Context.diamond, Cslib.Logic.Modal.τUnimodal, Cslib.Frame.ofRelation_unimodal_rel_iff, Cslib.Logic.Modal.Unimodal.Model, Cslib.Logic.Modal.Unimodal.Proposition
statement: formalized
proof: formalized
---

# Basic Modal Logic

`Cslib.Logics.Modal.Unimodal.Basic`, in [Cslib/Logics/Modal/Unimodal/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean), by Fabrizio Montesi, Marianna Girlando.

> Basic modal logic is the modal logic with a single unary modality.
>
> ## References
>
> * [P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*][Blackburn2001]

`Cslib.Frame.rel` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L35))

> The accessibility relation of a unimodal frame.

```lean
def rel (f : Frame World τ) : World → World → Prop
```

`Cslib.Frame.rel_iff_diagonal` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L39))

```lean
theorem rel_iff_diagonal (f : Frame World τ) (w w' : World) :
    f.rel w w' ↔ f.diagonal default w w'
```

`Cslib.Frame.ofRelation` (definition, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L44))

> Builds a unimodal frame out of a binary relation.

```lean
def ofRelation (r : World → World → Prop) : Frame World τ
```

`Cslib.Frame.ofRelation_rel` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L48))

```lean
theorem ofRelation_rel (r : World → World → Prop) : Frame.rel (Frame.ofRelation (τ := τ) r) = r
```

`Cslib.Frame.ofRelation_rel_iff` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L63))

```lean
theorem ofRelation_rel_iff (r : World → World → Prop) (w w' : World) :
    (ofRelation (τ := τ) r).rel w w' ↔ r w w'
```

`Cslib.Frame.ofRelation_rel_of` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L67))

```lean
theorem ofRelation_rel_of {r : World → World → Prop} {w w' : World}
    (h : r w w') : (ofRelation (τ := τ) r).rel w w'
```

`Cslib.Frame.preservesMap_const_iff_preserves` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L72))

```lean
theorem preservesMap_const_iff_preserves {r : α → α → Prop} {P : α → Prop} :
    (ofRelation (τ := τ) r).PreservesMap default P (fun _ => P) ↔ Preserves r P
```

`Cslib.Logic.Modal.Satisfies.diamond_iff_exists` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L89))

```lean
theorem Satisfies.diamond_iff_exists {m : Model World τ Atom} {φ : Proposition τ Atom} :
    ⇓Modal[m,w ⊨ ◇φ] ↔ ∃ w', m.rel w w' ∧ ⇓Modal[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.diamond_of` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L96))

```lean
theorem Satisfies.diamond_of {m : Model World τ Atom} {φ : Proposition τ Atom}
    (hr : m.toFrame.rel w w') (hφ : ⇓Modal[m,w' ⊨ φ]) : ⇓Modal[m,w ⊨ ◇φ]
```

`Cslib.Logic.Modal.Satisfies.box_iff_forall` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L101))

```lean
theorem Satisfies.box_iff_forall {m : Model World τ Atom} {φ : Proposition τ Atom} :
    ⇓Modal[m,w ⊨ □φ] ↔ ∀ w', m.rel w w' → ⇓Modal[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.unimodal_k` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L107))

> Axiom K for unimodal logic.

```lean
theorem Satisfies.unimodal_k (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    Axiom f⇓(□(φ₁ → φ₂) → (□φ₁ → □φ₂))
```

`Cslib.Logic.Modal.Satisfies.unimodal_dual` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L111))

> The dual axiom for unimodal logic.

```lean
theorem Satisfies.unimodal_dual (f : Frame World τ) (φ : Proposition τ Atom) :
    Axiom f⇓(◇φ ↔ ¬□¬φ)
```

`Cslib.Logic.Modal.Satisfies.diamond_and` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L115))

```lean
theorem Satisfies.diamond_and (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    Axiom f⇓(◇(φ₁ ∧ φ₂) → (◇φ₁ ∧ ◇φ₂))
```

`Cslib.Logic.Modal.Satisfies.diamond_and_box` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L119))

```lean
theorem Satisfies.diamond_and_box (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    Axiom f⇓((◇φ₁ ∧ □φ₂) → ◇(φ₁ ∧ φ₂))
```

`Cslib.Logic.Modal.Satisfies.diamond_of_box` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L123))

```lean
theorem Satisfies.diamond_of_box (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    Axiom f⇓(□φ₁ ∧ ◇φ₂ → ◇φ₁)
```

`Cslib.Logic.Modal.Satisfies.unimodal_t` (theorem, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L127))

> Axiom T.

```lean
theorem Satisfies.unimodal_t (f : Frame World τ) [instRefl : Std.Refl f.rel]
    (φ : Proposition τ Atom) : Axiom f⇓(φ → ◇φ)
```

`Cslib.Logic.Modal.Satisfies.unimodal_t_refl` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L131))

> Any frame that admits T is reflexive.

```lean
theorem Satisfies.unimodal_t_refl (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(φ → ◇φ)) : Std.Refl f.rel
```

`Cslib.Logic.Modal.Satisfies.t_box_diamond` (theorem, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L140))

> In any reflexive model, `□φ → φ` is equivalent to `φ → ◇φ`.

```lean
theorem Satisfies.t_box_diamond {m : Model World τ Atom} [Std.Refl m.rel] :
    ⇓Modal[m,w ⊨ □φ → φ] ↔ ⇓Modal[m,w ⊨ φ → ◇φ]
```

`Cslib.Logic.Modal.Satisfies.unimodal_b` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L146))

> Axiom B.

```lean
theorem Satisfies.unimodal_b (f : Frame World τ) [Std.Symm f.rel]
    (φ : Proposition τ Atom) : Axiom f⇓(φ → □◇φ)
```

`Cslib.Logic.Modal.Satisfies.unimodal_b_symm` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L153))

> Any frame that admits B is symmetric.

```lean
theorem Satisfies.unimodal_b_symm (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(φ → □◇φ)) : Std.Symm f.rel
```

`Cslib.Logic.Modal.Satisfies.unimodal_four` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L162))

> Axiom 4, valid for all transitive frames.

```lean
theorem Satisfies.unimodal_four (f : Frame World τ) [IsTrans World f.rel]
    (φ : Proposition τ Atom) : Axiom f⇓(◇◇φ → ◇φ)
```

`Cslib.Logic.Modal.Satisfies.unimodal_four_trans` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L170))

> Any frame that admits 4 is transitive.

```lean
theorem Satisfies.unimodal_four_trans (f : Frame World τ) [Nonempty Atom]
    (h : ∀ (φ : Proposition τ Atom), Axiom f⇓(◇◇φ → ◇φ)) : IsTrans World f.rel
```

`Cslib.Logic.Modal.Satisfies.unimodal_five` (theorem, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L179))

> Axiom 5.

```lean
theorem Satisfies.unimodal_five (f : Frame World τ) [Relation.RightEuclidean f.rel]
    (φ : Proposition τ Atom) : Axiom f⇓(◇φ → □◇φ)
```

`Cslib.Logic.Modal.Satisfies.unimodal_five_rightEuclidean` (theorem, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L185))

> Any frame that admits 5 is right Euclidean.

```lean
theorem Satisfies.unimodal_five_rightEuclidean (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(◇φ → □◇φ)) :
    Relation.RightEuclidean f.rel
```

`Cslib.Logic.Modal.Satisfies.d` (theorem, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L195))

> Axiom D, valid for all serial frames.

```lean
theorem Satisfies.d (f : Frame World τ) [Relation.Serial f.rel]
    (φ : Proposition τ Atom) : Axiom f⇓(□φ → ◇φ)
```

`Cslib.Logic.Modal.Satisfies.d_serial` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L202))

> Any model that admits D is serial.

```lean
theorem Satisfies.d_serial (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(□φ → ◇φ)) : Relation.Serial f.rel
```

`Cslib.Logic.Modal.Satisfies.l` (theorem, [line 211](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L211))

> The L axiom, or Löb's theorem, valid for all transitive and converse well-founded models.

```lean
theorem Satisfies.l (f : Frame World τ) [IsTrans World f.rel]
    (hwf : Relation.Terminating f.rel) (φ : Proposition τ Atom) :
    Axiom f⇓(□(□φ → φ) → □φ)
```

`Cslib.Logic.Modal.Satisfies.l_induction` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L228))

> Löb induction, via the L axiom.

```lean
theorem Satisfies.l_induction (m : Model World τ Atom) [IsTrans World m.rel]
    (hwf : Relation.Terminating m.rel) (hstep : ∀ w, ⇓Modal[m,w ⊨ □φ → φ]) (w : World) :
    ⇓Modal[m, w ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.pointTwo` (theorem, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L238))

> Axiom .2, valid for all frames with the diamond property.

```lean
theorem Satisfies.pointTwo (f : Frame World τ) (h : Diamond f.rel)
    (φ : Proposition τ Atom) : Axiom f⇓(◇□φ → □◇φ)
```

`Cslib.Logic.Modal.Satisfies.pointTwo_diamond` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L248))

> Any model that admits axiom .2 has the diamond property.

```lean
theorem Satisfies.pointTwo_diamond (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(◇□φ → □◇φ)) : Diamond f.rel
```

`Cslib.Logic.Modal.Proposition.diamond_and_equiv_of_preserves` (theorem, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L258))

> In a transitive diamond model, possibility distributes over conjunction for propositions
> whose satisfaction is preserved along accessibility.

```lean
theorem Proposition.diamond_and_equiv_of_preserves {m : Model World τ Atom}
    [IsTrans World m.rel] {φ₁ φ₂ : Proposition τ Atom} (hd : Diamond m.rel)
    (h₁ : Preserves m.rel (⇓Modal[m,· ⊨ φ₁])) (h₂ : Preserves m.rel (⇓Modal[m,· ⊨ φ₂])) :
    ◇(φ₁ ∧ φ₂) ≡[Equiv m] (◇φ₁ ∧ ◇φ₂)
```

`Cslib.Logic.Modal.Proposition.diamond_diamond_equiv` (theorem, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L278))

> In a reflexive and transitive model, diamond absorbs itself (idempotency).

```lean
theorem Proposition.diamond_diamond_equiv {m : Model World τ Atom} [Std.Refl m.rel]
    [IsTrans World m.rel] (φ : Proposition τ Atom) : ◇◇φ ≡[Equiv m] ◇φ
```

`Cslib.Logic.Modal.Proposition.Context.diamond` (definition, [line 288](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L288))

> Context constructor for the diamond modality.

```lean
def Proposition.Context.diamond (c : Context τ Atom) : Context τ Atom
```

`Cslib.Logic.Modal.τUnimodal` (definition, [line 291](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L291))

> Constructs a signature for basic modal logic at the same universe level of the input type.

```lean
def τUnimodal (_ : Type u) : PFunctor.{u,u}
```

`Cslib.Frame.ofRelation_unimodal_rel_iff` (theorem, [line 307](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L307))

```lean
theorem _root_.Cslib.Frame.ofRelation_unimodal_rel_iff
    (r : World → World → Prop) (w w' : World) :
    (Frame.ofRelation (τ := τUnimodal World) r).rel w w' ↔ r w w'
```

`Cslib.Logic.Modal.Unimodal.Model` (abbreviation, [line 315](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L315))

> A basic model, constructed on `τUnimodal`.

```lean
abbrev Model World Atom
```

`Cslib.Logic.Modal.Unimodal.Proposition` (abbreviation, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean#L318))

> The language of modal propositions instantiated for `τUnimodal Atom`.

```lean
abbrev Proposition Atom
```

## Depends on

- [Relations: Definitions](../../../foundations/relation/defs.md)
- [Unary Modal Logic](../unary/basic.md)

## Sources

- [Cslib/Logics/Modal/Unimodal/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Basic.lean)
