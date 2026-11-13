---
declaration: module
origin: cited
lean: Matrix.traceNorm_neg, Matrix.traceNorm_isometry_left, Matrix.traceNorm_isometry_right, Matrix.traceNorm_unitary_conj, Matrix.traceNorm_Hermitian_eq_sum_abs_eigenvalues, Matrix.traceNorm_nonneg, Matrix.traceNorm_zero_iff, Matrix.traceNorm_smul
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.MatrixNorm.TraceNorm

The module `QuantumInfo.ForMathlib.MatrixNorm.TraceNorm`, [QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean): 23 declarations, 22 with a docstring, 21 listed as significant; 3 private, not shown.

**`Matrix.traceNorm`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L27).

> The trace norm of a matrix: Tr[√(A† A)].

```lean
def traceNorm (A : Matrix m n R) : ℝ
```

**`Matrix.traceNorm_zero`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L32).

```lean
lemma traceNorm_zero : traceNorm (0 : Matrix m n R) = 0
```

**`Matrix.traceNorm_neg`**, a theorem, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L37). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm of the negative is equal to the trace norm.

```lean
theorem traceNorm_neg (A : Matrix m n R) : traceNorm (-A) = traceNorm A
```

**`Matrix.traceNorm_isometry_left`**, a theorem, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L47). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is invariant under left multiplication by an isometry.

```lean
theorem traceNorm_isometry_left [Fintype k] {A : Matrix n m R} {u : Matrix k n R}
  (hu₁ : u.Isometry) : traceNorm (u * A) = traceNorm A
```

**`Matrix.traceNorm_isometry_right`**, a theorem, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L56). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is invariant under right multiplication by the adjoint of an isometry.

```lean
theorem traceNorm_isometry_right [Fintype k] {A : Matrix n m R} {u : Matrix k m R}
  (hu₁ : u.Isometry) : traceNorm (A * uᴴ) = traceNorm A
```

**`Matrix.traceNorm_unitary_conj`**, a theorem, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L81). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is invariant under unitary conjugation.

```lean
theorem traceNorm_unitary_conj {A : Matrix n n R} {U : Matrix.unitaryGroup n R} :
  traceNorm (U.val * A * U.valᴴ) = traceNorm A
```

**`Matrix.traceNorm_Hermitian_eq_sum_abs_eigenvalues`**, a theorem, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L89). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For Hermitian matrices, the trace norm is the sum of absolute eigenvalues.
>
> This is Proposition 9.1.1 in Wilde.

```lean
theorem traceNorm_Hermitian_eq_sum_abs_eigenvalues {A : Matrix n n R} (hA : A.IsHermitian) :
    A.traceNorm = ∑ i, abs (hA.eigenvalues i)
```

**`Matrix.traceNorm_nonneg`**, a theorem, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L109). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is nonnegative. Property 9.1.1 in Wilde.

```lean
theorem traceNorm_nonneg (A : Matrix m n R) : 0 ≤ A.traceNorm
```

**`Matrix.traceNorm_zero_iff`**, a theorem, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L115). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is zero iff the matrix is zero.

```lean
theorem traceNorm_zero_iff (A : Matrix m n R) : A.traceNorm = 0 ↔ A = 0
```

**`Matrix.traceNorm_smul`**, a theorem, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L144). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is homogeneous under scalar multiplication. Property 9.1.2 in Wilde.

```lean
theorem traceNorm_smul (A : Matrix m n R) (c : R) : (c • A).traceNorm = ‖c‖ * A.traceNorm
```

**`Matrix.exists_svd_sqrt_eigenvalues`**, a theorem, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L181). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Singular value decomposition for square complex matrices, with singular values expressed as
> square roots of the eigenvalues of `Aᴴ * A`.

```lean
theorem exists_svd_sqrt_eigenvalues (A : Matrix n n ℂ) :
    let hH : (Aᴴ * A).IsHermitian := by
      simpa using (Matrix.isHermitian_mul_conjTranspose_self A.conjTranspose)
    ∃ V W : Matrix.unitaryGroup n ℂ,
      A = V.val * Matrix.diagonal (fun i => (Real.sqrt (hH.eigenvalues i) : ℂ)) * W.valᴴ
```

**`Matrix.traceNorm_eq_sum_singularValues`**, a theorem, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L261). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm of a square complex matrix is the sum of its singular values.

