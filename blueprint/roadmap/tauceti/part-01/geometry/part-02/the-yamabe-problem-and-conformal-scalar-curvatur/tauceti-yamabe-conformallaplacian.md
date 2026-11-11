---
declaration: def
origin: cited
lean: TauCeti.Yamabe.conformalLaplacian
statement: formalized
---

# TauCeti.Yamabe.conformalLaplacian

The **conformal Laplacian** `L_g u = aₙ Δ⁺_g u + Scal_g u` of a function `u` on a smooth
Riemannian manifold of dimension `n`, where `aₙ = 4 (n - 1) / (n - 2)`, `Δ⁺_g = -Δ_g` is the
nonnegative Laplacian and `Scal_g` is the scalar curvature.

```lean
TauCeti.Yamabe.conformalLaplacian.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (u : M → ℝ) (x : M) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian)
- [Source of `TauCeti.Yamabe.conformalLaplacian` in TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean#L93)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Yamabe/STATUS.md)
