---
declaration: def
origin: cited
lean: TauCeti.IsSolidTorusNeighborhood.framingNumber
statement: formalized
---

# TauCeti.IsSolidTorusNeighborhood.framingNumber

The **framing number** of the solid torus neighbourhood `Φ`: the longitude of `Φ` is
homologous in the knot complement to `framingNumber` times the meridian. Equivalently, the
longitude of `Φ` is `λ₀ + n · μ` for the preferred longitude `λ₀`
(`TauCeti.IsSolidTorusNeighborhood.preferredFramedBoundaryTorus_basis_one`). For a knot in `S³`
it is the linking number of the longitude of `Φ` with the knot.

```lean
TauCeti.IsSolidTorusNeighborhood.framingNumber {X : Type} [TopologicalSpace X] {f : Circle → X}
  {Φ : TauCeti.SolidTorus → X} [T2Space X]
  (h₁ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor (↧ℤ) 1).obj ↧X))
  (h₂ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor (↧ℤ) 2).obj ↧X))
  (h : TauCeti.IsSolidTorusNeighborhood f Φ) : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSolidTorusNeighborhood.framingNumber`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/SeifertFraming.html#TauCeti.IsSolidTorusNeighborhood.framingNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.IsSolidTorusNeighborhood.framingNumber`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/SeifertFraming.html#TauCeti.IsSolidTorusNeighborhood.framingNumber)
- [Source of `TauCeti.IsSolidTorusNeighborhood.framingNumber` in TauCeti/LowDimTopology/DehnSurgery/SeifertFraming.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LowDimTopology/DehnSurgery/SeifertFraming.lean#L510)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
