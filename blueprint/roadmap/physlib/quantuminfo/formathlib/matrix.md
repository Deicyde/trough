---
declaration: module
origin: cited
lean: Matrix.fromBlocks_gram_posSemidef, Matrix.IsHermitian.sum_eigenvalues_eq_trace, Matrix.IsHermitian.eigenvalues_zero_eq_zero, Matrix.PosSemidef.stdBasisMatrix_iff_eq, Matrix.trace_mul_kron_one_right, Matrix.trace_mul_one_kron_right, Matrix.traceRight_eq_traceLeft_reindex, Matrix.zero_rank_eq_zero
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Matrix

The module `QuantumInfo.ForMathlib.Matrix`, [QuantumInfo/ForMathlib/Matrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean): 94 declarations, 9 with a docstring, 7 listed as significant; 2 private, not shown.

**`Matrix.fromBlocks_gram_posSemidef`**, a theorem, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L29). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The block Gram matrix `[[YᴴY, YᴴX], [XᴴY, XᴴX]]` is positive semidefinite.

```lean
theorem fromBlocks_gram_posSemidef {m n k : Type*} [Fintype m] [Fintype n] [Fintype k]
    (X : Matrix k n ℂ) (Y : Matrix k m ℂ) :
    (fromBlocks (Yᴴ * Y) (Yᴴ * X) (Xᴴ * Y) (Xᴴ * X)).PosSemidef
```

**`Matrix.zero_rank_eq_zero`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L38).

```lean
lemma zero_rank_eq_zero {A : Matrix n n 𝕜} [Fintype n] (hA : A.rank = 0) : A = 0
```

**`Matrix.IsHermitian.smul_selfAdjoint`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L54).

```lean
lemma smul_selfAdjoint {c : 𝕜} (hc : _root_.IsSelfAdjoint c) : (c • A).IsHermitian
```

**`Matrix.IsHermitian.smul_im_zero`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L59).

```lean
lemma smul_im_zero {c : 𝕜} (h : RCLike.im c = 0) : (c • A).IsHermitian
```

**`Matrix.IsHermitian.smul_real`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L64).

```lean
lemma smul_real (c : ℝ) : (c • A).IsHermitian
```

**`Matrix.IsHermitian.HermitianSubspace`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L69).

```lean
def HermitianSubspace (n 𝕜 : Type*) [Fintype n] [RCLike 𝕜] : Subspace ℝ (Matrix n n 𝕜)
```

**`Matrix.IsHermitian.re_trace_eq_trace`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L83).

```lean
lemma re_trace_eq_trace : RCLike.re (A.trace) = A.trace
```

**`Matrix.IsHermitian.sum_eigenvalues_eq_trace`**, a theorem, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L89). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The sum of the eigenvalues of a Hermitian matrix is equal to its trace.

```lean
theorem sum_eigenvalues_eq_trace : ∑ i, hA.eigenvalues i = A.trace
```

**`Matrix.IsHermitian.eigenvalues_zero_eq_zero`**, a theorem, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L96). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If all eigenvalues are equal to zero, then the matrix is zero.

```lean
theorem eigenvalues_zero_eq_zero (h : ∀ i, hA.eigenvalues i = 0) : A = 0
```

**`Matrix.kroneckerMap_conjTranspose`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L112).

```lean
lemma kroneckerMap_conjTranspose : (A ⊗ₖ B)ᴴ = (Aᴴ ⊗ₖ Bᴴ)
```

**`Matrix.kroneckerMap_IsHermitian`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L120).

```lean
lemma kroneckerMap_IsHermitian : (A ⊗ₖ B).IsHermitian
```

**`Matrix.PosSemidef.trace_zero`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L139).

```lean
lemma trace_zero : A.trace = 0 → A = 0
```

**`Matrix.PosSemidef.trace_zero_iff`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L149).

```lean
lemma trace_zero_iff : A.trace = 0 ↔ A = 0
```

**`RCLike.normSq_eq_conj_mul_self`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L154).

```lean
lemma _root_.RCLike.normSq_eq_conj_mul_self {z : 𝕜} : RCLike.normSq z = conj z * z
```

**`Matrix.PosSemidef.Finsupp.sum_eq_ite`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L160).

