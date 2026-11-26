---
declaration: module
origin: cited
lean: GlobalGaugeGroup.sum_derivConv_sum_fam, GlobalGaugeGroup.repLorentz_eq_lorentzMix, GlobalGaugeGroup.repLorentz_apply_mix, GlobalGaugeGroup.isLorentzDerivTransforms_mix, GlobalGaugeGroup.repLorentz_sum_derivConv, GlobalGaugeGroup.actionFam_apply_eq_sum, GlobalGaugeGroup.actionFamConv_eq_sum, GlobalGaugeGroup.actionFamConv_sum_fam
statement: formalized
proof: formalized
---

# The Lorentz law of the covariant derivatives of a matter family

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.LorentzCovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean): 16 declarations, 16 with a docstring.

> How the iterated covariant derivatives of a matter family transform under the Lorentz group.

## i. Overview

> The covariant derivative of a matter family adds one ordered derivative slot and the
> correction `A_ρ · F`, the derived action `actionFamConv` of the gauge field on the value
> index. Expanded in bases, the correction is a scalar combination of Leibniz convolutions of
> gauge-field symbols against matter symbols, which gives its Lorentz law and its linearity
> in the matter family. The contragredient twist `rep.dual Λ` of the value index passes
> through it when the infinitesimal gauge action commutes with the Lorentz action on the
> value space, the one hypothesis on the species. These are the inputs of the
> abstract induction `Lorentz.repLorentz_tower`, for any family of gauge-field symbols in a
> complex algebra `B` with the Lorentz law `GaugeBoson.LorentzTransformsAsGaugeField`, under a
> Lorentz action by multiplicative maps.

## ii. Key results

> - `GlobalGaugeGroup.repLorentz_covDerivIter` : the Lorentz law of the iterated
>   covariant derivative at every derivative multiset.
> - `GlobalGaugeGroup.isLorentzCovDerivTransforms_covDerivIter`, `..._conj` : the
>   covariant tower of a matter family, and of a conjugate family, transforms as the
>   covariant derivatives of a Lorentz-covariant field.

## iv. References

> * None.

## A. Families in the multiset form of the Lorentz law

**`GlobalGaugeGroup.sum_derivConv_sum_fam`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L75).

> A scalar combination of convolutions against the gauge field is linear in the
> right-hand families.

```lean
lemma sum_derivConv_sum_fam {ι κ ι' : Type} [Fintype ι] [Fintype κ] [Fintype ι']
    (f : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (coef : ι → κ → ℂ) (c : ι' → ℂ)
    (g : ι' → κ → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∑ j, ∑ k, coef j k • derivConv (f j) (fun y => ∑ i, c i • g i k y) s =
      ∑ i, c i • ∑ j, ∑ k, coef j k • derivConv (f j) (g i k) s
```

**`GlobalGaugeGroup.repLorentz_eq_lorentzMix`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L85).

> A Lorentz law in the tuple form, read on the underlying multisets. The transformed
> family mixes by `lorentzMix`.

```lean
lemma repLorentz_eq_lorentzMix (Λ : SL(2,ℂ)) (f g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (hfg : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)), repLorentz Λ (f (List.ofFn l)) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) • g (List.ofFn p))
    (x : Multiset (Fin 1 ⊕ Fin 3)) : repLorentz Λ (f x) = lorentzMix Λ g x 0
```

**`GlobalGaugeGroup.repLorentz_apply_mix`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L96).

> The Lorentz law of the gauge-field symbols, in the multiset form.

```lean
lemma repLorentz_apply_mix (Λ : SL(2,ℂ))
    (x : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (χ : Module.Dual ℝ G.lieSubalgebra) :
    repLorentz Λ (A x μ χ) = lorentzMix Λ (fun t => ∑ a, L[Λ] a μ • A t a χ) x 0
```

**`GlobalGaugeGroup.isLorentzDerivTransforms_mix`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L104).

> The Lorentz law of a family of derivative symbols, in the multiset form.

