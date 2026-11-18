---
declaration: module
origin: cited
lean: HermitianMat.compoundHermitian, HermitianMat.compoundHermitian_eigenvalues, HermitianMat.compoundHermitian_nonneg, HermitianMat.compoundHermitian_conj
statement: formalized
proof: formalized
---

# Compound matrices on `HermitianMat`

The module `QuantumInfo.ForMathlib.HermitianMat.CompoundMatrix`, [QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean): 4 declarations, 4 with a docstring.

> This file lifts the compound-matrix construction from
> `QuantumInfo.ForMathlib.Majorization` to `HermitianMat`. The compound matrix of
> a Hermitian matrix is again Hermitian, and inherits the natural spectral and
> positivity properties of the original.

**`HermitianMat.compoundHermitian`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean#L29).

> The `k`-th compound matrix of a Hermitian matrix, packaged as a
> `HermitianMat`.

```lean
noncomputable def compoundHermitian (A : HermitianMat d ℂ) (k : ℕ) :
    HermitianMat {S : Finset d // S.card = k} ℂ
```

**`HermitianMat.compoundHermitian_eigenvalues`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean#L37).

> The eigenvalues of `compoundHermitian A k` are the products of eigenvalues
> of `A` over `k`-subsets, up to an index permutation.

```lean
lemma compoundHermitian_eigenvalues (A : HermitianMat d ℂ) (k : ℕ) :
    ∃ σ : {S : Finset d // S.card = k} ≃ {S : Finset d // S.card = k},
      (compoundHermitian A k).H.eigenvalues ∘ σ =
        fun S => ∏ i : Fin k, A.H.eigenvalues (S.1.orderEmbOfFin S.2 i)
```

**`HermitianMat.compoundHermitian_nonneg`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean#L49).

> `compoundHermitian` preserves positive semidefiniteness.

```lean
lemma compoundHermitian_nonneg (A : HermitianMat d ℂ) (hA : 0 ≤ A) (k : ℕ) :
    0 ≤ compoundHermitian A k
```

**`HermitianMat.compoundHermitian_conj`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean#L61).

> `compoundHermitian` distributes over `HermitianMat.conj`: the compound of
> `A.conj B` equals the conjugation of `compoundHermitian A k` by `compoundMatrix B k`.

```lean
lemma compoundHermitian_conj (A : HermitianMat d ℂ) (B : Matrix d d ℂ) (k : ℕ) :
    compoundHermitian (A.conj B) k =
      (compoundHermitian A k).conj (compoundMatrix B k)
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Order](order.md)
- [Majorization and weak log-majorization](../majorization.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CompoundMatrix.lean)
