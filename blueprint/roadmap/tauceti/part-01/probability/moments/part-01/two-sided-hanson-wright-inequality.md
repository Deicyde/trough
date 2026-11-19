---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le
statement: formalized
proof: formalized
---

# Two-sided Hanson–Wright inequality

**Two-sided Hanson–Wright inequality** (Rudelson–Vershynin 2013, Theorem 1.1) with constant
`1 / 3200`.

```lean
ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {X : ι → Ω → ℝ} (hindep : ProbabilityTheory.iIndepFun X P) {K : NNReal}
  (hX : ∀ (i : ι), ProbabilityTheory.HasSubgaussianMGF (X i) K P) [DecidableEq ι] (A : Matrix ι ι ℝ)
  {t : ℝ} (ht : 0 ≤ t) :
  P.real
      {ω |
        t <
          |((fun i => X i ω) ⬝ᵥ A.mulVec fun i => X i ω) -
              ∫ (ω' : Ω), (fun i => X i ω') ⬝ᵥ A.mulVec fun i => X i ω' ∂P|} ≤
    2 * Real.exp (-(1 / 3200) * min (t ^ 2 / (↑K ^ 2 * ∑ i, ∑ j, A i j ^ 2)) (t / (↑K * ‖A‖)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Two-sided sub-exponential Chernoff bound](../part-02/two-sided-sub-exponential-chernoff-bound.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_abs_dotProduct_mulVec_sub_integral_gt_le` in TauCeti/Probability/Moments/HansonWright.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/HansonWright.lean#L171)
