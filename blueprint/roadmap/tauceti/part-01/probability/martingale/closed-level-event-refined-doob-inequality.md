---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral
statement: formalized
proof: formalized
---

# Closed-level event-refined Doob inequality

The running supremum is taken in `ℝ≥0∞`,
so no pathwise boundedness assumption or convention for an unattained real supremum is needed.
The terminal expectation retains exactly the event that this supremum is at least `ε`.

```lean
MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [MeasureTheory.IsFiniteMeasure μ]
  [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ↑ε ≤ ⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ↑ε ≤ ⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)}, f T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Event-refined Doob inequality on a finite set](event-refined-doob-inequality-on-a-finite-set.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Event.html#MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Event.html#MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral)
- [Source of `MeasureTheory.Submartingale.mul_measure_le_iSup_le_setIntegral` in TauCeti/Probability/Martingale/MaximalInequality/Event.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/MaximalInequality/Event.lean#L44)
