---
declaration: def
origin: cited
lean: TauCeti.CoveringSpace.monodromyEquivalence
statement: formalized
---

# The classification of covering spaces by fundamental-groupoid actions

Over a
path-connected, locally path-connected, semilocally simply connected base, monodromy is an
equivalence from covering spaces to functors from the fundamental groupoid to types.

```lean
TauCeti.CoveringSpace.monodromyEquivalence.{u} (X : TopCat) [PathConnectedSpace ↑X]
  [LocallyPathConnectedSpace ↑X] [TauCeti.SemilocallySimplyConnectedSpace ↑X] :
  TauCeti.CoveringSpace X ≌ CategoryTheory.Functor (FundamentalGroupoid ↑X) (Type u)
```

## Depends on

- [TauCeti.CoveringSpace](tauceti-coveringspace.md)

## Proof depends on

- [TauCeti.CoveringSpace.mk](tauceti-coveringspace-mk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CoveringSpace.monodromyEquivalence`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/MonodromyEquivalence.html#TauCeti.CoveringSpace.monodromyEquivalence).

## Sources

- [Tau Ceti documentation: `TauCeti.CoveringSpace.monodromyEquivalence`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/MonodromyEquivalence.html#TauCeti.CoveringSpace.monodromyEquivalence)
- [Source of `TauCeti.CoveringSpace.monodromyEquivalence` in TauCeti/AlgebraicTopology/UniversalCover/Classification/MonodromyEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/UniversalCover/Classification/MonodromyEquivalence.lean#L202)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
