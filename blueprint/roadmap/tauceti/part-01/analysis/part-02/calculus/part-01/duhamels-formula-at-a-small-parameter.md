---
declaration: theorem
origin: cited
lean: TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt, TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral
statement: formalized
proof: formalized
---

# Duhamel's formula at a small parameter

For a parameter `s₀` of norm less than `1`, the
derivative of the perturbed flow of `f` at `(x, s₀)` in a parameter direction `e` is
`-Dφ_T(x) ∫₀ᵀ Dφ_{-σ}(φ_σ x) (∑ᵢ eᵢ ∇hᵢ(φ_σ x)) dσ`, where `φ` is now the negative-gradient flow
of the perturbation `f_{s₀}`.

```lean
TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt.{u_1, u_2} {E : Type u_1}
  {ι : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Fintype ι]
  {f : E → ℝ} {h : ι → E → ℝ} {K : NNReal} (hfs : ContDiff ℝ 2 f)
  (hf : LipschitzWith K (gradient f)) (hh : ∀ (i : ι), ContDiff ℝ 2 (h i))
  (hc : ∀ (i : ι), HasCompactSupport (h i)) {s₀ : EuclideanSpace ℝ ι} (hs₀ : ‖s₀‖ < 1) {K' : NNReal}
  (hf' : LipschitzWith K' (gradient (TauCeti.perturb f h s₀))) (x : E) (e : EuclideanSpace ℝ ι)
  (T : ℝ) :
  ((fderiv ℝ ((TauCeti.perturbedFlow f h hf hh hc).toFun T) (x, s₀)) (0, e)).1 =
    -(fderiv ℝ ((TauCeti.negativeGradientFlow (TauCeti.perturb f h s₀) hf').toFun T) x)
        (∫ (σ : ℝ) in 0..T,
          (fderiv ℝ ((TauCeti.negativeGradientFlow (TauCeti.perturb f h s₀) hf').toFun (-σ))
              ((TauCeti.negativeGradientFlow (TauCeti.perturb f h s₀) hf').toFun σ x))
            (∑ i,
              e.ofLp i •
                gradient (h i)
                  ((TauCeti.negativeGradientFlow (TauCeti.perturb f h s₀) hf').toFun σ x)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/MorseSmale/Perturbation.html#TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt).

## Other forms

**Duhamel's formula for the parameter variation.** Formalized in Tau Ceti as [`TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/MorseSmale/Perturbation.html#TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral).

```lean
TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral.{u_1, u_2} {E : Type u_1} {ι : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Fintype ι] {f : E → ℝ}
  {h : ι → E → ℝ} {K : NNReal} (hfs : ContDiff ℝ 2 f) (hf : LipschitzWith K (gradient f))
  (hh : ∀ (i : ι), ContDiff ℝ 2 (h i)) (hc : ∀ (i : ι), HasCompactSupport (h i)) (x : E)
  (e : EuclideanSpace ℝ ι) (T : ℝ) :
  ((fderiv ℝ ((TauCeti.perturbedFlow f h hf hh hc).toFun T) (x, 0)) (0, e)).1 =
    -(fderiv ℝ ((TauCeti.negativeGradientFlow f hf).toFun T) x)
        (∫ (σ : ℝ) in 0..T,
          (fderiv ℝ ((TauCeti.negativeGradientFlow f hf).toFun (-σ))
              ((TauCeti.negativeGradientFlow f hf).toFun σ x))
            (∑ i, e.ofLp i • gradient (h i) ((TauCeti.negativeGradientFlow f hf).toFun σ x)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/MorseSmale/Perturbation.html#TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt)
- [Source of `TauCeti.fst_fderiv_perturbedFlow_apply_eq_neg_integral_of_norm_lt` in TauCeti/Analysis/Calculus/Morse/MorseSmale/Perturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/MorseSmale/Perturbation.lean#L774)
