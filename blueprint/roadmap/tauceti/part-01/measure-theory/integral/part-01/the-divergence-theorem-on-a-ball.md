---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_ball_trace_fderiv
statement: formalized
proof: formalized
---

# The divergence theorem on a ball

Let `V : E → E` be `C¹` near the closed ball of radius
`R ≥ 0` about `c`. The integral of its divergence `tr (DV)` over the open ball is the flux of `V`
through the boundary sphere: with the unit sphere `S` and its surface measure `μ.toSphere`,

`∫_{ball c R} tr (DV) dμ = R ^ (n - 1) ∫_{θ ∈ S} ⟪V (c + R θ), θ⟫ dμ.toSphere`,

where `n` is the dimension of `E`.

```lean
TauCeti.setIntegral_ball_trace_fderiv.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] (c : E) {R : ℝ} (hR : 0 ≤ R) {V : E → E}
  (hV : ∀ x ∈ Metric.closedBall c R, ContDiffAt ℝ 1 V x) :
  ∫ (x : E) in Metric.ball c R, (LinearMap.trace ℝ E) ↑(fderiv ℝ V x) ∂μ =
    R ^ (Module.finrank ℝ E - 1) *
      ∫ (θ : ↑(Metric.sphere 0 1)), inner ℝ (V (c + R • ↑θ)) ↑θ ∂μ.toSphere
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../../analysis/part-04/sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_ball_trace_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Ball.html#TauCeti.setIntegral_ball_trace_fderiv).

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_ball_trace_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Ball.html#TauCeti.setIntegral_ball_trace_fderiv)
- [Source of `TauCeti.setIntegral_ball_trace_fderiv` in TauCeti/MeasureTheory/Integral/DivergenceTheorem/Ball.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Ball.lean#L187)
