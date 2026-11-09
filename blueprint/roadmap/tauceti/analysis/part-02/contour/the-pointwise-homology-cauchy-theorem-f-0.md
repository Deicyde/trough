---
declaration: theorem
origin: cited
lean: TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero
statement: formalized
proof: formalized
---

# The pointwise homology Cauchy theorem `∮_γ f = 0`

Applying the Cauchy integral formula to
the twist `g z = (z - w₀) · f z`, which satisfies `g w₀ = 0`, forces `dixonH2 g γ a b w₀ = 0`; and
since `g (γ t) / (γ t - w₀) = f (γ t)` for `γ` off `w₀`, that Cauchy-type integral is the contour
integral of `f`. Hence `∫ t in a..b, deriv γ t • f (γ t) = 0`, given the pointwise vanishing
`dixonFunction (fun z ↦ (z - w₀) * f z) U γ a b w₀ = 0`, interval-integrability of the contour
integrand `deriv γ • f ∘ γ`, and of the index integrand. Discharging the vanishing via
`dixonFunction_eq_zero` yields the roadmap `homologyCauchyTheorem`.

```lean
TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero {f : ℂ → ℂ} {U : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} (h_cont : ContinuousOn γ (Set.uIcc a b)) (w₀ : ℂ) (hw₀_in_U : w₀ ∈ U)
  (hw₀_off : ∀ t ∈ Set.uIcc a b, γ t ≠ w₀)
  (h_zero_at : TauCeti.Contour.dixonFunction (fun z => (z - w₀) * f z) U γ a b w₀ = 0)
  (h_int : IntervalIntegrable (fun t => deriv γ t • f (γ t)) MeasureTheory.volume a b)
  (h_base_int : IntervalIntegrable (fun t => (γ t - w₀)⁻¹ * deriv γ t) MeasureTheory.volume a b) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy's integral formula for the `k`-th derivative, homology form](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/cauchys-integral-formula-for-the-k-th-derivative.md)
- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/IntegralFormula.html#TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/IntegralFormula.html#TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero)
- [Source of `TauCeti.Contour.intervalIntegral_deriv_smul_eq_zero_of_dixonFunction_eq_zero` in TauCeti/Analysis/Contour/Cauchy/IntegralFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cauchy/IntegralFormula.lean#L69)
