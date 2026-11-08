---
declaration: theorem
origin: cited
lean: TauCeti.meas_ge_le_integral_norm_sq_div_sq
statement: formalized
proof: formalized
---

# Chebyshev's inequality for the second moment

For any measure, if `‖Y‖²` is integrable
and `0 < c`, the set where `‖Y‖` is at least `c` has measure at most `(∫ ‖Y‖²) / c²`. Unlike
`ProbabilityTheory.meas_ge_le_variance_div_sq`, `Y` is not centered at its mean.

```lean
TauCeti.meas_ge_le_integral_norm_sq_div_sq.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [Norm E] {Y : Ω → E}
  (hY : MeasureTheory.Integrable (fun ω => ‖Y ω‖ ^ 2) μ) {c : ℝ} (hc : 0 < c) :
  μ {ω | c ≤ ‖Y ω‖} ≤ ENNReal.ofReal ((∫ (ω : Ω), ‖Y ω‖ ^ 2 ∂μ) / c ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.meas_ge_le_integral_norm_sq_div_sq`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Chebyshev.html#TauCeti.meas_ge_le_integral_norm_sq_div_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.meas_ge_le_integral_norm_sq_div_sq`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Chebyshev.html#TauCeti.meas_ge_le_integral_norm_sq_div_sq)
- [Source of `TauCeti.meas_ge_le_integral_norm_sq_div_sq` in TauCeti/Probability/Moments/Chebyshev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/Chebyshev.lean#L40)
