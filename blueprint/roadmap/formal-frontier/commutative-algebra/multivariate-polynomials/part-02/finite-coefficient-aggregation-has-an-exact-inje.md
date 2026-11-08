---
declaration: theorem
origin: cited
lean: Finsupp.mapDomain_injective_iff
statement: formalized
proof: formalized
---

# Finite coefficient aggregation has an exact injectivity criterion

For
types `α`, `β` and `M` in independent universes, an additive commutative
monoid `M`, and any index map `f : α → β`,
[`Finsupp.mapDomain_injective_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean)
characterizes injectivity of `Finsupp.mapDomain f : (α →₀ M) → (β →₀ M)`:
it holds exactly when `f` is injective **or** `M` is subsingleton. The map
adds coefficients whose indices have the same image; cancellation, a ring
structure and nontrivial coefficients are not required. The
[applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/FiniteSupport.lean) contrast the
identity and a constant index map with natural-number coefficients.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Finsupp.mapDomain_injective_iff` (theorem), declared in [MultivariatePolynomials/FiniteSupport.lean, line 45](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean#L45).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Finsupp.mapDomain_injective_iff` in MultivariatePolynomials/FiniteSupport.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean#L45)
