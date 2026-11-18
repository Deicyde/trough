---
declaration: module
origin: cited
lean: complexLorentzTensor.coContrUnit, complexLorentzTensor.contrCoUnit, complexLorentzTensor.dualLeftLeftUnit, complexLorentzTensor.leftDualLeftUnit, complexLorentzTensor.dualRightRightUnit, complexLorentzTensor.rightDualRightUnit, complexLorentzTensor.coContrUnit_eq_fromConstPair, complexLorentzTensor.contrCoUnit_eq_fromConstPair
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Units.Basic

The module `Physlib.Relativity.Tensors.ComplexTensor.Units.Basic`, [Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean): 44 declarations, 12 with a docstring.

## Unit tensors for complex Lorentz tensors

## Definitions.

**`complexLorentzTensor.coContrUnit`**, an abbrev, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L34).

> The unit `δᵢⁱ` as a complex Lorentz tensor.

```lean
abbrev coContrUnit : ℂT[.down, .up]
```

**`complexLorentzTensor.contrCoUnit`**, an abbrev, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L37).

> The unit `δⁱᵢ` as a complex Lorentz tensor.

```lean
abbrev contrCoUnit : ℂT[.up, .down]
```

**`complexLorentzTensor.dualLeftLeftUnit`**, an abbrev, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L40).

> The unit `δₐᵃ` as a complex Lorentz tensor.

```lean
abbrev dualLeftLeftUnit : ℂT[.downL, .upL]
```

**`complexLorentzTensor.leftDualLeftUnit`**, an abbrev, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L43).

> The unit `δᵃₐ` as a complex Lorentz tensor.

```lean
abbrev leftDualLeftUnit : ℂT[.upL, .downL]
```

**`complexLorentzTensor.dualRightRightUnit`**, an abbrev, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L46).

> The unit `δ_{dot a}^{dot a}` as a complex Lorentz tensor.

```lean
abbrev dualRightRightUnit : ℂT[.downR, .upR]
```

**`complexLorentzTensor.rightDualRightUnit`**, an abbrev, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L49).

> The unit `δ^{dot a}_{dot a}` as a complex Lorentz tensor.

```lean
abbrev rightDualRightUnit : ℂT[.upR, .downR]
```

## Notation

## Other forms

### fromConstPair

**`complexLorentzTensor.coContrUnit_eq_fromConstPair`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L87).

```lean
lemma coContrUnit_eq_fromConstPair : δ' = fromConstPair Lorentz.ComplexVector.unit
```

**`complexLorentzTensor.contrCoUnit_eq_fromConstPair`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L91).

```lean
lemma contrCoUnit_eq_fromConstPair : δ = fromConstPair Lorentz.ComplexCoVector.unit
```

**`complexLorentzTensor.dualLeftLeftUnit_eq_fromConstPair`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L95).

```lean
lemma dualLeftLeftUnit_eq_fromConstPair : δL' = fromConstPair Fermion.LeftHandedWeyl.unit
```

**`complexLorentzTensor.leftDualLeftUnit_eq_fromConstPair`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L99).

```lean
lemma leftDualLeftUnit_eq_fromConstPair : δL = fromConstPair Fermion.DualLeftHandedWeyl.unit
```

**`complexLorentzTensor.dualRightRightUnit_eq_fromConstPair`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L103).

```lean
lemma dualRightRightUnit_eq_fromConstPair : δR' = fromConstPair Fermion.RightHandedWeyl.unit
```

**`complexLorentzTensor.rightDualRightUnit_eq_fromConstPair`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L107).

```lean
lemma rightDualRightUnit_eq_fromConstPair :
    δR = fromConstPair Fermion.DualRightHandedWeyl.unit
```

### fromPairT

**`complexLorentzTensor.coContrUnit_eq_fromPairT`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L118).

```lean
lemma coContrUnit_eq_fromPairT : δ' = fromPairT (Lorentz.ComplexVector.unitVal)
```

**`complexLorentzTensor.contrCoUnit_eq_fromPairT`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L123).

