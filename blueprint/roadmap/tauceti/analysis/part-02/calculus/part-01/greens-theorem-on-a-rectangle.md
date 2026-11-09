---
declaration: theorem
origin: cited
lean: TauCeti.integral_fderiv_sub_fderiv_Icc
statement: formalized
proof: formalized
---

# Green's theorem on a rectangle

For a one-form `f_s ds + f_t dt` that is `C¹` over an
open neighbourhood of a rectangle `[a₁, b₁] × [a₂, b₂]`, the integral of its exterior derivative
`∂_s f_t - ∂_t f_s` over the rectangle is its integral over the positively oriented boundary.

```lean
TauCeti.integral_fderiv_sub_fderiv_Icc {U : Set (ℝ × ℝ)} {fs ft : ℝ × ℝ → ℝ} {a b : ℝ × ℝ}
  (hU : IsOpen U) (hfs : ContDiffOn ℝ 1 fs U) (hft : ContDiffOn ℝ 1 ft U) (hab : a ≤ b)
  (habU : Set.Icc a b ⊆ U) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b, (fderiv ℝ ft z) (1, 0) - (fderiv ℝ fs z) (0, 1) =
    (((∫ (s : ℝ) in a.1..b.1, fs (s, a.2)) + ∫ (t : ℝ) in a.2..b.2, ft (b.1, t)) -
        ∫ (s : ℝ) in a.1..b.1, fs (s, b.2)) -
      ∫ (t : ℝ) in a.2..b.2, ft (a.1, t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_fderiv_sub_fderiv_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral_fderiv_sub_fderiv_Icc).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_fderiv_sub_fderiv_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral_fderiv_sub_fderiv_Icc)
- [Source of `TauCeti.integral_fderiv_sub_fderiv_Icc` in TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean#L116)
