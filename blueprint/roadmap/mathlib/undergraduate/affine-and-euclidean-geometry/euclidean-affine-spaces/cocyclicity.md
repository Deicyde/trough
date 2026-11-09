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
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.Concyclic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Basic.html#EuclideanGeometry.Concyclic)
- [Source of `EuclideanGeometry.Concyclic` in Mathlib/Geometry/Euclidean/Sphere/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Euclidean/Sphere/Basic.lean#L235)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L267)
