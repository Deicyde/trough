---
declaration: module
origin: cited
lean: schattenNorm, schattenNorm_hermitian_pow, schattenNorm_nonneg, schattenNorm_pow_eq, trace_eq_schattenNorm_rpow, schattenNorm_trace_as_eigenvalue_sum, schattenNorm_rpow_eq_sum_singularValues, schattenNorm_eq_sum_singularValues_rpow
statement: formalized
proof: formalized
---

# Schatten norms

The module `QuantumInfo.ForMathlib.HermitianMat.Schatten`, [QuantumInfo/ForMathlib/HermitianMat/Schatten.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean): 14 declarations, 4 with a docstring.

**`schattenNorm`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L25).

> The Schatten p-norm of a matrix A is (Tr[(A*A)^(p/2)])^(1/p).

```lean
noncomputable def schattenNorm (A : Matrix d d ℂ) (p : ℝ) : ℝ
```

**`schattenNorm_hermitian_pow`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L31).

```lean
lemma schattenNorm_hermitian_pow {A : HermitianMat d ℂ} (hA : 0 ≤ A) {p : ℝ} (hp : 0 < p) :
    schattenNorm A.mat p = (A ^ p).trace ^ (1/p)
```

**`schattenNorm_nonneg`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L44).

```lean
lemma schattenNorm_nonneg (A : Matrix d d ℂ) (p : ℝ) :
    0 ≤ schattenNorm A p
```

**`schattenNorm_pow_eq`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L56).

```lean
lemma schattenNorm_pow_eq
  (A : HermitianMat d ℂ) (hA : 0 ≤ A) (p k : ℝ) (hp : 0 < p) (hk : 0 < k) :
    schattenNorm (A ^ k).mat p = (schattenNorm A.mat (k * p)) ^ k
```

**`trace_eq_schattenNorm_rpow`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L69).

```lean
lemma trace_eq_schattenNorm_rpow
    (A : HermitianMat d ℂ) (hA : 0 ≤ A) (r : ℝ) (hr : 0 < r) :
    (A ^ r).trace = (schattenNorm A.mat r) ^ r
```

## Relating schattenNorm to singular values

**`schattenNorm_trace_as_eigenvalue_sum`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L79).

```lean
lemma schattenNorm_trace_as_eigenvalue_sum (A : Matrix d d ℂ) (p : ℝ) :
    RCLike.re ((Matrix.isHermitian_mul_conjTranspose_self A.conjTranspose).cfc (· ^ (p/2))).trace =
    ∑ i : d, ((Matrix.isHermitian_mul_conjTranspose_self A.conjTranspose).eigenvalues i) ^ (p/2)
```

**`schattenNorm_rpow_eq_sum_singularValues`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L89).

```lean
lemma schattenNorm_rpow_eq_sum_singularValues (A : Matrix d d ℂ) {p : ℝ} (hp : 0 < p) :
    schattenNorm A p ^ p = ∑ i : d, singularValues A i ^ p
```

**`schattenNorm_eq_sum_singularValues_rpow`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L106).

```lean
lemma schattenNorm_eq_sum_singularValues_rpow (A : Matrix d d ℂ) {p : ℝ} (hp : 0 < p) :
    schattenNorm A p = (∑ i : d, singularValues A i ^ p) ^ (1/p)
```

**`schattenNorm_rpow_eq_sum_sorted`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L119).

> `‖A‖_p^p` equals the same sum over sorted singular values.

```lean
lemma schattenNorm_rpow_eq_sum_sorted (A : Matrix d d ℂ) {p : ℝ} (hp : 0 < p) :
    schattenNorm A p ^ p =
    ∑ i : Fin (Fintype.card d), singularValuesSorted A i ^ p
```

**`HermitianMat.trace_young`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L130).

> Scalar trace Young inequality for PSD matrices:
> ⟪A, B⟫ ≤ Tr[A^p]/p + Tr[B^q]/q for PSD A, B and conjugate p, q > 1.

```lean
lemma HermitianMat.trace_young
    (A B : HermitianMat d ℂ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (p q : ℝ) (hp : 1 < p) (hpq : 1/p + 1/q = 1) :
    ⟪A, B⟫_ℝ ≤ (A ^ p).trace / p + (B ^ q).trace / q
```

**`conjTranspose_half_mul_eq_conj`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L169).

> For PSD `A` and Hermitian `B`, the product
> `C = A^{1/2} * B` satisfies `C^* C = (A.conj B.mat).mat = B * A * B`.

```lean
lemma conjTranspose_half_mul_eq_conj
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A) :
    ((A ^ (1/2 : ℝ)).mat * B.mat).conjTranspose * ((A ^ (1/2 : ℝ)).mat * B.mat)
    = (A.conj B.mat).mat
```

**`schattenNorm_half_mul_rpow_eq_trace_conj`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L176).

```lean
lemma schattenNorm_half_mul_rpow_eq_trace_conj
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A)
    {α : ℝ} (hα : 0 < α) :
    (schattenNorm ((A ^ (1/2 : ℝ)).mat * B.mat) (2 * α)) ^ (2 * α) =
    ((A.conj B.mat) ^ α).trace
```

## Schatten–Hölder inequality

> The *Schatten–Hölder inequality* for matrix products:
> For matrices `A`, `B` and exponents `r, p, q > 0` with `1/r = 1/p + 1/q`,
> the Schatten `r`-norm of the product satisfies
>   `‖A * B‖_{S^r} ≤ ‖A‖_{S^p} * ‖B‖_{S^q}`.
> This version includes the quasi-norm case (r, p, q < 1).

### Proof sketch

> The proof proceeds in three steps:
> 1. Express Schatten norms in terms of singular values:
>    `‖A‖_p = (∑ σᵢ(A)^p)^{1/p}`.
> 2. Use the **weak log-majorization** of singular values of products
>    (`weakLogMaj_singularValues_mul` + `sum_rpow_le_of_weakLogMaj`) to obtain
>    `∑ σᵢ(AB)^r ≤ ∑ σ↓ᵢ(A)^r · σ↓ᵢ(B)^r`.
> 3. Apply the **classical Hölder inequality** for finite sums
>    (`NNReal.inner_le_Lp_mul_Lq` from Mathlib, with conjugate exponents
>    `p/r` and `q/r`) to bound
>    `∑ σ↓ᵢ(A)^r · σ↓ᵢ(B)^r ≤ (∑ σᵢ(A)^p)^{r/p} · (∑ σᵢ(B)^q)^{r/q}`.
> 4. Take `1/r`-th powers and combine.

**`schattenNorm_mul_le`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L233).

```lean
lemma schattenNorm_mul_le (A B : Matrix d d ℂ) {r p q : ℝ}
    (hr : 0 < r) (hp : 0 < p) (hq : 0 < q) (hpqr : 1 / r = 1 / p + 1 / q) :
    schattenNorm (A * B) r ≤ schattenNorm A p * schattenNorm B q
```

**`HermitianMat.trace_rpow_conj_le`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean#L288).

```lean
lemma HermitianMat.trace_rpow_conj_le
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A) (hB : 0 ≤ B)
    {α p q : ℝ} (hα : 0 < α) (hp : 0 < p) (hq : 0 < q)
    (hpq : 1 / (2 * α) = 1 / p + 1 / q) :
    ((A.conj B.mat) ^ α).trace ≤
    (((A ^ (p / 2)).trace) ^ (1 / p) * ((B ^ q).trace) ^ (1 / q)) ^ (2 * α)
```

## Depends on

- [Matrix Powers With Real Exponents](rpow.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Schatten.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Schatten.lean)
