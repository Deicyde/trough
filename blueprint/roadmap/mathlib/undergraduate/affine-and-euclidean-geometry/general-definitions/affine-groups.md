---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: AffineEquiv.group
mathlib_file: Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean
---

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
- [Source of `AffineEquiv.group` in Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean#L325)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L250)
