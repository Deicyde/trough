# Stable range

> Bass stable-range conditions for finite right-unimodular rows, quotient and local-ring consequences, regular and unit-regular rings, categorical biproduct cancellation and module cancellation, division-ring matrix row rank and repeated blocks, commutative dimension bounds, kernel-product decompositions with specified sections over semirings, arbitrary-ring right-coefficient row splittings and rectangular completion from free right kernels, commutative free coefficient-row kernels, explicit two-element row completion and supplied-product cancellation, exact-size finite-free cancellation and first-row completion, and elementary diagonalization over commutative rings satisfying Bass S_1, with determinant-one generation and the stable elementary quotient. A commutative ring with finite maximal spectrum satisfies S_1. Idempotent corners of arbitrary rings satisfying S_1 also satisfy S_1. Division semirings are local and have zero nonunits additive submonoid. In a commutative local semiring, the additive view of the maximal ideal is the submonoid of nonunits. In a possibly noncommutative local ring, every proper left ideal lies in the Jacobson radical, which is the unique maximal left ideal. Conversely, a ring is local exactly when its canonical Jacobson radical is maximal among all left ideals; properness supplies nontriviality. General rings need not be commutative; commutative and division-ring results retain their separate hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/formalization.yaml) of [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range) at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 12 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range), read at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “author-verified”
- Review notes: “Metadata verification does not establish independent source correspondence, rights clearance or complete coverage of the book.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “Lean compiler feedback, mathlib APIs and tactics including simp, rw, ext, ring, noncomm_ring, abel and omega.”
- Automation notes: “AI agents authored code, proofs, documentation and metadata. No human mathematical review or source-author endorsement is asserted. AI generation does not establish correctness, originality, copyright ownership or clearance.”

## Scope

The aggregate root imports the mathematical leaves, including exact-size finite-free cancellation under a stable-range bound and coefficient-row completion with the original row in the first matrix position. It includes elementary unit pivots and diagonalization over commutative S_1 rings. Biproduct cancellation in a preadditive category assumes S_1 only for the canonical End of the cancelled object and requires only the two displayed biproducts. It imposes no commutativity, global-sum or remainder hypotheses; the local-End corollary uses the existing local-ring producer. Module cancellation specializes this result while retaining independent scalar and carrier universes. It also imports finite determinant-one generation, the stable determinant kernel theorem and the quotient-to-units equivalence under S_1. It also imports S_1 inheritance for the corner of any idempotent, without centrality or nontriviality. The aggregate root also re-exports kernel-product decompositions with a specified linear section over a semiring, with an additive-group source, additive-monoid target and independent scalar and carrier universes. Forward and inverse coordinates retain that section; splitting alone asserts neither finiteness nor freeness. The full injective-first-map comparison uses Mathlib's right-split-exact equivalence and the same section. The aggregate root also re-exports RowKernel's arbitrary-ring right-coefficient row section and kernel-product splitting, and RightRowCompletion's rectangular two-sided inverse criterion when that kernel is free. Splitting alone makes no freeness claim. Separately, its explicit two-element commutative supplied-witness completion gives scalar kernel coordinates and cancellation from a supplied rank-two product equivalence. The local-semiring interface supplies division-semiring locality and the zero nonunits additive submonoid without commutativity or additive inverses, and identifies the additive view of the existing maximal ideal with nonunits for commutative local semirings. For possibly noncommutative local rings, the Jacobson radical is the unique maximal left ideal; the classification ranges over all left ideals, not only two-sided ones. Conversely, maximality of the canonical radical among all left ideals recognizes unit-theoretic locality in any ring, without a locality or separate nontriviality premise. A separate test root imports PublicAPIClient, FiniteFreeClient, RowCompletionClient, ElementaryGenerationClient, SemilocalClient, CornerClient, RightCoefficientClient, RowCompletionTwoClient, RightRowCompletionClient, LocalIdealCommRingClient and ProductMaximalIdealClient. RightRowCompletionClient uses independent two-by-two integer-matrix fixtures, including a nonzero kernel column and noncentral multiplication. RowCompletionTwoClient uses independently checked integer fixtures, a nonidentity product equivalence and the zero ring; RightCoefficientClient imports integer and matrix right-coefficient fixtures with zero/empty-row boundaries. Other test-only fixtures include zero-ring, rank-one and noncentral matrix corners and a nonlocal product of fields. The commutative finite-maximal-spectrum S_1 theorem supplies shortening and stable quotient determinant clients. Bass S_1 need not mean least stable index one: the zero ring also has S_0. The remaining principal results below summarize proved mathematics rather than enumerate every declaration or claim full coverage of the source.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/formalization.yaml) of [FormalFrontier/stable-range](https://github.com/FormalFrontier/stable-range) at commit [4d01f179](https://github.com/FormalFrontier/stable-range/tree/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book build dated 2013-08-29: Chapter I stable-range and module-theoretic material, including I.1.2.1 and Exercises I.1.12(v) and I.1.13. (book; adapts).