```lean
theorem traceNorm_eq_sum_singularValues [DecidableEq n] (A : Matrix n n ℂ) :
    A.traceNorm = ∑ i, singularValues A i
```

**`Matrix.traceNorm_eq_sum_singularValuesSorted`**, a theorem, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L272). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm of a square complex matrix is the sum of its sorted singular values.

```lean
theorem traceNorm_eq_sum_singularValuesSorted [DecidableEq n] (A : Matrix n n ℂ) :
    A.traceNorm = ∑ i : Fin (Fintype.card n), singularValuesSorted A i
```

**`Matrix.singularValues_le_opNorm`**, a theorem, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L282). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every singular value is bounded by the operator norm.

```lean
theorem singularValues_le_opNorm [DecidableEq n] (A : Matrix n n ℂ) (i : n) :
    singularValues A i ≤ ‖A‖
```

**`Matrix.traceNorm_mul_le_opNorm_traceNorm`**, a theorem, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L305). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is bounded by the operator norm on the left times the trace norm on the right.

```lean
theorem traceNorm_mul_le_opNorm_traceNorm [DecidableEq n] (A B : Matrix n n ℂ) :
    (A * B).traceNorm ≤ ‖A‖ * B.traceNorm
```

**`Matrix.traceNorm_conjTranspose`**, a theorem, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L336). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is invariant under conjugate transpose.

```lean
theorem traceNorm_conjTranspose (A : Matrix n n ℂ) :
    Aᴴ.traceNorm = A.traceNorm
```

**`Matrix.traceNorm_mul_le_traceNorm_opNorm`**, a theorem, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L359). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is bounded by trace norm on the left times operator norm on the right.

```lean
theorem traceNorm_mul_le_traceNorm_opNorm [DecidableEq n] (A B : Matrix n n ℂ) :
    (A * B).traceNorm ≤ A.traceNorm * ‖B‖
```

**`Matrix.traceNorm_sandwich_le`**, a theorem, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L370). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Multiplication on both sides by contractions does not increase trace norm.

```lean
theorem traceNorm_sandwich_le [DecidableEq n] {S M T : Matrix n n ℂ} (hS : ‖S‖ ≤ 1)
    (hT : ‖T‖ ≤ 1) : (S * M * T).traceNorm ≤ M.traceNorm
```

**`Matrix.abs_trace_le_traceNorm`**, a theorem, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L384). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The absolute value of the trace is bounded by the trace norm.

```lean
theorem abs_trace_le_traceNorm (A : Matrix n n ℂ) :
    ‖A.trace‖ ≤ A.traceNorm
```

**`Matrix.traceNorm_eq_max_re_tr_U`**, a theorem, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L413). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For square complex matrices, the trace norm is the maximum of `re (Tr[U * A])`
> over unitaries `U`.

```lean
theorem traceNorm_eq_max_re_tr_U (A : Matrix n n ℂ) :
    IsGreatest {x : ℝ | ∃ U : unitaryGroup n ℂ, Complex.re ((U.val * A).trace) = x} A.traceNorm
```

**`Matrix.traceNorm_add_le`**, a theorem, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L459). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm satisfies the triangle inequality for square complex matrices.

```lean
theorem traceNorm_add_le (A B : Matrix n n ℂ) : (A + B).traceNorm ≤ A.traceNorm + B.traceNorm
```

**`Matrix.PosSemidef.traceNorm_eq_trace`**, a theorem, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L476). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A positive semidefinite matrix has trace norm equal to its trace.

```lean
theorem PosSemidef.traceNorm_eq_trace {A : Matrix m m R} (hA : A.PosSemidef) :
    A.traceNorm = A.trace
```

**`Matrix.traceNorm_convex`**, a theorem, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean#L483). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace norm is convex. Property 9.1.5 in Wilde.

```lean
theorem traceNorm_convex (M N : Matrix n n ℂ) (l : ℝ) (hl : 0 ≤ l ∧ l ≤ 1) :
  ((l:ℂ) • M + ((1 - l) : ℂ) • N).traceNorm ≤ l * M.traceNorm + (1-l) * N.traceNorm
```

## Depends on

- [QuantumInfo.ForMathlib.Isometry](../isometry.md)
- [Majorization and weak log-majorization](../majorization.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HermitianMat.Unitary](../hermitianmat/unitary.md)

## Sources

- [QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/MatrixNorm/TraceNorm.lean)
