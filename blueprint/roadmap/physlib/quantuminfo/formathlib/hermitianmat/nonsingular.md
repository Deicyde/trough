---
declaration: module
origin: cited
lean: Matrix.isUnit_smul, Matrix.isUnit_natCast, Matrix.isUnit_real_smul, Matrix.isUnit_real_cast, HermitianMat.NonSingular, HermitianMat.isUnit_mat_of_nonSingular, HermitianMat.nonsingular_iff_isUnit, HermitianMat.instHasInv_of_invertible
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.NonSingular

The module `QuantumInfo.ForMathlib.HermitianMat.NonSingular`, [QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean): 34 declarations (1 instance with no name), 0 with a docstring.

**`Matrix.isUnit_smul`**, a lemma, [line 19](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L19).

```lean
lemma isUnit_smul {c : R} (hA : IsUnit c) {M : Matrix d d S} (hM : IsUnit M) :
    IsUnit (c • M : Matrix d d S)
```

**`Matrix.isUnit_natCast`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L26).

```lean
lemma isUnit_natCast {n : ℕ} (hn : n ≠ 0) [CharZero F] : IsUnit (n : Matrix d d F)
```

**`Matrix.isUnit_real_smul`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L29).

```lean
lemma isUnit_real_smul {r : ℝ} (hr : r ≠ 0) {M : Matrix d d 𝕜} (hM : IsUnit M) :
    IsUnit (r • M : Matrix d d 𝕜)
```

**`Matrix.isUnit_real_cast`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L33).

```lean
lemma isUnit_real_cast {r : ℝ} (hr : r ≠ 0) : IsUnit (r • 1 : Matrix d d 𝕜)
```

**`HermitianMat.NonSingular`**, a class, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L44).

```lean
class NonSingular (A : HermitianMat n R) : Prop where
  isUnit : IsUnit A.mat
```

**`HermitianMat.isUnit_mat_of_nonSingular`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L48).

```lean
lemma isUnit_mat_of_nonSingular [NonSingular A] : IsUnit A.mat
```

**`HermitianMat.nonsingular_iff_isUnit`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L51).

```lean
lemma nonsingular_iff_isUnit : NonSingular A ↔ IsUnit A.mat
```

**`HermitianMat.instHasInv_of_invertible`**, an instance, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L54).

```lean
instance instHasInv_of_invertible [i : Invertible A.mat] : NonSingular A
```

**`HermitianMat.instInvertible_of_hasInv`**, an instance, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L57).

```lean
instance instInvertible_of_hasInv [h : NonSingular A] : Invertible A.mat
```

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L60).

```lean
instance : NonSingular (1 : HermitianMat n R)
```

**`HermitianMat.nonSingular_of_posDef`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L66).

```lean
lemma nonSingular_of_posDef (hA : A.mat.PosDef) : NonSingular A
```

**`HermitianMat.nonSingular_iff_posDef_of_PSD`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L69).

```lean
lemma nonSingular_iff_posDef_of_PSD (hA : 0 ≤ A) :
    NonSingular A ↔ A.mat.PosDef
```

**`HermitianMat.nonSingular_smul`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L75).

```lean
lemma nonSingular_smul [i : NonSingular A] {c : ℝ} (hc : IsUnit c) : NonSingular (c • A)
```

**`HermitianMat.nonSingular_iff_zero_notMem_spectrum`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L78).

```lean
lemma nonSingular_iff_zero_notMem_spectrum : NonSingular A ↔ 0 ∉ spectrum ℝ A.mat
```

**`HermitianMat.nonSingular_iff_eigenvalue_ne_zero`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L81).

```lean
lemma nonSingular_iff_eigenvalue_ne_zero : NonSingular A ↔ ∀ i, A.H.eigenvalues i ≠ 0
```

**`HermitianMat.nonSingular_iff_det_ne_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L84).

```lean
lemma nonSingular_iff_det_ne_zero : NonSingular A ↔ A.mat.det ≠ 0
```

**`HermitianMat.nonSingular_iff_ker_bot`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L87).

```lean
lemma nonSingular_iff_ker_bot : NonSingular A ↔ A.ker = ⊥
```

**`HermitianMat.nonSingular_iff_support_top`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L113).

```lean
lemma nonSingular_iff_support_top : NonSingular A ↔ A.support = ⊤
```

**`HermitianMat.nonSingular_iff_neg`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L133).

```lean
lemma nonSingular_iff_neg : NonSingular (-A) ↔ NonSingular A
```

**`HermitianMat.nonSingular_iff_inv`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L137).

```lean
lemma nonSingular_iff_inv : NonSingular (A⁻¹) ↔ NonSingular A
```

**`HermitianMat.nonSingular_iff_kronecker`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L142).

```lean
lemma nonSingular_iff_kronecker [Nonempty n] [Nonempty m] :
    NonSingular (A ⊗ₖ B) ↔ NonSingular A ∧ NonSingular B
```

**`HermitianMat.nonSingular_iff_conj`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L146).

```lean
lemma nonSingular_iff_conj (hC : IsUnit C) : NonSingular (A.conj C) ↔ NonSingular A
```

**`HermitianMat.nonSingular_iff_reindex`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L150).

```lean
lemma nonSingular_iff_reindex (e : n ≃ m) : NonSingular (A.reindex e) ↔ NonSingular A
```

**`HermitianMat.nonSingular_empty`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L159).

```lean
lemma nonSingular_empty [IsEmpty n] : NonSingular A
```

**`HermitianMat.nonSingular_det_ne_zero`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L165).

```lean
lemma nonSingular_det_ne_zero : A.mat.det ≠ 0
```

**`HermitianMat.nonSingular_ker_bot`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L169).

```lean
lemma nonSingular_ker_bot : A.ker = ⊥
```

**`HermitianMat.nonSingular_support_top`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L173).

```lean
lemma nonSingular_support_top : A.support = ⊤
```

**`HermitianMat.nonSingular_neg`**, an instance, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L176).

```lean
instance nonSingular_neg : NonSingular (-A)
```

**`HermitianMat.nonSingular_inv`**, an instance, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L179).

```lean
instance nonSingular_inv : NonSingular (A⁻¹)
```

**`HermitianMat.nonSingular_kron`**, an instance, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L182).

```lean
instance nonSingular_kron [Nonempty n] [Nonempty m] : NonSingular (A ⊗ₖ B)
```

**`HermitianMat.nonSingular_conj`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L185).

```lean
lemma nonSingular_conj (hC : IsUnit C) : NonSingular (A.conj C)
```

**`HermitianMat.nonSingular_conj_isometry`**, an instance, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L188).

```lean
instance nonSingular_conj_isometry {B : HermitianMat n 𝕜} [NonSingular B] :
    NonSingular (A.conj B.mat)
```

**`HermitianMat.nonSingular_zero_notMem_spectrum`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L192).

```lean
lemma nonSingular_zero_notMem_spectrum : 0 ∉ spectrum ℝ A.mat
```

**`HermitianMat.nonSingular_eigenvalue_ne_zero`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean#L195).

```lean
lemma nonSingular_eigenvalue_ne_zero : ∀ i, A.H.eigenvalues i ≠ 0
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Order](order.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/NonSingular.lean)
