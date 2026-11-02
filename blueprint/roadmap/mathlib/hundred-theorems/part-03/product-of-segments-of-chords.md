---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi
mathlib_file: Mathlib/Geometry/Euclidean/Sphere/Power.lean
---

# Product of Segments of Chords

**Intersecting Chords Theorem**.

```lean
EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {P : Type u_2} [MetricSpace P]
  [NormedAddTorsor V P] {a b c d p : P} (h : EuclideanGeometry.Cospherical {a, b, c, d})
  (hapb : EuclideanGeometry.angle a p b = Real.pi)
  (hcpd : EuclideanGeometry.angle c p d = Real.pi) : dist a p * dist b p = dist c p * dist d p
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Affine span](../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Cauchy-Schwarz inequality](../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Cluster point](../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Intermediate value theorem](../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Self-adjoint operator](../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](the-binomial-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Power.html#EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi)
- [Source of `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi` in Mathlib/Geometry/Euclidean/Sphere/Power.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Power.lean#L118)
- [Freek Wiedijk's 100 theorems, no. 55](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L283)
- [1000+ theorems list: Q2266397](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2132)
- [1000+ theorems project: Q2266397](https://1000-plus.github.io/?length=-1#Q2266397)
- [Wikipedia: Intersecting chords theorem](https://en.wikipedia.org/wiki/Intersecting_chords_theorem)
- [Wikidata: Q2266397](https://www.wikidata.org/wiki/Q2266397)
