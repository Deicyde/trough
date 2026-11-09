---
declaration: theorem
origin: cited
lean: TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure, TauCeti.Probability.bartlett_nonsingularWishartMeasure
statement: formalized
proof: formalized
---

# The Bartlett decomposition of the standard Wishart law

Lift
`TauCeti.Probability.nonsingularWishartMeasure n 1` to the positive-definite cone, where Cholesky
factorization is defined, and read the on-or-below-diagonal entries of the factor: the resulting
law is the product of the Bartlett coordinate laws. Cholesky factorization inverts the Gram map
of `TauCeti.Probability.map_lowerTriangleGram_pi_bartlettCoordinateMeasure`, and the product law
lives on the
positive-diagonal region where that inversion is valid.

```lean
TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure {p : ℕ} {n : ℝ}
  (hn : ↑p - 1 < n) :
  MeasureTheory.Measure.map (TauCeti.choleskyLowerCoordinates p)
      (MeasureTheory.Measure.comap Subtype.val
        (TauCeti.Probability.nonsingularWishartMeasure n 1)) =
    MeasureTheory.Measure.pi (TauCeti.Probability.bartlettCoordinateMeasure n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Wishart/Bartlett.html#TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure).

## Other forms

**The Bartlett decomposition.** Formalized in Tau Ceti as [`TauCeti.Probability.bartlett_nonsingularWishartMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Wishart/Bartlett.html#TauCeti.Probability.bartlett_nonsingularWishartMeasure).

```lean
TauCeti.Probability.bartlett_nonsingularWishartMeasure.{u_1} {p : ℕ} {n : ℝ} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω} (hn : ↑p - 1 < n)
  {A : Ω → TauCeti.PosDefMatrix p}
  (hA :
    ProbabilityTheory.HasLaw A
      (MeasureTheory.Measure.comap Subtype.val (TauCeti.Probability.nonsingularWishartMeasure n 1))
      P) :
  ProbabilityTheory.iIndepFun (fun ij ω => ↑(TauCeti.cholesky (A ω)) (↑ij).1 (↑ij).2) P ∧
    (∀ (i : Fin p),
        ProbabilityTheory.HasLaw (fun ω => ↑(TauCeti.cholesky (A ω)) i i ^ 2)
          (TauCeti.Probability.chiSquaredMeasure (n - ↑↑i)) P) ∧
      ∀ (i j : Fin p),
        j < i →
          ProbabilityTheory.HasLaw (fun ω => ↑(TauCeti.cholesky (A ω)) i j)
            (ProbabilityTheory.gaussianReal 0 1) P
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Wishart/Bartlett.html#TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure)
- [Source of `TauCeti.Probability.map_choleskyLowerCoordinates_comap_nonsingularWishartMeasure` in TauCeti/Probability/Distributions/Wishart/Bartlett.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/Wishart/Bartlett.lean#L415)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
