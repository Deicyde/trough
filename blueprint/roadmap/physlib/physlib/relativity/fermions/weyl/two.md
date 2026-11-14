---
declaration: module
origin: cited
lean: Fermion.leftLeftToMatrix, Fermion.leftLeftToMatrix_symm_expand_tmul, Fermion.dualLeftdualLeftToMatrix, Fermion.dualLeftdualLeftToMatrix_symm_expand_tmul, Fermion.leftDualLeftToMatrix, Fermion.leftDualLeftToMatrix_symm_expand_tmul, Fermion.dualLeftLeftToMatrix, Fermion.dualLeftLeftToMatrix_symm_expand_tmul
statement: formalized
proof: formalized
---

# Tensor product of two Weyl fermion

The module `Physlib.Relativity.Fermions.Weyl.Two`, [Physlib/Relativity/Fermions/Weyl/Two.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean): 42 declarations, 28 with a docstring; 1 private, not shown.

## Equivalences to matrices.

**`Fermion.leftLeftToMatrix`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L37).

> Equivalence of `leftHanded ⊗ leftHanded` to `2 x 2` complex matrices.

```lean
def leftLeftToMatrix : (LeftHandedWeyl ⊗[ℂ] LeftHandedWeyl) ≃ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.leftLeftToMatrix_symm_expand_tmul`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L44).

> Expanding `leftLeftToMatrix` in terms of the standard basis.

```lean
lemma leftLeftToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    leftLeftToMatrix.symm M = ∑ i, ∑ j, M i j •
      (LeftHandedWeyl.basis i ⊗ₜ[ℂ] LeftHandedWeyl.basis j)
```

**`Fermion.dualLeftdualLeftToMatrix`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L56).

> Equivalence of `dualLeftHanded ⊗ dualLeftHanded` to `2 x 2` complex matrices.

```lean
def dualLeftdualLeftToMatrix : (DualLeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.dualLeftdualLeftToMatrix_symm_expand_tmul`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L64).

> Expanding `dualLeftdualLeftToMatrix` in terms of the standard basis.

```lean
lemma dualLeftdualLeftToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    dualLeftdualLeftToMatrix.symm M = ∑ i, ∑ j, M i j •
      (DualLeftHandedWeyl.basis i ⊗ₜ[ℂ] DualLeftHandedWeyl.basis j)
```

**`Fermion.leftDualLeftToMatrix`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L77).

> Equivalence of `leftHanded ⊗ dualLeftHanded` to `2 x 2` complex matrices.

```lean
def leftDualLeftToMatrix : (LeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.leftDualLeftToMatrix_symm_expand_tmul`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L85).

> Expanding `leftDualLeftToMatrix` in terms of the standard basis.

```lean
lemma leftDualLeftToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    leftDualLeftToMatrix.symm M = ∑ i, ∑ j, M i j •
      (LeftHandedWeyl.basis i ⊗ₜ[ℂ] DualLeftHandedWeyl.basis j)
```

**`Fermion.dualLeftLeftToMatrix`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L97).

> Equivalence of `dualLeftHanded ⊗ leftHanded` to `2 x 2` complex matrices.

```lean
def dualLeftLeftToMatrix : (DualLeftHandedWeyl ⊗[ℂ] LeftHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.dualLeftLeftToMatrix_symm_expand_tmul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L105).

> Expanding `dualLeftLeftToMatrix` in terms of the standard basis.

```lean
lemma dualLeftLeftToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    dualLeftLeftToMatrix.symm M = ∑ i, ∑ j, M i j •
      (DualLeftHandedWeyl.basis i ⊗ₜ[ℂ] LeftHandedWeyl.basis j)
