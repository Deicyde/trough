---
declaration: def
origin: cited
lean: QuadraticAlgebra.complexEmbedding
statement: formalized
---

# The distinguished complex embedding of `ℚ(√a)` for `a ≤ 0`

the `ℚ`-algebra map
`QuadraticAlgebra ℚ a 0 →ₐ[ℚ] ℂ` sending `ω` to `√(-a) · i`, the square root of `a` with
nonnegative imaginary part.

```lean
QuadraticAlgebra.complexEmbedding {a : ℚ} (ha : a ≤ 0) : QuadraticAlgebra ℚ a 0 →ₐ[ℚ] ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.complexEmbedding`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.complexEmbedding).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.complexEmbedding`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.complexEmbedding)
- [Source of `QuadraticAlgebra.complexEmbedding` in TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean#L69)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
