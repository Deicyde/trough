# Heron’s Formula

**Heron's formula**: The area of a triangle with side lengths `a`, `b`, and `c` is
`√(s * (s - a) * (s - b) * (s - c))` where `s = (a + b + c) / 2` is the semiperimeter.
We show this by equating this formula to `a * b * sin γ`, where `γ` is the angle opposite
the side `c`.

```lean
Theorems100.heron.{u_1, u_2} {V : Type u_1} {P : Type u_2} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P] {p₁ p₂ p₃ : P} (h1 : p₁ ≠ p₂)
  (h2 : p₃ ≠ p₂) :
  have a := dist p₁ p₂;
  have b := dist p₃ p₂;
  have c := dist p₁ p₃;
  have s := (a + b + c) / 2;
  1 / 2 * a * b * Real.sin (EuclideanGeometry.angle p₁ p₂ p₃) = √(s * (s - a) * (s - b) * (s - c))
```

## Depends on

- [Angle](../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [The Law of Cosines](../part-04/the-law-of-cosines.md)

## Sources

- [Mathlib documentation: `Theorems100.heron`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/HeronsFormula.html#Theorems100.heron)
- [Source of `Theorems100.heron` in Archive/Wiedijk100Theorems/HeronsFormula.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Archive/Wiedijk100Theorems/HeronsFormula.lean#L29)
- [Freek Wiedijk's 100 theorems, no. 57](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L293)
