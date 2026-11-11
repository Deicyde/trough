---
declaration: def
origin: cited
lean: TopCat.eilenbergZilberHomotopyEquiv
statement: formalized
---

# The Eilenberg–Zilber theorem for singular chains

the Alexander–Whitney map
`C(X × Y; R ⊗ S) ⟶ C(X; R) ⊗ C(Y; S)` is a chain homotopy equivalence, with homotopy inverse the
shuffle map.

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

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.eilenbergZilberHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/EilenbergZilber.html#TopCat.eilenbergZilberHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TopCat.eilenbergZilberHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/EilenbergZilber.html#TopCat.eilenbergZilberHomotopyEquiv)
- [Source of `TopCat.eilenbergZilberHomotopyEquiv` in TauCeti/AlgebraicTopology/Singular/EilenbergZilber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/EilenbergZilber.lean#L74)
