---
declaration: module
origin: cited
lean: GaugeBoson.JetComponentSpace.repLorentzGroup, SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton, GaugeBoson.JetComponentSpace.repLorentzGroup_jetDeriv, LocalGaugeFieldAlgebra.repLorentzGroup, LocalGaugeFieldAlgebra.repLorentzGroup_apply, LocalGaugeFieldAlgebra.repLorentzGroup_apply_one, LocalGaugeFieldAlgebra.repLorentzGroup_apply_mul, LocalGaugeFieldAlgebra.repLorentzGroup_ι
statement: formalized
proof: formalized
---

# The Lorentz action on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.LorentzAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean): 19 declarations, 12 with a docstring.

## i. Overview

> The Lorentz group acts on the jet algebra of the gauge bosons by the symmetric-algebra
> functor applied to its action on the jet component space: the derivative labels transform
> in `SpaceTimeDerivAlgebraℝ` and the target index contragrediently through the covector action on
> `GaugeBoson`. The formal total derivative is a Lorentz vector for this action; on the
> complexification this is packaged as a `Lorentz.IsLorentzDeriv` instance, giving access to
> the boost-weight machinery.

## ii. Key results

> - `GaugeBoson.JetComponentSpace.repLorentzGroup` : the Lorentz action on the component
>   space.
> - `LocalGaugeFieldAlgebra.repLorentzGroup` : the Lorentz action on the jet algebra.
> - `LocalGaugeFieldAlgebra.repLorentzGroup_jetDeriv` : the total derivative is a Lorentz vector.
> - `LocalGaugeFieldAlgebra.complexRepLorentzGroup` : the action on the complexification.
> - `LocalGaugeFieldAlgebra.instIsLorentzDeriv` : the `Lorentz.IsLorentzDeriv` instance.

## iv. References

> * None.

## A. The Lorentz action on the component space

**`GaugeBoson.JetComponentSpace.repLorentzGroup`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L69).

> The Lorentz action on the jet component space of the gauge bosons: the derivative
> label transforms in `SpaceTimeDerivAlgebraℝ`, the target index contragrediently.

```lean
noncomputable def JetComponentSpace.repLorentzGroup :
    Representation ℝ SL(2,ℂ) (JetComponentSpace 𝔤)
```

### A.1. Covariance of the derivative shift

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L81).

> The Lorentz action on the singleton derivative symbol: the derivative slot transforms
> by the columns of the Lorentz matrix.

```lean
lemma _root_.SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton
    (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ
        (SpaceTimeDerivAlgebraℝ.basisMultiset ({μ} : Multiset (Fin 1 ⊕ Fin 3))) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        SpaceTimeDerivAlgebraℝ.basisMultiset ({a} : Multiset (Fin 1 ⊕ Fin 3))
```

**`GaugeBoson.JetComponentSpace.repLorentzGroup_jetDeriv`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L96).

> **The derivative shift is a Lorentz vector on the component space**: appending `∂_μ`
> and then acting is acting and then appending the transformed `∂_μ`.

```lean
lemma JetComponentSpace.repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (v : (JetComponentSpace 𝔤)) :
    (JetComponentSpace.repLorentzGroup 𝔤) Λ ((JetComponentSpace.jetDeriv 𝔤) μ v) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        (JetComponentSpace.jetDeriv 𝔤) a ((JetComponentSpace.repLorentzGroup 𝔤) Λ v)
```

## B. The Lorentz action on the jet algebra

**`LocalGaugeFieldAlgebra.repLorentzGroup`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L137).

> **The Lorentz action on the gauge-boson jet algebra**: the symmetric-algebra functor
> applied to the Lorentz action on the jet component space.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L147).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ)) (x : (LocalGaugeFieldAlgebra 𝔤)) :
    (repLorentzGroup 𝔤) Λ x =
      SymmetricAlgebra.map ((GaugeBoson.JetComponentSpace.repLorentzGroup 𝔤) Λ) x
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply_one`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L153).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    (repLorentzGroup 𝔤) Λ (1 : (LocalGaugeFieldAlgebra 𝔤)) = 1
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply_mul`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L158).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : (LocalGaugeFieldAlgebra 𝔤)) :
    (repLorentzGroup 𝔤) Λ (x * y) = (repLorentzGroup 𝔤) Λ x * (repLorentzGroup 𝔤) Λ y
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_ι`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L164).

```lean
lemma repLorentzGroup_ι (Λ : SL(2,ℂ)) (v : (GaugeBoson.JetComponentSpace 𝔤)) :
    (repLorentzGroup 𝔤) Λ (SymmetricAlgebra.ι ℝ _ v) =
      SymmetricAlgebra.ι ℝ _ ((GaugeBoson.JetComponentSpace.repLorentzGroup 𝔤) Λ v)
