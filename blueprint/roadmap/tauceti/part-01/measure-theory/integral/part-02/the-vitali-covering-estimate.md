---
declaration: theorem
origin: cited
lean: TauCeti.mul_measure_le_of_forall_exists_ball
statement: formalized
proof: formalized
---

# The Vitali covering estimate

If every point of `S` is the centre of a ball of radius at
most `R` on which `∫⁻ g` is at least `t` times the measure of the ball, then
`t * μ S ≤ 4 ^ n * ∫⁻ g`, with `n` the dimension of the space.

The factor `4 ^ n` is the cost of passing from a pairwise disjoint subfamily of those balls to its
fourfold enlargement, which still covers `S`.

```lean
TauCeti.mul_measure_le_of_forall_exists_ball.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {t : ENNReal} {S : Set E} {R : ℝ}
  {g : E → ENNReal}
  (hS :
    ∀ x ∈ S, ∃ r ∈ Set.Ioc 0 R, t * μ (Metric.ball x r) ≤ ∫⁻ (y : E) in Metric.ball x r, g y ∂μ) :
  t * μ S ≤ 4 ^ Module.finrank ℝ E * ∫⁻ (y : E), g y ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_measure_le_of_forall_exists_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.mul_measure_le_of_forall_exists_ball).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_measure_le_of_forall_exists_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.mul_measure_le_of_forall_exists_ball)
- [Source of `TauCeti.mul_measure_le_of_forall_exists_ball` in TauCeti/MeasureTheory/Integral/MaximalFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/MaximalFunction.lean#L333)
