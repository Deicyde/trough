---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AffineMap
mathlib_file: Mathlib/LinearAlgebra/AffineSpace/AffineMap.lean
---

# Affine function

An `AffineMap k P1 P2` (notation: `P1 →ᵃ[k] P2`) is a map from `P1` to `P2` that
induces a corresponding linear map from `V1` to `V2`.

```lean
AffineMap.{u_1, u_2, u_3, u_4, u_5} (k : Type u_1) {V1 : Type u_2} (P1 : Type u_3) {V2 : Type u_4}
  (P2 : Type u_5) [Ring k] [AddCommGroup V1] [_root_.Module k V1] [AddTorsor V1 P1]
  [AddCommGroup V2] [_root_.Module k V2] [AddTorsor V2 P2] : Type (max (max (max u_2 u_3) u_4) u_5)
```

## Depends on

- [Affine space](affine-space.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `AffineMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/AffineMap.html#AffineMap)
- [Source of `AffineMap` in Mathlib/LinearAlgebra/AffineSpace/AffineMap.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/AffineMap.lean#L54)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L432)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L245)