```lean
lemma contrCoUnit_eq_fromPairT : δ = fromPairT (Lorentz.ComplexCoVector.unitVal)
```

**`complexLorentzTensor.dualLeftLeftUnit_eq_fromPairT`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L128).

```lean
lemma dualLeftLeftUnit_eq_fromPairT : δL' = fromPairT (Fermion.LeftHandedWeyl.unitVal)
```

**`complexLorentzTensor.leftDualLeftUnit_eq_fromPairT`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L133).

```lean
lemma leftDualLeftUnit_eq_fromPairT : δL = fromPairT (Fermion.DualLeftHandedWeyl.unitVal)
```

**`complexLorentzTensor.dualRightRightUnit_eq_fromPairT`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L138).

```lean
lemma dualRightRightUnit_eq_fromPairT : δR' = fromPairT (Fermion.RightHandedWeyl.unitVal)
```

**`complexLorentzTensor.rightDualRightUnit_eq_fromPairT`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L143).

```lean
lemma rightDualRightUnit_eq_fromPairT : δR = fromPairT (Fermion.DualRightHandedWeyl.unitVal)
```

### ComplexCoVector.basis etc.

**`complexLorentzTensor.coContrUnit_eq_complexCoVector_basis_complexVector_basis`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L155).

```lean
lemma coContrUnit_eq_complexCoVector_basis_complexVector_basis : δ' =
    ∑ i, fromPairT (ComplexCoVector.basis i ⊗ₜ[ℂ] ComplexVector.basis i)
```

**`complexLorentzTensor.coContrUnit_eq_complexCoVector_basisFin4_complexVector_basisFin4`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L161).

```lean
lemma coContrUnit_eq_complexCoVector_basisFin4_complexVector_basisFin4 : δ' =
    ∑ i, fromPairT (ComplexCoVector.basisFin4 i ⊗ₜ[ℂ] ComplexVector.basisFin4 i)
```

**`complexLorentzTensor.contrCoUnit_eq_complexVector_basis_complexCoVector_basis`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L168).

```lean
lemma contrCoUnit_eq_complexVector_basis_complexCoVector_basis : δ =
    ∑ i, fromPairT (ComplexVector.basis i ⊗ₜ[ℂ] ComplexCoVector.basis i)
```

**`complexLorentzTensor.contrCoUnit_eq_complexVector_basisFin4_complexCoVector_basisFin4`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L174).

```lean
lemma contrCoUnit_eq_complexVector_basisFin4_complexCoVector_basisFin4 : δ =
    ∑ i, fromPairT (ComplexVector.basisFin4 i ⊗ₜ[ℂ] ComplexCoVector.basisFin4 i)
```

**`complexLorentzTensor.dualLeftLeftUnit_eq_basis`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L181).

```lean
lemma dualLeftLeftUnit_eq_basis : δL' =
    ∑ i, fromPairT (DualLeftHandedWeyl.basis i ⊗ₜ[ℂ] LeftHandedWeyl.basis i)
```

**`complexLorentzTensor.leftDualLeftUnit_eq_basis`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L187).

```lean
lemma leftDualLeftUnit_eq_basis : δL =
    ∑ i, fromPairT (LeftHandedWeyl.basis i ⊗ₜ[ℂ] DualLeftHandedWeyl.basis i)
```

**`complexLorentzTensor.dualRightRightUnit_eq_basis`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L193).

```lean
lemma dualRightRightUnit_eq_basis : δR' =
    ∑ i, fromPairT (DualRightHandedWeyl.basis i ⊗ₜ[ℂ] RightHandedWeyl.basis i)
```

**`complexLorentzTensor.rightDualRightUnit_eq_basis`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L199).

```lean
lemma rightDualRightUnit_eq_basis : δR =
    ∑ i, fromPairT (RightHandedWeyl.basis i ⊗ₜ[ℂ] DualRightHandedWeyl.basis i)
```

### basis

**`complexLorentzTensor.coContrUnit_eq_basis`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L210).