```lean
lemma Finsupp.sum_eq_ite
      {α : Type u_1} {M : Type u_8} {N : Type u_10} [Zero M] [AddCommMonoid N] [Fintype α]
      [DecidableEq M] (f : α →₀ M) (g : α → M → N) :
    f.sum g = ∑ i, if f i ≠ 0 then g i (f i) else 0
```

**`Matrix.PosSemidef.outer_self_conj`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L172).

```lean
lemma outer_self_conj (v : n → 𝕜) : PosSemidef (vecMulVec v (conj v))
```

**`Matrix.PosSemidef.convex_cone`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L194).

```lean
lemma convex_cone {c₁ c₂ : 𝕜} (hc₁ : 0 ≤ c₁) (hc₂ : 0 ≤ c₂) : (c₁ • A + c₂ • B).PosSemidef
```

**`Matrix.PosSemidef.stdBasisMatrix_iff_eq`**, a theorem, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L200). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A standard basis matrix (with a positive entry) is positive semidefinite iff the entry is on the diagonal.

```lean
theorem stdBasisMatrix_iff_eq (i j : m) {c : 𝕜} (hc : 0 < c) : (single i j c).PosSemidef ↔ i = j
```

**`Matrix.PosSemidef.PosSemidef_kronecker`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L253).

```lean
lemma PosSemidef_kronecker : (A ⊗ₖ B).PosSemidef
```

**`Matrix.PosSemidef.zero_dotProduct_zero_iff`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L276).

```lean
lemma zero_dotProduct_zero_iff : (∀ x : m → 𝕜, 0 = star x ⬝ᵥ A.mulVec x) ↔ A = 0
```

**`Matrix.PosSemidef.pos_smul`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L288).

```lean
lemma pos_smul {c : 𝕜} (hA : (c • A).PosSemidef) (hc : 0 < c) : A.PosSemidef
```

**`Matrix.PosSemidef.zero_posSemidef_neg_posSemidef_iff`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L295).

```lean
lemma zero_posSemidef_neg_posSemidef_iff : A.PosSemidef ∧ (-A).PosSemidef ↔ A = 0
```

**`Matrix.PosDef.toLin_ker_eq_bot`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L317).

```lean
lemma toLin_ker_eq_bot (hA : A.PosDef) : LinearMap.ker A.toLin' = ⊥
```

**`Matrix.PosDef.of_toLin_ker_eq_bot`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L323).

```lean
lemma of_toLin_ker_eq_bot (hA : LinearMap.ker A.toLin' = ⊥) (hA₂ : A.PosSemidef) : A.PosDef
```

**`Matrix.PosDef.ker_range_antitone`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L326).

```lean
lemma ker_range_antitone {d : Type*} [Fintype d] [DecidableEq d] {A B : Matrix d d ℂ}
  (hA : A.IsHermitian) (hB : B.IsHermitian) :
    LinearMap.ker A.toEuclideanLin ≤ LinearMap.ker B.toEuclideanLin ↔
    LinearMap.range B.toEuclideanLin ≤ LinearMap.range A.toEuclideanLin
```

**`Matrix.PosSemidef.le_of_nonneg_imp`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L348).

```lean
lemma le_of_nonneg_imp {R : Type*} [AddCommGroup R] [PartialOrder R] [IsOrderedAddMonoid R]
    (f : Matrix n n 𝕜 →+ R) (h : ∀ A, A.PosSemidef → 0 ≤ f A) :
    (A ≤ B → f A ≤ f B)
```

**`Matrix.PosSemidef.le_of_nonneg_imp'`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L356).

```lean
lemma le_of_nonneg_imp' {R : Type*} [AddCommGroup R] [PartialOrder R] [IsOrderedAddMonoid R]
    {x y : R} (f : R →+ Matrix n n 𝕜) (h : ∀ x, 0 ≤ x → (f x).PosSemidef) :
    (x ≤ y → f x ≤ f y)
```

**`Matrix.PosSemidef.mul_mul_conjTranspose_mono`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L365).

```lean
lemma mul_mul_conjTranspose_mono (C : Matrix m n 𝕜) :
  A ≤ B → C * A * C.conjTranspose ≤ C * B * C.conjTranspose
```

