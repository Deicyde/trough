---
declaration: theorem
origin: cited
lean: Ideal.jacobson_map_mvPolynomial_C
statement: formalized
proof: formalized
---

# Jacobson radicals of coefficient ideals

For any commutative ring `R`,
ideal `I` and nonempty variable type `σ`,
[`Ideal.jacobson_map_mvPolynomial_C`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Jacobson.lean)
identifies `Ideal.jacobson (I.map C)` with `I.radical.map C`.
In particular, the Jacobson radical of zero in `MvPolynomial σ R` is its
nilradical. Coefficient and variable universes are independent; no
Jacobson-ring, Noetherian, properness or nontriviality hypothesis is needed.
The [integer example](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/Jacobson.lean) separates
the extended ideal `(4)` from its proper Jacobson radical using `2 * X`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.jacobson_map_mvPolynomial_C` (theorem), declared in [MultivariatePolynomials/Jacobson.lean, line 87](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Jacobson.lean#L87).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Ideal.jacobson_map_mvPolynomial_C` in MultivariatePolynomials/Jacobson.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Jacobson.lean#L87)
