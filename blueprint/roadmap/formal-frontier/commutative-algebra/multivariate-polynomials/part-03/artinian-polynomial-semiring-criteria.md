---
declaration: theorem
origin: cited
lean: Polynomial.isArtinianRing_iff
statement: formalized
proof: formalized
---

# Artinian polynomial-semiring criteria

For any `R : Type u` with
`[Semiring R]`, including noncommutative coefficients,
[`Polynomial.isArtinianRing_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Artinian.lean)
proves `IsArtinianRing (Polynomial R) ↔ Subsingleton R`.
For arbitrary variable types `σ : Type u` and coefficients `R : Type v`
with `[CommSemiring R]`,
[`MvPolynomial.isArtinianRing_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Artinian.lean)
proves `IsArtinianRing (MvPolynomial σ R) ↔ IsArtinianRing R ∧
(IsEmpty σ ∨ Subsingleton R)`. Both use polynomial multiplication on the
canonical left self-module, not the coefficient `R`-module action.
All universes are arbitrary; the multivariate universes are independent.
No ring or finite-variable hypothesis is imposed. Empty multivariate
variables recover coefficient Artinianity; trivial coefficients make every
polynomial zero. The [univariate applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/PolynomialArtinianClient.lean)
include the usual non-ring semiring `ℝ≥0`, the noncommutative 16-element
matrix ring over `ZMod 2`, and the zero ring `ZMod 1`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.isArtinianRing_iff` (theorem), declared in [MultivariatePolynomials/Artinian.lean, line 103](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Artinian.lean#L103).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Polynomial.isArtinianRing_iff` in MultivariatePolynomials/Artinian.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Artinian.lean#L103)