**`Matrix.PosSemidef.conjTranspose_mul_mul_mono`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L376).

```lean
lemma conjTranspose_mul_mul_mono (C : Matrix n m 𝕜) :
  A ≤ B → C.conjTranspose * A * C ≤ C.conjTranspose * B * C
```

**`Matrix.PosSemidef.nonneg_iff_eigenvalue_nonneg`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L381).

```lean
lemma nonneg_iff_eigenvalue_nonneg [DecidableEq n] : 0 ≤ A ↔ ∀ x, 0 ≤ hA.eigenvalues x
```

**`Matrix.PosSemidef.diag_monotone`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L385).

```lean
lemma diag_monotone : Monotone (diag : Matrix n n 𝕜 → (n → 𝕜))
```

**`Matrix.PosSemidef.diag_mono`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L389).

```lean
lemma diag_mono : A ≤ B → ∀ i, A.diag i ≤ B.diag i
```

**`Matrix.PosSemidef.trace_monotone`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L391).

```lean
lemma trace_monotone : Monotone (@trace n 𝕜 _ _)
```

**`Matrix.PosSemidef.trace_mono`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L394).

```lean
lemma trace_mono : A ≤ B → A.trace ≤ B.trace
```

**`Matrix.PosSemidef.diagonal_monotone`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L399).

```lean
lemma diagonal_monotone : Monotone (diagonal : (n → 𝕜) → _)
```

**`Matrix.PosSemidef.diagonal_mono`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L403).

```lean
lemma diagonal_mono {d₁ d₂ : n → 𝕜} : d₁ ≤ d₂ → diagonal d₁ ≤ diagonal d₂
```

**`Matrix.PosSemidef.diagonal_le_iff`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L406).

```lean
lemma diagonal_le_iff {d₁ d₂ : n → 𝕜} : d₁ ≤ d₂ ↔ diagonal d₁ ≤ diagonal d₂
```

**`Matrix.PosSemidef.le_smul_one_of_eigenvalues_iff`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L412).

```lean
lemma le_smul_one_of_eigenvalues_iff (hA : A.IsHermitian) (c : ℝ) :
  (∀ i, hA.eigenvalues i ≤ c) ↔ A ≤ c • (1 : Matrix n n 𝕜)
```

**`Matrix.PosSemidef.smul_one_le_of_eigenvalues_iff`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L449).

```lean
lemma smul_one_le_of_eigenvalues_iff (hA : A.IsHermitian) (c : ℝ) :
  (∀ i, c ≤ hA.eigenvalues i) ↔ c • (1 : Matrix n n 𝕜) ≤ A
```

**`Matrix.traceLeft`**, a def, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L590).

```lean
def traceLeft (m : Matrix (d × d₁) (d × d₂) R) : Matrix d₁ d₂ R
```

**`Matrix.traceRight`**, a def, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L593).

```lean
def traceRight (m : Matrix (d₁ × d) (d₂ × d) R) : Matrix d₁ d₂ R
```

**`Matrix.traceLeft_trace`**, a lemma, [line 598](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L598).

```lean
lemma traceLeft_trace (A : Matrix (d₁ × d₂) (d₁ × d₂) R) : A.traceLeft.trace = A.trace
```

**`Matrix.traceRight_trace`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L604).

```lean
lemma traceRight_trace (A : Matrix (d₁ × d₂) (d₁ × d₂) R) : A.traceRight.trace = A.trace
```

**`Matrix.IsHermitian.traceLeft`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L609).

```lean
lemma IsHermitian.traceLeft {A : Matrix (d × d₁) (d × d₁) R} (hA : A.IsHermitian) : A.traceLeft.IsHermitian
```

**`Matrix.IsHermitian.traceRight`**, a lemma, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L616).

```lean
lemma IsHermitian.traceRight {A : Matrix (d₁ × d) (d₁ × d) R} (hA : A.IsHermitian) : A.traceRight.IsHermitian
```

