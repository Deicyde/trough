---
declaration: theorem
origin: cited
lean: TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div
statement: formalized
proof: formalized
---

# Chebyshev's inequality for truncations

For `k < l`, the level set `{l < g}` in a
measurable set `s` has measure at most `∫_s ((g - k)⁺)² / (l - k)²`, when `((g - k)⁺)²` is
integrable on `s`.

```lean
TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div.{u_1} {X : Type u_1}
  [MeasurableSpace X] {ν : MeasureTheory.Measure X} {g : X → ℝ} {s : Set X} (hs : MeasurableSet s)
  {k l : ℝ} (hkl : k < l) (hint : MeasureTheory.IntegrableOn (fun x => max (g x - k) 0 ^ 2) s ν) :
  ν.real (s ∩ {x | l < g x}) ≤ (∫ (x : X) in s, max (g x - k) 0 ^ 2 ∂ν) / (l - k) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/Basic.html#TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div).

## Sources

- [Tau Ceti documentation: `TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/Basic.html#TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div)
- [Source of `TauCeti.MeasureTheory.measureReal_inter_lt_le_setIntegral_max_sub_sq_div` in TauCeti/MeasureTheory/Integral/Bochner/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Bochner/Basic.lean#L742)
