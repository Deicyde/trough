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
- [Source of `Matrix.minorGcd` in TauCeti/LinearAlgebra/Matrix/MaximalMinor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/MaximalMinor.lean#L152)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HeightsAndUnits/STATUS.md)
