---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.Sphere.dist_sq_eq_mul_dist_of_tangent_and_secant
mathlib_file: Mathlib/Geometry/Euclidean/Sphere/Power.lean
---

# Tangent-secant theorem

**Tangent-Secant Theorem**. The square of the tangent length equals
the product of secant segment lengths.

```lean
EuclideanGeometry.Sphere.dist_sq_eq_mul_dist_of_tangent_and_secant.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {P : Type u_2} [MetricSpace P]
  [NormedAddTorsor V P] {a b t p : P} {s : EuclideanGeometry.Sphere P} (ha : a ∈ s) (hb : b ∈ s)
  (hp : p ∈ line[ℝ, a, b]) (h_tangent : s.IsTangentAt t line[ℝ, p, t]) :
  dist p t ^ 2 = dist p a * dist p b
```

## Depends on

- [Affine span](../../../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Orthogonal complement](../../../../overview/analysis/hilbert-spaces/orthogonal-complement.md)

## Proof depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Squeeze theorem](../../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.Sphere.dist_sq_eq_mul_dist_of_tangent_and_secant`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Power.html#EuclideanGeometry.Sphere.dist_sq_eq_mul_dist_of_tangent_and_secant)
- [Source of `EuclideanGeometry.Sphere.dist_sq_eq_mul_dist_of_tangent_and_secant` in Mathlib/Geometry/Euclidean/Sphere/Power.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Power.lean#L298)
- [1000+ theorems list: Q2267175](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2138)
- [1000+ theorems project: Q2267175](https://1000-plus.github.io/?length=-1#Q2267175)
- [Wikipedia: Tangent-secant theorem](https://en.wikipedia.org/wiki/Tangent-secant_theorem)
- [Wikidata: Q2267175](https://www.wikidata.org/wiki/Q2267175)
