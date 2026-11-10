---
declaration: theorem
origin: cited
lean: CategoryTheory.isIso_id_sub_comp_comm
statement: formalized
proof: formalized
---

# Jacobson's lemma

`𝟙 X - a ≫ b` is invertible exactly when `𝟙 Y - b ≫ a` is.

```lean
CategoryTheory.isIso_id_sub_comp_comm.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] {X Y : C} (a : X ⟶ Y) (b : Y ⟶ X) :
  CategoryTheory.IsIso
      (CategoryTheory.CategoryStruct.id X - CategoryTheory.CategoryStruct.comp a b) ↔
    CategoryTheory.IsIso
      (CategoryTheory.CategoryStruct.id Y - CategoryTheory.CategoryStruct.comp b a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.isIso_id_sub_comp_comm`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Jacobson.html#CategoryTheory.isIso_id_sub_comp_comm).

## Sources

- [Tau Ceti documentation: `CategoryTheory.isIso_id_sub_comp_comm`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Jacobson.html#CategoryTheory.isIso_id_sub_comp_comm)
- [Source of `CategoryTheory.isIso_id_sub_comp_comm` in TauCeti/CategoryTheory/Preadditive/Jacobson.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Preadditive/Jacobson.lean#L55)
