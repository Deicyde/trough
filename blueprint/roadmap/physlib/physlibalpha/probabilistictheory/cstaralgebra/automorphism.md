---
declaration: module
origin: cited
lean: StarAlgEquiv.observable, StarAlgEquiv.observable_coe, StarAlgEquiv.refl_observable, StarAlgEquiv.trans_observable, StarAlgEquiv.symm_observable_observable, StarAlgEquiv.observable_symm_observable, StarAlgEquiv.observable_bracket, StarAlgEquiv.toQuantumChannel
statement: formalized
proof: formalized
---

# ⋆-automorphisms and reversible dynamics

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Automorphism`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean): 32 declarations, 30 with a docstring.

> ⋆-automorphisms as channels on observables, and one-parameter groups of them as reversible dynamics.

## i. Overview

> Reversible transformations of a quantum system act on its algebra by `⋆`-automorphisms. A
> `⋆`-automorphism maps observables to observables, compatibly with composition, inverses and the Lie
> bracket, and it is a quantum channel. A one-parameter group of `⋆`-automorphisms is reversible
> dynamics; it can be transported along a `⋆`-isomorphism and induces dynamics of the observables.

## ii. Key results

> - `StarAlgEquiv.observable` : a `⋆`-automorphism acting on observables.
> - `StarAlgEquiv.observable_bracket` : `⋆`-automorphisms preserve the Lie bracket.
> - `StarAlgEquiv.toQuantumChannel`, `StarAlgEquiv.toObservableChannel` : a `⋆`-isomorphism as a
>   quantum channel and as a channel of observables.
> - `AutomorphismGroup` : a one-parameter group of `⋆`-automorphisms.
> - `AutomorphismGroup.conj` : conjugating dynamics by a `⋆`-automorphism.
> - `AutomorphismGroup.toObservableDynamics` : the induced dynamics of observables.

## iv. References

> * None.

## A. Action on observables

**`StarAlgEquiv.observable`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L64).

> A ⋆-automorphism `β` acts on observables by `a ↦ β a`.

```lean
def _root_.StarAlgEquiv.observable (β : A ≃⋆ₐ[ℂ] A) (a : Observable A) : Observable A
```

**`StarAlgEquiv.observable_coe`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L72).

> Unfolds `StarAlgEquiv.observable` to its underlying algebra element.

```lean
lemma _root_.StarAlgEquiv.observable_coe (β : A ≃⋆ₐ[ℂ] A) (a : Observable A) :
    (β.observable a : A) = β (a : A)
```

**`StarAlgEquiv.refl_observable`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L78).

> The identity automorphism acts trivially on observables.

```lean
lemma _root_.StarAlgEquiv.refl_observable :
    (StarAlgEquiv.refl (R := ℂ) (A := A)).observable = id
```

**`StarAlgEquiv.trans_observable`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L86).

> Composing `β` then `γ` acts on observables as `γ ∘ β`.

```lean
lemma _root_.StarAlgEquiv.trans_observable (β γ : A ≃⋆ₐ[ℂ] A) (a : Observable A) :
    (β.trans γ).observable a = γ.observable (β.observable a)
```

**`StarAlgEquiv.symm_observable_observable`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L93).

> Undoing `β.observable` by `β.symm.observable` recovers the original observable.

```lean
lemma _root_.StarAlgEquiv.symm_observable_observable (β : A ≃⋆ₐ[ℂ] A) (a : Observable A) :
    β.symm.observable (β.observable a) = a
```

**`StarAlgEquiv.observable_symm_observable`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L100).

> Applying `β.observable` after `β.symm.observable` recovers the original observable.

```lean
lemma _root_.StarAlgEquiv.observable_symm_observable (β : A ≃⋆ₐ[ℂ] A) (a : Observable A) :
    β.observable (β.symm.observable a) = a
```

**`StarAlgEquiv.observable_bracket`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L105).

> Star automorphisms preserve the observable Lie bracket.

```lean
lemma _root_.StarAlgEquiv.observable_bracket (β : A ≃⋆ₐ[ℂ] A) (a b : Observable A) :
    β.observable ⁅a, b⁆ = ⁅β.observable a, β.observable b⁆
```

## B. ⋆-isomorphisms as channels

**`StarAlgEquiv.toQuantumChannel`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L120).

> The quantum channel of a ⋆-isomorphism.

```lean
noncomputable def _root_.StarAlgEquiv.toQuantumChannel (β : A ≃⋆ₐ[ℂ] B) : QuantumChannel A B
```

**`StarAlgEquiv.toObservableChannel`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L125).

> The channel a ⋆-isomorphism induces between the self-adjoint observables.

```lean
noncomputable def _root_.StarAlgEquiv.toObservableChannel (β : A ≃⋆ₐ[ℂ] B) :
    Channel (selfAdjoint A) (selfAdjoint B)
```

**`StarAlgEquiv.coe_toObservableChannel_apply`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L146).

```lean
lemma _root_.StarAlgEquiv.coe_toObservableChannel_apply (β : A ≃⋆ₐ[ℂ] B) (a : selfAdjoint A) :
    (β.toObservableChannel a : B) = β (a : A)