```lean
lemma isLorentzDerivTransforms_mix {rep : Representation ℂ SL(2,ℂ) V}
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : IsLorentzDerivTransforms repLorentz rep F) (Λ : SL(2,ℂ))
    (x : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V) :
    repLorentz Λ (F x χ) = lorentzMix Λ (fun t => F t (rep.dual Λ χ)) x 0
```

**`GlobalGaugeGroup.repLorentz_sum_derivConv`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L116).

> The Lorentz law of a scalar combination of convolutions against the gauge field. The
> direction of the gauge field mixes by its own column, the derivative slots by
> `lorentzMix`, and the right-hand families are replaced by their transforms.

```lean
lemma repLorentz_sum_derivConv (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    {ι κ : Type} [Fintype ι] [Fintype κ] (bg : Module.Basis ι ℝ G.lieSubalgebra) (coef : ι → κ → ℂ)
    (g g' : κ → Multiset (Fin 1 ⊕ Fin 3) → B)
    (hg : ∀ k y, repLorentz Λ (g k y) = lorentzMix Λ (g' k) y 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repLorentz Λ (∑ j, ∑ k, coef j k • derivConv (fun x => A x ρ (bg.coord j)) (g k) s) =
      ∑ a, L[Λ] a ρ • lorentzMix Λ
        (fun t => ∑ j, ∑ k, coef j k • derivConv (fun x => A x a (bg.coord j)) (g' k) t)
        s 0
```

## B. The derived action family in bases

**`GlobalGaugeGroup.actionFam_apply_eq_sum`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L144).

> The action of families expanded in bases of the gauge algebra and the value space.

```lean
lemma actionFam_apply_eq_sum {ι κ : Type} [Fintype ι] [Fintype κ]
    (bg : Module.Basis ι ℝ G.lieSubalgebra) (bv : Module.Basis κ ℂ V)
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B)
    (φ : Module.Dual ℂ V) :
    actionFam act f g φ =
      ∑ j, ∑ k, φ (act (bg j) (bv k)) • (f (bg.coord j) * g (bv.coord k))
```

**`GlobalGaugeGroup.actionFamConv_eq_sum`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L155).

> The derived action family expanded in bases.

```lean
lemma actionFamConv_eq_sum {ι κ : Type} [Fintype ι] [Fintype κ]
    (bg : Module.Basis ι ℝ G.lieSubalgebra) (bv : Module.Basis κ ℂ V)
    (ρ : Fin 1 ⊕ Fin 3) (Fm : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ Fm s φ = ∑ j, ∑ k, φ (act (bg j) (bv k)) •
      derivConv (fun x => A x ρ (bg.coord j)) (fun y => Fm y (bv.coord k)) s
```

**`GlobalGaugeGroup.actionFamConv_sum_fam`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L165).

> The derived action family is linear in the matter family.

```lean
lemma actionFamConv_sum_fam {ι : Type} [Fintype ι] (ρ : Fin 1 ⊕ Fin 3) (c : ι → ℂ)
    (H : ι → Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ (fun t => ∑ i, c i • H i t) s φ =
      ∑ i, c i • actionFamConv A act ρ (H i) s φ
```

**`GlobalGaugeGroup.repLorentz_actionFamConv`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L179).

> The Lorentz law of the derived action family. The derivative slots mix, the direction
> of the gauge field mixes by its own column, and the value index is carried by the
> transformed matter family.

```lean
lemma repLorentz_actionFamConv (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (Fm Fm' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hG : ∀ y χ, repLorentz Λ (Fm y χ) = lorentzMix Λ (fun t => Fm' t χ) y 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    repLorentz Λ (actionFamConv A act ρ Fm s φ) =
      ∑ a, L[Λ] a ρ • lorentzMix Λ (fun t => actionFamConv A act a Fm' t φ) s 0
```

**`GlobalGaugeGroup.dual_twist`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L195).

> The twist of the value index past the gauge action. An endomorphism commuting with
> the gauge action may be moved from the dual basis onto the dual vector.

