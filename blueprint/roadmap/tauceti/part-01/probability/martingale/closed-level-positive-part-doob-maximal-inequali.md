---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart
statement: formalized
proof: formalized
---

# Closed-level positive-part Doob maximal inequality (`ε P(sup_{t ≤ T} f_t ≥ ε) ≤ E[(f_T)⁺]`)

Holds for every real submartingale `f` with right-continuous paths before `T` and `ε : ℝ≥0`.

```lean
MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [MeasureTheory.IsFiniteMeasure μ]
  [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ↑ε ≤ ⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)} ≤
    ENNReal.ofReal (∫ (ω : Ω), f⁺ T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Closed-level event-refined Doob inequality](closed-level-event-refined-doob-inequality.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Event.html#MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Event.html#MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart)
- [Source of `MeasureTheory.Submartingale.mul_measure_le_iSup_le_integral_posPart` in TauCeti/Probability/Martingale/MaximalInequality/Event.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Event.lean#L123)
