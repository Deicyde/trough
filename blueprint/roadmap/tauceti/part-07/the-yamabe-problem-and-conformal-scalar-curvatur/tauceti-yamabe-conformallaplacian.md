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

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian)
- [Source of `TauCeti.Yamabe.conformalLaplacian` in TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean#L89)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
