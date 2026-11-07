---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq
statement: formalized
proof: formalized
---

# The Yamabe equation

In dimension `n ≠ 2`, let `u` be a positive function such that
`ĝ = u ^ (4 / (n - 2)) g` is a smooth metric. Then `ĝ` has scalar curvature `c` at a point exactly
when `u` solves the Yamabe equation `L_g u = c u ^ (pₙ - 1)` there, where `pₙ = 2 n / (n - 2)`.

```lean
TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hn : Module.finrank ℝ E ≠ 2) {u : M → ℝ} (hu_pos : ∀ (x : M), 0 < u x)
  {hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) ↑⊤ fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))}
  {hf_pos : ∀ (x : M), 0 < u x ^ (4 / (↑(Module.finrank ℝ E) - 2))} (c : ℝ) (x : M) :
  (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos).scalarCurvature x = c ↔
    TauCeti.Yamabe.conformalLaplacian I u x =
      c * u x ^ (TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E) - 1)
```

## Depends on

- [TauCeti.Yamabe.conformalLaplacian](tauceti-yamabe-conformallaplacian.md)

## Proof depends on

- [Scalar curvature of a conformal metric](scalar-curvature-of-a-conformal-metric.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq)
- [Source of `TauCeti.Yamabe.scalarCurvature_rescale_eq_iff_conformalLaplacian_eq` in TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean#L237)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
