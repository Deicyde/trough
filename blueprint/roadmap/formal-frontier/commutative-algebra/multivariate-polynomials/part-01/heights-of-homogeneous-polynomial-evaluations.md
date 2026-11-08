---
declaration: theorem
origin: cited
lean: Height.exists_logHeight_eval_sub_mul_bound
statement: formalized
proof: formalized
---

# Heights of homogeneous polynomial evaluations

Over any field with
`Height.AdmissibleAbsValues`, a homogeneous polynomial family of common degree
`d`, with finite input and output coordinate types and no nonzero common zero
over an algebraic closure, has evaluation height uniformly comparable to the
input height raised to `d`. More precisely,
[`Height.exists_logHeight_eval_sub_mul_bound`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Height/Homogeneous.lean)
bounds the difference between evaluation logarithmic height and `d` times input
logarithmic height, while
[`Height.exists_mulHeight_eval_bounds`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Height/Homogeneous.lean)
bounds positive multiplicative height above and below by reciprocal constant
factors, with comparison constant at least one. The coordinate universes are
independent. Zero tuples, degree zero and empty coordinate types are included.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Height.exists_logHeight_eval_sub_mul_bound` (theorem), declared in [MultivariatePolynomials/Height/Homogeneous.lean, line 40](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Height/Homogeneous.lean#L40).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Height.exists_logHeight_eval_sub_mul_bound` in MultivariatePolynomials/Height/Homogeneous.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Height/Homogeneous.lean#L40)
