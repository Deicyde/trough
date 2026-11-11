---
declaration: abbrev
origin: cited
lean: TauCeti.SmoothMappingTorus
statement: formalized
---

# TauCeti.SmoothMappingTorus

The smooth mapping torus `(ℝ × M) / ((t, x) ∼ (t + 1, φ⁻¹ x))` of a `C^n` diffeomorphism `φ`:
the orbit space of the action of `Multiplicative ℤ` on `ℝ × M` by
`k • (t, x) = (t + k, φ ^ (-k) x)`. It is a `C^n` manifold modelled on `𝓘(ℝ).prod I` when `M` is
a locally compact Hausdorff `C^n` manifold.

```lean
TauCeti.SmoothMappingTorus.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] {n : WithTop ℕ∞} (φ : Diffeomorph I I M M n) : Type u_3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothMappingTorus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/MappingTorus.html#TauCeti.SmoothMappingTorus).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothMappingTorus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/MappingTorus.html#TauCeti.SmoothMappingTorus)
- [Source of `TauCeti.SmoothMappingTorus` in TauCeti/Geometry/Manifold/Instances/MappingTorus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Instances/MappingTorus.lean#L265)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
