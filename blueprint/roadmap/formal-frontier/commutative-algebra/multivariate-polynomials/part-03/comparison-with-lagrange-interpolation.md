---
declaration: theorem
origin: cited
lean: MvPolynomial.uniqueAlgEquiv_eq_interpolate_of_eval_eq
statement: formalized
proof: formalized
---

# Comparison with Lagrange interpolation

Over a field, for a unique
variable type, a polynomial taking prescribed values at distinct nodes and
having total degree strictly below the number of nodes maps to Mathlib's
Lagrange interpolant under the canonical single-variable equivalence
([`MvPolynomial.uniqueAlgEquiv_eq_interpolate_of_eval_eq`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LagrangeComparison.lean)).
The univariate degree bound follows from the total-degree bound. On a
nonempty selection, the bound `s.card - 1` also suffices, so the comparison
applies to any bounded witness supplied by the commutative-ring existence
theorem. Zero agrees with the empty interpolant separately; an arbitrary
degree-zero witness need not do so.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.uniqueAlgEquiv_eq_interpolate_of_eval_eq` (theorem), declared in [MultivariatePolynomials/LagrangeComparison.lean, line 41](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LagrangeComparison.lean#L41).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.uniqueAlgEquiv_eq_interpolate_of_eval_eq` in MultivariatePolynomials/LagrangeComparison.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LagrangeComparison.lean#L41)
