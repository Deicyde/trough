---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le, MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le, MeasureTheory.Submartingale.lintegral_iSup_ofReal_rpow_le, MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le_mul_eLpNorm_posPart, MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le_mul_integral_posPart_rpow, MeasureTheory.Martingale.eLpNorm_iSup_eNorm_le, MeasureTheory.Martingale.integral_toReal_iSup_eNorm_rpow_le, MeasureTheory.Martingale.lintegral_iSup_eNorm_rpow_le
statement: formalized
proof: formalized
---

# Doob's continuous-time `Lᵖ` maximal inequality (`eLpNorm` form)

Holds for any real
submartingale `f` and `1 < p < ∞` with no sign or `MemLp` hypothesis, since
`‖(f⁺) T ω‖ ≤ ‖f T ω‖` pointwise.

```lean
MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι] [TopologicalSpace ι]
  [OrderTopology ι] [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} (hf : MeasureTheory.Submartingale f ℱ μ)
  {T : ι} (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t)
  {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (f T) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Doob's `Lᵖ` maximal inequality on a countable set](doobs-lp-maximal-inequality-on-a-countable-set.md)
- [Event-refined positive-part Doob inequality on a finite set](event-refined-positive-part-doob-inequality-on-a.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le).

## Other forms

**Doob's continuous-time `Lᵖ` maximal inequality (Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le).

```lean
MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t)
  (hposT : 0 ≤ᵐ[μ] f T) {p : ℝ} (hp : 1 < p) (hT : MeasureTheory.MemLp (f T) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)).toReal ^ p ∂μ ≤
    (p / (p - 1)) ^ p * ∫ (ω : Ω), f T ω ^ p ∂μ
```

**Doob's continuous-time `Lᵖ` maximal inequality (lower-integral form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.lintegral_iSup_ofReal_rpow_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.lintegral_iSup_ofReal_rpow_le).

```lean
MeasureTheory.Submartingale.lintegral_iSup_ofReal_rpow_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι] [TopologicalSpace ι]
  [OrderTopology ι] [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ} (hf : MeasureTheory.Submartingale f ℱ μ)
  {T : ι} (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t)
  {p : ℝ} (hp : 1 < p) :
  ∫⁻ (ω : Ω), (⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)) ^ p ∂μ ≤
    ENNReal.ofReal (p / (p - 1)) ^ p * ∫⁻ (ω : Ω), ENNReal.ofReal (f T ω) ^ p ∂μ
```

**Doob's continuous-time `Lᵖ` maximal inequality (positive-part `eLpNorm` form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le_mul_eLpNorm_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le_mul_eLpNorm_posPart).

```lean
MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le_mul_eLpNorm_posPart.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) {p : ENNReal}
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (f⁺ T) p μ
```

**Doob's continuous-time `Lᵖ` maximal inequality (positive-part Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le_mul_integral_posPart_rpow`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le_mul_integral_posPart_rpow).

```lean
MeasureTheory.Submartingale.integral_toReal_iSup_ofReal_rpow_le_mul_integral_posPart_rpow.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [LinearOrder ι] [TopologicalSpace ι] [OrderTopology ι] [SecondCountableTopology ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => f u ω) (Set.Ioi t) t) {p : ℝ}
  (hp : 1 < p) (hT : MeasureTheory.MemLp (f⁺ T) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (⨆ t, ⨆ (_ : t ≤ T), ENNReal.ofReal (f t ω)).toReal ^ p ∂μ ≤
    (p / (p - 1)) ^ p * ∫ (ω : Ω), f⁺ T ω ^ p ∂μ
```

**Doob's continuous-time `Lᵖ` maximal inequality for Banach-valued martingales (`eLpNorm` form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.eLpNorm_iSup_eNorm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.eLpNorm_iSup_eNorm_le).

```lean
MeasureTheory.Martingale.eLpNorm_iSup_eNorm_le.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2}
  {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [TopologicalSpace ι] [OrderTopology ι]
  [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι mΩ}
  {M : ι → Ω → E} (hM : MeasureTheory.Martingale M ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => M u ω) (Set.Ioi t) t) {p : ENNReal}
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t, ⨆ (_ : t ≤ T), ‖M t ω‖ₑ) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (M T) p μ
```

**Doob's continuous-time `Lᵖ` maximal inequality for Banach-valued martingales (Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.integral_toReal_iSup_eNorm_rpow_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.integral_toReal_iSup_eNorm_rpow_le).

```lean
MeasureTheory.Martingale.integral_toReal_iSup_eNorm_rpow_le.{u_1, u_2, u_3} {Ω : Type u_1}
  {E : Type u_2} {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [TopologicalSpace ι]
  [OrderTopology ι] [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ι mΩ} {M : ι → Ω → E} (hM : MeasureTheory.Martingale M ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => M u ω) (Set.Ioi t) t) {p : ℝ}
  (hp : 1 < p) (hT : MeasureTheory.MemLp (M T) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (⨆ t, ⨆ (_ : t ≤ T), ‖M t ω‖ₑ).toReal ^ p ∂μ ≤
    (p / (p - 1)) ^ p * ∫ (ω : Ω), ‖M T ω‖ ^ p ∂μ
```

**Doob's continuous-time `Lᵖ` maximal inequality for Banach-valued martingales (lower-integral form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.lintegral_iSup_eNorm_rpow_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.lintegral_iSup_eNorm_rpow_le).

```lean
MeasureTheory.Martingale.lintegral_iSup_eNorm_rpow_le.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2}
  {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [TopologicalSpace ι] [OrderTopology ι]
  [SecondCountableTopology ι] [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι mΩ}
  {M : ι → Ω → E} (hM : MeasureTheory.Martingale M ℱ μ) {T : ι}
  (hcont : ∀ᵐ (ω : Ω) ∂μ, ∀ t < T, ContinuousWithinAt (fun u => M u ω) (Set.Ioi t) t) {p : ℝ}
  (hp : 1 < p) :
  ∫⁻ (ω : Ω), (⨆ t, ⨆ (_ : t ≤ T), ‖M t ω‖ₑ) ^ p ∂μ ≤
    ENNReal.ofReal (p / (p - 1)) ^ p * ∫⁻ (ω : Ω), ‖M T ω‖ₑ ^ p ∂μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le)
- [Source of `MeasureTheory.Submartingale.eLpNorm_iSup_ofReal_le` in TauCeti/Probability/Martingale/MaximalInequality/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Lp.lean#L447)
