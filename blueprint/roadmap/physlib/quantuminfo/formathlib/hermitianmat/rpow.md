---
declaration: module
origin: cited
lean: HermitianMat.continuousOn_rpow_pos, HermitianMat.continuousOn_rpow_neg, HermitianMat.reindex_rpow, HermitianMat.continuousOn_rpow_joint_nonneg_pos, HermitianMat.cfc_sq_rpow_eq_cfc_rpow, HermitianMat.rpow_le_rpow_of_posDef, HermitianMat.rpow_le_rpow_of_le, HermitianMat.rpow
statement: formalized
proof: formalized
---

# Matrix Powers With Real Exponents

The module `QuantumInfo.ForMathlib.HermitianMat.Rpow`, [QuantumInfo/ForMathlib/HermitianMat/Rpow.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean): 50 declarations, 19 with a docstring, 7 listed as significant; 19 private, not shown.

> This file defines real powers of finite-dimensional Hermitian matrices by continuous
> functional calculus:
>
> `A ^ r = A.cfc (fun x => x ^ r)`.
>
> The scalar function is `Real.rpow`, so this is a total operation on Hermitian matrices.
> For positive semidefinite matrices it has the expected spectral meaning. For negative
> exponents on singular matrices it follows the `Real.rpow` convention, so zero eigenvalues
> remain zero; use positive-definiteness hypotheses for inverse laws.
>
> Main results:
> * algebraic and spectral lemmas for real powers;
> * continuity in the exponent and in the matrix argument;
> * the Loewner-Heinz monotonicity theorem for `0 < q <= 1`;
> * Lieb-Thirring and Rotfel'd trace inequalities for `0 < p <= 1`.

**`HermitianMat.rpow`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L47).

> Real powers of Hermitian matrices via continuous functional calculus.
>
> This is the total functional-calculus definition `A.cfc (fun x => x ^ r)`. For positive
> semidefinite `A`, this is the usual spectral power. For negative exponents on singular
> matrices, zero eigenvalues stay zero because this uses `Real.rpow`.

```lean
def rpow (A : HermitianMat d 𝕜) (r : ℝ) : HermitianMat d 𝕜
```

**`HermitianMat.instRPow`**, an instance, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L50).

```lean
instance instRPow : Pow (HermitianMat d 𝕜) ℝ
```

**`HermitianMat.rpow_conj_unitary`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L53).

```lean
lemma rpow_conj_unitary (A : HermitianMat d 𝕜) (U : Matrix.unitaryGroup d 𝕜) (r : ℝ) :
    (HermitianMat.conj U.val A) ^ r = HermitianMat.conj U.val (A ^ r)
```

**`HermitianMat.pow_eq_rpow`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L57).

```lean
lemma pow_eq_rpow : A ^ r = A.rpow r
```

**`HermitianMat.rpow_eq_cfc`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L60).

```lean
lemma rpow_eq_cfc : A ^ r = A.cfc (· ^ r)
```

**`HermitianMat.diagonal_pow`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L63).

```lean
lemma diagonal_pow (f : d → ℝ) :
    (diagonal 𝕜 f) ^ r = diagonal 𝕜 (fun i ↦ (f i) ^ r)
```

**`HermitianMat.rpow_const_continuous`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L69).

```lean
lemma rpow_const_continuous {r : ℝ} (hr : 0 ≤ r) : Continuous (fun A : HermitianMat d ℂ ↦ A ^ r)
```

**`HermitianMat.const_rpow_continuous`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L73).

```lean
lemma const_rpow_continuous [NonSingular A] : Continuous (fun r : ℝ ↦ A ^ r)
```

**`HermitianMat.continuousOn_rpow_pos`**, a theorem, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L83). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a fixed Hermitian matrix A, the function x ↦ A^x is continuous for x > 0.

