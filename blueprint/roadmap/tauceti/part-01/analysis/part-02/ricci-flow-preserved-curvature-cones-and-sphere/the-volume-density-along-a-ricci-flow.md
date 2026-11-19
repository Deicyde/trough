---
declaration: theorem
origin: cited
lean: TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow
statement: formalized
proof: formalized
---

# The volume density along a Ricci flow

If the metrics satisfy the Ricci flow equation
`∂_τ g = -2 Ric(g)` at `x` at `τ = t` within `s`, then in every chart containing `x` the volume
density has derivative `-Scal(g_t)(x) ρ` there; that is, `∂_τ dμ_g = -Scal(g) dμ_g`.

```lean
TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] {s : Set ℝ} {t : ℝ} {x : M} [T2Space M] [IsManifold I (↑⊤) M]
  {g : ℝ → Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x} (α : M)
  (hx : x ∈ (chartAt H α).source)
  (hg :
    ∀ (v w : TangentSpace I x),
      HasDerivWithinAt (fun τ => (((g τ).inner x) v) w)
        (-2 * (((CovariantDerivative.leviCivitaConnection I M).ricciTensor x) v) w) s t) :
  HasDerivWithinAt (fun τ => TauCeti.chartVolumeDensity α x)
    (-(g t).scalarCurvature x * TauCeti.chartVolumeDensity α x) s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula along a curve](jacobis-formula-along-a-curve.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.html#TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow).

## Sources

- [Tau Ceti documentation: `TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.html#TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow)
- [Source of `TauCeti.hasDerivWithinAt_chartVolumeDensity_of_ricciFlow` in TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.lean#L164)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
