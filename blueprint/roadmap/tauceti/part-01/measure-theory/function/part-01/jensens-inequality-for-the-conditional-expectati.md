---
declaration: theorem
origin: cited
lean: TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le
statement: formalized
proof: formalized
---

# Jensen's inequality for the conditional expectation, as an inequality of `lintegral`s

for
`1 ≤ p`, the `p`-th power of the norm of `μ[f | m]` integrates to at most that of `f`. Unlike
Mathlib's `integral_norm_condExp_rpow_le`, this needs no integrability of `‖f‖ ^ p`, nor any
measurability of `f`.

```lean
TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {m m₀ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} (f : Ω → E) {p : ℝ} (hp : 1 ≤ p) :
  ∫⁻ (ω : Ω), ‖μ[f | m] ω‖ₑ ^ p ∂μ ≤ ∫⁻ (ω : Ω), ‖f ω‖ₑ ^ p ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation.html#TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation.html#TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le)
- [Source of `TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le` in TauCeti/MeasureTheory/Function/ConditionalExpectation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/ConditionalExpectation.lean#L283)
