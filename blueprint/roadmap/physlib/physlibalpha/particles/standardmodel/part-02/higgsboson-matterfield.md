---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.tensorEquiv, StandardModel.HiggsVec.gaugeRep, StandardModel.HiggsVec.matterField, StandardModel.HiggsVec.matterField_V, StandardModel.HiggsVec.matterField_repAlgebra, StandardModel.HiggsVec.matterField_repLorentz, StandardModel.HiggsVec.matterField_massWeight, StandardModel.HiggsVec.matterField_statistic
statement: formalized
proof: formalized
---

# The Higgs field as a matter field

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.MatterField`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean): 12 declarations, 12 with a docstring.

> The Higgs doublet `(1, 2)_{3}` as a matter field of the Standard Model global gauge group.

## i. Overview

> The target space `HiggsVec` is the Euclidean space `ℂ²`, already normed. The Higgs is a Lorentz
> scalar, so its Lorentz representation is the trivial one on `ℂ`. The global gauge group acts on
> it by the fundamental representation of the `SU(2)` block, twisted by the power `3` of the
> hypercharge phase. This is the charge `3` twist of the fundamental representation of `SU(2)`,
> which gives a bosonic matter field of mass weight two. Its action of the global gauge group, on
> the image of `StandardModel.gaugeGroupEquiv`, is the existing action
> `StandardModel.HiggsVec.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.HiggsVec.matterField` : the Higgs as a matter field of
>   `StandardModel.globalGaugeGroup`.
> - `StandardModel.HiggsVec.matterField_repAlgebra` : its action of the gauge algebra.
> - `StandardModel.HiggsVec.matterField_rep_gaugeGroupEquiv` : its action of the gauge
>   group is `StandardModel.HiggsVec.repGaugeGroupI`.
> - `StandardModel.HiggsVec.matterField_lorentzContinuous`,
>   `StandardModel.HiggsVec.matterField_gaugeLorentzCommute` : its Lorentz action is continuous and
>   commutes with its gauge action.

## iv. References

> * None.

## A. The gauge representation

**`StandardModel.HiggsVec.tensorEquiv`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L61).

> The Higgs vectors as a Lorentz scalar valued in `ℂ ⊗ ℂ²`.

```lean
noncomputable def tensorEquiv : HiggsVec ≃ₗ[ℂ] ℂ ⊗[ℂ] (Fin 2 → ℂ)
```

**`StandardModel.HiggsVec.gaugeRep`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L66).

> The representation of the global gauge group on the weak index of the Higgs, the
> fundamental representation of `SU(2)` twisted by the power `3` of the hypercharge.

```lean
noncomputable def gaugeRep : globalGaugeGroup.group →ₜ* (Matrix (Fin 2) (Fin 2) ℂ)ˣ
```

## B. The matter field

**`StandardModel.HiggsVec.matterField`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L77).

> The Higgs `(1, 2)_{3}` as a matter field of the Standard Model global gauge group,
> a Lorentz scalar.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.HiggsVec.matterField_V`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L82).

> The target space of the matter field is `HiggsVec`.

```lean
lemma matterField_V : matterField.V = HiggsVec
```

**`StandardModel.HiggsVec.matterField_repAlgebra`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L86).

> The action of the gauge algebra of the matter field is the action matrix of its matrix
> representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

**`StandardModel.HiggsVec.matterField_repLorentz`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L93).

> The Lorentz action of the matter field is that of the trivial scalar
> representation.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz =
      MatrixRep.repLorentz tensorEquiv (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

**`StandardModel.HiggsVec.matterField_massWeight`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L99).

> The mass weight of the Higgs.

```lean
lemma matterField_massWeight : matterField.massWeight = 2
```

**`StandardModel.HiggsVec.matterField_statistic`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L103).

> The Higgs is bosonic.

```lean
lemma matterField_statistic : matterField.statistic = .bosonic
```

**`StandardModel.HiggsVec.matterField_lorentzContinuous`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L106).

> The Lorentz action of the matter field of the Higgs is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.HiggsVec.matterField_gaugeLorentzCommute`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L111).

> The gauge and Lorentz representations of the matter field of the Higgs commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.HiggsVec.matterField_repLorentz_eq`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L115).

> The Lorentz action of the matter field is trivial.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : HiggsVec →ₗ[ℂ] HiggsVec) = LinearMap.id
```

**`StandardModel.HiggsVec.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L131).

> The action of the gauge group on the matter field of the Higgs, through
> `gaugeGroupEquiv`, is the action `repGaugeGroupI`.

```lean
lemma matterField_rep_gaugeGroupEquiv (g : GaugeGroupI) :
    (((matterField.rep (gaugeGroupEquiv g) : _ˣ) :
      matterField.V →L[ℂ] matterField.V) : matterField.V →ₗ[ℂ]
        matterField.V) =
        (repGaugeGroupI g : matterField.V →ₗ[ℂ] matterField.V)
```

## Depends on

- [The Higgs field](../../../../physlib/particles/standardmodel/higgsboson/basic.md)
- [Conditions for the reduction of invariants](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-conditions.md)
- [The Standard Model gauge group as a global gauge group](gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean)
