---
declaration: theorem
origin: cited
lean: TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue
statement: formalized
proof: formalized
---

# The residue theorem for a fixed polar-part decomposition

Once `f` is presented on `U` as
an analytic remainder plus finite Laurent tails at the points of `S`, a closed null-homologous
piecewise-`C¹` curve in `U` avoiding `S` integrates to the winding-weighted residue sum. This is
the sum of the two preceding facts: the remainder contributes nothing
(`intervalIntegral_deriv_smul_analyticRemainder_eq_zero`) and the tails contribute the residue sum
(`intervalIntegral_deriv_smul_eq_analyticRemainder_add_sum`).

```lean
TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue
  {f : ℂ → ℂ} {S : Finset ℂ} {U : Set ℂ} (decomp : TauCeti.Contour.PolarPartDecomposition f S U)
  (hU : IsOpen U) {γ : ℝ → ℂ} {a b : ℝ} (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b) (hoff : ∀ t ∈ Set.uIcc a b, γ t ∉ ↑S)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, TauCeti.Contour.windingNumber γ a b s * TauCeti.Contour.residue f s
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](the-homology-cauchy-theorem-roadmap-homologycauc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Cycle.html#TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Cycle.html#TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue)
- [Source of `TauCeti.Contour.PolarPartDecomposition.intervalIntegral_deriv_smul_eq_sum_windingNumber_mul_residue` in TauCeti/Analysis/Contour/Residue/Cycle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/Residue/Cycle.lean#L191)
