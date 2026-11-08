---
declaration: theorem
origin: cited
lean: TauCeti.centralUnitIso_naturality_comp_iff
statement: formalized
proof: formalized
---

# TauCeti.centralUnitIso_naturality_comp_iff

The composition condition of a strong transformation with identity components and
naturality `2`-cells `centralUnitIso C (b g)`, between pseudofunctors with identity `1`-cells
and central compositors `centralUnitIso C (c (h, g))` and `centralUnitIso C (c' (h, g))` at
`g ≫ h = h * g`, evaluated at `(g, h)`, states that `c'` is `c` multiplied by the coboundary of
`b` at `(h, g)`.

```lean
TauCeti.centralUnitIso_naturality_comp_iff.{w, v, u} {G : Type u} [Monoid G] (C : Type w)
  [CategoryTheory.Category.{v, w} C] (b : G → (CategoryTheory.CatCenter C)ˣ)
  (c c' : G × G → (CategoryTheory.CatCenter C)ˣ) (g h : G) :
  CategoryTheory.CategoryStruct.comp (TauCeti.centralUnitIso C (b (h * g))).hom
        (CategoryTheory.Bicategory.whiskerLeft (CategoryTheory.CategoryStruct.id ↧C)
          (TauCeti.centralUnitIso C (c' (h, g))).hom) =
      CategoryTheory.CategoryStruct.comp
        (CategoryTheory.Bicategory.whiskerRight (TauCeti.centralUnitIso C (c (h, g))).hom
          (CategoryTheory.CategoryStruct.id ↧C))
        (CategoryTheory.CategoryStruct.comp
          (CategoryTheory.Bicategory.associator (CategoryTheory.CategoryStruct.id ↧C)
              (CategoryTheory.CategoryStruct.id ↧C) (CategoryTheory.CategoryStruct.id ↧C)).hom
          (CategoryTheory.CategoryStruct.comp
            (CategoryTheory.Bicategory.whiskerLeft (CategoryTheory.CategoryStruct.id ↧C)
              (TauCeti.centralUnitIso C (b h)).hom)
            (CategoryTheory.CategoryStruct.comp
              (CategoryTheory.Bicategory.associator (CategoryTheory.CategoryStruct.id ↧C)
                  (CategoryTheory.CategoryStruct.id ↧C) (CategoryTheory.CategoryStruct.id ↧C)).inv
              (CategoryTheory.CategoryStruct.comp
                (CategoryTheory.Bicategory.whiskerRight (TauCeti.centralUnitIso C (b g)).hom
                  (CategoryTheory.CategoryStruct.id ↧C))
                (CategoryTheory.Bicategory.associator (CategoryTheory.CategoryStruct.id ↧C)
                    (CategoryTheory.CategoryStruct.id ↧C)
                    (CategoryTheory.CategoryStruct.id ↧C)).hom)))) ↔
    c' (h, g) = b h * b g / b (h * g) * c (h, g)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.centralUnitIso_naturality_comp_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.html#TauCeti.centralUnitIso_naturality_comp_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.centralUnitIso_naturality_comp_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.html#TauCeti.centralUnitIso_naturality_comp_iff)
- [Source of `TauCeti.centralUnitIso_naturality_comp_iff` in TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Bicategory/Functor/CentralCocycle.lean#L246)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
