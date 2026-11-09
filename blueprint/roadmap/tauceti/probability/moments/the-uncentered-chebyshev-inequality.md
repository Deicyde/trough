---
declaration: theorem
origin: cited
lean: TauCeti.meas_gt_le_div_sq_of_integral_sq_le
statement: formalized
proof: formalized
---

# The uncentered Chebyshev inequality

If `Y²` is integrable with `∫ Y² ≤ v` and `0 < η`,
then the set where `Y` exceeds `η` has measure at most `v / η²`.

```lean
TauCeti.meas_gt_le_div_sq_of_integral_sq_le.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {Y : Ω → ℝ} (hY : MeasureTheory.Integrable (fun ω => Y ω ^ 2) μ)
  {v η : ℝ} (hv : ∫ (ω : Ω), Y ω ^ 2 ∂μ ≤ v) (hη : 0 < η) :
  μ {ω | η < Y ω} ≤ ENNReal.ofReal (v / η ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chebyshev's inequality for the second moment](chebyshevs-inequality-for-the-second-moment.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.meas_gt_le_div_sq_of_integral_sq_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Chebyshev.html#TauCeti.meas_gt_le_div_sq_of_integral_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.meas_gt_le_div_sq_of_integral_sq_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Chebyshev.html#TauCeti.meas_gt_le_div_sq_of_integral_sq_le)
- [Source of `TauCeti.meas_gt_le_div_sq_of_integral_sq_le` in TauCeti/Probability/Moments/Chebyshev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/Chebyshev.lean#L58)
