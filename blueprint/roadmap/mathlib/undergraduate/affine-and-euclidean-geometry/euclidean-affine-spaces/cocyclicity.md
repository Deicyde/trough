---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.Concyclic
mathlib_file: Mathlib/Geometry/Euclidean/Sphere/Basic.lean
---

# Cocyclicity

A set of points is concyclic if it is cospherical and coplanar. (Most results are stated
directly in terms of `Cospherical` instead of using `Concyclic`.)

```lean
EuclideanGeometry.Concyclic.{u_1, u_2} {V : Type u_1} {P : Type u_2} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P] (ps : Set P) : Prop
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.Concyclic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Basic.html#EuclideanGeometry.Concyclic)
- [Source of `EuclideanGeometry.Concyclic` in Mathlib/Geometry/Euclidean/Sphere/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Basic.lean#L235)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L267)