**`Matrix.trace_mul_kron_one_right`**, a theorem, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L627). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Tr(M (A ⊗ I)) = Tr(Tr_B(M) A)`

```lean
theorem trace_mul_kron_one_right {R : Type*} [Ring R]
    (M : Matrix (dA × dB) (dA × dB) R) (A : Matrix dA dA R) :
    (M * (A ⊗ₖ (1 : Matrix dB dB R))).trace = (M.traceRight * A).trace
```

**`Matrix.trace_mul_one_kron_right`**, a theorem, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L639). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Tr(M (I ⊗ B)) = Tr(Tr_A(M) B)`

```lean
theorem trace_mul_one_kron_right {R : Type*} [Ring R]
    (M : Matrix (dA × dB) (dA × dB) R) (B : Matrix dB dB R) :
    (M * ((1 : Matrix dA dA R) ⊗ₖ B)).trace = (M.traceLeft * B).trace
```

**`Matrix.PosSemidef.traceLeft`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L652).

```lean
lemma PosSemidef.traceLeft [DecidableEq d₁] (hA : A.PosSemidef) : A.traceLeft.PosSemidef
```

**`Matrix.PosSemidef.traceRight`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L663).

```lean
lemma PosSemidef.traceRight [DecidableEq d₂] (hA : A.PosSemidef) : A.traceRight.PosSemidef
```

**`Matrix.PosDef.kron`**, a lemma, [line 681](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L681).

```lean
lemma PosDef.kron {d₁ d₂ 𝕜 : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂] [RCLike 𝕜]
    {A : Matrix d₁ d₁ 𝕜} {B : Matrix d₂ d₂ 𝕜} (hA : A.PosDef) (hB : B.PosDef) : (A ⊗ₖ B).PosDef
```

**`Matrix.PosDef.reindex`**, a lemma, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L700).

```lean
lemma PosDef.reindex {d₁ d₂ 𝕜 : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂] [RCLike 𝕜]
    {M : Matrix d₁ d₁ 𝕜} (hM : M.PosDef) (e : d₁ ≃ d₂) : (M.reindex e e).PosDef
```

**`Matrix.PosDef.reindex_iff`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L705).

```lean
lemma PosDef.reindex_iff {d₁ d₂ 𝕜 : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂] [RCLike 𝕜]
    {M : Matrix d₁ d₁ 𝕜} (e : d₁ ≃ d₂) : (M.reindex e e).PosDef ↔ M.PosDef
```

**`Matrix.PosSemidef.rsmul`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L711).

```lean
lemma PosSemidef.rsmul {n : Type*} [Fintype n] {M : Matrix n n ℂ} (hM : M.PosSemidef) {c : ℝ} (hc : 0 ≤ c) :
    (c • M).PosSemidef
```

**`Matrix.PosDef.Convex`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L721).

```lean
lemma PosDef.Convex {n 𝕜 : Type*} [Fintype n] [RCLike 𝕜] :
    Convex ℝ {A : Matrix n n 𝕜 | A.PosDef}
```

**`Matrix.PosDef_iff_eigenvalues'`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L740).

```lean
lemma PosDef_iff_eigenvalues' (M : Matrix d d 𝕜) :
    M.PosDef ↔ ∃ (h : M.IsHermitian), ∀ i, 0 < h.eigenvalues i
```

**`Matrix.IsHermitian.cfc_eigenvalues`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L746).

```lean
lemma IsHermitian.cfc_eigenvalues {M : Matrix d d 𝕜} (hM : M.IsHermitian) (f : ℝ → ℝ) :
    ∃ (e : d ≃ d), Matrix.IsHermitian.eigenvalues (cfc_predicate f M) = f ∘ hM.eigenvalues ∘ e
```

**`Matrix.IsHermitian.eigenvalues_eq_of_unitary_similarity_diagonal`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L794).

> If a Hermitian matrix A is unitarily similar to a diagonal matrix with real entries f, then the eigenvalues of A are a permutation of f.

```lean
lemma IsHermitian.eigenvalues_eq_of_unitary_similarity_diagonal {d 𝕜 : Type*}
    [Fintype d] [DecidableEq d] [RCLike 𝕜]
    {A : Matrix d d 𝕜} (hA : A.IsHermitian)
    {U : Matrix d d 𝕜} (hU : U ∈ Matrix.unitaryGroup d 𝕜)
    {f : d → ℝ}
    (h : A = U * Matrix.diagonal (fun i => (RCLike.ofReal (f i) : 𝕜)) * Matrix.conjTranspose U) :
    ∃ σ : d ≃ d, hA.eigenvalues ∘ σ = f
```

