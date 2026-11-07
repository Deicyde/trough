---
declaration: theorem
origin: cited
lean: TauCeti.contDiffGroupoid_eq_of_ne_zero
statement: formalized
proof: formalized
---

# TauCeti.contDiffGroupoid\_eq\_of\_ne\_zero

For a boundaryless model on a finite-dimensional complex space, the `C^m` and `C^n` groupoids
agree whenever `m` and `n` are nonzero.

```lean
TauCeti.contDiffGroupoid_eq_of_ne_zero.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℂ E H} [I.Boundaryless] {m n : WithTop ℕ∞} (hm : m ≠ 0) (hn : n ≠ 0) :
  contDiffGroupoid m I = contDiffGroupoid n I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.contDiffGroupoid_eq_of_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#TauCeti.contDiffGroupoid_eq_of_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.contDiffGroupoid_eq_of_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Analytic.html#TauCeti.contDiffGroupoid_eq_of_ne_zero)
- [Source of `TauCeti.contDiffGroupoid_eq_of_ne_zero` in TauCeti/Geometry/Manifold/Complex/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/Analytic.lean#L86)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
