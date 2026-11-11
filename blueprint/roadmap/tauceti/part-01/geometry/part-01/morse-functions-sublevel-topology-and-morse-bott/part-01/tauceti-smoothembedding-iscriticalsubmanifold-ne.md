---
declaration: def
origin: cited
lean: TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace
statement: formalized
---

# TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace

The **negative normal space** of a critical submanifold at `s`, relative to a fibre metric
`g` on the normal spaces: the span of the normal vectors `v` with `Hess v = μ g v` for some
`μ < 0`, where `Hess` is the normal Hessian.

```lean
TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type u_4} {H' : Type u_5} {S : Type u_6} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} [TopologicalSpace S] [ChartedSpace H' S]
  {f : M → ℝ} {n : WithTop ℕ∞} {i : TauCeti.SmoothEmbedding J I n S M} (hn : n ≠ 0) [I.Boundaryless]
  [IsManifold I 2 M] (h : i.IsCriticalSubmanifold f)
  (g : Bundle.RiemannianMetric fun s => i.NormalSpace s hn) (s : S) :
  Submodule ℝ (i.NormalSpace s hn)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Splitting.html#TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Splitting.html#TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace)
- [Source of `TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace` in TauCeti/Geometry/Manifold/Morse/Bott/Splitting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Bott/Splitting.lean#L82)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
