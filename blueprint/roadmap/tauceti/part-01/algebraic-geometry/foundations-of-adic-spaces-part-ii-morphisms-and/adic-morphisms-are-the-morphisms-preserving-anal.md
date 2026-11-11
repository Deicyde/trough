---
declaration: theorem
origin: cited
lean: TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints
statement: formalized
proof: formalized
---

# Adic morphisms are the morphisms preserving analytic points

**Adic morphisms are the morphisms preserving analytic points** (Huber 1994, Proposition
3.2(ii); Wedhorn, Proposition 8.39): a morphism of adic spaces is adic exactly when it sends
analytic points to analytic points.

```lean
TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints.{u} {X Y : TauCeti.AdicSpace} (f : X ⟶ Y) :
  TauCeti.AdicSpace.IsAdic f ↔
    Set.MapsTo (⇑(CategoryTheory.ConcreteCategory.hom f.hom.base)) X.obj.analyticPoints
      Y.obj.analyticPoints
```

## Depends on

- [Adic morphisms (Huber 1994, §3)](adic-morphisms-huber-1994-3.md)
- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)
- [Analytic points of a pre-adic space (Wedhorn, Proposition and Definition 8.36)](../../ring-theory/part-01/analytic-adic-geometry-for-diamonds/analytic-points-of-a-pre-adic-space-wedhorn-prop.md)

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints)
- [Source of `TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints` in TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean#L182)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
