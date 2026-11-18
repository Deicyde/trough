---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound
statement: formalized
proof: formalized
---

# Complex conditional Hanson–Wright inequality

The random matrix is independent of the
whole coordinate vector. Its squared Frobenius norm and Euclidean operator norm need only be
bounded almost everywhere. The center is expressed using the coordinate second moments; no
integrability of the random matrix is required.

```lean
ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound.{u_1,
    u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {Z : ι → Ω → ℂ} (hindep : ProbabilityTheory.iIndepFun Z P) {K : NNReal}
  (hZ :
    ∀ (i : ι) (u : ℂ),
      ProbabilityTheory.HasSubgaussianMGF (fun ω => (star u * Z i ω).re) (‖u‖₊ ^ 2 * K) P)
  [DecidableEq ι] {A : Ω → Matrix ι ι ℂ} (hA : AEMeasurable A P)
  (hAZ : ProbabilityTheory.IndepFun A (fun ω i => Z i ω) P) {F op : ℝ}
  (hF : ∀ᵐ (ω : Ω) ∂P, ∑ i, ∑ j, ‖A ω i j‖ ^ 2 ≤ F) (hop : ∀ᵐ (ω : Ω) ∂P, ‖A ω‖ ≤ op) {t : ℝ} :
  P.real
      {ω |
        t <
          ‖((star fun i => Z i ω) ⬝ᵥ (A ω).mulVec fun i => Z i ω) -
              ∑ i, A ω i i * ↑(∫ (x : Ω), (fun ω' => ‖Z i ω'‖ ^ 2) x ∂P)‖} ≤
    2 * Real.exp (-(1 / 150528) * min (t ^ 2 / (↑K ^ 2 * F)) (t / (↑K * op)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex Hanson–Wright inequality for bounded mean-zero coordinates](complex-hanson-wright-inequality-for-bounded-mea.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_sum_diag_gt_le_of_ae_bound` in TauCeti/Probability/Moments/HansonWright.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/HansonWright.lean#L576)
