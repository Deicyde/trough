---
declaration: theorem
origin: cited
lean: Matrix.det_confluentVandermonde
statement: formalized
proof: formalized
---

# The confluent Vandermonde determinant

over every commutative ring,
`det (confluentVandermonde a m) = ∏_{i < j} (a j - a i) ^ (m i * m j)`, with the sign fixed by
the lexicographic row order and no injectivity hypothesis on `a`.

```lean
Matrix.det_confluentVandermonde.{u_1} {R : Type u_1} [CommRing R] {r : ℕ} (a : Fin r → R)
  (m : Fin r → ℕ) :
  (Matrix.confluentVandermonde a m).det = ∏ i, ∏ j, if i < j then (a j - a i) ^ (m i * m j) else 1
```

## Depends on

- [Matrix.confluentVandermonde](matrix-confluentvandermonde.md)

## Lean

Formalized in Tau Ceti as [`Matrix.det_confluentVandermonde`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.html#Matrix.det_confluentVandermonde).

## Sources

- [Tau Ceti documentation: `Matrix.det_confluentVandermonde`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.html#Matrix.det_confluentVandermonde)
- [Source of `Matrix.det_confluentVandermonde` in TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.lean#L153)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
