---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: affineSpan
mathlib_file: Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.lean
---

# Affine span

The affine span of a set of points is the smallest affine subspace containing those points.
(Actually defined here in terms of spans in modules.)

```lean
affineSpan.{u_1, u_2, u_3} (k : Type u_1) {V : Type u_2} {P : Type u_3} [Ring k] [AddCommGroup V]
  [_root_.Module k V] [AddTorsor V P] (s : Set P) : AffineSubspace k P
```

## Depends on

- [Affine subspace](affine-subspace.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)

## Sources

- [Mathlib documentation: `affineSpan`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.html#affineSpan)
- [Source of `affineSpan` in Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.lean#L535)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L435)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L248)
