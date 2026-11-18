---
declaration: module
origin: cited
lean: JetComponentSpace, JetComponentSpace.repLorentzGroup, JetComponentSpace.repLorentzGroup_fst, JetComponentSpace.repLorentzGroup_snd, JetComponentSpace.repLorentzGroup_fst_tmul, JetComponentSpace.jetDeriv, JetComponentSpace.jetDeriv_fst_tmul, JetComponentSpace.jetDeriv_snd_tmul
statement: formalized
proof: formalized
---

# The jet component space of a matter field

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetComponent.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean): 35 declarations, 23 with a docstring; 2 private, not shown.

## i. Overview

> For a matter field valued in a complex vector space `V`, the *jet component space* is the
> span of the derivative symbols `∂_s ψ_α` and their conjugates `∂_s ψ̄_α`: the local
> coordinate functions on the space of jets of the field. This file defines that space and
> the structure on it that does not involve a gauge group: the Lorentz action, the jet
> derivative, functoriality in `V` and the mass-weight scaling. The action of a gauge group
> is in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetComponent.GaugeAction`.
>
>
> - `JetComponentSpace` : the space of component functions.
> - `JetComponentSpace.repLorentzGroup` : the Lorentz action on the component space.
> - `JetComponentSpace.jetDeriv` : the shift `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the label.
> - `JetComponentSpace.jetDeriv_comm` : the shifts in different directions commute.
> - `JetComponentSpace.repLorentzGroup_jetDeriv` : the shift is a Lorentz vector.
> - `JetComponentSpace.comap` : functoriality, contravariant in the target space.
> - `JetComponentSpace.comapEquiv` : a relabelling of the target space relabels the
>   component functions.
> - `JetComponentSpace.massWeightScale` : the mass-weight scaling.
> - `JetComponentSpace.comap_comp_massWeightScale` : the scaling is natural in the target
>   space, hence blind to which part of it a component function came from.
> - `JetComponentSpace.fstPiEquiv`, `JetComponentSpace.sndPiEquiv` : the two halves of the
>   component space of a finite product of target spaces split.

## ii. Key results

> - `JetComponentSpace` : the space of component functions of the matter field `M`: the span of the
>   symbols `∂_s ψ_α` and their conjugates `∂_s ψ̄_α`, where `α` runs over the target space `M.V`
> - `JetComponentSpace.repLorentzGroup` : the Lorentz action on the jet component space
> - `JetComponentSpace.jetDeriv` : the derivative of components in the jet component space, in the
>   direction `μ`: the shift `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the derivative label, and likewise on the
>   conjugate components
> - `JetComponentSpace.jetDeriv_comm` : total derivatives commute
> - `JetComponentSpace.repLorentzGroup_jetDeriv` : the jet derivative is a Lorentz vector on the
>   component space
> - `JetComponentSpace.comap` : the component space is contravariant in the target space
> - `JetComponentSpace.comapEquiv` : a relabelling of the target space relabels the component
>   functions
> - `JetComponentSpace.massWeightScale` : the mass-weight scaling on the jet component space of a
>   field of mass weight `w` (twice the mass dimension): the generator `∂_s φ_α` and its conjugate are
>   scaled by `c ^ (w + 2 |s|)`, through the derivative-degree scaling
>   `SpaceTimeDerivAlgebraℂ.gradeScale` on the derivative label
> - `JetComponentSpace.comap_comp_massWeightScale` : the mass-weight scaling is natural in the target
>   space
> - `JetComponentSpace.fstPiEquiv` : the unconjugated half of the component space of a finite direct
>   sum splits
> - `JetComponentSpace.sndPiEquiv` : the conjugate half of the component space of a finite direct sum
>   splits, by the same argument applied to the conjugate modules, using that conjugation commutes
>   with products

## iv. References

> * None.

**`JetComponentSpace`**, an abbrev, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L97).

> The space of component functions of the matter field `M`: the span of the symbols
> `∂_s ψ_α` and their conjugates `∂_s ψ̄_α`, where `α` runs over the target space `M.V`. The
> first factor holds the unconjugated symbols, the second the conjugate ones; in each,
> `SpaceTimeDerivAlgebraℂ` carries the derivative label `s` and the dual factor the target
> component `α`.
>
> Only `M.V` enters the space itself; the field's Lorentz and gauge representations and its
> mass weight enter the structure carried on it below. Taking the whole matter field rather
> than its value space is what lets that structure be read off `M` instead of being supplied
> by hand at each use.

```lean
abbrev JetComponentSpace (M : MatterField jets) : Type
```

## A. The Lorentz action on the component space

**`JetComponentSpace.repLorentzGroup`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L117).

> **The Lorentz action on the jet component space.** Under a Lorentz transformation a
> matter field transforms as `ψ(x) ↦ ρ(Λ) ψ(Λ⁻¹ x)`, so a derivative symbol `∂_s ψ_α` is
> acted on in *both* of its labels: the derivative multiset `s` by the Lorentz action on
> covectors, extended to `SpaceTimeDerivAlgebraℂ`, and the target index `α` by the
> contragredient of `ρ`.
>
> Unlike the gauge action, this needs no fibrewise-linearity or finite-dimensionality
> hypothesis: the two labels transform independently, so the action is simply a tensor
> product of representations. The conjugate half is the same with `ρ` replaced by its
> conjugate, the symbols `∂_s ψ̄_α` transforming by `star` of the spinor matrix.

```lean
noncomputable def JetComponentSpace.repLorentzGroup (M : MatterField jets) :
    Representation ℂ SL(2,ℂ) (JetComponentSpace M)
