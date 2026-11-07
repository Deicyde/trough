---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.nrComplexPlaces_eq_one
statement: formalized
proof: formalized
---

# QuadraticAlgebra.nrComplexPlaces\_eq\_one

An imaginary quadratic field has exactly one complex place, so its signature is `(0, 1)`.

```lean
QuadraticAlgebra.nrComplexPlaces_eq_one {a : ℚ} [Fact ¬IsSquare a] (ha : a < 0) :
  NumberField.InfinitePlace.nrComplexPlaces (QuadraticAlgebra ℚ a 0) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.nrComplexPlaces_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.nrComplexPlaces_eq_one).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.nrComplexPlaces_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.nrComplexPlaces_eq_one)
- [Source of `QuadraticAlgebra.nrComplexPlaces_eq_one` in TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean#L197)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
