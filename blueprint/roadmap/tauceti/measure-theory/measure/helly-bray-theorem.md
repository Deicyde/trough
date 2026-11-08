---
declaration: theorem
origin: cited
lean: MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf
statement: formalized
proof: formalized
---

# Helly–Bray theorem

Along a countably generated filter, probability measures on `ℝ`
converge weakly if and only if their cumulative distribution functions converge pointwise at every
continuity point of the limiting cumulative distribution function.

```lean
MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf.{u_1} {ι : Type u_1}
  {l : Filter ι} {μs : ι → MeasureTheory.ProbabilityMeasure ℝ}
  {μ : MeasureTheory.ProbabilityMeasure ℝ} [l.IsCountablyGenerated] :
  Filter.Tendsto μs l (nhds μ) ↔
    ∀ (x : ℝ),
      ContinuousAt (↑(ProbabilityTheory.cdf ↑μ)) x →
        Filter.Tendsto (fun i => ↑(ProbabilityTheory.cdf ↑(μs i)) x) l
          (nhds (↑(ProbabilityTheory.cdf ↑μ) x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Cdf.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf).

## Sources

- [Tau Ceti documentation: `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Cdf.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_continuousAt_tendsto_cdf` in TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Cdf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/ProbabilityMeasure/Cdf.lean#L105)
