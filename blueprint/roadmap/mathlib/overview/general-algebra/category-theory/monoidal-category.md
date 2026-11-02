---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.MonoidalCategory
mathlib_file: Mathlib/CategoryTheory/Monoidal/Category.lean
---

# Monoidal category

In a monoidal category, we can take the tensor product of objects, `X ⊗ Y` and of morphisms
`f ⊗ₘ g`.
Tensor product does not need to be strictly associative on objects, but there is a
specified associator, `α_ X Y Z : (X ⊗ Y) ⊗ Z ≅ X ⊗ (Y ⊗ Z)`. There is a tensor unit `𝟙_ C`,
with specified left and right unitor isomorphisms `λ_ X : 𝟙_ C ⊗ X ≅ X` and `ρ_ X : X ⊗ 𝟙_ C ≅ X`.
These associators and unitors satisfy the pentagon and triangle equations.

```lean
CategoryTheory.MonoidalCategory.{v, u} (C : Type u) [𝒞 : CategoryTheory.Category.{v, u} C] :
  Type (max u v)
```

## Depends on

- [Isomorphism](isomorphism.md)

## Sources

- [Mathlib documentation: `CategoryTheory.MonoidalCategory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Monoidal/Category.html#CategoryTheory.MonoidalCategory)
- [Source of `CategoryTheory.MonoidalCategory` in Mathlib/CategoryTheory/Monoidal/Category.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Monoidal/Category.lean#L152)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L15)