```lean
theorem continuousOn_rpow_pos (A : HermitianMat d ℂ) : ContinuousOn (fun x : ℝ ↦ A ^ x) (Set.Ioi 0)
```

**`HermitianMat.continuousOn_rpow_neg`**, a theorem, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L92). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a fixed Hermitian matrix A, the function x ↦ A^x is continuous for x < 0.

```lean
theorem continuousOn_rpow_neg (A : HermitianMat d ℂ) : ContinuousOn (fun x : ℝ ↦ A ^ x) (Set.Iio 0)
```

**`HermitianMat.rpow_one`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L98).

```lean
lemma rpow_one : A ^ (1 : ℝ) = A
```

**`HermitianMat.sqrt_eq_cfc_rpow_half`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L104).

> Functional calculus of Real.sqrt is equal to functional calculus of x^(1/2).

```lean
lemma sqrt_eq_cfc_rpow_half (A : HermitianMat d 𝕜)  :
    A.sqrt = A.cfc (fun x ↦ x ^ (1/2 : ℝ))
```

**`HermitianMat.one_rpow`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L111).

```lean
lemma one_rpow : (1 : HermitianMat d 𝕜) ^ r = 1
```

**`HermitianMat.rpow_zero`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L119).

```lean
lemma rpow_zero (A : HermitianMat d 𝕜) : A ^ (0 : ℝ) = 1
```

**`HermitianMat.rpow_diagonal`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L122).

```lean
lemma rpow_diagonal (a : d → ℝ) (r : ℝ) :
  (diagonal ℂ a) ^ r = diagonal ℂ (fun i => a i ^ r)
```

**`HermitianMat.reindex_rpow`**, a theorem, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L128). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Keeps in line with our simp-normal form for moving reindex outwards.

```lean
theorem reindex_rpow (e : d ≃ d₂) :
    A.reindex e ^ r = (A ^ r).reindex e
```

**`HermitianMat.mat_rpow_add`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L132).

```lean
lemma mat_rpow_add (hA : 0 ≤ A) {p q : ℝ} (hpq : p + q ≠ 0) :
    (A ^ (p + q)).mat = (A ^ p).mat * (A ^ q).mat
```

**`HermitianMat.rpow_mul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L137).

```lean
lemma rpow_mul (hA : 0 ≤ A) {p q : ℝ} : A ^ (p * q) = (A ^ p) ^ q
```

**`HermitianMat.conj_rpow`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L141).

```lean
lemma conj_rpow (hA : 0 ≤ A) (hq : q ≠ 0) (hqr : r + 2 * q ≠ 0) :
    (A ^ r).conj (A ^ q) = A ^ (r + 2 * q)
```

**`HermitianMat.pow_half_mul`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L148).

```lean
lemma pow_half_mul (hA : 0 ≤ A) :
    (A ^ (1/2 : ℝ)).mat * (A ^ (1/2 : ℝ)).mat = A
```

**`HermitianMat.rpow_pos`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L154).

```lean
lemma rpow_pos {A : HermitianMat d 𝕜} (hA : 0 < A) {p : ℝ} : 0 < A ^ p
```

**`HermitianMat.rpow_nonneg`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L159).

```lean
lemma rpow_nonneg (hA : 0 ≤ A) {p : ℝ} : 0 ≤ A ^ p
```

**`HermitianMat.inv_eq_rpow_neg_one`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L164).

```lean
lemma inv_eq_rpow_neg_one (hA : A.mat.PosDef) : A⁻¹ = A ^ (-1 : ℝ)
```

**`HermitianMat.sandwich_self`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L170).

```lean
lemma sandwich_self (hB : B.mat.PosDef) :
    (B.conj (B ^ (-1/2 : ℝ)).mat) = 1
