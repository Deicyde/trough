# Spectral Stone duality

> Prime-ideal spectra of bounded distributive lattices and their contravariant equivalence with spectral spaces. Also proves spectrality of small cofiltered limits with spectral arrows, compact-open cylinder bases and descent over actual limits, and compact-open lifting from arbitrary subspaces of prespectral spaces. Finite labelled families, including empty families, descend to coherent whole-stage covers. Also proves retrocompactness and prespectral, compact, quasi-separated subtype topology for compact locally closed subsets of prespectral quasi-separated spaces, without ambient compactness. These results do not assert sobriety. It also constructs the soberification of any topological space and its reflection into T0 quasi-sober spaces, independently of spectral Stone duality. Every finite irreducible subset of any topological space contains a generic point of its closure, so every finite topological space is quasi-sober, without a separation or nonemptiness assumption. In T0 spaces, the original point is the unique closed point of its generization subspace, without a spectrality assumption. Finite joins in the underlying order category of a distributive lattice with bottom are universal coproducts; disjointness is characterized by pairwise-zero meets at distinct indices. Functors between thin order categories of bounded lattices preserve finite limits and colimits exactly when their object maps are bounded lattice homomorphisms, without distributivity or shared carrier universe. A cofinite space is quasi-sober exactly when its underlying type is finite, including the empty space. For any quasi-sober space, topological Krull dimension equals the order-theoretic Krull dimension of the original points with their specialization preorder, without a T0 assumption. The canonical soberification of every topological space preserves its topological Krull dimension, without quasi-sobriety or separation assumptions on the input.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/formalization.yaml) of [FormalFrontier/spectral-stone-duality](https://github.com/FormalFrontier/spectral-stone-duality) at commit [3d9e22b2](https://github.com/FormalFrontier/spectral-stone-duality/tree/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f), Apache-2.0.*

2 articles: 1 for highlights of its formalization.yaml and 1 for headline results in its README whose declaration link names a declaration the linked file declares. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/spectral-stone-duality](https://github.com/FormalFrontier/spectral-stone-duality), read at commit [3d9e22b2](https://github.com/FormalFrontier/spectral-stone-duality/tree/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”
- Automation: agent; tool setup “Formal Frontier AI agents use Lean, Lake and Git for formalization and maintenance.”

## Scope

Reusable bounded distributive-lattice Stone duality and the documented spectral-limit, cylinder and subspace topology, including retrocompactness and compact locally closed subspaces of prespectral quasi-separated spaces without ambient compactness or sobriety claims, together with general soberification and its reflective adjunction, plus universal finite coproducts and conditional disjointness in thin lattice categories. The original point is the unique closed point among its generizations in a T0 space. Finite-limit- and finite-colimit-preserving functors between thin bounded lattice categories correspond to bounded lattice homomorphisms; the binary preservation laws also hold for the corresponding semilattices. Cofinite topology is quasi-sober precisely on finite underlying types, with no nonemptiness assumption. Quasi-sober spaces have topological Krull dimension equal to the Krull dimension of their original-point specialization preorder. Soberification preserves topological Krull dimension for every topological space, with no quasi-sobriety or separation assumption on the input. Both results include empty spaces and unbounded finite chain lengths without an attainment assumption. Source-specific correspondence and coverage decisions are maintained separately.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/formalization.yaml) of [FormalFrontier/spectral-stone-duality](https://github.com/FormalFrontier/spectral-stone-duality) at commit [3d9e22b2](https://github.com/FormalFrontier/spectral-stone-duality/tree/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Stone duality for bounded distributive lattices and spectral spaces* (folklore; independently-proves).
- *Cofiltered spectral limits, cylinders and subspaces* (folklore; independently-proves).
- *Soberification of topological spaces* (folklore; independently-proves).
- *Cofinite quasi-sobriety* (folklore; independently-proves).
- [Foundations of Rigid Geometry I](https://arxiv.org/abs/1308.4734v5), Kazuhiro Fujiwara, Fumiharu Kato, Chapter 0, Sections 1.2(e), 2.2(a) and 2.2(b) (book; background).

## Builds on

- [Ideal completion](../ideal-completion/README.md) (a Lake dependency, pinned at 001e3b75)

## Used by

- [Sheaf cohomology](../../homological-algebra-and-category-theory/sheaf-cohomology/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)

## Highlights

- [Specialization and soberification dimensions](specialization-and-soberification-dimensions.md)

## Headline results

[Tube predicates](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/Tube.lean) are defined for arbitrary topological spaces: a tube-closed set is the closure of a retrocompact open subset, and a tube-open set has tube-closed complement. The API provides witness and complement characterizations, ordinary closedness and openness, and empty-set and whole-space cases. Tube-closed sets are stable under finite unions, and tube-open sets under finite intersections, including empty families.

**Maximal-generization reflection.** In any topological space where every point
has a unique maximal generization as an original point,
[`MaximalGenerizationSpace X h`](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/MaximalGenerization.lean)
carries the projection-final topology, not the inherited subtype topology.
Its quotient unit has singleton-closure fibres; the target is T₁ and canonically
homeomorphic to `T1Quotient X`, preserving the unit. Maps to every T₁ target
in an independent universe factor uniquely. Continuous maps between such spaces
induce maps by projecting after mapping, with identity, composition and
naturality laws. No global T₀, compactness, coherence or nonemptiness is required.

**Universal T₁ quotient.** For every topological space `X`,
[`T1Quotient X`](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/T1Quotient.lean) is the quotient
by the infimum of all setoids with closed equivalence classes. Its unit is
a continuous quotient map, universal for maps to every T₁ space, with source
and target in independent universes. Induced continuous maps preserve identities
and composition. The unit is a homeomorphism when `X` is T₁; for an R₀ input,
the construction agrees homeomorphically with Mathlib's `SeparationQuotient`.

**Prime spectrum and compact opens.** For a bounded distributive lattice `A`,
[`PrimeIdealSpectrum`](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/PrimeSpectrum.lean) consists of prime
**order ideals**. The opens `D(I)` are primes *not containing* the ideal `I`;
every open arises this way, and `D(I)` is compact (quasi-compact, not
necessarily Hausdorff) exactly when `I` is principal. Specialization is
inclusion of prime ideals. The trivial lattice is permitted and has an empty
spectrum. See the [spectrum guide](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/Guide.md#prime-spectra-and-the-open-set-convention).

**Spectral Stone duality.** Bounded lattice homomorphisms induce contravariant
spectral maps; compact opens recover the lattice, and points of a spectral
space are recovered from its compact-open lattice. The natural equivalence is
[`SpectralStoneDuality.stoneDuality : BddDistLatᵒᵖ ≌ SpectralCat`](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Equivalence.lean).
Its space-side reconstruction uses sobriety; it does not assert a duality for
arbitrary spaces. See [maps and reconstruction](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/Guide.md#maps-reconstruction-and-naturality).

**Finite compact-open reconstruction.** At each finite set of compact opens,
realized membership patterns form a finite spectral space with its Sierpiński
product-subtype topology. Restriction maps are continuous and surjective.
Evaluation into compatible families induces the topology when compact opens
form a basis. It is injective when compact opens form a basis and the space
is `T₀`. It is surjective when compact opens form a basis and the space is
compact, quasi-separated and quasi-sober; this does not require `T₀`.
Thus [`spaceHomeomorph`](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/FiniteCoordinates.lean) identifies
any spectral space with its compatible finite patterns. The compatible-family
cone is limiting for any topological space, and the point-evaluation cone is
limiting for spectral spaces; see [finite-coordinate limits](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/FiniteCoordinates/Limits.lean)
and the [finite-coordinate guide](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/Guide.md#finite-compact-open-coordinates).

**Thin-lattice finite coproducts.** In the order category of a distributive
lattice with bottom, finite joins are universal coproducts without requiring
a top element. In any lattice with bottom, a finite coproduct is disjoint
exactly when summands at distinct indices have meet bottom. Such disjoint
coproducts stay disjoint after base change in the distributive case; every
finite coproduct's injections generate a covering sieve for the extensive
topology. This does
not assert that every finite coproduct is disjoint or that the category is
`FinitaryExtensive`. See [thin lattices](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/CategoryTheory/Lattice/Extensive.lean).

**Finite preservation and lattice maps.** A functor between the order
categories of bounded lattices preserves finite limits and finite colimits
exactly when its object map is a bounded lattice homomorphism. The two maps
recover each other; no distributivity or shared carrier universe is needed.
Empty diagrams detect top and bottom, while binary discrete diagrams detect
meets and joins. See [preservation](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/CategoryTheory/Lattice/Preserves.lean).

**Soberification.** For any topological space, the topology on its nonempty
irreducible closed subsets yields a `T₀` quasi-sober space. The unit sends
a point to its singleton closure; continuous maps into `T₀` quasi-sober
spaces extend uniquely, giving a left adjoint to their inclusion in `TopCat`.
No separation, compactness or spectrality is required of the input. This
general-topology reflection is separate from the spectral-space
reconstruction in Stone duality. See [topology](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/Soberification.lean)
and [adjunction](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/Category/Soberification.lean).

- [Krull dimension, specialization and soberification](specialization-and-soberification-dimensions.md)

**Finite quasi-sobriety.** Every finite irreducible subset of any topological
space contains a generic point of its closure. In particular, every finite
topological space is quasi-sober, including the empty space and spaces that
are not `T₀`; sobriety additionally requires `T₀`. See
[finite topology](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/Finite.lean).

**Cofinite quasi-sobriety.** `CofiniteTopology.quasiSober_iff_finite X`
characterizes quasi-sobriety by `Finite X`, without a nonemptiness
hypothesis: empty and finite cofinite spaces are sober, whereas an infinite
cofinite space is `T₁` but not quasi-sober. See [cofinite topology](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/Cofinite.lean).

- [Closed points among generizations](closed-points-among-generizations.md)

**Generic-point removal.** In an Alexandrov space, select any set of points
each with no other generizations (including indistinguishable ones). The
discrete boundary labelled by strict specialization incidences maps to a sum
of independent generic-point forks and to the complementary subspace; together
these form a four-map pushout in `TopCat`. Openness and continuity on the
original space are detected on the forks and complement, and compatible
continuous maps glue uniquely. Neither a finite-space representation nor a
ring- or scheme-level pushout is asserted. See
[generic-point removal](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/GenericPointRemoval.lean).

**Closed-subspace strict specializations.** If all ambient specializations of
a selected point lie in a subspace and the selected points there have no
other generizations, the ambient strict indices agree with the subspace
strict-incidence indices, preserving both endpoints. Closed subspaces give
the containment condition. Finite containing subspaces bound the ambient
indices without a selected-point assumption; an Alexandrov subspace makes
the selected points relatively open. No `T₀` assumption is needed. See
[subspace strict specializations](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/SubspaceStrictSpecializations.lean).

**Limits and cylinder bases.** Small cofiltered diagrams of spectral spaces
with **spectral transition maps** have spectral limits and spectral
projections. Compact-open inverse-image cylinders form a basis for a supplied
`IsLimit` cone or the chosen limit. The separate limit-nonemptiness theorem
additionally assumes every stage nonempty; the basis results do not.
See [limits](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Limits.lean) and the
[cylinder-basis supplement](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/CompactOpenBasis.md).

**Maps of cofiltered spectral limits.** Given a natural transformation of
small cofiltered diagrams with spectral source and target stages, spectral
source transitions, spectral component maps, and arbitrary supplied `IsLimit`
cones, the induced map is spectral when target transitions are spectral
(`isSpectralMap_isLimit_map`), surjective when each component is surjective
(`surjective_isLimit_map`), and closed when each component is a closed map
(`isClosedMap_isLimit_map`). Surjectivity and closedness do not require spectral
target transitions; no result assumes nonempty stages or Hausdorff spaces.
If the spectral transition maps themselves are surjective or closed, respectively,
each projection of a supplied limiting cone is surjective
(`surjective_isLimit_projection`) or closed (`isClosedMap_isLimit_projection`).
The closed-projection result does not require surjective transitions.
See [limit maps](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/LimitMaps.lean).

**Subspaces and descent.** A compact open of *any* subspace of a prespectral
space lifts to an ambient compact open; closedness is unnecessary. A map to
that subspace is spectral when its composite with the inclusion is spectral.
For an actual limiting cone, compact-open/merely-open cylinder containment
descends over an `Over` witness. Finite, possibly empty, labelled families
descend coherently, including whole-stage covers. These results do not require
surjective arrows or inhabited stages, and do not construct sheaves or their
gluing. See [subspaces](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Subspace.lean),
[single-cylinder descent](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/LimitCylinderDescent.md) and
[finite-cylinder descent](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/docs/FiniteCylinderDescent.md).

**Compact locally closed subspaces.** Inducing spectral maps into prespectral
quasi-separated spaces preserve quasi-separatedness without injectivity.
A compact locally closed subset is retrocompact, and its ordinary subtype
is prespectral, compact and quasi-separated, even when the ambient space is
not compact. These conclusions do not assert sobriety. See
[locally closed topology](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/LocallyClosed.lean).

**Constructibly closed spectral subspaces.** A constructibly closed subset of
a spectral space is spectral in the original subspace topology and includes
spectrally into the ambient space or any containing subspace. Arbitrary
compact-open intersections, including cofinal compact-open families, and
generization subspaces `nhdsKer {x}` are instances. The members of a cofinal
family need not all be open. See
[constructibly closed subspaces](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDuality/Topology/ConstructibleSubspace.lean)
and [examples](https://github.com/FormalFrontier/spectral-stone-duality/blob/3d9e22b25e636e8c1303bb66b8902beb8c5f4b1f/SpectralStoneDualityExamples/ConstructibleSubspace.lean).
