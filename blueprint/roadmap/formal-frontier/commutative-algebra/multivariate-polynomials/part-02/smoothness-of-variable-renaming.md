---
declaration: theorem
origin: cited
lean: MvPolynomial.rename_smooth_iff
statement: formalized
proof: formalized
---

# Smoothness of variable renaming

Over any commutative ring `R`,
[`MvPolynomial.rename_smooth_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameSmooth.lean)
says that the canonical homomorphism on full polynomial rings is smooth
exactly when the variable map is injective with finite complement, or `R`
is subsingleton. This is stock `RingHom.Smooth`, including finite
presentation, for the source-polynomial action induced by renaming.
Coefficients and both variable types have independent universes; no
finiteness or nontriviality hypothesis is imposed on them.
[`MvPolynomial.rename_smooth_iff_flat_and_finiteType`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameSmooth.lean)
compares smoothness with flatness and finite type for these renamings.
Five concrete settings in the same file distinguish the collision/flatness
obstruction from the infinite-complement/finite-type obstruction and exhibit
the zero-ring exception. A derived application uses the comparison to extract
flatness and finite type from an independent one-variable extension over `ℤ`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.rename_smooth_iff` (theorem), declared in [MultivariatePolynomials/RenameSmooth.lean, line 68](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameSmooth.lean#L68).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.rename_smooth_iff` in MultivariatePolynomials/RenameSmooth.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameSmooth.lean#L68)
