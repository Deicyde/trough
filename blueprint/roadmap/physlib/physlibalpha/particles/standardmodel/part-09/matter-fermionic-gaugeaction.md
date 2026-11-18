---
declaration: module
origin: cited
lean: StandardModel.FermionicAlgebra.repJetGaugeGroupI, StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply, StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply_one, StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply_mul, StandardModel.FermionicAlgebra.repJetGaugeGroupI_ι, StandardModel.FermionicAlgebra.repJetGaugeGroupIAlgHom, StandardModel.FermionicAlgebra.repJetGaugeGroupI_ofField, StandardModel.FermionicAlgebra.repJetGaugeGroupI_ofConjField
statement: formalized
proof: formalized
---

# The gauge action on the fermionic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.GaugeAction`, [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean): 14 declarations, 8 with a docstring.

## i. Overview

> Given a fibrewise action of the jet gauge group on the jets `SpaceTimeAlgebra ⊗[ℂ] V` of a matter
> field, the jet gauge group acts on the fermionic algebra by the exterior-algebra functor
> applied to the induced action on the jet component space. On a component function `∂_s ψ_α`
> the action is the all-orders Leibniz rule: each splitting of the derivative multiset
> contributes a Taylor coefficient of the gauge jet against a lower component function.
>
> Restricting along `JetGaugeGroupI.ofConstant` gives the action of the constant — that is,
> global — gauge transformations, which is diagonal in the derivative label.

## ii. Key results

> - `FermionicAlgebra.repJetGaugeGroupI` : the jet gauge action on the fermionic algebra.
> - `FermionicAlgebra.repJetGaugeGroupIAlgHom` : the action as an algebra homomorphism.
> - `FermionicAlgebra.repJetGaugeGroupI_ofField` : `ofField` is gauge equivariant, for the
>   value of the gauge transformation at the base point.
> - `FermionicAlgebra.repGaugeGroupI` : the action of the constant gauge transformations.

## iv. References

> * None.

## A. The action of the jet gauge group

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L64).

> **The jet gauge action on the fermionic algebra** of the matter field `M`: the exterior-algebra
> functor applied to the gauge action on the jet component space. The fibrewise action on the jets
> and its fibrewise-linearity are fields of `M`.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ GJ (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L75).

```lean
lemma repJetGaugeGroupI_apply
    (U : GJ) (x : FermionicAlgebra M) :
    repJetGaugeGroupI M U x =
      ExteriorAlgebra.map (JetComponentSpace.repJet M U) x
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply_one`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L81).

```lean
lemma repJetGaugeGroupI_apply_one
    (U : GJ) :
    repJetGaugeGroupI M U (1 : FermionicAlgebra M) = 1
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_apply_mul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L86).

```lean
lemma repJetGaugeGroupI_apply_mul
    (U : GJ) (x y : FermionicAlgebra M) :
    repJetGaugeGroupI M U (x * y) =
      repJetGaugeGroupI M U x * repJetGaugeGroupI M U y
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_ι`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L94).

> On a component function the jet gauge action is the action on the component space.

```lean
lemma repJetGaugeGroupI_ι
    (U : GJ) (v : JetComponentSpace M) :
    repJetGaugeGroupI M U (ExteriorAlgebra.ι ℂ v) =
      ExteriorAlgebra.ι ℂ (JetComponentSpace.repJet M U v)
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupIAlgHom`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L102).

> The jet gauge action as an algebra homomorphism: a gauge transformation acts on a
> Lagrangian term factor by factor.

```lean
noncomputable def repJetGaugeGroupIAlgHom
    (U : GJ) : FermionicAlgebra M →ₐ[ℂ] FermionicAlgebra M
```

### A.1. Equivariance of the field and its conjugate

> Unlike a derivative generator `∂_s ψ_φ`, which mixes with lower generators through the
> Taylor coefficients of the gauge jet, the undifferentiated generator `ψ_φ` transforms by
> the *value* of the gauge transformation at the base point alone. So `ofField` and
> `ofConjField` are equivariant on the nose, for the contragredient of that value.

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_ofField`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L125).

