---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.isField_iff_not_isSquare
statement: formalized
proof: formalized
---

# QuadraticAlgebra.isField_iff_not_isSquare

`K[X]/(X² - r)` is a field exactly when `r` is not a square in `K`. Unlike the
discriminant criterion `isField_iff_not_isSquare_discr`, this needs no assumption on the
characteristic.

```lean
QuadraticAlgebra.isField_iff_not_isSquare.{u_1} {K : Type u_1} [Field K] {r : K} :
  IsField (QuadraticAlgebra K r 0) ↔ ¬IsSquare r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.isField_iff_not_isSquare`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.isField_iff_not_isSquare).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.isField_iff_not_isSquare`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.isField_iff_not_isSquare)
- [Source of `QuadraticAlgebra.isField_iff_not_isSquare` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L48)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
