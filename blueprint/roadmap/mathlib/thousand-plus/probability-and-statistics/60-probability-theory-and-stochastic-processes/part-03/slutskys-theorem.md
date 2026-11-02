---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.TendstoInDistribution.continuous_comp_prodMk_of_tendstoInMeasure_const
mathlib_file: Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean
---

# Slutsky's theorem

**Slutsky's theorem** for a continuous function: if `X n` converges in distribution to `Z`,
`Y n` converges in probability to a constant `c`, and `g` is a continuous function, then
`g (X n, Y n)` converges in distribution to `g (Z, c)`.

```lean
MeasureTheory.TendstoInDistribution.continuous_comp_prodMk_of_tendstoInMeasure_const.{u_1, u_2, u_3,
    u_4, u_6, u_7}
  {ι : Type u_1} {E : Type u_2} {Ω' : Type u_3} {Ω'' : Type u_4} {m' : MeasurableSpace Ω'}
  {μ' : MeasureTheory.Measure Ω'} [MeasureTheory.IsProbabilityMeasure μ']
  {m'' : MeasurableSpace Ω''} {μ'' : MeasureTheory.Measure Ω''}
  [MeasureTheory.IsProbabilityMeasure μ''] {mE : MeasurableSpace E} {Z : Ω' → E} {l : Filter ι}
  [SeminormedAddCommGroup E] [SecondCountableTopology E] [BorelSpace E] {E' : Type u_6}
  {F : Type u_7} {mE' : MeasurableSpace E'} [SeminormedAddCommGroup E'] [SecondCountableTopology E']
  [BorelSpace E'] [TopologicalSpace F] [MeasurableSpace F] [BorelSpace F] {g : E × E' → F}
  (hg : Continuous g) [l.IsCountablyGenerated] {X : ι → Ω'' → E} {Y : ι → Ω'' → E'} {c : E'}
  (hXZ : MeasureTheory.TendstoInDistribution X l Z (fun x => μ'') μ')
  (hY_tendsto : MeasureTheory.TendstoInMeasure μ'' Y l fun x => c)
  (hY : ∀ (i : ι), AEMeasurable (Y i) μ'') :
  MeasureTheory.TendstoInDistribution (fun n ω => g (X n ω, Y n ω)) l (fun ω => g (Z ω, c))
    (fun x => μ'') μ'
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Carathéodory's theorem (measure theory)](../../../analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Convergence in probability](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/convergence-in-probability.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order (Real numbers)](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuous mapping theorem](../part-01/continuous-mapping-theorem.md)
- [Convergence in distribution](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/convergence-in-distribution.md)
- [Fatou's lemma](../../../../overview/analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.TendstoInDistribution.continuous_comp_prodMk_of_tendstoInMeasure_const`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.html#MeasureTheory.TendstoInDistribution.continuous_comp_prodMk_of_tendstoInMeasure_const)
- [Source of `MeasureTheory.TendstoInDistribution.continuous_comp_prodMk_of_tendstoInMeasure_const` in Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/ConvergenceInDistribution.lean#L326)
- [1000+ theorems list: Q643826](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L664)
- [1000+ theorems project: Q643826](https://1000-plus.github.io/all.html?length=-1#Q643826)
- [Wikipedia: Slutsky's theorem](https://en.wikipedia.org/wiki/Slutsky's_theorem)
- [Wikidata: Q643826](https://www.wikidata.org/wiki/Q643826)
