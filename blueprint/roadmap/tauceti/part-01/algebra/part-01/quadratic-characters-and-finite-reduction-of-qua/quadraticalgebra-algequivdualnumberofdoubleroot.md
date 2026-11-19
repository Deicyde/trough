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
- [Source of `QuadraticAlgebra.algEquivDualNumberOfDoubleRoot` in TauCeti/Algebra/QuadraticAlgebra/DualNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/QuadraticAlgebra/DualNumber.lean#L71)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
