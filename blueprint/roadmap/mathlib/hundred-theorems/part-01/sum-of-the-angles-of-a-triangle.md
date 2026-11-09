# Sum of the Angles of a Triangle

The **sum of the angles of a triangle** (possibly degenerate, where two
given vertices are distinct), angle-at-point.

```lean
EuclideanGeometry.angle_add_angle_add_angle_eq_pi.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P] {p₁ p₂ : P}
  (p₃ : P) (h : p₂ ≠ p₁) :
  EuclideanGeometry.angle p₁ p₂ p₃ + EuclideanGeometry.angle p₂ p₃ p₁ +
      EuclideanGeometry.angle p₃ p₁ p₂ =
    Real.pi
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Cauchy-Schwarz inequality](../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.angle_add_angle_add_angle_eq_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Triangle.html#EuclideanGeometry.angle_add_angle_add_angle_eq_pi)
- [Source of `EuclideanGeometry.angle_add_angle_add_angle_eq_pi` in Mathlib/Geometry/Euclidean/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Euclidean/Triangle.lean#L314)
- [Freek Wiedijk's 100 theorems, no. 27](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L131)
