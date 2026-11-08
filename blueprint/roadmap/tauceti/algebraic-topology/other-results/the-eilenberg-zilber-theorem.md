---
declaration: def
origin: cited
lean: SSet.eilenbergZilberHomotopyEquiv, TopCat.eilenbergZilberHomotopyEquiv
statement: formalized
---

# The Eilenberg–Zilber theorem

the Alexander–Whitney map
`C(K × L; R ⊗ S) ⟶ C(K; R) ⊗ C(L; S)` is a chain homotopy equivalence, with homotopy inverse the
shuffle map.

```lean
SSet.eilenbergZilberHomotopyEquiv.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [∀ (X : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorLeft X)]
  [∀ (X : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorRight X)]
  (K L : _root_.SSet) (R S : C) :
  HomotopyEquiv
    ((CategoryTheory.MonoidalCategoryStruct.tensorObj K L).chainComplex
      (CategoryTheory.MonoidalCategoryStruct.tensorObj R S))
    (CategoryTheory.MonoidalCategoryStruct.tensorObj (K.chainComplex R) (L.chainComplex S))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SSet.eilenbergZilberHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/EilenbergZilber.html#SSet.eilenbergZilberHomotopyEquiv).

## Other forms

**The Eilenberg–Zilber theorem for singular chains.** Formalized in Tau Ceti as [`TopCat.eilenbergZilberHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/EilenbergZilber.html#TopCat.eilenbergZilberHomotopyEquiv).

```lean
TopCat.eilenbergZilberHomotopyEquiv.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.Limits.HasCoproducts C]
  [∀ (T : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorLeft T)]
  [∀ (T : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorRight T)]
  (X Y : TopCat) (R S : C) :
  HomotopyEquiv
    ((TopCat.toSSet.obj (CategoryTheory.MonoidalCategoryStruct.tensorObj X Y)).chainComplex
      (CategoryTheory.MonoidalCategoryStruct.tensorObj R S))
    (CategoryTheory.MonoidalCategoryStruct.tensorObj ((TopCat.toSSet.obj X).chainComplex R)
      ((TopCat.toSSet.obj Y).chainComplex S))
```

## Sources

- [Tau Ceti documentation: `SSet.eilenbergZilberHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/EilenbergZilber.html#SSet.eilenbergZilberHomotopyEquiv)
- [Source of `SSet.eilenbergZilberHomotopyEquiv` in TauCeti/AlgebraicTopology/SimplicialSet/EilenbergZilber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/SimplicialSet/EilenbergZilber.lean#L758)
