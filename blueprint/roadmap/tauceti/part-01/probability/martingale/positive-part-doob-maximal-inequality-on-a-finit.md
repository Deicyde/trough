---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart, MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_integral_posPart
statement: formalized
proof: formalized
---

# Positive-part Doob maximal inequality on a finite set

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) (ε : NNReal) {F : Finset ι} {T : ι}
  (hF : ∀ t ∈ F, t ≤ T) : ↑ε * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤ ENNReal.ofReal (∫ (ω : Ω), f⁺ T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Event-refined positive-part Doob inequality on a finite set](event-refined-positive-part-doob-inequality-on-a.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart).

## Other forms

**Positive-part Doob maximal inequality for strict crossings in continuous time.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_integral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_integral_posPart).

```lean
MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_integral_posPart.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [TopologicalSpace ι] [OrderTopology ι]
  [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ∃ t ≤ T, ↑ε < f t ω} ≤ ENNReal.ofReal (∫ (ω : Ω), f⁺ T ω ∂μ)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart)
- [Source of `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_integral_posPart` in TauCeti/Probability/Martingale/MaximalInequality/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Basic.lean#L226)
