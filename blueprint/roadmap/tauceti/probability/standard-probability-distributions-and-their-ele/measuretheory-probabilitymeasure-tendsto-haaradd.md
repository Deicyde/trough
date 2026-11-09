---
declaration: theorem
origin: cited
lean: MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff
statement: formalized
proof: formalized
---

# MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff

Circle probability measures tend weakly to Haar probability exactly when every nonzero
integer Fourier moment tends to zero.

```lean
MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff.{u_1} {T : ℝ} [Fact (0 < T)]
  {ι : Type u_1} {L : Filter ι} {μs : ι → MeasureTheory.ProbabilityMeasure (AddCircle T)} :
  Filter.Tendsto μs L (nhds AddCircle.haarAddCircle.toProbabilityMeasure) ↔
    ∀ (n : ℤ),
      n ≠ 0 → Filter.Tendsto (fun i => ∫ (x : AddCircle T), (fourier n) x ∂↑(μs i)) L (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Fourier.html#MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff).

## Sources

- [Tau Ceti documentation: `MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Fourier.html#MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_haarAddCircle_iff` in TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Fourier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Fourier.lean#L89)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
