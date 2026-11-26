---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet.colourWeakValLinEquiv, StandardModel.QuarkDoublet.colourWeakEnd, StandardModel.QuarkDoublet.colourWeakEnd_apply_mk, StandardModel.QuarkDoublet.colourWeakEnd_add, StandardModel.QuarkDoublet.colourWeakEnd_smul, StandardModel.QuarkDoublet.actionMatrix, StandardModel.QuarkDoublet.gaugeAlgebraAction, StandardModel.QuarkDoublet.colourWeakEnd_eq_valEnd
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the quark doublet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.QuarkDoublet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean): 11 declarations, 8 with a docstring.

> The explicit `(3, 2)_{1}` action of the gauge algebra on the quark doublet, and its agreement
> with the matter field.

## i. Overview

> The `(3, 2)_{1}` action of the gauge algebra on the quark doublet. The colour and weak
> parts of the algebra element act on the combined colour–weak index through the Kronecker
> sum, and the hypercharge part scales, all through the physicists' factor of `i`, matching
> the group action `u • (U₃ ⊗ₖ U₂)` infinitesimally. The action is the action of the gauge
> algebra of the matter field of the quark doublet, transported along
> `StandardModel.gaugeAlgebraEquiv`, and it commutes with the Lorentz action.

## ii. Key results

> - `colourWeakEnd` : the endomorphism of the quark doublet defined by a colour–weak
>   matrix.
> - `gaugeAlgebraAction` : the infinitesimal `(3, 2)_{1}` action of the gauge algebra.
> - `matterField_repAlgebra_gaugeAlgebraEquiv` : the action of the gauge algebra of the
>   matter field is `gaugeAlgebraAction`.
> - `gaugeAlgebraAction_comm_repLorentzGroup` : the gauge action commutes with the Lorentz
>   action.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.QuarkDoublet.colourWeakValLinEquiv`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L66).

> The complex-linear identification of the quark doublet with a left-handed Weyl spinor
> tensored with a colour–weak vector over the combined index `Fin 3 × Fin 2`.

```lean
noncomputable def colourWeakValLinEquiv :
    QuarkDoublet ≃ₗ[ℂ] Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3 × Fin 2)
```

**`StandardModel.QuarkDoublet.colourWeakEnd`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L75).

> The endomorphism of the quark doublet defined by a complex matrix over the
> combined colour–weak index, with the Weyl factor untouched.

```lean
noncomputable def colourWeakEnd (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    QuarkDoublet →ₗ[ℂ] QuarkDoublet
```

**`StandardModel.QuarkDoublet.colourWeakEnd_apply_mk`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L81).

```lean
lemma colourWeakEnd_apply_mk (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ)
    (v : QuarkDoublet) :
    colourWeakEnd A v
      = colourWeakValLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3 × Fin 2))
            Fermion.LeftHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (colourWeakValLinEquiv v))
```

**`StandardModel.QuarkDoublet.colourWeakEnd_add`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L89).

```lean
lemma colourWeakEnd_add (A B : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (A + B) = colourWeakEnd A + colourWeakEnd B
```

**`StandardModel.QuarkDoublet.colourWeakEnd_smul`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L94).

```lean
lemma colourWeakEnd_smul (z : ℂ) (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (z • A) = z • colourWeakEnd A
```

**`StandardModel.QuarkDoublet.actionMatrix`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L102).

> The matrix of the infinitesimal `(3, 2)_{1}` action of a gauge algebra element on
> the combined colour–weak index, `i` times the Kronecker sum of the colour and weak
> parts shifted by `i` times the hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) :
    Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ
```

**`StandardModel.QuarkDoublet.gaugeAlgebraAction`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L111).

> The infinitesimal action of the gauge algebra on the quark doublet, the derivative of
> the `(3, 2)_{1}` action of the gauge group, real-linear in the algebra slot and
> complex-linear in the value slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] QuarkDoublet →ₗ[ℂ] QuarkDoublet
```

## B. The matter field

**`StandardModel.QuarkDoublet.colourWeakEnd_eq_valEnd`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L152).

> The colour–weak endomorphism of a matrix is the endomorphism of the matter field
> of the quark doublet defined by that matrix.

```lean
lemma colourWeakEnd_eq_valEnd (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd A = MatrixRep.valEnd tensorEquiv A
```

**`StandardModel.QuarkDoublet.derivMat_gaugeRep_gaugeAlgebraEquiv`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L177).

> The matrix of the action of the gauge algebra element `gaugeAlgebraEquiv c` in the
> gauge representation of the quark doublet is `actionMatrix c`.

```lean
lemma derivMat_gaugeRep_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat gaugeRep (gaugeAlgebraEquiv c) = actionMatrix c
```

**`StandardModel.QuarkDoublet.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L190).

> The action of the gauge algebra of the matter field of the quark doublet, on the
> image of `gaugeAlgebraEquiv`, is `gaugeAlgebraAction`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.QuarkDoublet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L203).

> The infinitesimal gauge action on the quark doublet acts on the combined colour–weak
> factor, the Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : QuarkDoublet) :
    QuarkDoublet.gaugeAlgebraAction c (QuarkDoublet.repLorentzGroup Λ v) =
      QuarkDoublet.repLorentzGroup Λ (QuarkDoublet.gaugeAlgebraAction c v)
```

## Depends on

- [The quark doublet as a matter field](fermions-quarkdoublet-matterfield.md)
- [The gauge algebra as the Lie algebra of the global gauge group](../part-02/gaugegroup-liealgebra.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean)
