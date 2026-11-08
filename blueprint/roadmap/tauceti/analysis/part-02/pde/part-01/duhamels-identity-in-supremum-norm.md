---
declaration: theorem
origin: cited
lean: TauCeti.heatSemigroupBUC_sub_eq_integral, ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral
statement: formalized
proof: formalized
---

# Duhamel's identity in supremum norm

For bounded uniformly continuous `C²` data `f`
with bounded first and second derivatives and bounded uniformly continuous Laplacian `g`,
`e^{tΔ} f - f = ∫₀ᵗ e^{sΔ} g ds` as a Banach-valued integral.

```lean
TauCeti.heatSemigroupBUC_sub_eq_integral.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {f g : ↥(BoundedContinuousFunction.uniformContinuousSubmodule ℝ E F)} {M₁ M₂ : ℝ}
  (hf : ContDiff ℝ 2 ⇑↑f) (h₁ : ∀ (y : E), ‖fderiv ℝ (⇑↑f) y‖ ≤ M₁)
  (h₂ : ∀ (y : E), ‖fderiv ℝ (fderiv ℝ ⇑↑f) y‖ ≤ M₂) (hg : Laplacian.laplacian ⇑↑f = ⇑↑g) {t : ℝ}
  (ht : 0 < t) :
  (TauCeti.heatSemigroupBUC.realOperator t) f - f =
    ∫ (s : ℝ) in Set.Ioc 0 t, (TauCeti.heatSemigroupBUC.realOperator s) g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.heatSemigroupBUC_sub_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/UniformContinuous/Generator.html#TauCeti.heatSemigroupBUC_sub_eq_integral).

## Other forms

**The Duhamel identity for the exponential of a bounded operator.** Formalized in Tau Ceti as [`ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Exponential.html#ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral).

```lean
ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (B : X →L[ℝ] X) (t : ℝ) (x : X) :
  (NormedSpace.exp (t • B)) x - x = ∫ (u : ℝ) in 0..t, (NormedSpace.exp (u • B)) (B x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.heatSemigroupBUC_sub_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/UniformContinuous/Generator.html#TauCeti.heatSemigroupBUC_sub_eq_integral)
- [Source of `TauCeti.heatSemigroupBUC_sub_eq_integral` in TauCeti/Analysis/PDE/HeatKernel/UniformContinuous/Generator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/UniformContinuous/Generator.lean#L45)
