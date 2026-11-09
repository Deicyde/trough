---
declaration: theorem
origin: cited
lean: TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral
statement: formalized
proof: formalized
---

# TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral

The sum of squares of independent unit-variance Gaussian coordinates has noncentral
chi-squared law, including the empty family.

```lean
TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral.{u_1} {ι : Type u_1} [Fintype ι]
  (m : ι → ℝ) :
  MeasureTheory.Measure.map (fun x => ∑ i, x i ^ 2)
      (MeasureTheory.Measure.pi fun i => ProbabilityTheory.gaussianReal (m i) 1) =
    TauCeti.Probability.noncentralChiSquaredMeasure (↑(Fintype.card ι)) (∑ i, ‖m i‖₊ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/NoncentralChiSquared/Gaussian.html#TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/NoncentralChiSquared/Gaussian.html#TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral)
- [Source of `TauCeti.Probability.map_sum_sq_pi_gaussianReal_noncentral` in TauCeti/Probability/Distributions/NoncentralChiSquared/Gaussian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/NoncentralChiSquared/Gaussian.lean#L44)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
