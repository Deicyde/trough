---
declaration: def
origin: cited
lean: TauCeti.compactlySupportedDeRhamCohomology.integral
statement: formalized
---

# TauCeti.compactlySupportedDeRhamCohomology.integral

Integration `H^n_c(M) → ℝ` over an oriented boundaryless manifold, induced by integrating
compactly supported closed top forms.

```lean
TauCeti.compactlySupportedDeRhamCohomology.integral.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M] {n : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin n)) :
  TauCeti.compactlySupportedDeRhamCohomology I M n →ₗ[ℝ] ℝ
```

## Depends on

- [TauCeti.compactlySupportedDeRhamCohomology](tauceti-compactlysupportedderhamcohomology.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.compactlySupportedDeRhamCohomology.integral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.html#TauCeti.compactlySupportedDeRhamCohomology.integral).

## Sources

- [Tau Ceti documentation: `TauCeti.compactlySupportedDeRhamCohomology.integral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.html#TauCeti.compactlySupportedDeRhamCohomology.integral)
- [Source of `TauCeti.compactlySupportedDeRhamCohomology.integral` in TauCeti/Geometry/Manifold/DeRham/PoincarePairing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.lean#L105)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
