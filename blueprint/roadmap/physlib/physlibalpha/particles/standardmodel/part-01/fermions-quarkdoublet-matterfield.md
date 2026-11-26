---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet.instNormedAddCommGroup, StandardModel.QuarkDoublet.instNormedSpace, StandardModel.QuarkDoublet.tensorEquiv, StandardModel.QuarkDoublet.tensorEquiv_mk, StandardModel.QuarkDoublet.tensorEquiv_symm_tmul, StandardModel.QuarkDoublet.linearMap_ext_mk, StandardModel.QuarkDoublet.gaugeRep, StandardModel.QuarkDoublet.matterField
statement: formalized
proof: formalized
---

# The quark doublet as a matter field

The module `PhyslibAlpha.Particles.StandardModel.Fermions.QuarkDoublet.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean): 18 declarations, 18 with a docstring.

> The quark doublet `(3, 2)_1` as a matter field of the Standard Model global gauge group.

## i. Overview

> The target space `QuarkDoublet` is normed by the coordinates of its basis. A quark doublet is a
> left-handed Weyl spinor with a combined colour and weak index in `Fin 3 × Fin 2`, and the global
> gauge group acts on it by the hypercharge phase times the Kronecker product of the `SU(3)` and
> `SU(2)` blocks. This is the charge `1` twist of the Kronecker product of the fundamental
> representations of the two factors, which gives a matter field of mass weight three. Its action
> of the global gauge group, on the image of `StandardModel.gaugeGroupEquiv`, is the existing
> action `StandardModel.QuarkDoublet.repGaugeGroupI`.

## ii. Key results

> - `StandardModel.QuarkDoublet.matterField` : the quark doublet as a matter field of
>   `StandardModel.globalGaugeGroup`.
> - `StandardModel.QuarkDoublet.matterField_repAlgebra` : its action of the gauge algebra.
> - `StandardModel.QuarkDoublet.valEnd_smul_kronecker` : the action of a scaled Kronecker product
>   of matrices on the combined colour and weak index.
> - `StandardModel.QuarkDoublet.matterField_rep_gaugeGroupEquiv` : its action of the gauge
>   group is `StandardModel.QuarkDoublet.repGaugeGroupI`.
> - `StandardModel.QuarkDoublet.matterField_lorentzContinuous`,
>   `StandardModel.QuarkDoublet.matterField_gaugeLorentzCommute` :
>   its Lorentz action is continuous and commutes with its gauge action.

## iv. References

> * None.

## A. The normed structure

> The target space is normed by the largest modulus of its coordinates in its basis.

**`StandardModel.QuarkDoublet.instNormedAddCommGroup`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L71).

> The norm on the quark doublets, the largest modulus of the coordinates in its
> basis.

```lean
noncomputable def instNormedAddCommGroup : NormedAddCommGroup QuarkDoublet
```

**`StandardModel.QuarkDoublet.instNormedSpace`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L79).

> The quark doublets as a normed space over `ℂ`.

```lean
noncomputable def instNormedSpace : NormedSpace ℂ QuarkDoublet
```

## B. The gauge representation

**`StandardModel.QuarkDoublet.tensorEquiv`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L91).

> The quark doublets as a left-handed Weyl spinor with a combined colour and weak index.

```lean
noncomputable def tensorEquiv :
    QuarkDoublet ≃ₗ[ℂ] Fermion.LeftHandedWeyl ⊗[ℂ] (Fin 3 × Fin 2 → ℂ)
```

**`StandardModel.QuarkDoublet.tensorEquiv_mk`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L99).

> The identification `tensorEquiv` on a pure tensor.

```lean
lemma tensorEquiv_mk (s : Fermion.LeftHandedWeyl) (c : EuclideanSpace ℂ (Fin 3))
    (w : EuclideanSpace ℂ (Fin 2)) :
    tensorEquiv ⟨(s ⊗ₜ[ℂ] c) ⊗ₜ[ℂ] w⟩ = s ⊗ₜ[ℂ] colourWeakEquiv (c ⊗ₜ[ℂ] w)
```

**`StandardModel.QuarkDoublet.tensorEquiv_symm_tmul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L104).

> The inverse of the identification `tensorEquiv` on a pure tensor.

```lean
lemma tensorEquiv_symm_tmul (s : Fermion.LeftHandedWeyl) (c : EuclideanSpace ℂ (Fin 3))
    (w : EuclideanSpace ℂ (Fin 2)) :
    tensorEquiv.symm (s ⊗ₜ[ℂ] colourWeakEquiv (c ⊗ₜ[ℂ] w)) = ⟨(s ⊗ₜ[ℂ] c) ⊗ₜ[ℂ] w⟩
```

