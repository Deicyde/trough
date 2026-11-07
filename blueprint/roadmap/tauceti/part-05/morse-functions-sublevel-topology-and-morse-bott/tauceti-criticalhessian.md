---
declaration: def
origin: cited
lean: TauCeti.criticalHessian
statement: formalized
---

# TauCeti.criticalHessian

The **critical Hessian** of a real function `f` at a point `x` of a manifold: the second
derivative at `extChartAt I x x` of the coordinate expression of `f` in the preferred extended
chart, as a bilinear form on the tangent space at `x`.

Like `TauCeti.manifoldMorseIndex`, the definition makes sense at every point and carries no
regularity hypotheses. At a critical point of a `C²` function on a manifold without boundary it is
intrinsic: `TauCeti.criticalHessian_apply_eq_of_mem_maximalAtlas` computes it in an arbitrary chart
there. At a noncritical point it depends on the preferred chart, and on a manifold with boundary
or corners it may also depend on the chart inverse outside `range I`.

```lean
TauCeti.criticalHessian.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] [TopologicalSpace M]
  [ChartedSpace H M] (I : ModelWithCorners ℝ E H) (f : M → ℝ) (x : M) :
  TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.criticalHessian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Hessian.html#TauCeti.criticalHessian).

## Sources

- [Tau Ceti documentation: `TauCeti.criticalHessian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Hessian.html#TauCeti.criticalHessian)
- [Source of `TauCeti.criticalHessian` in TauCeti/Geometry/Manifold/Morse/Hessian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Hessian.lean#L92)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
