---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add, TauCeti.SeibergWitten.measure_closedBall_le_mul_deriv_add
statement: formalized
proof: formalized
---

# Taubes's monotonicity inequality in a flat chart

Let `J` be an orthogonal complex
structure with unitary frame `e` (`J e₀ = e₁`, `J e₂ = e₃`), let `F` be a two-form field that is
`C¹` at the points of the closed ball `closedBall c σ` and closed on the open ball, and let `δ` be
continuous on the closed ball. Suppose that `δ` is
bounded by the Kähler component of `F` on the ball, `δ ≤ F(e₀, e₁) + F(e₂, e₃) + K`, and that the
Hermitian part of `F` is bounded by `δ` on the boundary sphere,
`F(v, J v) ≤ ((1 + κ) δ + K) ‖v‖²`. Then

`∫_{B_σ} δ ≤ (σ / 2) (1 + κ) σ³ ∫_S δ (c + σ θ) dθ + K (|S| / 2 + |B₁|) σ⁴`,

where `S` is the unit sphere with its surface measure `μ.toSphere` and `B₁` the unit ball.

```lean
TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {e : OrthonormalBasis (Fin 4) ℝ E} {c : E}
  {F : E → E [⋀^Fin 2]→L[ℝ] ℝ} [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {J : TauCeti.AlmostComplexStructure E}
  (h₀ : J.toLinearMap (e 0) = e 1) (h₂ : J.toLinearMap (e 2) = e 3) {δ : E → ℝ} {σ κ K : ℝ}
  (hσ : 0 ≤ σ) (hF : ∀ x ∈ Metric.closedBall c σ, ContDiffAt ℝ 1 F x)
  (hdF : ∀ x ∈ Metric.ball c σ, extDeriv F x = 0) (hδ : ContinuousOn δ (Metric.closedBall c σ))
  (hω : ∀ x ∈ Metric.ball c σ, δ x ≤ (F x) ![e 0, e 1] + (F x) ![e 2, e 3] + K)
  (hB :
    ∀ x ∈ Metric.sphere c σ,
      ∀ (v : E), (F x) ![v, J.toLinearMap v] ≤ ((1 + κ) * δ x + K) * ‖v‖ ^ 2) :
  ∫ (x : E) in Metric.ball c σ, δ x ∂μ ≤
    σ / 2 * (1 + κ) * (σ ^ 3 * ∫ (θ : ↑(Metric.sphere 0 1)), δ (c + σ • ↑θ) ∂μ.toSphere) +
      K * (μ.toSphere.real Set.univ / 2 + μ.real (Metric.ball 0 1)) * σ ^ 4
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The divergence theorem on a ball](../../../../measure-theory/integral/part-01/the-divergence-theorem-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ZeroSet/Monotonicity.html#TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add).

## Other forms

**Taubes's monotonicity inequality for the defect measure.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.measure_closedBall_le_mul_deriv_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ZeroSet/Monotonicity.html#TauCeti.SeibergWitten.measure_closedBall_le_mul_deriv_add).

```lean
TauCeti.SeibergWitten.measure_closedBall_le_mul_deriv_add.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {e : OrthonormalBasis (Fin 4) ℝ E} {c : E}
  {F : E → E [⋀^Fin 2]→L[ℝ] ℝ} [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {J : TauCeti.AlmostComplexStructure E}
  (h₀ : J.toLinearMap (e 0) = e 1) (h₂ : J.toLinearMap (e 2) = e 3) {δ : E → ℝ} {R κ K σ : ℝ}
  (hF : ∀ x ∈ Metric.ball c R, ContDiffAt ℝ 1 F x) (hdF : ∀ x ∈ Metric.ball c R, extDeriv F x = 0)
  (hδ : ContinuousOn δ (Metric.ball c R)) (hδ₀ : ∀ x ∈ Metric.ball c R, 0 ≤ δ x)
  (hω : ∀ x ∈ Metric.ball c R, δ x ≤ (F x) ![e 0, e 1] + (F x) ![e 2, e 3] + K)
  (hB :
    ∀ x ∈ Metric.ball c R, ∀ (v : E), (F x) ![v, J.toLinearMap v] ≤ ((1 + κ) * δ x + K) * ‖v‖ ^ 2)
  (hσ : σ ∈ Set.Ioo 0 R) :
  ((μ.withDensity fun x => ENNReal.ofReal (δ x)) (Metric.closedBall c σ)).toReal ≤
    σ / 2 * (1 + κ) *
        deriv
          (fun s => ((μ.withDensity fun x => ENNReal.ofReal (δ x)) (Metric.closedBall c s)).toReal)
          σ +
      K * (μ.toSphere.real Set.univ / 2 + μ.real (Metric.ball 0 1)) * σ ^ 4
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ZeroSet/Monotonicity.html#TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add)
- [Source of `TauCeti.SeibergWitten.setIntegral_ball_le_mul_integral_toSphere_add` in TauCeti/Analysis/PDE/SeibergWitten/ZeroSet/Monotonicity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/ZeroSet/Monotonicity.lean#L260)
