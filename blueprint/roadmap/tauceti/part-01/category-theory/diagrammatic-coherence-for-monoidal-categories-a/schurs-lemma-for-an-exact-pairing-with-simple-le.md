---
declaration: theorem
origin: cited
lean: TauCeti.isIso_comp_evaluation_of_simple_left, TauCeti.isIso_comp_evaluation_of_simple_right
statement: formalized
proof: formalized
---

# Schur's lemma for an exact pairing with simple left member

if `X` is simple with
finite-dimensional endomorphisms, every nonzero `η : 𝟙_ C ⟶ Y ⊗ X` closes up with the evaluation
of an exact pairing of `X` and `Y` to an invertible scalar.

```lean
TauCeti.isIso_comp_evaluation_of_simple_left.{v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.MonoidalCategory C] (k : Type u_1) [Field k]
  [IsAlgClosed k] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)] {X Y : C}
  [CategoryTheory.ExactPairing X Y] [CategoryTheory.Simple X] [FiniteDimensional k (X ⟶ X)]
  {η :
    CategoryTheory.MonoidalCategoryStruct.tensorUnit C ⟶
      CategoryTheory.MonoidalCategoryStruct.tensorObj Y X}
  (hη : η ≠ 0) : CategoryTheory.IsIso (CategoryTheory.CategoryStruct.comp η (ε_ X Y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_comp_evaluation_of_simple_left`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Simple.html#TauCeti.isIso_comp_evaluation_of_simple_left).

## Other forms

**Schur's lemma for an exact pairing with simple right member.** Formalized in Tau Ceti as [`TauCeti.isIso_comp_evaluation_of_simple_right`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Simple.html#TauCeti.isIso_comp_evaluation_of_simple_right).

```lean
TauCeti.isIso_comp_evaluation_of_simple_right.{v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.MonoidalCategory C] (k : Type u_1) [Field k]
  [IsAlgClosed k] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)] {X Y : C}
  [CategoryTheory.ExactPairing X Y] [CategoryTheory.Simple Y] [FiniteDimensional k (Y ⟶ Y)]
  {η :
    CategoryTheory.MonoidalCategoryStruct.tensorUnit C ⟶
      CategoryTheory.MonoidalCategoryStruct.tensorObj Y X}
  (hη : η ≠ 0) : CategoryTheory.IsIso (CategoryTheory.CategoryStruct.comp η (ε_ X Y))
```

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_comp_evaluation_of_simple_left`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Simple.html#TauCeti.isIso_comp_evaluation_of_simple_left)
- [Source of `TauCeti.isIso_comp_evaluation_of_simple_left` in TauCeti/CategoryTheory/Monoidal/Rigid/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Rigid/Simple.lean#L153)
