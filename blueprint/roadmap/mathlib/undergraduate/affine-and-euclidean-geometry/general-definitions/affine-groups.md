# Affine groups

Mathlib states this as `AffineEquiv.group`.

```lean
AffineEquiv.group.{u_1, u_2, u_6} {k : Type u_1} {P₁ : Type u_2} {V₁ : Type u_6} [Ring k]
  [AddCommGroup V₁] [_root_.Module k V₁] [AddTorsor V₁ P₁] : Group (P₁ ≃ᵃ[k] P₁)
```

## Depends on

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `AffineEquiv.group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.html#AffineEquiv.group)
- [Source of `AffineEquiv.group` in Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean#L325)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L250)
