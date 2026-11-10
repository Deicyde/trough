---
declaration: theorem
origin: cited
lean: MvPolynomial.isAlgebraic_rename_iff
statement: formalized
proof: formalized
---

# Algebraicity of polynomial variable renaming

Over any commutative ring `R`,
[`MvPolynomial.isAlgebraic_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean)
states that the full target polynomial ring is algebraic over the full source
via the specified renaming exactly when the coefficients are nontrivial and
the variable map is surjective or noninjective. A collision gives a nonzero
constant annihilator, even when a target variable is missed; zero coefficients
give no such polynomial, even for identity renaming. This is weak algebraicity,
not integrality or module finiteness. The coefficient and both variable types
have independent universes, with no additional ring or finiteness hypotheses.
[Criterion applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean)
are colocated with the public result. The independent
[positive models](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean)
and [negative models](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean)
use stock Mathlib directly for algebraicity. The shifted-projection models over
the integers and `ZMod 4` use the existing integrality criterion for their
missing-variable nonintegrality proofs:
[`MvPolynomial.isIntegral_X_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameIntegral.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isAlgebraic_rename_iff` (theorem), declared in [MultivariatePolynomials/RenameAlgebraic.lean, line 129](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean#L129).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isAlgebraic_rename_iff` in MultivariatePolynomials/RenameAlgebraic.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameAlgebraic.lean#L129)
