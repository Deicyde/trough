---
declaration: theorem
origin: cited
lean: TauCeti.mayerVietorisShortComplex_shortExact
statement: formalized
proof: formalized
---

# The Mayer–Vietoris short exact sequence of de Rham complexes

On a Hausdorff σ-compact
manifold modelled on a finite-dimensional space, the Mayer–Vietoris short complex of two open
subsets is short exact.

```lean
TauCeti.mayerVietorisShortComplex_shortExact.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  (U V : TopologicalSpace.Opens M) : (TauCeti.mayerVietorisShortComplex I U V).ShortExact
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mayerVietorisShortComplex_shortExact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.html#TauCeti.mayerVietorisShortComplex_shortExact).

## Sources

- [Tau Ceti documentation: `TauCeti.mayerVietorisShortComplex_shortExact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.html#TauCeti.mayerVietorisShortComplex_shortExact)
- [Source of `TauCeti.mayerVietorisShortComplex_shortExact` in TauCeti/Geometry/Manifold/DeRham/MayerVietoris.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.lean#L391)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