```

**`StarAlgEquiv.toObservableChannel_apply`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L157).

> On observables of a single algebra, the induced channel is the action on observables.

```lean
lemma _root_.StarAlgEquiv.toObservableChannel_apply (β : A ≃⋆ₐ[ℂ] A) (a : selfAdjoint A) :
    β.toObservableChannel a = β.observable a
```

**`StarAlgEquiv.observableSymmetry`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L161).

> Every C⋆-⋆-automorphism induces a symmetry of the self-adjoint observables.

```lean
noncomputable def _root_.StarAlgEquiv.observableSymmetry (β : A ≃⋆ₐ[ℂ] A) :
    Symmetry (selfAdjoint A)
```

**`StarAlgEquiv.val_observableSymmetry`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L168).

```lean
lemma _root_.StarAlgEquiv.val_observableSymmetry (β : A ≃⋆ₐ[ℂ] A) :
    (β.observableSymmetry : Channel (selfAdjoint A) (selfAdjoint A)) = β.toObservableChannel
```

## C. Reversible one-parameter dynamics

**`ProbabilisticTheory.AutomorphismGroup`**, a structure, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L177).

> A one-parameter group of star-algebra automorphisms.

```lean
structure AutomorphismGroup (A : Type*) [Ring A] [StarRing A] [Module ℂ A] where
  /-- The automorphism at time `t`. -/
  toFun : ℝ → (A ≃⋆ₐ[ℂ] A)
  /-- Evolution at time zero is the identity. -/
  map_zero_apply : ∀ a : A, toFun 0 a = a
  /-- The group law, with evolution by `t` followed by evolution by `s`. -/
  map_add_apply : ∀ (s t : ℝ) (a : A), toFun (s + t) a = toFun s (toFun t a)
```

**`ProbabilisticTheory.AutomorphismGroup.ext`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L187).

> An automorphism group is determined by its action at every time.

```lean
lemma AutomorphismGroup.ext {A : Type*} [Ring A] [StarRing A] [Module ℂ A]
    {α β : AutomorphismGroup A} (h : ∀ t a, α.toFun t a = β.toFun t a) : α = β
```

## D. Order-unit dynamics induced by C⋆-automorphisms

**`ProbabilisticTheory.AutomorphismGroup.toObservableDynamics`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L204).

> The dynamics of observables induced by a one-parameter group of `⋆`-automorphisms.

```lean
noncomputable def AutomorphismGroup.toObservableDynamics (α : AutomorphismGroup A) :
    OneParameterAutomorphismGroup (selfAdjoint A)
```

**`ProbabilisticTheory.AutomorphismGroup.toObservableDynamics_apply`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L223).

> The observable dynamics is the restriction of the algebraic dynamics at each time.

```lean
lemma AutomorphismGroup.toObservableDynamics_apply (α : AutomorphismGroup A) (t : ℝ)
    (a : selfAdjoint A) : α.toObservableDynamics t a = (α.toFun t).observable a
```

## E. Transporting and conjugating automorphism groups

> A ⋆-isomorphism `β : A ≃⋆ₐ[ℂ] B` transports a dynamics on `A` to one on `B`. The defining
> commuting square says that applying `β` after evolving in `A` agrees with evolving after applying
> `β`. This is the dynamics-level counterpart of the channel covariance API: it is the form used by
> a quadratic normal-form equivalence, and it also applies to any later change of algebraic
> description.
>
> Conjugation is the special case `A = B`.

**`ProbabilisticTheory.AutomorphismGroup.transport`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L244).

> Transport a one-parameter ⋆-automorphism group across a ⋆-isomorphism.

```lean
def AutomorphismGroup.transport (β : A ≃⋆ₐ[ℂ] B) (α : AutomorphismGroup A) :
    AutomorphismGroup B
```

**`ProbabilisticTheory.AutomorphismGroup.transport_apply`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L254).

> Unfolds transported dynamics: evolve after pulling back through the ⋆-isomorphism.

```lean
lemma AutomorphismGroup.transport_apply (β : A ≃⋆ₐ[ℂ] B) (α : AutomorphismGroup A)
    (t : ℝ) (b : B) :
    (α.transport β).toFun t b = β (α.toFun t (β.symm b))
```

**`ProbabilisticTheory.AutomorphismGroup.IsIntertwining`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L260).

> A ⋆-isomorphism intertwines two dynamics when its square commutes at every time.

```lean
def AutomorphismGroup.IsIntertwining (α : AutomorphismGroup A) (γ : AutomorphismGroup B)
    (β : A ≃⋆ₐ[ℂ] B) : Prop
```

**`ProbabilisticTheory.AutomorphismGroup.isIntertwining_transport`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L266).

> Transported dynamics is intertwined with the original dynamics by the transporting
> ⋆-isomorphism.

```lean
lemma AutomorphismGroup.isIntertwining_transport (β : A ≃⋆ₐ[ℂ] B)
    (α : AutomorphismGroup A) :
    α.IsIntertwining (α.transport β) β
