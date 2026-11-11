---
declaration: theorem
origin: cited
lean: Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq
statement: formalized
proof: formalized
---

# Every sublattice of `ℤ^m` has a unique Hermite basis

For every sublattice `L` of `ℤ^m`
there is exactly one pair `⟨k, H⟩` of a number `k` and a matrix `H` with `m` rows and `k` columns
in Hermite normal form whose column lattice is `L`.

```lean
Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq {m : ℕ} (L : Submodule ℤ (Fin m → ℤ)) :
  ∃! H, H.snd.IsHermiteNormalForm ∧ H.snd.mulVecLin.range = L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/HermiteNormalForm/Existence.html#Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq).

## Sources

- [Tau Ceti documentation: `Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/HermiteNormalForm/Existence.html#Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq)
- [Source of `Matrix.existsUnique_isHermiteNormalForm_range_mulVecLin_eq` in TauCeti/LinearAlgebra/Matrix/HermiteNormalForm/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/HermiteNormalForm/Existence.lean#L166)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
