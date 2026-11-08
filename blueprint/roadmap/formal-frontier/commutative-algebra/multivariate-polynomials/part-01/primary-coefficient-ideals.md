---
declaration: theorem
origin: cited
lean: MvPolynomial.isPrimary_map_C_of_subtractive
statement: formalized
proof: formalized
---

# Primary coefficient ideals

Over any commutative semiring `R`,
[`MvPolynomial.isPrimary_map_C_of_subtractive`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Primary.lean)
extends a primary ideal `I` satisfying `a ∈ I → a + b ∈ I → b ∈ I` to a
primary coefficient ideal, for every variable type `σ`. When `σ` is nonempty,
[`MvPolynomial.isPrimary_map_C_iff_subtractive`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Primary.lean)
proves that primaryness and this subtractivity condition are also necessary.
For a commutative ring, subtractivity is automatic, and
[`MvPolynomial.isPrimary_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Primary.lean)
gives the equivalence without any restriction on `σ`. Coefficients and
variables have independent universes; empty variable types and the unit ideal
are included, with no Noetherian or nontriviality hypothesis. The
[integer example](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/Primary.lean) extends the
primary, nonradical ideal `(4)`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isPrimary_map_C_of_subtractive` (theorem), declared in [MultivariatePolynomials/Primary.lean, line 71](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Primary.lean#L71).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isPrimary_map_C_of_subtractive` in MultivariatePolynomials/Primary.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Primary.lean#L71)
