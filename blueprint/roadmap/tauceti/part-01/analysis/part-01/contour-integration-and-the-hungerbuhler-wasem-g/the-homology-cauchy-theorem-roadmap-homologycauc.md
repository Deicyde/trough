---
declaration: theorem
origin: cited
lean: TauCeti.Contour.homologyCauchyTheorem, TauCeti.Contour.Cycle.homologyCauchyTheorem, TauCeti.Contour.homologyCauchyTheorem_of_point_off_curve
statement: formalized
proof: formalized
---

# The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)

Let `γ` be a
closed piecewise-`C¹` curve on `[[a, b]]`, null-homologous in an open set `Ω` containing it, and
let `f` be holomorphic on `Ω`. Then the contour integral of `f` along `γ` vanishes:
`∫ t in a..b, deriv γ t • f (γ t) = 0`.

Dixon's argument: the piecewise-`C¹` regularity supplies continuity, differentiability off the
finitely many breakpoints, and interval-integrability of `deriv γ` (the `IsPiecewiseC1On` API);
the compact curve image cannot exhaust the open `Ω`, giving a base point `w₀ ∈ Ω` off the curve
(`exists_mem_off_curve`); and `homologyCauchyTheorem_of_point_off_curve` — vanishing of the glued
Dixon function by Liouville, then the Cauchy integral formula at `w₀` — concludes.

```lean
TauCeti.Contour.homologyCauchyTheorem {f : ℂ → ℂ} {Ω : Set ℂ} (hΩ : IsOpen Ω) (γ : ℝ → ℂ) (a b : ℝ)
  (hγ_pc1 : TauCeti.IsPiecewiseC1On γ a b) (hγ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hclosed : γ a = γ b)
  (hf : DifferentiableOn ℂ f Ω) (hnull : TauCeti.Contour.IsNullHomologous γ a b Ω) :
  ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Proof depends on

- [The pointwise homology Cauchy theorem `∮_γ f = 0`](../../part-02/contour/the-pointwise-homology-cauchy-theorem-f-0.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.homologyCauchyTheorem).

## Other forms

**The homology Cauchy theorem for contour cycles.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HomologyCauchy.html#TauCeti.Contour.Cycle.homologyCauchyTheorem).

```lean
TauCeti.Contour.Cycle.homologyCauchyTheorem.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {C : TauCeti.Contour.Cycle} {U : Set ℂ} (hU : IsOpen U)
  (hCU : C.IsIn U) (hf : DifferentiableOn ℂ f U) (hnull : C.IsNullHomologous U) :
  (TauCeti.Contour.Cycle.integral f) C = 0
```

**Homology Cauchy theorem with a supplied off-curve point.** Formalized in Tau Ceti as [`TauCeti.Contour.homologyCauchyTheorem_of_point_off_curve`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.homologyCauchyTheorem_of_point_off_curve).

```lean
TauCeti.Contour.homologyCauchyTheorem_of_point_off_curve {f : ℂ → ℂ} {U : Set ℂ} {γ : ℝ → ℂ}
  {a b : ℝ} {P : Set ℝ} {w₀ : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U)
  (hγ_cont : ContinuousOn γ (Set.uIcc a b)) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hderiv_int : IntervalIntegrable (fun t => deriv γ t) MeasureTheory.volume a b)
  (hclosed : γ a = γ b) (hP : P.Countable)
  (hγ_diff : ∀ t ∈ Set.Ioo (min a b) (max a b) \ P, DifferentiableAt ℝ γ t)
  (h_null : TauCeti.Contour.IsNullHomologous γ a b U) (hw₀U : w₀ ∈ U)
  (hw₀off : ∀ t ∈ Set.uIcc a b, γ t ≠ w₀) : ∫ (t : ℝ) in a..b, deriv γ t • f (γ t) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.homologyCauchyTheorem)
- [Source of `TauCeti.Contour.homologyCauchyTheorem` in TauCeti/Analysis/Contour/HomologyCauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/HomologyCauchy.lean#L98)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ContourIntegration/STATUS.md)
