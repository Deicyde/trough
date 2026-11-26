---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV.instNormedAddCommGroup, StandardModel.LeptonDoubletV.instNormedSpace, StandardModel.LeptonDoubletV.tensorEquiv, StandardModel.LeptonDoubletV.gaugeRep, StandardModel.LeptonDoubletV.matterField, StandardModel.LeptonDoubletV.matterField_V, StandardModel.LeptonDoubletV.matterField_repAlgebra, StandardModel.LeptonDoubletV.matterField_repLorentz
statement: formalized
proof: formalized
---

# The lepton doublet as a matter field

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonDoublet.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean): 15 declarations, 15 with a docstring.

> The lepton doublet `(1, 2)_{-3}` as a matter field of the Standard Model global gauge
> group.

## i. Overview

> The target space `LeptonDoubletV` is normed by the coordinates of its basis. A lepton doublet
> is a left-handed Weyl spinor with a weak index, and the global gauge group acts on the weak
> index by its `SU(2)` block scaled by the power `-3` of the hypercharge phase. This is the
> charge `-3` twist of the fundamental representation of `SU(2)`, which gives a matter field of
> mass weight three. Its action of the global gauge group, on the image of
> `StandardModel.gaugeGroupEquiv`, is the existing action
> `StandardModel.LeptonDoubletV.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.LeptonDoubletV.matterField` : the lepton doublet as a matrix matter
>   field of `StandardModel.globalGaugeGroup`.
> - `StandardModel.LeptonDoubletV.matterField_repAlgebra` : its action of the gauge
>   algebra.
> - `StandardModel.LeptonDoubletV.matterField_rep_gaugeGroupEquiv` : its action of the
>   gauge group is `StandardModel.LeptonDoubletV.repGaugeGroupI`.
> - `StandardModel.LeptonDoubletV.matterField_lorentzContinuous`,
>   `StandardModel.LeptonDoubletV.matterField_gaugeLorentzCommute` :
>   its Lorentz action is continuous and commutes with its gauge action.

## iv. References

> * None.

## A. The normed structure

> The target space is normed by the largest modulus of its coordinates in its basis.

**`StandardModel.LeptonDoubletV.instNormedAddCommGroup`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L67).

> The norm on the lepton doublets, the largest modulus of the coordinates in its basis.

```lean
noncomputable def instNormedAddCommGroup : NormedAddCommGroup LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.instNormedSpace`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L75).

> The lepton doublets as a normed space over `ℂ`.

```lean
noncomputable def instNormedSpace : NormedSpace ℂ LeptonDoubletV
```

## B. The gauge representation

**`StandardModel.LeptonDoubletV.tensorEquiv`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L87).

> The lepton doublets as a left-handed Weyl spinor tensored with the weak coordinates.

```lean
noncomputable def tensorEquiv : LeptonDoubletV ≃ₗ[ℂ] Fermion.LeftHandedWeyl ⊗[ℂ] (Fin 2 → ℂ)
```

**`StandardModel.LeptonDoubletV.gaugeRep`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L92).

> The representation of the global gauge group on the weak index of the lepton doublet,
> the fundamental representation of `SU(2)` twisted by the power `-3` of the hypercharge.

```lean
noncomputable def gaugeRep : globalGaugeGroup.group →ₜ* (Matrix (Fin 2) (Fin 2) ℂ)ˣ
```

## C. The matter field

**`StandardModel.LeptonDoubletV.matterField`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L103).

> The lepton doublet `(1, 2)_{-3}` as a matter field of the Standard Model global
> gauge group, with its left-handed Lorentz action.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.LeptonDoubletV.matterField_V`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L109).

> The target space of the matter field is the lepton doublets.

```lean
lemma matterField_V : matterField.V = LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.matterField_repAlgebra`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L113).

> The action of the gauge algebra of the matter field is the action matrix of its matrix
> representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

**`StandardModel.LeptonDoubletV.matterField_repLorentz`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L119).

> The Lorentz action of the matter field is that of the left-handed Weyl spinor.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = MatrixRep.repLorentz tensorEquiv Fermion.LeftHandedWeyl.rep
```

**`StandardModel.LeptonDoubletV.matterField_massWeight`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L124).

> The mass weight of the lepton doublet.

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.LeptonDoubletV.matterField_statistic`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L128).

> The lepton doublet is fermionic.

```lean
lemma matterField_statistic : matterField.statistic = .fermionic
```

**`StandardModel.LeptonDoubletV.matterField_lorentzContinuous`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L131).

> The Lorentz action of the matter field of the lepton doublet is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.LeptonDoubletV.matterField_gaugeLorentzCommute`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L135).

> The gauge and Lorentz representations of the matter field of the lepton doublet commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.LeptonDoubletV.matterField_repLorentz_eq`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L139).

> The Lorentz action of the matter field is the left-handed Lorentz action.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : LeptonDoubletV →ₗ[ℂ] LeptonDoubletV) =
      repLorentzGroup Λ
```

**`StandardModel.LeptonDoubletV.valEnd_eq_map`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L155).

> A matrix acts on the lepton doublet, through the identification `tensorEquiv`, on the weak
> index alone.

```lean
lemma valEnd_eq_map (B : Matrix (Fin 2) (Fin 2) ℂ) :
    MatrixRep.valEnd tensorEquiv B = TensorProduct.map LinearMap.id (Matrix.toLin' B)
```

**`StandardModel.LeptonDoubletV.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean#L161).

> The action of the gauge group on the matter field of the lepton doublet, through
> `gaugeGroupEquiv`, is the action `repGaugeGroupI`.

```lean
lemma matterField_rep_gaugeGroupEquiv (g : GaugeGroupI) :
    (((matterField.rep (gaugeGroupEquiv g) : _ˣ) :
      matterField.V →L[ℂ] matterField.V) : matterField.V →ₗ[ℂ]
        matterField.V) =
        (repGaugeGroupI g : matterField.V →ₗ[ℂ] matterField.V)
```

## Depends on

- [Conditions for the reduction of invariants](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-conditions.md)
- [Lepton doublets (PhyslibAlpha)](fermions-leptondoublet-basic.md)
- [The Standard Model gauge group as a global gauge group](../part-02/gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/MatterField.lean)
