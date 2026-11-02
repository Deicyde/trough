---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Monad
mathlib_file: Mathlib/CategoryTheory/Monad/Basic.lean
---

# Monad

The data of a monad on C consists of an endofunctor T together with natural transformations
`η : 𝟭 C ⟶ T` and `μ : T ⋙ T ⟶ T` satisfying three equations:
- `T μ_X ≫ μ_X = μ_(TX) ≫ μ_X` (associativity)
- `η_(TX) ≫ μ_X = 1_X` (left unit)
- `Tη_X ≫ μ_X = 1_X` (right unit)

```lean
CategoryTheory.Monad.{v₁, u₁} (C : Type u₁) [CategoryTheory.Category.{v₁, u₁} C] : Type (max u₁ v₁)
```

## Depends on

- [Natural transformation](natural-transformation.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Monad`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Monad/Basic.html#CategoryTheory.Monad)
- [Source of `CategoryTheory.Monad` in Mathlib/CategoryTheory/Monad/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Monad/Basic.lean#L33)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L10)
