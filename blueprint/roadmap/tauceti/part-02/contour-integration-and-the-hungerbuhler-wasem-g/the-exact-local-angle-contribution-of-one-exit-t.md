---
declaration: theorem
origin: cited
lean: TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi
statement: formalized
proof: formalized
---

# The exact local angle contribution of one exit-time cap window

The winding number of
the curve over the window minus that of its cap is `crossingAngle γ t₀ / 2π`.  Beyond the
standing continuity, tangent, and radius hypotheses -- which already give equal endpoint radii
and endpoint matching -- the only extra input is the principal value of `(z - s)⁻¹` along the
generally asymmetric exit-time interval.

```lean
TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi {γ : ℝ → ℂ} {s : ℂ}
  {t₀ δ ε : ℝ} {L_R L_L : ℂ} (hδ : 0 < δ) (hε : 0 < ε) (h_at : γ t₀ = s)
  (hγ : ContinuousOn γ (Set.Icc (t₀ - δ) (t₀ + δ))) (hεL : ε ≤ ‖γ (t₀ - δ) - s‖)
  (hεR : ε ≤ ‖γ (t₀ + δ) - s‖) (hL_R : L_R ≠ 0) (hL_L : L_L ≠ 0)
  (h_R : Filter.Tendsto (deriv γ) (nhdsWithin t₀ (Set.Ioi t₀)) (nhds L_R))
  (h_L : Filter.Tendsto (deriv γ) (nhdsWithin t₀ (Set.Iio t₀)) (nhds L_L))
  (hpv :
    TauCeti.Contour.HasCauchyPVAt γ (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).lower
      (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).upper (fun z => (z - s)⁻¹) s
      (↑((-L_L / (γ (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).lower - s)).arg +
            ((γ (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).upper - s) / L_R).arg) *
        Complex.I)) :
  TauCeti.Contour.windingNumber γ (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).lower
        (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).upper s -
      TauCeti.Contour.windingNumber ((TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).cap s)
        (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).lower
        (TauCeti.Contour.exitCapWindow γ s t₀ δ ε L_R L_L).upper s =
    ↑(TauCeti.Contour.crossingAngle γ t₀) / (2 * ↑Real.pi)
```

## Depends on

- [First exit time at radius `ε` (left side)](first-exit-time-at-radius-left-side.md)
- [Generalized winding number](generalized-winding-number.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Crossing/ExitWindow.html#TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Crossing/ExitWindow.html#TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi)
- [Source of `TauCeti.Contour.windingNumber_sub_cap_exitCapWindow_eq_crossingAngle_div_two_pi` in TauCeti/Analysis/Contour/Crossing/ExitWindow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Crossing/ExitWindow.lean#L466)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
