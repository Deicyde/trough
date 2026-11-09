# Geometric mean theorem

**Geometric mean theorem** (or right triangle altitude theorem): in a right-angled triangle
`p₁ p₂ p₃` with the right angle at `p₂`, the square of the altitude `dist p₂ p₄` to the
hypotenuse is the product of the two segments `dist p₁ p₄` and `dist p₃ p₄` into which its foot
`p₄` divides the hypotenuse.

```lean
EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two.{u_1, u_2} {V : Type u_1}
  {P : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P]
  [NormedAddTorsor V P] {p₁ p₂ p₃ p₄ : P} (hf : Sbtw ℝ p₁ p₄ p₃)
  (hc : EuclideanGeometry.angle p₁ p₄ p₂ = Real.pi / 2)
  (h : EuclideanGeometry.angle p₁ p₂ p₃ = Real.pi / 2) : dist p₂ p₄ ^ 2 = dist p₁ p₄ * dist p₃ p₄
```

## Depends on

- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Angle](../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.html#EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two)
- [Source of `EuclideanGeometry.dist_sq_eq_dist_mul_dist_of_angle_eq_pi_div_two` in Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Euclidean/Angle/Unoriented/RightAngle.lean#L501)
- [1000+ theorems list: Q2226868](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2118)
- [1000+ theorems project: Q2226868](https://1000-plus.github.io/all.html?length=-1#Q2226868)
- [Wikipedia: Geometric mean theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem)
- [Wikidata: Q2226868](https://www.wikidata.org/wiki/Q2226868)
