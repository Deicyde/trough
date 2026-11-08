---
declaration: def
origin: cited
lean: MvPolynomial.projectivize
statement: formalized
---

# Homogeneous polynomial maps on projective coordinate spaces

[`MvPolynomial.projectivize`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Projectivization.lean)
sends a nonzero tuple's class to the class of its polynomial evaluation tuple.
The coefficients may lie in any commutative semiring equipped with a homomorphism
to the field of points. A common homogeneity degree and nonvanishing on nonzero
input tuples make this map well-defined; its values on these classes characterize
it uniquely. Coordinate variables induce the identity, and homogeneous
substitution induces composition. The coordinate types may be infinite or empty,
their universes are independent, and the degree may be zero. With coefficients
in the field of points, finite coordinates and admissible absolute values, the
[projective height comparisons](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Height/Projectivization.lean)
descend the tuple bounds under the same algebraic-closure common-zero condition.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.projectivize` (def), declared in [MultivariatePolynomials/Projectivization.lean, line 74](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Projectivization.lean#L74).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.projectivize` in MultivariatePolynomials/Projectivization.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Projectivization.lean#L74)
