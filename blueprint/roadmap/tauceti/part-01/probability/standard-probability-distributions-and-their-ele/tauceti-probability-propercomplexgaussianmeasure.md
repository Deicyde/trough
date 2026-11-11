---
declaration: def
origin: cited
lean: TauCeti.Probability.properComplexGaussianMeasure
statement: formalized
---

# TauCeti.Probability.properComplexGaussianMeasure

The proper complex Gaussian law with mean `m` and covariance `C`. For a covariance
that is not Hermitian positive semidefinite, it is the Dirac law at `m`.

```lean
TauCeti.Probability.properComplexGaussianMeasure.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  (m : ι → ℂ) (C : Matrix ι ι ℂ) : MeasureTheory.Measure (ι → ℂ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.properComplexGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/Basic.html#TauCeti.Probability.properComplexGaussianMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.properComplexGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/ProperComplex/Basic.html#TauCeti.Probability.properComplexGaussianMeasure)
- [Source of `TauCeti.Probability.properComplexGaussianMeasure` in TauCeti/Probability/Distributions/Gaussian/ProperComplex/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/ProperComplex/Basic.lean#L115)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
