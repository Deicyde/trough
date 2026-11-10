---
declaration: theorem
origin: cited
lean: MvPolynomial.rename_flat_iff
statement: formalized
proof: formalized
---

# Flatness of commutative-ring variable renaming

For every commutative
ring `R` and arbitrary `f : σ → τ`, with coefficient and variable types in
independent universes,
[`MvPolynomial.rename_flat_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFlatness.lean)
characterizes flatness of the full ring homomorphism
`MvPolynomial.rename (R := R) f` by injectivity of `f` or subsingleton
coefficients. The scalar action is induced by this original polynomial-ring
map, not just by `R` or by its image. Injective maps give free polynomial
extensions after complementary variables are separated; a collision kills
the regular difference of two distinct variables. The
[regularity API](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Regularity.lean) works over every
commutative ring, including the zero ring. The
[independent models](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/RenameFlatnessModels.lean)
and [criterion applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTypeTests/RenameFlatness.lean)
include a proper inclusion over the integers, a collision over the nonreduced
ring `ZMod 4`, and the same collision over `ZMod 1`.
The same module also gives
[`MvPolynomial.comap_rename_surjective_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFlatness.lean)
for commutative semirings and
[`MvPolynomial.rename_faithfullyFlat_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFlatness.lean)
for commutative rings: each uses the same injectivity-or-subsingleton condition
for the original full polynomial map. Their criterion applications include
the strict inclusion over `ℤ`, prime-spectrum surjectivity over the non-ring
semiring `ℕ`, an empty source, and a collision over the zero ring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.rename_flat_iff` (theorem), declared in [MultivariatePolynomials/RenameFlatness.lean, line 118](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFlatness.lean#L118).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.rename_flat_iff` in MultivariatePolynomials/RenameFlatness.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFlatness.lean#L118)
