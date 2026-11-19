---
declaration: theorem
origin: cited
lean: TauCeti.hasDerivAt_chartVolumeDensity
statement: formalized
proof: formalized
---

# The variation of the volume density

If the metrics `g_τ` have parameter derivative `h`
at `x` at `τ = t`, then in every chart containing `x` the volume density `ρ_τ = √(det G_τ)` has
derivative `½ tr_g(h) ρ` at `t`, with the trace and the density computed for `g_t`.

```lean
TauCeti.hasDerivAt_chartVolumeDensity.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {t : ℝ}
  {x : M} [IsManifold I 1 M] {g : ℝ → Bundle.RiemannianMetric fun x => TangentSpace I x} (α : M)
  (hx : x ∈ (chartAt H α).source) {h : LinearMap.BilinForm ℝ (TangentSpace I x)}
  (hg : ∀ (v w : TangentSpace I x), HasDerivAt (fun τ => (((g τ).inner x) v) w) ((h v) w) t) :
  HasDerivAt (fun τ => TauCeti.chartVolumeDensity α x)
    (2⁻¹ * TauCeti.bilinFormTrace h * TauCeti.chartVolumeDensity α x) t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula along a curve](jacobis-formula-along-a-curve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasDerivAt_chartVolumeDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.html#TauCeti.hasDerivAt_chartVolumeDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.hasDerivAt_chartVolumeDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.html#TauCeti.hasDerivAt_chartVolumeDensity)
- [Source of `TauCeti.hasDerivAt_chartVolumeDensity` in TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/Variation.lean#L124)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
