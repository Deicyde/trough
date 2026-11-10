---
declaration: theorem
origin: cited
lean: MvPolynomial.algebraicIndependent_fractionRing_map_rename_compl
statement: formalized
proof: formalized
---

# Omitted variables are algebraically independent over the source fraction ring

For a commutative domain `R`, an injective map `ρ : τ → σ`, and arbitrary
commutative-ring fraction rings `L` of `MvPolynomial τ R` and `K` of
`MvPolynomial σ R`,
[`MvPolynomial.algebraicIndependent_fractionRing_map_rename_compl`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingAlgebraicIndependence.lean)
proves that the images of `X i` in `K`, indexed by
`{i : σ // i ∉ Set.range ρ}`, are algebraically independent over `L`.
The `L`-algebra structure on `K` must be induced by the same canonical
fraction-ring map of `MvPolynomial.rename ρ`, not an arbitrary scalar action.
The five universes of `R`, `τ`, `σ`, `L` and `K` are independent;
no `Field` instances or finite index types are required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.algebraicIndependent_fractionRing_map_rename_compl` (theorem), declared in [MultivariatePolynomials/FractionRingAlgebraicIndependence.lean, line 62](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingAlgebraicIndependence.lean#L62).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.algebraicIndependent_fractionRing_map_rename_compl` in MultivariatePolynomials/FractionRingAlgebraicIndependence.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingAlgebraicIndependence.lean#L62)
