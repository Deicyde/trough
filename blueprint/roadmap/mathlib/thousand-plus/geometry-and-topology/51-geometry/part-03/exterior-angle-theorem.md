---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.exterior_angle_eq_angle_add_angle
mathlib_file: Mathlib/Geometry/Euclidean/Triangle.lean
---

# Exterior angle theorem

The **Exterior angle theorem**. an exterior angle of a triangle is equal to the sum of the
measures of the remote interior angles.

```lean
EuclideanGeometry.exterior_angle_eq_angle_add_angle.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]
  {p₁ p₂ p₃ : P} (p : P) (h : Sbtw ℝ p p₁ p₂) :
  EuclideanGeometry.angle p₃ p₁ p =
    EuclideanGeometry.angle p₁ p₃ p₂ + EuclideanGeometry.angle p₃ p₂ p₁
```

## Depends on

- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Sum of the Angles of a Triangle](../../../../hundred-theorems/part-02/sum-of-the-angles-of-a-triangle.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.exterior_angle_eq_angle_add_angle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Triangle.html#EuclideanGeometry.exterior_angle_eq_angle_add_angle)
- [Source of `EuclideanGeometry.exterior_angle_eq_angle_add_angle` in Mathlib/Geometry/Euclidean/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Triangle.lean#L325)
- [1000+ theorems list: Q5421989](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3170)
- [1000+ theorems project: Q5421989](https://1000-plus.github.io/all.html?length=-1#Q5421989)
- [Wikipedia: Exterior angle theorem](https://en.wikipedia.org/wiki/Exterior_angle_theorem)
- [Wikidata: Q5421989](https://www.wikidata.org/wiki/Q5421989)
