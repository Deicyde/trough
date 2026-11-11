---
declaration: theorem
origin: cited
lean: TauCeti.mul_measure_le_lintegral_of_forall_exists_ball
statement: formalized
proof: formalized
---

# The Vitali covering estimate, for two measures

If every point of `S` is the centre of a
ball `ball x r` of radius at most `R` such that `t` times the `ν`-measure of the fourfold enlarged
closed ball `closedBall x (4 * r)` is at most `∫⁻ y in ball x r, g y ∂μ`, then
`t * ν S ≤ ∫⁻ g ∂μ`.

Mathlib's `Vitali.exists_disjoint_subfamily_covering_enlargement_closedBall` extracts a pairwise
disjoint subfamily of those balls whose fourfold enlargements still cover `S`, and disjointness
turns the sum of the integrals over the selected balls into a single integral over their union.
With `ν = μ` an additive Haar measure this is `TauCeti.mul_measure_le_of_forall_exists_ball`; a
weight `ν = μ.withDensity w` gives the weighted maximal inequality.

```lean
TauCeti.mul_measure_le_lintegral_of_forall_exists_ball.{u_1} {X : Type u_1} [PseudoMetricSpace X]
  [MeasurableSpace X] [TopologicalSpace.SeparableSpace X] [OpensMeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} {t : ENNReal} {S : Set X} {R : ℝ} {g : X → ENNReal}
  (hS :
    ∀ x ∈ S,
      ∃ r ∈ Set.Ioc 0 R,
        t * ν (Metric.closedBall x (4 * r)) ≤ ∫⁻ (y : X) in Metric.ball x r, g y ∂μ) :
  t * ν S ≤ ∫⁻ (y : X), g y ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_measure_le_lintegral_of_forall_exists_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Vitali.html#TauCeti.mul_measure_le_lintegral_of_forall_exists_ball).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_measure_le_lintegral_of_forall_exists_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Vitali.html#TauCeti.mul_measure_le_lintegral_of_forall_exists_ball)
- [Source of `TauCeti.mul_measure_le_lintegral_of_forall_exists_ball` in TauCeti/MeasureTheory/Covering/Vitali.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Covering/Vitali.lean#L86)
