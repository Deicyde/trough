---
declaration: theorem
origin: cited
lean: TauCeti.Probability.condDistrib_multivariateGaussian
statement: formalized
proof: formalized
---

# TauCeti.Probability.condDistrib_multivariateGaussian

For a jointly Gaussian vector with positive-semidefinite covariance, the regular conditional
law of the first block given the second is Gaussian with the generalized Schur complement and
pseudoinverse regression mean. Singular observed blocks and Dirac conditional laws are included.

```lean
TauCeti.Probability.condDistrib_multivariateGaussian.{u_3, u_4, u_5} {ι : Type u_3} {κ : Type u_4}
  [Fintype ι] [Fintype κ] [DecidableEq ι] [DecidableEq κ] {Ω : Type u_5} [MeasurableSpace Ω]
  {P : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure P] (X : Ω → EuclideanSpace ℝ (ι ⊕ κ))
  (m : EuclideanSpace ℝ (ι ⊕ κ)) {S : Matrix (ι ⊕ κ) (ι ⊕ κ) ℝ}
  (hX : ProbabilityTheory.HasLaw X (ProbabilityTheory.multivariateGaussian m S) P)
  (hS : S.PosSemidef) :
  ⇑(ProbabilityTheory.condDistrib (fun ω => (EuclideanSpace.sumEquivProd (X ω)).1)
        (fun ω => (EuclideanSpace.sumEquivProd (X ω)).2)
        P) =ᵐ[MeasureTheory.Measure.map (fun ω => (EuclideanSpace.sumEquivProd (X ω)).2) P]
    ⇑(m.gaussianCondKernel S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.condDistrib_multivariateGaussian`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Conditional/Basic.html#TauCeti.Probability.condDistrib_multivariateGaussian).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.condDistrib_multivariateGaussian`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Conditional/Basic.html#TauCeti.Probability.condDistrib_multivariateGaussian)
- [Source of `TauCeti.Probability.condDistrib_multivariateGaussian` in TauCeti/Probability/Distributions/Gaussian/Conditional/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Conditional/Basic.lean#L534)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
