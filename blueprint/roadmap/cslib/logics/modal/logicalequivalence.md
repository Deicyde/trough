---
catalog: module
lean: Cslib.Logic.Modal.Proposition.Equiv, Cslib.Logic.Modal.Proposition.equiv_def, Cslib.Logic.Modal.Proposition.equiv_iff_forall_der, Cslib.Logic.Modal.Proposition.equiv_iff_forall_iff, Cslib.Logic.Modal.ModelClass, Cslib.Logic.Modal.Proposition.EquivWithin, Cslib.Logic.Modal.Proposition.UEquiv, Cslib.Logic.Modal.Proposition.equivWithin_def, Cslib.Logic.Modal.Proposition.equivWithin_iff_forall_iff, Cslib.Logic.Modal.Proposition.equiv_of_EquivWithin, Cslib.Logic.Modal.Proposition.equivWithin_valid, Cslib.Logic.Modal.PropositionMap.Without, Cslib.Logic.Modal.Proposition.Context, Cslib.Logic.Modal.Proposition.Context.fill, Cslib.Logic.Modal.Proposition.Context.fill_def, Cslib.Logic.Modal.Judgement.Context, Cslib.Logic.Modal.Judgement.Context.fill, Cslib.Logic.Modal.Judgement.Context.fill_def, Cslib.Logic.Modal.Proposition.axiom_iff_forall_equiv, Cslib.Logic.Modal.Proposition.equiv_of_axiom, Cslib.Logic.Modal.Proposition.axiom_iff_equivWithin_modelsOfFrame, Cslib.Logic.Modal.Proposition.dual_equiv
statement: formalized
proof: formalized
---

# Logical Equivalence in Modal Logic

`Cslib.Logics.Modal.LogicalEquivalence`, in [Cslib/Logics/Modal/LogicalEquivalence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean), by Fabrizio Montesi.

> This module defines logical equivalence for modal propositions.
> The definitions are parametric on the class of models under consideration.
>
> We also instantiate `LogicalEquivalence` for Modal Logic K, i.e., equivalence
> for the class of all models.

`Cslib.Logic.Modal.Proposition.Equiv` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L28))

> The modal propositions `φ₁` and `φ₂` are equivalent in the model `m`.

```lean
def Proposition.Equiv (m : Model World τ Atom) (φ₁ φ₂ : Proposition τ Atom) : Prop
```

`Cslib.Logic.Modal.Proposition.equiv_def` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L34))

```lean
theorem Proposition.equiv_def (m : Model World τ Atom) (φ₁ φ₂ : Proposition τ Atom) :
    (φ₁.Equiv m φ₂) ↔ φ₁ ≡[Equiv m] φ₂
```

`Cslib.Logic.Modal.Proposition.equiv_iff_forall_der` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L38))

```lean
theorem Proposition.equiv_iff_forall_der (m : Model World τ Atom) (φ₁ φ₂ : Proposition τ Atom)
    : (φ₁ ≡[Equiv m] φ₂) ↔ ∀ (w : World), ⇓Modal[m,w ⊨ φ₁ ↔ φ₂]
```

`Cslib.Logic.Modal.Proposition.equiv_iff_forall_iff` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L42))

```lean
theorem Proposition.equiv_iff_forall_iff {m : Model World τ Atom} {φ₁ φ₂ : Proposition τ Atom} :
    (φ₁ ≡[Equiv m] φ₂) ↔ ∀ (w : World), ⇓Modal[m,w ⊨ φ₁] ↔ ⇓Modal[m,w ⊨ φ₂]
```

`Cslib.Logic.Modal.ModelClass` (abbreviation, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L47))

> A class of models, defined as a set.

```lean
abbrev ModelClass (World : Type*) (τ : PFunctor) (Atom : Type*)
```

`Cslib.Logic.Modal.Proposition.EquivWithin` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L50))

> The modal propositions `φ₁` and `φ₂` are equivalent in the model class `S`.

```lean
def Proposition.EquivWithin (S : ModelClass World τ Atom) (φ₁ φ₂ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.UEquiv` (abbreviation, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L56))

> Universal logical equivalence: `φ₁` and `φ₂` are equivalent in the class of all models.

```lean
abbrev Proposition.UEquiv {World : Type*} (φ₁ φ₂ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.equivWithin_def` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L60))

```lean
theorem Proposition.equivWithin_def (S : ModelClass World τ Atom) (φ₁ φ₂ : Proposition τ Atom) :
    φ₁.EquivWithin S φ₂ ↔ (φ₁ ≡[EquivWithin S] φ₂)
```

`Cslib.Logic.Modal.Proposition.equivWithin_iff_forall_iff` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L64))

```lean
theorem Proposition.equivWithin_iff_forall_iff :
    (φ₁ ≡[EquivWithin S] φ₂) ↔ ∀ m ∈ S, φ₁ ≡[Equiv m] φ₂
```

`Cslib.Logic.Modal.Proposition.equiv_of_EquivWithin` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L68))

