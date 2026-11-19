---
declaration: theorem
origin: cited
lean: TauCeti.integral_mul_inner_le
statement: formalized
proof: formalized
---

# Weighted Young inequality for a pairing

For a nonnegative weight `w` and `δ > 0`,

`∫ w ⟪G, η⟫ ≤ (δ / 2) ∫ w ‖η‖² + (2 δ)⁻¹ ∫ w ‖G‖²`,

provided the two integrals on the right exist.

```lean
TauCeti.integral_mul_inner_le.{u_1, u_2} {β : Type u_1} [MeasurableSpace β]
  {ν : MeasureTheory.Measure β} {F : Type u_2} [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  {w : β → ℝ} {G η : β → F} (hw : ∀ (z : β), 0 ≤ w z)
  (hη : MeasureTheory.Integrable (fun z => w z * ‖η z‖ ^ 2) ν)
  (hG : MeasureTheory.Integrable (fun z => w z * ‖G z‖ ^ 2) ν) {δ : ℝ} (hδ : 0 < δ) :
  ∫ (z : β), w z * inner ℝ (G z) (η z) ∂ν ≤
    δ / 2 * ∫ (z : β), w z * ‖η z‖ ^ 2 ∂ν + 1 / (2 * δ) * ∫ (z : β), w z * ‖G z‖ ^ 2 ∂ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_mul_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.integral_mul_inner_le).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_mul_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.integral_mul_inner_le)
- [Source of `TauCeti.integral_mul_inner_le` in TauCeti/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/MeanInequalities.lean#L135)
