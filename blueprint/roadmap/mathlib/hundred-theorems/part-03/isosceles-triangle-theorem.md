---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.angle_eq_angle_of_dist_eq
mathlib_file: Mathlib/Geometry/Euclidean/Triangle.lean
---

# Isosceles Triangle Theorem

**Isosceles Triangle Theorem**: Pons asinorum, angle-at-point form.

```lean
EuclideanGeometry.angle_eq_angle_of_dist_eq.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]
  {p₁ p₂ p₃ : P} (h : dist p₁ p₂ = dist p₁ p₃) :
  EuclideanGeometry.angle p₁ p₂ p₃ = EuclideanGeometry.angle p₁ p₃ p₂
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.angle_eq_angle_of_dist_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Triangle.html#EuclideanGeometry.angle_eq_angle_of_dist_eq)
- [Source of `EuclideanGeometry.angle_eq_angle_of_dist_eq` in Mathlib/Geometry/Euclidean/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Triangle.lean#L281)
- [Freek Wiedijk's 100 theorems, no. 65](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L327)
