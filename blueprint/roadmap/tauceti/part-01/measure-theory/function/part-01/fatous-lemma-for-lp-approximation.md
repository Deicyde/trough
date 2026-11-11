---
declaration: theorem
origin: cited
lean: TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le, TauCeti.eLpNorm_ennreal_le_of_ae_tendsto
statement: formalized
proof: formalized
---

# Fatou's lemma for `Lᵖ` approximation

If `g n → g₀` almost everywhere and the `Lᵖ`
seminorms of `g n` are bounded by a sequence tending to `0`, then `g₀ = 0` almost everywhere.

```lean
TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le.{u_1, u_3} {α : Type u_1} {E : Type u_3}
  [MeasurableSpace α] {μ : MeasureTheory.Measure α} {p : ENNReal} [NormedAddCommGroup E]
  {g : ℕ → α → E} {g₀ : α → E} {c : ℕ → ENNReal} (hp : p ≠ 0)
  (hg : ∀ (n : ℕ), MeasureTheory.AEStronglyMeasurable (g n) μ)
  (hg₀ : MeasureTheory.AEStronglyMeasurable g₀ μ)
  (hlim : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun n => g n x) Filter.atTop (nhds (g₀ x)))
  (hgc : ∀ (n : ℕ), MeasureTheory.eLpNorm (g n) p μ ≤ c n)
  (hc : Filter.Tendsto c Filter.atTop (nhds 0)) : g₀ =ᵐ[μ] 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Complete.html#TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le).

## Other forms

**Fatou's lemma for the `Lᵖ` seminorm of `ℝ≥0∞`-valued functions.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_ennreal_le_of_ae_tendsto`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.eLpNorm_ennreal_le_of_ae_tendsto).

```lean
TauCeti.eLpNorm_ennreal_le_of_ae_tendsto.{u_1, u_2} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {p : ENNReal} {ι : Type u_2} {u : Filter ι} [u.IsCountablyGenerated]
  {f : ι → α → ENNReal} {g : α → ENNReal} {C : ENNReal} (hf : ∀ (i : ι), AEMeasurable (f i) μ)
  (hlim : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun i => f i x) u (nhds (g x)))
  (hle : ∃ᶠ (i : ι) in u, MeasureTheory.eLpNorm (f i) p μ ≤ C) : MeasureTheory.eLpNorm g p μ ≤ C
```

## Sources

- [Tau Ceti documentation: `TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Complete.html#TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le)
- [Source of `TauCeti.ae_eq_zero_of_tendsto_of_eLpNorm_le` in TauCeti/MeasureTheory/Function/Lp/Complete.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/Complete.lean#L158)
