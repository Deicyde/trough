---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian
statement: formalized
proof: formalized
---

# Scalar curvature of a conformal metric

In dimension `n ≠ 2`, let `u` be a positive
function such that `ĝ = u ^ (4 / (n - 2)) g` is a smooth metric. Then the scalar curvature of `ĝ`
is `Scal_ĝ = u ^ (-(n + 2) / (n - 2)) L_g u`, where `L_g` is the conformal Laplacian of `g`.
Such a `u` is automatically smooth.

```lean
TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hn : Module.finrank ℝ E ≠ 2) {u : M → ℝ} (hu_pos : ∀ (x : M), 0 < u x)
  {hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) ↑⊤ fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))}
  {hf_pos : ∀ (x : M), 0 < u x ^ (4 / (↑(Module.finrank ℝ E) - 2))} (x : M) :
  (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos).scalarCurvature x =
    u x ^ (-(↑(Module.finrank ℝ E) + 2) / (↑(Module.finrank ℝ E) - 2)) *
      TauCeti.Yamabe.conformalLaplacian I u x
```

## Depends on

- [TauCeti.Yamabe.conformalLaplacian](tauceti-yamabe-conformallaplacian.md)

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian)
- [Source of `TauCeti.Yamabe.scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian` in TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean#L200)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Yamabe/STATUS.md)
