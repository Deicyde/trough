---
declaration: def
origin: cited
lean: TauCeti.SmoothForm.hodgeStar
statement: formalized
---

# TauCeti.SmoothForm.hodgeStar

The Hodge star of smooth real `k`-forms on an oriented manifold of dimension `m = k + l`
with a smooth Riemannian metric.

```lean
TauCeti.SmoothForm.hodgeStar.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] {m k l : ℕ} [IsManifold I (↑⊤) M]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + l = m) :
  TauCeti.SmoothForm I M ℝ k →ₗ[ℝ] TauCeti.SmoothForm I M ℝ l
```

## Depends on

- [Orientation.hodgeStar](../../../analysis/part-01/four-dimensional-seiberg-witten-theory/orientation-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.hodgeStar`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/HodgeStar.html#TauCeti.SmoothForm.hodgeStar).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.hodgeStar`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/HodgeStar.html#TauCeti.SmoothForm.hodgeStar)
- [Source of `TauCeti.SmoothForm.hodgeStar` in TauCeti/Geometry/Manifold/Riemannian/HodgeStar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/HodgeStar.lean#L350)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
