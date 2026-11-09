---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_ennreal_le_of_ae_tendsto, TauCeti.eLpNorm_le_of_ae_tendsto_ennreal
statement: formalized
proof: formalized
---

# Fatou's lemma for the `Lᵖ` seminorm of `ℝ≥0∞`-valued functions

**Fatou's lemma for the `Lᵖ` seminorm of `ℝ≥0∞`-valued functions**, at every exponent
`p : ℝ≥0∞` (including `0` and `∞`) and along any countably generated `NeBot` filter. Almost
everywhere measurability of the limit is deduced from the pointwise convergence.

```lean
TauCeti.eLpNorm_ennreal_le_of_ae_tendsto.{u_1, u_2} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {p : ENNReal} {ι : Type u_2} {u : Filter ι} [u.NeBot]
  [u.IsCountablyGenerated] {f : ι → α → ENNReal} {g : α → ENNReal} {C : ENNReal}
  (hf : ∀ (i : ι), AEMeasurable (f i) μ)
  (hlim : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun i => f i x) u (nhds (g x)))
  (hle : ∀ᶠ (i : ι) in u, MeasureTheory.eLpNorm (f i) p μ ≤ C) : MeasureTheory.eLpNorm g p μ ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_ennreal_le_of_ae_tendsto`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.eLpNorm_ennreal_le_of_ae_tendsto).

## Other forms

**Fatou's lemma for the `Lᵖ` seminorm of `ℝ≥0∞`-valued functions.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_of_ae_tendsto_ennreal`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.eLpNorm_le_of_ae_tendsto_ennreal).

```lean
TauCeti.eLpNorm_le_of_ae_tendsto_ennreal.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {p : ENNReal} (hp0 : p ≠ 0) (hp : p ≠ ⊤) {f : ℕ → α → ENNReal}
  {g : α → ENNReal} {c : ENNReal} (hf : ∀ (n : ℕ), AEMeasurable (f n) μ)
  (hlim : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun n => f n x) Filter.atTop (nhds (g x)))
  (hle : ∀ (n : ℕ), MeasureTheory.eLpNorm (f n) p μ ≤ c) : MeasureTheory.eLpNorm g p μ ≤ c
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_ennreal_le_of_ae_tendsto`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.eLpNorm_ennreal_le_of_ae_tendsto)
- [Source of `TauCeti.eLpNorm_ennreal_le_of_ae_tendsto` in TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.lean#L99)
