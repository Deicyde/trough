---
declaration: theorem
origin: cited
lean: ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure
statement: formalized
proof: formalized
---

# ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure

The partial correlations of a random matrix with LKJ law are jointly independent.

```lean
ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure.{u_1} {Ω : Type u_1}
  [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} {p : ℕ} {η : ℝ}
  {X : Ω → ↥(selfAdjoint.submodule ℝ (Matrix (Fin p) (Fin p) ℝ))}
  (hX : ProbabilityTheory.HasLaw X (TauCeti.Probability.lkjMeasure p η) P) (hη : 0 < η) :
  ProbabilityTheory.iIndepFun
    (fun ij ω =>
      TauCeti.partialCorrelationOfCorrelationCoordinates ((TauCeti.correlationCoordinates p) (X ω))
        ij)
    P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Change of variables to partial correlations](change-of-variables-to-partial-correlations.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/LKJ/PartialCorrelation.html#ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/LKJ/PartialCorrelation.html#ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure)
- [Source of `ProbabilityTheory.HasLaw.iIndepFun_partialCorrelation_lkjMeasure` in TauCeti/Probability/Distributions/LKJ/PartialCorrelation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/LKJ/PartialCorrelation.lean#L266)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