> **`ofField` is gauge equivariant.** The undifferentiated component functions transform
> by the contragredient of the value of the gauge transformation at the base point; no
> derivative of the gauge jet contributes.

```lean
lemma repJetGaugeGroupI_ofField
    (U : GJ) (φ : Module.Dual ℂ M.V) :
    repJetGaugeGroupI M U (ofField φ) =
      ofField (Module.Dual.transpose (jetEval ∘ₗ (M.repJet U⁻¹).comp jetOfConstant) φ)
```

**`StandardModel.FermionicAlgebra.repJetGaugeGroupI_ofConjField`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L139).

> **`ofConjField` is gauge equivariant**, for the conjugate action
> `JetComponentSpace.repConj rep` on the
> jets of the conjugate field — which is the physicists' `ψ̄ ↦ ψ̄ U†`.

```lean
lemma repJetGaugeGroupI_ofConjField
    (U : GJ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    repJetGaugeGroupI M U (ofConjField φ) =
      ofConjField (Module.Dual.transpose
        (jetEval ∘ₗ (JetComponentSpace.repConj M.repJet U⁻¹).comp jetOfConstant) φ)
```

## B. Constant gauge transformations

**`StandardModel.FermionicAlgebra.repGaugeGroupI`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L160).

> The action of the constant — that is, global — gauge transformations on the fermionic
> algebra, obtained by including a gauge transformation as a constant gauge jet.

```lean
noncomputable def repGaugeGroupI :
    Representation ℂ G₀ (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.repGaugeGroupI_apply`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L164).

```lean
lemma repGaugeGroupI_apply
    (g : G₀) (x : FermionicAlgebra M) :
    repGaugeGroupI M g x =
      repJetGaugeGroupI M (jets.ofConstant g) x
```

**`StandardModel.FermionicAlgebra.repGaugeGroupI_apply_one`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L170).

```lean
lemma repGaugeGroupI_apply_one
    (g : G₀) :
    repGaugeGroupI M g (1 : FermionicAlgebra M) = 1
```

**`StandardModel.FermionicAlgebra.repGaugeGroupI_apply_mul`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L175).

```lean
lemma repGaugeGroupI_apply_mul
    (g : G₀) (x y : FermionicAlgebra M) :
    repGaugeGroupI M g (x * y) =
      repGaugeGroupI M g x * repGaugeGroupI M g y
```

**`StandardModel.FermionicAlgebra.repGaugeGroupI_ofField`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L183).

> A constant gauge transformation acts on the undifferentiated field by the
> contragredient of its value — which for a constant jet is the transformation itself.

```lean
lemma repGaugeGroupI_ofField
    (g : G₀) (φ : Module.Dual ℂ M.V) :
    repGaugeGroupI M g (ofField φ) =
      ofField (Module.Dual.transpose
        (jetEval ∘ₗ (M.repJet (jets.ofConstant g⁻¹)).comp jetOfConstant) φ)
```

**`StandardModel.FermionicAlgebra.repGaugeGroupI_ofConjField`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean#L194).

> A constant gauge transformation acts on the undifferentiated conjugate field by the
> conjugate contragredient of its value.

```lean
lemma repGaugeGroupI_ofConjField
    (g : G₀) (φ : Module.Dual ℂ (ConjModule M.V)) :
    repGaugeGroupI M g (ofConjField φ) =
      ofConjField (Module.Dual.transpose
        (jetEval ∘ₗ (JetComponentSpace.repConj M.repJet (jets.ofConstant g⁻¹)).comp
          jetOfConstant) φ)
```

## Depends on

- [The gauge action on the jet component space](../../../classicalfieldtheory/gaugetheory/part-06/matterfield-jetcomponent-gaugeaction.md)
- [The fermionic algebra of a matter field](matter-fermionic-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/GaugeAction.lean)