```

**`JetComponentSpace.repLorentzGroup_fst`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L123).

```lean
lemma JetComponentSpace.repLorentzGroup_fst (Λ : SL(2,ℂ)) (x : JetComponentSpace M) :
    (JetComponentSpace.repLorentzGroup M Λ x).1
      = (SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod M.repLorentz.dual) Λ x.1
```

**`JetComponentSpace.repLorentzGroup_snd`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L128).

```lean
lemma JetComponentSpace.repLorentzGroup_snd (Λ : SL(2,ℂ)) (x : JetComponentSpace M) :
    (JetComponentSpace.repLorentzGroup M Λ x).2
      = (SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod M.repLorentz.conj.dual) Λ x.2
```

**`JetComponentSpace.repLorentzGroup_fst_tmul`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L134).

> On a pure symbol the Lorentz action is diagonal in the two labels: the derivative
> label transforms in `SpaceTimeDerivAlgebraℂ`, the target index contragrediently.

```lean
lemma JetComponentSpace.repLorentzGroup_fst_tmul (Λ : SL(2,ℂ)) (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ M.V)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V)) :
    (JetComponentSpace.repLorentzGroup M Λ (a ⊗ₜ[ℂ] φ, y)).1
      = SpaceTimeDerivAlgebraℂ.repLorentzGroup Λ a ⊗ₜ[ℂ] (φ ∘ₗ M.repLorentz Λ⁻¹)
```

## B. The jet derivative

**`JetComponentSpace.jetDeriv`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L153).

> the derivative of components in the jet component space,
> in the direction `μ`: the shift `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the derivative label,
> and likewise on the conjugate components.
>
> This is right multiplication by the degree-one element `∂_μ` on the
> `SpaceTimeDerivAlgebraℂ` factor, leaving the target index untouched. It uses a basis of
> the Lorentz covectors — that is what the index `μ` is — but no basis of `V`.

```lean
noncomputable def JetComponentSpace.jetDeriv (μ : Fin 1 ⊕ Fin 3) :
    JetComponentSpace M →ₗ[ℂ] JetComponentSpace M
```

**`JetComponentSpace.jetDeriv_fst_tmul`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L164).

```lean
lemma JetComponentSpace.jetDeriv_fst_tmul (μ : Fin 1 ⊕ Fin 3)
    (a : SpaceTimeDerivAlgebraℂ) (φ : Module.Dual ℂ M.V)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V)) :
    (JetComponentSpace.jetDeriv μ (a ⊗ₜ[ℂ] φ, y)).1
      = (a * SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) ⊗ₜ[ℂ] φ
```

**`JetComponentSpace.jetDeriv_snd_tmul`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L171).

