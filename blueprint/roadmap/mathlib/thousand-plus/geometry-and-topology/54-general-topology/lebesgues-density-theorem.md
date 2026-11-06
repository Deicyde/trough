# Lebesgue's density theorem

Given an arbitrary set `s`, then `μ (s ∩ closedBall x r) / μ (closedBall x r)` converges
to `1` when `r` tends to `0`, for almost every `x` in `s`.
This shows that almost every point of `s` is a Lebesgue density point for `s`.
A stronger version holds for measurable sets, see `ae_tendsto_measure_inter_div_of_measurableSet`.

See also `IsUnifLocDoublingMeasure.ae_tendsto_measure_inter_div`.

```lean
Besicovitch.ae_tendsto_measure_inter_div.{u} {β : Type u} [MetricSpace β] [MeasurableSpace β]
  [BorelSpace β] [SecondCountableTopology β] [HasBesicovitchCovering β]
  (μ : MeasureTheory.Measure β) [MeasureTheory.IsLocallyFiniteMeasure μ] (s : Set β) :
  ∀ᵐ (x : β) ∂μ.restrict s,
    Filter.Tendsto (fun r => μ (s ∩ Metric.closedBall x r) / μ (Metric.closedBall x r))
      (nhdsWithin 0 (Set.Ioi 0)) (nhds 1)
```

## Depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Positive measure](../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Lebesgue's decomposition theorem](lebesgues-decomposition-theorem.md)

## Sources

- [Mathlib documentation: `Besicovitch.ae_tendsto_measure_inter_div`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Covering/Besicovitch.html#Besicovitch.ae_tendsto_measure_inter_div)
- [Source of `Besicovitch.ae_tendsto_measure_inter_div` in Mathlib/MeasureTheory/Covering/Besicovitch.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Covering/Besicovitch.lean#L1098)
- [1000+ theorems list: Q842953](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L942)
- [1000+ theorems project: Q842953](https://1000-plus.github.io/all.html?length=-1#Q842953)
- [Wikipedia: Lebesgue's density theorem](https://en.wikipedia.org/wiki/Lebesgue's_density_theorem)
- [Wikidata: Q842953](https://www.wikidata.org/wiki/Q842953)
