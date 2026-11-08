# Stable range

> Bass stable-range conditions for finite right-unimodular rows, quotient and local-ring consequences, regular and unit-regular rings, categorical biproduct cancellation and module cancellation, division-ring matrix row rank and repeated blocks, commutative dimension bounds, kernel-product decompositions with specified sections over semirings, arbitrary-ring right-coefficient row splittings and rectangular completion from free right kernels, commutative free coefficient-row kernels, explicit two-element row completion and supplied-product cancellation, exact-size finite-free cancellation and first-row completion, and elementary diagonalization over commutative rings satisfying Bass S_1, with determinant-one generation and the stable elementary quotient. A commutative ring with finite maximal spectrum satisfies S_1. Idempotent corners of arbitrary rings satisfying S_1 also satisfy S_1. Division semirings are local and have zero nonunits additive submonoid. In a commutative local semiring, the additive view of the maximal ideal is the submonoid of nonunits. In a possibly noncommutative local ring, every proper left ideal lies in the Jacobson radical, which is the unique maximal left ideal. Conversely, a ring is local exactly when its canonical Jacobson radical is maximal among all left ideals; properness supplies nontriviality. General rings need not be commutative; commutative and division-ring results retain their separate hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/formalization.yaml) of [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range) at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 12 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range), read at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “author-verified”.
- Review notes: “Metadata verification does not establish independent source correspondence, rights clearance or complete coverage of the book.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “Lean compiler feedback, mathlib APIs and tactics including simp, rw, ext, ring, noncomm_ring, abel and omega.”
- Automation notes: “AI agents authored code, proofs, documentation and metadata. No human mathematical review or source-author endorsement is asserted. AI generation does not establish correctness, originality, copyright ownership or clearance.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book build dated 2013-08-29: Chapter I stable-range and module-theoretic material, including I.1.2.1 and Exercises I.1.12(v) and I.1.13 (book; adapts).

## Builds on

- [General linear groups](../../group-theory/general-linear-groups/README.md) (a Lake dependency, pinned at 2683f75e)

## Used by

