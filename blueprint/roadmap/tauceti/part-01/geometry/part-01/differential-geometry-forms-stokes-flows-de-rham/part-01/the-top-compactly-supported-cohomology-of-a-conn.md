---
declaration: def
origin: cited
lean: TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv
statement: formalized
---

# The top compactly supported cohomology of a connected manifold

integration as a linear
isomorphism `H^n_c(M) ≃ₗ[ℝ] ℝ`, for a connected, oriented, boundaryless, Hausdorff, σ-compact
finite-dimensional smooth manifold.

```lean
TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M] {n : ℕ}
  [ConnectedSpace M] (o : TauCeti.Manifold.Orientation I M (Fin n)) :
  TauCeti.compactlySupportedDeRhamCohomology I M n ≃ₗ[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The compactly supported Poincaré lemma on the line](../../../part-02/manifold/part-01/the-compactly-supported-poincare-lemma-on-the-li.md)
- [The Poincaré lemma on manifolds](../../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Integration/Bijective.html#TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Integration/Bijective.html#TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv)
- [Source of `TauCeti.compactlySupportedDeRhamCohomologyIntegralEquiv` in TauCeti/Geometry/Manifold/DeRham/Integration/Bijective.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/Integration/Bijective.lean#L106)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
