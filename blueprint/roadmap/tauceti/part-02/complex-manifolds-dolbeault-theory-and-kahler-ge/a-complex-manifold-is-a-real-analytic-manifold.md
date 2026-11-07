---
declaration: theorem
origin: cited
lean: IsManifold.restrictScalars_of_ne_zero
statement: formalized
proof: formalized
---

# A complex manifold is a real-analytic manifold

A complex manifold modelled on
`𝓘(ℂ, E)`, of class `C^m` for some `m ≠ 0` with `E` finite-dimensional, is with the same charts a
real `C^n` manifold modelled on `𝓘(ℝ, E)` for every `n`; for `n = ω` it is real-analytic.

```lean
IsManifold.restrictScalars_of_ne_zero.{u_1, u_4} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {m : WithTop ℕ∞} (n : WithTop ℕ∞) {M : Type u_4}
  [TopologicalSpace M] [ChartedSpace E M] (hm : m ≠ 0)
  (h : IsManifold (modelWithCornersSelf ℂ E) m M) : IsManifold (modelWithCornersSelf ℝ E) n M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsManifold.restrictScalars_of_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#IsManifold.restrictScalars_of_ne_zero).

## Sources

- [Tau Ceti documentation: `IsManifold.restrictScalars_of_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#IsManifold.restrictScalars_of_ne_zero)
- [Source of `IsManifold.restrictScalars_of_ne_zero` in TauCeti/Geometry/Manifold/Complex/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/Analytic.lean#L112)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
