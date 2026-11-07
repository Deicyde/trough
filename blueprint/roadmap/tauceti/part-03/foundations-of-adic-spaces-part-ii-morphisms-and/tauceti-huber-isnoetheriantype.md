---
declaration: class
origin: cited
lean: TauCeti.Huber.IsNoetherianType
statement: formalized
---

# TauCeti.Huber.IsNoetherianType

A Huber ring is **of noetherian type** if it has a noetherian ring of definition, or if it is
a strongly noetherian Tate ring.

```lean
TauCeti.Huber.IsNoetherianType.{u_1} (A : Type u_1) [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsNoetherianType`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianType/Basic.html#TauCeti.Huber.IsNoetherianType).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsNoetherianType`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianType/Basic.html#TauCeti.Huber.IsNoetherianType)
- [Source of `TauCeti.Huber.IsNoetherianType` in TauCeti/RingTheory/Huber/NoetherianType/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/NoetherianType/Basic.lean#L35)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