```

**`HermitianMat.rpow_inv_eq_neg_rpow`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L186).

```lean
lemma rpow_inv_eq_neg_rpow (hA : A.mat.PosDef) (p : ℝ) : (A ^ p)⁻¹ = A ^ (-p)
```

**`HermitianMat.sandwich_le_one`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L210).

```lean
lemma sandwich_le_one (hB : B.mat.PosDef) (h : A ≤ B) :
    (A.conj (B ^ (-1/2 : ℝ)).mat) ≤ 1
```

**`HermitianMat.rpow_neg_mul_rpow_self`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L215).

```lean
lemma rpow_neg_mul_rpow_self (hA : A.mat.PosDef) (p : ℝ) :
    (A ^ (-p)).mat * (A ^ p).mat = 1
```

**`HermitianMat.isUnit_rpow_toMat`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L235).

```lean
lemma isUnit_rpow_toMat (hA : A.mat.PosDef) (p : ℝ) : IsUnit (A ^ p).mat
```

**`HermitianMat.sandwich_inv`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L248).

```lean
lemma sandwich_inv (hB : B.mat.PosDef) :
    (A.conj (B ^ (-1/2 : ℝ)).mat)⁻¹ = A⁻¹.conj (B ^ (1/2 : ℝ)).mat
```

**`HermitianMat.ker_rpow_eq_of_nonneg`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L255).

```lean
lemma ker_rpow_eq_of_nonneg {A : HermitianMat d ℂ} (hA : 0 ≤ A) (hp : r ≠ 0):
    (A ^ r).ker = A.ker
```

**`HermitianMat.ker_rpow_le_of_nonneg`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L260).

```lean
lemma ker_rpow_le_of_nonneg {A : HermitianMat d ℂ} (hA : 0 ≤ A) :
    (A ^ r).ker ≤ A.ker
```

**`HermitianMat.conj_kron`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L276).

```lean
lemma conj_kron
  (A : Matrix d d 𝕜) (B : Matrix d₂ d₂ 𝕜) (C : HermitianMat d 𝕜) (D : HermitianMat d₂ 𝕜) :
    conj (A ⊗ₖ B) (C ⊗ₖ D) = conj A C ⊗ₖ conj B D
```

**`HermitianMat.rpow_kron`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L282).

```lean
lemma rpow_kron
    {A : HermitianMat d ℂ} {B : HermitianMat d₂ ℂ} (r : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) :
    (A ⊗ₖ B) ^ r = (A ^ r) ⊗ₖ (B ^ r)
```

**`HermitianMat.continuousOn_rpow_uniform`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L303).

```lean
lemma continuousOn_rpow_uniform {K : Set ℝ} (hK : IsCompact K) :
    ContinuousOn (fun r : ℝ ↦ UniformOnFun.ofFun {K} (fun t : ℝ ↦ t ^ r)) (Set.Ioi 0)
```

**`HermitianMat.continuousOn_rpow_joint_nonneg_pos`**, a theorem, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L330). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Joint continuity of matrix rpow for Hermitian matrices with positive exponent

```lean
theorem continuousOn_rpow_joint_nonneg_pos
    {X : Type*} [TopologicalSpace X]
    {A : X → HermitianMat d ℂ} {p : X → ℝ} {S : Set X}
    (hA : ContinuousOn A S) (hp : ContinuousOn p S)
    (hp_pos : ∀ x ∈ S, 0 < p x) :
    ContinuousOn (fun x ↦ A x ^ p x) S
```

**`HermitianMat.cfc_sq_rpow_eq_cfc_rpow`**, a theorem, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L350). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For positive semidefinite `A`, `(A ^ 2) ^ (p / 2) = A ^ p` in functional calculus form.
>
> The nonnegative exponent assumption is needed for continuity at zero. For positive definite
> matrices, the same identity should hold for all real `p`.

```lean
theorem cfc_sq_rpow_eq_cfc_rpow
    (A : HermitianMat d 𝕜) (hA : 0 ≤ A) (p : ℝ) (hp : 0 ≤ p) :
    (A ^ 2).cfc (fun x => x ^ (p/2)) = A.cfc (fun x => x ^ p)
