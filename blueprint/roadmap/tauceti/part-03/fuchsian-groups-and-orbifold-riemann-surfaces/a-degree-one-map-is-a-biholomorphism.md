---
declaration: def
origin: cited
lean: TauCeti.RiemannSurface.biholomorphOfDegreeEqOne
statement: formalized
---

# A degree-one map is a biholomorphism

construct a biholomorphism from a finite holomorphic
map of degree one from a compact Riemann surface to a connected one.

```lean
TauCeti.RiemannSurface.biholomorphOfDegreeEqOne.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  [CompactSpace X] [T2Space X] [T2Space Y] [PreconnectedSpace Y]
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X Y)
  (hf : TauCeti.RiemannSurface.degree ↑f = 1) :
  Diffeomorph (modelWithCornersSelf ℂ ℂ) (modelWithCornersSelf ℂ ℂ) X Y ↑⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.biholomorphOfDegreeEqOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Degree.html#TauCeti.RiemannSurface.biholomorphOfDegreeEqOne).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.biholomorphOfDegreeEqOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Degree.html#TauCeti.RiemannSurface.biholomorphOfDegreeEqOne)
- [Source of `TauCeti.RiemannSurface.biholomorphOfDegreeEqOne` in TauCeti/Analysis/Complex/RiemannSurface/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RiemannSurface/Degree.lean#L475)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
