---
declaration: module
origin: cited
lean: Lorentz.contrContrToMatrix, Lorentz.contrContrToMatrix_symm_expand_tmul, Lorentz.coCoToMatrix, Lorentz.coCoToMatrix_symm_expand_tmul, Lorentz.contrCoToMatrix, Lorentz.contrCoToMatrix_symm_expand_tmul, Lorentz.coContrToMatrix, Lorentz.coContrToMatrix_symm_expand_tmul
statement: formalized
proof: formalized
---

# Tensor products of two complex Lorentz vectors

The module `Physlib.Relativity.Tensors.ComplexTensor.Matrix.Pre`, [Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean): 16 declarations, 8 with a docstring.

**`Lorentz.contrContrToMatrix`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L27).

> Equivalence of `complexContr ⊗ complexContr` to `4 x 4` complex matrices.

```lean
def contrContrToMatrix : (ComplexVector ⊗[ℂ] ComplexVector) ≃ₗ[ℂ]
    Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ
```

**`Lorentz.contrContrToMatrix_symm_expand_tmul`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L35).

> Expanding `contrContrToMatrix` in terms of the standard basis.

```lean
lemma contrContrToMatrix_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) :
    contrContrToMatrix.symm M =
    ∑ i, ∑ j, M i j • (ComplexVector.basis i ⊗ₜ[ℂ] ComplexVector.basis j)
```

**`Lorentz.coCoToMatrix`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L47).

> Equivalence of `complexCo ⊗ complexCo` to `4 x 4` complex matrices.

```lean
def coCoToMatrix : (ComplexCoVector ⊗[ℂ] ComplexCoVector) ≃ₗ[ℂ]
    Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ
```

**`Lorentz.coCoToMatrix_symm_expand_tmul`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L55).

> Expanding `coCoToMatrix` in terms of the standard basis.

```lean
lemma coCoToMatrix_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) :
    coCoToMatrix.symm M =
      ∑ i, ∑ j, M i j • (ComplexCoVector.basis i ⊗ₜ[ℂ] ComplexCoVector.basis j)
```

**`Lorentz.contrCoToMatrix`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L66).

> Equivalence of `complexContr ⊗ complexCo` to `4 x 4` complex matrices.

```lean
def contrCoToMatrix : (ComplexVector ⊗[ℂ] ComplexCoVector) ≃ₗ[ℂ]
    Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ
```

**`Lorentz.contrCoToMatrix_symm_expand_tmul`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L74).

> Expansion of `contrCoToMatrix` in terms of the standard basis.

```lean
lemma contrCoToMatrix_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) :
    contrCoToMatrix.symm M =
      ∑ i, ∑ j, M i j • (ComplexVector.basis i ⊗ₜ[ℂ] ComplexCoVector.basis j)
```

**`Lorentz.coContrToMatrix`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L86).

> Equivalence of `complexCo ⊗ complexContr` to `4 x 4` complex matrices.

```lean
def coContrToMatrix : (ComplexCoVector ⊗[ℂ] ComplexVector) ≃ₗ[ℂ]
    Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ
```

**`Lorentz.coContrToMatrix_symm_expand_tmul`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L94).

> Expansion of `coContrToMatrix` in terms of the standard basis.

```lean
lemma coContrToMatrix_symm_expand_tmul (M : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) :
    coContrToMatrix.symm M =
      ∑ i, ∑ j, M i j • (ComplexCoVector.basis i ⊗ₜ[ℂ] ComplexVector.basis j)
```

## Group actions

**`Lorentz.contrContrToMatrix_ρ`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L112).

```lean
lemma contrContrToMatrix_ρ (v : (ComplexVector ⊗[ℂ] ComplexVector)) (M : SL(2,ℂ)) :
    contrContrToMatrix (TensorProduct.map (ComplexVector.SL2CRep M) (ComplexVector.SL2CRep M) v) =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M)) * contrContrToMatrix v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))ᵀ
```

**`Lorentz.coCoToMatrix_ρ`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L154).

```lean
lemma coCoToMatrix_ρ (v : (ComplexCoVector ⊗[ℂ] ComplexCoVector)) (M : SL(2,ℂ)) :
    coCoToMatrix (TensorProduct.map (ComplexCoVector.SL2CRep M) (ComplexCoVector.SL2CRep M) v) =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ * coCoToMatrix v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹
```

**`Lorentz.contrCoToMatrix_ρ`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L198).

```lean
lemma contrCoToMatrix_ρ (v : (ComplexVector ⊗[ℂ] ComplexCoVector)) (M : SL(2,ℂ)) :
    contrCoToMatrix (TensorProduct.map (ComplexVector.SL2CRep M) (ComplexCoVector.SL2CRep M) v) =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M)) * contrCoToMatrix v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹
```

**`Lorentz.coContrToMatrix_ρ`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L240).

```lean
lemma coContrToMatrix_ρ (v : (ComplexCoVector ⊗[ℂ] ComplexVector)) (M : SL(2,ℂ)) :
    coContrToMatrix (TensorProduct.map (ComplexCoVector.SL2CRep M) (ComplexVector.SL2CRep M) v) =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ * coContrToMatrix v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))ᵀ
```

## The symm version of the group actions.

**`Lorentz.contrContrToMatrix_ρ_symm`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L288).

```lean
lemma contrContrToMatrix_ρ_symm (v : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (ComplexVector.SL2CRep M) (ComplexVector.SL2CRep M)
      (contrContrToMatrix.symm v) =
    contrContrToMatrix.symm ((LorentzGroup.toComplex (SL2C.toLorentzGroup M)) * v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))ᵀ)
```

**`Lorentz.coCoToMatrix_ρ_symm`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L297).

```lean
lemma coCoToMatrix_ρ_symm (v : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (ComplexCoVector.SL2CRep M) (ComplexCoVector.SL2CRep M)
      (coCoToMatrix.symm v) =
    coCoToMatrix.symm ((LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ * v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹)
```

**`Lorentz.contrCoToMatrix_ρ_symm`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L306).

```lean
lemma contrCoToMatrix_ρ_symm (v : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (ComplexVector.SL2CRep M) (ComplexCoVector.SL2CRep M)
      (contrCoToMatrix.symm v) =
    contrCoToMatrix.symm ((LorentzGroup.toComplex (SL2C.toLorentzGroup M)) * v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹)
```

**`Lorentz.coContrToMatrix_ρ_symm`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean#L315).

```lean
lemma coContrToMatrix_ρ_symm (v : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (ComplexCoVector.SL2CRep M) (ComplexVector.SL2CRep M)
      (coContrToMatrix.symm v) =
    coContrToMatrix.symm ((LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ * v *
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))ᵀ)
```

## Depends on

- [Complex Lorentz vectors](../part-02/complextensor-vector-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Matrix/Pre.lean)
