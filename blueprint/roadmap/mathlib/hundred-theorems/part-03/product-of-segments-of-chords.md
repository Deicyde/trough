---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi
mathlib_file: Mathlib/Geometry/Euclidean/Sphere/Power.lean
---

# Product of Segments of Chords

**Intersecting Chords Theorem**.

```lean
EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {P : Type u_2} [MetricSpace P]
  [NormedAddTorsor V P] {a b c d p : P} (h : EuclideanGeometry.Cospherical {a, b, c, d})
  (hapb : EuclideanGeometry.angle a p b = Real.pi)
  (hcpd : EuclideanGeometry.angle c p d = Real.pi) : dist a p * dist b p = dist c p * dist d p
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Affine span](../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Power.html#EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi)
- [Source of `EuclideanGeometry.mul_dist_eq_mul_dist_of_cospherical_of_angle_eq_pi` in Mathlib/Geometry/Euclidean/Sphere/Power.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Power.lean#L118)
- [Freek Wiedijk's 100 theorems, no. 55](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L283)
- [1000+ theorems list: Q2266397](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2132)
- [1000+ theorems project: Q2266397](https://1000-plus.github.io/?length=-1#Q2266397)
- [Wikipedia: Intersecting chords theorem](https://en.wikipedia.org/wiki/Intersecting_chords_theorem)
- [Wikidata: Q2266397](https://www.wikidata.org/wiki/Q2266397)
