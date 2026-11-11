---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.nonempty_algEquiv_prod_iff
statement: formalized
proof: formalized
---

# QuadraticAlgebra.nonempty_algEquiv_prod_iff

Over a field with `2 ≠ 0`, `K[X]/(X² - r)` splits as `K × K` exactly when `r` is a
nonzero square.

```lean
QuadraticAlgebra.nonempty_algEquiv_prod_iff.{u_1} {K : Type u_1} [Field K] {r : K} [NeZero 2] :
  Nonempty (QuadraticAlgebra K r 0 ≃ₐ[K] K × K) ↔ IsSquare r ∧ r ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [QuadraticAlgebra.algEquivDualNumberOfDoubleRoot](quadraticalgebra-algequivdualnumberofdoubleroot.md)
- [QuadraticAlgebra.isField_iff_not_isSquare](quadraticalgebra-isfield-iff-not-issquare.md)

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.nonempty_algEquiv_prod_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.nonempty_algEquiv_prod_iff).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.nonempty_algEquiv_prod_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.html#QuadraticAlgebra.nonempty_algEquiv_prod_iff)
- [Source of `QuadraticAlgebra.nonempty_algEquiv_prod_iff` in TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/Trichotomy.lean#L61)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
