---
declaration: theorem
origin: cited
lean: TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous
statement: formalized
proof: formalized
---

# Null-homologous Cauchy integral formula at an off-curve point

Let `γ` be a closed curve in
an open set `U`, continuous on `uIcc a b`, differentiable off a countable set, with
interval-integrable derivative, and null-homologous in `U`. If `f` is holomorphic on `U` and
`w ∈ U` is not on the curve, then the Cauchy-type integral evaluates to
`2πi · windingNumber γ a b w · f w`.

This is the Cauchy-integral-formula output of Dixon's vanishing theorem. The off-curve point is
kept as an explicit hypothesis; proving that such a point exists in the ambient domain is a separate
geometric prerequisite for the full global homology Cauchy theorem.

```lean
TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous {f : ℂ → ℂ} {U : Set ℂ} {γ : ℝ → ℂ}
  {a b : ℝ} {P : Set ℝ} {w : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U)
  (hγ_cont : ContinuousOn γ (Set.uIcc a b)) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hderiv_int : IntervalIntegrable (fun t => deriv γ t) MeasureTheory.volume a b)
  (hclosed : γ a = γ b) (hP : P.Countable)
  (hγ_diff : ∀ t ∈ Set.Ioo (min a b) (max a b) \ P, DifferentiableAt ℝ γ t)
  (h_null : TauCeti.Contour.IsNullHomologous γ a b U) (hwU : w ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ w) :
  TauCeti.Contour.dixonH2 f γ a b w =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b w * f w
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Cauchy's integral formula for the `k`-th derivative, homology form](cauchys-integral-formula-for-the-k-th-derivative.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous)
- [Source of `TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_nullHomologous` in TauCeti/Analysis/Contour/HomologyCauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/HomologyCauchy.lean#L51)
