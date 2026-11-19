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
- [Source of `QuadraticAlgebra.isField_iff_not_isSquare` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L48)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