```lean
lemma JetComponentSpace.jetDeriv_snd_tmul (μ : Fin 1 ⊕ Fin 3)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ M.V)
    (a : SpaceTimeDerivAlgebraℂ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    (JetComponentSpace.jetDeriv μ (x, a ⊗ₜ[ℂ] φ)).2
      = (a * SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) ⊗ₜ[ℂ] φ
```

**`JetComponentSpace.jetDeriv_comm`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L179).

> **Total derivatives commute.** Mixed partials agree because the derivative labels
> live in a *symmetric* algebra; no basis of `V` is involved.

```lean
lemma JetComponentSpace.jetDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (JetComponentSpace.jetDeriv (M := M) μ).comp (JetComponentSpace.jetDeriv ν)
      = (JetComponentSpace.jetDeriv (M := M) ν).comp (JetComponentSpace.jetDeriv μ)
```

**`JetComponentSpace.jetDeriv_eq_ι`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L193).

> The element being multiplied in is the degree-one derivative symbol `∂_μ`, the image
> of the dual basis covector under `SymmetricAlgebra.ι`.

```lean
lemma JetComponentSpace.jetDeriv_eq_ι (μ : Fin 1 ⊕ Fin 3) :
    JetComponentSpace.jetDeriv (M := M) μ
      = LinearMap.prodMap
        (TensorProduct.map
          (LinearMap.mulRight ℂ (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
            (Lorentz.ComplexCoVector.basis.dualBasis μ))) LinearMap.id)
        (TensorProduct.map
          (LinearMap.mulRight ℂ (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
            (Lorentz.ComplexCoVector.basis.dualBasis μ))) LinearMap.id)
```

**`JetComponentSpace.jetDeriv_fst`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L205).

```lean
lemma JetComponentSpace.jetDeriv_fst (μ : Fin 1 ⊕ Fin 3) (v : JetComponentSpace M) :
    (JetComponentSpace.jetDeriv μ v).1
      = TensorProduct.map
        (LinearMap.mulRight ℂ (SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))))
        LinearMap.id v.1
```

**`JetComponentSpace.jetDeriv_snd`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L212).

```lean
lemma JetComponentSpace.jetDeriv_snd (μ : Fin 1 ⊕ Fin 3) (v : JetComponentSpace M) :
    (JetComponentSpace.jetDeriv μ v).2
      = TensorProduct.map
        (LinearMap.mulRight ℂ (SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))))
        LinearMap.id v.2
```

## C. Lorentz covariance of the jet derivative

**`JetComponentSpace.repLorentzGroup_jetDeriv`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L265).

> **The jet derivative is a Lorentz vector on the component space.** Appending `∂_μ` and
> then acting is acting and then appending the transformed `∂_μ`, which is a combination of
> the `∂_a`. Both halves of the component space are covered by the same argument: the
> derivative label lives in the first tensor factor, and what sits in the second factor —
> `M.repLorentz.dual` or `M.repLorentz.conj.dual` — plays no role.

```lean
lemma JetComponentSpace.repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (v : JetComponentSpace M) :
    JetComponentSpace.repLorentzGroup M Λ (JetComponentSpace.jetDeriv μ v) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        JetComponentSpace.jetDeriv a (JetComponentSpace.repLorentzGroup M Λ v)
```

## D. Functoriality in the target space

**`JetComponentSpace.comap`**, a def, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L291).

> **The component space is contravariant in the target space.** A linear map `f : M.V →ₗ N.V`
> of target spaces pulls the component functions of the field `N` back to component
> functions of the field `M`: a component function is a *covector* on the target, so it
> transposes. The derivative label is untouched, and the conjugate half transposes the
> conjugate of `f`.

```lean
noncomputable def JetComponentSpace.comap (f : M.V →ₗ[ℂ] N.V) :
    JetComponentSpace N →ₗ[ℂ] JetComponentSpace M
```

**`JetComponentSpace.comap_fst_tmul`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L298).

```lean
lemma JetComponentSpace.comap_fst_tmul (f : M.V →ₗ[ℂ] N.V) (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ N.V) (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule N.V)) :
    (JetComponentSpace.comap f (a ⊗ₜ[ℂ] φ, y)).1 = a ⊗ₜ[ℂ] (φ ∘ₗ f)
```

