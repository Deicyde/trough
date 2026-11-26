---
declaration: module
origin: cited
lean: StandardModel.DownSinglet.colourEnd, StandardModel.DownSinglet.colourEnd_apply_mk, StandardModel.DownSinglet.colourEnd_add, StandardModel.DownSinglet.colourEnd_smul, StandardModel.DownSinglet.actionMatrix, StandardModel.DownSinglet.gaugeAlgebraAction, StandardModel.DownSinglet.gaugeAlgebraAction_comm_repLorentzGroup, StandardModel.DownSinglet.colourEnd_eq_valEnd
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the down-type singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean): 10 declarations, 7 with a docstring.

> The explicit `(3, 1)_{-2}` action of the gauge algebra on the down-type singlet, and its agreement
> with the matter field.

## i. Overview

> The infinitesimal `(3, 1)_{-2}` action of the gauge algebra on the down-type singlet, its
> compatibility with the Lorentz action, and its identification with the action of the gauge
> algebra of the matter field `DownSinglet.matterField`.

## ii. Key results

> - `DownSinglet.colourEnd` : the endomorphism of the down singlet defined by a `3 × 3` complex
>   matrix acting on the colour index, with the Weyl factor untouched.
> - `DownSinglet.actionMatrix` : the matrix of the infinitesimal action of a gauge algebra
>   element.
> - `DownSinglet.gaugeAlgebraAction` : the infinitesimal `(3, 1)_{-2}` action.
> - `DownSinglet.gaugeAlgebraAction_comm_repLorentzGroup` : the gauge action commutes with the
>   Lorentz action.
> - `DownSinglet.matterField_repAlgebra_gaugeAlgebraEquiv` : the action of the gauge algebra
>   of the matter field is `DownSinglet.gaugeAlgebraAction`.

## iv. References

> * None.

## A. The action of the gauge algebra

> The infinitesimal `(3, 1)_{-2}` action of the gauge algebra on the down-type singlet:
> the colour part of the algebra element acts on the colour index and the hypercharge
> part scales, both through the physicists' factor of `i`, matching the group action
> `(star u) ^ 2 • U₃` infinitesimally.

**`StandardModel.DownSinglet.colourEnd`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L68).

> The endomorphism of the down singlet defined by a `3 × 3` complex matrix acting on
> the colour index, with the Weyl factor untouched.

```lean
noncomputable def colourEnd (A : Matrix (Fin 3) (Fin 3) ℂ) :
    DownSinglet →ₗ[ℂ] DownSinglet
```

**`StandardModel.DownSinglet.colourEnd_apply_mk`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L74).

```lean
lemma colourEnd_apply_mk (A : Matrix (Fin 3) (Fin 3) ℂ) (v : DownSinglet) :
    colourEnd A v
      = valLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3)) Fermion.RightHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (valLinEquiv v))
```

**`StandardModel.DownSinglet.colourEnd_add`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L80).

```lean
lemma colourEnd_add (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A + B) = colourEnd A + colourEnd B
```

**`StandardModel.DownSinglet.colourEnd_smul`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L85).

```lean
lemma colourEnd_smul (z : ℂ) (A : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (z • A) = z • colourEnd A
```

**`StandardModel.DownSinglet.actionMatrix`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L93).

> The matrix of the infinitesimal `(3, 1)_{-2}` action of a gauge algebra element on
> the colour index, `i` times the colour part shifted by `i` times `-2` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.DownSinglet.gaugeAlgebraAction`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L99).

> The infinitesimal action of the gauge algebra on the down-type singlet, the
> derivative of the `(3, 1)_{-2}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] DownSinglet →ₗ[ℂ] DownSinglet
```

## B. The gauge action commutes with the Lorentz action

**`StandardModel.DownSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L132).

> The infinitesimal gauge action on the down-type singlet acts on the colour factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : DownSinglet) :
    DownSinglet.gaugeAlgebraAction c (DownSinglet.repLorentzGroup Λ v) =
      DownSinglet.repLorentzGroup Λ (DownSinglet.gaugeAlgebraAction c v)
```

## C. The matter field

**`StandardModel.DownSinglet.colourEnd_eq_valEnd`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L146).

> The colour endomorphism of a matrix is the endomorphism of the matrix representation.

```lean
lemma colourEnd_eq_valEnd (A : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd A = MatrixRep.valEnd tensorEquiv A
```

**`StandardModel.DownSinglet.derivMat_gaugeRep_gaugeAlgebraEquiv`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L159).

> The action matrix of the matrix representation on `gaugeAlgebraEquiv c` is `actionMatrix c`.

```lean
lemma derivMat_gaugeRep_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat gaugeRep (gaugeAlgebraEquiv c) = actionMatrix c
```

**`StandardModel.DownSinglet.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L169).

> The action of the gauge algebra of the matter field of the down-type singlet, on the
> image of `gaugeAlgebraEquiv`, is `gaugeAlgebraAction`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## Depends on

- [The down-type singlet as a matter field](fermions-downsinglet-matterfield.md)
- [The gauge algebra as the Lie algebra of the global gauge group](../part-02/gaugegroup-liealgebra.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean)
