---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_zero
mathlib_file: Mathlib/Geometry/Euclidean/Sphere/Power.lean
---

# Intersecting secants theorem

**Intersecting Secants Theorem**.

```lean
EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_zero.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {P : Type u_2} [MetricSpace P]
  [NormedAddTorsor V P] {a b c d p : P} (h : EuclideanGeometry.Cospherical {a, b, c, d})
  (hab : a ≠ b) (hcd : c ≠ d) (hapb : EuclideanGeometry.angle a p b = 0)
  (hcpd : EuclideanGeometry.angle c p d = 0) : dist a p * dist b p = dist c p * dist d p
```

## Depends on

- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Affine span](../../../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Aleph numbers](../../../../overview/logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Cauchy-Schwarz inequality](../../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Fundamental sequences](../../../../overview/logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Ideal of a commutative ring](../../../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Noetherian ring](../../../../overview/general-algebra/rings/noetherian-ring.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Principal ideal domain](../../../../overview/general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Self-adjoint operator](../../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Squeeze theorem](../../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)
- [Well-ordering theorem](../../../general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Power.html#EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_zero)
- [Source of `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_zero` in Mathlib/Geometry/Euclidean/Sphere/Power.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Power.lean#L208)
- [1000+ theorems list: Q1727461](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1854)
- [1000+ theorems project: Q1727461](https://1000-plus.github.io/?length=-1#Q1727461)
- [Wikipedia: Intersecting secants theorem](https://en.wikipedia.org/wiki/Intersecting_secants_theorem)
- [Wikidata: Q1727461](https://www.wikidata.org/wiki/Q1727461)
