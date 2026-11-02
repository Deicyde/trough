---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two
mathlib_file: Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean
---

# Geometric mean theorem

**Geometric mean theorem** (or right triangle altitude theorem): in a right-angled triangle
`p₁ p₂ p₃` with the right angle at `p₂`, the square of the altitude `dist p₂ p₄` to the
hypotenuse is the product of the two segments `dist p₁ p₄` and `dist p₃ p₄` into which its foot
`p₄` divides the hypotenuse.

```lean
EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two.{u_1, u_2} {V : Type u_1}
  {P : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P]
  [NormedAddTorsor V P] {p₁ p₂ p₃ p₄ : P} (hf : Sbtw ℝ p₁ p₄ p₃)
  (hc : EuclideanGeometry.angle p₁ p₄ p₂ = Real.pi / 2)
  (h : EuclideanGeometry.angle p₁ p₂ p₃ = Real.pi / 2) : dist p₂ p₄ ^ 2 = dist p₁ p₄ * dist p₃ p₄
```

## Depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Cauchy-Schwarz inequality](../../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Generating sets](../../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Self-adjoint operator](../../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Squeeze theorem](../../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.html#EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two)
- [Source of `EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two` in Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean#L501)
- [1000+ theorems list: Q2226868](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2118)
- [1000+ theorems project: Q2226868](https://1000-plus.github.io/?length=-1#Q2226868)
- [Wikipedia: Geometric mean theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem)
- [Wikidata: Q2226868](https://www.wikidata.org/wiki/Q2226868)