## Builds on

- [General linear groups](../../group-theory/general-linear-groups/README.md) (a Lake dependency, pinned at 2683f75e)

## Used by

- [Homological algebra](../../homological-algebra-and-category-theory/homological-algebra/README.md)
- [Projective modules](../projective-modules/README.md)
- [Vector bundles](../../topology/vector-bundles/README.md)


## Headline results

These results use Mathlib. The quasiregular-ideal predicate and unit characterization
come from pinned `general-linear-groups`; the stable-range consequences are proved
here. The [guide](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/docs/GUIDE.md#headline-results) retains detailed statements,
coordinate formulas, compatibility names and client inventories.

**[Bass conditions](StableRange/Basic.lean).** For arbitrary possibly noncommutative rings: right-unimodular
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

**[Retract endomorphisms](StableRange/CategoryTheory/EndRetract.lean).** In any preadditive category, `i : X ⟶ Z`, `p : Z ⟶ X` and `i ≫ p = 𝟙 X`
transfer `Bass.StableRangeCondition (End Z) 1` to
`Bass.StableRangeCondition (End X) 1` for the original canonical endomorphism
rings. Object and morphism universes are independent; no complementary object,
finite-length or nonzero hypothesis is needed.

**[Finite biproduct endomorphisms](StableRange/CategoryTheory/FiniteLocalEnd.lean).** In any preadditive category, a displayed finite biproduct of objects with local
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

The 54 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `Bass.StableRangeCondition` | def | [StableRange/Basic.lean, line 62](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Basic.lean#L62) | Bass S_n uses finite right-unimodular rows with witness coefficients on the right; IsStableRange is a relational least natural index, not a default value when no finite bound exists. |
| `Bass.stableRangeCondition_one_of_finite_maximalSpectrum` | theorem | [StableRange/Semilocal.lean, line 39](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Semilocal.lean#L39) | Under CommRing and finite maximal spectrum, the proved S_1 condition shortens the second entry of a right-unimodular pair by b - a*t, including the zero ring. |
| `Bass.stableRangeCondition_one_corner` | theorem | [StableRange/Corner.lean, line 35](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Corner.lean#L35) | For any idempotent e in a possibly noncommutative ring satisfying S_1, Mathlib's corner eRe with identity e also satisfies S_1. Neither centrality, fullness nor nontriviality is required. |
| `Bass.stableRangeCondition_mono` | theorem | [StableRange/Basic.lean, line 150](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Basic.lean#L150) | S_m implies S_n for m <= n, over arbitrary possibly noncommutative rings. |
| `Bass.stableRangeCondition_of_surjective` | theorem | [StableRange/Quotient.lean, line 62](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Quotient.lean#L62) | Stable-range conditions descend along surjective ring homomorphisms. |
| `Bass.stableRangeCondition_quotient_iff` | theorem | [StableRange/Quotient.lean, line 135](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Quotient.lean#L135) | Quotienting by a quasiregular two-sided ideal preserves every S_n; reflection is not asserted for arbitrary quotient ideals. |
| `Bass.stableRange_one_of_isLocalRing` | theorem | [StableRange/Local.lean, line 252](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean#L252) | A native possibly noncommutative local ring has least stable range one. The native local-ring hypotheses exclude the zero ring. |
| `IsLocalRing.le_ringJacobson` | theorem | [StableRange/Local.lean, line 308](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean#L308) | Every proper left ideal of a possibly noncommutative local ring lies in its Jacobson radical, without a two-sidedness hypothesis. Locality includes nontriviality. |
| `IsLocalRing.isMaximal_iff_eq_ringJacobson` | theorem | [StableRange/Local.lean, line 332](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean#L332) | In any possibly noncommutative local ring, a left ideal is maximal exactly when it is the Jacobson radical. The radical is maximal, and every maximal left ideal is identified with this same ideal; no two-sidedness hypothesis is imposed. Locality includes nontriviality. |
| `IsLocalRing.of_ringJacobson_isMaximal` | theorem | [StableRange/Local.lean, line 366](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean#L366) | For any possibly noncommutative ring, maximality of its canonical Jacobson radical among all left ideals supplies unit-theoretic locality. No locality or separate nontriviality premise is required; maximality includes properness. |
| `IsLocalRing.iff_ringJacobson_isMaximal` | theorem | [StableRange/Local.lean, line 398](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Local.lean#L398) | A ring is local exactly when its canonical Jacobson radical is maximal among all left ideals, not only two-sided ideals. This ring criterion does not subsume Mathlib's commutative-semiring unique-maximal-ideal provider. |
| `Bass.stableRangeCondition_one_isDedekindFinite` | theorem | [StableRange/Regular.lean, line 46](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Regular.lean#L46) | S_1 makes every one-sided inverse two-sided. |
| `Bass.isUnitRegular_iff_stableRangeCondition_one` | theorem | [StableRange/Regular.lean, line 365](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Regular.lean#L365) | For a von Neumann-regular ring, unit-regularity is equivalent to S_1. Replacing S_1 by least stable range one additionally requires Nontrivial. |
| `Bass.principalRightIdeals_isCompl_of_innerInverse` | theorem | [StableRange/Regular.lean, line 185](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Regular.lean#L185) | An inner inverse x for a gives complementary aR and (1-a*x)R, represented as submodules over the opposite ring. |
| `Bass.not_isUnitRegular_moduleEnd_finsupp_nat` | theorem | [StableRange/Regular.lean, line 287](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Regular.lean#L287) | The endomorphism ring of a countable direct sum of copies of any nonzero additive module is not unit-regular. Neither the coefficient module nor this direct sum is asserted to be free. |
| `CategoryTheory.nonempty_iso_of_biprod_iso_of_end_stableRangeCondition_one` | theorem | [StableRange/CategoryTheory/Cancellation.lean, line 101](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CategoryTheory/Cancellation.lean#L101) | In a preadditive category with independent object and Hom universes, S_1 for the canonical End(X) makes X cancel from X biprod Y isomorphic to X biprod Z. Only those two biproducts are required, with no restrictions on Y or Z. The End ring need not be commutative or nontrivial. This generalizes the existing module cancellation proof. |
| `CategoryTheory.nonempty_iso_of_biprod_iso_of_isLocalRing_end` | theorem | [StableRange/CategoryTheory/Cancellation.lean, line 119](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CategoryTheory/Cancellation.lean#L119) | A possibly noncommutative local endomorphism ring supplies S_1 and hence biproduct cancellation with the same two-sum floor. |
| `Bass.exists_linearEquiv_of_prod_of_end_stableRangeCondition_one` | theorem | [StableRange/Cancellation.lean, line 53](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Cancellation.lean#L53) | If End_R(M) satisfies S_1, an equivalence M x A = M x B gives an equivalence A = B, with no finiteness or projectivity hypothesis. This is a specialization of categorical cancellation, retaining all independent scalar and carrier universes. |
| `Bass.IsUnitRegular.subsingleton_of_fin_linearEquiv_fin_prod` | theorem | [StableRange/Cancellation.lean, line 107](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Cancellation.lean#L107) | Finite powers of the regular right module over a unit-regular ring cannot absorb a nontrivial complementary module, including power zero. |
| `Bass.isVonNeumannRegular_moduleEnd` | theorem | [StableRange/DivisionRing.lean, line 125](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRing.lean#L125) | The endomorphism ring of any vector space over a division ring is regular. |
| `Bass.isUnitRegular_matrix` | theorem | [StableRange/DivisionRing.lean, line 133](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRing.lean#L133) | Every finite square matrix ring over a division ring is unit-regular, including the empty index case; finite dimension supplies automorphic inner inverses, unlike the arbitrary-vector-space assertion. |
| `Matrix.repeatBlockHom` | def | [StableRange/RepeatedBlock.lean, line 59](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RepeatedBlock.lean#L59) | Repeating square matrices on finite diagonal blocks is a ring homomorphism at NonAssocSemiring generality. Its value is Kronecker product with an identity; injectivity needs a nonempty block family. |
| `Matrix.rowRank` | def | [StableRange/DivisionRingRank.lean, line 49](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRingRank.lean#L49) | Finrank of the range of the left-linear row-vector map given by right multiplication, over a possibly noncommutative division ring. The API includes multiplication bounds, reindex invariance and additivity on mutually orthogonal idempotents. |
| `Matrix.exists_rowRank_eq` | theorem | [StableRange/DivisionRingRank.lean, line 158](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRingRank.lean#L158) | Every natural rank bounded by the finite square size is realized. |
| `Matrix.rowRank_repeatBlock` | theorem | [StableRange/DivisionRingRank.lean, line 327](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRingRank.lean#L327) | Repeated blocks scale row rank by their number, including an empty block family. |
| `Matrix.normalizedRowRank_repeatBlock` | theorem | [StableRange/DivisionRingRank.lean, line 421](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DivisionRingRank.lean#L421) | Normalized real rank is preserved for nonempty square matrices and nonempty finite block families. Normalized rank of the identity is one only under the nonempty-size hypothesis; empty-size division is totalized in Lean and does not give that assertion. |
| `Bass.isVonNeumannRegular_iff_isReduced_and_krullDimLE_zero` | theorem | [StableRange/Commutative.lean, line 111](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Commutative.lean#L111) | Commutative regular rings are exactly reduced rings of Krull dimension at most zero. |
| `Bass.IsVonNeumannRegular.flat` | theorem | [StableRange/Commutative.lean, line 142](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Commutative.lean#L142) | Every module over a commutative regular ring is flat, with no finite-generation assumption. |
| `Bass.stableRangeCondition_one_of_krullDimLE_zero` | theorem | [StableRange/CommutativeStableRange.lean, line 112](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CommutativeStableRange.lean#L112) | Krull dimension at most zero implies S_1 for commutative rings, without reducedness or nontriviality. The separate least-index-one result requires Nontrivial; the zero ring satisfies S_0. |
| `Bass.IsVonNeumannRegular.isUnitRegular` | theorem | [StableRange/CommutativeStableRange.lean, line 50](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/CommutativeStableRange.lean#L50) | Every commutative regular ring is unit-regular. |
| `Bass.stableRangeCondition_succ_of_krullDimLE` | theorem | [StableRange/BassDimension.lean, line 561](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/BassDimension.lean#L561) | A commutative noetherian ring of Krull dimension at most d satisfies S_(d+1). No reducedness, nontriviality or infinite-residue-field assumption is imposed; the proof uses finite-prime avoidance and height. |
| `LinearMap.kerProdEquivOfRightInverse` | def | [StableRange/Module/SplitSurjective.lean, line 96](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Module/SplitSurjective.lean#L96) | Over a semiring, a specified linear right inverse gives ker(f) x N equivalent to the additive-group source M, with additive-monoid target N and independent universes. Forward coordinates add the kernel element to the section image; inverse coordinates are x - s(f(x)) and f(x). Neither finiteness, projectivity nor freeness is required. |
| `LinearMap.kerProdEquivOfRightInverse_ofInjective` | theorem | [StableRange/Module/SplitSurjective.lean, line 216](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/Module/SplitSurjective.lean#L216) | Under the ring hypotheses of Mathlib's right-split-exact equivalence, identifying any injective first map with the kernel transports the kernel-product equivalence to that construction using the same section. |
| `LinearMap.isRightUnimodular_iff_surjective_dotProductBilin` | theorem | [StableRange/RowKernel.lean, line 605](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L605) | For any ring R and finite row a, the right-linear map over Rᵐᵒᵖ evaluates to sum a_i*x_i. Right-unimodularity is equivalent to its surjectivity; companion section and right-span criteria include the empty row and the zero ring. |
| `LinearEquiv.rightCoefficientKernelProd` | def | [StableRange/RowKernel.lean, line 541](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L541) | A right-inverse column b gives the section y ↦ (b_i*y) and an explicit right-linear equivalence ker(σ) × R ≃ R^n whose inverse second coordinate is the original row σ. No free kernel or matrix completion follows from this arbitrary-ring splitting. |
| `LinearEquiv.rightCoefficientRowCoordinates` | def | [StableRange/RightRowCompletion.lean, line 44](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RightRowCompletion.lean#L44) | A chosen right-inverse column and finite coordinates of the right kernel give a right-linear equivalence whose first coordinate is the original row and whose tail is the chosen coordinate of its witness-dependent kernel projection. |
| `Matrix.rightRowCompletion` | def | [StableRange/RightRowCompletion.lean, line 131](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RightRowCompletion.lean#L131) | The supplied witness and kernel coordinates yield a rectangular matrix with first row equal to the original row, paired with an explicit two-sided inverse that retains the supplied witness as its first column. Matrix actions agree with the coordinate maps. |
| `LinearEquiv.rightCoefficientKernelEquivOfMatrixInverse` | def | [StableRange/RightRowCompletion.lean, line 254](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RightRowCompletion.lean#L254) | A two-sided rectangular inverse with specified first row gives actual right-kernel coordinates by tail(A *ᵥ k), reconstructed by B *ᵥ Fin.cons 0 t; no prior freeness assumption is required. |
| `Matrix.isRightUnimodular_and_free_kernel_iff_exists_rectangular_inverse` | theorem | [StableRange/RightRowCompletion.lean, line 416](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RightRowCompletion.lean#L416) | Over any ring, right-unimodularity with a free right kernel is equivalent to some finite rectangular two-sided inverse pair retaining the row. Splitting derives finite generation of the kernel; no commutativity, stable-range or invariant-basis-number condition is imposed. |
| `LinearEquiv.isRightUnimodular_iff_exists_kernelProdEquiv` | theorem | [StableRange/RowKernel.lean, line 678](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L678) | A finite row is right-unimodular exactly when it has a kernel-product equivalence over the opposite ring with inverse second coordinate equal to the original row, not just an abstract product equivalence. |
| `LinearEquiv.kernelProdEquivOfIsRightUnimodular_eq_rightCoefficientKernelProd` | theorem | [StableRange/RowKernel.lean, line 760](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L760) | For commutative rings, kernel transport compares the scalar and right-linear splittings using the same chosen witness in both; the comparison does not identify that witness with a test fixture. |
| `Bass.coefficientRowKernelEquivSuccOfStableRangeCondition` | def | [StableRange/RowKernel.lean, line 448](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L448) | Over a commutative ring satisfying S_n, a right-unimodular row of length n+1 has kernel explicitly equivalent to the free module on Fin n. Monotonicity gives free kernels for lengths at least s+1 under S_s, without Noetherianity or a dimension bound. |
| `Bass.coefficientRowKernelEquivOfMatrixInverse` | def | [StableRange/RowKernel.lean, line 172](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowKernel.lean#L172) | Over a commutative ring, any chosen row i of a matrix with a specified two-sided inverse has kernel equivalent to functions on the other indices. No stable-range assumption is used; i : Fin n supplies nonemptiness and n=1 gives the empty complementary index type. |
| `Matrix.coefficientRowCompletionTwo` | def | [StableRange/RowCompletionTwo.lean, line 50](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletionTwo.lean#L50) | Over any commutative ring, a specified witness a₀b₀+a₁b₁=1 completes the row (a₀,a₁) to a determinant-one matrix with second row (-b₁,b₀). Its inverse has rows (b₀,-a₁) and (b₁,a₀). |
| `Bass.coefficientRowKernelEquivTwo` | def | [StableRange/RowCompletionTwo.lean, line 222](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletionTwo.lean#L222) | The supplied completion identifies the kernel of the original two-element coefficient functional with R, with coordinate -b₁x₀+b₀x₁ and inverse generator (-a₁t,a₀t). |
| `LinearEquiv.coefficientProductCancellationTwo` | def | [StableRange/RowCompletionTwo.lean, line 343](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletionTwo.lean#L343) | Any supplied (Fin 2 → R) ≃ₗ[R] (R × P) over a commutative ring identifies P ≃ₗ[R] R via its original first projection and kernel; no stable-range, freeness or nontriviality hypothesis is required. |
| `Module.finLinearEquivOfStableRangeCondition` | def | [StableRange/FiniteFree.lean, line 47](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/FiniteFree.lean#L47) | For a commutative R satisfying S_s, an explicit equivalence P x R^m = R^(n+m) with s <= n yields P = R^n, with the exact coordinate count, independent module universe and zero ring allowed. The noetherian Krull-dimension-bound specialization has separate hypotheses. |
| `LinearEquiv.coefficientRowCompletionOfStableRangeCondition` | def | [StableRange/RowCompletion.lean, line 44](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/RowCompletion.lean#L44) | A right-unimodular row of length n+1 over a commutative ring satisfying S_s with s <= n yields a self-equivalence whose first output coordinate is the original coefficient functional. Its matrix has that first row and the same specified inverse satisfies both inverse identities. |
| `Matrix.GeneralLinearGroup.exists_elementary_unit_pivot_of_stableRangeCondition_one` | theorem | [StableRange/ElementaryGeneration.lean, line 40](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/ElementaryGeneration.lean#L40) | Bass S_1 over a commutative ring yields an elementary left factor with a unit leading entry for every invertible successor-rank matrix, including rank one and the zero ring; locality is not required. |
| `Matrix.GeneralLinearGroup.exists_elementary_diagonalization_of_stableRangeCondition_one` | theorem | [StableRange/ElementaryGeneration.lean, line 93](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/ElementaryGeneration.lean#L93) | Two-sided elementary factors diagonalize every invertible Fin n matrix into units under commutative S_1, including the empty matrix. The generic all-rank unit-pivot induction comes from general-linear-groups. |
| `Matrix.GeneralLinearGroup.exists_elementary_diagonalization_finite_of_stableRangeCondition_one` | theorem | [StableRange/ElementaryGeneration.lean, line 104](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/ElementaryGeneration.lean#L104) | The same diagonalization transports along a finite equivalence to any finite decidable index type, without a chosen order or Nontrivial. |
| `Matrix.GeneralLinearGroup.mem_elementarySubgroup_iff_det_eq_one_of_stableRangeCondition_one` | theorem | [StableRange/DeterminantGeneration.lean, line 78](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DeterminantGeneration.lean#L78) | Over a commutative S_1 ring, an invertible matrix at any finite decidable index type is elementary exactly when its determinant is one; the empty index type and the zero ring are included. |
| `Matrix.GeneralLinearGroup.StableGL.elementary_eq_ker_det_of_stableRangeCondition_one` | theorem | [StableRange/DeterminantGeneration.lean, line 104](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DeterminantGeneration.lean#L104) | The stable elementary subgroup is the kernel of the stable determinant, by reducing a stable representative to a finite stage. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDetMulEquivOfStableRangeConditionOne` | def | [StableRange/DeterminantGeneration.lean, line 142](https://github.com/FormalFrontier/stable-range/blob/4d01f17954ba77e8ec53cf1524c9057e8f3d72e3/StableRange/DeterminantGeneration.lean#L142) | The stable elementary quotient is equivalent to the coefficient units; the forward map is the quotient determinant and the inverse is the existing rank-one section. |
