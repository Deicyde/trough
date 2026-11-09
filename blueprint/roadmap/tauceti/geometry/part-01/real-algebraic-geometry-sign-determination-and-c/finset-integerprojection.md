---
declaration: def
origin: cited
lean: Finset.integerProjection
statement: formalized
---

# Finset.integerProjection

The Collins projection of a finite family `P` of integer polynomials in the variables
`X 0, …, X n`, computed over `ℤ`: single out the distinguished variable `X 0` and take the Collins
projection of the resulting family of polynomials in `X 0` over `ℤ[X 1, …, X n]`.

```lean
Finset.integerProjection {n : ℕ} (P : Finset (MvPolynomial (Fin (n + 1)) ℤ)) :
  Finset (MvPolynomial (Fin n) ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.integerProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Integer.html#Finset.integerProjection).

## Sources

- [Tau Ceti documentation: `Finset.integerProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Integer.html#Finset.integerProjection)
- [Source of `Finset.integerProjection` in TauCeti/Geometry/RealAlgebraic/Projection/Integer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Projection/Integer.lean#L65)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
