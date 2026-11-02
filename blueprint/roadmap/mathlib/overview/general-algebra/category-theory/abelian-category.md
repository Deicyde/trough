---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Abelian
mathlib_file: Mathlib/CategoryTheory/Abelian/Basic.lean
---

# Abelian category

A (preadditive) category `C` is called abelian if it has all finite products,
all kernels and cokernels, and if every monomorphism is the kernel of some morphism
and every epimorphism is the cokernel of some morphism.

(This definition implies the existence of zero objects:
finite products give a terminal object, and in a preadditive category
any terminal object is a zero object.)

```lean
CategoryTheory.Abelian.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C] : Type (max u v)
```

## Depends on

- [Integer](../numbers/integer.md)
- [Limits](limits.md)
- [Small category](small-category.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Abelian`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Abelian/Basic.html#CategoryTheory.Abelian)
- [Source of `CategoryTheory.Abelian` in Mathlib/CategoryTheory/Abelian/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Abelian/Basic.lean#L102)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L17)
