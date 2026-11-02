---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.Sphere.thales_theorem
mathlib_file: Mathlib/Geometry/Euclidean/Angle/Sphere.lean
---

# Thales's theorem

**Alias** of `EuclideanGeometry.Sphere.angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter`.

---

**Thales' theorem**: The angle inscribed in a semicircle is a right angle.

```lean
EuclideanGeometry.Sphere.thales_theorem.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]
  {p₁ p₂ p₃ : P} {s : EuclideanGeometry.Sphere P} (hd : s.IsDiameter p₁ p₃) :
  EuclideanGeometry.angle p₁ p₂ p₃ = Real.pi / 2 ↔ p₂ ∈ s
```

## Depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
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

- [Mathlib documentation: `EuclideanGeometry.Sphere.thales_theorem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Sphere.html#EuclideanGeometry.Sphere.thales_theorem)
- [Source of `EuclideanGeometry.Sphere.thales_theorem` in Mathlib/Geometry/Euclidean/Angle/Sphere.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L105)
- [1000+ theorems list: Q285719](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L343)
- [1000+ theorems project: Q285719](https://1000-plus.github.io/?length=-1#Q285719)
- [Wikipedia: Thales's theorem](https://en.wikipedia.org/wiki/Thales's_theorem)
- [Wikidata: Q285719](https://www.wikidata.org/wiki/Q285719)
