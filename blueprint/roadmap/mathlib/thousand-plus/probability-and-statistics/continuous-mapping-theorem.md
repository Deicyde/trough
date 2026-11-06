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

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Continuous function](../../overview/topology/general-topology/part-01/continuous-function.md)
- [Linear map](../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.TendstoInDistribution.continuous_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.html#MeasureTheory.TendstoInDistribution.continuous_comp)
- [Source of `MeasureTheory.TendstoInDistribution.continuous_comp` in Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean#L134)
- [1000+ theorems list: Q5165492](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3071)
- [1000+ theorems project: Q5165492](https://1000-plus.github.io/all.html?length=-1#Q5165492)
- [Wikipedia: Continuous mapping theorem](https://en.wikipedia.org/wiki/Continuous_mapping_theorem)
- [Wikidata: Q5165492](https://www.wikidata.org/wiki/Q5165492)
