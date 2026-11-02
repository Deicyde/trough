---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Iso
mathlib_file: Mathlib/CategoryTheory/Iso.lean
---

# Isomorphism

An isomorphism (a.k.a. an invertible morphism) between two objects of a category.
The inverse morphism is bundled.

See also `CategoryTheory.Core` for the category with the same objects and isomorphisms playing
the role of morphisms.

```lean
CategoryTheory.Iso.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C] (X Y : C) : Type v
```

## Depends on

- [Category](category.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Iso`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Iso.html#CategoryTheory.Iso)
- [Source of `CategoryTheory.Iso` in Mathlib/CategoryTheory/Iso.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Iso.lean#L48)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L8)