**`Matrix.toEuclideanLin_one`**, a lemma, [line 842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L842).

```lean
lemma toEuclideanLin_one : Matrix.toEuclideanLin (1 : Matrix n n α) = .id
```

**`Matrix.cfc_diagonal`**, a lemma, [line 856](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L856).

```lean
lemma cfc_diagonal (g : d → ℝ) (f : ℝ → ℝ) :
    cfc f (Matrix.diagonal (fun x ↦ (g x : 𝕜))) = diagonal (RCLike.ofReal ∘ f ∘ g)
```

**`Matrix.PosSemidef.pos_of_mem_spectrum`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L892).

```lean
lemma PosSemidef.pos_of_mem_spectrum {A : Matrix d d 𝕜} (hA : A.PosSemidef) (r : ℝ) :
    r ∈ spectrum ℝ A → 0 ≤ r
```

**`Matrix.PosSemidef.pow_add`**, a lemma, [line 899](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L899).

```lean
lemma PosSemidef.pow_add {A : Matrix d d 𝕜} (hA : A.PosSemidef) {x y : ℝ} (hxy : x + y ≠ 0) :
    cfc (· ^ (x + y) : ℝ → ℝ) A = cfc (fun r ↦ r ^ x * r ^ y : ℝ → ℝ) A
```

**`Matrix.PosSemidef.pow_mul`**, a lemma, [line 904](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L904).

```lean
lemma PosSemidef.pow_mul {A : Matrix d d 𝕜} {x y : ℝ} (hA : A.PosSemidef) :
    cfc (· ^ (x * y) : ℝ → ℝ) A = cfc (fun r ↦ (r ^ x) ^ y : ℝ → ℝ) A
```

**`Matrix.trace_submatrix`**, a lemma, [line 917](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L917).

```lean
lemma trace_submatrix
  (A : Matrix d₁ d₁ α) (e : d₂ ≃ d₁) :
    (A.submatrix e e).trace = A.trace
```

**`Matrix.spectrum_prod`**, a lemma, [line 1077](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1077).

```lean
lemma spectrum_prod {d d₂ : Type*}
  [Fintype d] [DecidableEq d] [Fintype d₂] [DecidableEq d₂]
  {A : Matrix d d 𝕜} {B : Matrix d₂ d₂ 𝕜}
  (hA : A.IsHermitian) (hB : B.IsHermitian) :
    spectrum ℝ (A ⊗ₖ B) = spectrum ℝ A * spectrum ℝ B
```

**`Matrix.PosDef.zero_lt`**, a lemma, [line 1142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1142).

```lean
lemma PosDef.zero_lt {n : Type*} [Nonempty n] [Fintype n] {A : Matrix n n ℂ} (hA : A.PosDef) : 0 < A
```

**`Matrix.IsHermitian.spectrum_eq_image_eigenvalues`**, a lemma, [line 1149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1149).

```lean
lemma IsHermitian.spectrum_eq_image_eigenvalues [Fintype n] {A : Matrix n n ℂ} (hA : A.IsHermitian) :
    spectrum ℝ A = Finset.univ.image hA.eigenvalues
```

**`Matrix.IsHermitian.card_spectrum_eq_image`**, a lemma, [line 1157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1157).

```lean
lemma IsHermitian.card_spectrum_eq_image [Fintype n] {A : Matrix n n ℂ} (hA : A.IsHermitian)
  [Fintype (spectrum ℝ A)] :
    Fintype.card (spectrum ℝ A) = (Finset.univ.image hA.eigenvalues).card
```

**`Matrix.IsHermitian.sub_iInf_eignevalues`**, a lemma, [line 1174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1174).

```lean
lemma sub_iInf_eignevalues (hA : A.IsHermitian) :
    (A - iInf hA.eigenvalues • 1).PosSemidef
```

**`Matrix.IsHermitian.iInf_eigenvalues_le_dotProduct_mulVec`**, a lemma, [line 1229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1229).

