# Finite-group Tate cohomology

> Reusable Lean norms, exceptional Tate degrees, and objectwise additive cyclic period-two comparisons for finite-group representations.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/formalization.yaml) of [FormalFrontier/finite-group-tate-cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology) at commit [c0c9d563](https://github.com/FormalFrontier/finite-group-tate-cohomology/tree/c0c9d563d45adfa81bff78821042089f750b1d44), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 5 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/finite-group-tate-cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology), read at commit [c0c9d563](https://github.com/FormalFrontier/finite-group-tate-cohomology/tree/c0c9d563d45adfa81bff78821042089f750b1d44) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “The mathematical development and checked-use clients underwent independent review on earlier pinned inputs; each release has separate exact-artifact acceptance. This metadata alone does not certify source-specific correspondence.”.
- Review notes: “Earlier development review and later component review bind distinct inputs. Exact-artifact release approval and source-specific coverage remain separate decisions, not consequences of this catalogue or metadata.”
- Reviewers: “Lattice”, “Formal Frontier agents”, “Formal Frontier independent norm-component reviewer”.
- Automation: agent; framework “OpenAI Codex CLI with Lean verification”; tool setup “Lean 4.34.0-rc2 and pinned mathlib4 with cache-first Lake builds”; prompting notes “AI-assisted Formal Frontier agents and formalization workers contributed distinct mathematical modules, norm and NatIso component interfaces, checked examples, the original mixed-kind native catalogue and later documentation adaptations. The mathematical work was Lean-checked and independently reviewed; source-specific correspondence is separate.”
- Automation notes: “Formal Frontier source maintainers retain mathematical acceptance and source correspondence responsibility; AI assistance alone establishes neither.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Classical finite-group Tate cohomology, norm and additive cyclic periodicity* (folklore; independently-proves).
- [mathlib4 representation-theory Tate and finite-cyclic formal APIs](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5/Mathlib/RepresentationTheory/Homological) (software; background).

## Builds on

No other Formal Frontier library.

## Used by

- [Continuous group cohomology](../continuous-group-cohomology/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/README.md#headline-results) of [FormalFrontier/finite-group-tate-cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology) at commit [c0c9d563](https://github.com/FormalFrontier/finite-group-tate-cohomology/tree/c0c9d563d45adfa81bff78821042089f750b1d44), Apache-2.0.*

**Natural norms.** For a commutative scalar ring and finite group, the
[norm from coinvariants to invariants](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Norm.lean#L29)
is natural in the coefficient representation. For a finite normal subgroup
of an arbitrary ambient group, the
[residual-quotient-equivariant norm](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Norm.lean#L102)
is natural as well; the ambient group need not be finite or commutative.
This module permits independent scalar, group and coefficient universes.

**Exceptional degrees.** The
[exact norm sequence](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Basic.lean#L285)
`Tate⁻¹ → M_G → M^G → Tate⁰` identifies degrees −1 and 0 naturally with
the norm's kernel and cokernel. Both
[natural isomorphisms](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Basic.lean#L352)
(including their [component identities](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Basic.lean#L452))
are shipped, not proposed; this layer inherits the same-universe boundary
of the pinned Tate-complex API.

**Fixed-element coefficient functors.** For an element `g` of a finite
commutative group, the [even](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/CyclicModelFunctor.lean#L127)
and [odd](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/CyclicModelFunctor.lean#L133)
alternating `N`/`g−1` homology models are functorial in coefficients.
This construction does not require `g` to generate the group.

**Objectwise additive period two.** With a chosen element satisfying
`∀ x, x ∈ Subgroup.zpowers g`, the
[all-integer Tate comparisons](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/CyclicPeriodicity.lean#L197)
give [period-two isomorphisms](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/CyclicPeriodicity.lean#L305).
[Same-parity comparisons](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/CyclicPeriodicity.lean#L262)
have identity, inverse and telescoping laws; these Tate comparisons are
**objectwise**, not claimed natural in the coefficient representation.

**Hilbert's theorem 90.** For a finite Galois extension `L/K` and a specified
automorphism generating the full Galois group, every norm-one element of `L`
is `y / g(y)` for a unit `y` of the original field. The
[field endpoint](https://github.com/FormalFrontier/finite-group-tate-cohomology/blob/c0c9d563d45adfa81bff78821042089f750b1d44/FiniteGroupTateCohomology/Hilbert90.lean) permits independent
universes for `K` and `L`, with no characteristic or invertible-degree
assumption. It reuses Mathlib's cocycle theorem and finite-cyclic calculation.

## Main results

Its formalization.yaml lists 4 main results, and the scan finds 4 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
