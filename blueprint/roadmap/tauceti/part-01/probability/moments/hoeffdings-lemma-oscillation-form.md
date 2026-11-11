---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le
statement: formalized
proof: formalized
---

# Hoeffding's lemma, oscillation form

If an almost everywhere measurable real function on a
probability space has oscillation at most `C`, then its centered exponential moment is at most
`exp ((C / 2) ^ 2 * t ^ 2 / 2)`.

```lean
MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le.{u_2} {β : Type u_2}
  [MeasurableSpace β] (ν : MeasureTheory.Measure β) [MeasureTheory.IsProbabilityMeasure ν]
  {X : β → ℝ} (hX : AEMeasurable X ν) {C : ℝ} (hosc : ∀ (a a' : β), |X a - X a'| ≤ C) (t : ℝ) :
  ∫ (a : β), Real.exp (t * (X a - ∫ (a' : β), X a' ∂ν)) ∂ν ≤ Real.exp ((C / 2) ^ 2 * t ^ 2 / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Azuma.html#MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Azuma.html#MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le)
- [Source of `MeasureTheory.Measure.integral_exp_mul_sub_integral_le_of_abs_sub_le` in TauCeti/Probability/Moments/Azuma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/Azuma.lean#L62)
