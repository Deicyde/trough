---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.ringHom_eq_or_eq_conjugate
statement: formalized
proof: formalized
---

# The two complex embeddings of an imaginary quadratic field

For a nonsquare `a ≤ 0`, every
complex embedding of the field `QuadraticAlgebra ℚ a 0` is the distinguished embedding or its
complex conjugate.

```lean
QuadraticAlgebra.ringHom_eq_or_eq_conjugate {a : ℚ} [Fact ¬IsSquare a] (ha : a ≤ 0)
  (φ : QuadraticAlgebra ℚ a 0 →+* ℂ) :
  φ = ↑(QuadraticAlgebra.complexEmbedding ha) ∨
    φ = NumberField.ComplexEmbedding.conjugate ↑(QuadraticAlgebra.complexEmbedding ha)
```

## Depends on

- [The distinguished complex embedding of `ℚ(√a)` for `a ≤ 0`](the-distinguished-complex-embedding-of-q-a-for-a.md)

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.ringHom_eq_or_eq_conjugate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.ringHom_eq_or_eq_conjugate).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.ringHom_eq_or_eq_conjugate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.html#QuadraticAlgebra.ringHom_eq_or_eq_conjugate)
- [Source of `QuadraticAlgebra.ringHom_eq_or_eq_conjugate` in TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/ComplexEmbedding.lean#L162)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
