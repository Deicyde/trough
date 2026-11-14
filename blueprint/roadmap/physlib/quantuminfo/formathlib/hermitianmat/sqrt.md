---
declaration: module
origin: cited
lean: HermitianMat.sqrt, HermitianMat.sqrt_sq_eq_proj, HermitianMat.sqrt_sq, HermitianMat.commute_sqrt_left, HermitianMat.commute_sqrt_right, HermitianMat.sqrt_inv_mul_self_mul_sqrt_inv_eq_one, HermitianMat.sqrt_nonneg, HermitianMat.sqrt_pos
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Sqrt

The module `QuantumInfo.ForMathlib.HermitianMat.Sqrt`, [QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean): 10 declarations, 3 with a docstring.

**`HermitianMat.sqrt`**, a def, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L22).

> The square root of a Hermitian matrix. Negative eigenvalues are mapped to zero.

```lean
noncomputable def sqrt (A : HermitianMat d 𝕜) : HermitianMat d 𝕜
```

**`HermitianMat.sqrt_sq_eq_proj`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L25).

```lean
lemma sqrt_sq_eq_proj (A : HermitianMat d 𝕜) :
    A.sqrt.mat * A.sqrt.mat = A⁺
```

**`HermitianMat.sqrt_sq`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L31).

```lean
lemma sqrt_sq (hA : 0 ≤ A) :
    A.sqrt.mat * A.sqrt.mat = A
```

**`HermitianMat.commute_sqrt_left`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L36).

```lean
lemma commute_sqrt_left (hAB : Commute A.mat B.mat) :
    Commute A.sqrt.mat B.mat
```

**`HermitianMat.commute_sqrt_right`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L42).

```lean
lemma commute_sqrt_right (hAB : Commute A.mat B.mat) :
    Commute A.mat B.sqrt.mat
```

**`HermitianMat.sqrt_inv_mul_self_mul_sqrt_inv_eq_one`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L49).

> For a positive definite matrix A, A^\{-1/2} * A * A^\{-1/2} = I.

```lean
lemma sqrt_inv_mul_self_mul_sqrt_inv_eq_one {A : HermitianMat d 𝕜} (hA : A.mat.PosDef) :
    A⁻¹.sqrt.mat * A.mat * A⁻¹.sqrt.mat = 1
```

**`HermitianMat.sqrt_nonneg`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L61).

```lean
lemma sqrt_nonneg (A : HermitianMat d 𝕜) : 0 ≤ A.sqrt
```

**`HermitianMat.sqrt_pos`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L65).

```lean
lemma sqrt_pos (h : 0 < A) : 0 < A.sqrt
```

**`HermitianMat.sqrt_posDef`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L69).

```lean
lemma sqrt_posDef {A : HermitianMat d 𝕜} (hA : A.mat.PosDef) :
    A.sqrt.mat.PosDef
```

**`HermitianMat.evalHermitianMatSqrt`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean#L77).

> Positivity extension for `HermitianMat.sqrt`

```lean
meta def evalHermitianMatSqrt : PositivityExt
```

## Depends on

- [Projectors associated to Hermitian matrices](proj.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Sqrt.lean)
