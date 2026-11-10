---
declaration: theorem
origin: cited
lean: MvPolynomial.natDegree_uniqueAlgEquiv
statement: formalized
proof: formalized
---

# Canonical unique-variable degree

For any commutative semiring `R`,
unique variable type `σ` (`[Unique σ]`), and `p : MvPolynomial σ R`,
[`MvPolynomial.natDegree_uniqueAlgEquiv`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UniqueAlgEquiv.lean)
identifies `Polynomial.natDegree (MvPolynomial.uniqueAlgEquiv R σ p)`
with `p.totalDegree`. The coefficient and variable universes are independent.
No nonzero-polynomial or nontrivial-coefficient premise is needed:
both natural-number degrees assign zero to the zero polynomial.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.natDegree_uniqueAlgEquiv` (theorem), declared in [MultivariatePolynomials/UniqueAlgEquiv.lean, line 36](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UniqueAlgEquiv.lean#L36).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.natDegree_uniqueAlgEquiv` in MultivariatePolynomials/UniqueAlgEquiv.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/UniqueAlgEquiv.lean#L36)
