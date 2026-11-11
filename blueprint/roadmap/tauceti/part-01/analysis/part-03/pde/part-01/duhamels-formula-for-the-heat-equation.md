---
declaration: theorem
origin: cited
lean: TauCeti.heatKernel_convolution_sub_eq_integral, TauCeti.heatSemigroup_sub_eq_integral
statement: formalized
proof: formalized
---

# Duhamel's formula for the heat equation

For `φ` of class `C²` with compact support and
`t > 0`, `(K_t ⋆ φ)(x) - φ(x) = ∫₀ᵗ (K_s ⋆ Δ φ)(x) ds` at every point `x`.

```lean
TauCeti.heatKernel_convolution_sub_eq_integral.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {t : ℝ} [MeasurableSpace E] [BorelSpace E] [CompleteSpace F] {φ : E → F}
  (hφ : ContDiff ℝ 2 φ) (hc : HasCompactSupport φ) (ht : 0 < t) (x : E) :
  MeasureTheory.convolution (TauCeti.heatKernel t) φ (ContinuousLinearMap.lsmul ℝ ℝ)
        MeasureTheory.volume x -
      φ x =
    ∫ (s : ℝ) in 0..t,
      MeasureTheory.convolution (TauCeti.heatKernel s) (Laplacian.laplacian φ)
        (ContinuousLinearMap.lsmul ℝ ℝ) MeasureTheory.volume x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Young's inequality for an `L¹` kernel](../../../../measure-theory/function/part-02/youngs-inequality-for-an-l1-kernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.heatKernel_convolution_sub_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.heatKernel_convolution_sub_eq_integral).

## Other forms

**Duhamel's formula for the heat semigroup.** Formalized in Tau Ceti as [`TauCeti.heatSemigroup_sub_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/Generator.html#TauCeti.heatSemigroup_sub_eq_integral).

```lean
TauCeti.heatSemigroup_sub_eq_integral.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {p : ENNReal}
  [Fact (1 ≤ p)] {φ : E → F} (hp : p ≠ ⊤) (hφ : ContDiff ℝ 2 φ) (hc : HasCompactSupport φ)
  {f g : ↥(MeasureTheory.Lp F p MeasureTheory.volume)} (hf : ↑↑f =ᵐ[MeasureTheory.volume] φ)
  (hg : ↑↑g =ᵐ[MeasureTheory.volume] Laplacian.laplacian φ) {t : ℝ} (ht : 0 < t) :
  ((TauCeti.heatSemigroup hp).realOperator t) f - f =
    ∫ (s : ℝ) in Set.Ioc 0 t, ((TauCeti.heatSemigroup hp).realOperator s) g
```

## Sources

- [Tau Ceti documentation: `TauCeti.heatKernel_convolution_sub_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.heatKernel_convolution_sub_eq_integral)
- [Source of `TauCeti.heatKernel_convolution_sub_eq_integral` in TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean#L371)
