---
declaration: theorem
origin: cited
lean: TauCeti.contMDiff_iff_mdifferentiable
statement: formalized
proof: formalized
---

# TauCeti.contMDiff_iff_mdifferentiable

A map between complex manifolds is `C^n`, for any `n ≠ 0`, if and only if it is
holomorphic.

```lean
TauCeti.contMDiff_iff_mdifferentiable.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℂ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] {n : WithTop ℕ∞} {E' : Type u_4} [NormedAddCommGroup E']
  [NormedSpace ℂ E'] [CompleteSpace E'] {H' : Type u_5} [TopologicalSpace H']
  {I' : ModelWithCorners ℂ E' H'} {M' : Type u_6} [TopologicalSpace M'] [ChartedSpace H' M']
  [IsManifold I 1 M] [IsManifold I' 1 M'] {f : M → M'} (hn : n ≠ 0) : ContMDiff I I' n f ↔ MDiff f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.contMDiff_iff_mdifferentiable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#TauCeti.contMDiff_iff_mdifferentiable).

## Sources

- [Tau Ceti documentation: `TauCeti.contMDiff_iff_mdifferentiable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#TauCeti.contMDiff_iff_mdifferentiable)
- [Source of `TauCeti.contMDiff_iff_mdifferentiable` in TauCeti/Geometry/Manifold/Complex/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/Analytic.lean#L172)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
