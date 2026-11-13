---
declaration: module
origin: cited
lean: HermitianMat.eigenvalues_conj, Matrix.neg_unitary_val, Matrix.star_kron, Matrix.kron_unitary, Matrix.unitary_kron, Matrix.unitary_kron_apply, Matrix.unitary_kron_one_one, Matrix.unitary_row_sum_norm_sq
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Unitary

The module `QuantumInfo.ForMathlib.HermitianMat.Unitary`, [QuantumInfo/ForMathlib/HermitianMat/Unitary.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean): 12 declarations, 3 with a docstring, 1 listed as significant.

**`Matrix.neg_unitary_val`**, a lemma, [line 21](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L21).

```lean
lemma neg_unitary_val (u : 𝐔[α]) : (-u).val = -u
```

**`Matrix.star_kron`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L27).

```lean
lemma star_kron (a : Matrix α α ℂ) (b : Matrix β β ℂ) : star (a ⊗ₖ b) = (star a) ⊗ₖ (star b)
```

**`Matrix.kron_unitary`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L32).

```lean
lemma kron_unitary (a : 𝐔[α]) (b : 𝐔[β]) : a.val ⊗ₖ b.val ∈ 𝐔[α × β]
```

**`Matrix.unitary_kron`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L36).

```lean
def unitary_kron (a : 𝐔[α]) (b : 𝐔[β]) : 𝐔[α × β]
```

**`Matrix.unitary_kron_apply`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L42).

```lean
lemma unitary_kron_apply (a : 𝐔[α]) (b : 𝐔[β]) (i₁ i₂ : α) (j₁ j₂ : β) :
    (a ⊗ᵤ b) (i₁, j₁) (i₂, j₂) = (a i₁ i₂) * (b j₁ j₂)
```

**`Matrix.unitary_kron_one_one`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L47).

```lean
lemma unitary_kron_one_one : (1 : 𝐔[α]) ⊗ᵤ (1 : 𝐔[β]) = (1 : 𝐔[α × β])
```

**`Matrix.unitary_row_sum_norm_sq`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L57).

> For a unitary matrix C, the row sums of ‖C i j‖^2 equal 1.

```lean
lemma unitary_row_sum_norm_sq (C : Matrix d d ℂ) (hC : C * C.conjTranspose = 1) (i : d) :
    ∑ j, ‖C i j‖ ^ 2 = 1
```

**`Matrix.unitary_col_sum_norm_sq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L67).

> For a unitary matrix C, the column sums of ‖C i j‖^2 equal 1.

```lean
lemma unitary_col_sum_norm_sq (C : Matrix d d ℂ) (hC : C.conjTranspose * C = 1) (j : d) :
    ∑ i, ‖C i j‖ ^ 2 = 1
```

**`HermitianMat.trace_conj_unitary`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L84).

```lean
lemma trace_conj_unitary : (conj U.val A).trace = A.trace
```

**`HermitianMat.le_conj_unitary`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L88).

```lean
lemma le_conj_unitary : A.conj U.val ≤ B.conj U ↔ A ≤ B
```

**`HermitianMat.inner_conj_unitary`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L98).

```lean
lemma inner_conj_unitary : ⟪A.conj U.val, B.conj U.val⟫ = ⟪A, B⟫
```

**`HermitianMat.eigenvalues_conj`**, a theorem, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean#L110). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The eigenvalues of a Hermitian matrix conjugated by a unitary matrix are the same
> as the eigenvalues of the original matrix.

```lean
theorem eigenvalues_conj : (A.conj U.val).H.eigenvalues = A.H.eigenvalues
```

## Depends on

- [Inner product of Hermitian Matrices](inner.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Unitary.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Unitary.lean)
