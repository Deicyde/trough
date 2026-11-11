---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus in the first coordinate

The integral of a continuous
partial derivative `φ = ∂₁ Φ` over the rectangle `[a₁, b₁] × [a₂, b₂]` is the integral over
`[a₂, b₂]` of the difference of the values of `Φ` on the two vertical sides.

```lean
TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {a₁ b₁ a₂ b₂ : ℝ} {Φ φ : ℝ × ℝ → E} (hφ : Continuous φ)
  (hΦ : ∀ (s t : ℝ), HasDerivAt (fun s => Φ (s, t)) (φ (s, t)) s) (hab : a₁ ≤ b₁) :
  ∫ (z : ℝ × ℝ) in Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂, φ z =
    ∫ (t : ℝ) in Set.Icc a₂ b₂, Φ (b₁, t) - Φ (a₁, t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Rectangle.html#TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst).

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Rectangle.html#TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst)
- [Source of `TauCeti.setIntegral_rect_eq_setIntegral_sub_of_hasDerivAt_fst` in TauCeti/MeasureTheory/Integral/Rectangle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Rectangle.lean#L53)