**`JetComponentSpace.comap_snd_tmul`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L303).

```lean
lemma JetComponentSpace.comap_snd_tmul (f : M.V →ₗ[ℂ] N.V)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ N.V) (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ (ConjModule N.V)) :
    (JetComponentSpace.comap f (x, a ⊗ₜ[ℂ] φ)).2 = a ⊗ₜ[ℂ] (φ ∘ₗ ConjModule.map f)
```

**`JetComponentSpace.comap_id`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L309).

```lean
lemma JetComponentSpace.comap_id :
    JetComponentSpace.comap (LinearMap.id : M.V →ₗ[ℂ] M.V) = LinearMap.id
```

**`JetComponentSpace.comap_comp`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L320).

> Functoriality: pulling back along `g ∘ f` is pulling back along `g` and then along `f`.
> The order reverses, as it must for a contravariant construction.

```lean
lemma JetComponentSpace.comap_comp {P : MatterField jets}
    (f : M.V →ₗ[ℂ] N.V) (g : N.V →ₗ[ℂ] P.V) :
    JetComponentSpace.comap (g.comp f)
      = (JetComponentSpace.comap f).comp (JetComponentSpace.comap g)
```

**`JetComponentSpace.comapEquiv`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L334).

> A relabelling of the target space relabels the component functions. An isomorphism
> `e : M.V ≃ₗ N.V` of target spaces identifies the two component spaces, contravariantly: the
> component functions of the field `N` become those of the field `M`. This is
> `comap` upgraded to an equivalence, the two directions being mutually inverse by
> functoriality.

```lean
noncomputable def JetComponentSpace.comapEquiv (e : M.V ≃ₗ[ℂ] N.V) :
    JetComponentSpace N ≃ₗ[ℂ] JetComponentSpace M
```

**`JetComponentSpace.comapEquiv_apply`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L346).

```lean
lemma JetComponentSpace.comapEquiv_apply (e : M.V ≃ₗ[ℂ] N.V) (x : JetComponentSpace N) :
    JetComponentSpace.comapEquiv e x = JetComponentSpace.comap e.toLinearMap x
```

**`JetComponentSpace.comap_comp_repLorentzGroup`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L354).

> **An equivariant map of target spaces gives an equivariant pullback.** If `f : M.V →ₗ N.V`
> intertwines the two Lorentz representations then `comap f` intertwines the induced actions on
> the component spaces, in the opposite direction. Component functions are covectors, so
> the unconjugated half transposes `f` against the contragredient action and the conjugate
> half against its conjugate; both reduce to equivariance of `f` at `Λ⁻¹`.

```lean
lemma JetComponentSpace.comap_comp_repLorentzGroup (f : M.V →ₗ[ℂ] N.V)
    (hf : ∀ Λ : SL(2,ℂ), f.comp (M.repLorentz Λ) = (N.repLorentz Λ).comp f)
    (Λ : SL(2,ℂ)) :
    (JetComponentSpace.comap f).comp (JetComponentSpace.repLorentzGroup N Λ)
      = (JetComponentSpace.repLorentzGroup M Λ).comp (JetComponentSpace.comap f)
```

**`JetComponentSpace.comap_jetDeriv`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L390).

> **The pullback commutes with the jet derivative.** The two act on different tensor
> factors — the derivative label and the target index — so an inclusion of species is a map
> of differential algebras.

```lean
lemma JetComponentSpace.comap_jetDeriv (f : M.V →ₗ[ℂ] N.V) (μ : Fin 1 ⊕ Fin 3) :
    (JetComponentSpace.comap f).comp (JetComponentSpace.jetDeriv μ)
      = (JetComponentSpace.jetDeriv μ).comp (JetComponentSpace.comap f)
```

## E. The mass-weight scaling

> The mass dimension is tracked multiplicatively, through a scaling action: for a field of
> *mass weight* `w` — twice the mass dimension, kept integral so that fermions of dimension
> `3/2` carry weight `3` — the generator `∂_s φ_α` scales by `c ^ (w + 2 |s|)`, one factor
> of `c ^ 2` per derivative. The scaling on the component space below lifts functorially to
> the bosonic and fermionic algebras, where it defines their mass-dimension grading.

