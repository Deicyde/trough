---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.conformalLaplacian_rescale
statement: formalized
proof: formalized
---

# The conformal Laplacian of a conformal metric

In dimension `n ≠ 2`, let `u` be a
positive function such that `ĝ = u ^ (4 / (n - 2)) g` is a smooth metric. Then the conformal
Laplacians of `ĝ` and `g` are related by `L_ĝ v = u ^ (-(n + 2) / (n - 2)) L_g (u v)` for every
`C²` function `v`. For `v = 1` this is the scalar curvature law
`scalarCurvature_rescale_eq_rpow_mul_conformalLaplacian`.

```lean
TauCeti.Yamabe.conformalLaplacian_rescale.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hn : Module.finrank ℝ E ≠ 2) {u : M → ℝ} (hu_pos : ∀ (x : M), 0 < u x)
  {hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) ↑⊤ fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))}
  {hf_pos : ∀ (x : M), 0 < u x ^ (4 / (↑(Module.finrank ℝ E) - 2))} {v : M → ℝ}
  (hv : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 v) (x : M) :
  TauCeti.Yamabe.conformalLaplacian I v x =
    u x ^ (-(↑(Module.finrank ℝ E) + 2) / (↑(Module.finrank ℝ E) - 2)) *
      TauCeti.Yamabe.conformalLaplacian I (u * v) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)
- [Scalar curvature of a conformal metric](scalar-curvature-of-a-conformal-metric.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.conformalLaplacian_rescale`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian_rescale).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.conformalLaplacian_rescale`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.html#TauCeti.Yamabe.conformalLaplacian_rescale)
- [Source of `TauCeti.Yamabe.conformalLaplacian_rescale` in TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Yamabe/ConformalLaplacian.lean#L262)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
