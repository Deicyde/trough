---
declaration: theorem
origin: cited
lean: TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale
statement: formalized
proof: formalized
---

# Uniqueness of the hyperbolic metric in a conformal class

On a closed surface two
hyperbolic metrics conformal to the same metric `g` are equal.

```lean
TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T3Space M]
  [PreconnectedSpace M] [CompactSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [I.Boundaryless]
  (hE : Module.finrank ℝ E = 2)
  {g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x}
  (G₁ G₂ : TauCeti.HyperbolicMetric) {f₁ f₂ : M → ℝ}
  {hf₁ : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f₁} {hf₁_pos : ∀ (x : M), 0 < f₁ x}
  {hf₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f₂} {hf₂_pos : ∀ (x : M), 0 < f₂ x}
  (h₁ : G₁.metric = g.rescale f₁ hf₁ hf₁_pos) (h₂ : G₂.metric = g.rescale f₂ hf₂ hf₂_pos) : G₁ = G₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](../../morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)
- [The Koszul formula](../../../part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.html#TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale).

## Sources

- [Tau Ceti documentation: `TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.html#TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale)
- [Source of `TauCeti.HyperbolicMetric.eq_of_metric_eq_rescale` in TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.lean#L103)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