**`JetComponentSpace.massWeightScale`**, a def, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L414).

> The mass-weight scaling on the jet component space of a field of mass weight `w`
> (twice the mass dimension): the generator `∂_s φ_α` and its conjugate are scaled by
> `c ^ (w + 2 |s|)`, through the derivative-degree scaling `SpaceTimeDerivAlgebraℂ.gradeScale`
> on the derivative label.

```lean
noncomputable def JetComponentSpace.massWeightScale (w : ℕ) (c : ℂ) :
    JetComponentSpace M →ₗ[ℂ] JetComponentSpace M
```

**`JetComponentSpace.massWeightScale_fst_basis_tmul`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L422).

> On an unconjugated component function `∂_s φ_α` the mass-weight scaling is
> multiplication by `c ^ (w + 2 |s|)`.

```lean
lemma JetComponentSpace.massWeightScale_fst_basis_tmul (w : ℕ) (c : ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ M.V)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V)) :
    (JetComponentSpace.massWeightScale w c
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, y) : JetComponentSpace M)).1
      = c ^ (w + 2 * Multiset.card s) • (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

**`JetComponentSpace.massWeightScale_fst`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L434).

```lean
lemma JetComponentSpace.massWeightScale_fst (w : ℕ) (c : ℂ) (v : JetComponentSpace M) :
    (JetComponentSpace.massWeightScale w c v).1
      = c ^ w • TensorProduct.map
          (SpaceTimeDerivAlgebraℂ.gradeScale (c ^ 2)).toLinearMap LinearMap.id v.1
```

**`JetComponentSpace.massWeightScale_snd`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L440).

```lean
lemma JetComponentSpace.massWeightScale_snd (w : ℕ) (c : ℂ) (v : JetComponentSpace M) :
    (JetComponentSpace.massWeightScale w c v).2
      = c ^ w • TensorProduct.map
          (SpaceTimeDerivAlgebraℂ.gradeScale (c ^ 2)).toLinearMap LinearMap.id v.2
```

**`JetComponentSpace.massWeightScale_jetDeriv`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L466).

> **The total derivative carries mass weight two** on the component space: the scaling
> intertwines the derivative shift up to a factor `c ^ 2`.

```lean
lemma JetComponentSpace.massWeightScale_jetDeriv (w : ℕ) (c : ℂ) (μ : Fin 1 ⊕ Fin 3) :
    (JetComponentSpace.massWeightScale (M := M) w c).comp (JetComponentSpace.jetDeriv μ)
      = c ^ 2 • (JetComponentSpace.jetDeriv μ).comp
          (JetComponentSpace.massWeightScale w c)
```

**`JetComponentSpace.comap_comp_massWeightScale`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L490).

> **The mass-weight scaling is natural in the target space.** It commutes with every
> pullback, acting as it does on the derivative label and not on the target index. So the
> scaling cannot see which part of a target space a component function came from: in
> `JetComponentSpace (∀ i, V i)`, where a species enters through
> `comap (LinearMap.proj i)`, every species is scaled by the same weight. This is why the
> generator space of a multi-species theory, `GaugeFieldData.FermionGenerators`, records
> the weights on a direct sum, one per species, rather than on a single component space of
> the product.

```lean
lemma JetComponentSpace.comap_comp_massWeightScale (f : M.V →ₗ[ℂ] N.V) (w : ℕ) (c : ℂ) :
    (JetComponentSpace.comap f).comp (JetComponentSpace.massWeightScale w c)
      = (JetComponentSpace.massWeightScale w c).comp (JetComponentSpace.comap f)
