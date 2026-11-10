---
declaration: theorem
origin: cited
lean: MvPolynomial.formallyUnramified_rename_iff_surjective
statement: formalized
proof: formalized
---

# Formal unramifiedness of variable renaming

Over any commutative ring
`R`, [`MvPolynomial.formallyUnramified_rename_iff_surjective`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameUnramified.lean)
says that `MvPolynomial.rename f`, as a homomorphism from the full source
polynomial ring, is formally unramified exactly when it is surjective:
equivalently, when `f` is surjective or `R` is subsingleton. The coefficient
and variable types may lie in independent universes, and neither variable
type must be finite or inhabited. The [private boundary models](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameUnramified.lean)
include a collision of variables over the integers, an omitted variable over
the integers, and an omitted variable over `ZMod 1`. The collision uses
`MvPolynomial.formallyUnramified_rename_iff_moduleFinite`, with the full source
polynomial ring acting by multiplication by the renamed polynomial.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.formallyUnramified_rename_iff_surjective` (theorem), declared in [MultivariatePolynomials/RenameUnramified.lean, line 59](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameUnramified.lean#L59).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.formallyUnramified_rename_iff_surjective` in MultivariatePolynomials/RenameUnramified.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameUnramified.lean#L59)
