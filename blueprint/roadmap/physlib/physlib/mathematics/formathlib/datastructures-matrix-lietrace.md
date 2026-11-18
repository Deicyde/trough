---
declaration: module
origin: cited
lean: Matrix.diag_exp_of_blockTriangular_id, Matrix.det_exp, Matrix.det_exp_real, Matrix.tsum_eq_zero, Matrix.matrix_tsum_apply, Matrix.diag_mul_of_blockTriangular_id, Matrix.blockTriangular.pow, Matrix.diag_pow_of_blockTriangular_id
statement: formalized
proof: formalized
---

# Lie's Trace Formula

The module `Physlib.Mathematics.ForMathlib.DataStructures.Matrix.LieTrace`, [Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean): 20 declarations (1 instance with no name), 16 with a docstring, 3 listed as significant.

> This file proves the formula `det (exp A) = exp (tr A)` for matrices, also known as Lie's trace
> formula.
>
> The proof proceeds by first showing the formula for upper-triangular matrices and then
> leveraging Schur triangulation to generalize to any matrix. An upper-triangular matrix `A`
> is defined in `mathlib` as `Matrix.BlockTriangular A id`.

## Main results

> - `Matrix.det_exp`: The determinant of the exponential of a matrix is the exponential of its trace.

**An instance with no name**, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L37).

```lean
instance [UniformSpace 𝕂] : UniformSpace (Matrix m n 𝕂)
```

**`Matrix.tsum_eq_zero`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L40).

> If every term of a series is zero, then its sum is zero.

```lean
lemma tsum_eq_zero
    {β : Type*} [TopologicalSpace β] [AddCommMonoid β]
    {f : ℕ → β} (h : ∀ n, f n = 0) :
    (∑' n, f n) = 0
```

### The determinant of the matrix exponential

**`Matrix.matrix_tsum_apply`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L58).

> Apply a matrix `tsum` to a given entry.

```lean
lemma matrix_tsum_apply
    {f : ℕ → Matrix m m 𝕂} (hf : Summable f) (i j : m) :
    (∑' n, f n) i j = ∑' n, (f n) i j
```

**`Matrix.diag_mul_of_blockTriangular_id`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L74).

> For upper-triangular matrices, the diagonal of a product is the product of the diagonals.
> This is a specific case of a more general property for block-triangular matrices.

```lean
lemma diag_mul_of_blockTriangular_id {A B : Matrix m m 𝕂}
    (hA : BlockTriangular A id) (hB : BlockTriangular B id) : (A * B).diag = A.diag * B.diag
```

**`Matrix.blockTriangular.pow`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L86).

> Powers of block triangular matrices are block triangular.

```lean
lemma blockTriangular.pow {A : Matrix m m 𝕂} (hA : BlockTriangular A id) (k : ℕ) :
    BlockTriangular (A ^ k) id
```

**`Matrix.diag_pow_of_blockTriangular_id`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L93).

> For an upper-triangular matrix, the diagonal of a power is the power of the diagonal.

```lean
lemma diag_pow_of_blockTriangular_id {A : Matrix m m 𝕂}
    (hA : BlockTriangular A id) (k : ℕ) : (A ^ k).diag = A.diag ^ k
```

**`Matrix.blockTriangular_exp_of_blockTriangular_id`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L102).

> The exponential of an upper-triangular matrix is upper-triangular.

```lean
lemma blockTriangular_exp_of_blockTriangular_id
    {A : Matrix m m 𝕂} (hA : BlockTriangular A id) :
    (NormedSpace.exp A).BlockTriangular id
```

**`Matrix.diag_pow_entry_eq_pow_diag_entry`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L123).

> For an upper–triangular matrix `A`, the `(i,i)` entry of the power `A ^ n`
> is simply the `n`-th power of the original diagonal entry.

```lean
lemma diag_pow_entry_eq_pow_diag_entry {A : Matrix m m 𝕂}
    (hA : BlockTriangular A id) (n : ℕ) (i : m) :
    (A ^ n) i i = (A i i) ^ n
```

**`Matrix.exp_series_diag_term_eq`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L131).

> Each term in the matrix exponential series equals the corresponding scalar term on the
> diagonal

```lean
lemma exp_series_diag_term_eq {A : Matrix m m 𝕂} (hA : BlockTriangular A id)
    (n : ℕ) (i : m) :
    ((n.factorial : 𝕂)⁻¹ • (A ^ n)) i i = (n.factorial : 𝕂)⁻¹ • (A i i) ^ n
```

