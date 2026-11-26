---
declaration: module
origin: cited
lean: FieldDerivSpace, FieldDerivSpace.repLorentzGroup, FieldDerivSpace.repLorentzGroup_fst, FieldDerivSpace.repLorentzGroup_snd, FieldDerivSpace.jetDeriv, FieldDerivSpace.jetDeriv_fst_tmul, FieldDerivSpace.jetDeriv_snd_tmul, FieldDerivSpace.jetDeriv_comm
statement: formalized
proof: formalized
---

# The field-derivative space of a matter field

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.FieldDerivSpace.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean): 33 declarations, 21 with a docstring; 2 private, not shown.

> The span of the derivative symbols of a matter field and their conjugates, with its Lorentz
> action, jet derivative and mass-weight scaling.

## i. Overview

> For a matter field valued in a complex vector space `V`, the field-derivative space is the span
> of the derivative symbols `∂_s ψ_α` and their conjugates `∂_s ψ̄_α`, the local coordinate
> functions on the space of jets of the field. This file defines that space and the structure on
> it that does not involve a gauge group. This is the Lorentz action, the jet derivative,
> functoriality in `V` and the mass-weight scaling. The action of the gauge group is in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.FieldDerivSpace.GaugeAction`.

## ii. Key results

> - `FieldDerivSpace` : the space of component functions of the matter field `M`, the span of the
>   symbols `∂_s ψ_α` and their conjugates `∂_s ψ̄_α`, where `α` runs over the target space `M.V`
> - `FieldDerivSpace.repLorentzGroup` : the Lorentz action on the field-derivative space
> - `FieldDerivSpace.jetDeriv` : the derivative of components in the field-derivative space, in the
>   direction `μ`, the shift `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the derivative label, and likewise on the
>   conjugate components
> - `FieldDerivSpace.jetDeriv_comm` : total derivatives commute
> - `FieldDerivSpace.repLorentzGroup_jetDeriv` : the jet derivative is a Lorentz vector on the
>   component space
> - `FieldDerivSpace.comap` : the component space is contravariant in the target space
> - `FieldDerivSpace.comapEquiv` : a relabelling of the target space relabels the component
>   functions
> - `FieldDerivSpace.massWeightScale` : the mass-weight scaling on the field-derivative space of a
>   field of mass weight `w` (twice the mass dimension), scaling the generator `∂_s φ_α` and its
>   conjugate by `c ^ (w + 2 |s|)`, through the derivative-degree scaling
>   `SpaceTimeDerivAlgebraℂ.gradeScale` on the derivative label
> - `FieldDerivSpace.comap_comp_massWeightScale` : the mass-weight scaling is natural in the target
>   space
> - `FieldDerivSpace.fstPiEquiv` : the unconjugated half of the component space of a finite direct
>   sum splits
> - `FieldDerivSpace.sndPiEquiv` : the conjugate half of the component space of a finite direct sum
>   splits, by the same argument applied to the conjugate modules, using that conjugation commutes
>   with products

## iv. References

> * None.

**`FieldDerivSpace`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L83).

> The space of component functions of the matter field `M`, the span of the symbols
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
abbrev FieldDerivSpace (M : G.MatterField) : Type
```

## A. The Lorentz action on the component space

**`FieldDerivSpace.repLorentzGroup`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L103).

> The Lorentz action on the field-derivative space. Under a Lorentz transformation a
> matter field transforms as `ψ(x) ↦ ρ(Λ) ψ(Λ⁻¹ x)`, so a derivative symbol `∂_s ψ_α` is
> acted on in both of its labels, the derivative multiset `s` by the Lorentz action on
> covectors, extended to `SpaceTimeDerivAlgebraℂ`, and the target index `α` by the
> contragredient of `ρ`.
>
> Unlike the gauge action, this needs no fibrewise-linearity or finite-dimensionality
> hypothesis. The two labels transform independently, so the action is simply a tensor
> product of representations. The conjugate half is the same with `ρ` replaced by its
> conjugate, the symbols `∂_s ψ̄_α` transforming by `star` of the spinor matrix.

```lean
noncomputable def FieldDerivSpace.repLorentzGroup (M : G.MatterField) :
    Representation ℂ SL(2,ℂ) (FieldDerivSpace M)
```

**`FieldDerivSpace.repLorentzGroup_fst`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L109).

```lean
lemma FieldDerivSpace.repLorentzGroup_fst (Λ : SL(2,ℂ)) (x : FieldDerivSpace M) :
    (FieldDerivSpace.repLorentzGroup M Λ x).1
      = (SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod M.repLorentz.dual) Λ x.1