```

## F. The dual and the conjugate of a finite product

> The component space of a direct sum of matter fields splits, and both halves split for the
> same two reasons: the dual of a finite product is the product of the duals, and conjugation
> commutes with products. Neither statement mentions a matter field, so both are recorded
> here, on a bare family of modules; the splitting they add up to is
> `MatterField.jetComponentSpacePiEquiv`, downstream where `MatterField.pi` is available. The
> index type must be finite — the dual of an infinite product is strictly larger than the
> product of the duals, and `TensorProduct.piRight` is an equivalence only in the finite case.

**`prodPiEquiv`**, a def, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L520).

> A pair of families is the same thing as a family of pairs. This is the last step of
> the splitting of a component space over a product of target spaces: the two halves split
> separately into families, and this puts the two families back together index by index.
> Everything is the identity on underlying data, so every law is `rfl`.

```lean
def prodPiEquiv {A B : ι → Type*} [∀ i, AddCommGroup (A i)] [∀ i, Module ℂ (A i)]
    [∀ i, AddCommGroup (B i)] [∀ i, Module ℂ (B i)] :
    ((∀ i, A i) × (∀ i, B i)) ≃ₗ[ℂ] ∀ i, (A i × B i)
```

**`JetComponentSpace.fstPiEquiv`**, a def, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L534).

> **The unconjugated half of the component space of a finite direct sum splits.** The
> symbols `∂_s ψ_α` of a `(∀ i, E i)`-valued field are the families, over the index, of
> the symbols of the summands: the dual distributes over the finite product and the
> derivative label is untouched.

```lean
noncomputable def JetComponentSpace.fstPiEquiv :
    (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (∀ i, E i))
      ≃ₗ[ℂ] ∀ i, SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (E i)
```

**`JetComponentSpace.fstPiEquiv_tmul`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L545).

> On a pure symbol the splitting restricts the target index to one summand: the
> component `∂_s ψ_α` of the direct sum in the summand `i` is `∂_s` of the covector `φ`
> precomposed with the inclusion of that summand.

```lean
lemma JetComponentSpace.fstPiEquiv_tmul (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ (∀ i, E i)) (i : ι) :
    fstPiEquiv E (a ⊗ₜ[ℂ] φ) i = a ⊗ₜ[ℂ] (φ ∘ₗ LinearMap.single ℂ E i)
```

**`JetComponentSpace.sndPiEquiv`**, a def, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L552).

> **The conjugate half of the component space of a finite direct sum splits**, by the
> same argument applied to the conjugate modules, using that conjugation commutes with
> products.

```lean
noncomputable def JetComponentSpace.sndPiEquiv :
    (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (∀ i, E i)))
      ≃ₗ[ℂ] ∀ i, SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (E i))
```

**`JetComponentSpace.sndPiEquiv_tmul`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L563).

> On a pure conjugate symbol the splitting again restricts the target index to one
> summand, the inclusion being read through the conjugation.

```lean
lemma JetComponentSpace.sndPiEquiv_tmul (a : SpaceTimeDerivAlgebraℂ)
    (ψ : Module.Dual ℂ (ConjModule (∀ i, E i))) (i : ι) :
    sndPiEquiv E (a ⊗ₜ[ℂ] ψ) i
      = a ⊗ₜ[ℂ] (ψ ∘ₗ ConjModule.map (k := ℂ) (LinearMap.single ℂ E i))
```

**`JetComponentSpace.fstPiEquiv_symm_single`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L571).

> The splitting sends the family supported on one summand back to the pullback along
> the projection onto that summand: a component function of the summand `i`, read as a
> component function of the whole, is `φ ∘ proj i`.

```lean
lemma JetComponentSpace.fstPiEquiv_symm_single (i : ι)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (E i)) :
    (fstPiEquiv E).symm (Pi.single i z)
      = TensorProduct.map LinearMap.id (Module.Dual.transpose (LinearMap.proj i)) z
```

**`JetComponentSpace.sndPiEquiv_symm_single`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean#L594).

> The conjugate half of the splitting behaves in the same way, the projection read
> through the conjugation.

```lean
lemma JetComponentSpace.sndPiEquiv_symm_single (i : ι)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (E i))) :
    (sndPiEquiv E).symm (Pi.single i z)
      = TensorProduct.map LinearMap.id
          (Module.Dual.transpose (ConjModule.map (k := ℂ) (LinearMap.proj i))) z
```

## Depends on

- [Matter fields of a gauge theory](matterfield-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/Basic.lean)
