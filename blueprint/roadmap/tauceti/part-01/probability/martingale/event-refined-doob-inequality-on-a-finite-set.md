---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral, MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral, MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_of_countable
statement: formalized
proof: formalized
---

# Event-refined Doob inequality on a finite set

The terminal expectation is restricted
to the same crossing event, even when the terminal time does not belong to the sampled set.

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f) (ε : NNReal) {F : Finset ι} {T : ι}
  (hF : ∀ t ∈ F, t ≤ T) :
  ↑ε * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ F, ↑ε ≤ f t ω}, f T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral).

## Other forms

**Event-refined Doob inequality in continuous time.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral).

```lean
MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [TopologicalSpace ι] [OrderTopology ι]
  [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ∃ t ≤ T, ↑ε < f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ≤ T, ↑ε < f t ω}, f T ω ∂μ)
```

**Event-refined Doob inequality on a countable set.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_of_countable`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_of_countable).

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_of_countable.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  [MeasureTheory.IsFiniteMeasure μ] (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f)
  (ε : NNReal) {S : Set ι} (hS : S.Countable) {T : ι} (hST : ∀ t ∈ S, t ≤ T) :
  ↑ε * μ {ω | ∃ t ∈ S, ↑ε ≤ f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ S, ↑ε ≤ f t ω}, f T ω ∂μ)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral)
- [Source of `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral` in TauCeti/Probability/Martingale/MaximalInequality/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/MaximalInequality/Basic.lean#L79)
