---
declaration: theorem
origin: cited
lean: MvPolynomial.rename_formallySmooth_iff_injective
statement: formalized
proof: formalized
---

# Formal smoothness of variable renaming

Over any commutative ring `R`,
[`MvPolynomial.rename_formallySmooth_iff_injective`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFormalSmoothness.lean)
characterizes formal smoothness of the full source polynomial-ring
homomorphism by injectivity of that homomorphism. Equivalently,
[`MvPolynomial.rename_formallySmooth_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFormalSmoothness.lean)
says that the variable map is injective or the coefficients are subsingleton.
The scalar action is induced by the original renaming, not just by `R`.
The coefficient and variable types have independent universes, with no
finiteness or nontriviality hypotheses. Complementary variables give the
polynomial-extension direction; a square-zero lifting obstruction detects
collisions over nontrivial coefficients.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.rename_formallySmooth_iff_injective` (theorem), declared in [MultivariatePolynomials/RenameFormalSmoothness.lean, line 221](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFormalSmoothness.lean#L221).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.rename_formallySmooth_iff_injective` in MultivariatePolynomials/RenameFormalSmoothness.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFormalSmoothness.lean#L221)
