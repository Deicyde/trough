---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_exists_le_lt_le, MeasureTheory.Submartingale.mul_measure_exists_mem_le_le
statement: formalized
proof: formalized
---

# Doob's maximal inequality in continuous time

Let `f` be a nonnegative submartingale
indexed by a second countable time set, such as `ℝ≥0`, whose paths are almost surely
right-continuous at every time before `T`. Then `ε P(∃ t ≤ T, ε < f_t) ≤ E[f_T]`.

```lean
MeasureTheory.Submartingale.mul_measure_exists_le_lt_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [TopologicalSpace ι] [OrderTopology ι]
  [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ∃ t ≤ T, ↑ε < f t ω} ≤ ENNReal.ofReal (∫ (ω : Ω), f T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Event-refined Doob inequality on a finite set](event-refined-doob-inequality-on-a-finite-set.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_le_lt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_le_lt_le).

## Other forms

**Doob's maximal inequality over a finite set of times.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_le_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le).

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_le_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) (hnonneg : 0 ≤ f) (ε : NNReal) {F : Finset ι} {T : ι}
  (hF : ∀ t ∈ F, t ≤ T) : ↑ε * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤ ENNReal.ofReal (∫ (ω : Ω), f T ω ∂μ)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_exists_le_lt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_le_lt_le)
- [Source of `MeasureTheory.Submartingale.mul_measure_exists_le_lt_le` in TauCeti/Probability/Martingale/MaximalInequality/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/MaximalInequality/Basic.lean#L223)
