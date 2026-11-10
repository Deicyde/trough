---
declaration: theorem
origin: cited
lean: Algebra.FinitePresentation.of_surjective_algebraMap
statement: formalized
proof: formalized
---

# Zero-variable presentations and semiring renaming

[`Algebra.FinitePresentation.of_surjective_algebraMap`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FinitePresentation.lean)
gives a zero-variable presentation for a surjective scalar map from a
commutative semiring to any semiring, with finitely generated ideal kernel.
For commutative-semiring coefficients with subsingleton additive units,
[renaming reflects zero](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameFinitePresentationSemiring.lean)
and every surjective variable map is finitely presented over its full source
polynomial semiring. No cancellation, order, or finiteness assumption is needed.
This is Mathlib's ideal-kernel convention, not congruence-based semiring
finite presentation; a bottom ideal kernel need not imply injectivity.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Algebra.FinitePresentation.of_surjective_algebraMap` (theorem), declared in [MultivariatePolynomials/FinitePresentation.lean, line 99](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FinitePresentation.lean#L99).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Algebra.FinitePresentation.of_surjective_algebraMap` in MultivariatePolynomials/FinitePresentation.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FinitePresentation.lean#L99)
