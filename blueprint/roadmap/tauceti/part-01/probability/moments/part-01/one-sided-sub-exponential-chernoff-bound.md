---
declaration: theorem
origin: cited
lean: TauCeti.measureReal_gt_le_exp_min_of_mgf_le
statement: formalized
proof: formalized
---

# One-sided sub-exponential Chernoff bound

```lean
TauCeti.measureReal_gt_le_exp_min_of_mgf_le.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {P : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure P] {Y : Ω → ℝ} {C₁ C₂ F op : ℝ}
  (hC₁ : 0 < C₁) (hC₂ : 0 < C₂) (hF : 0 ≤ F) (hop : 0 ≤ op)
  (hmgf :
    ∀ (θ : ℝ),
      C₂ * op * |θ| ≤ 1 →
        MeasureTheory.Integrable (fun ω => Real.exp (θ * Y ω)) P ∧
          ProbabilityTheory.mgf Y P θ ≤ Real.exp (C₁ * F * θ ^ 2))
  {t : ℝ} (ht : 0 ≤ t) :
  P.real {ω | t < Y ω} ≤ Real.exp (-min (1 / (4 * C₁)) (1 / (2 * C₂)) * min (t ^ 2 / F) (t / op))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.measureReal_gt_le_exp_min_of_mgf_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#TauCeti.measureReal_gt_le_exp_min_of_mgf_le).

## Sources

- [Tau Ceti documentation: `TauCeti.measureReal_gt_le_exp_min_of_mgf_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#TauCeti.measureReal_gt_le_exp_min_of_mgf_le)
- [Source of `TauCeti.measureReal_gt_le_exp_min_of_mgf_le` in TauCeti/Probability/Moments/SubExponential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/SubExponential.lean#L107)
