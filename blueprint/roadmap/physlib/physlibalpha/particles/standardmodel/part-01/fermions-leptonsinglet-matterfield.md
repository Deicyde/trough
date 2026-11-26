---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet.instNormedAddCommGroup, StandardModel.LeptonSinglet.instNormedSpace, StandardModel.LeptonSinglet.tensorEquiv, StandardModel.LeptonSinglet.tensorEquiv_symm_tmul, StandardModel.LeptonSinglet.gaugeRep, StandardModel.LeptonSinglet.matterField, StandardModel.LeptonSinglet.matterField_V, StandardModel.LeptonSinglet.matterField_repLorentz
statement: formalized
proof: formalized
---

# The charged-lepton singlet as a matter field

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonSinglet.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean): 15 declarations, 15 with a docstring.

> The charged-lepton singlet `(1, 1)_{-6}` as a matter field of the Standard Model global gauge
> group.

## i. Overview

> The target space `LeptonSinglet` is normed by the coordinates of its basis. A charged-lepton
> singlet is a right-handed Weyl spinor with a trivial internal index, and the global gauge group
> acts on it by the power `-6` of the hypercharge phase. This is the charge `-6` twist of the
> trivial matrix representation, which gives a matter field of mass weight three. Its action of
> the global gauge group, on the image of `StandardModel.gaugeGroupEquiv`, is the existing action
> `StandardModel.LeptonSinglet.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.LeptonSinglet.matterField` : the charged-lepton singlet as a matter field of
>   `StandardModel.globalGaugeGroup`.
> - `StandardModel.LeptonSinglet.matterField_repAlgebra` : its action of the gauge algebra.
> - `StandardModel.LeptonSinglet.matterField_rep_gaugeGroupEquiv` : its action of the gauge
>   group is `StandardModel.LeptonSinglet.repGaugeGroupI`.
> - `StandardModel.LeptonSinglet.matterField_lorentzContinuous`,
>   `StandardModel.LeptonSinglet.matterField_gaugeLorentzCommute` :
>   its Lorentz action is continuous and commutes with its gauge action.

## iv. References

> * None.

## A. The normed structure

> The target space is normed by the largest modulus of its coordinates in its basis.

**`StandardModel.LeptonSinglet.instNormedAddCommGroup`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L66).

> The norm on the charged-lepton singlets, the largest modulus of the coordinates in its
> basis.

```lean
noncomputable def instNormedAddCommGroup : NormedAddCommGroup LeptonSinglet
```

**`StandardModel.LeptonSinglet.instNormedSpace`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L73).

> The charged-lepton singlets as a normed space over `ℂ`.

```lean
noncomputable def instNormedSpace : NormedSpace ℂ LeptonSinglet
```

## B. The matter field

> The field is a right-handed Weyl spinor with a trivial internal index, and its gauge group
> acts through the hypercharge only.

**`StandardModel.LeptonSinglet.tensorEquiv`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L89).

> The identification of the charged-lepton singlets with a right-handed Weyl spinor tensored
> with a trivial internal index.

```lean
noncomputable def tensorEquiv :
    LeptonSinglet ≃ₗ[ℂ] Fermion.RightHandedWeyl ⊗[ℂ] (Fin 1 → ℂ)
```

**`StandardModel.LeptonSinglet.tensorEquiv_symm_tmul`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L95).

> The identification `tensorEquiv` on a pure tensor.

```lean
lemma tensorEquiv_symm_tmul (s : Fermion.RightHandedWeyl) (w : Fin 1 → ℂ) :
    tensorEquiv.symm (s ⊗ₜ[ℂ] w) = ⟨w 0 • s⟩
```

**`StandardModel.LeptonSinglet.gaugeRep`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L102).

> The representation of the global gauge group on the internal index of the charged-lepton
> singlet, the trivial representation twisted by the power `-6` of the hypercharge.

```lean
noncomputable def gaugeRep : globalGaugeGroup.group →ₜ* (Matrix (Fin 1) (Fin 1) ℂ)ˣ
```

**`StandardModel.LeptonSinglet.matterField`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L107).

> The charged-lepton singlet `(1, 1)_{-6}` as a matter field of the Standard Model global
> gauge group, with its right-handed Lorentz action.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.LeptonSinglet.matterField_V`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L113).

> The target space of the matter field is the charged-lepton singlets.

```lean
lemma matterField_V : matterField.V = LeptonSinglet
```

**`StandardModel.LeptonSinglet.matterField_repLorentz`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L117).

> The Lorentz action of the matter field is that of the right-handed Weyl spinor.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = MatrixRep.repLorentz tensorEquiv Fermion.RightHandedWeyl.rep
```

**`StandardModel.LeptonSinglet.matterField_massWeight`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L122).

> The mass weight of the charged-lepton singlet.

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.LeptonSinglet.matterField_statistic`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L126).

> The charged-lepton singlet is fermionic.

```lean
lemma matterField_statistic : matterField.statistic = .fermionic
```

**`StandardModel.LeptonSinglet.matterField_repAlgebra`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L130).

> The action of the gauge algebra of the matter field of the charged-lepton singlet is the
> action matrix of its matrix representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

## C. Its actions

**`StandardModel.LeptonSinglet.matterField_repLorentz_eq`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L141).

> The Lorentz action of the matter field is the right-handed Lorentz action.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : LeptonSinglet →ₗ[ℂ] LeptonSinglet) =
      repLorentzGroup Λ
```

**`StandardModel.LeptonSinglet.matterField_lorentzContinuous`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L159).

> The Lorentz action of the matter field of the charged-lepton singlet is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.LeptonSinglet.matterField_gaugeLorentzCommute`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L164).

> The gauge and Lorentz representations of the matter field of the charged-lepton singlet
> commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.LeptonSinglet.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean#L169).

> The action of the gauge group on the matter field of the charged-lepton singlet,
> through `gaugeGroupEquiv`, is the action `repGaugeGroupI`.

```lean
lemma matterField_rep_gaugeGroupEquiv (g : GaugeGroupI) :
    (((matterField.rep (gaugeGroupEquiv g) : _ˣ) : matterField.V →L[ℂ] matterField.V) :
      matterField.V →ₗ[ℂ] matterField.V) =
        (repGaugeGroupI g : matterField.V →ₗ[ℂ] matterField.V)
```

## Depends on

- [Conditions for the reduction of invariants](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-conditions.md)
- [Charged-lepton singlets (PhyslibAlpha)](fermions-leptonsinglet-basic.md)
- [The Standard Model gauge group as a global gauge group](../part-02/gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/MatterField.lean)
