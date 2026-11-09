---
declaration: theorem
origin: cited
lean: TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings
statement: formalized
proof: formalized
---

# The real bounded-integrand formula, allowing crossings (Hungerbühler–Wasem Prop 2.3)

For a closed piecewise-`C¹` immersion `γ` on `[[a, b]]` that avoids `s` at the basepoint `a`
(`hsa`, so also at `b` by closedness — every other crossing of `s`, if any, is automatically
interior to `[[a, b]]`) and is `C^{1,1}` on each side of any such crossing (`derivWithin γ`
Lipschitz on a one-sided closed piece ending or starting there, `hγ_lip` — the two sides need not
agree, so a crossing may coincide with a breakpoint of the immersion) — in particular satisfied
vacuously if `γ` never meets `s` — the generalized winding number `n_s(γ)` is a real number equal
to its ordinary (non-principal-value) integral:

`n_s(γ) = (1 / 2π) ∫_a^b (x ẏ - y ẋ) / (x² + y²) dt`, `x + i y = γ - s`.

The two sides of a crossing need not agree: `hγ_lip` allows the crossing to coincide with a
breakpoint of the piecewise-`C¹` immersion (a corner), matching Hungerbühler–Wasem's own proof of
Prop 2.3, which handles that case via the same one-sided splitting (arXiv:1808.00997, p. 9).
Orientation-generic, like `windingNumber` and `intervalIntegral` themselves: no `a ≤ b` is
needed.

```lean
TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings {γ : ℝ → ℂ} {a b : ℝ}
  {s : ℂ} (h_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hclosed : γ a = γ b) (hsa : γ a ≠ s)
  (hγ_lip : ∀ t ∈ Set.uIcc a b, γ t = s → TauCeti.Contour.HasLipschitzDerivOnEachSideAt γ t) :
  TauCeti.Contour.windingNumber γ a b s =
    ↑(1 / (2 * Real.pi) *
        ∫ (t : ℝ) in a..b, TauCeti.Contour.realWindingIntegrand (γ t - s) (deriv γ t))
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [First exit time at radius `ε` (left side)](first-exit-time-at-radius-left-side.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/RealIntegral/OnCurve.html#TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/RealIntegral/OnCurve.html#TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings)
- [Source of `TauCeti.Contour.windingNumber_eq_real_integral_of_closed_interior_crossings` in TauCeti/Analysis/Contour/Winding/RealIntegral/OnCurve.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Winding/RealIntegral/OnCurve.lean#L467)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
