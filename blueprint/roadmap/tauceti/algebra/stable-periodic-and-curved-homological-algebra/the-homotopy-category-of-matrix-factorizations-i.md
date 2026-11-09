---
declaration: theorem
origin: cited
lean: TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated
statement: formalized
proof: formalized
---

# The homotopy category of matrix factorizations is triangulated, with the shift by `1` given by the parity shift

```lean
TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated.{u} (S : Type u) [CommRing S]
  (w : S) : CategoryTheory.IsTriangulated TauCeti.MatrixFactorization.HomotopyCategory
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [Happel's theorem](happels-theorem.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated`](https://taucetiproject.org/docs/TauCeti/CommutativeAlgebra/MatrixFactorization/Triangulated.html#TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated).

## Sources

- [Tau Ceti documentation: `TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated`](https://taucetiproject.org/docs/TauCeti/CommutativeAlgebra/MatrixFactorization/Triangulated.html#TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated)
- [Source of `TauCeti.MatrixFactorization.HomotopyCategory.instIsTriangulated` in TauCeti/CommutativeAlgebra/MatrixFactorization/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CommutativeAlgebra/MatrixFactorization/Triangulated.lean#L99)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
