---
declaration: def
origin: cited
lean: SSet.fullEnhancedSubcategory
statement: formalized
---

# SSet.fullEnhancedSubcategory

The full enhanced subcategory of a simplicial set `X` on a predicate `P` on its vertices: the
subcomplex of the simplices all of whose vertices satisfy `P`.

```lean
SSet.fullEnhancedSubcategory.{u} (X : _root_.SSet) (P : X.obj (Opposite.op { len := 0 }) → Prop) :
  X.Subcomplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SSet.fullEnhancedSubcategory`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/FullSubcategory.html#SSet.fullEnhancedSubcategory).

## Sources

- [Tau Ceti documentation: `SSet.fullEnhancedSubcategory`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/FullSubcategory.html#SSet.fullEnhancedSubcategory)
- [Source of `SSet.fullEnhancedSubcategory` in TauCeti/AlgebraicTopology/Quasicategory/FullSubcategory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Quasicategory/FullSubcategory.lean#L51)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
