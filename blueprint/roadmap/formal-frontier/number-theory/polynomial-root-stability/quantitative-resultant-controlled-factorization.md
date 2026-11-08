---
declaration: theorem
origin: cited
lean: Polynomial.exists_factorization_of_supNorm_lt_resultant_sq
statement: formalized
proof: formalized
---

# Quantitative resultant-controlled factorization

Let `K` be a complete ultrametric normed field, and let `f, g₀, h₀ : K[X]`.
Write `m = g₀.natDegree`, `n = h₀.natDegree`, `e = f - g₀ * h₀`,
`δ = e.supNorm` and `r = ‖g₀.resultant h₀‖`, using the natural-degree resultant.
Assume `g₀.supNorm ≤ 1`, `h₀.supNorm ≤ 1`, `e.degree < (m + n : WithBot ℕ)`
and `δ < r²`. Then
[`Polynomial.exists_factorization_of_supNorm_lt_resultant_sq`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ResultantFactorization.lean)
gives `f = g * h`, preserving each initial factor's degree and leading coefficient.
The corrections have degrees strictly less than `m` and `n`, both factors have
sup norm at most one, and both correction sup norms are at most `δ / r`.

There is no monicity, norm-one-leading-coefficient, characteristic-zero, discreteness,
nontrivial-norm or positive-factor-degree assumption. The strict degree bounds use
`WithBot ℕ`, so degree less than zero forces the zero polynomial. In particular,
both constant initial factors force zero error, and zero error returns the
initial factors. The proof uses the initial Sylvester inverse, finite coefficient
coordinates and Mathlib's Banach fixed-point theorem.

The [5-adic example](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/ResultantFactorization.lean) uses
`g₀ = 5X² + 2`, `h₀ = 5X² + 7` and `f = g₀h₀ + 5⁹X`. Its independently proved
inputs give `r = 5⁻⁴`, `δ = 5⁻⁹` and correction bounds `5⁻⁵`. The full-output client
produces degree-two factors with leading coefficients `5` and these correction
bounds. The leading coefficients and resultant are nonunits in the valuation
integer ring, not in the field.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.exists_factorization_of_supNorm_lt_resultant_sq` (theorem), declared in [PolynomialRootStability/ResultantFactorization.lean, line 214](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ResultantFactorization.lean#L214).

Read from the source at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), without running Lean.

## Sources

- [polynomial-root-stability at efade497: README, headline results](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results)
- [Source of `Polynomial.exists_factorization_of_supNorm_lt_resultant_sq` in PolynomialRootStability/ResultantFactorization.lean](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ResultantFactorization.lean#L214)
