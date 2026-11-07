---
declaration: theorem
origin: cited
lean: TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact
statement: formalized
proof: formalized
---

# The compactly supported Mayer–Vietoris short exact sequence

On a Hausdorff σ-compact
manifold modelled on a finite-dimensional space, the compactly supported Mayer–Vietoris short
complex of two open subsets is short exact.

```lean
TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I 2 M] [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [SigmaCompactSpace M]
  (U V : TopologicalSpace.Opens M) :
  (TauCeti.compactlySupportedMayerVietorisShortComplex I U V).ShortExact
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/CompactlySupportedMayerVietoris.html#TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact).

## Sources

- [Tau Ceti documentation: `TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/CompactlySupportedMayerVietoris.html#TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact)
- [Source of `TauCeti.compactlySupportedMayerVietorisShortComplex_shortExact` in TauCeti/Geometry/Manifold/DeRham/CompactlySupportedMayerVietoris.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/CompactlySupportedMayerVietoris.lean#L198)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
