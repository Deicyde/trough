---
declaration: theorem
origin: cited
lean: CategoryTheory.SimplicialObject.alexanderWhitney_coassoc
statement: formalized
proof: formalized
---

# Coassociativity of the Alexander–Whitney map

the two ways of splitting a simplex into
a front, a middle and a back face agree, up to the associators of simplicial objects and of
chain complexes.

```lean
CategoryTheory.SimplicialObject.alexanderWhitney_coassoc.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.Limits.HasFiniteCoproducts C] (A B D : CategoryTheory.SimplicialObject C) :
  CategoryTheory.CategoryStruct.comp
      ((CategoryTheory.MonoidalCategoryStruct.tensorObj A B).alexanderWhitney D)
      (CategoryTheory.CategoryStruct.comp
        (CategoryTheory.MonoidalCategoryStruct.whiskerRight (A.alexanderWhitney B)
          ((AlgebraicTopology.alternatingFaceMapComplex C).obj D))
        (CategoryTheory.MonoidalCategoryStruct.associator
            ((AlgebraicTopology.alternatingFaceMapComplex C).obj A)
            ((AlgebraicTopology.alternatingFaceMapComplex C).obj B)
            ((AlgebraicTopology.alternatingFaceMapComplex C).obj D)).hom) =
    CategoryTheory.CategoryStruct.comp
      ((AlgebraicTopology.alternatingFaceMapComplex C).map
        (CategoryTheory.MonoidalCategoryStruct.associator A B D).hom)
      (CategoryTheory.CategoryStruct.comp
        (A.alexanderWhitney (CategoryTheory.MonoidalCategoryStruct.tensorObj B D))
        (CategoryTheory.MonoidalCategoryStruct.whiskerLeft
          ((AlgebraicTopology.alternatingFaceMapComplex C).obj A) (B.alexanderWhitney D)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.SimplicialObject.alexanderWhitney_coassoc`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialObject/AlexanderWhitney.html#CategoryTheory.SimplicialObject.alexanderWhitney_coassoc).

## Sources

- [Tau Ceti documentation: `CategoryTheory.SimplicialObject.alexanderWhitney_coassoc`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialObject/AlexanderWhitney.html#CategoryTheory.SimplicialObject.alexanderWhitney_coassoc)
- [Source of `CategoryTheory.SimplicialObject.alexanderWhitney_coassoc` in TauCeti/AlgebraicTopology/SimplicialObject/AlexanderWhitney.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/SimplicialObject/AlexanderWhitney.lean#L309)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
