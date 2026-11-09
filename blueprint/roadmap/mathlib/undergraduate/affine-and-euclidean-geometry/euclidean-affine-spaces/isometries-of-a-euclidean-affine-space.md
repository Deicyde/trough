# Isometries of a Euclidean affine space

An affine isometric equivalence between two normed vector spaces,
denoted `f : P ≃ᵃⁱ[𝕜] P₂`.

```lean
AffineIsometryEquiv.{u_1, u_2, u_4, u_7, u_8} (𝕜 : Type u_1) {V : Type u_2} {V₂ : Type u_4}
  (P : Type u_7) (P₂ : Type u_8) [NormedField 𝕜] [SeminormedAddCommGroup V] [NormedSpace 𝕜 V]
  [PseudoMetricSpace P] [NormedAddTorsor V P] [SeminormedAddCommGroup V₂] [NormedSpace 𝕜 V₂]
  [PseudoMetricSpace P₂] [NormedAddTorsor V₂ P₂] : Type (max (max (max u_2 u_4) u_7) u_8)
```

## Depends on

- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `AffineIsometryEquiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Affine/Isometry.html#AffineIsometryEquiv)
- [Source of `AffineIsometryEquiv` in Mathlib/Analysis/Normed/Affine/Isometry.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Affine/Isometry.lean#L300)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L259)
