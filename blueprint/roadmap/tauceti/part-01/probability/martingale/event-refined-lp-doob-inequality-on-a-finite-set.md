---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral, MeasureTheory.Martingale.rpow_mul_measure_le_iSup_eNorm_le_setIntegral, MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral_posPart
statement: formalized
proof: formalized
---

# Event-refined `Lᵖ` Doob inequality on a finite set

Requires `0 ≤ᵐ[μ] f T` and `MemLp`
only at the terminal time `T`.

```lean
MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) (ε : NNReal) {F : Finset ι} {T : ι} (hF : ∀ t ∈ F, t ≤ T)
  (hposT : 0 ≤ᵐ[μ] f T) {p : ℝ} (hp : 1 ≤ p) (hT : MeasureTheory.MemLp (f T) (ENNReal.ofReal p) μ) :
  ↑ε ^ p * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ F, ↑ε ≤ f t ω}, f T ω ^ p ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Closed-level event-refined Doob inequality](closed-level-event-refined-doob-inequality.md)
- [Event-refined Doob inequality on a finite set](event-refined-doob-inequality-on-a-finite-set.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral).

## Other forms

**Event-refined `Lᵖ` Doob inequality for Banach-valued martingales (Bochner form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.rpow_mul_measure_le_iSup_eNorm_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.rpow_mul_measure_le_iSup_eNorm_le_setIntegral).

```lean
MeasureTheory.Martingale.rpow_mul_measure_le_iSup_eNorm_le_setIntegral.{u_1, u_2, u_3}
  {Ω : Type u_1} {E : Type u_2} {ι : Type u_3} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [LinearOrder ι] [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι mΩ} {M : ι → Ω → E}
  (hM : MeasureTheory.Martingale M ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => M u ω) (Set.Ioi t) t) (ε : NNReal)
  {p : ℝ} (hp : 1 ≤ p) (hT : MeasureTheory.MemLp (M T) (ENNReal.ofReal p) μ) :
  ↑ε ^ p * μ {ω | ↑ε ≤ ⨆ t, ⨆ (_ : t ≤ T), ‖M t ω‖ₑ} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ↑ε ≤ ⨆ t, ⨆ (_ : t ≤ T), ‖M t ω‖ₑ}, ‖M T ω‖ ^ p ∂μ)
```

**Event-refined `Lᵖ` Doob inequality on a finite set (positive-part Bochner form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral_posPart).

```lean
MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral_posPart.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0}
  {f : ι → Ω → ℝ} (hf : MeasureTheory.Submartingale f ℱ μ) (ε : NNReal) {F : Finset ι} {T : ι}
  (hF : ∀ t ∈ F, t ≤ T) {p : ℝ} (hp : 1 ≤ p)
  (hT : MeasureTheory.MemLp (f⁺ T) (ENNReal.ofReal p) μ) :
  ↑ε ^ p * μ {ω | ∃ t ∈ F, ↑ε ≤ f t ω} ≤
    ENNReal.ofReal (∫ (ω : Ω) in {ω | ∃ t ∈ F, ↑ε ≤ f t ω}, f⁺ T ω ^ p ∂μ)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral)
- [Source of `MeasureTheory.Submartingale.rpow_mul_measure_exists_mem_le_le_setIntegral` in TauCeti/Probability/Martingale/MaximalInequality/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Lp.lean#L150)
