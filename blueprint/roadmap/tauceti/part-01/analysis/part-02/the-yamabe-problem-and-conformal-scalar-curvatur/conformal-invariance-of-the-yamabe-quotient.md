---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale
statement: formalized
proof: formalized
---

# Conformal invariance of the Yamabe quotient

In dimension `n ≠ 2`, let `u` be a positive
function such that `ĝ = u ^ (4 / (n - 2)) g` is a smooth metric on a manifold without boundary.
Then `Q_ĝ(v) = Q_g(u v)` for every compactly supported `C²` function `v`.

```lean
Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [SigmaCompactSpace M] [IsManifold I (↑⊤) M]
  [MeasurableSpace M] [BorelSpace M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hn : Module.finrank ℝ E ≠ 2) {u : M → ℝ} (hu_pos : ∀ (x : M), 0 < u x)
  {hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) ↑⊤ fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))}
  {hf_pos : ∀ (x : M), 0 < u x ^ (4 / (↑(Module.finrank ℝ E) - 2))} {v : M → ℝ}
  (hv : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 v) (hvc : HasCompactSupport v) :
  TauCeti.Yamabe.yamabeQuotient I v = TauCeti.Yamabe.yamabeQuotient I (u * v)
```

## Depends on

- [TauCeti.Yamabe.yamabeQuotient](tauceti-yamabe-yamabequotient.md)

## Proof depends on

- [The conformal Laplacian of a conformal metric](the-conformal-laplacian-of-a-conformal-metric.md)
- [Green's first identity on a manifold without boundary](../../../geometry/part-02/manifold/part-02/greens-first-identity-on-a-manifold-without-boun.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)
- [Lusin–Souslin theorem in charts](../../../geometry/part-02/manifold/part-03/lusin-souslin-theorem-in-charts.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalInvariance.html#Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/ConformalInvariance.html#Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale)
- [Source of `Bundle.ContMDiffRiemannianMetric.yamabeQuotient_rescale` in TauCeti/Analysis/PDE/Yamabe/ConformalInvariance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Yamabe/ConformalInvariance.lean#L111)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