```lean
lemma iInf_eigenvalues_le_dotProduct_mulVec (hA : A.IsHermitian) (v : d → ℂ) :
    iInf hA.eigenvalues * (star v ⬝ᵥ v) ≤ star v ⬝ᵥ A *ᵥ v
```

**`Matrix.IsHermitian.iInf_eigenvalues_le_of_posSemidef`**, a lemma, [line 1240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1240).

```lean
lemma iInf_eigenvalues_le_of_posSemidef
  (hAB : (B - A).PosSemidef) (hA : A.IsHermitian) (hB : B.IsHermitian) :
    iInf hA.eigenvalues ≤ iInf hB.eigenvalues
```

**`Matrix.IsHermitian.iInf_eigenvalues_le`**, a lemma, [line 1264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1264).

```lean
lemma iInf_eigenvalues_le (hAB : A ≤ B) (hA : A.IsHermitian) (hB : B.IsHermitian) :
    iInf hA.eigenvalues ≤ iInf hB.eigenvalues
```

**`Matrix.IsHermitian.iInf_eigenvalues_smul_one_le`**, a lemma, [line 1269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1269).

```lean
lemma iInf_eigenvalues_smul_one_le (hA : A.IsHermitian) : iInf hA.eigenvalues • 1 ≤ A
```

**`Matrix._shortcut_posSMulMono`**, a lemma, [line 1283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1283).

```lean
lemma _shortcut_posSMulMono : PosSMulMono ℝ (Matrix d d ℂ)
```

**`Matrix._shortcut_posSmulReflectLE`**, a lemma, [line 1286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1286).

```lean
lemma _shortcut_posSmulReflectLE : PosSMulReflectLE ℝ (Matrix d d ℂ)
```

**`Matrix.IsHermitian.spectrum_subset_Ici_of_sub`**, a lemma, [line 1295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1295).

```lean
lemma IsHermitian.spectrum_subset_Ici_of_sub {d 𝕜 : Type*} [Fintype d] [DecidableEq d] [RCLike 𝕜]
  {A x : Matrix d d 𝕜} (hA : A.IsHermitian) (hl : (x - A).PosSemidef) :
    spectrum ℝ x ⊆ Set.Ici (⨅ i, hA.eigenvalues i)
```

**`Matrix.IsHermitian.spectrum_subset_Iic_of_sub`**, a lemma, [line 1416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1416).

```lean
lemma IsHermitian.spectrum_subset_Iic_of_sub {d 𝕜 : Type*} [Fintype d] [DecidableEq d] [RCLike 𝕜]
  {A x : Matrix d d 𝕜} (hA : A.IsHermitian) (hl : (A - x).PosSemidef) :
    spectrum ℝ x ⊆ Set.Iic (⨆ i, hA.eigenvalues i)
```

**`Matrix.IsHermitian.spectrum_subset_of_mem_Icc`**, a lemma, [line 1434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1434).

```lean
lemma IsHermitian.spectrum_subset_of_mem_Icc {d 𝕜 : Type*} [Fintype d] [DecidableEq d] [RCLike 𝕜]
  {A B x : Matrix d d 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  (hl : (x - A).PosSemidef) (hr : (B - x).PosSemidef) :
    spectrum ℝ x ⊆ Set.Icc (⨅ i, hA.eigenvalues i) (⨆ i, hB.eigenvalues i)
```

**`Matrix.traceRight_eq_traceLeft_reindex`**, a theorem, [line 1444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1444). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The right partial trace of a matrix is equal to the left partial trace of the matrix reindexed by swapping the tensor factors.

```lean
theorem traceRight_eq_traceLeft_reindex {n m R : Type*} [Fintype m] [AddCommMonoid R]
  (M : Matrix (n × m) (n × m) R) :
    M.traceRight = (M.reindex (.prodComm ..) (.prodComm ..)).traceLeft
```

**`Matrix.PosSemidef.trace_pos`**, a lemma, [line 1450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1450).

```lean
lemma PosSemidef.trace_pos {n 𝕜 : Type*} [Fintype n] [RCLike 𝕜]
    {A : Matrix n n 𝕜} (hA : A.PosSemidef) (h : A ≠ 0) : 0 < A.trace
```

