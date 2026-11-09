---
declaration: def
origin: cited
lean: TauCeti.poincarePairing
statement: formalized
---

# TauCeti.poincarePairing

The Poincaré pairing `H^k_dR(M) → H^l_c(M) → ℝ` on an oriented boundaryless manifold of
dimension `k + l`, sending classes `[φ]` and `[ψ]` to `∫_M φ ∧ ψ`. It is the wedge product
`H^k_dR(M) → H^l_c(M) → H^(k+l)_c(M)` followed by integration.

```lean
TauCeti.poincarePairing.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H)
  (M : Type u_3) [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M] {k l : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin (k + l))) :
  TauCeti.deRhamCohomology I M k →ₗ[ℝ] TauCeti.compactlySupportedDeRhamCohomology I M l →ₗ[ℝ] ℝ
```

## Depends on

- [TauCeti.compactlySupportedDeRhamCohomology](tauceti-compactlysupportedderhamcohomology.md)
- [TauCeti.compactlySupportedDeRhamCohomology.integral](tauceti-compactlysupportedderhamcohomology-integ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.poincarePairing`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.html#TauCeti.poincarePairing).

## Sources

- [Tau Ceti documentation: `TauCeti.poincarePairing`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.html#TauCeti.poincarePairing)
- [Source of `TauCeti.poincarePairing` in TauCeti/Geometry/Manifold/DeRham/PoincarePairing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/PoincarePairing.lean#L164)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
