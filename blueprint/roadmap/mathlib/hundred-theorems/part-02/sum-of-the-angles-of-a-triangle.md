---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.angle_add_angle_add_angle_eq_pi
mathlib_file: Mathlib/Geometry/Euclidean/Triangle.lean
---

# Sum of the Angles of a Triangle

The **sum of the angles of a triangle** (possibly degenerate, where two
given vertices are distinct), angle-at-point.

```lean
EuclideanGeometry.angle_add_angle_add_angle_eq_pi.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P] {p₁ p₂ : P}
  (p₃ : P) (h : p₂ ≠ p₁) :
  EuclideanGeometry.angle p₁ p₂ p₃ + EuclideanGeometry.angle p₂ p₃ p₁ +
      EuclideanGeometry.angle p₃ p₁ p₂ =
    Real.pi
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Cauchy-Schwarz inequality](../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Closed map](../../overview/topology/general-topology/part-01/closed-map.md)
- [Cluster point](../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Generating sets](../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Intermediate value theorem](../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../overview/topology/general-topology/part-01/open-map.md)
- [Self-adjoint operator](../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.angle_add_angle_add_angle_eq_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Triangle.html#EuclideanGeometry.angle_add_angle_add_angle_eq_pi)
- [Source of `EuclideanGeometry.angle_add_angle_add_angle_eq_pi` in Mathlib/Geometry/Euclidean/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Triangle.lean#L314)
- [Freek Wiedijk's 100 theorems, no. 27](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L131)