```

**`FieldDerivSpace.repLorentzGroup_snd`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L114).

```lean
lemma FieldDerivSpace.repLorentzGroup_snd (Λ : SL(2,ℂ)) (x : FieldDerivSpace M) :
    (FieldDerivSpace.repLorentzGroup M Λ x).2
      = (SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod M.repLorentz.conj.dual) Λ x.2
```

## B. The jet derivative

**`FieldDerivSpace.jetDeriv`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L131).

> The derivative of components in the field-derivative space,
> in the direction `μ`, the shift `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the derivative label,
> and likewise on the conjugate components.
>
> This is right multiplication by the degree-one element `∂_μ` on the
> `SpaceTimeDerivAlgebraℂ` factor, leaving the target index untouched. It uses a basis of
> the Lorentz covectors — that is what the index `μ` is — but no basis of `V`.

```lean
noncomputable def FieldDerivSpace.jetDeriv (μ : Fin 1 ⊕ Fin 3) :
    FieldDerivSpace M →ₗ[ℂ] FieldDerivSpace M
```

**`FieldDerivSpace.jetDeriv_fst_tmul`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L142).

```lean
lemma FieldDerivSpace.jetDeriv_fst_tmul (μ : Fin 1 ⊕ Fin 3)
    (a : SpaceTimeDerivAlgebraℂ) (φ : Module.Dual ℂ M.V)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V)) :
    (FieldDerivSpace.jetDeriv μ (a ⊗ₜ[ℂ] φ, y)).1
      = (a * SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) ⊗ₜ[ℂ] φ
```

**`FieldDerivSpace.jetDeriv_snd_tmul`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L149).

```lean
lemma FieldDerivSpace.jetDeriv_snd_tmul (μ : Fin 1 ⊕ Fin 3)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ M.V)
    (a : SpaceTimeDerivAlgebraℂ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    (FieldDerivSpace.jetDeriv μ (x, a ⊗ₜ[ℂ] φ)).2
      = (a * SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) ⊗ₜ[ℂ] φ
```

**`FieldDerivSpace.jetDeriv_comm`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L157).

> Total derivatives commute. Mixed partials agree because the derivative labels
> live in a *symmetric* algebra; no basis of `V` is involved.

```lean
lemma FieldDerivSpace.jetDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (FieldDerivSpace.jetDeriv (M := M) μ).comp (FieldDerivSpace.jetDeriv ν)
      = (FieldDerivSpace.jetDeriv (M := M) ν).comp (FieldDerivSpace.jetDeriv μ)
```

**`FieldDerivSpace.jetDeriv_fst`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L170).

```lean
lemma FieldDerivSpace.jetDeriv_fst (μ : Fin 1 ⊕ Fin 3) (v : FieldDerivSpace M) :
    (FieldDerivSpace.jetDeriv μ v).1
      = TensorProduct.map
        (LinearMap.mulRight ℂ (SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))))
        LinearMap.id v.1
```

**`FieldDerivSpace.jetDeriv_snd`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L177).

```lean
lemma FieldDerivSpace.jetDeriv_snd (μ : Fin 1 ⊕ Fin 3) (v : FieldDerivSpace M) :
    (FieldDerivSpace.jetDeriv μ v).2
      = TensorProduct.map
        (LinearMap.mulRight ℂ (SpaceTimeDerivAlgebraℂ.basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))))
        LinearMap.id v.2
```

## C. Lorentz covariance of the jet derivative

**`FieldDerivSpace.repLorentzGroup_jetDeriv`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L230).

> The jet derivative is a Lorentz vector on the component space. Appending `∂_μ` and
> then acting is acting and then appending the transformed `∂_μ`, which is a combination of
> the `∂_a`. Both halves of the component space are covered by the same argument. The
> derivative label lives in the first tensor factor, and what sits in the second factor —
> `M.repLorentz.dual` or `M.repLorentz.conj.dual` — plays no role.

```lean
lemma FieldDerivSpace.repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (v : FieldDerivSpace M) :
    FieldDerivSpace.repLorentzGroup M Λ (FieldDerivSpace.jetDeriv μ v) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        FieldDerivSpace.jetDeriv a (FieldDerivSpace.repLorentzGroup M Λ v)
```

## D. Functoriality in the target space

**`FieldDerivSpace.comap`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L256).

> The component space is contravariant in the target space. A linear map `f : M.V →ₗ N.V`
> of target spaces pulls the component functions of the field `N` back to component
> functions of the field `M`. A component function is a covector on the target, so it
> transposes. The derivative label is untouched, and the conjugate half transposes the
> conjugate of `f`.

