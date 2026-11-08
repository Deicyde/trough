---
navigation: transparent
---

# Brouwer fixed points on complex… to Fundamental groups of…

## Highlights

- [Brouwer fixed points on complex disks](brouwer-fixed-points-on-complex-disks.md)
- [Hairy-ball theorem for the metric two-sphere](hairy-ball-theorem-for-the-metric-two-sphere.md)
- [Free fundamental groups of circle bouquets](free-fundamental-groups-of-circle-bouquets.md)
- [Sphere cogroups and sharp cocommutativity](sphere-cogroups-and-sharp-cocommutativity.md)
- [Nontrivial second homotopy group of the metric two-sphere](nontrivial-second-homotopy-group-of-the-metric-t.md)

## Headline results

- [H-space fundamental groups commute](h-space-fundamental-groups-commute.md)

**Normalized circle fundamental groups and degree.** For real `T ≠ 0`,
[`AddCircle.fundamentalGroupEquivInt`](https://github.com/FormalFrontier/fundamental-groupoids/blob/main/FundamentalGroupoids/AlgebraicTopology/FundamentalGroup/Circle.lean)
is supplied by Fundamental Groupoids and identifies `π₁(AddCircle T, 0)`
with `Multiplicative ℤ`, including signed periods, lifted endpoints and
agreement with the complex unit circle.
[`Circle.degree`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleDegree.lean) classifies free
homotopy of arbitrary continuous circle self-maps. Composition multiplies
degree, while pointwise multiplication adds it, including multiset products
with repeated factors. The map `z ↦ z^n` has degree `n : ℤ`, and degree different
from `1` is a sufficient, not necessary, fixed-point condition. No based-map
premise is needed.

**Disk boundary degree and non-retraction.** Every continuous map
`G : C(Metric.closedBall (0 : ℂ) 1, Circle)` has boundary restriction of
degree zero, so that restriction is not the identity on `Circle`
([`Disk`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/Disk.lean)). The boundary map is the
coordinate-preserving inclusion of the complex unit circle into the closed
unit disk; no basedness premise is imposed. This is not a theorem about
arbitrary-dimensional disks or an extension converse.

**Forward intersections with spheres.** In a real inner-product affine space,
[`Sphere.rayInter`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/ForwardRay.lean) continues from
`q` through a distinct closed-ball point `x` to the sphere, with parameter
at least one even when `q` is outside the ball. For a closed-ball start,
positive sphere-intersection parameters are characterized by the upper root,
and a boundary second point is fixed, including the diagonal. The total
parameter and point formulas are jointly continuous on the whole off-diagonal;
boundary starts agree with Mathlib's `Sphere.secondInter` when `x` is in the
closed ball. No finite-dimensionality, completeness or global radius-sign
assumption is needed.

**Continuous ray maps and boundary-only strict retractions.** In a real
inner-product affine torsor,
[`Sphere.rayInterMap`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/ForwardRayMap.lean) turns an
ambient-valued continuous map `f` on a closed ball, with `f x ≠ x` at every
point, into a continuous map to its sphere. If boundary points have images
in the closed ball, composition with the boundary inclusion is exactly the
identity. No image condition is imposed on interior points; a fixed-point-free
continuous closed-ball selfmap is a specialization.
Vector and point universes are independent, and radii are arbitrary real
numbers, with no finite-dimensionality, completeness or nontriviality premise.
This generalizes the boundary-fixing construction in May's closed-disk
argument (Chapter 1, §6), not a fixed-point theorem in this generality.

**Generic stereographic geometry.** For
`E : Type u` with `[NormedAddCommGroup E]` and `[InnerProductSpace ℝ E]`,
let `S := Metric.sphere (0 : E) 1` be the canonical sphere subtype,
`p q : S`, `H := (ℝ ∙ (p : E))ᗮ` and
`σ := stereographic (norm_eq_of_mem_sphere p)`.
[`stereographicHomeomorph p`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/Stereographic.lean)
identifies `({p}ᶜ : Set S)` with `H`; for `hpq : p ≠ q`,
`stereographicOverlapHomeomorph p q hpq` identifies
`({p}ᶜ ∩ {q}ᶜ : Set S)` with `H \ {σ q}`.
These retain Mathlib's factor-2 stereographic map: the excluded pole is
`+p`, and the one-pole inverse sends `0` to `-p`. The overlap target deletes
zero exactly when `q = -p`.

- [Last-axis one-point compactification coordinates](last-axis-one-point-compactification-coordinates.md)
- [Finite generalized loops and based sphere-map classes](finite-generalized-loops-and-based-sphere-map-cl.md)

**Positive-dimensional sphere pinch and folding.** For `d = n + 1 > 0`,
[`Metric.Sphere.pinch n`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/SpherePinch.lean) maps the
existing last-axis unit sphere `Sᵈ` to its two-factor point-wide-pushout.
Its cube pullback traverses the left factor before the right factor in
coordinate zero; the two closed-half formulas agree at the separating slice,
and fixed quarter-point witnesses give distinct non-head values.
`surjective_pinch` and `isQuotientMap_pinch` show that it is surjective and a
quotient map for the topology of that categorical target. `pinch_eq_head_iff`
identifies its head fiber with the equator where ambient coordinate zero
vanishes; `pinch_eq_pinch_iff` says that two points have the same image exactly
when they are equal or both lie on that equator.
[`Metric.Sphere.pinchFold`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SpherePinchFold.lean)
is jointly continuous on the ordinary compact-open based-map subtype and
preserves simultaneous paths of its factors, for arbitrary topological targets.
Its identity/constant folds in opposite orders differ at the left quarter-point,
including for the circle.
[`pinch_fold_class`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SpherePinch.lean)
compares folding based maps `F, G` with the existing homotopy-group
multiplication: writing `J` for the inverse sphere-class comparison, the
result is `J(G) * J(F)`, including in dimension one. Each original factor
retraction composed with the pinch is homotopic to the identity relative to
the north pole. `pinch_fold_homotopicRel_assoc` gives associativity of folding
three arbitrary based maps up to north-pole-relative homotopy for every `d > 0`;
its original three-inclusion specialization, `pinch_homotopicRel_coassoc`,
gives coassociativity into the three-factor point-wide-pushout. The two
iterated maps are not equal: `pinch_coassoc_nondegenerate` exhibits their
different values at the same cube time `3/8`, and three distinct non-head
inclusion values of the left nesting. For `d = n + 2 ≥ 2`,
`pinch_fold_homotopicRel_swap` gives a north-pole-relative homotopy when the
two arbitrary based factor maps are interchanged. Its original-inclusion specialization,
`pinch_homotopicRel_swap`, identifies the pinch up to that relative homotopy
with the original categorical factor swap after the pinch. Raw folding and
based postcomposition allow independently universed targets with only a
topology. No dimension-one cocommutativity, zero-sphere pinch or choice of
sphere orientation is asserted by these geometric comparisons.

**Based coordinate reflections and coinverses.** For every positive sphere
dimension `d = n + 1`, including S¹, and every pre-last axis `i : Fin (n + 1)`,
[`coordinateReflection`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/SphereCoordinateReflection.lean)
negates exactly ambient coordinate `i.castSucc` and fixes the last-axis north
pole. It is involutive, differs from the identity, and is uniquely determined
by its cube pullback: reversing axis `i` of the original collapse. For an
arbitrary based map to a topological space,
[`coordinateReflection_precomp_class`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereCoordinateReflection.lean)
identifies precomposition by this reflection with the existing homotopy-group
inverse. Folding the pinch with reflection and identity in either order is
homotopic to the north constant relative to the north pole, for every such
axis; neither folded map is equal to that constant. These results do not
require commutativity and do not assert S¹ cocommutativity.

- [Positive-dimensional spheres as cogroups](sphere-cogroups-and-sharp-cocommutativity.md)
- [Homotopy groups and the sphere-map group](homotopy-groups-and-the-sphere-map-group.md)
- [Sharp cocommutativity of sphere cogroups](sphere-cogroups-and-sharp-cocommutativity.md)
- [Nontrivial second homotopy group of S²](nontrivial-second-homotopy-group-of-s2.md)

**Topology of real normed unit spheres.** The topology-only APIs in
[`Homotopy.Sphere`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/Sphere.lean) are stated for
`E : Type u` with `[NormedAddCommGroup E] [NormedSpace ℝ E]`, using its
original norm and `S := Metric.sphere (0 : E) 1`.
`contractibleSpace_sphere_compl_singleton p` gives
`ContractibleSpace ({p}ᶜ : Set S)` without a rank premise; simple connectivity
follows from Mathlib's `SimplyConnectedSpace.ofContractible`.
`pathConnectedSpace_sphere_compl_poles p q h` gives
`PathConnectedSpace ({p}ᶜ ∩ {q}ᶜ : Set S)` for all `p,q`, including equal
poles, when `h : 2 < Module.rank ℝ E` (cardinal rank).
`simplyConnectedSpace_unitSphere h` gives `SimplyConnectedSpace S` under the
same rank bound, including the usual `Sⁿ` for `n ≥ 2` and infinite-dimensional
spaces. No completeness, finite-dimensionality, supplied pole for the whole
sphere, ambient connectivity or overlap-nonemptiness assumption is needed.
These statements generalize May's finite Euclidean sphere setting; the
orthogonal-coordinate charts above still require an inner product.

- [Canonical antipodal quotient covering](canonical-antipodal-quotient-covering.md)
- [Real projective fundamental groups and lifted endpoints](real-projective-fundamental-groups-and-lifted-en.md)
- [Boundary-only fixed points on complex closed balls](brouwer-fixed-points-on-complex-disks.md)

**Quotient presentations of topological wide pushouts (Fundamental Groupoids).** [`TopCat.widePushoutHomeomorph`](https://github.com/FormalFrontier/fundamental-groupoids/blob/main/FundamentalGroupoids/Topology/Category/TopCat/Limits/WidePushout.lean)
identifies the quotient of `B ⊕ Σ i, X i` by `b ∼ (i, f i b)` with the
categorical wide pushout of arbitrary continuous maps `f i : B ⟶ X i`,
preserving the head and every factor. Continuity and descent have an
independent target universe; empty and singleton families need no separation,
compactness or homotopy assumptions.

- [Embeddings, closed maps and neighborhoods of point-wide-pushouts](embeddings-closed-maps-and-neighborhoods-of-poin.md)

**Parametrized continuity and homotopy gluing (Fundamental Groupoids).** [`TopCat.continuous_prod_iff_of_isColimit`](https://github.com/FormalFrontier/fundamental-groupoids/blob/main/FundamentalGroupoids/Topology/Category/TopCat/Limits/Products.lean)
checks joint continuity on the legs of any supplied topological colimit under
Mathlib's `LocallyCompactPair P Y` hypothesis; a locally compact parameter
suffices, with no separation condition on the target. Parameter and target
universes are independent. Compatible families on a wide pushout's head and
every factor descend continuously, with computation, uniqueness, fixed-parameter
and reparametrization laws. Compatible interval homotopies glue at all times,
without requiring the common point to stay fixed. Point-relative descent is
supplied by
[`TopCat.widePushoutPointHomotopyRel`](https://github.com/FormalFrontier/fundamental-groupoids/blob/main/FundamentalGroupoids/Topology/Homotopy/WidePushout.lean).

- [Point-relative equivalences and contractions](point-relative-equivalences-and-contractions.md)
- [Factor retractions and separation of point-wide-pushouts](factor-retractions-and-separation-of-point-wide.md)

**Compact subsets meet finitely many pointed factors.** [`finite_widePushoutPointSupport`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/Compactness.lean)
applies to arbitrary indexed T₁ spaces attached at chosen points. A compact
subset of their categorical wide pushout meets only finitely many factors
away from the common point. The support API characterizes coverings by the
common point plus factor ranges; every continuous map from a compact domain,
including a path, has such a finite-factor covering. There is no Hausdorff,
compact-factor, countability or finite-index assumption.

- [Charts around a common subset](charts-around-a-common-subset.md)
- [Fundamental groups of factor-plus-core charts](fundamental-groups-of-factor-plus-core-charts.md)
