---
declaration: theorem
origin: cited
lean: NumberField.existsUnique_neg_squarefree_algEquiv
statement: formalized
proof: formalized
---

# The radicand classification of imaginary quadratic fields

Every totally complex number
field of degree `2` over `ℚ` is isomorphic to `QuadraticAlgebra ℚ d 0` for exactly one negative
squarefree integer `d`.

```lean
NumberField.existsUnique_neg_squarefree_algEquiv.{u_1} {K : Type u_1} [Field K] [NumberField K]
  [NumberField.IsTotallyComplex K] (hK : Module.finrank ℚ K = 2) :
  ∃! d, d < 0 ∧ Squarefree d ∧ Nonempty (K ≃ₐ[ℚ] QuadraticAlgebra ℚ (↑d) 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.existsUnique_neg_squarefree_algEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.html#NumberField.existsUnique_neg_squarefree_algEquiv).

## Sources

- [Tau Ceti documentation: `NumberField.existsUnique_neg_squarefree_algEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.html#NumberField.existsUnique_neg_squarefree_algEquiv)
- [Source of `NumberField.existsUnique_neg_squarefree_algEquiv` in TauCeti/NumberTheory/NumberField/Quadratic/Radicand.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.lean#L102)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