```lean
noncomputable def FieldDerivSpace.comap (f : M.V →ₗ[ℂ] N.V) :
    FieldDerivSpace N →ₗ[ℂ] FieldDerivSpace M
```

**`FieldDerivSpace.comap_fst_tmul`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L263).

```lean
lemma FieldDerivSpace.comap_fst_tmul (f : M.V →ₗ[ℂ] N.V) (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ N.V) (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule N.V)) :
    (FieldDerivSpace.comap f (a ⊗ₜ[ℂ] φ, y)).1 = a ⊗ₜ[ℂ] (φ ∘ₗ f)
```

**`FieldDerivSpace.comap_snd_tmul`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L268).

```lean
lemma FieldDerivSpace.comap_snd_tmul (f : M.V →ₗ[ℂ] N.V)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ N.V) (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ (ConjModule N.V)) :
    (FieldDerivSpace.comap f (x, a ⊗ₜ[ℂ] φ)).2 = a ⊗ₜ[ℂ] (φ ∘ₗ ConjModule.map f)
```

**`FieldDerivSpace.comap_id`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L274).

```lean
lemma FieldDerivSpace.comap_id :
    FieldDerivSpace.comap (LinearMap.id : M.V →ₗ[ℂ] M.V) = LinearMap.id
```

**`FieldDerivSpace.comap_comp`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L285).

> Functoriality. Pulling back along `g ∘ f` is pulling back along `g` and then along `f`.
> The order reverses, as it must for a contravariant construction.

```lean
lemma FieldDerivSpace.comap_comp {P : G.MatterField}
    (f : M.V →ₗ[ℂ] N.V) (g : N.V →ₗ[ℂ] P.V) :
    FieldDerivSpace.comap (g.comp f)
      = (FieldDerivSpace.comap f).comp (FieldDerivSpace.comap g)
```

**`FieldDerivSpace.comapEquiv`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L299).

> A relabelling of the target space relabels the component functions. An isomorphism
> `e : M.V ≃ₗ N.V` of target spaces identifies the two component spaces, contravariantly, so the
> component functions of the field `N` become those of the field `M`. This is
> `comap` upgraded to an equivalence, the two directions being mutually inverse by
> functoriality.

```lean
noncomputable def FieldDerivSpace.comapEquiv (e : M.V ≃ₗ[ℂ] N.V) :
    FieldDerivSpace N ≃ₗ[ℂ] FieldDerivSpace M
```

**`FieldDerivSpace.comapEquiv_apply`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L311).

```lean
lemma FieldDerivSpace.comapEquiv_apply (e : M.V ≃ₗ[ℂ] N.V) (x : FieldDerivSpace N) :
    FieldDerivSpace.comapEquiv e x = FieldDerivSpace.comap e.toLinearMap x
```

**`FieldDerivSpace.comap_comp_repLorentzGroup`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L319).

> An equivariant map of target spaces gives an equivariant pullback. If `f : M.V →ₗ N.V`
> intertwines the two Lorentz representations then `comap f` intertwines the induced actions on
> the component spaces, in the opposite direction. Component functions are covectors, so
> the unconjugated half transposes `f` against the contragredient action and the conjugate
> half against its conjugate; both reduce to equivariance of `f` at `Λ⁻¹`.

```lean
lemma FieldDerivSpace.comap_comp_repLorentzGroup (f : M.V →ₗ[ℂ] N.V)
    (hf : ∀ Λ : SL(2,ℂ), f.comp (M.repLorentz Λ) = (N.repLorentz Λ).comp f)
    (Λ : SL(2,ℂ)) :
    (FieldDerivSpace.comap f).comp (FieldDerivSpace.repLorentzGroup N Λ)
      = (FieldDerivSpace.repLorentzGroup M Λ).comp (FieldDerivSpace.comap f)
```

**`FieldDerivSpace.comap_jetDeriv`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L355).

> The pullback commutes with the jet derivative. The two act on different tensor
> factors — the derivative label and the target index — so an inclusion of species is a map
> of differential algebras.

```lean
lemma FieldDerivSpace.comap_jetDeriv (f : M.V →ₗ[ℂ] N.V) (μ : Fin 1 ⊕ Fin 3) :
    (FieldDerivSpace.comap f).comp (FieldDerivSpace.jetDeriv μ)
      = (FieldDerivSpace.jetDeriv μ).comp (FieldDerivSpace.comap f)
```

