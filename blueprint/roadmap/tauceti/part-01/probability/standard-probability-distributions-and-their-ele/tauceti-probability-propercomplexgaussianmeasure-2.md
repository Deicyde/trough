---
declaration: theorem
origin: cited
lean: TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity
statement: formalized
proof: formalized
---

# TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity

A proper complex Gaussian at positive-definite covariance has the Hermitian
quadratic-form density relative to real product Lebesgue measure.

```lean
TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {C : Matrix ι ι ℂ} (m : ι → ℂ) (hC : C.PosDef) :
  TauCeti.Probability.properComplexGaussianMeasure m C =
    MeasureTheory.volume.withDensity (TauCeti.Probability.properComplexGaussianPDF m C)
```

## Depends on

- [TauCeti.Probability.properComplexGaussianMeasure](tauceti-probability-propercomplexgaussianmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/PDF.html#TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/PDF.html#TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity)
- [Source of `TauCeti.Probability.properComplexGaussianMeasure_eq_withDensity` in TauCeti/Probability/Distributions/Gaussian/ProperComplex/PDF.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/ProperComplex/PDF.lean#L184)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
