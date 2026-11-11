---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt
statement: formalized
proof: formalized
---

# TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt

A cut-norm defect larger than `ε` produces a measurable common refinement with at most four
times as many parts and graphon partition energy **more than** `ε²` larger.

```lean
TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  (μ : MeasureTheory.Measure Ω) [MeasureTheory.IsProbabilityMeasure μ] (P : Finpartition Set.univ)
  (hP : ∀ p ∈ P.parts, MeasurableSet p) (W : TauCeti.DenseGraphLimits.Graphon Ω μ) {ε : ℝ}
  (hε : 0 ≤ ε)
  (hbad :
    ε <
      TauCeti.DenseGraphLimits.cutNorm μ
        (W.toSymmKernel - (TauCeti.DenseGraphLimits.stepGraphonAvg P hP W).toSymmKernel)) :
  ∃ Q,
    ∃ (hQ : ∀ q ∈ Q.parts, MeasurableSet q),
      Q ≤ P ∧
        Q.parts.card ≤ 4 * P.parts.card ∧
          TauCeti.DenseGraphLimits.graphonPartitionEnergy μ P hP W + ε ^ 2 <
            TauCeti.DenseGraphLimits.graphonPartitionEnergy μ Q hQ W
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt)
- [Source of `TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt` in TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean#L61)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
