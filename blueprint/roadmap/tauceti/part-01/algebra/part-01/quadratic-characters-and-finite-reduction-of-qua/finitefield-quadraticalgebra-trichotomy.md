---
declaration: theorem
origin: cited
lean: FiniteField.quadraticAlgebra_trichotomy
statement: formalized
proof: formalized
---

# FiniteField.quadraticAlgebra_trichotomy

Over a finite field of odd cardinality, `F[X]/(X² - r)` is a product of two copies of
`F`, a field, or the ring of dual numbers; see `QuadraticAlgebra.trichotomy`.

```lean
FiniteField.quadraticAlgebra_trichotomy.{u_1} {F : Type u_1} [Field F] [Finite F]
  (hodd : Odd (Nat.card F)) (r : F) :
  Nonempty (QuadraticAlgebra F r 0 ≃ₐ[F] F × F) ∨
    IsField (QuadraticAlgebra F r 0) ∨ Nonempty (QuadraticAlgebra F r 0 ≃ₐ[F] DualNumber F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [QuadraticAlgebra.trichotomy](quadraticalgebra-trichotomy.md)

## Lean

Formalized in Tau Ceti as [`FiniteField.quadraticAlgebra_trichotomy`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#FiniteField.quadraticAlgebra_trichotomy).

## Sources

- [Tau Ceti documentation: `FiniteField.quadraticAlgebra_trichotomy`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#FiniteField.quadraticAlgebra_trichotomy)
- [Source of `FiniteField.quadraticAlgebra_trichotomy` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L123)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
