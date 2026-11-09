---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient
statement: formalized
proof: formalized
---

# Negative gradient trajectories of a proper Morse function converge

If `f` is a proper
Morse function bounded below, the maximal integral curve of `-grad f` through any point converges
to a critical point of `f`, for any `C¹` Riemannian metric.

```lean
TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I 2 M] [BoundarylessManifold I M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {f : M → ℝ} [I.Boundaryless]
  (hf : TauCeti.IsMorse I f) (hp : IsProperMap f) (hbdd : BddBelow (Set.range f)) (x : M) :
  ∃ p ∈ TauCeti.criticalPoints I f,
    Filter.Tendsto (maximalIntegralCurve (-TauCeti.Manifold.mgradient I f) x) Filter.atTop (nhds p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/GradientFlow.html#TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/GradientFlow.html#TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient)
- [Source of `TauCeti.IsMorse.exists_tendsto_maximalIntegralCurve_neg_mgradient` in TauCeti/Geometry/Manifold/Morse/GradientFlow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/GradientFlow.lean#L295)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
