---
declaration: theorem
origin: cited
lean: TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous
statement: formalized
proof: formalized
---

# Cauchy's integral formula for the `k`-th derivative, homology form

Let `f` be holomorphic
on an open `U`, let `γ` be a closed piecewise-`C¹` curve in `U` that is null-homologous there, and
let `z ∈ U` lie off the curve. Then for every `k`,

`∫ t in a..b, γ' t • (f (γ t) / (γ t − z) ^ (k + 1)) = 2πi · n_z(γ) · f⁽ᵏ⁾(z) / k !`,

the `k`-th Taylor coefficient of `f` at `z` weighted by the generalized winding number of `γ` about
`z`. Only the residue at `z` contributes: the residue theorem for a null-homologous cycle applied
to the Cauchy kernel `w ↦ f w / (w − z) ^ (k + 1)`, whose only possible singularity in `U` is at
`z`, leaves the single residue `iteratedDeriv k f z / k !`.

```lean
TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous {f : ℂ → ℂ} {U : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} {z : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) (hz : z ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) (k : ℕ) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z) ^ (k + 1)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z *
      (iteratedDeriv k f z / ↑k.factorial)
```

## Depends on

- [Generalized winding number](generalized-winding-number.md)

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](the-classical-residue-theorem-for-a-null-homolog.md)
- [The residue of the Cauchy kernel](the-residue-of-the-cauchy-kernel.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous)
- [Source of `TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous` in TauCeti/Analysis/Contour/Cauchy/HomologyFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.lean#L71)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
