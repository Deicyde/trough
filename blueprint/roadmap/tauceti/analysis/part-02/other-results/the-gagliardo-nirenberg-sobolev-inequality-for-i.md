---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable
statement: formalized
proof: formalized
---

# The Gagliardo–Nirenberg–Sobolev inequality for integrable functions

Let `E` have
dimension `n ≥ 2` and let `p = n / (n - 1)`. Every integrable `C¹` function `u` satisfies
`‖u‖_p ≤ C ‖Du‖₁`, with `‖Du‖₁` finite or infinite, where `C` is the constant
`MeasureTheory.eLpNormLESNormFDerivOneConst μ p` of the compactly supported case
`MeasureTheory.eLpNorm_le_eLpNorm_fderiv_one`.

```lean
TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E]
  (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {F : Type u_2} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {u : E → F} (hu : ContDiff ℝ 1 u) (hi : MeasureTheory.Integrable u μ)
  {p : NNReal} (hp : (↑(Module.finrank ℝ E)).HolderConjugate p) :
  MeasureTheory.eLpNorm u (↑p) μ ≤
    ↑(MeasureTheory.eLpNormLESNormFDerivOneConst μ ↑p) * MeasureTheory.eLpNorm (fderiv ℝ u) 1 μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/SobolevInequality.html#TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable).

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/SobolevInequality.html#TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable)
- [Source of `TauCeti.eLpNorm_le_eLpNorm_fderiv_one_of_integrable` in TauCeti/Analysis/FunctionalSpaces/SobolevInequality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/FunctionalSpaces/SobolevInequality.lean#L66)