```

**`Fermion.rightRightToMatrix`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L117).

> Equivalence of `rightHanded ⊗ rightHanded` to `2 x 2` complex matrices.

```lean
def rightRightToMatrix : (RightHandedWeyl ⊗[ℂ] RightHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.rightRightToMatrix_symm_expand_tmul`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L125).

> Expanding `rightRightToMatrix` in terms of the standard basis.

```lean
lemma rightRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    rightRightToMatrix.symm M = ∑ i, ∑ j, M i j •
      (RightHandedWeyl.basis i ⊗ₜ[ℂ] RightHandedWeyl.basis j)
```

**`Fermion.dualRightDualRightToMatrix`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L137).

> Equivalence of `dualRightHanded ⊗ dualRightHanded` to `2 x 2` complex matrices.

```lean
def dualRightDualRightToMatrix : (DualRightHandedWeyl ⊗[ℂ] DualRightHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.dualRightDualRightToMatrix_symm_expand_tmul`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L145).

> Expanding `dualRightDualRightToMatrix` in terms of the standard basis.

```lean
lemma dualRightDualRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    dualRightDualRightToMatrix.symm M =
    ∑ i, ∑ j, M i j • (DualRightHandedWeyl.basis i ⊗ₜ[ℂ] DualRightHandedWeyl.basis j)
```

**`Fermion.rightDualRightToMatrix`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L158).

> Equivalence of `rightHanded ⊗ dualRightHanded` to `2 x 2` complex matrices.

```lean
def rightDualRightToMatrix : (RightHandedWeyl ⊗[ℂ] DualRightHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.rightDualRightToMatrix_symm_expand_tmul`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L166).

> Expanding `rightDualRightToMatrix` in terms of the standard basis.

```lean
lemma rightDualRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    rightDualRightToMatrix.symm M = ∑ i, ∑ j, M i j •
      (RightHandedWeyl.basis i ⊗ₜ[ℂ] DualRightHandedWeyl.basis j)
```

**`Fermion.dualRightRightToMatrix`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L178).

> Equivalence of `dualRightHanded ⊗ rightHanded` to `2 x 2` complex matrices.

```lean
def dualRightRightToMatrix : (DualRightHandedWeyl ⊗[ℂ] RightHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.dualRightRightToMatrix_symm_expand_tmul`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L186).

> Expanding `dualRightRightToMatrix` in terms of the standard basis.

```lean
lemma dualRightRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    dualRightRightToMatrix.symm M = ∑ i, ∑ j, M i j •
      (DualRightHandedWeyl.basis i ⊗ₜ[ℂ] RightHandedWeyl.basis j)
```

**`Fermion.dualLeftDualRightToMatrix`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L198).

> Equivalence of `dualLeftHanded ⊗ dualRightHanded` to `2 x 2` complex matrices.

```lean
def dualLeftDualRightToMatrix : (DualLeftHandedWeyl ⊗[ℂ] DualRightHandedWeyl) ≃ₗ[ℂ]
    Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.dualLeftDualRightToMatrix_symm_expand_tmul`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L206).

> Expanding `dualLeftDualRightToMatrix` in terms of the standard basis.

```lean
lemma dualLeftDualRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    dualLeftDualRightToMatrix.symm M = ∑ i, ∑ j, M i j •
      (DualLeftHandedWeyl.basis i ⊗ₜ[ℂ] DualRightHandedWeyl.basis j)
```

**`Fermion.leftRightToMatrix`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L219).

> Equivalence of `leftHanded ⊗ rightHanded` to `2 x 2` complex matrices.

```lean
def leftRightToMatrix : (LeftHandedWeyl ⊗[ℂ] RightHandedWeyl) ≃ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.leftRightToMatrix_symm_expand_tmul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L226).

> Expanding `leftRightToMatrix` in terms of the standard basis.

```lean
lemma leftRightToMatrix_symm_expand_tmul (M : Matrix (Fin 2) (Fin 2) ℂ) :
    leftRightToMatrix.symm M = ∑ i, ∑ j, M i j •
      (LeftHandedWeyl.basis i ⊗ₜ[ℂ] RightHandedWeyl.basis j)
```

## Group actions

**`Fermion.leftLeftToMatrix_ρ`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L251).

> The group action of `SL(2,ℂ)` on `leftHanded ⊗ leftHanded` is equivalent to
> `M.1 * leftLeftToMatrix v * (M.1)ᵀ`.

```lean
lemma leftLeftToMatrix_ρ (v : (LeftHandedWeyl ⊗[ℂ] LeftHandedWeyl)) (M : SL(2,ℂ)) :
    leftLeftToMatrix (TensorProduct.map (LeftHandedWeyl.rep M) (LeftHandedWeyl.rep M) v) =
    M.1 * leftLeftToMatrix v * (M.1)ᵀ
```

**`Fermion.dualLeftdualLeftToMatrix_ρ`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L297).

> The group action of `SL(2,ℂ)` on `dualLeftHanded ⊗ dualLeftHanded` is equivalent to
> `(M.1⁻¹)ᵀ * leftLeftToMatrix v * (M.1⁻¹)`.

```lean
lemma dualLeftdualLeftToMatrix_ρ (v : (DualLeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl)) (M : SL(2,ℂ)) :
    dualLeftdualLeftToMatrix (TensorProduct.map (DualLeftHandedWeyl.rep M)
      (DualLeftHandedWeyl.rep M) v) =
    (M.1⁻¹)ᵀ * dualLeftdualLeftToMatrix v * (M.1⁻¹)
```

**`Fermion.leftDualLeftToMatrix_ρ`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L345).

