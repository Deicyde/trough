---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le, ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le, ProbabilityTheory.iIndepFun.measureReal_abs_re_star_dotProduct_mulVec_sub_integral_gt_le
statement: formalized
proof: formalized
---

# Complex Hanson–Wright inequality for bounded mean-zero coordinates

```lean
ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le.{u_1,
    u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {Z : ι → Ω → ℂ} (hindep : ProbabilityTheory.iIndepFun Z P) [DecidableEq ι]
  (hZ_meas : ∀ (i : ι), AEMeasurable (Z i) P) {b : NNReal}
  (hZ_norm : ∀ (i : ι), ∀ᵐ (ω : Ω) ∂P, ‖Z i ω‖ ≤ ↑b) (hZ_mean : ∀ (i : ι), ∫ (ω : Ω), Z i ω ∂P = 0)
  (A : Matrix ι ι ℂ) {t : ℝ} (ht : 0 ≤ t) :
  P.real
      {ω |
        t <
          ‖((star fun i => Z i ω) ⬝ᵥ A.mulVec fun i => Z i ω) -
              ∫ (ω' : Ω), (star fun i => Z i ω') ⬝ᵥ A.mulVec fun i => Z i ω' ∂P‖} ≤
    2 *
      Real.exp
        (-(1 / 150528) *
          min (t ^ 2 / (↑(b ^ 2) ^ 2 * ∑ i, ∑ j, ‖A i j‖ ^ 2)) (t / (↑(b ^ 2) * ‖A‖)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Two-sided sub-exponential Chernoff bound](../part-02/two-sided-sub-exponential-chernoff-bound.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le).

## Other forms

**Complex Hanson–Wright inequality (full complex norm) with constant `1 / 150528`.** Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le).

```lean
ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {Z : ι → Ω → ℂ} (hindep : ProbabilityTheory.iIndepFun Z P) {K : NNReal}
  (hZ :
    ∀ (i : ι) (u : ℂ),
      ProbabilityTheory.HasSubgaussianMGF (fun ω => (star u * Z i ω).re) (‖u‖₊ ^ 2 * K) P)
  [DecidableEq ι] (A : Matrix ι ι ℂ) {t : ℝ} (ht : 0 ≤ t) :
  P.real
      {ω |
        t <
          ‖((star fun i => Z i ω) ⬝ᵥ A.mulVec fun i => Z i ω) -
              ∫ (ω' : Ω), (star fun i => Z i ω') ⬝ᵥ A.mulVec fun i => Z i ω' ∂P‖} ≤
    2 * Real.exp (-(1 / 150528) * min (t ^ 2 / (↑K ^ 2 * ∑ i, ∑ j, ‖A i j‖ ^ 2)) (t / (↑K * ‖A‖)))
```

**Complex Hanson–Wright inequality (real part) with constant `1 / 12544`.** Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_abs_re_star_dotProduct_mulVec_sub_integral_gt_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_abs_re_star_dotProduct_mulVec_sub_integral_gt_le).

```lean
ProbabilityTheory.iIndepFun.measureReal_abs_re_star_dotProduct_mulVec_sub_integral_gt_le.{u_1, u_2}
  {Ω : Type u_1} {ι : Type u_2} [MeasurableSpace Ω] [Fintype ι] {P : MeasureTheory.Measure Ω}
  {Z : ι → Ω → ℂ} (hindep : ProbabilityTheory.iIndepFun Z P) {K : NNReal}
  (hZ :
    ∀ (i : ι) (u : ℂ),
      ProbabilityTheory.HasSubgaussianMGF (fun ω => (star u * Z i ω).re) (‖u‖₊ ^ 2 * K) P)
  [DecidableEq ι] (A : Matrix ι ι ℂ) {t : ℝ} (ht : 0 ≤ t) :
  P.real
      {ω |
        t <
          |((star fun i => Z i ω) ⬝ᵥ A.mulVec fun i => Z i ω).re -
              ∫ (ω' : Ω), ((star fun i => Z i ω') ⬝ᵥ A.mulVec fun i => Z i ω').re ∂P|} ≤
    2 * Real.exp (-(1 / 12544) * min (t ^ 2 / (↑K ^ 2 * ∑ i, ∑ j, ‖A i j‖ ^ 2)) (t / (↑K * ‖A‖)))
```

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_norm_star_dotProduct_mulVec_sub_integral_gt_le_of_norm_le` in TauCeti/Probability/Moments/HansonWright.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/HansonWright.lean#L611)
