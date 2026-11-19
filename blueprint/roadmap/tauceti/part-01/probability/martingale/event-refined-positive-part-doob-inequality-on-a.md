---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart, MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral_posPart, MeasureTheory.Submartingale.mul_measure_exists_mem_lt_le_setIntegral_posPart_of_countable
statement: formalized
proof: formalized
---

# Event-refined positive-part Doob inequality on a finite set

No sign assumption on `f` or
positivity side condition on `ε` is needed.

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  [MeasureTheory.IsFiniteMeasure μ] (hf : MeasureTheory.Submartingale f ℱ μ) (ε : NNReal)
  {F : Finset ι} {T : ι} (hF : ∀ t ∈ F, t ≤ T) :
  ↑ε * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ F, ↑ε ≤ f t ω}, f⁺ T ω ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Event-refined Doob inequality on a finite set](event-refined-doob-inequality-on-a-finite-set.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart).

## Other forms

**Event-refined positive-part Doob inequality for strict crossings in continuous time.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral_posPart).

```lean
MeasureTheory.Submartingale.mul_measure_exists_le_lt_le_setIntegral_posPart.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} [TopologicalSpace ι]
  [OrderTopology ι] [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) (ε : NNReal) :
  ↑ε * μ {ω | ∃ t ≤ T, ↑ε < f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ≤ T, ↑ε < f t ω}, f⁺ T ω ∂μ)
```

**Event-refined positive-part Doob inequality for strict crossings on a countable set.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.mul_measure_exists_mem_lt_le_setIntegral_posPart_of_countable`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_lt_le_setIntegral_posPart_of_countable).

```lean
MeasureTheory.Submartingale.mul_measure_exists_mem_lt_le_setIntegral_posPart_of_countable.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  [MeasureTheory.IsFiniteMeasure μ] (hf : MeasureTheory.Submartingale f ℱ μ) (ε : NNReal)
  {S : Set ι} (hS : S.Countable) {T : ι} (hST : ∀ t ∈ S, t ≤ T) :
  ↑ε * μ {ω | ∃ t ∈ S, ↑ε < f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ S, ↑ε < f t ω}, f⁺ T ω ∂μ)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Basic.html#MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart)
- [Source of `MeasureTheory.Submartingale.mul_measure_exists_mem_le_le_setIntegral_posPart` in TauCeti/Probability/Martingale/MaximalInequality/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Basic.lean#L209)
