# Continuous group cohomology

> Native continuous group cohomology in low degrees; transfer and compact-group degree-one torsion; finite-level Tate deflation, compact exceptional Tate groups and diagrams, compact finite-bar homology and norm-limit sequences. For compact topological groups with discrete jointly continuous coefficients over a topologized ring, every continuous cohomology class lifts from a finite open-normal quotient with invariant coefficients. In positive degrees a class-dependent quotient order annihilates the class. The native open-normal inflation cocone is a filtered colimit in all degrees, including zero, with the actual cohomology topology and arbitrary topological-module targets. Its equality refinements depend on the classes; no fixed-stage injection, uniform bound or closed-boundary-range hypothesis is claimed. For arbitrary finite index types, finite functions are naturally equivalent to coefficient-left tensors over a commutative semiring; for finite groups, the twisted action agrees with the diagonal left-regular tensor action. This algebraic result gives no continuous or topological-representation equivalence. At each fixed acting group, the degree-zero coefficient functor is naturally isomorphic to invariants over a ring with its supplied topology.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/formalization.yaml) of [FormalFrontier/continuous-group-cohomology](https://github.com/FormalFrontier/continuous-group-cohomology) at commit [4434e3f2](https://github.com/FormalFrontier/continuous-group-cohomology/tree/4434e3f215302e5c9ac4214c27646d0d21884169), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 6 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/continuous-group-cohomology](https://github.com/FormalFrontier/continuous-group-cohomology), read at commit [4434e3f2](https://github.com/FormalFrontier/continuous-group-cohomology/tree/4434e3f215302e5c9ac4214c27646d0d21884169) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other”.
- Review notes: “Scoped mathematical and API contributions received independent review; formal journal review and complete source coverage are not claimed.”
- Automation: agent; framework “Codex CLI”; tool setup “Codex CLI assisted Lean proof and documentation development using Lake, Lean and mathlib.”
- Automation notes: “Proof development and documentation were AI-assisted using Codex CLI.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Native-core continuous group cohomology (original Formal Frontier development)* (original-development; other).
- *Cohomology of Number Fields (corrected second edition)*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Chapter I, §3, Proposition 1.3.6(ii); Chapter I, §1, Exercise 4 (book; adapts).

## Builds on

- [Finite-group Tate cohomology](../finite-group-tate-cohomology/README.md) (a Lake dependency, pinned at d17f93bb)
- [Group theory](../../group-theory/group-theory/README.md) (named in its formalization.yaml)
- [Profinite groups](../../group-theory/profinite-groups/README.md) (a Lake dependency, pinned at 5f11ef67)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/README.md#headline-results) of [FormalFrontier/continuous-group-cohomology](https://github.com/FormalFrontier/continuous-group-cohomology) at commit [4434e3f2](https://github.com/FormalFrontier/continuous-group-cohomology/tree/4434e3f215302e5c9ac4214c27646d0d21884169), Apache-2.0.*

These results are proved here for representations over a ring
`k` equipped with a topology. The group, discreteness and action-continuity
hypotheses are specified separately below; foundations come from Mathlib.

### Finite-quotient descent, torsion and the topological colimit

See [`CompactDiscreteTorsion`](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/CompactDiscreteTorsion.lean)
and [`FiniteStageColimit`](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/FiniteStageColimit.lean) for these APIs.

For a compact topological group `G` and discrete `X : TopRep k G` over a
ring with a supplied topology, the homogeneous cochain complex is the colimit
of its open-normal finite-quotient cochain complexes, with coefficients in
`X^U` at a stage `U`. This is a colimit in complexes of topological modules
and separately in every degree. Joint continuity of the action is not needed.
The [quotient-stage diagram](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/OpenNormalDiagram.lean)
and inflation cocone also have coefficient naturality without compactness or
discreteness assumptions. The [integer sign example](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/examples/FiniteStageColimitNative.lean)
uses a nonconstant cochain and checks the descendant equation, uniqueness of
its lift at a chosen stage, and compatibility with every refinement.

Separately, for a compact topological group `G` and discrete
`X : TopRep k G` with `[Ring k] [TopologicalSpace k]`, every continuous
cohomology class lifts from an open-normal finite quotient with its
quotient-invariant coefficients. In positive degrees a class-dependent quotient
order annihilates the class; this gives additive torsion, not a uniform bound.
Joint continuity of the action is not needed for these class-lift and torsion
statements, nor for the cohomology colimit. The open-normal cohomology inflation
cocone is a filtered colimit in topological modules in **every degree, including
zero**, with arbitrary topological-module targets.
It uses the cohomology topology, algebraic boundaries and class-dependent
eventual refinements, not fixed-stage positive-degree injectivity, a uniform
refinement or a closed-boundary-range assumption. The concrete sign-orbit
cochain construction still uses joint continuity.

### Additivity in coefficient maps in every degree

For `[Ring k] [TopologicalSpace k]`, topological groups `H` and `G`, and a
continuous homomorphism `φ : H →ₜ* G`, the
[coefficient-map API](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/ContinuousCohomologyFunctor.lean)
proves additivity and preservation of zero in the coefficient morphism in
**every natural degree, including zero**. For a fixed acting group,
`ContinuousCohomology.coefficientFunctor n` is an additive functor on topological
representations, using the existing continuous-cohomology objects and maps.
In degree zero, `ContinuousCohomology.zeroNatIso` naturally identifies this
fixed-group functor with invariants; its forward and inverse components are
the canonical `ContinuousCohomology.zeroIso` maps. The same ring with its supplied
topology suffices: neither commutativity nor continuity of the ring operations,
compactness of the groups nor discreteness of the coefficients is required.
The [integer model](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/CoefficientAdditivity.lean) uses the one-element
group `PUnit` acting trivially on `ℤ`: the sum of two identity coefficient
morphisms doubles every class in every degree. Its degree-zero calculation uses
`zeroNatIso` naturality to send the class with invariant value `1` to a nonzero
class with invariant value `2`.

### Positive coinduced cohomology after closed restriction

For compact topological groups and discrete coefficients,
[diagonal insertion](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/CoinducedAcyclic.lean)
gives a map on the recursively iterated coinduced homogeneous cochains with an
explicit evaluation law. This insertion contracts the cochain complex in every
positive degree, so continuous cohomology with coinduced discrete coefficients
vanishes there. Degree-zero vanishing is false even for the two-element group
acting trivially on nonzero integers (see the
[two-element-group client](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/CoinducedAcyclic.lean)).
The [coefficient functor](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/ContinuousCohomologyFunctor.lean)
for a fixed acting group and degree uses Mathlib's continuous-cohomology maps;
its object and morphism laws transport positive vanishing across coefficient
isomorphisms in the same group. For compact Hausdorff totally disconnected
`G`, the [closed-subgroup positive-vanishing theorem](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/ProfiniteCoinducedAcyclic.lean)
then applies to every closed `H`, and also to restrictions of representations
isomorphic to `TopRep.coind₁ B`. The restricted representation is `H`-coinduced
from all of `C(G ⧸ H, B)` with its generally nontrivial pointwise `H`-action.
Only discrete `B` is needed; neither openness or normality of `H` nor joint
continuity of the coefficient action is required. The finite signed
[`S₃` clients](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/CoinducedRestriction.lean) instantiate positive
vanishing at a nonnormal subgroup, not at a closed nonopen subgroup. These
are strictly positive-degree conclusions, corresponding to the closed-subgroup
clause of Neukirch–Schmidt–Wingberg, I §3, Proposition 1.3.7; they do not
assert degree-zero vanishing or all-integer Tate acyclicity.

### Normal-quotient coinduction

For `[Ring k] [TopologicalSpace k]`, a compact topological group `G`, any
normal subgroup `N` and a discrete, jointly continuous `B : TopRep k G`, the
[normal-quotient coinduction equivalence](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/CoinducedInvariants.lean)
identifies `TopRep.quotientInvariants N (TopRep.coind₁ B)` with
`TopRep.coind₁ (TopRep.of (ContRepresentation.trivial k (G ⧸ N) B))`
as representations of `G ⧸ N`. This is universe-polymorphic and requires no
closedness or openness of `N`, Hausdorff condition or choice of section. Its
forward and inverse maps satisfy `(P f)(mk N t) = B.ρ t⁻¹ (f t)` and
`(J F)(t) = B.ρ t (F (mk N t))`. The right-hand coefficient is the **whole**
`B`, not `B^N`, and has trivial quotient action. The
[sign-product and full-group clients](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/CoinducedInvariants.lean)
exhibit `B^N = 0` with nonzero `B`, a quotient function moved by the residual
quotient action, and an invariant function whose value at the identity is
moved by `N`.

### Degreewise exactness under coefficient embeddings

For any topological group `G` and `A B C : TopRep.{max v w} k G`,
[`cochainsMap_exact_of_isEmbedding`](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/CochainExactness.lean)
proves that an exact underlying coefficient row `A → B → C` whose first map is a
topological embedding induces an exact row of homogeneous invariant cochains in
every natural degree. No local compactness, coefficient discreteness or extra
joint-action continuity is required. The original `cochainsMap_exact` is the
discrete-middle, injective-first-map corollary. This is underlying algebraic
exactness, not topological strictness or an exactness assertion on cohomology.
The separate cochain-surjectivity theorem still assumes locally compact `G`,
a discrete target and jointly continuous source coefficients.

### Algebraic connecting maps, naturality and initial invariants

The [algebraic connecting-map guide](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/docs/CohomologyExactSequence.md) describes
a connecting `k`-linear map in each natural degree and proves the three
recurring exactness assertions for the underlying modules of continuous cohomology.
They use locally compact `G`, discrete `B` and `C`, jointly continuous action
on `B`, injective `i`, exact `A → B → C`, and surjective `p`. The connecting
construction uses the cochain short exact sequence and Mathlib's homology
boundary; its representative formula and comparison with the
topologically split degree-zero map specify its sign. The algebraic assertions
also show that vanishing of the underlying `Hⁿ(G,B)` makes the connector mono,
vanishing of `Hⁿ⁺¹(G,B)` makes it epi, and both together give an isomorphism
whose forward arrow is the existing connector, for every natural `n`, including
zero. They do not establish continuity of this new map. For the integer sign action on
`ℤ --×2→ ℤ → ZMod 2`, the quotient invariant `1` has a nonzero connecting
class; its lack of an invariant integer lift is independently verified.
The [coinduced two-point row](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/ConnectingIsomorphism.lean)
embeds trivial integers as constant functions and projects to signed integers
by subtracting the values at the two units. Its middle cohomology vanishes in
degrees one and two; the existing exactness statements show that its degree-one
connector has nonzero image and is surjective, without using a general
connecting-isomorphism result in these independent witness proofs. Separate
private clients apply the general mono, epi and isomorphism APIs to this row.
Two split rows give complementary degree-zero boundaries: for
`Multiplicative (ZMod 2)`, coinduced `B` has `H¹(G,B) = 0` but its degree-zero
connector is not mono; for the distinct group `ℤˣ`, the middle signed
coefficient `B` has `H⁰(G,B) = 0` but its degree-zero connector is not epi.
In that second row, the final coefficient `C` is the zero representation on `PUnit`.

Under the same short-exact-row and topological hypotheses, the
[initial-invariants module](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/InitialInvariantsExactSequence.lean)
proves exactness of the underlying-module segment
`0 → Aᴳ → Bᴳ → Cᴳ → H¹(G,A) → H¹(G,B) → H¹(G,C)` at its five internal positions.
It uses Mathlib's invariant functor and natural degree-zero isomorphism and the
existing algebraic connector. The coefficient-level lemmas
`TopRep.mapInvariants_injective` and `TopRep.exact_mapInvariants` have weaker
hypotheses. Their earlier `ContinuousCohomology` names remain deprecated aliases. The
[example](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/InitialInvariantsExactSequence.lean) checks a nonzero
displayed invariant inclusion and a nonsplit sign-action boundary. Its
coefficient-level obstruction and existing nonzero connector are independent
of the segment theorem. Neither surjectivity at `H¹(G,C)` nor continuity
of the connector is claimed.

For a ring with a supplied topology and any monoid,
[`TopRep.mono_iff_injective`](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/TopRepMonomorphisms.lean)
characterizes monomorphisms by injectivity, with independent ring, monoid and
carrier universes. The action operators are individually continuous; no jointly
continuous action or topology on the monoid is assumed. For topological groups,
`ContinuousCohomology.map_zero_mono` preserves monicity under any continuous
group homomorphism, and the existing `coefficientFunctor 0` preserves
monomorphisms. No group-map surjectivity or all-degree preservation is asserted.
The [integer-doubling example](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomologyExamples/CoefficientMonicity.lean)
uses a nonsurjective map of the two-element group and nonzero degree-zero classes.

The [coefficient-naturality theorem](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/ConnectingNaturality.lean)
proves that, for two short exact coefficient sequences over the
same locally compact `G`, with the preceding discreteness and joint-continuity
hypotheses in each row, commuting coefficient maps `(α, β, γ)`
give `δ ≫ Hⁿ⁺¹(α) = Hⁿ(γ) ≫ δ′` for every natural degree. This is an equality
of underlying-module maps, not continuity of `δ`, change-of-group naturality,
or a topological delta-functor. The
[nonidentity sign-sequence client](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/CGCExamples/ConnectingNaturality.lean)
independently verifies the coefficient squares and a nonzero boundary, then
applies the naturality theorem.

See [Results and use](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/docs/Results.md) for the other constructions, full
module boundaries, conventions and client map.

## Main results

Its formalization.yaml lists 205 main results, and the scan finds 203 of them declared in the file the yaml gives; they are on their own page, not made articles. The scan does not find `ContinuousCohomology.openNormalInflationCoconeIsColimit_type` ([ContinuousGroupCohomology/FiniteStageColimit.lean](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/FiniteStageColimit.lean)), `ContinuousGroupCohomology.LevelCompact.compactTotalInvariantsCone_isLimit` ([ContinuousGroupCohomology/CompactTateNormLimitSequence.lean](https://github.com/FormalFrontier/continuous-group-cohomology/blob/4434e3f215302e5c9ac4214c27646d0d21884169/ContinuousGroupCohomology/CompactTateNormLimitSequence.lean)).

- [Main results](main-results/README.md)
