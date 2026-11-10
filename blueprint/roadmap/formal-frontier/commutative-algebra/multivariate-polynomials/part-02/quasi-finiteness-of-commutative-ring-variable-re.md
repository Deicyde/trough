---
declaration: theorem
origin: cited
lean: MvPolynomial.rename_quasiFinite_iff
statement: formalized
proof: formalized
---

# Quasi-finiteness of commutative-ring variable renaming

For any
commutative ring `R` and arbitrary `f : σ → τ`, with all three types in
independent universes,
[`MvPolynomial.rename_quasiFinite_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameQuasiFinite.lean)
states that the original full polynomial-ring map is quasi-finite exactly
when `f` is surjective or `R` is subsingleton. It uses Mathlib's
residue-field-fiber convention, without a `FiniteType` hypothesis, and
the full source-polynomial action. Module finiteness supplies the positive
direction; an omitted target variable gives a surjective evaluation onto
`R[X]`, reducing the converse to Mathlib's polynomial local obstruction. The
comparison `MvPolynomial.rename_quasiFinite_iff_finite` identifies
quasi-finiteness with finiteness of that same ring homomorphism. The
[boundary applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameQuasiFinite.lean)
contrast an omitted variable and a noninjective surjection over `ℤ`, and
include the same omitted-variable map over `ZMod 1`. In the collision case,
a nonzero source polynomial annihilates every target polynomial under the
full renaming-induced action.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.rename_quasiFinite_iff` (theorem), declared in [MultivariatePolynomials/RenameQuasiFinite.lean, line 66](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameQuasiFinite.lean#L66).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.rename_quasiFinite_iff` in MultivariatePolynomials/RenameQuasiFinite.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameQuasiFinite.lean#L66)