> The group action of `SL(2,ℂ)` on `leftHanded ⊗ dualLeftHanded` is equivalent to
> `M.1 * leftDualLeftToMatrix v * (M.1⁻¹)`.

```lean
lemma leftDualLeftToMatrix_ρ (v : (LeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl)) (M : SL(2,ℂ)) :
    leftDualLeftToMatrix (TensorProduct.map (LeftHandedWeyl.rep M) (DualLeftHandedWeyl.rep M) v) =
    M.1 * leftDualLeftToMatrix v * (M.1⁻¹)
```

**`Fermion.dualLeftLeftToMatrix_ρ`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L389).

> The group action of `SL(2,ℂ)` on `dualLeftHanded ⊗ leftHanded` is equivalent to
> `(M.1⁻¹)ᵀ * leftDualLeftToMatrix v * (M.1)ᵀ`.

```lean
lemma dualLeftLeftToMatrix_ρ (v : (DualLeftHandedWeyl ⊗[ℂ] LeftHandedWeyl)) (M : SL(2,ℂ)) :
    dualLeftLeftToMatrix (TensorProduct.map (DualLeftHandedWeyl.rep M) (LeftHandedWeyl.rep M) v) =
    (M.1⁻¹)ᵀ * dualLeftLeftToMatrix v * (M.1)ᵀ
```

**`Fermion.rightRightToMatrix_ρ`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L434).

> The group action of `SL(2,ℂ)` on `rightHanded ⊗ rightHanded` is equivalent to
> `(M.1.map star) * rightRightToMatrix v * ((M.1.map star))ᵀ`.

```lean
lemma rightRightToMatrix_ρ (v : (RightHandedWeyl ⊗[ℂ] RightHandedWeyl)) (M : SL(2,ℂ)) :
    rightRightToMatrix (TensorProduct.map (RightHandedWeyl.rep M) (RightHandedWeyl.rep M) v) =
    (M.1.map star) * rightRightToMatrix v * ((M.1.map star))ᵀ
```

**`Fermion.dualRightDualRightToMatrix_ρ`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L479).

> The group action of `SL(2,ℂ)` on `dualRightHanded ⊗ dualRightHanded` is equivalent to
> `((M.1⁻¹).conjTranspose * rightRightToMatrix v * (((M.1⁻¹).conjTranspose)ᵀ`.

```lean
lemma dualRightDualRightToMatrix_ρ (v : (DualRightHandedWeyl ⊗[ℂ] DualRightHandedWeyl))
    (M : SL(2,ℂ)) :
    dualRightDualRightToMatrix (TensorProduct.map (DualRightHandedWeyl.rep M)
      (DualRightHandedWeyl.rep M) v) =
    ((M.1⁻¹).conjTranspose) * dualRightDualRightToMatrix v * (((M.1⁻¹).conjTranspose)ᵀ)
```

