---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le, TauCeti.exists_eLpNorm_rieszPotential_le
statement: formalized
proof: formalized
---

# The Hardy–Littlewood–Sobolev inequality

**The Hardy–Littlewood–Sobolev inequality** for the Bochner integral
`∫ ‖x - y‖ ^ (α - n) • f y dμ(y)` of a function with values in a real normed space: for `0 < α`,
`1 < p` and `1 / q = 1 / p - α / n`, there is `C`, depending only on `μ`, `α` and `p`, with
`‖∫ ‖· - y‖ ^ (α - n) • f y dμ(y)‖_q ≤ C ‖f‖_p`.

```lean
TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le.{u_1, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] {α : ℝ} {G : Type u_3}
  [NormedAddCommGroup G] [NormedSpace ℝ G] [FiniteDimensional ℝ E] (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] (hα : 0 < α) {p q : NNReal} (hp : 1 < p)
  (hpq : (↑q)⁻¹ = (↑p)⁻¹ - α / ↑(Module.finrank ℝ E)) :
  ∃ C,
    ∀ (f : E → G),
      MeasureTheory.eLpNorm (fun x => ∫ (y : E), ‖x - y‖ ^ (α - ↑(Module.finrank ℝ E)) • f y ∂μ)
          (↑q) μ ≤
        ↑C * MeasureTheory.eLpNorm f (↑p) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hardy–Littlewood maximal inequality](the-hardy-littlewood-maximal-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszPotential.html#TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le).

## Other forms

**The Hardy–Littlewood–Sobolev inequality.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_rieszPotential_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszPotential.html#TauCeti.exists_eLpNorm_rieszPotential_le).

```lean
TauCeti.exists_eLpNorm_rieszPotential_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [TopologicalSpace F]
  [ContinuousENorm F] {α : ℝ} [FiniteDimensional ℝ E] (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] (hα : 0 < α) {p q : NNReal} (hp : 1 < p)
  (hpq : (↑q)⁻¹ = (↑p)⁻¹ - α / ↑(Module.finrank ℝ E)) :
  ∃ C,
    ∀ (f : E → F),
      MeasureTheory.eLpNorm (TauCeti.rieszPotential μ α f) (↑q) μ ≤
        ↑C * MeasureTheory.eLpNorm f (↑p) μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszPotential.html#TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le)
- [Source of `TauCeti.exists_eLpNorm_integral_norm_sub_rpow_smul_le` in TauCeti/MeasureTheory/Integral/RieszPotential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/RieszPotential.lean#L915)
