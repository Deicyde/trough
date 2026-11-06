# Affine subspace

An `AffineSubspace k P` is a subset of an `AffineSpace V P` that, if not empty, has an affine
space structure induced by a corresponding subspace of the `Module k V`.

```lean
AffineSubspace.{u_1, u_2, u_3} (k : Type u_1) {V : Type u_2} (P : Type u_3) [Ring k]
  [AddCommGroup V] [_root_.Module k V] [AddTorsor V P] : Type u_3
```

## Depends on

- [Affine space](affine-space.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Ring](../../general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `AffineSubspace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.html#AffineSubspace)
- [Source of `AffineSubspace` in Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Defs.lean#L151)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L433)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L246)
