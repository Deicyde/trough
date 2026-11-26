---
declaration: module
origin: cited
lean: StandardModel.DownSinglet.instNormedAddCommGroup, StandardModel.DownSinglet.instNormedSpace, StandardModel.DownSinglet.tensorEquiv, StandardModel.DownSinglet.tensorEquiv_symm_tmul, StandardModel.DownSinglet.gaugeRep, StandardModel.DownSinglet.matterField, StandardModel.DownSinglet.matterField_V, StandardModel.DownSinglet.matterField_repAlgebra
statement: formalized
proof: formalized
---

# The down-type singlet as a matter field

The module `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean): 15 declarations, 15 with a docstring.

> The down-type singlet `(3, 1)_{-2}` as a matter field of the Standard Model global
> gauge group.

## i. Overview

> The target space `DownSinglet` is normed by the coordinates of its basis. A down-type singlet
> is a right-handed Weyl spinor with a colour index, and the global gauge group acts on it by the
> fundamental representation of `SU(3)` twisted by the power `-2` of the hypercharge phase. This
> is the charge `-2` twist of the fundamental representation of the colour factor, which gives a
> matter field of mass weight three. Its action of the global gauge group, on the image of
> `StandardModel.gaugeGroupEquiv`, is the existing action
> `StandardModel.DownSinglet.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.DownSinglet.matterField` : the down-type singlet as a matrix matter
>   field of `StandardModel.globalGaugeGroup`.
> - `StandardModel.DownSinglet.matterField_repAlgebra` : its action of the gauge algebra.
> - `StandardModel.DownSinglet.matterField_rep_gaugeGroupEquiv` : its action of the gauge
>   group is `StandardModel.DownSinglet.repGaugeGroupI`.
> - `StandardModel.DownSinglet.matterField_lorentzContinuous`,
>   `StandardModel.DownSinglet.matterField_gaugeLorentzCommute` :
>   its Lorentz action is continuous and commutes with its gauge action.

## iv. References

> * None.

## A. The normed structure

> The target space is normed by the largest modulus of its coordinates in its basis.

**`StandardModel.DownSinglet.instNormedAddCommGroup`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L67).

> The norm on the down singlets, the largest modulus of the coordinates in its
> basis.

```lean
noncomputable def instNormedAddCommGroup : NormedAddCommGroup DownSinglet
```

**`StandardModel.DownSinglet.instNormedSpace`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L75).

> The down singlets as a normed space over `ℂ`.

```lean
noncomputable def instNormedSpace : NormedSpace ℂ DownSinglet
```

## B. The gauge representation

**`StandardModel.DownSinglet.tensorEquiv`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L87).

> The down singlets as a right-handed Weyl spinor with a colour index.

```lean
noncomputable def tensorEquiv : DownSinglet ≃ₗ[ℂ] Fermion.RightHandedWeyl ⊗[ℂ] (Fin 3 → ℂ)
```

**`StandardModel.DownSinglet.tensorEquiv_symm_tmul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L92).

> The inverse of the identification `tensorEquiv` on a pure tensor.

```lean
lemma tensorEquiv_symm_tmul (s : Fermion.RightHandedWeyl) (w : Fin 3 → ℂ) :
    tensorEquiv.symm (s ⊗ₜ[ℂ] w) = ⟨s ⊗ₜ[ℂ] (WithLp.toLp 2 w)⟩
```

**`StandardModel.DownSinglet.gaugeRep`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L99).

> The representation of the global gauge group on the colour index of the down-type
> singlet, the fundamental representation of `SU(3)` twisted by the power `-2` of the
> hypercharge.

```lean
noncomputable def gaugeRep : globalGaugeGroup.group →ₜ* (Matrix (Fin 3) (Fin 3) ℂ)ˣ
```

## C. The matter field

**`StandardModel.DownSinglet.matterField`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L110).

> The down-type singlet `(3, 1)_{-2}` as a matter field of the Standard Model
> global gauge group, with its right-handed Lorentz action.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.DownSinglet.matterField_V`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L116).

> The target space of the matter field is the down singlets.

```lean
lemma matterField_V : matterField.V = DownSinglet
```

**`StandardModel.DownSinglet.matterField_repAlgebra`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L120).

> The action of the gauge algebra of the matter field is the action matrix of its matrix
> representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

**`StandardModel.DownSinglet.matterField_repLorentz`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L127).

> The Lorentz action of the matter field is that of the right-handed Weyl
> spinor.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = MatrixRep.repLorentz tensorEquiv Fermion.RightHandedWeyl.rep
```

**`StandardModel.DownSinglet.matterField_massWeight`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L132).

> The mass weight of the down-type singlet.

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.DownSinglet.matterField_statistic`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L136).

> The down-type singlet is fermionic.

```lean
lemma matterField_statistic : matterField.statistic = .fermionic
```

**`StandardModel.DownSinglet.matterField_lorentzContinuous`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L139).

> The Lorentz action of the matter field of the down-type quark singlet is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.DownSinglet.matterField_gaugeLorentzCommute`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L144).

> The gauge and Lorentz representations of the matter field of the down-type quark singlet
> commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.DownSinglet.matterField_repLorentz_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L148).

> The Lorentz action of the matter field is the right-handed Lorentz action.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : DownSinglet →ₗ[ℂ] DownSinglet) =
      repLorentzGroup Λ
```

**`StandardModel.DownSinglet.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean#L166).

> The action of the gauge group on the matter field of the down-type singlet,
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
- [Down-type singlets (PhyslibAlpha)](fermions-downsinglet-basic.md)
- [The Standard Model gauge group as a global gauge group](../part-02/gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/MatterField.lean)
