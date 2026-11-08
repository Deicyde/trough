# Simplicial rings

> Central polynomial simplices over arbitrary unital rings, their coefficient-natural polynomial retraction and explicit algebraic simplicial homotopy on the polynomial extension.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/formalization.yaml) of [FormalFrontier/simplicial-rings](https://github.com/FormalFrontier/simplicial-rings) at commit [72878574](https://github.com/FormalFrontier/simplicial-rings/tree/728785746bd0ddcca62c91cf3f50507ec71107ce), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 3 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/simplicial-rings](https://github.com/FormalFrontier/simplicial-rings), read at commit [72878574](https://github.com/FormalFrontier/simplicial-rings/tree/728785746bd0ddcca62c91cf3f50507ec71107ce) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “self-assessed”
- Automation: agent; framework “Formal Frontier agents using Lean 4”; tool setup “AI-assisted proof development”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *The K-book: An Introduction to Algebraic K-theory*, Charles A. Weibel, Chapter IV, section 11 (mathematical motivation) (book; background).

## Builds on

No other Formal Frontier library.


## Headline results

**`PolyRing R n`.** Has `n` central
indeterminates over any `Ring R`; homogeneous
[`coordinate`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean) values sum to one.
[`substitute`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean) evaluates free
generators at **whole-target-center** elements (a sufficient, not necessarily
minimal, condition); [`hom_ext`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean)
determines ring maps by coefficients and generators.

**`simplexFunctor`.** Sends a ring
to an actual simplicial ring, with contravariant
[`ordinalMap`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean) for every ordinal
arrow, including empty fibres. Polynomial
[`constantInclusion`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean) followed
by [`evalAtZero`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex.lean) is strictly
the identity on the unextended simplex; both maps are coefficient-natural.

**`contraction`.** Is a
native seven-identity `SimplicialObject.Homotopy` from evaluation-then-inclusion
to the identity on the polynomially extended simplex. Its first face is the
**identity** endpoint and its last face is **evaluation-then-inclusion**;
[`homotopyMap_natural`](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/SimplicialRings/CentralPolynomialSimplex/Homotopy.lean)
handles every unital coefficient map. Whiskering along a supplied covariant
functor uses mathlib's existing `Homotopy.whiskerRight`, not a new wrapper here.

See the [simplex guide](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/docs/CentralPolynomialSimplex.md) and
[homotopy guide](https://github.com/FormalFrontier/simplicial-rings/blob/728785746bd0ddcca62c91cf3f50507ec71107ce/docs/CentralPolynomialSimplexHomotopy.md) for the precise
coordinate, degree, face, degeneracy and universe conventions.