```

**`ProbabilisticTheory.AutomorphismGroup.isIntertwining_iff_eq_transport`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L273).

> A ⋆-isomorphism intertwines a flow with precisely the dynamics transported along it.

```lean
lemma AutomorphismGroup.isIntertwining_iff_eq_transport (α : AutomorphismGroup A)
    (γ : AutomorphismGroup B) (β : A ≃⋆ₐ[ℂ] B) :
    α.IsIntertwining γ β ↔ γ = α.transport β
```

**`ProbabilisticTheory.AutomorphismGroup.IsIntertwining.trans`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L285).

> Intertwining squares compose along composable ⋆-isomorphisms.

```lean
lemma AutomorphismGroup.IsIntertwining.trans {α : AutomorphismGroup A} {γ : AutomorphismGroup B}
    {δ : AutomorphismGroup C} {β : A ≃⋆ₐ[ℂ] B} {χ : B ≃⋆ₐ[ℂ] C}
    (hβ : α.IsIntertwining γ β) (hχ : γ.IsIntertwining δ χ) :
    α.IsIntertwining δ (β.trans χ)
```

**`ProbabilisticTheory.AutomorphismGroup.transport_refl`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L295).

> Transport through the identity ⋆-isomorphism leaves a flow unchanged.

```lean
lemma AutomorphismGroup.transport_refl (α : AutomorphismGroup A) :
    α.transport (StarAlgEquiv.refl (R := ℂ) (A := A)) = α
```

**`ProbabilisticTheory.AutomorphismGroup.transport_trans`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L302).

> Successive changes of algebraic coordinates transport a flow by their composite.

```lean
lemma AutomorphismGroup.transport_trans (α : AutomorphismGroup A) (β : A ≃⋆ₐ[ℂ] B)
    (γ : B ≃⋆ₐ[ℂ] C) :
    (α.transport β).transport γ = α.transport (β.trans γ)
```

**`ProbabilisticTheory.AutomorphismGroup.transport_symm_transport`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L312).

> Transporting back through the inverse ⋆-isomorphism recovers the original flow.

```lean
lemma AutomorphismGroup.transport_symm_transport (α : AutomorphismGroup A) (β : A ≃⋆ₐ[ℂ] B) :
    (α.transport β).transport β.symm = α
```

## F. Conjugating an automorphism group by a star automorphism

> Changing which ⋆-automorphism `β` identifies the algebra with itself conjugates a flow `α`:
> `(conj β α) t = β ∘ α t ∘ β⁻¹`.

**`ProbabilisticTheory.AutomorphismGroup.conj`**, a def, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L331).

> The automorphism group `α`, viewed through the change of coordinates `β`:
> `(conj β α) t = β ∘ (α t) ∘ β⁻¹`.

```lean
def AutomorphismGroup.conj (β : A ≃⋆ₐ[ℂ] A) (α : AutomorphismGroup A) : AutomorphismGroup A
```

**`ProbabilisticTheory.AutomorphismGroup.conj_apply`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L338).

> Unfolds `AutomorphismGroup.conj` to `(conj β α) t a = β (α t (β⁻¹ a))`.

```lean
lemma AutomorphismGroup.conj_apply (β : A ≃⋆ₐ[ℂ] A) (α : AutomorphismGroup A) (t : ℝ) (a : A) :
    (α.conj β).toFun t a = β (α.toFun t (β.symm a))
```

**`ProbabilisticTheory.AutomorphismGroup.conj_refl`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L344).

> Conjugating by the identity automorphism changes nothing.

```lean
lemma AutomorphismGroup.conj_refl (α : AutomorphismGroup A) :
    α.conj (StarAlgEquiv.refl (R := ℂ) (A := A)) = α
```

**`ProbabilisticTheory.AutomorphismGroup.conj_conj`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L351).

> Conjugating successively by `β` then `γ` is the same as conjugating once by `β.trans γ`.

```lean
lemma AutomorphismGroup.conj_conj (α : AutomorphismGroup A) (β γ : A ≃⋆ₐ[ℂ] A) :
    (α.conj β).conj γ = α.conj (β.trans γ)
```

**`ProbabilisticTheory.AutomorphismGroup.conj_symm_conj`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L359).

> Conjugating by `β` and then undoing it with `β.symm` recovers the original flow.

```lean
lemma AutomorphismGroup.conj_symm_conj (α : AutomorphismGroup A) (β : A ≃⋆ₐ[ℂ] A) :
    (α.conj β).conj β.symm = α
```

**`ProbabilisticTheory.AutomorphismGroup.conj_conj_symm`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean#L367).

> Conjugating by `β.symm` and then undoing it with `β` recovers the original flow.

```lean
lemma AutomorphismGroup.conj_conj_symm (α : AutomorphismGroup A) (β : A ≃⋆ₐ[ℂ] A) :
    (α.conj β.symm).conj β = α
```

## Depends on

- [Symmetries](../channel/symmetry.md)
- [Quantum channels](quantumchannel.md)
- [The Lie bracket of observables](../staralgebra/lie.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Automorphism.lean)
