---
declaration: theorem
origin: cited
lean: MvPolynomial.primary_family_map_C_iff_of_subtractive
statement: formalized
proof: formalized
---

# Supplied primary families and deletion irredundance

Over a commutative
semiring `R`, for an ideal `I` and family `Q : ι → Ideal R`,
[`MvPolynomial.primary_family_map_C_iff_of_subtractive`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean)
assumes `a ∈ Q i → a + b ∈ Q i → b ∈ Q i` for each component. For every variable
type `σ`, it equates `I.map C = ⨅ i, (Q i).map C` with all mapped components
primary to `I = ⨅ i, Q i` with all original components primary. For nonempty
`σ`, [`MvPolynomial.primary_family_map_C_iff_subtractive`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean)
gives the exact equivalence with `I = ⨅ i, Q i` and componentwise primaryness
and subtractivity, recovering the latter from the mapped primary family.
The ring theorem
[`MvPolynomial.primary_family_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean)
specializes the first equivalence using automatic subtractivity, for every `σ`.
The intersection itself need not be primary. Over any commutative semiring,
[`MvPolynomial.irredundant_iInf_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean)
preserves and reflects the condition that each intersection of the other
components is not contained in the omitted component, without subtractivity.
Indices may form any sort; coefficient, variable and index universes are
independent. Empty or infinite families are allowed, with no finiteness or
Noetherian hypothesis. These statements give no existence, uniqueness or
associated-prime claim. The
[integer model](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/PrimaryDecomposition.lean)
uses the ring equivalence and deletion irredundance for `(12) = (4) ∩ (3)`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.primary_family_map_C_iff_of_subtractive` (theorem), declared in [MultivariatePolynomials/PrimaryDecomposition.lean, line 46](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean#L46).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.primary_family_map_C_iff_of_subtractive` in MultivariatePolynomials/PrimaryDecomposition.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimaryDecomposition.lean#L46)
