---
declaration: theorem
origin: cited
lean: TauCeti.centralUnitIso_associativity_iff
statement: formalized
proof: formalized
---

# TauCeti.centralUnitIso\_associativity\_iff

The associativity condition of a pseudofunctor out of `LocallyDiscrete (SingleObj G)` with
identity `1`-cells and central compositors `centralUnitIso C (c (h, g))` at `g ≫ h = h * g`,
evaluated at `(g, h, j)`, is the `2`-cocycle identity
`c (j * h, g) * c (j, h) = c (h, g) * c (j, h * g)` of `c` at `(j, h, g)`.

```lean
TauCeti.centralUnitIso_associativity_iff.{w, v, u} {G : Type u} [Monoid G] (C : Type w)
  [CategoryTheory.Category.{v, w} C] (c : G × G → (CategoryTheory.CatCenter C)ˣ) (g h j : G) :
  CategoryTheory.CategoryStruct.comp (TauCeti.centralUnitIso C (c (j, h * g))).hom
        (CategoryTheory.CategoryStruct.comp
          (CategoryTheory.Bicategory.whiskerRight (TauCeti.centralUnitIso C (c (h, g))).hom
            (CategoryTheory.CategoryStruct.id ↧C))
          (CategoryTheory.CategoryStruct.comp
            (CategoryTheory.Bicategory.associator (CategoryTheory.CategoryStruct.id ↧C)
                (CategoryTheory.CategoryStruct.id ↧C) (CategoryTheory.CategoryStruct.id ↧C)).hom
            (CategoryTheory.CategoryStruct.comp
              (CategoryTheory.Bicategory.whiskerLeft (CategoryTheory.CategoryStruct.id ↧C)
                (TauCeti.centralUnitIso C (c (j, h))).inv)
              (TauCeti.centralUnitIso C (c (j * h, g))).inv))) =
      CategoryTheory.CategoryStruct.id (CategoryTheory.CategoryStruct.id ↧C) ↔
    c (j * h, g) * c (j, h) = c (h, g) * c (j, h * g)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.centralUnitIso_associativity_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.html#TauCeti.centralUnitIso_associativity_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.centralUnitIso_associativity_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.html#TauCeti.centralUnitIso_associativity_iff)
- [Source of `TauCeti.centralUnitIso_associativity_iff` in TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.lean#L141)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