**`Matrix.traceLeft_add`**, a lemma, [line 1466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1466).

```lean
lemma traceLeft_add : (A + B).traceLeft = A.traceLeft + B.traceLeft
```

**`Matrix.traceLeft_neg`**, a lemma, [line 1471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1471).

```lean
lemma traceLeft_neg : (-A).traceLeft = -A.traceLeft
```

**`Matrix.traceLeft_sub`**, a lemma, [line 1475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1475).

```lean
lemma traceLeft_sub : (A - B).traceLeft = A.traceLeft - B.traceLeft
```

**`Matrix.traceRight_add`**, a lemma, [line 1481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1481).

```lean
lemma traceRight_add : (A + B).traceRight = A.traceRight + B.traceRight
```

**`Matrix.traceRight_neg`**, a lemma, [line 1486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1486).

```lean
lemma traceRight_neg : (-A).traceRight = -A.traceRight
```

**`Matrix.traceRight_sub`**, a lemma, [line 1490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1490).

```lean
lemma traceRight_sub : (A - B).traceRight = A.traceRight - B.traceRight
```

**`Matrix.traceLeft_smul`**, a lemma, [line 1495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1495).

```lean
lemma traceLeft_smul {A : Matrix (m × n) (m × n) α} (r : R) :
    (r • A).traceLeft = r • A.traceLeft
```

**`Matrix.traceRight_smul`**, a lemma, [line 1500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1500).

```lean
lemma traceRight_smul {A : Matrix (n × m) (n × m) α} (r : R) :
    (r • A).traceRight = r • A.traceRight
```

**`Matrix.unitaryGroup_row_norm`**, a lemma, [line 1506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1506).

```lean
lemma unitaryGroup_row_norm [Fintype n] (U : Matrix.unitaryGroup n ℂ) (i : n) :
    ∑ j, ‖U j i‖^2 = 1
```

**`Matrix.piProd`**, a def, [line 1517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1517).

```lean
def piProd [CommMonoid R] (A : ∀ i, Matrix (d i) (d i) R) : Matrix (∀ i, d i) (∀ i, d i) R
```

**`Matrix.IsHermitian.piProd`**, a lemma, [line 1522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1522).

```lean
lemma IsHermitian.piProd [CommSemiring R] [StarRing R] (hA : ∀ i, (A i).IsHermitian) :
    (piProd A).IsHermitian
```

**`Matrix.trace_piProd`**, a lemma, [line 1530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1530).

```lean
lemma trace_piProd [CommSemiring R] :
    (piProd A).trace = ∏ i, (A i).trace
```

**`Matrix.PosSemidef.piProd`**, a lemma, [line 1536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1536).

```lean
lemma PosSemidef.piProd [RCLike R] (hA : ∀ i, (A i).PosSemidef) :
    (piProd A).PosSemidef
```

**`Matrix.submatrix_eq_mul_mul`**, a lemma, [line 1576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1576).

```lean
lemma submatrix_eq_mul_mul {d d₂ d₃ R : Type*} [DecidableEq d] [Fintype d] [Semiring R]
  (A : Matrix d d R) (e : d₂ → d) (f : d₃ → d) :
    A.submatrix e f = (submatrix (α := R) 1 e id : Matrix d₂ d R) * A * (submatrix (α := R) 1 id f)
```

**`Matrix.kronecker_conj_eq`**, a lemma, [line 1586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean#L1586).

> The conjugate of a Kronecker product by a Kronecker product is the Kronecker product of the conjugates (for matrices).

```lean
lemma kronecker_conj_eq {m n p q α : Type*} [CommSemiring α] [StarRing α] [Fintype m] [Fintype n]
    (A : Matrix m m α) (B : Matrix n n α) (C : Matrix p m α) (D : Matrix q n α) :
    (C ⊗ₖ D) * (A ⊗ₖ B) * (C ⊗ₖ D)ᴴ = (C * A * Cᴴ) ⊗ₖ (D * B * Dᴴ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [QuantumInfo.ForMathlib.Misc](misc.md)

## Sources

- [QuantumInfo/ForMathlib/Matrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Matrix.lean)
