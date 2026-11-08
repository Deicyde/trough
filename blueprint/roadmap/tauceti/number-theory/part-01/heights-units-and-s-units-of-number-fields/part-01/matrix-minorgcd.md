---
declaration: def
origin: cited
lean: Matrix.minorGcd
statement: formalized
---

# Matrix.minorGcd

The gcd of the maximal minors of `A`: the normalized gcd of the determinants
`det (A.submatrix id e)` over all embeddings `e : m ↪ n`. It is `0` exactly when every maximal
minor vanishes, in particular when `n` has fewer elements than `m`.

```lean
Matrix.minorGcd.{u_1, u_2, u_3} {m : Type u_1} {n : Type u_2} {R : Type u_3} [Fintype m]
  [DecidableEq m] [Fintype n] [CommRing R] [NormalizedGCDMonoid R] (A : Matrix m n R) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.minorGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/MaximalMinor.html#Matrix.minorGcd).

## Sources

- [Tau Ceti documentation: `Matrix.minorGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/MaximalMinor.html#Matrix.minorGcd)
- [Source of `Matrix.minorGcd` in TauCeti/LinearAlgebra/Matrix/MaximalMinor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/MaximalMinor.lean#L84)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
