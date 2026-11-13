---
declaration: module
origin: cited
lean: HermitianMat.symmMul, HermitianMat.symmMul_comm, HermitianMat.symmMul_zero, HermitianMat.zero_symmMul, HermitianMat.symmMul_toMat, HermitianMat.symmMul_of_commute, HermitianMat.symmMul_self, HermitianMat.symmMul_one
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Jordan

The module `QuantumInfo.ForMathlib.HermitianMat.Jordan`, [QuantumInfo/ForMathlib/HermitianMat/Jordan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean): 19 declarations (7 instances with no name), 0 with a docstring.

> Hermitian matrices have a Jordan algebra structure given by
> `A * B := 2⁻¹ • (A.toMat * B.toMat + B.toMat * A.toMat)`. We call this operation
> `HermitianMat.symmMul`, but it's available as `*` multiplication scoped under
> `HermMul`. When `A` and `B` commute, this reduces to standard matrix multiplication.

**`HermitianMat.symmMul`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L30).

```lean
def symmMul : HermitianMat d 𝕜
```

**`HermitianMat.symmMul_comm`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L35).

```lean
lemma symmMul_comm : A.symmMul B = B.symmMul A
```

**`HermitianMat.symmMul_zero`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L40).

```lean
lemma symmMul_zero : A.symmMul 0 = 0
```

**`HermitianMat.zero_symmMul`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L45).

```lean
lemma zero_symmMul : symmMul 0 A = 0
```

**`HermitianMat.symmMul_toMat`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L48).

```lean
lemma symmMul_toMat : (A.symmMul B).mat =
    (2 : 𝕜)⁻¹ • (A.mat * B.mat + B.mat * A.mat)
```

**`HermitianMat.symmMul_of_commute`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L56).

```lean
lemma symmMul_of_commute (hAB : Commute A.mat B.mat) :
    (A.symmMul B).mat = A.mat * B.mat
```

**`HermitianMat.symmMul_self`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L62).

```lean
lemma symmMul_self : (symmMul A A).mat = A.mat * A.mat
```

**`HermitianMat.symmMul_one`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L68).

```lean
lemma symmMul_one : A.symmMul 1 = A
```

**`HermitianMat.one_symmMul`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L72).

```lean
lemma one_symmMul : symmMul 1 A = A
```

**`HermitianMat.symmMul_neg_one`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L76).

```lean
lemma symmMul_neg_one : A.symmMul (-1) = -A
```

**`HermitianMat.neg_one_symmMul`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L80).

```lean
lemma neg_one_symmMul : symmMul (-1) A = -A
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L93).

```lean
scoped instance : CommMagma (HermitianMat d 𝕜)
```

**`HermMul.mul_eq_symmMul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L101).

```lean
lemma mul_eq_symmMul : A * B = A.symmMul B
```

**An instance with no name**, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L104).

```lean
scoped instance : IsCommJordan (HermitianMat d 𝕜)
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L111).

```lean
scoped instance : MulZeroClass (HermitianMat d 𝕜)
```

**An instance with no name**, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L117).

```lean
scoped instance : MulZeroOneClass (HermitianMat d 𝕜)
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L127).

```lean
scoped instance : NonUnitalNonAssocRing (HermitianMat d 𝕜)
```

**An instance with no name**, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L139).

```lean
scoped instance : NonAssocCommRing (HermitianMat d 𝕜)
```

**An instance with no name**, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean#L148).

```lean
scoped instance : IsScalarTower ℝ (HermitianMat d 𝕜) (HermitianMat d 𝕜)
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Basic](basic.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Jordan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Jordan.lean)
