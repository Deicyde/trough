# Heron’s Formula

**Heron's formula** for triangle. The area of a triangle with side lengths
`a`, `b`, and `c` is `√(s * (s - a) * (s - b) * (s - c))` where `s = (a + b + c) / 2` is the
semiperimeter.

```lean
Affine.Triangle.volume_eq_sqrt_mul_sub_mul_sub_mul_sub.{u_1, u_2} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]
  (t : Affine.Triangle ℝ P) {i₁ i₂ i₃ : Fin 3} (h₁₂ : i₁ ≠ i₂) (h₁₃ : i₁ ≠ i₃) (h₂₃ : i₂ ≠ i₃) :
  Affine.Simplex.volume t =
    √((dist (t.points i₁) (t.points i₂) + dist (t.points i₁) (t.points i₃) +
                dist (t.points i₂) (t.points i₃)) /
              2 *
            ((dist (t.points i₁) (t.points i₂) + dist (t.points i₁) (t.points i₃) +
                  dist (t.points i₂) (t.points i₃)) /
                2 -
              dist (t.points i₁) (t.points i₂)) *
          ((dist (t.points i₁) (t.points i₂) + dist (t.points i₁) (t.points i₃) +
                dist (t.points i₂) (t.points i₃)) /
              2 -
            dist (t.points i₁) (t.points i₃)) *
        ((dist (t.points i₁) (t.points i₂) + dist (t.points i₁) (t.points i₃) +
              dist (t.points i₂) (t.points i₃)) /
            2 -
          dist (t.points i₂) (t.points i₃)))
```

## Depends on

- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Affine span](../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isometries of a Euclidean affine space](../../undergraduate/affine-and-euclidean-geometry/euclidean-affine-spaces/isometries-of-a-euclidean-affine-space.md)
- [Orthogonal projection](../../overview/analysis/hilbert-spaces/orthogonal-projection.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [The Law of Cosines](../part-04/the-law-of-cosines.md)

## Sources

- [Mathlib documentation: `Affine.Triangle.volume_eq_sqrt_mul_sub_mul_sub_mul_sub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Volume/Triangle.html#Affine.Triangle.volume_eq_sqrt_mul_sub_mul_sub_mul_sub)
- [Source of `Affine.Triangle.volume_eq_sqrt_mul_sub_mul_sub_mul_sub` in Mathlib/Geometry/Euclidean/Volume/Triangle.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Geometry/Euclidean/Volume/Triangle.lean#L73)
- [Freek Wiedijk's 100 theorems, no. 57](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L293)