**`Matrix.matrix_exp_series_diag_eq_scalar_series`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L137).

> The diagonal of the matrix exponential series equals the scalar exponential series

```lean
lemma matrix_exp_series_diag_eq_scalar_series {A : Matrix m m 𝕂} (hA : BlockTriangular A id)
    (i : m) :
    (∑' n, ((n.factorial : 𝕂)⁻¹ • (A ^ n)) i i) = ∑' n, (n.factorial : 𝕂)⁻¹ • (A i i) ^ n
```

**`Matrix.diag_exp_of_blockTriangular_id`**, a theorem, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L144). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The diagonal of the exponential of an upper-triangular matrix `A` consists of the
> exponentials of the diagonal entries of `A`.

```lean
theorem diag_exp_of_blockTriangular_id
    {A : Matrix m m 𝕂} (hA : BlockTriangular A id) :
    (NormedSpace.exp A).diag = fun i => NormedSpace.exp (A i i)
```

**`Matrix.det_exp_of_blockTriangular_id`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L154).

> Lie's trace formula for upper triangular matrices.

```lean
lemma det_exp_of_blockTriangular_id {A : Matrix m m 𝕂} (hA : BlockTriangular A id) :
    (NormedSpace.exp A).det = NormedSpace.exp A.trace
```

**`Matrix.trace_unitary_conj`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L167).

> The trace is invariant under unitary conjugation.

```lean
lemma trace_unitary_conj (A : Matrix m m 𝕂) (U : unitaryGroup m 𝕂) :
    trace ((U : Matrix m m 𝕂) * A * star (U : Matrix m m 𝕂)) = trace A
```

**`Matrix.det_unitary_conj`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L175).

> The determinant is invariant under unitary conjugation.

```lean
lemma det_unitary_conj (A : Matrix m m 𝕂) (U : unitaryGroup m 𝕂) :
    det ((U : Matrix m m 𝕂) * A * star (U : Matrix m m 𝕂)) = det A
```

**`Matrix.exp_unitary_conj`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L181).

> The exponential of a matrix commutes with unitary conjugation.

```lean
lemma exp_unitary_conj (A : Matrix m m 𝕂) (U : unitaryGroup m 𝕂) :
    NormedSpace.exp ((U : Matrix m m 𝕂) * A * star (U : Matrix m m 𝕂)) =
      (U : Matrix m m 𝕂) * NormedSpace.exp A * star (U : Matrix m m 𝕂)
```

**`Matrix.det_exp_unitary_conj`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L192).

```lean
lemma det_exp_unitary_conj (A : Matrix m m 𝕂) (U : unitaryGroup m 𝕂) :
    (NormedSpace.exp ((U : Matrix m m 𝕂) * A * star (U : Matrix m m 𝕂))).det =
    (NormedSpace.exp A).det
```

**`Matrix.det_exp`**, a theorem, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L199). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The determinant of the exponential of a matrix is the exponential of its trace.
> This is also known as **Lie's trace formula**.

```lean
theorem det_exp {𝕂 m : Type*} [RCLike 𝕂] [IsAlgClosed 𝕂] [Fintype m] [LinearOrder m]
    (A : Matrix m m 𝕂) :
    (NormedSpace.exp A).det = NormedSpace.exp A.trace
```

**`Matrix.map_tsum`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L217).

```lean
lemma map_tsum {α β m n : Type*}
    [AddCommMonoid α] [AddCommMonoid β] [TopologicalSpace α] [TopologicalSpace β]
    [T2Space β]
    (f : α →+ β) (hf : Continuous f) {s : ℕ → Matrix m n α} (hs : Summable s) :
    (∑' k, s k).map f = ∑' k, (s k).map f
```

**`NormedSpace.exp_map_algebraMap`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L234).

```lean
lemma exp_map_algebraMap {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) :
    (exp A).map (algebraMap ℝ ℂ) = exp (A.map (algebraMap ℝ ℂ))
```

**`Matrix.det_exp_real`**, a theorem, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean#L262). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Lie's trace formula over ℝ: det(exp(A)) = exp(tr(A)) for any real matrix A.
> This is proved by transferring the result from ℂ using the naturality of polynomial identities.

```lean
theorem det_exp_real {n : Type*} [Fintype n] [LinearOrder n]
    (A : Matrix n n ℝ) : (NormedSpace.exp A).det = Real.exp A.trace
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Schur triangulation](schurtriangulation.md)

## Sources

- [Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/DataStructures/Matrix/LieTrace.lean)
