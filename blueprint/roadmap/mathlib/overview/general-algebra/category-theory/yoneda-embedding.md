---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.yoneda
mathlib_file: Mathlib/CategoryTheory/Yoneda.lean
---

# Yoneda embedding

The Yoneda embedding, as a functor from `C` into presheaves on `C`.

```lean
CategoryTheory.yoneda.{v₁, u₁} {C : Type u₁} [CategoryTheory.Category.{v₁, u₁} C] :
  CategoryTheory.Functor C (CategoryTheory.Functor Cᵒᵖ (Type v₁))
```

## Depends on

- [Natural transformation](natural-transformation.md)

## Sources

- [Mathlib documentation: `CategoryTheory.yoneda`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Yoneda.html#CategoryTheory.yoneda)
- [Source of `CategoryTheory.yoneda` in Mathlib/CategoryTheory/Yoneda.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Yoneda.lean#L39)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L7)
