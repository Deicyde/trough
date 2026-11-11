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
- [Source of `FiniteField.quadraticAlgebra_trichotomy` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L123)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
