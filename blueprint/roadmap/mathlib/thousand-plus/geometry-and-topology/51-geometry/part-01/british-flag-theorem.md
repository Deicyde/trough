---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.dist_sq_add_dist_sq_eq_dist_sq_add_dist_sq_of_angle_eq_pi_div_two
mathlib_file: Mathlib/Geometry/Euclidean/BritishFlag.lean
---

# British flag theorem

**British flag theorem**: for a rectangle `a b c d` and any point `p` (not necessarily in
the plane of the rectangle), the sum of the squares of the distances from `p` to the opposite
corners `a` and `c` equals the sum of the squares of the distances from `p` to `b` and `d`.

```lean
EuclideanGeometry.dist_sq_add_dist_sq_eq_dist_sq_add_dist_sq_of_angle_eq_pi_div_two.{u_1, u_2}
  {V : Type u_1} {P : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P]
  [NormedAddTorsor V P] {a b c d : P} (h : midpoint ℝ a c = midpoint ℝ b d)
  (ha : EuclideanGeometry.angle b a d = Real.pi / 2) (p : P) :
  dist p a ^ 2 + dist p c ^ 2 = dist p b ^ 2 + dist p d ^ 2
```

## Depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Self-adjoint operator](../../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Squeeze theorem](../../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.dist_sq_add_dist_sq_eq_dist_sq_add_dist_sq_of_angle_eq_pi_div_two`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/BritishFlag.html#EuclideanGeometry.dist_sq_add_dist_sq_eq_dist_sq_add_dist_sq_of_angle_eq_pi_div_two)
- [Source of `EuclideanGeometry.dist_sq_add_dist_sq_eq_dist_sq_add_dist_sq_of_angle_eq_pi_div_two` in Mathlib/Geometry/Euclidean/BritishFlag.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/BritishFlag.lean#L100)
- [1000+ theorems list: Q4971339](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2965)
- [1000+ theorems project: Q4971339](https://1000-plus.github.io/?length=-1#Q4971339)
- [Wikipedia: British flag theorem](https://en.wikipedia.org/wiki/British_flag_theorem)
- [Wikidata: Q4971339](https://www.wikidata.org/wiki/Q4971339)
