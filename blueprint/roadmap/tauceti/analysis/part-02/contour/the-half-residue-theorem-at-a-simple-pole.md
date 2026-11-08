---
declaration: theorem
origin: cited
lean: TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole
statement: formalized
proof: formalized
---

# The half-residue theorem at a simple pole

the winding-`½` case with the conditions
discharged automatically — an on-cycle simple pole crossed by the immersion contributes
`πi · Res_s f`. The acceptance form for the valence formula's `i` and `ρ`.

```lean
TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
  (γ : ℝ → ℂ) (a b : ℝ) (s : ℂ) (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hsU : s ∈ U)
  (hclosed : γ a = γ b) (hγa : γ a ≠ s) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hf : DifferentiableOn ℂ f (U \ {s})) (hmero : MeromorphicAt f s)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) (h_simple : ↑(-1) ≤ meromorphicOrderAt f s)
  (hwind : TauCeti.Contour.windingNumber γ a b s = 1 / 2) :
  TauCeti.Contour.HasCauchyPV γ a b f (↑Real.pi * Complex.I * TauCeti.Contour.residue f s)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Hungerbühler--Wasem Proposition 2.2 (winding decomposition)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/hungerbuhler-wasem-proposition-2-2-winding-decom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole)
- [Source of `TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole` in TauCeti/Analysis/Contour/HungerbuhlerWasem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/HungerbuhlerWasem.lean#L271)
