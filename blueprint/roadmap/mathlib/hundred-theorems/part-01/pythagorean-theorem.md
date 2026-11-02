---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two
mathlib_file: Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean
---

# Pythagorean Theorem

**Pythagorean theorem**, if-and-only-if angle-at-point form.

```lean
EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two.{u_1, u_2} {V : Type u_1}
  {P : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P]
  [NormedAddTorsor V P] (p₁ p₂ p₃ : P) :
  dist p₁ p₃ * dist p₁ p₃ = dist p₁ p₂ * dist p₁ p₂ + dist p₃ p₂ * dist p₃ p₂ ↔
    EuclideanGeometry.angle p₁ p₂ p₃ = Real.pi / 2
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.html#EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two)
- [Source of `EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two` in Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean#L326)
- [Freek Wiedijk's 100 theorems, no. 4](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L20)
- [1000+ theorems list: Q11518](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L14)
- [1000+ theorems project: Q11518](https://1000-plus.github.io/?length=-1#Q11518)
- [Wikipedia: Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)
- [Wikidata: Q11518](https://www.wikidata.org/wiki/Q11518)
