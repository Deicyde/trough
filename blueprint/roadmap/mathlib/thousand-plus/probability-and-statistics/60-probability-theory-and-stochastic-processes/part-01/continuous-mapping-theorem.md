---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.TendstoInDistribution.continuous_comp
mathlib_file: Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean
---

# Continuous mapping theorem

**Continuous mapping theorem**: if `X n` tends to `Z` in distribution and `g` is continuous,
then `g ∘ X n` tends to `g ∘ Z` in distribution.

```lean
MeasureTheory.TendstoInDistribution.continuous_comp.{u_1, u_2, u_3, u_5, u_6} {ι : Type u_1}
  {E : Type u_2} {Ω' : Type u_3} {Ω : ι → Type u_5} {m : (i : ι) → MeasurableSpace (Ω i)}
  {μ : (i : ι) → MeasureTheory.Measure (Ω i)} [∀ (i : ι), MeasureTheory.IsProbabilityMeasure (μ i)]
  {m' : MeasurableSpace Ω'} {μ' : MeasureTheory.Measure Ω'} [MeasureTheory.IsProbabilityMeasure μ']
  {mE : MeasurableSpace E} {X : (i : ι) → Ω i → E} {Z : Ω' → E} {l : Filter ι} [TopologicalSpace E]
  {F : Type u_6} [OpensMeasurableSpace E] [TopologicalSpace F] [MeasurableSpace F] [BorelSpace F]
  {g : E → F} (hg : Continuous g) (h : MeasureTheory.TendstoInDistribution X l Z μ μ') :
  MeasureTheory.TendstoInDistribution (fun n => g ∘ X n) l (g ∘ Z) μ μ'
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of inverse functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-inverse-functions.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)
- [Weak-* topology for dualities](../../../../overview/analysis/topological-vector-spaces/weak-topology-for-dualities.md)

## Sources

- [Mathlib documentation: `MeasureTheory.TendstoInDistribution.continuous_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.html#MeasureTheory.TendstoInDistribution.continuous_comp)
- [Source of `MeasureTheory.TendstoInDistribution.continuous_comp` in Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean#L134)
- [1000+ theorems list: Q5165492](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3071)
- [1000+ theorems project: Q5165492](https://1000-plus.github.io/?length=-1#Q5165492)
- [Wikipedia: Continuous mapping theorem](https://en.wikipedia.org/wiki/Continuous_mapping_theorem)
- [Wikidata: Q5165492](https://www.wikidata.org/wiki/Q5165492)
