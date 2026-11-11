---
declaration: def
origin: cited
lean: QuadraticAlgebra.algEquivDualNumberOfDoubleRoot
statement: formalized
---

# QuadraticAlgebra.algEquivDualNumberOfDoubleRoot

A quadratic algebra whose defining polynomial is `(X - r)²` is the ring of dual numbers,
with `ω ↦ r + ε`.

```lean
QuadraticAlgebra.algEquivDualNumberOfDoubleRoot.{u_1} {R : Type u_1} [CommRing R] {a b : R} (r : R)
  (ha : a = -r ^ 2) (hb : b = 2 * r) : QuadraticAlgebra R a b ≃ₐ[R] DualNumber R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.algEquivDualNumberOfDoubleRoot`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/DualNumber.html#QuadraticAlgebra.algEquivDualNumberOfDoubleRoot).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.algEquivDualNumberOfDoubleRoot`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/DualNumber.html#QuadraticAlgebra.algEquivDualNumberOfDoubleRoot)
- [Source of `QuadraticAlgebra.algEquivDualNumberOfDoubleRoot` in TauCeti/Algebra/QuadraticAlgebra/DualNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/DualNumber.lean#L71)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
