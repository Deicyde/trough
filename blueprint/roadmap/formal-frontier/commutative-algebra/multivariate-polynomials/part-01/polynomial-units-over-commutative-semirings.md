---
declaration: theorem
origin: cited
lean: MvPolynomial.isUnit_iff_coeff_isNilpotent_isAddUnit
statement: formalized
proof: formalized
---

# Polynomial units over commutative semirings

For any commutative semiring
`R` and arbitrary variable type `σ`, a polynomial in `MvPolynomial σ R` is a
unit if and only if its constant coefficient is a unit and its coefficient at
every nonzero exponent is both nilpotent and additively invertible, by
[`MvPolynomial.isUnit_iff_coeff_isNilpotent_isAddUnit`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UnitCriterion.lean).
The coefficient and variable types have independent universes; empty variable
types and the zero semiring are included. The lemma
[`MvPolynomial.isUnit_coeff_zero_and_isNilpotent_isAddUnit_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UnitCriterion.lean)
identifies the coefficient conditions over a commutative ring with those in
Mathlib's `MvPolynomial.isUnit_iff`. The sufficiency direction remains available as
[`MvPolynomial.isUnit_of_coeff_isNilpotent_isAddUnit`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UnitSufficiency.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isUnit_iff_coeff_isNilpotent_isAddUnit` (theorem), declared in [MultivariatePolynomials/UnitCriterion.lean, line 40](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UnitCriterion.lean#L40).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isUnit_iff_coeff_isNilpotent_isAddUnit` in MultivariatePolynomials/UnitCriterion.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UnitCriterion.lean#L40)
