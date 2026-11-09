---
declaration: def
origin: cited
lean: TauCeti.FormalCoordinate.jetLimitEquiv
statement: formalized
---

# TauCeti.FormalCoordinate.jetLimitEquiv

The formal coordinates are the inverse limit of their jet groups: passing to all jets is an
isomorphism of topological groups onto the compatible families of jets.

```lean
TauCeti.FormalCoordinate.jetLimitEquiv.{u_1} (R : Type u_1) [CommRing R] :
  TauCeti.FormalCoordinate R ≃ₜ* ↥(TauCeti.FormalCoordinate.jetLimit R)
```

## Depends on

- [TauCeti.FormalCoordinate](tauceti-formalcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalCoordinate.jetLimitEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Coordinate/Jet.html#TauCeti.FormalCoordinate.jetLimitEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalCoordinate.jetLimitEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Coordinate/Jet.html#TauCeti.FormalCoordinate.jetLimitEquiv)
- [Source of `TauCeti.FormalCoordinate.jetLimitEquiv` in TauCeti/RingTheory/PowerSeries/Coordinate/Jet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Coordinate/Jet.lean#L373)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
