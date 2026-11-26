---
declaration: module
origin: cited
lean: HermitianMat.symmMul, HermitianMat.symmMul_comm, HermitianMat.symmMul_zero, HermitianMat.zero_symmMul, HermitianMat.symmMul_toMat, HermitianMat.symmMul_of_commute, HermitianMat.symmMul_self, HermitianMat.symmMul_one
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Jordan

The module `QuantumInfo.ForMathlib.HermitianMat.Jordan`, [QuantumInfo/ForMathlib/HermitianMat/Jordan.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean): 19 declarations (7 instances with no name), none with a docstring.

> Hermitian matrices have a Jordan algebra structure given by
> `A * B := 2⁻¹ • (A.toMat * B.toMat + B.toMat * A.toMat)`. We call this operation
> `HermitianMat.symmMul`, but it's available as `*` multiplication scoped under
> `HermMul`. When `A` and `B` commute, this reduces to standard matrix multiplication.

**`HermitianMat.symmMul`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L30).

```lean
def symmMul : HermitianMat d 𝕜
```

**`HermitianMat.symmMul_comm`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L42).

```lean
lemma symmMul_comm : A.symmMul B = B.symmMul A
```

**`HermitianMat.symmMul_zero`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L47).

```lean
lemma symmMul_zero : A.symmMul 0 = 0
```

**`HermitianMat.zero_symmMul`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L52).

```lean
lemma zero_symmMul : symmMul 0 A = 0
```

**`HermitianMat.symmMul_toMat`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L55).

```lean
lemma symmMul_toMat : (A.symmMul B).mat =
    (2 : 𝕜)⁻¹ • (A.mat * B.mat + B.mat * A.mat)
```

**`HermitianMat.symmMul_of_commute`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L63).

```lean
lemma symmMul_of_commute (hAB : Commute A.mat B.mat) :
    (A.symmMul B).mat = A.mat * B.mat
```

**`HermitianMat.symmMul_self`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L69).

```lean
lemma symmMul_self : (symmMul A A).mat = A.mat * A.mat
```

**`HermitianMat.symmMul_one`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L75).

```lean
lemma symmMul_one : A.symmMul 1 = A
```

**`HermitianMat.one_symmMul`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L79).

```lean
lemma one_symmMul : symmMul 1 A = A
```

**`HermitianMat.symmMul_neg_one`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L83).

```lean
lemma symmMul_neg_one : A.symmMul (-1) = -A
```

**`HermitianMat.neg_one_symmMul`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L87).

```lean
lemma neg_one_symmMul : symmMul (-1) A = -A
```

**An instance with no name**, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L100).

```lean
scoped instance : CommMagma (HermitianMat d 𝕜)
```

**`HermMul.mul_eq_symmMul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L108).

```lean
lemma mul_eq_symmMul : A * B = A.symmMul B
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L111).

```lean
scoped instance : IsCommJordan (HermitianMat d 𝕜)
```

**An instance with no name**, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L118).

```lean
scoped instance : MulZeroClass (HermitianMat d 𝕜)
```

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L124).

```lean
scoped instance : MulZeroOneClass (HermitianMat d 𝕜)
```

**An instance with no name**, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L134).

```lean
scoped instance : NonUnitalNonAssocRing (HermitianMat d 𝕜)
```

**An instance with no name**, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L146).

```lean
scoped instance : NonAssocCommRing (HermitianMat d 𝕜)
```

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L155).

```lean
scoped instance : IsScalarTower ℝ (HermitianMat d 𝕜) (HermitianMat d 𝕜)
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Basic](basic.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Jordan.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean)
