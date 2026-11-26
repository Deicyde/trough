---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV.weakEnd, StandardModel.LeptonDoubletV.weakEnd_add, StandardModel.LeptonDoubletV.weakEnd_smul, StandardModel.LeptonDoubletV.actionMatrix, StandardModel.LeptonDoubletV.gaugeAlgebraAction, StandardModel.LeptonDoubletV.derivMat_gaugeRep_gaugeAlgebraEquiv, StandardModel.LeptonDoubletV.matterField_repAlgebra_gaugeAlgebraEquiv, StandardModel.LeptonDoubletV.gaugeAlgebraAction_comm_repLorentzGroup
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the lepton doublet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonDoublet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean): 8 declarations, 6 with a docstring.

> The explicit `(1, 2)_{-3}` action of the gauge algebra on the lepton doublet, and its agreement
> with the matter field.

## i. Overview

> In the infinitesimal `(1, 2)_{-3}` action of the gauge algebra on the lepton doublet, the
> weak part of the algebra element acts on the weak index and the hypercharge part scales,
> both through the physicists' factor of `i`, matching the group action
> `(star u) ^ 3 • U₂` infinitesimally. This action is the action of the Lie algebra of the
> global gauge group on the matter field of the lepton doublet, transported along
> `StandardModel.gaugeAlgebraEquiv`, and it commutes with the Lorentz action.

## ii. Key results

> - `weakEnd` : the endomorphism of the lepton doublet defined by a `2 × 2` matrix on the
>   weak index.
> - `gaugeAlgebraAction` : the infinitesimal `(1, 2)_{-3}` action of the gauge algebra.
> - `matterField_repAlgebra_gaugeAlgebraEquiv` : the gauge-algebra action is the action of
>   the matter field of the lepton doublet.
> - `gaugeAlgebraAction_comm_repLorentzGroup` : the gauge action commutes with the Lorentz
>   action.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.LeptonDoubletV.weakEnd`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L65).

> The endomorphism of the lepton doublet defined by a `2 × 2` complex matrix acting on
> the weak index, with the Weyl factor untouched.

```lean
noncomputable def weakEnd (A : Matrix (Fin 2) (Fin 2) ℂ) :
    LeptonDoubletV →ₗ[ℂ] LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.weakEnd_add`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L69).

```lean
lemma weakEnd_add (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A + B) = weakEnd A + weakEnd B
```

**`StandardModel.LeptonDoubletV.weakEnd_smul`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L73).

```lean
lemma weakEnd_smul (z : ℂ) (A : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (z • A) = z • weakEnd A
```

**`StandardModel.LeptonDoubletV.actionMatrix`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L80).

> The matrix of the infinitesimal `(1, 2)_{-3}` action of a gauge algebra element on
> the weak index, `i` times the weak part shifted by `i` times `-3` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.LeptonDoubletV.gaugeAlgebraAction`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L86).

> The infinitesimal action of the gauge algebra on the lepton doublet, the
> derivative of the `(1, 2)_{-3}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] LeptonDoubletV →ₗ[ℂ] LeptonDoubletV
```

## B. The action of the matter field

> The action of the Lie algebra of the global gauge group on the matter field of the lepton
> doublet is the gauge-algebra action, transported along `gaugeAlgebraEquiv`.

**`StandardModel.LeptonDoubletV.derivMat_gaugeRep_gaugeAlgebraEquiv`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L122).

> The action matrix of the gauge representation of the lepton doublet on the image of a gauge
> algebra element under `gaugeAlgebraEquiv` is the action matrix of the gauge algebra.

```lean
lemma derivMat_gaugeRep_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat gaugeRep (gaugeAlgebraEquiv c) = actionMatrix c
```

**`StandardModel.LeptonDoubletV.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L132).

> The action of the gauge algebra of the matter field of the lepton doublet, on the
> image of a gauge algebra element under `gaugeAlgebraEquiv`, is `gaugeAlgebraAction`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.LeptonDoubletV.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L145).

> The infinitesimal gauge action on the lepton doublet acts on the weak factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : LeptonDoubletV) :
    LeptonDoubletV.gaugeAlgebraAction c (LeptonDoubletV.repLorentzGroup Λ v) =
      LeptonDoubletV.repLorentzGroup Λ (LeptonDoubletV.gaugeAlgebraAction c v)
```

## Depends on

- [The lepton doublet as a matter field](fermions-leptondoublet-matterfield.md)
- [The gauge algebra as the Lie algebra of the global gauge group](../part-02/gaugegroup-liealgebra.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean)
