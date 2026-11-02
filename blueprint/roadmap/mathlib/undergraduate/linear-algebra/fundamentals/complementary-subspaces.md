---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Submodule.exists_isCompl
mathlib_file: Mathlib/LinearAlgebra/Basis/VectorSpace.lean
---

# Complementary subspaces

Mathlib states this as `Submodule.exists_isCompl`.

```lean
Submodule.exists_isCompl.{u_3, u_4} {K : Type u_3} {V : Type u_4} [DivisionRing K] [AddCommGroup V]
  [_root_.Module K V] (p : Submodule K V) : ∃ q, IsCompl p q
```

## Depends on

- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Sum of subspaces](sum-of-subspaces.md)

## Proof depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Existence of bases](existence-of-bases.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Kernel of a linear map](kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Submodule.exists_isCompl`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis/VectorSpace.html#Submodule.exists_isCompl)
- [Source of `Submodule.exists_isCompl` in Mathlib/LinearAlgebra/Basis/VectorSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Basis/VectorSpace.lean#L280)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L13)
