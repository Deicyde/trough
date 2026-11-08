---
declaration: theorem
origin: cited
lean: MvPolynomial.essFiniteType_rename_iff
statement: formalized
proof: formalized
---

# Variable renaming has an exact relative essentially finite-type criterion

[`MvPolynomial.essFiniteType_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameEssentialFiniteType.lean)
characterizes `RingHom.EssFiniteType` of renaming for arbitrary `f : σ → τ`
over a commutative ring `R`, with independent coefficient and variable
universes: `R` is subsingleton or `Set.Finite ((Set.range f)ᶜ)`. Scalars are
`MvPolynomial σ R`, acting on `MvPolynomial τ R` by `p • q = rename f p * q`.
Essential finite type is distinct from finite type, but their criteria
coincide for these maps. The
[worked applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameEssentialFiniteType.lean)
contrast successor renaming over `ℤ` (only `0` is missed), `Empty → ℕ`
with subsingleton coefficients (infinitely many missed variables), and
even-index renaming over `ℤ`, which is not essentially of finite type.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.essFiniteType_rename_iff` (theorem), declared in [MultivariatePolynomials/RenameEssentialFiniteType.lean, line 51](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameEssentialFiniteType.lean#L51).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.essFiniteType_rename_iff` in MultivariatePolynomials/RenameEssentialFiniteType.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameEssentialFiniteType.lean#L51)