## E. The mass-weight scaling

> The mass dimension is tracked multiplicatively, through a scaling action: for a field of
> *mass weight* `w` — twice the mass dimension, kept integral so that fermions of dimension
> `3/2` carry weight `3` — the generator `∂_s φ_α` scales by `c ^ (w + 2 |s|)`, one factor
> of `c ^ 2` per derivative. The scaling on the component space below lifts functorially to
> the bosonic and fermionic algebras, where it defines their mass-dimension grading.

**`FieldDerivSpace.massWeightScale`**, a def, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L379).

> The mass-weight scaling on the field-derivative space of a field of mass weight `w`
> (twice the mass dimension). The generator `∂_s φ_α` and its conjugate are scaled by
> `c ^ (w + 2 |s|)`, through the derivative-degree scaling `SpaceTimeDerivAlgebraℂ.gradeScale`
> on the derivative label.

```lean
noncomputable def FieldDerivSpace.massWeightScale (w : ℕ) (c : ℂ) :
    FieldDerivSpace M →ₗ[ℂ] FieldDerivSpace M
```

**`FieldDerivSpace.massWeightScale_fst_basis_tmul`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L387).

> On an unconjugated component function `∂_s φ_α` the mass-weight scaling is
> multiplication by `c ^ (w + 2 |s|)`.

```lean
lemma FieldDerivSpace.massWeightScale_fst_basis_tmul (w : ℕ) (c : ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ M.V)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V)) :
    (FieldDerivSpace.massWeightScale w c
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, y) : FieldDerivSpace M)).1
      = c ^ (w + 2 * Multiset.card s) • (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

**`FieldDerivSpace.massWeightScale_fst`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L399).

```lean
lemma FieldDerivSpace.massWeightScale_fst (w : ℕ) (c : ℂ) (v : FieldDerivSpace M) :
    (FieldDerivSpace.massWeightScale w c v).1
      = c ^ w • TensorProduct.map
          (SpaceTimeDerivAlgebraℂ.gradeScale (c ^ 2)).toLinearMap LinearMap.id v.1
```

**`FieldDerivSpace.massWeightScale_snd`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L405).

```lean
lemma FieldDerivSpace.massWeightScale_snd (w : ℕ) (c : ℂ) (v : FieldDerivSpace M) :
    (FieldDerivSpace.massWeightScale w c v).2
      = c ^ w • TensorProduct.map
          (SpaceTimeDerivAlgebraℂ.gradeScale (c ^ 2)).toLinearMap LinearMap.id v.2
```

**`FieldDerivSpace.massWeightScale_jetDeriv`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L431).

> The total derivative carries mass weight two on the component space. The scaling
> intertwines the derivative shift up to a factor `c ^ 2`.

```lean
lemma FieldDerivSpace.massWeightScale_jetDeriv (w : ℕ) (c : ℂ) (μ : Fin 1 ⊕ Fin 3) :
    (FieldDerivSpace.massWeightScale (M := M) w c).comp (FieldDerivSpace.jetDeriv μ)
      = c ^ 2 • (FieldDerivSpace.jetDeriv μ).comp
          (FieldDerivSpace.massWeightScale w c)
```

**`FieldDerivSpace.comap_comp_massWeightScale`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L455).

> The mass-weight scaling is natural in the target space. It commutes with every
> pullback, acting as it does on the derivative label and not on the target index. So the
> scaling cannot see which part of a target space a component function came from. In
> `FieldDerivSpace (∀ i, V i)`, where a species enters through
> `comap (LinearMap.proj i)`, every species is scaled by the same weight. This is why the
> generator space of a multi-species theory, `GaugeFieldData.FermionGenerators`, records
> the weights on a direct sum, one per species, rather than on a single component space of
> the product.

```lean
lemma FieldDerivSpace.comap_comp_massWeightScale (f : M.V →ₗ[ℂ] N.V) (w : ℕ) (c : ℂ) :
    (FieldDerivSpace.comap f).comp (FieldDerivSpace.massWeightScale w c)
      = (FieldDerivSpace.massWeightScale w c).comp (FieldDerivSpace.comap f)