- [Homological algebra](../../homological-algebra-and-category-theory/homological-algebra/README.md)
- [Projective modules](../projective-modules/README.md)
- [Vector bundles](../../topology/vector-bundles/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/README.md#headline-results) of [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range) at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3), Apache-2.0.*

These results use Mathlib. The quasiregular-ideal predicate and unit characterization
come from pinned `general-linear-groups`; the stable-range consequences are proved
here. The [guide](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/docs/GUIDE.md#headline-results) retains detailed statements,
coordinate formulas, compatibility names and client inventories.

**Bass conditions.** For arbitrary possibly noncommutative rings: right-unimodular
rows, `(S_n)`, least stable index, monotonicity, ring-equivalence invariance and
[surjective descent/quasiregular quotients](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Quotient.lean).
[Nontrivial local rings](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean) have least stable range one.

**Local interfaces.** [Division semirings](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean) are local with
zero nonunits submonoid; the maximal-ideal additive comparison requires a
commutative local semiring.
For rings, locality is equivalent to Jacobson-radical maximality among all left
ideals. In local rings the radical is the nonunits and contains every proper
left ideal; these statements do not assume two-sidedness of the left ideals.

**Preservation.** [Products](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Product.lean) preserve every `(S_n)`.
[Semisimple rings and semisimple radical quotients](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Semisimple.lean)
satisfy `(S₁)` without radical nilpotence. [Finite matrix rings](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Matrix.lean),
[idempotent corners](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Corner.lean) and [opposites](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Opposite.lean)
preserve `(S₁)`; matrix reflection needs nonempty indices, corners neither
centrality nor fullness. [Commutative semilocal rings](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Semilocal.lean)
satisfy `(S₁)` assuming only finite maximal spectrum, including the zero ring.

**Retract endomorphisms.** In any preadditive category, `i : X ⟶ Z`, `p : Z ⟶ X` and `i ≫ p = 𝟙 X`
transfer `Bass.StableRangeCondition (End Z) 1` to
`Bass.StableRangeCondition (End X) 1` for the original canonical endomorphism
rings. Object and morphism universes are independent; no complementary object,
finite-length or nonzero hypothesis is needed.

**Finite biproduct endomorphisms.** In any preadditive category, a displayed finite biproduct of objects with local
endomorphism rings, and every displayed retract of that biproduct, have canonical
endomorphism rings satisfying `(S₁)`. Only that biproduct and, for the retract,
its supplied retraction are required, with independent index universe; empty
families and the zero biproduct are included. No vanishing of morphisms between
summands is assumed.

**Regularity and cancellation.** [`(S₁)`](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Regular.lean) implies direct
finiteness, is equivalent to unit-valued pair shortening, and under von Neumann
regularity is equivalent to unit-regularity.
[Biproduct cancellation](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CategoryTheory/Cancellation.lean) in any
preadditive category needs `(S₁)` for the canonical `End(X)` and only the two
displayed biproducts. The remaining objects are unrestricted; local End is
sufficient, and neither global sums nor commutativity is assumed.
[Module cancellation](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Cancellation.lean) is a specialization,
with independent carrier universes and no finiteness or projectivity;
regular right modules use the opposite ring. [Division-ring vector-space endomorphisms](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRing.lean)
have inner inverses; finite dimension gives automorphic inner inverses and
unit-regular finite matrix rings, including empty indices.

**Ranks and blocks.** [Division-ring row rank](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRingRank.lean)
has rectangular bounds, reindexing, realization and repeated-block laws;
normalized empty square rank is zero. [Repeated-block homomorphisms](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RepeatedBlock.lean)
work over `NonAssocSemiring` coefficients, injectively for nonempty block families.

**Commutative dimension bounds.** [Regularity](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Commutative.lean) is
equivalent to reducedness and dimension at most zero; all modules over such
regular rings are flat.
[Dimension at most zero gives `(S₁)`](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CommutativeStableRange.lean)
without reducedness or nontriviality; commutative regular rings are unit-regular.
[Noetherian dimension at most `d` gives `(S_(d+1))`](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/BassDimension.lean),
with no infinite-residue-fields premise.

**Specified splittings.** [A supplied linear right inverse of a linear map `f`](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Module/SplitSurjective.lean)
gives `ker f × N ≃ₗ[R] M` over a semiring, for an additive commutative group `M`
and additive commutative monoid `N`, in independent universes. The prescribed
complementary endomorphism `id - g.comp f` has range exactly `ker f`.
[Complementary-range ranks](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Module/SplitSurjectiveRank.lean) over a
division ring satisfy `finrank K (range (id - g.comp f)) = finrank K M - finrank K N`
assuming only that `M` is finite-dimensional. A family with given equivalences
`N b ≃ₗ[K] F` has this rank equal to `finrank K M - finrank K F` at every `b`,
without a nonempty base or a finite-dimensionality assumption on `F`.
[Right-unimodular
coefficient rows](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean) split over `Rᵐᵒᵖ` for any ring, including empty
rows and the zero ring. Splitting alone does not give freeness.

**Completion and IBN.** [Right-unimodularity and free right kernels](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RightRowCompletion.lean)
characterize two-sided rectangular completion, preserving a supplied inverse
column. For successor-length rows, [square completion](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/SquareRightRowCompletionCriterion.lean)
needs IBN only to infer kernel size; supplied matching coordinates and the
converse need no IBN. The [countable endomorphism example](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CountableEndomorphism.lean)
separates rectangular from square completion for nontrivial underlying modules,
even for a unary row.

**Commutative cancellation.** Under `(S_s)`, right-unimodular rows of length at
least `s + 1` have free kernels. [Finite-free cancellation](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/FiniteFree.lean) uses an
explicit `P × R^m ≃ R^(n+m)` and `s ≤ n`, without prior freeness of `P`;
[completion](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletion.lean) preserves the literal first row.
Both allow zero rings; dimension-bound variants require Noetherianity.
[Two-entry completion](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletionTwo.lean) retains supplied Bézout
coefficients over commutative rings, with explicit scalar kernel coordinates.

**Elementary matrices and determinants.** For commutative rings satisfying `(S₁)`,
[elementary diagonalization](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/ElementaryGeneration.lean) works in all
finite ranks, including zero. [Determinant generation](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DeterminantGeneration.lean)
identifies invertible determinant-one matrices with elementary matrices, the stable
elementary subgroup with the determinant kernel, and its quotient with units,
without locality, nontriviality or positive-rank hypotheses.

## Main results

Its formalization.yaml lists 54 main results, and the scan finds 54 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
