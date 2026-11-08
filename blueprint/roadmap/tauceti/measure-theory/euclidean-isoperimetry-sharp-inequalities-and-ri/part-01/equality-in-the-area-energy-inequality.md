---
declaration: theorem
origin: cited
lean: TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff
statement: formalized
proof: formalized
---

# Equality in the area–energy inequality

For an absolutely continuous closed plane curve
with square-integrable derivative, `(b - a) ∫ₐᵇ ‖γ'‖² = 4π |signedArea γ a b|` exactly when `γ`
is constant or traverses a circle once at constant angular speed, in either orientation.

```lean
TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff {a b : ℝ} {γ γ' : ℝ → ℂ}
  (hab : a < b) (hγ : AbsolutelyContinuousOnInterval γ a b)
  (hγ' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt γ (γ' t) t) (hγab : γ a = γ b)
  (hL2 : MeasureTheory.MemLp γ' 2 (MeasureTheory.volume.restrict (Set.Ioc a b))) :
  (b - a) * ∫ (t : ℝ) in a..b, ‖γ' t‖ ^ 2 = 4 * Real.pi * |TauCeti.signedArea γ a b| ↔
    ∃ c w,
      (∀ t ∈ Set.Icc a b, γ t = c + w * Complex.exp (2 * ↑Real.pi * Complex.I * ↑t / (↑b - ↑a))) ∨
        ∀ t ∈ Set.Icc a b, γ t = c + w * Complex.exp (-(2 * ↑Real.pi * Complex.I * ↑t / (↑b - ↑a)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Parseval's energy identity for an absolutely continuous closed complex curve with square-integrable derivative](../../../analysis/part-02/fourier/parsevals-energy-identity-for-an-absolutely-cont.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/AreaEnergy.html#TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/AreaEnergy.html#TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff)
- [Source of `TauCeti.mul_integral_norm_sq_eq_four_pi_mul_abs_signedArea_iff` in TauCeti/Analysis/Fourier/AreaEnergy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/AreaEnergy.lean#L232)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
