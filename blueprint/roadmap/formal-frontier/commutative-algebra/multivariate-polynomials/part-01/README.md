---
navigation: transparent
---

# Heights of homogeneous… to Jacobson radicals of…

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

- [Heights of homogeneous polynomial evaluations](heights-of-homogeneous-polynomial-evaluations.md)
- [Homogeneous polynomial maps on projective coordinate spaces](homogeneous-polynomial-maps-on-projective-coordi.md)

**Homogeneous coordinate-power certificates.** For an arbitrarily indexed homogeneous family `p : J → MvPolynomial I R`
of common degree `d` over any commutative semiring, with finitely many
variables, the
[certificate module](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/HomogeneousCertificates.lean)
states that radical membership of every variable gives finitely supported
coefficients `q : I → (J →₀ MvPolynomial I R)` and one common `M`, with
every `q i j` homogeneous of degree `M` and
`(q i).sum (fun j r => r * p j) = X i ^ (M + d)`. Over a field, the second
statement replaces radical membership by absence of nonzero common zeros
over the algebraic closure. The finite-index function-sum corollaries
`exists_homogeneous_sum_mul_eq_X_pow` and
`exists_homogeneous_sum_mul_eq_X_pow_of_forall_aeval_eq_zero` convert these
conclusions to `∑ j, q (i, j) * p j = X i ^ (M + d)` using
`Finsupp.sum_fintype`.
The variable, generator and coefficient universes are independent; empty
types, trivial semirings and degree zero are included. The
[coordinate-power and constant-one examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/HomogeneousCertificates.lean)
verify the hypotheses and explicit certificates independently of the core statements.

- [Polynomial closed points and algebraic-closure orbits](polynomial-closed-points-and-algebraic-closure-o.md)
- [Infinitely many maximal ideals of polynomial rings](infinitely-many-maximal-ideals-of-polynomial-rin.md)
- [Factorization uniqueness from a regular crossed resultant](factorization-uniqueness-from-a-regular-crossed.md)

**Non-unital rings of additive units.** For a non-unital, non-associative semiring
`R`, the existing `AddUnits R` inherits multiplication and forms a non-unital,
non-associative ring. Associativity and commutativity are inherited when present.
For every non-unital, non-associative ring `S`, value inclusion induces
`(S →ₙ+* AddUnits R) ≃ (S →ₙ+* R)`, with a unique factorization through the
additive units. See [`AddUnits`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/AddUnits.lean).

- [Nonconstant coefficients of polynomial units](nonconstant-coefficients-of-polynomial-units.md)
- [Polynomial units over commutative semirings](polynomial-units-over-commutative-semirings.md)
- [Prime coefficient extensions over commutative semirings](prime-coefficient-extensions-over-commutative-se.md)
- [Maximal coefficient extensions over commutative semirings](maximal-coefficient-extensions-over-commutative.md)
- [Finite coefficient-product equations determine whole products](finite-coefficient-product-equations-determine-w.md)
- [Radicals of coefficient-ideal extensions](radicals-of-coefficient-ideal-extensions.md)
- [Scalar annihilators and non-zero-divisors](scalar-annihilators-and-non-zero-divisors.md)
- [The degree-zero homogeneous component](the-degree-zero-homogeneous-component.md)
- [Coefficient ideals over commutative semirings](coefficient-ideals-over-commutative-semirings.md)
- [Square witnesses for failure of subtractivity](square-witnesses-for-failure-of-subtractivity.md)
- [Powers of augmented coefficient ideals](powers-of-augmented-coefficient-ideals.md)
- [Primary coefficient ideals](primary-coefficient-ideals.md)
- [Supplied primary families and deletion irredundance](supplied-primary-families-and-deletion-irredunda.md)
- [Nilpotent coefficients and irreducible polynomial spectra](nilpotent-coefficients-and-irreducible-polynomia.md)
- [Jacobson radicals of coefficient ideals](jacobson-radicals-of-coefficient-ideals.md)