**`StandardModel.QuarkDoublet.linearMap_ext_mk`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L111).

> Two linear maps on the quark doublets are equal when they agree on the elements built from
> pure tensors.

```lean
lemma linearMap_ext_mk {f g : QuarkDoublet →ₗ[ℂ] QuarkDoublet}
    (h : ∀ (s : Fermion.LeftHandedWeyl) (c : EuclideanSpace ℂ (Fin 3))
      (w : EuclideanSpace ℂ (Fin 2)), f ⟨(s ⊗ₜ[ℂ] c) ⊗ₜ[ℂ] w⟩ = g ⟨(s ⊗ₜ[ℂ] c) ⊗ₜ[ℂ] w⟩) :
    f = g
```

**`StandardModel.QuarkDoublet.gaugeRep`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L124).

> The representation of the global gauge group on the colour and weak index of the quark
> doublet, the Kronecker product of the fundamental representations of `SU(3)` and `SU(2)`
> twisted by the power `1` of the hypercharge.

```lean
noncomputable def gaugeRep :
    globalGaugeGroup.group →ₜ* (Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ)ˣ
```

## C. The matter field

**`StandardModel.QuarkDoublet.matterField`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L136).

> The quark doublet `(3, 2)_1` as a matter field of the Standard Model global gauge
> group, with its left-handed Lorentz action.

```lean
noncomputable def matterField : globalGaugeGroup.MatterField
```

**`StandardModel.QuarkDoublet.matterField_V`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L141).

> The target space of the matter field is the quark doublets.

```lean
lemma matterField_V : matterField.V = QuarkDoublet
```

**`StandardModel.QuarkDoublet.matterField_repAlgebra`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L145).

> The action of the gauge algebra of the matter field is the action matrix of its matrix
> representation.

```lean
lemma matterField_repAlgebra (c : globalGaugeGroup.lieSubalgebra) :
    matterField.repAlgebra c = MatrixRep.valEnd tensorEquiv (derivMat gaugeRep c)
```

**`StandardModel.QuarkDoublet.matterField_repLorentz`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L152).

> The Lorentz action of the matter field is that of the left-handed Weyl
> spinor.

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = MatrixRep.repLorentz tensorEquiv Fermion.LeftHandedWeyl.rep
```

**`StandardModel.QuarkDoublet.matterField_massWeight`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L157).

> The mass weight of the quark doublet.

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.QuarkDoublet.matterField_statistic`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L161).

> The quark doublet is fermionic.

```lean
lemma matterField_statistic : matterField.statistic = .fermionic
```

**`StandardModel.QuarkDoublet.matterField_lorentzContinuous`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L164).

> The Lorentz action of the matter field of the quark doublet is continuous.

```lean
lemma matterField_lorentzContinuous : matterField.LorentzContinuous
```

**`StandardModel.QuarkDoublet.matterField_gaugeLorentzCommute`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L168).

> The gauge and Lorentz representations of the matter field of the quark doublet commute.

```lean
lemma matterField_gaugeLorentzCommute : matterField.GaugeLorentzCommute
```

**`StandardModel.QuarkDoublet.matterField_repLorentz_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L172).

> The Lorentz action of the matter field is the left-handed Lorentz action.

```lean
lemma matterField_repLorentz_eq (Λ : SL(2,ℂ)) :
    (matterField.repLorentz Λ : QuarkDoublet →ₗ[ℂ] QuarkDoublet) =
      repLorentzGroup Λ
```

## D. The action of matrices on the combined index

**`StandardModel.QuarkDoublet.valEnd_smul_kronecker`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L191).

> The action of a scaled Kronecker product of a colour matrix and a weak matrix on the
> quark doublets, through the identification `tensorEquiv`, is the action of the two matrices on the
> colour and weak factors, scaled.

```lean
lemma valEnd_smul_kronecker (z : ℂ) (A : Matrix (Fin 3) (Fin 3) ℂ)
    (B : Matrix (Fin 2) (Fin 2) ℂ) (q : QuarkDoublet) :
    MatrixRep.valEnd tensorEquiv (z • (A ⊗ₖ B)) q =
      ⟨z • TensorProduct.map (TensorProduct.map LinearMap.id A.toEuclideanLin)
        B.toEuclideanLin q.val⟩
```

## E. The action of the gauge group

**`StandardModel.QuarkDoublet.matterField_rep_gaugeGroupEquiv`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean#L220).

> The action of the gauge group on the matter field of the quark doublet,
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
- [Quark doublets](fermions-quarkdoublet-basic.md)
- [The Standard Model gauge group as a global gauge group](../part-02/gaugegroup-globalgaugegroup.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/MatterField.lean)
