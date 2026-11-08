---
declaration: theorem
origin: cited
lean: TauCeti.integral_fderiv_sub_fderiv_Icc, TauCeti.Green.green_ac_jordan
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

- [Generalized winding number (HW Def 2.1)](../../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Jordan index theorem (orientation sign dichotomy)](../../../part-02/contour/jordan-index-theorem-orientation-sign-dichotomy.md)
- [TauCeti.Green.green_ac_winding](../../../../geometry/part-01/differential-geometry-forms-de-rham-cohomology-f/part-01/tauceti-green-green-ac-winding.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_fderiv_sub_fderiv_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral_fderiv_sub_fderiv_Icc).

## Other forms

**Green's theorem for a simple closed absolutely continuous curve.** Formalized in Tau Ceti as [`TauCeti.Green.green_ac_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Jordan.html#TauCeti.Green.green_ac_jordan).

```lean
TauCeti.Green.green_ac_jordan {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ} {P Q : ℂ → ℝ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) (hU : IsOpen U)
  (hregion : TauCeti.filledHull (γ '' Set.uIcc a b) ⊆ U) (hP : ContDiffOn ℝ 1 P U)
  (hQ : ContDiffOn ℝ 1 Q U) :
  IntervalIntegrable (TauCeti.Green.circulationFun P Q γ) MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn (TauCeti.Green.curl P Q)
        (TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b) MeasureTheory.volume ∧
      ∫ (t : ℝ) in a..b, TauCeti.Green.circulationFun P Q γ t =
        ↑(TauCeti.Contour.jordanSign γ a b) *
          ∫ (z : ℂ) in TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b,
            TauCeti.Green.curl P Q z
```

## Sources

- [Tau Ceti documentation: `TauCeti.integral_fderiv_sub_fderiv_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral_fderiv_sub_fderiv_Icc)
- [Source of `TauCeti.integral_fderiv_sub_fderiv_Icc` in TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.lean#L116)
