---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ConvexOn.continuousOn
mathlib_file: Mathlib/Analysis/Convex/Continuous.lean
---

# Continuity

Mathlib states this as `ConvexOn.continuousOn`.

```lean
ConvexOn.continuousOn.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {C : Set E}
  {f : E → ℝ} [FiniteDimensional ℝ E] (hC : IsOpen C) (hf : ConvexOn ℝ C f) : ContinuousOn f C
```

## Depends on

- [Convex function](../../../../overview/analysis/convexity/convex-function.md)
- [Field $\R$ of real numbers](../../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Metric structure](../../topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)

## Proof depends on

- [Affine span](../../../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Aleph numbers](../../../../overview/logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Barycenter](../../../../overview/geometry/affine-and-euclidean-geometry/barycenter.md)
- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Complementary subspaces](../../../linear-algebra/fundamentals/complementary-subspaces.md)
- [Completeness of R](../../topology-of-r/completeness-of-r.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Convex hull of a subset of an affine real space](../../../affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fundamental sequences](../../../../overview/logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Hilbert basis theorem](../../../../overview/general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Homeomorphisms](../../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isomorphism with $K^n$](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Local ring](../../../../overview/general-algebra/rings/local-ring.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Polynomial in several indeterminates](../../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Quotient space](../../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Squeeze theorem](../../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subring](../../../../overview/general-algebra/rings/subring.md)
- [The Fundamental Theorem of Arithmetic](../../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)
- [Well-ordering theorem](../../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `ConvexOn.continuousOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Continuous.html#ConvexOn.continuousOn)
- [Source of `ConvexOn.continuousOn` in Mathlib/Analysis/Convex/Continuous.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Continuous.lean#L203)
- [Mathlib undergraduate list: Single Variable Real Analysis › Convexity › continuity and differentiability of convex functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L361)
