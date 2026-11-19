---
declaration: theorem
origin: cited
lean: TauCeti.Real.mul_lintegral_add_mul_lintegral_le
statement: formalized
proof: formalized
---

# Prékopa–Leindler inequality for the minimum on `ℝ`

If `f` and `g` have the same
supremum and `h (c * x + d * y)` dominates `min (f x) (g y)` for all `x` and `y`, then
`c ∫ f + d ∫ g ≤ ∫ h`. The coefficients may vanish or be negative (a negative coefficient
contributes `0`), and the common supremum and the integrals may be infinite.

```lean
TauCeti.Real.mul_lintegral_add_mul_lintegral_le {f g h : ℝ → ENNReal}
  (hf : AEMeasurable f MeasureTheory.volume) (hg : AEMeasurable g MeasureTheory.volume)
  (hh : AEMeasurable h MeasureTheory.volume) (hfg : ⨆ x, f x = ⨆ y, g y) {c d : ℝ}
  (hmin : ∀ (x y : ℝ), min (f x) (g y) ≤ h (c * x + d * y)) :
  (ENNReal.ofReal c * ∫⁻ (x : ℝ), f x) + ENNReal.ofReal d * ∫⁻ (y : ℝ), g y ≤ ∫⁻ (z : ℝ), h z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.mul_lintegral_add_mul_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.html#TauCeti.Real.mul_lintegral_add_mul_lintegral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.mul_lintegral_add_mul_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.html#TauCeti.Real.mul_lintegral_add_mul_lintegral_le)
- [Source of `TauCeti.Real.mul_lintegral_add_mul_lintegral_le` in TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.lean#L300)
