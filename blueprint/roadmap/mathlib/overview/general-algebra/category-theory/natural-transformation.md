---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.NatTrans
mathlib_file: Mathlib/CategoryTheory/NatTrans.lean
---

# Natural transformation

`NatTrans F G` represents a natural transformation between functors `F` and `G`.

The field `app` provides the components of the natural transformation.

Naturality is expressed by `α.naturality`.

```lean
CategoryTheory.NatTrans.{v₁, v₂, u₁, u₂} {C : Type u₁} [CategoryTheory.Category.{v₁, u₁} C]
  {D : Type u₂} [CategoryTheory.Category.{v₂, u₂} D] (F G : CategoryTheory.Functor C D) :
  Type (max u₁ v₂)
```

## Depends on

- [Functor](functor.md)

## Sources

- [Mathlib documentation: `CategoryTheory.NatTrans`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/NatTrans.html#CategoryTheory.NatTrans)
- [Source of `CategoryTheory.NatTrans` in Mathlib/CategoryTheory/NatTrans.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/NatTrans.lean#L47)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L6)
