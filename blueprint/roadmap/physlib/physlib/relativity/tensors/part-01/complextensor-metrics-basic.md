---
declaration: module
origin: cited
lean: complexLorentzTensor.coMetric, complexLorentzTensor.contrMetric, complexLorentzTensor.leftMetric, complexLorentzTensor.rightMetric, complexLorentzTensor.dualLeftMetric, complexLorentzTensor.dualRightMetric, complexLorentzTensor.coMetric_eq_fromConstPair, complexLorentzTensor.contrMetric_eq_fromConstPair
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic

The module `Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic`, [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean): 44 declarations, 12 with a docstring.

## Metrics as complex Lorentz tensors

## Definitions.

**`complexLorentzTensor.coMetric`**, an abbrev, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L33).

> The metric `ηᵢᵢ` as a complex Lorentz tensor.

```lean
abbrev coMetric : ℂT[.down, .down]
```

**`complexLorentzTensor.contrMetric`**, an abbrev, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L36).

> The metric `ηⁱⁱ` as a complex Lorentz tensor.

```lean
abbrev contrMetric : ℂT[.up, .up]
```

**`complexLorentzTensor.leftMetric`**, an abbrev, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L39).

> The metric `εᵃᵃ` as a complex Lorentz tensor.

```lean
abbrev leftMetric : ℂT[.upL, .upL]
```

**`complexLorentzTensor.rightMetric`**, an abbrev, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L42).

> The metric `ε^{dot a}^{dot a}` as a complex Lorentz tensor.

```lean
abbrev rightMetric : ℂT[.upR, .upR]
```

**`complexLorentzTensor.dualLeftMetric`**, an abbrev, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L45).

> The metric `εₐₐ` as a complex Lorentz tensor.

```lean
abbrev dualLeftMetric : ℂT[.downL, .downL]
```

**`complexLorentzTensor.dualRightMetric`**, an abbrev, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L48).

> The metric `ε_{dot a}_{dot a}` as a complex Lorentz tensor.

```lean
abbrev dualRightMetric : ℂT[.downR, .downR]
```

## Notation

## Other forms

### fromConstPair

**`complexLorentzTensor.coMetric_eq_fromConstPair`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L87).

```lean
lemma coMetric_eq_fromConstPair : η' = fromConstPair (S := complexLorentzTensor)
    (c1 := .down) (c2 := .down) Lorentz.ComplexCoVector.metric
```

**`complexLorentzTensor.contrMetric_eq_fromConstPair`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L92).

```lean
lemma contrMetric_eq_fromConstPair : η = fromConstPair (S := complexLorentzTensor)
    (c1 := .up) (c2 := .up) Lorentz.ComplexVector.metric
```

**`complexLorentzTensor.leftMetric_eq_fromConstPair`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L97).

```lean
lemma leftMetric_eq_fromConstPair : εL = fromConstPair Fermion.LeftHandedWeyl.metric
```

**`complexLorentzTensor.rightMetric_eq_fromConstPair`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L99).

```lean
lemma rightMetric_eq_fromConstPair : εR = fromConstPair Fermion.RightHandedWeyl.metric
```

**`complexLorentzTensor.dualLeftMetric_eq_fromConstPair`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L101).

```lean
lemma dualLeftMetric_eq_fromConstPair : εL' = fromConstPair Fermion.DualLeftHandedWeyl.metric
```

**`complexLorentzTensor.dualRightMetric_eq_fromConstPair`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L103).

```lean
lemma dualRightMetric_eq_fromConstPair :
    εR' = fromConstPair Fermion.DualRightHandedWeyl.metric
```

### fromPairT

**`complexLorentzTensor.coMetric_eq_fromPairT`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L112).

```lean
lemma coMetric_eq_fromPairT : η' = fromPairT (Lorentz.ComplexCoVector.metricVal)
```

**`complexLorentzTensor.contrMetric_eq_fromPairT`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L117).

```lean
lemma contrMetric_eq_fromPairT : η = fromPairT (Lorentz.ComplexVector.metricVal)
```

**`complexLorentzTensor.leftMetric_eq_fromPairT`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L122).

```lean
lemma leftMetric_eq_fromPairT : εL = fromPairT (Fermion.LeftHandedWeyl.metricVal)
```

**`complexLorentzTensor.rightMetric_eq_fromPairT`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L127).

```lean
lemma rightMetric_eq_fromPairT : εR = fromPairT (Fermion.RightHandedWeyl.metricVal)
```

**`complexLorentzTensor.dualLeftMetric_eq_fromPairT`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L132).

```lean
lemma dualLeftMetric_eq_fromPairT : εL' = fromPairT (Fermion.DualLeftHandedWeyl.metricVal)
```

**`complexLorentzTensor.dualRightMetric_eq_fromPairT`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L137).

```lean
lemma dualRightMetric_eq_fromPairT : εR' = fromPairT (Fermion.DualRightHandedWeyl.metricVal)
```

### ComplexCoVector.basis etc.

**`complexLorentzTensor.coMetric_eq_complexCoVector_basis`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L149).

