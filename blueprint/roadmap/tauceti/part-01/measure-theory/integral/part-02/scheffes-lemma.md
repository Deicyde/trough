---
declaration: theorem
origin: cited
lean: MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral
statement: formalized
proof: formalized
---

# Scheffé's lemma

If nonnegative integrable functions `f i` converge almost everywhere to an
integrable function `g` and their integrals converge to the integral of `g`, then `f i` converges
to `g` in `L¹`: `∫ ‖f i - g‖ → 0`.

```lean
MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] {μ : MeasureTheory.Measure α} {ι : Type u_2} {l : Filter ι}
  [l.IsCountablyGenerated] {f : ι → α → ℝ} {g : α → ℝ}
  (hf : ∀ (i : ι), MeasureTheory.Integrable (f i) μ) (hg : MeasureTheory.Integrable g μ)
  (hf₀ : ∀ (i : ι), 0 ≤ᵐ[μ] f i)
  (hlim : ∀ᵐ (a : α) ∂μ, Filter.Tendsto (fun i => f i a) l (nhds (g a)))
  (hint : Filter.Tendsto (fun i => ∫ (a : α), f i a ∂μ) l (nhds (∫ (a : α), g a ∂μ))) :
  Filter.Tendsto (fun i => ∫ (a : α), ‖f i a - g a‖ ∂μ) l (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Scheffe.html#MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral).

## Sources

- [Tau Ceti documentation: `MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Scheffe.html#MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral)
- [Source of `MeasureTheory.tendsto_integral_norm_sub_of_tendsto_integral` in TauCeti/MeasureTheory/Integral/Scheffe.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Scheffe.lean#L37)
