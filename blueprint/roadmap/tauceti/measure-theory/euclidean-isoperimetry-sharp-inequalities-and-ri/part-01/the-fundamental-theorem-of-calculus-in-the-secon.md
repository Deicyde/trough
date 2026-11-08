---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus in the second coordinate

The integral of a
continuous partial derivative `φ = ∂₂ Φ` over the rectangle `[a₁, b₁] × [a₂, b₂]` is the integral
over `[a₁, b₁]` of the difference of the values of `Φ` on the two horizontal sides.

```lean
TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {a₁ b₁ a₂ b₂ : ℝ} {Φ φ : ℝ × ℝ → E}
  (hφ : Continuous φ) (hΦ : ∀ (s t : ℝ), HasDerivAt (fun t => Φ (s, t)) (φ (s, t)) t)
  (hab : a₂ ≤ b₂) :
  ∫ (z : ℝ × ℝ) in Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂, φ z =
    ∫ (s : ℝ) in Set.Icc a₁ b₁, Φ (s, b₂) - Φ (s, a₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Rectangle.html#TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd).

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Rectangle.html#TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd)
- [Source of `TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_snd` in TauCeti/MeasureTheory/Integral/Rectangle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/Rectangle.lean#L71)