```lean
lemma coContrUnit_eq_basis : δ' =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.down, Color.up] (fun | 0 => i | 1 => i)
```

**`complexLorentzTensor.contrCoUnit_eq_basis`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L221).

```lean
lemma contrCoUnit_eq_basis : δ =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.up, Color.down] (fun | 0 => i | 1 => i)
```

**`complexLorentzTensor.dualLeftLeftUnit_eq_tensor_basis`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L232).

```lean
lemma dualLeftLeftUnit_eq_tensor_basis : δL' =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.downL, Color.upL] (fun | 0 => i | 1 => i)
```

**`complexLorentzTensor.leftDualLeftUnit_eq_tensor_basis`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L243).

```lean
lemma leftDualLeftUnit_eq_tensor_basis : δL =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.upL, Color.downL] (fun | 0 => i | 1 => i)
```

**`complexLorentzTensor.dualRightRightUnit_eq_tensor_basis`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L254).

```lean
lemma dualRightRightUnit_eq_tensor_basis : δR' =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.downR, Color.upR] (fun | 0 => i | 1 => i)
```

**`complexLorentzTensor.rightDualRightUnit_eq_tensor_basis`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L265).

```lean
lemma rightDualRightUnit_eq_tensor_basis : δR =
    ∑ i, Tensor.basis (S := complexLorentzTensor)
      ![Color.upR, Color.downR] (fun | 0 => i | 1 => i)
```

### ofGaussianInt

**`complexLorentzTensor.coContrUnit_eq_ofGaussianInt`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L283).

```lean
lemma coContrUnit_eq_ofGaussianInt : δ' = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

**`complexLorentzTensor.contrCoUnit_eq_ofGaussianInt`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L294).

```lean
lemma contrCoUnit_eq_ofGaussianInt : δ = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

**`complexLorentzTensor.dualLeftLeftUnit_eq_ofGaussianInt`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L305).

```lean
lemma dualLeftLeftUnit_eq_ofGaussianInt : δL' = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

**`complexLorentzTensor.leftDualLeftUnit_eq_ofGaussianInt`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L316).

```lean
lemma leftDualLeftUnit_eq_ofGaussianInt : δL = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

**`complexLorentzTensor.dualRightRightUnit_eq_ofGaussianInt`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L327).

```lean
lemma dualRightRightUnit_eq_ofGaussianInt : δR' = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

**`complexLorentzTensor.rightDualRightUnit_eq_ofGaussianInt`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L338).

```lean
lemma rightDualRightUnit_eq_ofGaussianInt : δR = ofGaussianInt fun f =>
    if f 0 = f 1 then 1 else 0
```

## Group actions

**`complexLorentzTensor.actionT_coContrUnit`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L356).

> The tensor `coContrUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_coContrUnit (g : SL(2,ℂ)) : g • δ' = δ'
```

**`complexLorentzTensor.actionT_contrCoUnit`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L361).

> The tensor `contrCoUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_contrCoUnit (g : SL(2,ℂ)) : g • δ = δ
```

**`complexLorentzTensor.actionT_dualLeftLeftUnit`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L366).

> The tensor `dualLeftLeftUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_dualLeftLeftUnit (g : SL(2,ℂ)) : g • δL' = δL'
```

**`complexLorentzTensor.actionT_leftDualLeftUnit`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L371).

> The tensor `leftDualLeftUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_leftDualLeftUnit (g : SL(2,ℂ)) : g • δL = δL
```

**`complexLorentzTensor.actionT_dualRightRightUnit`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L376).

> The tensor `dualRightRightUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_dualRightRightUnit (g : SL(2,ℂ)) : g • δR' = δR'
```

**`complexLorentzTensor.actionT_rightDualRightUnit`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean#L381).

> The tensor `rightDualRightUnit` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma actionT_rightDualRightUnit (g : SL(2,ℂ)) : g • δR = δR
```

## Depends on

- [Complex Lorentz tensors with Gaussian integer components](complextensor-ofgaussianint.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Basic.lean)
