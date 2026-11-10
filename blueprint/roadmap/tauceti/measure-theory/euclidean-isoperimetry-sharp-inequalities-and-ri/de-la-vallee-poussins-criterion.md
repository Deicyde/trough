---
declaration: theorem
origin: cited
lean: TauCeti.unifIntegrable_of_lintegral_ofReal_le, TauCeti.exists_setLIntegral_enorm_le_mul_add
statement: formalized
proof: formalized
---

# De la Vallée Poussin's criterion

A family of a.e. strongly measurable functions with
`∫ Φ(‖f i‖) ≤ C < ∞` for a superlinear `Φ` is uniformly integrable.

```lean
TauCeti.unifIntegrable_of_lintegral_ofReal_le.{u_1, u_2, u_3} {α : Type u_1} {F : Type u_2}
  {ι : Type u_3} [MeasurableSpace α] [NormedAddCommGroup F] {μ : MeasureTheory.Measure α}
  {Φ : ℝ → ℝ} (hΦ : Filter.Tendsto (fun t => Φ t / t) Filter.atTop Filter.atTop) {f : ι → α → F}
  (hfm : ∀ (i : ι), MeasureTheory.AEStronglyMeasurable (f i) μ) {C : ENNReal} (hC : C ≠ ⊤)
  (hf : ∀ (i : ι), ∫⁻ (a : α), ENNReal.ofReal (Φ ‖f i a‖) ∂μ ≤ C) :
  MeasureTheory.UnifIntegrable f 1 μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.unifIntegrable_of_lintegral_ofReal_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DeLaValleePoussin.html#TauCeti.unifIntegrable_of_lintegral_ofReal_le).

## Other forms

**De la Vallée Poussin's criterion, quantitative form.** Formalized in Tau Ceti as [`TauCeti.exists_setLIntegral_enorm_le_mul_add`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DeLaValleePoussin.html#TauCeti.exists_setLIntegral_enorm_le_mul_add).

```lean
TauCeti.exists_setLIntegral_enorm_le_mul_add.{u_1, u_2, u_3} {α : Type u_1} {F : Type u_2}
  {ι : Type u_3} [MeasurableSpace α] [NormedAddCommGroup F] {μ : MeasureTheory.Measure α}
  {Φ : ℝ → ℝ} (hΦ : Filter.Tendsto (fun t => Φ t / t) Filter.atTop Filter.atTop) {f : ι → α → F}
  {C : ENNReal} (hC : C ≠ ⊤) (hf : ∀ (i : ι), ∫⁻ (a : α), ENNReal.ofReal (Φ ‖f i a‖) ∂μ ≤ C)
  {ε : ENNReal} (hε : ε ≠ 0) :
  ∃ T, ∀ (i : ι) (s : Set α), ∫⁻ (a : α) in s, ‖f i a‖ₑ ∂μ ≤ ↑T * μ s + ε
```

## Sources

- [Tau Ceti documentation: `TauCeti.unifIntegrable_of_lintegral_ofReal_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DeLaValleePoussin.html#TauCeti.unifIntegrable_of_lintegral_ofReal_le)
- [Source of `TauCeti.unifIntegrable_of_lintegral_ofReal_le` in TauCeti/MeasureTheory/Function/DeLaValleePoussin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/DeLaValleePoussin.lean#L196)
