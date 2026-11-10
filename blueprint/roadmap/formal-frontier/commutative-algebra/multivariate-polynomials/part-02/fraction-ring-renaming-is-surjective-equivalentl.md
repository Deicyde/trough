---
declaration: theorem
origin: cited
lean: MvPolynomial.surjective_fractionRing_map_rename_iff
statement: formalized
proof: formalized
---

# Fraction-ring renaming is surjective, equivalently integral, exactly when it covers all variables

For any integral domain `R` (`[CommRing R] [IsDomain R]`) and injective
`ρ : τ → σ`,
[`MvPolynomial.surjective_fractionRing_map_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean)
characterizes surjectivity of the induced fraction-ring map by
`Function.Surjective ρ`. Its source `L` and target `K` may be any
commutative-ring fraction-ring realizations with their `Algebra` and
`IsFractionRing` instances, without `Field` instances. The five universes
of `R`, `τ`, `σ`, `L` and `K` are independent. For this same map,
[`MvPolynomial.isIntegral_fractionRing_map_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean)
characterizes integrality by the same condition `Function.Surjective ρ`.
[`MvPolynomial.surjective_fractionRing_map_finset_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean)
and
[`MvPolynomial.isIntegral_fractionRing_map_finset_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean)
specialize these criteria to a finite-variable stage `S : Finset σ`: the
stage map is surjective, equivalently integral, exactly when
`∀ i : σ, i ∈ S`, with no finiteness hypothesis on the ambient variable
type. The variable-image criterion identifies the image of `X i` in the
range exactly when `i ∈ Set.range ρ`. When `i ∉ Set.range ρ`,
[`MvPolynomial.not_isIntegralElem_fractionRing_map_rename_X`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean)
shows that the localized variable `X i` in `K` is not integral over the
image of the fraction-ring map. Thus every finite stage in infinitely
many variables is neither surjective nor integral, although each finite
family of fractions has a common finite stage. See the
[API guide](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/docs/API.md#multivariatepolynomialsfractionringfinitevariables).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.surjective_fractionRing_map_rename_iff` (theorem), declared in [MultivariatePolynomials/FractionRingFiniteVariables.lean, line 213](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean#L213).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.surjective_fractionRing_map_rename_iff` in MultivariatePolynomials/FractionRingFiniteVariables.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean#L213)