```

## C. Lorentz covariance of the total derivative

**`LocalGaugeFieldAlgebra.repLorentzGroup_jetDeriv`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L177).

> **The total derivative on the gauge-boson jet algebra is a Lorentz vector.**

```lean
lemma repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (x : (LocalGaugeFieldAlgebra 𝔤)) :
    (repLorentzGroup 𝔤) Λ ((jetDeriv 𝔤) μ x) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        (jetDeriv 𝔤) a ((repLorentzGroup 𝔤) Λ x)
```

## D. The complexified action

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L208).

> The Lorentz action on the complexified gauge-boson jet algebra, by base change.

```lean
noncomputable def complexRepLorentzGroup :
    Representation ℂ SL(2,ℂ) (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤))
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_tmul`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L218).

```lean
lemma complexRepLorentzGroup_tmul (Λ : SL(2,ℂ)) (z : ℂ) (x : (LocalGaugeFieldAlgebra 𝔤)) :
    (complexRepLorentzGroup 𝔤) Λ (z ⊗ₜ[ℝ] x) = z ⊗ₜ[ℝ] (repLorentzGroup 𝔤) Λ x
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroupAlgHom`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L225).

> The action of a Lorentz transformation on the complexified gauge-boson jet algebra, as
> an algebra endomorphism: the base change of the symmetric-algebra functor applied to the
> action on the jet component space.

```lean
noncomputable def complexRepLorentzGroupAlgHom (Λ : SL(2,ℂ)) :
    ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤) →ₐ[ℂ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_apply`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L231).

```lean
lemma complexRepLorentzGroup_apply (Λ : SL(2,ℂ)) (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) :
    (complexRepLorentzGroup 𝔤) Λ x = complexRepLorentzGroupAlgHom 𝔤 Λ x
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_apply_mul`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L238).

```lean
lemma complexRepLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) :
    (complexRepLorentzGroup 𝔤) Λ (x * y)
      = (complexRepLorentzGroup 𝔤) Λ x * (complexRepLorentzGroup 𝔤) Λ y
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_jetDeriv`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L253).

> **The complexified total derivative is a Lorentz vector.**

```lean
lemma complexRepLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) :
    (complexRepLorentzGroup 𝔤) Λ ((complexJetDeriv 𝔤) μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        (complexJetDeriv 𝔤) a ((complexRepLorentzGroup 𝔤) Λ x)
```

**`LocalGaugeFieldAlgebra.instIsLorentzDeriv`**, an instance, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L273).

> The complexified total derivatives form a Lorentz derivative, giving access to the
> boost-weight machinery.

```lean
instance instIsLorentzDeriv :
    Lorentz.IsLorentzDeriv (complexRepLorentzGroup 𝔤) (complexJetDeriv 𝔤)
```

## E. The Lorentz law of the gauge-field generators

**`GaugeBoson.repLorentzGroup_dual_componentDual`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L286).

> The contragredient Lorentz action passes through a component covector to its spacetime
> slot: the adjoint index is Lorentz-inert.

```lean
lemma _root_.GaugeBoson.repLorentzGroup_dual_componentDual (Λ : SL(2,ℂ))
    (ω : Module.Dual ℝ Lorentz.CoVector) (φ : Module.Dual ℝ 𝔤) :
    (GaugeBoson.repLorentzGroup 𝔤).dual Λ ((GaugeBoson.componentDual 𝔤) ω φ)
      = (GaugeBoson.componentDual 𝔤) (Lorentz.CoVector.sl2Rep.dual Λ ω) φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_ofA`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L306).

> **The gauge field is a Lorentz covector**: the generator `A_μ^φ` mixes into the `A_a^φ`
> by the columns of the Lorentz matrix, with the adjoint index untouched.

```lean
lemma repLorentzGroup_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    (repLorentzGroup 𝔤) Λ ((ofA 𝔤) μ φ)
      = ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) • (ofA 𝔤) a φ
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_one_tmul_ofA`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean#L327).

> The Lorentz law of the gauge-field generators on the complexification.

```lean
lemma complexRepLorentzGroup_one_tmul_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    (complexRepLorentzGroup 𝔤) Λ ((1 : ℂ) ⊗ₜ[ℝ] (ofA 𝔤) μ φ)
      = ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
          ((1 : ℂ) ⊗ₜ[ℝ] (ofA 𝔤) a φ)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgauge-jetderiv.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/LorentzAction.lean)
