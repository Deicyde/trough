---
declaration: theorem
origin: cited
lean: MvPolynomial.mem_pow_comap_constantCoeff_iff_coeff_mem_pow
statement: formalized
proof: formalized
---

# Powers of augmented coefficient ideals

For any commutative semiring
`R`, ideal `I`, natural number `n`, arbitrary variable type `σ`, and polynomial
`p`, [`MvPolynomial.mem_pow_comap_constantCoeff_iff_coeff_mem_pow`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/AugmentedIdealPowers.lean)
characterizes membership in `(I.comap constantCoeff) ^ n`: the coefficient
at each exponent `d` belongs to `I ^ (n - d.sum (fun _ k => k))`.
Subtraction is truncated in `ℕ`, so degrees at least `n` impose no
restriction, rather than vanishing. Coefficients and variables have
independent universes; empty or infinite variables and trivial coefficient
semirings are allowed. The bottom coefficient ideal recovers Mathlib's
variable-ideal power criterion. The
[integer and boundary examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/CoefficientVariableIdeal.lean)
apply the criterion to `2 * X ∈ (2, X)²`, contrast the constant `2`, and
include the zeroth power and empty variables.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.mem_pow_comap_constantCoeff_iff_coeff_mem_pow` (theorem), declared in [MultivariatePolynomials/AugmentedIdealPowers.lean, line 150](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/AugmentedIdealPowers.lean#L150).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.mem_pow_comap_constantCoeff_iff_coeff_mem_pow` in MultivariatePolynomials/AugmentedIdealPowers.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/AugmentedIdealPowers.lean#L150)
