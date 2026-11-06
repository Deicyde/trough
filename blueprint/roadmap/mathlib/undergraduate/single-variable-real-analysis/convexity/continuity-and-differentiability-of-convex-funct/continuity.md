# Continuity (continuity and differentiability of convex functions)

Mathlib states this as `ConvexOn.continuousOn`.

```lean
ConvexOn.continuousOn.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {C : Set E}
  {f : E → ℝ} [FiniteDimensional ℝ E] (hC : IsOpen C) (hf : ConvexOn ℝ C f) : ContinuousOn f C
```

## Depends on

- [Convex function](../../../../overview/analysis/convexity/convex-function.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Affine span](../../../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Convex hull of a subset of an affine real space](../../../affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Linear independence](../../../linear-algebra/fundamentals/linear-independence.md)
- [Metric structure](../../topology-of-r/metric-structure.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `ConvexOn.continuousOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Continuous.html#ConvexOn.continuousOn)
- [Source of `ConvexOn.continuousOn` in Mathlib/Analysis/Convex/Continuous.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Continuous.lean#L203)
- [Mathlib undergraduate list: Single Variable Real Analysis › Convexity › continuity and differentiability of convex functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L361)
