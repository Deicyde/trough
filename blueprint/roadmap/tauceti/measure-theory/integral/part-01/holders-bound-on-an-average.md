---
declaration: theorem
origin: cited
lean: TauCeti.enorm_setAverage_le, TauCeti.enorm_setAverage_rpow_le
statement: formalized
proof: formalized
---

# Hölder's bound on an average

the average of `f` over a set `s` is at most
`μ s ^ (-1/p)` times the `Lᵖ` seminorm of `f` on `s`. At `p = 1` this is the
bound by the average of `‖f‖`, and the volume factor sharpens as `p` grows because a larger
exponent controls the mass of `s` more efficiently. No measurability or integrability hypothesis
is needed, since a function not integrable on `s` has average zero.

```lean
TauCeti.enorm_setAverage_le.{u_1, u_2} {α : Type u_1} {F : Type u_2} [MeasurableSpace α]
  {mu : MeasureTheory.Measure α} [NormedAddCommGroup F] [NormedSpace ℝ F] {f : α → F} {p : ENNReal}
  {s : Set α} (hp : 1 ≤ p) (hp' : p ≠ ⊤) :
  ‖⨍ (y : α) in s, f y ∂mu‖ₑ ≤ mu s ^ (-p.toReal⁻¹) * MeasureTheory.eLpNorm f p (mu.restrict s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.enorm_setAverage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.enorm_setAverage_le).

## Other forms

**Hölder's bound on an average, in `∫⁻` form.** Formalized in Tau Ceti as [`TauCeti.enorm_setAverage_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.enorm_setAverage_rpow_le).

```lean
TauCeti.enorm_setAverage_rpow_le.{u_1, u_2} {α : Type u_1} {F : Type u_2} [MeasurableSpace α]
  {mu : MeasureTheory.Measure α} [NormedAddCommGroup F] [NormedSpace ℝ F] {f : α → F} {s : Set α}
  {q : ℝ} (hq : 1 ≤ q) : ‖⨍ (y : α) in s, f y ∂mu‖ₑ ^ q ≤ (mu s)⁻¹ * ∫⁻ (y : α) in s, ‖f y‖ₑ ^ q ∂mu
```

## Sources

- [Tau Ceti documentation: `TauCeti.enorm_setAverage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.enorm_setAverage_le)
- [Source of `TauCeti.enorm_setAverage_le` in TauCeti/MeasureTheory/Integral/Average.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/Average.lean#L182)
