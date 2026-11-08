---
declaration: theorem
origin: cited
lean: TauCeti.Green.green_ac_flux_jordan
statement: formalized
proof: formalized
---

# Flux-divergence form of Green's theorem for a simple closed absolutely continuous curve

the boundary integral of `X dy - Y dx` equals `Contour.jordanSign γ a b ∈ {1, -1}` times the
divergence integral over `filledHull (γ '' uIcc a b) \ (γ '' uIcc a b)`.

```lean
TauCeti.Green.green_ac_flux_jordan {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ} {X Y : ℂ → ℝ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) (hU : IsOpen U)
  (hregion : TauCeti.filledHull (γ '' Set.uIcc a b) ⊆ U) (hX : ContDiffOn ℝ 1 X U)
  (hY : ContDiffOn ℝ 1 Y U) :
  IntervalIntegrable (fun t => X (γ t) * (deriv γ t).im - Y (γ t) * (deriv γ t).re)
      MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn (fun z => (fderiv ℝ X z) 1 + (fderiv ℝ Y z) Complex.I)
        (TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b) MeasureTheory.volume ∧
      ∫ (t : ℝ) in a..b, X (γ t) * (deriv γ t).im - Y (γ t) * (deriv γ t).re =
        ↑(TauCeti.Contour.jordanSign γ a b) *
          ∫ (z : ℂ) in TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b,
            (fderiv ℝ X z) 1 + (fderiv ℝ Y z) Complex.I
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Green's theorem for a simple closed absolutely continuous curve](greens-theorem-for-a-simple-closed-absolutely-co.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Green.green_ac_flux_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Jordan.html#TauCeti.Green.green_ac_flux_jordan).

## Sources

- [Tau Ceti documentation: `TauCeti.Green.green_ac_flux_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Jordan.html#TauCeti.Green.green_ac_flux_jordan)
- [Source of `TauCeti.Green.green_ac_flux_jordan` in TauCeti/Analysis/Green/Jordan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Green/Jordan.lean#L90)
