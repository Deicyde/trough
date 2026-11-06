# Ptolemy’s Theorem

**Ptolemy’s Theorem**.

```lean
EuclideanGeometry.mul_dist_add_mul_dist_eq_mul_dist_of_cospherical.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {P : Type u_2} [MetricSpace P]
  [NormedAddTorsor V P] {a b c d p : P} (h : EuclideanGeometry.Cospherical {a, b, c, d})
  (hapc : EuclideanGeometry.angle a p c = Real.pi)
  (hbpd : EuclideanGeometry.angle b p d = Real.pi) :
  dist a b * dist c d + dist b c * dist d a = dist a c * dist b d
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Product of Segments of Chords](../part-02/product-of-segments-of-chords.md)
- [Stewart's theorem](../../thousand-plus/geometry-and-topology/51-geometry/stewarts-theorem.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.mul_dist_add_mul_dist_eq_mul_dist_of_cospherical`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Sphere/Ptolemy.html#EuclideanGeometry.mul_dist_add_mul_dist_eq_mul_dist_of_cospherical)
- [Source of `EuclideanGeometry.mul_dist_add_mul_dist_eq_mul_dist_of_cospherical` in Mathlib/Geometry/Euclidean/Sphere/Ptolemy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Sphere/Ptolemy.lean#L56)
- [Freek Wiedijk's 100 theorems, no. 95](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L488)
- [1000+ theorems list: Q459547](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L454)
- [1000+ theorems project: Q459547](https://1000-plus.github.io/all.html?length=-1#Q459547)
- [Wikipedia: Ptolemy's theorem](https://en.wikipedia.org/wiki/Ptolemy's_theorem)
- [Wikidata: Q459547](https://www.wikidata.org/wiki/Q459547)
