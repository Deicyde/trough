---
declaration: instance
origin: cited
lean: TauCeti.SmoothForm.instModule
statement: formalized
---

# TauCeti.SmoothForm.instModule

Scalars acting on the coefficients act on smooth forms, making them a module. For complex
coefficients this is the complex vector space of complex-valued smooth forms.

```lean
TauCeti.SmoothForm.instModule.{u_1, u_2, u_3, u_7, u_10} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_7} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  [TopologicalSpace M] [ChartedSpace H M] {I : ModelWithCorners ℝ E H} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {k : ℕ} [IsManifold I 1 M] {S : Type u_10} [Semiring S] [_root_.Module S F]
  [ContinuousConstSMul S F] [SMulCommClass ℝ S F] : _root_.Module S (TauCeti.SmoothForm I M F k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.instModule`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/MapCoeff.html#TauCeti.SmoothForm.instModule).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.instModule`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/MapCoeff.html#TauCeti.SmoothForm.instModule)
- [Source of `TauCeti.SmoothForm.instModule` in TauCeti/Geometry/Manifold/DifferentialForm/MapCoeff.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/MapCoeff.lean#L271)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
