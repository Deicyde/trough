---
declaration: theorem
origin: cited
lean: Polynomial.isNoetherianRing_of_isNoetherianRing
statement: formalized
proof: formalized
---

# Hilbert basis theorem for left-Noetherian rings

[`Polynomial.isNoetherianRing_of_isNoetherianRing`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean)
proves `IsNoetherianRing (Polynomial R)` for any `R : Type u` with
`[Ring R]` and `[IsNoetherianRing R]`. The polynomial variable is central;
coefficient commutativity, nontriviality and absence of zero divisors are
not required. On commutative rings,
`Polynomial.isNoetherianRing_of_isNoetherianRing_eq_isNoetherianRing`
identifies this proof with Mathlib's `Polynomial.isNoetherianRing`.
For any finite type `σ : Type v`, the named theorem
`AddMonoidAlgebra.isNoetherianRing_finsupp` proves left Noetherianity of
`AddMonoidAlgebra R (σ →₀ ℕ)`, with independently polymorphic universes.
It permits zero and noncommutative coefficient rings. For commutative rings,
this is definitionally `MvPolynomial σ R`.
Here `IsNoetherianRing R` means `IsNoetherian R R` for the canonical left
self-action. It does not assume `IsNoetherian R (Polynomial R)`: that
coefficient-module property is false for every nontrivial coefficient ring.
The [examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/Noetherian.lean) include the
noncommutative 16-element ring `Matrix (Fin 2) (Fin 2) (ZMod 2)`, whose
polynomial ring is infinite but left-Noetherian, the zero ring `ZMod 1`,
and `ZMod 4` with its nonzero nilpotent `2`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.isNoetherianRing_of_isNoetherianRing` (theorem), declared in [MultivariatePolynomials/Noetherian.lean, line 245](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean#L245).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Polynomial.isNoetherianRing_of_isNoetherianRing` in MultivariatePolynomials/Noetherian.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean#L245)
