---
declaration: theorem
origin: cited
lean: MvPolynomial.moduleFinite_rename_iff
statement: formalized
proof: formalized
---

# Module finiteness of variable renaming has a sharper criterion

For any
commutative semiring `R` and any map `f : σ → τ`, with all three types in
independent universes,
[`MvPolynomial.moduleFinite_rename_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameModuleFinite.lean)
states that the full target polynomial semiring is a finite module over the
full source polynomial semiring under `p • q = MvPolynomial.rename f p * q`
exactly when `f` is surjective or `R` is subsingleton. This is stronger than
finite type: over nontrivial coefficients, `Nat.succ : ℕ → ℕ` misses only
`0`, so its renaming is of finite type but is not module-finite. These are
source-polynomial scalars, not coefficient-`R` scalars. See the
[applications beside the criterion](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameModuleFinite.lean),
including nonreduced and noncancellative coefficients and independent universe lifts.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.moduleFinite_rename_iff` (theorem), declared in [MultivariatePolynomials/RenameModuleFinite.lean, line 52](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameModuleFinite.lean#L52).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.moduleFinite_rename_iff` in MultivariatePolynomials/RenameModuleFinite.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/RenameModuleFinite.lean#L52)
