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

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints)
- [Source of `TauCeti.AdicSpace.isAdic_iff_mapsTo_analyticPoints` in TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean#L182)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
