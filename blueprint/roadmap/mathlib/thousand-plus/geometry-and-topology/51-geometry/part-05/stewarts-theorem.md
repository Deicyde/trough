---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.dist_sq_mul_dist_add_dist_sq_mul_dist
mathlib_file: Mathlib/Geometry/Euclidean/Triangle.lean
---

# Stewart's theorem

**Stewart's Theorem**.

```lean
EuclideanGeometry.dist_sq_mul_dist_add_dist_sq_mul_dist.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P] (a b c p : P)
  (h : EuclideanGeometry.angle b p c = Real.pi) :
  dist a b ^ 2 * dist c p + dist a c ^ 2 * dist b p =
    dist b c * (dist a p ^ 2 + dist b p * dist c p)
```

## Depends on

- [Angle](../../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [The Law of Cosines](../../../../hundred-theorems/part-05/the-law-of-cosines.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.dist_sq_mul_dist_add_dist_sq_mul_dist`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Triangle.html#EuclideanGeometry.dist_sq_mul_dist_add_dist_sq_mul_dist)
- [Source of `EuclideanGeometry.dist_sq_mul_dist_add_dist_sq_mul_dist` in Mathlib/Geometry/Euclidean/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Triangle.lean#L382)
- [1000+ theorems list: Q739403](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L815)
- [1000+ theorems project: Q739403](https://1000-plus.github.io/all.html?length=-1#Q739403)
- [Wikipedia: Stewart's theorem](https://en.wikipedia.org/wiki/Stewart's_theorem)
- [Wikidata: Q739403](https://www.wikidata.org/wiki/Q739403)
