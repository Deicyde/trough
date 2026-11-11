---
declaration: theorem
origin: cited
lean: TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated
statement: formalized
proof: formalized
---

# The cokernel functor of matrix factorizations is a triangle functor

For a
non-zero-divisor `w` of a commutative ring `S`, the functor `HMF(S,w) ⥤ stable(Gproj-S/(w))`
sending a matrix factorization to the cokernel of its reduction modulo `w` is a triangle functor
for the triangulation of `HMF(S,w)` by the parity shift and Happel's triangulation of the stable
category of Gorenstein-projective `S/(w)`-modules.

```lean
TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated.{u}
  {S : Type u} [CommRing S] {w : S} (hw : w ∈ nonZeroDivisors S) :
  (TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel
      hw).IsTriangulated
```

## Depends on

- [Happel's theorem](happels-theorem.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated`](https://taucetiproject.org/docs/TauCeti/CommutativeAlgebra/MatrixFactorization/Cokernel/Triangulated.html#TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated).

## Sources

- [Tau Ceti documentation: `TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated`](https://taucetiproject.org/docs/TauCeti/CommutativeAlgebra/MatrixFactorization/Cokernel/Triangulated.html#TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated)
- [Source of `TauCeti.MatrixFactorization.HomotopyCategory.quotientGorensteinProjectiveStableCokernel_isTriangulated` in TauCeti/CommutativeAlgebra/MatrixFactorization/Cokernel/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CommutativeAlgebra/MatrixFactorization/Cokernel/Triangulated.lean#L200)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