```lean
lemma coMetric_eq_complexCoVector_basis : η' =
    fromPairT (ComplexCoVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inl 0))
    - fromPairT (ComplexCoVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 0))
    - fromPairT (ComplexCoVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 1))
    - fromPairT (ComplexCoVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 2))
```

**`complexLorentzTensor.coMetric_eq_complexCoVector_basisFin4`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L158).

```lean
lemma coMetric_eq_complexCoVector_basisFin4 : η' =
    fromPairT (ComplexCoVector.basisFin4 0 ⊗ₜ[ℂ] ComplexCoVector.basisFin4 0)
    - fromPairT (ComplexCoVector.basisFin4 1 ⊗ₜ[ℂ] ComplexCoVector.basisFin4 1)
    - fromPairT (ComplexCoVector.basisFin4 2 ⊗ₜ[ℂ] ComplexCoVector.basisFin4 2)
    - fromPairT (ComplexCoVector.basisFin4 3 ⊗ₜ[ℂ] ComplexCoVector.basisFin4 3)
```

**`complexLorentzTensor.contrMetric_eq_complexVector_basis`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L168).

```lean
lemma contrMetric_eq_complexVector_basis : η =
    fromPairT (ComplexVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inl 0))
    - fromPairT (ComplexVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 0))
    - fromPairT (ComplexVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 1))
    - fromPairT (ComplexVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 2))
```

**`complexLorentzTensor.contrMetric_eq_complexVector_basisFin4`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L177).

```lean
lemma contrMetric_eq_complexVector_basisFin4 : η =
    fromPairT (ComplexVector.basisFin4 0 ⊗ₜ[ℂ] ComplexVector.basisFin4 0)
    - fromPairT (ComplexVector.basisFin4 1 ⊗ₜ[ℂ] ComplexVector.basisFin4 1)
    - fromPairT (ComplexVector.basisFin4 2 ⊗ₜ[ℂ] ComplexVector.basisFin4 2)
    - fromPairT (ComplexVector.basisFin4 3 ⊗ₜ[ℂ] ComplexVector.basisFin4 3)
```

**`complexLorentzTensor.leftMetric_eq_leftHandedWeyl_basis`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L187).

```lean
lemma leftMetric_eq_leftHandedWeyl_basis : εL =
    - fromPairT (LeftHandedWeyl.basis 0 ⊗ₜ[ℂ] LeftHandedWeyl.basis 1)
    + fromPairT (LeftHandedWeyl.basis 1 ⊗ₜ[ℂ] LeftHandedWeyl.basis 0)
```

**`complexLorentzTensor.dualLeftMetric_eq_dualLeftHandedWeyl_basis`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L194).

```lean
lemma dualLeftMetric_eq_dualLeftHandedWeyl_basis : εL' =
    fromPairT (DualLeftHandedWeyl.basis 0 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 1)
    - fromPairT (DualLeftHandedWeyl.basis 1 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 0)
```

**`complexLorentzTensor.rightMetric_eq_rightHandedWeyl_basis`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L201).

```lean
lemma rightMetric_eq_rightHandedWeyl_basis : εR =
    - fromPairT (RightHandedWeyl.basis 0 ⊗ₜ[ℂ] RightHandedWeyl.basis 1)
    + fromPairT (RightHandedWeyl.basis 1 ⊗ₜ[ℂ] RightHandedWeyl.basis 0)
```

**`complexLorentzTensor.dualRightMetric_eq_dualRightHandedWeyl_basis`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L208).

```lean
lemma dualRightMetric_eq_dualRightHandedWeyl_basis : εR' =
    fromPairT (DualRightHandedWeyl.basis 0 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 1)
    - fromPairT (DualRightHandedWeyl.basis 1 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 0)
```

### basis

**`complexLorentzTensor.coMetric_eq_basis`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L221).

```lean
lemma coMetric_eq_basis : η' =
    (Tensor.basis (S := complexLorentzTensor) ![Color.down, Color.down]
      (fun | 0 => (Sum.inl 0 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inl 0 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.down, Color.down]
      (fun | 0 => (Sum.inr 0 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 0 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.down, Color.down]
      (fun | 0 => (Sum.inr 1 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 1 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.down, Color.down]
      (fun | 0 => (Sum.inr 2 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 2 : Fin 1 ⊕ Fin 3)))
```

**`complexLorentzTensor.contrMetric_eq_basis`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L254).

```lean
lemma contrMetric_eq_basis : η =
    (Tensor.basis (S := complexLorentzTensor) ![Color.up, Color.up]
      (fun | 0 => (Sum.inl 0 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inl 0 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.up, Color.up]
      (fun | 0 => (Sum.inr 0 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 0 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.up, Color.up]
      (fun | 0 => (Sum.inr 1 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 1 : Fin 1 ⊕ Fin 3)))
    - (Tensor.basis (S := complexLorentzTensor) ![Color.up, Color.up]
      (fun | 0 => (Sum.inr 2 : Fin 1 ⊕ Fin 3) | 1 => (Sum.inr 2 : Fin 1 ⊕ Fin 3)))
```