```

**`HermitianMat.trace_rpow_eq_sum`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L369).

> Tr[A^p] = ∑ᵢ λᵢ^p for a Hermitian matrix A.

```lean
lemma trace_rpow_eq_sum (A : HermitianMat d ℂ) (p : ℝ) :
    (A ^ p).trace = ∑ i, (A.H.eigenvalues i) ^ p
```

## Loewner-Heinz Theorem

> The operator monotonicity of `x ↦ x ^ q` for `0 < q ≤ 1`:
> if `A ≤ B` (in the Loewner order), then `A ^ q ≤ B ^ q`.
> This is proved using the resolvent integral representation, following the same
> approach as `log_mono` in `LogExp.lean`. The key identity is:
>   `x ^ q = c_q * ∫ t in (0,∞), t ^ (q-1) * x / (x + t) dt`
> where `c_q = sin(π q) / π`. Since each integrand `x / (x + t)` is operator
> monotone (via `inv_antitone`), the integral is operator monotone.

**`HermitianMat.rpowApprox`**, a def, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L389).

> Finite integral approximation for the rpow monotonicity proof.
> Same integrand as `logApprox` but with weight `t ^ q`.

```lean
noncomputable def rpowApprox (A : HermitianMat d ℂ) (q T : ℝ) : HermitianMat d ℂ
```

**`HermitianMat.rpowApprox_mono`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L394).

```lean
lemma rpowApprox_mono {A B : HermitianMat d ℂ} (hA : A.mat.PosDef) (hB : B.mat.PosDef)
    (hAB : A ≤ B) (hq : 0 ≤ q) (T : ℝ) (hT : 0 < T) :
    rpowApprox A q T ≤ rpowApprox B q T
```

**`HermitianMat.scalarRpowApprox`**, a def, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L434).

> The scalar function underlying rpowApprox via the CFC.

```lean
noncomputable def scalarRpowApprox (q T x : ℝ) : ℝ
```

**`HermitianMat.rpowApprox_eq_cfc_scalar`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L438).

```lean
lemma rpowApprox_eq_cfc_scalar (A : HermitianMat d ℂ) (hA : A.mat.PosDef) (q T : ℝ)
    (hq : 0 ≤ q) (hT : 0 < T) :
    rpowApprox A q T = A.cfc (scalarRpowApprox q T)
```

**`HermitianMat.rpowConst`**, a def, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L480).

> The positive constant arising from the resolvent integral.
> Equal to `∫ u in Set.Ioi 0, u ^ (q-1) / (1+u)` = `π / sin(π q)`,
> but we only need its positivity.

```lean
noncomputable def rpowConst (q : ℝ) : ℝ
```

**`HermitianMat.rpowConst_integrableOn`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L485).

> The integrand `u ^ (q-1) / (1+u)` is integrable on `(0, ∞)` for `0 < q < 1`.

```lean
lemma rpowConst_integrableOn (hq : 0 < q) (hq1 : q < 1) :
    IntegrableOn (fun u : ℝ => u ^ (q - 1) / (1 + u)) (Set.Ioi 0)
```

**`HermitianMat.rpowConst_pos`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L518).

> The resolvent constant is positive for `0 < q < 1`.

```lean
lemma rpowConst_pos (hq : 0 < q) (hq1 : q < 1) : 0 < rpowConst q
```

**`HermitianMat.scalarRpowApprox_tendsto`**, a lemma, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L533).

> The scalar rpow approximation converges pointwise.
> `scalarRpowApprox q T x → rpowConst q * (x^q - 1)` as `T → ∞`.

```lean
lemma scalarRpowApprox_tendsto {x : ℝ} (hx : 0 < x) (hq : 0 < q) (hq1 : q < 1) :
    Filter.Tendsto (fun T => scalarRpowApprox q T x) atTop (nhds (rpowConst q * (x ^ q - 1)))
