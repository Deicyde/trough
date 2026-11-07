---
declaration: theorem
origin: cited
lean: TauCeti.Contour.homologyCauchyTheorem
statement: formalized
proof: formalized
---

# The homology Cauchy theorem

(roadmap `homologyCauchyTheorem`, Layer 3). Let `γ` be a
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

- [Generalized winding number](generalized-winding-number.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.homologyCauchyTheorem).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HomologyCauchy.html#TauCeti.Contour.homologyCauchyTheorem)
- [Source of `TauCeti.Contour.homologyCauchyTheorem` in TauCeti/Analysis/Contour/HomologyCauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/HomologyCauchy.lean#L98)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
