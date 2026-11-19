---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral
statement: formalized
proof: formalized
---

# Integrated conditional Hanson–Wright inequality for an independent random matrix `A`

```lean
ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {X : ι → Ω → ℝ} (hindep : ProbabilityTheory.iIndepFun X P) {K : NNReal}
  (hX : ∀ (i : ι), ProbabilityTheory.HasSubgaussianMGF (X i) K P) [DecidableEq ι]
  {A : Ω → Matrix ι ι ℝ} (hA_meas : AEMeasurable A P)
  (hAX : ProbabilityTheory.IndepFun A (fun ω i => X i ω) P) {t : ℝ} (ht : 0 ≤ t) :
  P.real
      {ω |
        t <
          |((fun i => X i ω) ⬝ᵥ (A ω).mulVec fun i => X i ω) -
              ∑ i, A ω i i * ∫ (x : Ω), (fun ω' => X i ω' ^ 2) x ∂P|} ≤
    ∫ (ω : Ω),
      min 1
        (2 *
          Real.exp
            (-(1 / 3200) * min (t ^ 2 / (↑K ^ 2 * ∑ i, ∑ j, A ω i j ^ 2)) (t / (↑K * ‖A ω‖)))) ∂P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Two-sided Hanson–Wright inequality](two-sided-hanson-wright-inequality.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_sum_diag_gt_le_integral` in TauCeti/Probability/Moments/HansonWright.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/HansonWright.lean#L246)
