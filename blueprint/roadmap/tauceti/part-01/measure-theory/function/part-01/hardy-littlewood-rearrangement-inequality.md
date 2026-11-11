---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul
statement: formalized
proof: formalized
---

# Hardy--Littlewood rearrangement inequality

For two nonnegative a.e.-measurable
functions on a finite-dimensional real normed space, Schwarz rearrangement can only increase the
integral of their product. The statement includes infinite integrals and dimension zero.

```lean
TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  [FiniteDimensional ℝ E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {f g : E → ENNReal}
  (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) :
  ∫⁻ (x : E), f x * g x ∂μ ≤
    ∫⁻ (x : E), TauCeti.schwarzRearrangement μ f x * TauCeti.schwarzRearrangement μ g x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/SchwarzRearrangement.html#TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/SchwarzRearrangement.html#TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul)
- [Source of `TauCeti.lintegral_mul_le_lintegral_schwarzRearrangement_mul` in TauCeti/MeasureTheory/Function/SchwarzRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/SchwarzRearrangement.lean#L406)