```lean
lemma dual_twist {κ : Type} [Fintype κ] (bv : Module.Basis κ ℂ V) (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : G.lieSubalgebra) (v : V), act c (T v) = T (act c v))
    (ψ : Module.Dual ℂ V →ₗ[ℂ] B) (c : G.lieSubalgebra) (φ : Module.Dual ℂ V) :
    ∑ k, φ (act c (bv k)) • ψ (T.dualMap (bv.coord k)) =
      ∑ k, (T.dualMap φ) (act c (bv k)) • ψ (bv.coord k)
```

**`GlobalGaugeGroup.actionFam_comp_dual`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L209).

> The contragredient action may be pulled out of an action of families, provided the
> gauge action commutes with it on the value space.

```lean
lemma actionFam_comp_dual (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : G.lieSubalgebra) (v : V), act c (T v) = T (act c v))
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B)
    (φ : Module.Dual ℂ V) :
    actionFam act f (g ∘ₗ T.dualMap) φ = actionFam act f g (T.dualMap φ)
```

**`GlobalGaugeGroup.actionFamConv_comp_dual`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L219).

> The contragredient action may be pulled out of a derived action family.

```lean
lemma actionFamConv_comp_dual (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : G.lieSubalgebra) (v : V), act c (T v) = T (act c v)) (ρ : Fin 1 ⊕ Fin 3)
    (K : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ (fun t => K t ∘ₗ T.dualMap) s φ =
      actionFamConv A act ρ K s (T.dualMap φ)
```

## C. The Lorentz law of the covariant tower

**`GlobalGaugeGroup.repLorentz_covDerivIter`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L238).

> The Lorentz law of the iterated covariant derivative of a matter family. The ordered
> covariant slots mix by their own columns and the multiset of plain derivative slots
> mixes by `lorentzMix`, while the value index transforms contragrediently.

```lean
lemma repLorentz_covDerivIter {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : G.lieSubalgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep F) (Λ : SL(2,ℂ))
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    repLorentz Λ (covDerivIter A act F n l s φ) = ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
      (∏ i, L[Λ] (p i) (l i)) •
        lorentzMix Λ (fun t => covDerivIter A act F n p t (rep.dual Λ φ)) s 0
```

**`GlobalGaugeGroup.isLorentzCovDerivTransforms_covDerivIter`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L260).

> The iterated covariant derivative of a matter family transforms as the covariant
> derivatives of a Lorentz-covariant field, given the Lorentz law of the bare symbols,
> the Lorentz law of the gauge field, and the commutation of the infinitesimal gauge
> action with the Lorentz action on the value space.

```lean
lemma isLorentzCovDerivTransforms_covDerivIter {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : G.lieSubalgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep F) :
    IsLorentzCovDerivTransforms repLorentz rep (fun {n} l => covDerivIter A act F n l 0)
```

**`GlobalGaugeGroup.actionConj_comm_repConj`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L272).

> Conjugation preserves the commutation of the gauge action with the Lorentz action,
> since both are read on the conjugate module through the same underlying maps.

```lean
lemma actionConj_comm_repConj (rep : Representation ℂ SL(2,ℂ) V)
    (hcomm : ∀ (c : G.lieSubalgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (c : G.lieSubalgebra) (Λ : SL(2,ℂ)) (v : ConjModule V) :
    actionConj act c (rep.conj Λ v) =
      rep.conj Λ (actionConj act c v)
```

**`GlobalGaugeGroup.isLorentzCovDerivTransforms_covDerivIter_conj`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean#L282).

> The Lorentz law of the covariant tower of a conjugate family, from the commutation of
> the gauge action with the Lorentz action of the unconjugated species.

```lean
lemma isLorentzCovDerivTransforms_covDerivIter_conj {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : G.lieSubalgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ (ConjModule V) →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep.conj F) :
    IsLorentzCovDerivTransforms repLorentz rep.conj
      (fun {n} l => covDerivIter A (actionConj act) F n l 0)
```

## Depends on

- [The infinitesimal action underlying a matter representation](matterfield-infinitesimalaction.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)
- [The Lorentz mixing of derivative slots](../../../relativity/lorentzmix.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/LorentzCovariantDeriv.lean)