```

## F. The dual and the conjugate of a finite product

> The component space of a direct sum of matter fields splits, and both halves split for the same two
> reasons: the dual of a finite product is the product of the duals, and conjugation commutes with
> products. Neither statement mentions a matter field, so both are recorded here, on a bare family of
> modules; the splitting they add up to is
> `GlobalGaugeGroup.MatterField.fieldDerivSpacePiEquiv`, downstream where
> `GlobalGaugeGroup.MatterField.pi` is available. The index type must be finite — the dual of an
> infinite product is strictly larger than the product of the duals, and `TensorProduct.piRight` is an
> equivalence only in the finite case.

**`prodPiEquiv`**, a def, [line 486](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L486).

> A pair of families is the same thing as a family of pairs. This is the last step of
> the splitting of a component space over a product of target spaces. The two halves split
> separately into families, and this puts the two families back together index by index.
> Everything is the identity on underlying data, so every law is `rfl`.

```lean
def prodPiEquiv {A B : ι → Type*} [∀ i, AddCommGroup (A i)] [∀ i, Module ℂ (A i)]
    [∀ i, AddCommGroup (B i)] [∀ i, Module ℂ (B i)] :
    ((∀ i, A i) × (∀ i, B i)) ≃ₗ[ℂ] ∀ i, (A i × B i)
```

**`FieldDerivSpace.fstPiEquiv`**, a def, [line 500](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L500).

> The unconjugated half of the component space of a finite direct sum splits. The
> symbols `∂_s ψ_α` of a `(∀ i, E i)`-valued field are the families, over the index, of
> the symbols of the summands, since the dual distributes over the finite product and the
> derivative label is untouched.

```lean
noncomputable def FieldDerivSpace.fstPiEquiv :
    (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (∀ i, E i))
      ≃ₗ[ℂ] ∀ i, SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (E i)
```

**`FieldDerivSpace.fstPiEquiv_tmul`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L511).

> On a pure symbol the splitting restricts the target index to one summand. The
> component `∂_s ψ_α` of the direct sum in the summand `i` is `∂_s` of the covector `φ`
> precomposed with the inclusion of that summand.

```lean
lemma FieldDerivSpace.fstPiEquiv_tmul (a : SpaceTimeDerivAlgebraℂ)
    (φ : Module.Dual ℂ (∀ i, E i)) (i : ι) :
    fstPiEquiv E (a ⊗ₜ[ℂ] φ) i = a ⊗ₜ[ℂ] (φ ∘ₗ LinearMap.single ℂ E i)
```

**`FieldDerivSpace.sndPiEquiv`**, a def, [line 518](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L518).

> The conjugate half of the component space of a finite direct sum splits, by the
> same argument applied to the conjugate modules, using that conjugation commutes with
> products.

```lean
noncomputable def FieldDerivSpace.sndPiEquiv :
    (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (∀ i, E i)))
      ≃ₗ[ℂ] ∀ i, SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (E i))
```

**`FieldDerivSpace.sndPiEquiv_tmul`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L529).

> On a pure conjugate symbol the splitting again restricts the target index to one
> summand, the inclusion being read through the conjugation.

```lean
lemma FieldDerivSpace.sndPiEquiv_tmul (a : SpaceTimeDerivAlgebraℂ)
    (ψ : Module.Dual ℂ (ConjModule (∀ i, E i))) (i : ι) :
    sndPiEquiv E (a ⊗ₜ[ℂ] ψ) i
      = a ⊗ₜ[ℂ] (ψ ∘ₗ ConjModule.map (k := ℂ) (LinearMap.single ℂ E i))
```

**`FieldDerivSpace.fstPiEquiv_symm_single`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L537).

> The splitting sends the family supported on one summand back to the pullback along
> the projection onto that summand. A component function of the summand `i`, read as a
> component function of the whole, is `φ ∘ proj i`.

```lean
lemma FieldDerivSpace.fstPiEquiv_symm_single (i : ι)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (E i)) :
    (fstPiEquiv E).symm (Pi.single i z)
      = TensorProduct.map LinearMap.id (Module.Dual.transpose (LinearMap.proj i)) z
```

**`FieldDerivSpace.sndPiEquiv_symm_single`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean#L560).

> The conjugate half of the splitting behaves in the same way, the projection read
> through the conjugation.

```lean
lemma FieldDerivSpace.sndPiEquiv_symm_single (i : ι)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (E i))) :
    (sndPiEquiv E).symm (Pi.single i z)
      = TensorProduct.map LinearMap.id
          (Module.Dual.transpose (ConjModule.map (k := ℂ) (LinearMap.proj i))) z
```

## Depends on

- [Matter fields of a global gauge group](matterfield-basic.md)
- [Algebras, duals and representations on a conjugate module](../../../mathematics/part-02/modules/conjmodule.md)
- [Derivative algebras](../../../spaceandtime/spacetime/spacetimederivalgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/FieldDerivSpace/Basic.lean)