**`Fermion.rightDualRightToMatrix_ρ`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L527).

> The group action of `SL(2,ℂ)` on `rightHanded ⊗ dualRightHanded` is equivalent to
> `(M.1.map star) * rightDualRightToMatrix v * (((M.1⁻¹).conjTranspose)ᵀ`.

```lean
lemma rightDualRightToMatrix_ρ (v : (RightHandedWeyl ⊗[ℂ] DualRightHandedWeyl)) (M : SL(2,ℂ)) :
    rightDualRightToMatrix (TensorProduct.map (RightHandedWeyl.rep M)
      (DualRightHandedWeyl.rep M) v) =
    (M.1.map star) * rightDualRightToMatrix v * (((M.1⁻¹).conjTranspose)ᵀ)
```

**`Fermion.dualRightRightToMatrix_ρ`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L574).

> The group action of `SL(2,ℂ)` on `dualRightHanded ⊗ rightHanded` is equivalent to
> `((M.1⁻¹).conjTranspose * rightDualRightToMatrix v * ((M.1.map star)).ᵀ`.

```lean
lemma dualRightRightToMatrix_ρ (v : (DualRightHandedWeyl ⊗[ℂ] RightHandedWeyl)) (M : SL(2,ℂ)) :
    dualRightRightToMatrix (TensorProduct.map (DualRightHandedWeyl.rep M)
      (RightHandedWeyl.rep M) v) =
    ((M.1⁻¹).conjTranspose) * dualRightRightToMatrix v * (M.1.map star)ᵀ
```

**`Fermion.dualLeftDualRightToMatrix_ρ`**, a lemma, [line 620](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L620).

```lean
lemma dualLeftDualRightToMatrix_ρ (v : (DualLeftHandedWeyl ⊗[ℂ] DualRightHandedWeyl))
    (M : SL(2,ℂ)) :
    dualLeftDualRightToMatrix (TensorProduct.map (DualLeftHandedWeyl.rep M)
      (DualRightHandedWeyl.rep M) v) =
    (M.1⁻¹)ᵀ * dualLeftDualRightToMatrix v * ((M.1⁻¹).conjTranspose)ᵀ
```

**`Fermion.leftRightToMatrix_ρ`**, a lemma, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L666).

```lean
lemma leftRightToMatrix_ρ (v : (LeftHandedWeyl ⊗[ℂ] RightHandedWeyl)) (M : SL(2,ℂ)) :
    leftRightToMatrix (TensorProduct.map (LeftHandedWeyl.rep M) (RightHandedWeyl.rep M) v) =
    M.1 * leftRightToMatrix v * (M.1)ᴴ
```

## The symm version of the group actions.

**`Fermion.leftLeftToMatrix_ρ_symm`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L715).

```lean
lemma leftLeftToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (LeftHandedWeyl.rep M) (leftLeftToMatrix.symm v) =
    leftLeftToMatrix.symm (M.1 * v * (M.1)ᵀ)
```

**`Fermion.dualLeftdualLeftToMatrix_ρ_symm`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L722).

```lean
lemma dualLeftdualLeftToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (DualLeftHandedWeyl.rep M) (DualLeftHandedWeyl.rep M)
      (dualLeftdualLeftToMatrix.symm v) =
    dualLeftdualLeftToMatrix.symm ((M.1⁻¹)ᵀ * v * (M.1⁻¹))
```

**`Fermion.leftDualLeftToMatrix_ρ_symm`**, a lemma, [line 730](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L730).

```lean
lemma leftDualLeftToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (DualLeftHandedWeyl.rep M)
      (leftDualLeftToMatrix.symm v) =
    leftDualLeftToMatrix.symm (M.1 * v * (M.1⁻¹))
```

**`Fermion.dualLeftLeftToMatrix_ρ_symm`**, a lemma, [line 738](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L738).

```lean
lemma dualLeftLeftToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (DualLeftHandedWeyl.rep M) (LeftHandedWeyl.rep M)
      (dualLeftLeftToMatrix.symm v) =
    dualLeftLeftToMatrix.symm ((M.1⁻¹)ᵀ * v * (M.1)ᵀ)
```

