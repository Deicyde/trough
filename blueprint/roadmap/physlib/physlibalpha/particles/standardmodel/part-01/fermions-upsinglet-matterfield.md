---
declaration: module
origin: cited
lean: StandardModel.UpSinglet.instNormedAddCommGroup, StandardModel.UpSinglet.instNormedSpace, StandardModel.UpSinglet.tensorEquiv, StandardModel.UpSinglet.tensorEquiv_symm_tmul, StandardModel.UpSinglet.gaugeRep, StandardModel.UpSinglet.matterField, StandardModel.UpSinglet.matterField_V, StandardModel.UpSinglet.matterField_repAlgebra
statement: formalized
proof: formalized
---

# The up-type singlet as a matter field

The module `PhyslibAlpha.Particles.StandardModel.Fermions.UpSinglet.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean): 15 declarations, 15 with a docstring.

> The up-type singlet `(3, 1)_{4}` as a matter field of the Standard Model global
> gauge group.

## i. Overview

> The target space `UpSinglet` is normed by the coordinates of its basis. An up-type singlet is a
> right-handed Weyl spinor with a colour index in `Fin 3`, and the global gauge group acts on it by
> the fundamental representation of the `SU(3)` block twisted by the power `4` of the hypercharge
> phase. This is the charge `4` twist of the fundamental representation of the colour factor,
> which gives a matter field of mass weight three. Its action of the global gauge group, on the
> image of `StandardModel.gaugeGroupEquiv`, is the existing action
> `StandardModel.UpSinglet.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.UpSinglet.matterField` : the up-type singlet as a matter field of
>   `StandardModel.globalGaugeGroup`.
> - `StandardModel.UpSinglet.matterField_repAlgebra` : its action of the gauge algebra.
> - `StandardModel.UpSinglet.matterField_rep_gaugeGroupEquiv` : its action of the gauge
>   group is `StandardModel.UpSinglet.repGaugeGroupI`.
> - `StandardModel.UpSinglet.matterField_lorentzContinuous`,
>   `StandardModel.UpSinglet.matterField_gaugeLorentzCommute` :
>   its Lorentz action is continuous and commutes with its gauge action.

## iv. References

> * None.

## A. The normed structure

> The target space is normed by the largest modulus of its coordinates in its basis.

**`StandardModel.UpSinglet.instNormedAddCommGroup`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L67).

> The norm on the up-type singlets, the largest modulus of the coordinates in its
> basis.

```lean
noncomputable def instNormedAddCommGroup : NormedAddCommGroup UpSinglet
```

**`StandardModel.UpSinglet.instNormedSpace`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L75).

> The up-type singlets as a normed space over `ℂ`.

```lean
noncomputable def instNormedSpace : NormedSpace ℂ UpSinglet
```

## B. The gauge representation

**`StandardModel.UpSinglet.tensorEquiv`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L87).

> The up-type singlets as a right-handed Weyl spinor with a colour index.

```lean
noncomputable def tensorEquiv : UpSinglet ≃ₗ[ℂ] Fermion.RightHandedWeyl ⊗[ℂ] (Fin 3 → ℂ)
```

**`StandardModel.UpSinglet.tensorEquiv_symm_tmul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L92).

> The inverse of the identification `tensorEquiv` on a pure tensor.

```lean
lemma tensorEquiv_symm_tmul (s : Fermion.RightHandedWeyl) (w : Fin 3 → ℂ) :
    tensorEquiv.symm (s ⊗ₜ[ℂ] w) = ⟨s ⊗ₜ[ℂ] (WithLp.toLp 2 w)⟩
```

**`StandardModel.UpSinglet.gaugeRep`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L97).

> The representation of the global gauge group on the colour index of the up-type singlet,
> the fundamental representation of `SU(3)` twisted by the power `4` of the hypercharge.

```lean
noncomputable def gaugeRep : globalGaugeGroup.group →ₜ* (Matrix (Fin 3) (Fin 3) ℂ)ˣ
```

## C. The matter field

**`StandardModel.UpSinglet.matterField`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L108).

> The up-type singlet `(3, 1)_{4}` as a matter field of the Standard Model global
> gauge group, with its right-handed Lorentz action.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.UpSinglet.matterField_V`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L114).

> The target space of the matter field is the up-type singlets.

```lean
lemma matterField_V : matterField.V = UpSinglet
```

**`StandardModel.UpSinglet.matterField_repAlgebra`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L118).

> The action of the gauge algebra of the matter field is the action matrix of its matrix
> representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

**`StandardModel.UpSinglet.matterField_repLorentz`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L125).

> The Lorentz action of the matter field is that of the right-handed Weyl
> spinor.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = MatrixRep.repLorentz tensorEquiv Fermion.RightHandedWeyl.rep
```

**`StandardModel.UpSinglet.matterField_massWeight`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L130).

> The mass weight of the up-type singlet.

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.UpSinglet.matterField_statistic`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L134).

> The up-type singlet is fermionic.

```lean
lemma matterField_statistic : matterField.statistic = .fermionic
```

**`StandardModel.UpSinglet.matterField_lorentzContinuous`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L137).

> The Lorentz action of the matter field of the up-type quark singlet is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.UpSinglet.matterField_gaugeLorentzCommute`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L142).

> The gauge and Lorentz representations of the matter field of the up-type quark singlet
> commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.UpSinglet.matterField_repLorentz_eq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L146).

> The Lorentz action of the matter field is the right-handed Lorentz action.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : UpSinglet →ₗ[ℂ] UpSinglet) =
      repLorentzGroup Λ
```

**`StandardModel.UpSinglet.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean#L164).

> The action of the gauge group on the matter field of the up-type singlet,
> through `gaugeGroupEquiv`, is the action `repGaugeGroupI`.

```lean
lemma matterField_rep_gaugeGroupEquiv (g : GaugeGroupI) :
    (((matterField.rep (gaugeGroupEquiv g) : _ˣ) :
      matterField.V →L[ℂ] matterField.V) : matterField.V →ₗ[ℂ]
        matterField.V) =
        (repGaugeGroupI g : matterField.V →ₗ[ℂ] matterField.V)
```

## Depends on

- [Conditions for the reduction of invariants](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-conditions.md)
- [Up-type singlets (PhyslibAlpha)](fermions-upsinglet-basic.md)
- [The Standard Model gauge group as a global gauge group](../part-02/gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/MatterField.lean)
