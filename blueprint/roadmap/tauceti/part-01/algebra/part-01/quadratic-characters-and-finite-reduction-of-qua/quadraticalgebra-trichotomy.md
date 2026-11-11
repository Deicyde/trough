---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.trichotomy
statement: formalized
proof: formalized
---

# QuadraticAlgebra.trichotomy

Over a field with `2 ≠ 0`, `K[X]/(X² - r)` is a product of two copies of `K`, a field, or
the ring of dual numbers. By `nonempty_algEquiv_prod_iff`, `isField_iff_not_isSquare` and
`nonempty_algEquiv_dualNumber_iff`, exactly one case occurs.

```lean
QuadraticAlgebra.trichotomy.{u_1} {K : Type u_1} [Field K] [NeZero 2] (r : K) :
  Nonempty (QuadraticAlgebra K r 0 ≃ₐ[K] K × K) ∨
    IsField (QuadraticAlgebra K r 0) ∨ Nonempty (QuadraticAlgebra K r 0 ≃ₐ[K] DualNumber K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [QuadraticAlgebra.isField_iff_not_isSquare](quadraticalgebra-isfield-iff-not-issquare.md)
- [QuadraticAlgebra.nonempty_algEquiv_prod_iff](quadraticalgebra-nonempty-algequiv-prod-iff.md)

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.trichotomy`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.trichotomy).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.trichotomy`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.trichotomy)
- [Source of `QuadraticAlgebra.trichotomy` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L86)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
