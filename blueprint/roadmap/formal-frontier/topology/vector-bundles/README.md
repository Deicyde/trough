# Vector bundles

> Compatible Hermitian and real fiber metrics on finite-dimensional vector bundles; orthogonal subbundles, addition homeomorphisms and continuous projections for a supplied metric; pairing-preserving local coordinates; and fiberwise linear isomorphisms, supported by linear-chart and finite-dimensional operator APIs. Products, pullbacks, cylinder charts, frames, finite model-power embeddings, range bundles and finite-dimensional complements over compact normal bases.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/formalization.yaml) of [FormalFrontier/vector-bundles](https://github.com/FormalFrontier/vector-bundles) at commit [e3fb9de3](https://github.com/FormalFrontier/vector-bundles/tree/e3fb9de334c8b60bdb707b3e48b2094b2202c725), Apache-2.0.*

5 articles: 4 for highlights of its formalization.yaml whose declarations the scan finds and 1 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/vector-bundles](https://github.com/FormalFrontier/vector-bundles), read at commit [e3fb9de3](https://github.com/FormalFrontier/vector-bundles/tree/e3fb9de334c8b60bdb707b3e48b2094b2202c725) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Automation: agent; tool setup “Lean 4 and Mathlib”
- Automation notes: “AI agents contributed to the formalization and documentation.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Allen Hatcher, Version 2.2 (November 2017), section 1.1: Lemma 1.1, Proposition 1.2 and its Hermitian remark, supplied-metric ingredients of Proposition 1.3, finite complements in Proposition 1.4, pullbacks in Proposition 1.5, and the two preliminary cylinder facts used in Proposition 1.7 (book; adapts).
- [Mathlib](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5), The Mathlib Community, Topology.VectorBundle; module topology and continuous linear maps; inner products and orthogonal complements; partitions of unity; continuous functional calculus; sigma-compact spaces, compact refinements of finite open covers and bundle trivialization homeomorphisms (software; adapts).

## Builds on

- [Coherent modules](../../commutative-algebra/coherent-modules/README.md) (a Lake dependency, pinned at 8be3fb89)
- [Metrization](../metrization/README.md) (a Lake dependency, pinned at 4dcc0f6f)
- [Projective modules](../../ring-theory/projective-modules/README.md) (a Lake dependency, pinned at 77a601ff)
- [Stable range](../../ring-theory/stable-range/README.md) (a Lake dependency, pinned at a78ced2d)

## Used by

- [Fundamental groupoids](../fundamental-groupoids/README.md)

## Highlights

- [Compatible Hermitian metrics](compatible-hermitian-metrics.md)
- [Orthogonal complements for a supplied metric](orthogonal-complements-for-a-supplied-metric.md)
- [Fiberwise linear isomorphism criterion](fiberwise-linear-isomorphism-criterion.md)
- [Sigma-compactness of a fiber bundle](sigma-compactness-of-a-fiber-bundle.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/README.md#headline-results) of [FormalFrontier/vector-bundles](https://github.com/FormalFrontier/vector-bundles) at commit [e3fb9de3](https://github.com/FormalFrontier/vector-bundles/tree/e3fb9de334c8b60bdb707b3e48b2094b2202c725), Apache-2.0.*

**Semiring kernel projections and splitting compatibility.** The equivalence
`ContinuousLinearMap.equivProdKerOfRightInverse` is provided by
[ProjectiveModules](https://github.com/FormalFrontier/projective-modules/blob/77a601ffd885a18a7c0fd90e311b7f530ac4762b/ProjectiveModules/Topology/Splitting.lean).
This library extracts its continuous kernel projection and preserves its existing
kernel-product API by transparent reuse. Prefer the canonical ProjectiveModules
equivalence and its coordinate and Ring-agreement theorems; the corresponding
VectorBundles names remain as deprecated compatibility API. The extracted kernel
projection is not deprecated. For a semiring `R`, an additive commutative
group `E` with a topological additive-group structure, and an additive commutative
monoid `F` with a topology, a continuous `R`-linear map `f : E →L[R] F` with a given
continuous linear right inverse `s` gives `E ≃L[R] F × f.ker`, with coordinates
`(f x, x - s (f x))` and inverse `(y, k) ↦ s y + k`
([module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Algebra/Module/Splitting.lean)). When `R` is a ring
and `F` an additive group, both bundled constructions agree with Mathlib's on the
same data. No scalar topology, separation or completeness is assumed.

In a normed ring finite dimensional over an arbitrary field, every element `a`
with `‖1 - a‖ < 1` is a unit, and the unit locus is open. No scalar norm or
completeness is required. The same conclusions hold in left-Artinian normed
rings ([module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Algebra/Units.lean)). A
pointwise-continuous family of continuous endomorphisms of a finite-dimensional
normed space consequently has an open invertible locus, even over an incomplete
nontrivially normed field
([module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Algebra/OperatorFamilies.lean)).

Over a possibly incomplete nontrivially normed field, a family of existing continuous linear
maps between given seminormed norm-compatible vector spaces, with finite-dimensional original
domain, is continuous in the original operator-norm topology exactly when every original
fixed-vector evaluation is continuous
(`ContinuousLinearMap.continuous_iff_apply_of_finiteDimensional` in
[module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/FiniteCoordinates/FiniteDimensional.lean)). The canonical
identity to the pointwise-convergence copy of the same continuous linear maps is a continuous
linear equivalence (`ContinuousLinearEquiv.toPointwiseConvergenceCLMOfFiniteDimensional`);
convergence along any filter is therefore equivalent to convergence at every fixed vector
(`ContinuousLinearMap.tendsto_iff_apply_of_finiteDimensional`).
For an isometric field homomorphism `σ : K →+* L`, the same criterion holds for
continuous `σ`-semilinear maps with their original actions and seminorms
(`ContinuousLinearMap.continuous_iff_apply_of_finiteDimensionalₛₗ`). Here `K` is
nontrivially normed and `L` need only be a normed field. More generally, the ambient
domain need not be finite-dimensional: evaluations on a set `D` suffice when its original
`K`-span is finite-dimensional and dense
(`ContinuousLinearMap.continuous_iff_apply_of_dense_spanₛₗ`); `D` need not be bounded.
For any family of bounded sets, the canonical identity to uniform convergence on that
family is a continuous `L`-linear equivalence if `D` lies in the `K`-span of its union
(`ContinuousLinearEquiv.toUniformConvergenceCLMOfDenseTestSpan` in
[module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/FiniteCoordinates/FiniteDimensional/Basic.lean)).
Only the dense controlling span of `D` must be finite-dimensional, so further bounded
sets may be added even when they make the whole union span infinite-dimensional.
The union-based construction (`ContinuousLinearEquiv.toUniformConvergenceCLMOfDenseSpan`)
is the `D = ⋃₀𝔖` specialization, and the algebraic-spanning finite-dimensional construction
(`ContinuousLinearEquiv.toUniformConvergenceCLMOfFiniteDimensional`) specializes it further.
No completeness, separation or surjectivity of `σ` is required.
For example, `R` over `Q` has the one-dimensional dense test span `Q·1`, although its
ambient algebraic dimension is infinite: `D = {1}` controls the family consisting of
`{1}` and `[-1,1]`, whose union spans all of `R` over `Q`.
In `Q(√2)` with inherited real absolute value,
`Q·1` is proper and dense. The equivalence acts on the same full maps, not on their
restrictions; dense restriction need not be injective for a nonseparated target.

**Pointwise total boundedness, compactness and properness.** Let `σ : K →+* L` be
isometric, with `K` nontrivially normed and `L` a normed field. Let `A` and `G` be
seminormed spaces over `K` and `L`, and let `P` be a dense finite-dimensional
`K`-submodule of `A`. A family in the full space `A →SL[σ] G` is totally bounded
exactly when every evaluation image on `P` is totally bounded
(`ContinuousLinearMap.totallyBounded_iff_apply_of_dense_finiteDimensionalₛₗ`).
If `G` is complete, a closed family is compact exactly under this pointwise condition
(`ContinuousLinearMap.isCompact_iff_forall_totallyBounded_image_apply_of_isClosed_of_dense`).
For proper `G`, the evaluation images need only be metrically bounded
(`ContinuousLinearMap.isCompact_iff_forall_isBounded_image_apply_of_isClosed_of_dense`),
and the full map space is proper for its canonical operator seminorm
(`ContinuousLinearMap.properSpace_of_dense_finiteDimensionalₛₗ` in
[module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/FiniteCoordinates/FiniteDimensional/Compactness.lean)).
The ambient domain need not be finite-dimensional. No completeness of either field
or of `A`, separation, or surjectivity of `σ` is required.

**Projective isometry sections.** A surjective linear isometry onto a projective
module over a semiring has a chosen linear-isometric right inverse
(`LinearIsometry.sectionOfSurjective` in
[module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Operator/Projective.lean)). It is a uniform
embedding even for nonseparated seminormed modules; no scalar topology or completeness
is required. For an originally normed source it agrees with the inverse of Mathlib's
surjective-isometry equivalence. The separation quotient therefore has a linear-isometric
section when its module is projective, using the given continuous constant scalar actions.

**Isometric kernel-product decompositions.** Over any semiring, a linear isometry
`f : E →ₗᵢ[R] F` of seminormed additive groups with a linear right inverse `s`
gives `E ≃ₗᵢ[R] (F × f.toLinearMap.ker)`
(`LinearIsometry.equivProdKerOfRightInverse` in
[module](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Operator/Splitting.lean)). The kernel keeps
its original module and inherited geometry; the product uses the maximum norm.
The kernel may be nonzero. No separation, scalar norm or topology, or continuity
assumption on `s` is required. The whole underlying linear and continuous
equivalences agree with the canonical continuous splitting, including its ring form.

These families are proved here, with the original fiber and total-space topologies.
The [catalogue](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/docs/HeadlineResults.md) gives the individual statements and variants;
the [detailed guide](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/docs/Results.md) adds examples and distinguishes Mathlib constructions.

**Nearby noncommuting idempotents.** For bounded idempotents `P` and `Q` on a
normed space over a nontrivially normed field, finite-dimensional range of `P`
and `‖Q - P‖ < 1` give continuous linear equivalences between their ranges and
between their kernels. The
[compression and kernel-coordinate constructions](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Operator/NearbyIdempotent.lean)
use the original subspace norms; neither the field nor the ambient space needs
to be complete. Finite dimension of the range of `Q` is a consequence, not an
extra hypothesis. For a continuous family of idempotents over an arbitrary
topological base, the kernel graph on the norm neighborhood has product
coordinates preserving the base point. A kernel section is continuous exactly
when its fixed-kernel coordinate is continuous.

**Supported weighted coordinates.** Given module families over a commutative semiring
and linear chart equivalences on arbitrary subsets, the
[weighted coordinate map](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/LinearAlgebra/WeightedCoordinates.lean)
takes values in the full dependent product of model modules. Its membership,
nonmembership, zero-weight and chart-evaluation rules are explicit. At each point,
generating the unit ideal by the valid chart weights suffices for fibrewise
injectivity. In particular, one valid unit weight suffices; no individual
weight need be a unit in the general criterion.
On the original equality fibres of a topological projection, with given module
operations and inherited topology, the
[total coordinate map](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Maps/WeightedCoordinates.lean)
is continuous when the projection, weights and exact inverse coordinates are
continuous, scalar multiplication on each model is continuous, and the closure
of each weight's cozero set lies in its domain. No openness, finite-index,
finite-dimensionality, norm or continuity of fibre operations is required.

**Additive sum–kernel coordinates.** For a projection `p : T → B` with given
additive monoid structures on its equality fibres, additive maps `β b` into a
topological abelian group `A` and retractions `ρ b` give a
[homeomorphism](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Maps/FiberwiseSplitting.lean)
from `{z : T × A // ρ (p z.1) z.2 = 0}` to `B × A` when their two total maps
are continuous. Its coordinates are `(p t, β (p t) ⟨t,rfl⟩ + v)`; its inverse
uses the given retraction and residual `a - β b (ρ b a)`. Continuity into the
original subspace is equivalent to continuity of the base and sum coordinates.
No continuity of fibre operations or scalar topology is required. Given
semiring-linear maps specialize this scalar-free construction by forgetting
linearity, retaining their original scalar actions.
For semiring-linear split maps on a given family `E b`, the
[complementary-range sum coordinates](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/SumRange.lean)
identify the fiberwise product of `E b` and `range (id - β.comp ρ)` with `B × A`,
under the same two total continuity hypotheses. The source has the canonical
product-total topology from the given first total space and the range graph topology.
The inverse uses `ρ` and the complementary endomorphism, and the forward fiber map
is the linear coproduct. No separate kernel topology is assumed.

**Prescribed finite-dimensional projection families.** Over a nontrivially normed
field `K`, let the original finite-dimensional normed ambient `A` have its
module topology (`[IsModuleTopology K A]`). Linear encoders and retractions
between the equality fibres of `p : T → B` and `A`, with `ρ b (β b u) = u`,
yield an
[operator-norm-continuous family of idempotents](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Maps/FiberwiseProjection.lean)
acting by `β b (ρ b a)` when the two exact total maps are continuous.
The complete-field frontend obtains this module topology locally from finite
dimensionality; the core construction needs no scalar completeness.
The existing complementary continuous-map expression acts by
`a - β b (ρ b a)`, lies in the retraction kernel and vanishes on encoded
vectors; it gives the image–kernel decomposition of every ambient vector.
No fibre norm or continuity of fibre operations, ambient completeness,
nontriviality of `A`, or separation of the base is assumed. Neither
orthogonality nor commutation at different parameters is asserted; the
ambient norm stays unchanged, including the standard sup norm for finite Pi.

**Joint evaluation of algebraic semilinear families.** For possibly noncommutative
semirings `R,S`, a ring homomorphism `σ : R →+* S` and a finite `R`-basis of the source,
assume that its scalar coordinates composed with `σ` are continuous. Joint continuity
of a family of `σ`-semilinear maps is then equivalent to continuity at each basis vector.
Only `S`, the source, target and parameter carry topologies; the target needs continuous
addition and jointly continuous `S`-scalar multiplication. No continuity of source
operations or of `σ` is assumed. The linear criterion is the identity specialization.
Over a complete nontrivially normed field, a finite-dimensional Hausdorff topological
source module needs no explicit basis data: joint continuity is equivalent to continuity
at every fixed vector. For continuous linear maps from a finite-dimensional seminormed
domain to a seminormed target, joint continuity is equivalent to continuity in the given
operator-norm topology even over an incomplete field; neither space needs to be separated
or complete. See
[JointEvaluation](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Module/JointEvaluation.lean).

- [Total-space continuity of semilinear maps from finite local bases](total-space-continuity-of-semilinear-maps-from-f.md)

**Module topologies on retracts and finite-basis coordinates.** Over a semiring with
a given scalar topology, a continuous linear retract of a module with the module
topology inherits that topology, even when the continuous section is nonlinear.
In particular, the range of an algebraic idempotent of such a module has its
module topology as the inherited subspace topology. Over a topological semiring,
a supplied finite basis of a module with the module topology gives a continuous
linear equivalence with the standard finite scalar product;
neither a field, a norm, completeness nor separation is required. See
[module-topology descent](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/ModuleTopology.lean) and
[finite-basis coordinates](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/Basis.lean).
The [complete-field comparison](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/Basis/FiniteDimensional.lean)
agrees exactly with Mathlib's `Module.Basis.equivFunL` without assuming a source norm.

**Local constancy of fibre finrank.** Over a division ring, given pointwise
[linear equivalences to fixed models](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/Finrank.lean)
on sets whose interiors cover the base make natural-number fibre finrank locally
constant. Neither finite-dimensionality nor topology on the modules is assumed.
Infinite-dimensional modules have finrank zero; this is not a claim about their
cardinal dimension.

**Closed fiber embeddings.** For continuous `p : T → X`, give its equality-subtype fibers
their subspace topologies and `RCLike` module structures. An arbitrary open cover with
finite-dimensional normed linear coordinates, jointly continuous realizations and continuous
exact inverse-coordinate maps on the total-space restrictions gives a [closed embedding into `X × A`](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/FiberEmbedding.lean)
from supplied injective algebraic fiber maps whose local frames are parameter-continuous at
each fixed vector. The normed inner-product target need not be complete; local ranks may vary.
The inverse extends to a jointly continuous fiberwise linear retraction on the product.

**Finite Euclidean embeddings from weighted local coordinates.**
For a continuous map `p : T → X` over `K = ℝ` or `ℂ`, finitely many normed
finite-dimensional local models for the original equality-subtype fibre
modules give a closed embedding `T → X × E` into a finite Euclidean product.
The supplied domains need not be open: their forward realizations and exact
inverse coordinates are continuous on the given subspaces, and the continuous
scalar weights have no common zero and closed cozero supports contained in
their specified domains. The nonzero-weight sets provide an open cover. The second
coordinate is the weighted coordinate map followed by the inverse of a linear
equivalence from `E` to the full product of models. That product keeps its
supremum norm; no isometry is asserted. The inverse on the image extends to a
jointly continuous fibrewise linear retraction on all of `X × E`, preserving
the given fibre operations and inherited topologies. No positivity,
normalization, or separation of `X` is required. See
[`exists_retraction_isClosedEmbedding_of_weighted_local_coordinates`](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/WeightedFiberEmbedding.lean).

**Retractions and projection continuity.** Over real or complex scalars, original fibers
with [inducing realizations](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/InducingRetraction.lean),
jointly continuous local realizations on an open cover, finite-dimensional seminormed coordinate models
and injective algebraic fiber maps into a normed inner-product space with fixed-vector-continuous local frames admit continuous-linear
retractions, jointly continuous realizations and operator-norm-continuous orthogonal projections.
No fiber norms or ambient completeness are needed. Separately, a given self-adjoint idempotent
family is [continuous](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/ProjectionContinuity.lean) if its
images have local injective finite-dimensional algebraic frames with fixed-vector continuity;
those frame domains need no topology.

**Metrics and finite complements.** A finite-dimensional real or complex bundle over a
paracompact Hausdorff base admits a continuous positive-definite [Hermitian metric](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/MetricExistence.lean)
inducing its original fiber topologies. Over a compact normal base, a finite-dimensional
`RCLike` bundle has a [finite-dimensional complement](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/FiniteComplement.lean)
whose product is linearly trivial, not necessarily a complement to a prescribed embedding.

**Orthogonal splitting.** For a supplied continuous Hermitian metric, an intrinsic submodule
bundle with embedded total-space inclusion and a finite-dimensional `RCLike` ambient model,
[orthogonal addition](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/OrthogonalAddition.lean) is a homeomorphism
with continuous projections, over any base. [Comparison](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/OrthogonalComparison.lean)
identifies complements for two supplied metrics with their induced topologies; no metric is constructed.

**Given adjoint partners.** For `RCLike` inner products, a supplied partner `S : A → H`
[bundles linearly](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/AdjointPair.lean) when `H` is normed and
`A` seminormed; a pointwise norm bound on the first map makes it continuous-linear. A continuous-linear
first map supplies the bound, without completeness. The catalogue also gives the algebraic
semiring-valued pairing result; the partner is supplied, not constructed.

**Adjoints and Gram families.** A continuous linear map from a complete normed `RCLike`
inner-product space to a seminormed one has an [adjoint](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/Adjoint.lean).
For given raw adjoint partners between seminormed spaces, operator-norm continuity of the forward
family gives [joint continuity](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/AdjointPairFamily.lean) of the partners.
On a finite-dimensional normed domain with normed ambient space, injective forward operators and
given continuous-linear adjoint partners have [continuous inverse Gram composites](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/GramRetraction.lean)
when the forward family is operator-norm continuous. On a complete finite-dimensional normed
inner-product domain, a jointly continuous injective family instead [constructs canonical adjoints,
left inverses and projections](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/GramFamily.lean) continuously.
None of these results requires completeness of the ambient space.

**Algebraic orthogonal retractions and distance.** An injective linear map from a plain module into
a normed `RCLike` inner-product space has an [algebraic retraction](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/Projection/LinearMap.lean)
when its range has orthogonal projection; finite dimension of the module suffices. Given the
orthogonal-retraction laws, [best-approximation and squared-error formulas](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/InnerProductSpace/Projection/Distance.lean)
hold without completeness or a topology on the coefficient module. In a seminormed ambient space,
zero residual norm detects range closure; in a normed one, `β.range = r.kerᗮ` and minimizers are unique.
The catalogue also gives the [nonzero-idempotent norm bound](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Ring/Idempotent.lean).

**Finite orthogonal idempotent families.** Over any semiring and finite index type, the
[matched-product sum](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Algebra/Ring/OrthogonalIdempotents.lean) intertwines two orthogonal
idempotent families. If it is a unit, that same unit simultaneously conjugates them and forces both
families to sum to one; completeness of the families is a conclusion, not a hypothesis.

**Close idempotents and rank stability.** On a normed space over a nontrivially normed field,
[idempotents at operator-norm distance less than one](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Operator/Idempotent.lean)
have equal cardinal ranks of ranges and kernels; these ranks are locally constant in continuous
families, without completeness. When geometric series are summable in the endomorphism ring
(in particular for a complete space), one normalized unit gives continuous-linear equivalences of both.

**Fixed-kernel coordinates.** For seminormed spaces over a nontrivially normed field, a family
`Γ d : H →L[K] A` with supplied algebraic retractions `r d` has [product coordinates for its total kernel](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Analysis/Normed/Operator/KernelFamilyCoordinates.lean)
on any topological parameter domain where `q₀ ∘ Γ d` is a unit. Here `q₀` is fixed and continuous-linear;
joint continuity of the difference between the original and normalized ambient projections suffices.
No separate continuity of `r` or completeness is needed. The [catalogue](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/docs/HeadlineResults.md#fixed-kernel-coordinates-on-unit-domains)
gives the formulas, unit-subtype version and distinction between a unit comparison and a retraction.

**Linear families and bundle inverses.** Over a field with a T₁ topology making it a topological
ring, pointwise-continuous algebraic linear families have an [open surjectivity locus](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Algebra/Module/OpenMap.lean)
for a finite-dimensional target with its module topology; the source needs no topology. Over a
nontrivially normed field, continuous-forward fiberwise linear equivalences give [bundle homeomorphisms](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/Isomorphism.lean)
when the source normed model is finite-dimensional and the target normed model has its module topology.

**Compact refinements and partitions of unity.** An ambient open cover of two compact subsets'
product admits [finite ambient open grids](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Compactness/Product.lean) with each
full rectangle in a chosen cover member, without separation assumptions. [Closed-interval subdivisions](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/UnitInterval.lean)
allow repeated cuts and singleton intervals. A finite open cover of a normal space admits [continuous
weights](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/ContinuousMap/FiniteWeights.lean) in `[0,1]` summing to one, with closed
cozero supports subordinate to the cover; no T₁ hypothesis is needed.
On a [closed subset of a normal space](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiniteNormalWeights.lean),
a finite open cover similarly admits nonnegative continuous weights with closed
supports in its members, sum at most one everywhere and exactly one on that subset.

**Finite selection from supplied product charts.** For compact `X`, arbitrary topological `Y`
and chosen `y₀`, supplied whole-product charts with both base laws and agreement in both directions
with specified original charts at `y₀` admit a [finite ordered open cover](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/FiniteCylinderCover.lean).
This retains varying models and, when provided, matching linear coordinates over any semiring. It selects supplied
charts, not charts from an arbitrary atlas over `Y`, and needs neither compactness of `Y` nor projection continuity.

**Heterogeneous cylinder gluing.** For a continuous projection over `X × T`, with `T` linearly
ordered and topological with closed upper and lower rays, supplied base-preserving charts on the
closed half-cylinders may have different models. The [gluer](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/ClosedCylinder.lean)
gives a whole-cylinder homeomorphism into the left model, retaining its entire left chart.

**Whole-cylinder charts and transport.** An open base-preserving atlas for a continuous projection
over `X × unitInterval` gives [local whole-interval charts](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/ClosedCylinderSubdivisionData.lean),
with linear coordinates when the input coordinates are linear, over any semiring. Separately, finite ordered whole-cylinder charts with continuous
weights in `[0,1]` summing to one and closed cozero supports inside the chart base sets give [base-preserving,
bottom-fixing transport](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/FiniteTransport/Projection.lean) from the standard pullback
of the entire zero slice. A [finite open cylinder cover on a normal base](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/FiniteTransport/Existence.lean)
supplies the weights. Models may vary; full homotopy invariance is not asserted.

**Varying-rank atlases.** Over a field with a given topology, a supplied [finite-rank linear atlas](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/FiniteRank.lean)
allows unbounded, locally varying ranks, including zero, on the original fibers and total space. Its
[projection is continuous, open and quotient](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/FiniteRank/Projection.lean),
and its zero section is an embedding. Further separation and countability results use the corresponding
base and exact chart-coordinate hypotheses, not continuous scalar operations or a global fixed model.

**Stable complements.** Over a compact normal base, a finite-rank atlas over real or complex scalars has a
[defined stable complement](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/FiniteRank/StableComplement.lean)
in the finite coordinate space of its specified trivial embedding. The complement has its range-graph
finite-rank atlas, and its sum with the original family has a full-base trivialization in that coordinate
space. The ranks may vary; their pointwise sum is the ambient dimension. The original total-space topology
is unchanged. Separately, algebraic split families in a finite-dimensional normed space over a complete
nontrivially normed field, with continuous original-total embedding and retraction, have a
[fixed-model sum chart](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/VectorBundle/ProjectorAtlas/SplitFamilySum.lean)
over an arbitrary topological base, without topologies on the original fibres or their common model.

**Sharp projection criteria.** A fiber-bundle projection is an [open embedding](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/Projection.lean)
exactly when every original fiber is subsingleton, and [proper](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/Proper.lean)
exactly when each fiber is compact. Its total space is [second-countable](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/FiberBundle/Countability.lean)
exactly when the base or model is empty, or both are second-countable, without separation hypotheses.
Further compactness, separability and Lindelöf criteria are in the [detailed guide](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/docs/Results.md#topological-properties-of-bundle-total-spaces).

## Main results

Its formalization.yaml lists 14 main results, and the scan finds 14 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
