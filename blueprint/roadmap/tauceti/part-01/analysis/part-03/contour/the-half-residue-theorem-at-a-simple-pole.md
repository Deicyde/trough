---
declaration: theorem
origin: cited
lean: TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole
statement: formalized
proof: formalized
---

# The half-residue theorem at a simple pole

the `S = {s}`, winding-`½` specialization of
`hungerbuhlerWasem_residueTheorem_of_simple_poles`, with conditions (A′) and (B) discharged
automatically. Since `f` is differentiable on `U ∖ {s}`, the point `s`, at worst a simple pole, is
the only singularity of `f` in `U`, and the principal value is `πi · Res_s f`, for example when `γ`
is the boundary of a half-disc and `s` an interior point of its diameter. With several
singularities, such as the poles of a logarithmic derivative in the argument principle or the
valence formula, use `hungerbuhlerWasem_residueTheorem_of_simple_poles`, where each pole with
winding number `½` contributes the summand `πi · Res_s f`.

```lean
TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
  (γ : ℝ → ℂ) (a b : ℝ) (s : ℂ) (hγ_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b)
  (hclosed : γ a = γ b) (hγa : γ a ≠ s) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U)
  (hf : DifferentiableOn ℂ f (U \ {s})) (hmero : s ∈ U → MeromorphicAt f s)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (h_simple : s ∈ U → ↑(-1) ≤ meromorphicOrderAt f s)
  (hwind : TauCeti.Contour.windingNumber γ a b s = 1 / 2) :
  TauCeti.Contour.HasCauchyPV γ a b f (↑Real.pi * Complex.I * TauCeti.Contour.residue f s)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [The Hungerbühler–Wasem generalized residue theorem for a contour cycle (HW Thm 3.3)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-hungerbuhler-wasem-generalized-residue-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/HungerbuhlerWasem.html#TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole)
- [Source of `TauCeti.Contour.hasCauchyPV_half_residue_of_simple_pole` in TauCeti/Analysis/Contour/HungerbuhlerWasem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/HungerbuhlerWasem.lean#L284)
