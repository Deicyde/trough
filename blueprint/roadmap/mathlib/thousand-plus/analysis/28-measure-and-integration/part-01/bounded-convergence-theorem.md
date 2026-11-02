---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const, MeasureTheory.tendsto_lintegral_nn_filter_of_le_const
mathlib_file: Mathlib/MeasureTheory/Measure/FiniteMeasure.lean
---

# Bounded convergence theorem

Mathlib records this with 2 declarations.

`MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const`: A bounded convergence theorem for a finite measure:
If a sequence of bounded continuous non-negative functions are uniformly bounded by a constant
and tend pointwise to a limit, then their integrals (`MeasureTheory.lintegral`) against the finite
measure tend to the integral of the limit.

A related result with more general assumptions is
`MeasureTheory.tendsto_lintegral_nn_filter_of_le_const`.

```lean
MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const.{u_1} {Ω : Type u_1}
  [MeasurableSpace Ω] [TopologicalSpace Ω] [OpensMeasurableSpace Ω]
  (μ : MeasureTheory.FiniteMeasure Ω) {fs : ℕ → BoundedContinuousFunction Ω NNReal} {c : NNReal}
  (fs_le_const : ∀ (n : ℕ) (ω : Ω), (fs n) ω ≤ c) {f : Ω → NNReal}
  (fs_lim : ∀ (ω : Ω), Filter.Tendsto (fun n => (fs n) ω) Filter.atTop (nhds (f ω))) :
  Filter.Tendsto (fun n => ∫⁻ (ω : Ω), ↑((fs n) ω) ∂↑μ) Filter.atTop (nhds (∫⁻ (ω : Ω), ↑(f ω) ∂↑μ))
```

`MeasureTheory.tendsto_lintegral_nn_filter_of_le_const`: A bounded convergence theorem for a finite measure:
If bounded continuous non-negative functions are uniformly bounded by a constant and tend to a
limit, then their integrals against the finite measure tend to the integral of the limit.
This formulation assumes:
* the functions tend to a limit along a countably generated filter;
* the limit is in the almost everywhere sense;
* boundedness holds almost everywhere;
* integration is `MeasureTheory.lintegral`, i.e., the functions and their integrals are
  `ℝ≥0∞`-valued.

```lean
MeasureTheory.tendsto_lintegral_nn_filter_of_le_const.{u_1, u_2} {Ω : Type u_1} [TopologicalSpace Ω]
  [MeasurableSpace Ω] [OpensMeasurableSpace Ω] {ι : Type u_2} {L : Filter ι}
  [L.IsCountablyGenerated] (μ : MeasureTheory.Measure Ω) [MeasureTheory.IsFiniteMeasure μ]
  {fs : ι → BoundedContinuousFunction Ω NNReal} {c : NNReal}
  (fs_le_const : ∀ᶠ (i : ι) in L, ∀ᵐ (ω : Ω) ∂μ, (fs i) ω ≤ c) {f : Ω → NNReal}
  (fs_lim : ∀ᵐ (ω : Ω) ∂μ, Filter.Tendsto (fun i => (fs i) ω) L (nhds (f ω))) :
  Filter.Tendsto (fun i => ∫⁻ (ω : Ω), ↑((fs i) ω) ∂μ) L (nhds (∫⁻ (ω : Ω), ↑(f ω) ∂μ))
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/FiniteMeasure.html#MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const)
- [Source of `MeasureTheory.FiniteMeasure.tendsto_lintegral_nn_of_le_const` in Mathlib/MeasureTheory/Measure/FiniteMeasure.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/FiniteMeasure.lean#L631)
- [Mathlib documentation: `MeasureTheory.tendsto_lintegral_nn_filter_of_le_const`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/HasOuterApproxClosed.html#MeasureTheory.tendsto_lintegral_nn_filter_of_le_const)
- [Source of `MeasureTheory.tendsto_lintegral_nn_filter_of_le_const` in Mathlib/MeasureTheory/Measure/HasOuterApproxClosed.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/HasOuterApproxClosed.lean#L52)
- [1000+ theorems list: Q1067156X](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1303)
- [1000+ theorems project: Q1067156X](https://1000-plus.github.io/?length=-1#Q1067156X)
- [Wikipedia: Bounded convergence theorem](https://en.wikipedia.org/wiki/Bounded_convergence_theorem)
- [Wikidata: Q1067156](https://www.wikidata.org/wiki/Q1067156)
