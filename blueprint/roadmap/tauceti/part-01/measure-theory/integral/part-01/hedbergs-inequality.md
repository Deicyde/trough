---
declaration: theorem
origin: cited
lean: TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow
statement: formalized
proof: formalized
---

# Hedberg's inequality

for `0 < α`, `1 ≤ p` and `α p < n`, the Riesz potential is controlled
pointwise by the Hardy–Littlewood maximal function and the `Lᵖ` norm,

`I_α f (x) ≤ C (M f (x)) ^ (1 - θ) ‖f‖_p ^ θ`, where `θ = α p / n`,

with `C` depending only on `μ`, `α` and `p`.

```lean
TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  [TopologicalSpace F] [ContinuousENorm F] {α : ℝ} [FiniteDimensional ℝ E]
  (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] (hα : 0 < α) {p : NNReal} (hp : 1 ≤ p)
  (hαp : α * ↑p < ↑(Module.finrank ℝ E)) :
  ∃ C,
    ∀ (f : E → F) (x : E),
      TauCeti.rieszPotential μ α f x ≤
        ↑C * TauCeti.maximalFunction μ f x ^ (1 - α * ↑p / ↑(Module.finrank ℝ E)) *
          MeasureTheory.eLpNorm f (↑p) μ ^ (α * ↑p / ↑(Module.finrank ℝ E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszPotential.html#TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszPotential.html#TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow)
- [Source of `TauCeti.exists_rieszPotential_le_mul_maximalFunction_rpow_mul_eLpNorm_rpow` in TauCeti/MeasureTheory/Integral/RieszPotential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/RieszPotential.lean#L759)