**`Fermion.rightRightToMatrix_ρ_symm`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L746).

```lean
lemma rightRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (RightHandedWeyl.rep M) (RightHandedWeyl.rep M) (rightRightToMatrix.symm v) =
    rightRightToMatrix.symm ((M.1.map star) * v * ((M.1.map star))ᵀ)
```

**`Fermion.dualRightDualRightToMatrix_ρ_symm`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L753).

```lean
lemma dualRightDualRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (DualRightHandedWeyl.rep M) (DualRightHandedWeyl.rep M)
      (dualRightDualRightToMatrix.symm v) =
    dualRightDualRightToMatrix.symm (((M.1⁻¹).conjTranspose) * v * ((M.1⁻¹).conjTranspose)ᵀ)
```

**`Fermion.rightDualRightToMatrix_ρ_symm`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L761).

```lean
lemma rightDualRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (RightHandedWeyl.rep M) (DualRightHandedWeyl.rep M)
      (rightDualRightToMatrix.symm v) =
    rightDualRightToMatrix.symm ((M.1.map star) * v * (((M.1⁻¹).conjTranspose)ᵀ))
```

**`Fermion.dualRightRightToMatrix_ρ_symm`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L769).

```lean
lemma dualRightRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (DualRightHandedWeyl.rep M) (RightHandedWeyl.rep M)
      (dualRightRightToMatrix.symm v) =
    dualRightRightToMatrix.symm (((M.1⁻¹).conjTranspose) * v * (M.1.map star)ᵀ)
```

**`Fermion.dualLeftDualRightToMatrix_ρ_symm`**, a lemma, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L777).

```lean
lemma dualLeftDualRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (DualLeftHandedWeyl.rep M) (DualRightHandedWeyl.rep M)
      (dualLeftDualRightToMatrix.symm v) =
    dualLeftDualRightToMatrix.symm ((M.1⁻¹)ᵀ * v * ((M.1⁻¹).conjTranspose)ᵀ)
```

**`Fermion.leftRightToMatrix_ρ_symm`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L785).

```lean
lemma leftRightToMatrix_ρ_symm (v : Matrix (Fin 2) (Fin 2) ℂ) (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (RightHandedWeyl.rep M) (leftRightToMatrix.symm v) =
    leftRightToMatrix.symm (M.1 * v * (M.1)ᴴ)
```

**`Fermion.dualLeftDualRightToMatrix_ρ_symm_selfAdjoint`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L794).

```lean
lemma dualLeftDualRightToMatrix_ρ_symm_selfAdjoint (v : Matrix (Fin 2) (Fin 2) ℂ)
    (hv : IsSelfAdjoint v) (M : SL(2,ℂ)) :
    TensorProduct.map (DualLeftHandedWeyl.rep M) (DualRightHandedWeyl.rep M)
      (dualLeftDualRightToMatrix.symm v) =
    dualLeftDualRightToMatrix.symm (SL2C.toSelfAdjointMap (M.transpose⁻¹) ⟨v, hv⟩)
```

**`Fermion.leftRightToMatrix_ρ_symm_selfAdjoint`**, a lemma, [line 812](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean#L812).

```lean
lemma leftRightToMatrix_ρ_symm_selfAdjoint (v : Matrix (Fin 2) (Fin 2) ℂ)
    (hv : IsSelfAdjoint v) (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (RightHandedWeyl.rep M) (leftRightToMatrix.symm v) =
    leftRightToMatrix.symm (SL2C.toSelfAdjointMap M ⟨v, hv⟩)
```

## Depends on

- [Dual left handed Weyl fermions](duallefthanded.md)
- [Dual right handed Weyl fermions](dualrighthanded.md)
- [Left handed Weyl fermions](lefthanded.md)
- [Right handed Weyl fermions](righthanded.md)
- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../sl2c/basic.md)

## Sources

- [Physlib/Relativity/Fermions/Weyl/Two.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Two.lean)
