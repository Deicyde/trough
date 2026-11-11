---
declaration: theorem
origin: cited
lean: MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le
statement: formalized
proof: formalized
---

# Doob's weak maximal inequality for the norm of a martingale

A terminal L¹
bound controls the outer probability of a uniform path error.

```lean
MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le.{u_1, u_2, u_3} {Ω : Type u_1}
  {E : Type u_2} {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [TopologicalSpace ι]
  [OrderTopology ι] [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ι mΩ} {M : ι → Ω → E} (hM : MeasureTheory.Martingale M ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => M u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ∃ t ≤ T, ↑ε < ‖M t ω‖} ≤ ENNReal.ofReal (∫ (ω : Ω), ‖M T ω‖ ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Doob's maximal inequality in continuous time](doobs-maximal-inequality-in-continuous-time.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le)
- [Source of `MeasureTheory.Martingale.mul_measure_exists_le_norm_lt_le` in TauCeti/Probability/Martingale/MaximalInequality/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/MaximalInequality/Basic.lean#L315)