```

**`HermitianMat.tendsto_rpowApprox`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L580).

> The matrix rpow approximation converges: `rpowApprox A q T → rpowConst q • (A^q - 1)`.

```lean
lemma tendsto_rpowApprox (hA : A.mat.PosDef) (hq : 0 < q) (hq1 : q < 1) :
    Tendsto (rpowApprox A q) atTop (nhds (rpowConst q • (A ^ q - 1)))
```

**`HermitianMat.rpow_le_rpow_of_posDef`**, a theorem, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L612). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Loewner-Heinz for positive definite lower endpoint.
>
> This is the positive-definite core used to prove the positive-semidefinite statement by
> adding `ε • 1` and taking a limit.

```lean
theorem rpow_le_rpow_of_posDef (hA : A.mat.PosDef) (hAB : A ≤ B)
    (hq : 0 < q) (hq1 : q ≤ 1) : A ^ q ≤ B ^ q
```

**`HermitianMat.rpow_le_rpow_of_le`**, a theorem, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L627). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The **Löwner—Heinz theorem**: for matrices A and B, if `0 ≤ A ≤ B` and `0 < q ≤ 1`,
> then `A^q ≤ B^q`. That is, real roots are operator monotone.

```lean
theorem rpow_le_rpow_of_le (hA : 0 ≤ A) (hAB : A ≤ B)
    (hq : 0 < q) (hq1 : q ≤ 1) : A ^ q ≤ B ^ q
```

## Araki-Lieb-Thirring Inequality

> The next section proves the trace inequality
> `Tr[(B ^ r) (A ^ r) (B ^ r)] <= Tr[(B A B) ^ r]` for `0 < r <= 1`.
> The proof uses compound matrices to convert the multiplicative singular-value estimates
> into a weak log-majorization argument.

**`HermitianMat.lieb_thirring_le_one`**, a lemma, [line 1022](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L1022).

> Lieb-Thirring type inequality for positive semidefinite Hermitian matrices.
>
> For `0 < r <= 1`,
> `Tr[(B ^ r) (A ^ r) (B ^ r)] <= Tr[(B A B) ^ r]`, written using
> `HermitianMat.conj`.

```lean
lemma lieb_thirring_le_one
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A) (hB : 0 ≤ B)
    {r : ℝ} (hr0 : 0 < r) (hr1 : r ≤ 1) :
    ((A ^ r).conj (B ^ r).mat).trace ≤ ((A.conj B.mat) ^ r).trace
```

## Rotfel'd Trace Subadditivity

> For positive semidefinite `A`, `B` and `0 < p <= 1`, Rotfel'd's inequality says
> `Tr[(A + B) ^ p] <= Tr[A ^ p] + Tr[B ^ p]`.
>
> The proof here uses the same resolvent-integral representation as Loewner-Heinz, plus
> monotonicity of the trace after inserting square roots. A stronger version can be stated
> as a majorization theorem.

**`HermitianMat.trace_rpow_add_le`**, a lemma, [line 1300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean#L1300).

> Rotfel'd trace subadditivity for positive semidefinite Hermitian matrices.
>
> For `0 < p <= 1`, `Tr[(A + B) ^ p] <= Tr[A ^ p] + Tr[B ^ p]`.

```lean
lemma trace_rpow_add_le
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A) (hB : 0 ≤ B)
    (p : ℝ) (hp : 0 < p) (hp1 : p ≤ 1) :
    ((A + B) ^ p).trace ≤ (A ^ p).trace + (B ^ p).trace
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Sqrt](sqrt.md)
- [Majorization and weak log-majorization](../majorization.md)

## Proof depends on

- [Compound matrices on `HermitianMat`](compoundmatrix.md)
- [Properties of the matrix logarithm and exponential](logexp.md)
- [QuantumInfo.ForMathlib.HermitianMat.Unitary](unitary.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Rpow.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Rpow.lean)
