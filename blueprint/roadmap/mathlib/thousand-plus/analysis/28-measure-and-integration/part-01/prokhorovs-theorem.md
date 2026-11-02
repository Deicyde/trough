---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le, isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le, isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le, isCompact_closure_of_isTightMeasureSet
mathlib_file: Mathlib/MeasureTheory/Measure/Prokhorov.lean
---

# Prokhorov's theorem

Mathlib records this with 4 declarations.

`isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le`: **Prokhorov theorem**: Given a sequence of compact sets `Kₙ` and a sequence `uₙ` tending
to zero, the finite measures of mass at most `C` giving mass at most `uₙ` to the complement of `Kₙ`
form a compact set.

```lean
isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [TopologicalSpace E] [T2Space E] [BorelSpace E] {u : ℕ → NNReal}
  {K : ℕ → Set E} (C : NNReal) (hu : Filter.Tendsto u Filter.atTop (nhds 0))
  (hK : ∀ (n : ℕ), IsCompact (K n)) (h : NormalSpace E ∨ Monotone K) :
  IsCompact {μ | μ.mass ≤ C ∧ ∀ (n : ℕ), μ (K n)ᶜ ≤ u n}
```

`isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le`: **Prokhorov theorem**: Given a sequence of compact sets `Kₙ` and a sequence `uₙ` tending to
zero, the finite measures of mass `C` giving mass at most `uₙ` to the complement of `Kₙ` form a
compact set.

```lean
isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [TopologicalSpace E] [T2Space E] [BorelSpace E] {u : ℕ → NNReal}
  {K : ℕ → Set E} (C : NNReal) (hu : Filter.Tendsto u Filter.atTop (nhds 0))
  (hK : ∀ (n : ℕ), IsCompact (K n)) (h : NormalSpace E ∨ Monotone K) :
  IsCompact {μ | μ.mass = C ∧ ∀ (n : ℕ), μ (K n)ᶜ ≤ u n}
```

`isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le`: **Prokhorov theorem**: Given a sequence of compact sets `Kₙ` and a sequence `uₙ` tending to
zero, the probability measures giving mass at most `uₙ` to the complement of `Kₙ` form a
compact set.

```lean
isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [TopologicalSpace E] [T2Space E] [BorelSpace E] {u : ℕ → NNReal}
  {K : ℕ → Set E} (hu : Filter.Tendsto u Filter.atTop (nhds 0)) (hK : ∀ (n : ℕ), IsCompact (K n))
  (h : NormalSpace E ∨ Monotone K) : IsCompact {μ | ∀ (n : ℕ), μ (K n)ᶜ ≤ u n}
```

`isCompact_closure_of_isTightMeasureSet`: **Prokhorov theorem**: the closure of a tight set of probability measures is compact.
We only require the space to be T2.

```lean
isCompact_closure_of_isTightMeasureSet.{u_1} {E : Type u_1} [MeasurableSpace E] [TopologicalSpace E]
  [T2Space E] [BorelSpace E] {S : Set (MeasureTheory.ProbabilityMeasure E)}
  (hS : MeasureTheory.IsTightMeasureSet {x | ∃ μ ∈ S, ↑μ = x}) : IsCompact (closure S)
```

## Depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Characteristic p](../../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Fatou's lemma](../../../../overview/analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Heine-Borel theorem (proper metric space version)](../../../../overview/topology/metric-spaces/heine-borel-theorem-proper-metric-space-version.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Monotone convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Urysohn's lemma](../../../../overview/topology/general-topology/part-02/urysohns-lemma.md)
- [Weak-* topology for dualities](../../../../overview/analysis/topological-vector-spaces/weak-topology-for-dualities.md)

## Sources

- [Mathlib documentation: `isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Prokhorov.html#isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le)
- [Source of `isCompact_setOfPred_finiteMeasure_mass_le_compl_isCompact_le` in Mathlib/MeasureTheory/Measure/Prokhorov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Prokhorov.lean#L221)
- [Mathlib documentation: `isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Prokhorov.html#isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le)
- [Source of `isCompact_setOfPred_finiteMeasure_mass_eq_compl_isCompact_le` in Mathlib/MeasureTheory/Measure/Prokhorov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Prokhorov.lean#L484)
- [Mathlib documentation: `isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Prokhorov.html#isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le)
- [Source of `isCompact_setOfPred_probabilityMeasure_mass_eq_compl_isCompact_le` in Mathlib/MeasureTheory/Measure/Prokhorov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Prokhorov.lean#L502)
- [Mathlib documentation: `isCompact_closure_of_isTightMeasureSet`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Prokhorov.html#isCompact_closure_of_isTightMeasureSet)
- [Source of `isCompact_closure_of_isTightMeasureSet` in Mathlib/MeasureTheory/Measure/Prokhorov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Prokhorov.lean#L528)
- [1000+ theorems list: Q7249519](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3684)
- [1000+ theorems project: Q7249519](https://1000-plus.github.io/?length=-1#Q7249519)
- [Wikipedia: Prokhorov's theorem](https://en.wikipedia.org/wiki/Prokhorov's_theorem)
- [Wikidata: Q7249519](https://www.wikidata.org/wiki/Q7249519)