```lean
theorem Proposition.equiv_of_EquivWithin {S : ModelClass World τ Atom} (h : φ₁ ≡[EquivWithin S] φ₂)
    (m : Model World τ Atom) (hm : m ∈ S) : φ₁ ≡[Equiv m] φ₂
```

`Cslib.Logic.Modal.Proposition.equivWithin_valid` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L72))

> Logical equivalence preserves validity.

```lean
theorem Proposition.equivWithin_valid (S : ModelClass World τ Atom)
    (φ₁ φ₂ : Proposition τ Atom) (h : φ₁ ≡[EquivWithin S] φ₂) :
    (φ₁.valid S ↔ φ₂.valid S)
```

`Cslib.Logic.Modal.PropositionMap.Without` (abbreviation, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L78))

> A proposition map missing a particular case (index).

```lean
abbrev PropositionMap.Without (τ : PFunctor) (Atom : Type*) (op : τ.A) (i : τ.B op)
```

`Cslib.Logic.Modal.Proposition.Context` (inductive type, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L82))

> Propositional contexts.

```lean
inductive Proposition.Context (τ : PFunctor) (Atom : Type u) where
  | hole
  | not (c : Context τ Atom)
  | andL (c : Context τ Atom) (φ : Proposition τ Atom)
  | andR (φ : Proposition τ Atom) (c : Context τ Atom)
  | triangle (op : τ.A) (i : τ.B op) (c : Context τ Atom)
    (φs : PropositionMap.Without τ Atom op i)
```

`Cslib.Logic.Modal.Proposition.Context.fill` (definition, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L92))

> Replaces a hole in a propositional context with a proposition.

```lean
def Proposition.Context.fill {τ : PFunctor} [τ.DecidableEqChildren] {Atom : Type*}
    (c : Context τ Atom) (φ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.Context.fill_def` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L109))

```lean
lemma Proposition.Context.fill_def {τ : PFunctor} [τ.DecidableEqChildren] {Atom : Type*}
    {c : HasContext.Context (Proposition τ Atom)} {φ : Proposition τ Atom} :
  c.fill φ = c<[φ]
```

`Cslib.Logic.Modal.Judgement.Context` (structure, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L168))

> Judgemental contexts.

```lean
structure Judgement.Context (World : Type*) (τ : PFunctor) (Atom : Type*) where
  /-- The model to consider. -/
  m : Model World τ Atom
  /-- The world to check propositions against. -/
  w : World
```

`Cslib.Logic.Modal.Judgement.Context.fill` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L175))

> Fills a judgemental context with a proposition.

```lean
def Judgement.Context.fill (c : Judgement.Context World τ Atom) (φ : Proposition τ Atom) :
    Judgement World τ Atom
```

`Cslib.Logic.Modal.Judgement.Context.fill_def` (lemma, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L182))

```lean
lemma Judgement.Context.fill_def {c : Judgement.Context World τ Atom} {φ : Proposition τ Atom} :
    Modal[c.m,c.w ⊨ φ] = c<[φ]
```

`Cslib.Logic.Modal.Proposition.axiom_iff_forall_equiv` (theorem, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L200))

> Correspondence of equivalence and axiom validity.

```lean
theorem Proposition.axiom_iff_forall_equiv (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    (Axiom f⇓(φ₁ ↔ φ₂)) ↔ ∀ v, φ₁ ≡[Equiv ⟨f, v⟩] φ₂
```

`Cslib.Logic.Modal.Proposition.equiv_of_axiom` (theorem, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L205))

> A frame-valid bi-implication induces logical equivalence in every model over that frame.

```lean
theorem Proposition.equiv_of_axiom {f : Frame World τ} {φ₁ φ₂ : Proposition τ Atom}
    (h : Axiom f⇓(φ₁ ↔ φ₂)) (v : World → Atom → Prop) : φ₁ ≡[Equiv ⟨f, v⟩] φ₂
```

`Cslib.Logic.Modal.Proposition.axiom_iff_equivWithin_modelsOfFrame` (theorem, [line 211](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L211))

> A bi-implication is an axiom of `f` iff its sides are equivalent in every model over `f`.

```lean
theorem Proposition.axiom_iff_equivWithin_modelsOfFrame
    (f : Frame World τ) (φ₁ φ₂ : Proposition τ Atom) :
    Axiom f⇓(φ₁ ↔ φ₂) ↔ φ₁ ≡[EquivWithin (modelsOfFrame f)] φ₂
```

`Cslib.Logic.Modal.Proposition.dual_equiv` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean#L216))

> Triangle and the negation of the dual nabla are universally logically equivalent.

```lean
theorem Proposition.dual_equiv (φs : PropositionMap τ op Atom) :
    Δ[op]φs ≡[UEquiv (World := World)] ¬∇[op]¬φs
```

## Depends on

- [LogicalEquivalence](../../foundations/logic/logicalequivalence.md)
- [Semantics of Modal Logic](semantics.md)

## Sources

- [Cslib/Logics/Modal/LogicalEquivalence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/LogicalEquivalence.lean)
