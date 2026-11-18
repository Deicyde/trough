---
declaration: module
origin: cited
lean: HermitianMat.reindex, HermitianMat.mat_reindex, HermitianMat.reindex_refl, HermitianMat.reindex_reindex, HermitianMat.reindex_zero, HermitianMat.reindex_one, HermitianMat.reindex_add, HermitianMat.reindex_sub
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Reindex

The module `QuantumInfo.ForMathlib.HermitianMat.Reindex`, [QuantumInfo/ForMathlib/HermitianMat/Reindex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean): 15 declarations, none with a docstring.

> Much like `Matrix.reindex` and `Matrix.submatrix`, we can reindex a Hermitian matrix to get another
> Hermitian matrix; however, this only makes sense when both permutations are the same, accordingly,
> `HermitianMat.reindex` only takes one `Equiv` argument (as opposed to `Matrix.reindex`'s two).
>
> This file then gives relevant lemmas for simplifying this.

**`HermitianMat.reindex`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L26).

```lean
def reindex (e : d ≃ d₂) : HermitianMat d₂ 𝕜
```

**`HermitianMat.mat_reindex`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L30).

```lean
lemma mat_reindex : (A.reindex e).mat = A.mat.reindex e e
```

> Our simp-normal form for expressions involving `HermitianMat.reindex` is that we try to push
> the reindexing as far out as possible, so that it can be absorbed by `HermitianMat.trace`, or
> cancelled our in a `HermitianMat.inner`. In places where it commutes (like `HermitianMat.inner`)
> we push it to the right side. One downside is that we're not as likely to hit `reindex_one`.

**`HermitianMat.reindex_refl`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L39).

```lean
lemma reindex_refl (A : HermitianMat d 𝕜) :
    A.reindex (.refl _) = A
```

**`HermitianMat.reindex_reindex`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L44).

```lean
lemma reindex_reindex (A : HermitianMat d 𝕜) (e : d ≃ d₂) (f : d₂ ≃ d₃) :
    (A.reindex e).reindex f = A.reindex (e.trans f)
```

**`HermitianMat.reindex_zero`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L49).

```lean
lemma reindex_zero : (0 : HermitianMat d 𝕜).reindex e = 0
```

**`HermitianMat.reindex_one`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L53).

```lean
lemma reindex_one [DecidableEq d] [DecidableEq d₂] :
    (1 : HermitianMat d 𝕜).reindex e = 1
```

**`HermitianMat.reindex_add`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L59).

```lean
lemma reindex_add : A.reindex e + B.reindex e = (A + B).reindex e
```

**`HermitianMat.reindex_sub`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L63).

```lean
lemma reindex_sub  : A.reindex e - B.reindex e = (A - B).reindex e
```

**`HermitianMat.reindex_neg`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L67).

```lean
lemma reindex_neg : (-A).reindex e = -(A.reindex e)
```

**`HermitianMat.reindex_smul`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L71).

```lean
lemma reindex_smul (c : ℝ) : (c • A).reindex e = c • (A.reindex e)
```

**`HermitianMat.reindex_conj`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L75).

```lean
lemma reindex_conj [Fintype d₂] [Fintype d] (B : Matrix d₃ d₂ 𝕜) :
    (A.reindex e).conj B = A.conj (B.submatrix id e)
```

**`HermitianMat.conj_submatrix`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L86).

```lean
lemma conj_submatrix (B : Matrix d₂ d₄ 𝕜) (e : d₃ ≃ d₂) (f : d → d₄) :
    A.conj (B.submatrix e f) = (A.conj (B.submatrix id f)).reindex e.symm
```

**`HermitianMat.reindex_eq_conj`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L92).

```lean
lemma reindex_eq_conj [DecidableEq d] (e : d ≃ d₂) :
    A.reindex e = A.conj (Matrix.reindex e (.refl d) 1)
```

**`HermitianMat.ker_reindex`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L101).

```lean
lemma ker_reindex :
    (A.reindex e).ker = A.ker.comap (LinearEquiv.euclideanOfRelabel 𝕜 e).toLinearMap
```

**`HermitianMat.ker_reindex_le_iff`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean#L108).

```lean
lemma ker_reindex_le_iff :
    (A.reindex e).ker ≤ (B.reindex e).ker ↔ A.ker ≤ B.ker
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Basic](basic.md)
- [Relabelling linear equivalences](../linearequiv.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Reindex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Reindex.lean)
