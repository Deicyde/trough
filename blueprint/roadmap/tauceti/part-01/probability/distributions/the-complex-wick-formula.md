---
declaration: theorem
origin: cited
lean: TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure
statement: formalized
proof: formalized
---

# The complex Wick formula

A centered product of proper complex Gaussian coordinates
and conjugated coordinates is the sum of covariance products over all bijections between their
positions. For unequal degrees the sum is empty; for equal degrees it is a permanent.
The empty moment is one. Singular covariance matrices and repeated coordinates are allowed.

```lean
TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure.{u_1, u_2, u_3}
  {ι : Type u_1} {α : Type u_2} {β : Type u_3} [Fintype ι] [DecidableEq ι] [Fintype α] [Fintype β]
  [DecidableEq α] [DecidableEq β] (m : ι → ℂ) {C : Matrix ι ι ℂ} (hC : C.PosSemidef) (f : α → ι)
  (g : β → ι) :
  ∫ (z : ι → ℂ),
      (∏ i, (z (f i) - m (f i))) *
        ∏ j, star (z (g j) - m (g j)) ∂TauCeti.Probability.properComplexGaussianMeasure m C =
    ∑ e, ∏ i, C (f i) (g (e i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/MixedMoments.html#TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/MixedMoments.html#TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure)
- [Source of `TauCeti.Probability.integral_prod_mul_prod_conj_sub_properComplexGaussianMeasure` in TauCeti/Probability/Distributions/Gaussian/ProperComplex/MixedMoments.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/Gaussian/ProperComplex/MixedMoments.lean#L224)