**`complexLorentzTensor.leftMetric_eq_basis`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L287).

```lean
lemma leftMetric_eq_basis : εL =
    - (Tensor.basis (S := complexLorentzTensor) ![Color.upL, Color.upL]
      (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)))
    + (Tensor.basis (S := complexLorentzTensor)
      ![Color.upL, Color.upL] (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)))
```

**`complexLorentzTensor.dualLeftMetric_eq_basis`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L306).

```lean
lemma dualLeftMetric_eq_basis : εL' =
    (Tensor.basis (S := complexLorentzTensor) ![Color.downL, Color.downL]
      (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)))
    - (Tensor.basis (S := complexLorentzTensor)
      ![Color.downL, Color.downL] (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)))
```

**`complexLorentzTensor.rightMetric_eq_basis`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L325).

```lean
lemma rightMetric_eq_basis : εR =
    - (Tensor.basis (S := complexLorentzTensor) ![Color.upR, Color.upR]
      (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)))
    + (Tensor.basis (S := complexLorentzTensor)
      ![Color.upR, Color.upR] (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)))
```

**`complexLorentzTensor.dualRightMetric_eq_basis`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L344).

```lean
lemma dualRightMetric_eq_basis : εR' =
    (Tensor.basis (S := complexLorentzTensor)
      ![Color.downR, Color.downR] (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)))
    - (Tensor.basis (S := complexLorentzTensor)
      ![Color.downR, Color.downR] (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)))
```

### ofGaussianInt

**`complexLorentzTensor.coMetric_eq_ofGaussianInt`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L369).

```lean
lemma coMetric_eq_ofGaussianInt : η' = ofGaussianInt fun f =>
    if f 0 = (Sum.inl 0 : Fin 1 ⊕ Fin 3) ∧ f 1 = (Sum.inl 0 : Fin 1 ⊕ Fin 3) then 1 else
    if f 0 = f 1 then - 1 else 0
```

**`complexLorentzTensor.contrMetric_eq_ofGaussianInt`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L381).

```lean
lemma contrMetric_eq_ofGaussianInt : η = ofGaussianInt fun f =>
    if f 0 = (Sum.inl 0 : Fin 1 ⊕ Fin 3) ∧ f 1 = (Sum.inl 0 : Fin 1 ⊕ Fin 3) then 1 else
    if f 0 = f 1 then - 1 else 0
```

**`complexLorentzTensor.leftMetric_eq_ofGaussianInt`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L392).

```lean
lemma leftMetric_eq_ofGaussianInt : εL =
    ofGaussianInt (c := ![Color.upL, Color.upL]) fun f =>
    if f = (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)) then - 1 else
    if f = (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)) then 1 else 0
```

**`complexLorentzTensor.dualLeftMetric_eq_ofGaussianInt`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L403).

```lean
lemma dualLeftMetric_eq_ofGaussianInt : εL' =
    ofGaussianInt (c := ![Color.downL, Color.downL]) fun f =>
    if f = (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)) then 1 else
    if f = (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)) then - 1 else 0
```

**`complexLorentzTensor.rightMetric_eq_ofGaussianInt`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L414).

```lean
lemma rightMetric_eq_ofGaussianInt : εR =
    ofGaussianInt (c := ![Color.upR, Color.upR]) fun f =>
    if f = (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)) then - 1 else
    if f = (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)) then 1 else 0
```

**`complexLorentzTensor.dualRightMetric_eq_ofGaussianInt`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L425).

```lean
lemma dualRightMetric_eq_ofGaussianInt : εR' =
    ofGaussianInt (c := ![Color.downR, Color.downR]) fun f =>
    if f = (fun | 0 => (0 : Fin 2) | 1 => (1 : Fin 2)) then 1 else
    if f = (fun | 0 => (1 : Fin 2) | 1 => (0 : Fin 2)) then - 1 else 0
```

## Group actions

**`complexLorentzTensor.actionT_coMetric`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L445).

> The tensor `coMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_coMetric (g : SL(2,ℂ)) : g • η' = η'
```

**`complexLorentzTensor.actionT_contrMetric`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L449).

> The tensor `contrMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_contrMetric (g : SL(2,ℂ)) : g • η = η
```

**`complexLorentzTensor.actionT_leftMetric`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L453).

> The tensor `leftMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_leftMetric (g : SL(2,ℂ)) : g • εL = εL
```

**`complexLorentzTensor.actionT_rightMetric`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L457).

> The tensor `rightMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_rightMetric (g : SL(2,ℂ)) : g • εR = εR
```

**`complexLorentzTensor.actionT_dualLeftMetric`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L461).

> The tensor `dualLeftMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_dualLeftMetric (g : SL(2,ℂ)) : g • εL' = εL'
```

**`complexLorentzTensor.actionT_dualRightMetric`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L465).

> The tensor `dualRightMetric` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_dualRightMetric (g : SL(2,ℂ)) : g • εR' = εR'
```

## Depends on

- [Complex Lorentz tensors with Gaussian integer components](complextensor-ofgaussianint.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean)
