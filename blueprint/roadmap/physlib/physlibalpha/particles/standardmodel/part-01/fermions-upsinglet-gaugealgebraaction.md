---
declaration: module
origin: cited
lean: StandardModel.UpSinglet.colourEnd, StandardModel.UpSinglet.colourEnd_apply_mk, StandardModel.UpSinglet.colourEnd_add, StandardModel.UpSinglet.colourEnd_smul, StandardModel.UpSinglet.actionMatrix, StandardModel.UpSinglet.gaugeAlgebraAction, StandardModel.UpSinglet.colourEnd_eq_valEnd, StandardModel.UpSinglet.matterField_repAlgebra_gaugeAlgebraEquiv
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the up-type singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.UpSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean): 9 declarations, 6 with a docstring.

> The explicit `(3, 1)_{4}` action of the gauge algebra on the up-type singlet, and its agreement
> with the matter field.

## i. Overview

> The `(3, 1)_{4}` action of the gauge algebra on the up-type singlet. The colour part of
> the algebra element acts on the colour index and the hypercharge part scales, both
> through the physicists' factor of `i`, matching the group action `u ^ 4 • U₃`
> infinitesimally. This action is the action of the gauge algebra of the matter field
> `UpSinglet.matterField`, transported along `gaugeAlgebraEquiv`, and it commutes with
> the Lorentz action.

## ii. Key results

> - `colourEnd` : the endomorphism of the up singlet defined by a colour matrix.
> - `gaugeAlgebraAction` : the infinitesimal `(3, 1)_{4}` action of the gauge algebra.
> - `matterField_repAlgebra_gaugeAlgebraEquiv` : the gauge algebra action of the matrix
>   matter field is `gaugeAlgebraAction`.
> - `gaugeAlgebraAction_comm_repLorentzGroup` : the gauge action commutes with the Lorentz
>   action.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.UpSinglet.colourEnd`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L66).

> The endomorphism of the up singlet defined by a `3 × 3` complex matrix acting on
> the colour index, with the Weyl factor untouched.

```lean
noncomputable def colourEnd (A : Matrix (Fin 3) (Fin 3) ℂ) :
    UpSinglet →ₗ[ℂ] UpSinglet
```

**`StandardModel.UpSinglet.colourEnd_apply_mk`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L72).

```lean
lemma colourEnd_apply_mk (A : Matrix (Fin 3) (Fin 3) ℂ) (v : UpSinglet) :
    colourEnd A v
      = valLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3)) Fermion.RightHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (valLinEquiv v))
```

**`StandardModel.UpSinglet.colourEnd_add`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L78).

```lean
lemma colourEnd_add (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A + B) = colourEnd A + colourEnd B
```

**`StandardModel.UpSinglet.colourEnd_smul`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L83).

```lean
lemma colourEnd_smul (z : ℂ) (A : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (z • A) = z • colourEnd A
```

**`StandardModel.UpSinglet.actionMatrix`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L91).

> The matrix of the infinitesimal `(3, 1)_{4}` action of a gauge algebra element on
> the colour index, `i` times the colour part shifted by `i` times `4` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.UpSinglet.gaugeAlgebraAction`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L97).

> The infinitesimal action of the gauge algebra on the up-type singlet, the
> derivative of the `(3, 1)_{4}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] UpSinglet →ₗ[ℂ] UpSinglet
```

## B. Comparison with the matter field

**`StandardModel.UpSinglet.colourEnd_eq_valEnd`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L130).

> The colour endomorphism of a matrix is the endomorphism of the matrix representation
> picture `tensorEquiv`.

```lean
lemma colourEnd_eq_valEnd (B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd B = MatrixRep.valEnd tensorEquiv B
```

**`StandardModel.UpSinglet.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L147).

> The action of the gauge algebra of the matter field of the up-type singlet, on the
> image of `gaugeAlgebraEquiv`, is `gaugeAlgebraAction`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.UpSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L166).

> The infinitesimal gauge action on the up-type singlet acts on the colour factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : UpSinglet) :
    UpSinglet.gaugeAlgebraAction c (UpSinglet.repLorentzGroup Λ v) =
      UpSinglet.repLorentzGroup Λ (UpSinglet.gaugeAlgebraAction c v)
```

## Depends on

- [The up-type singlet as a matter field](fermions-upsinglet-matterfield.md)
- [The gauge algebra as the Lie algebra of the global gauge group](../part-02/gaugegroup-liealgebra.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean)
