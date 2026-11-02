---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun
mathlib_file: Mathlib/MeasureTheory/Measure/LevyConvergence.lean
---

# Lévy continuity theorem

The **Lévy convergence theorem**: the weak convergence of probability measures is equivalent
to the pointwise convergence of their characteristic functions.

```lean
MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ₀ : MeasureTheory.ProbabilityMeasure E}
  {μ : ℕ → MeasureTheory.ProbabilityMeasure E} :
  Filter.Tendsto μ Filter.atTop (nhds μ₀) ↔
    ∀ (t : E),
      Filter.Tendsto (fun n => MeasureTheory.charFun (↑(μ n)) t) Filter.atTop
        (nhds (MeasureTheory.charFun (↑μ₀) t))
```

## Depends on

- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Characteristic function](../../../../overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [$C^k$ function](../../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Bounded convergence theorem](../../../analysis/28-measure-and-integration/part-01/bounded-convergence-theorem.md)
- [Cauchy-Schwarz inequality](../../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Change of variable](../../../../undergraduate/single-variable-real-analysis/integration/change-of-variable.md)
- [Completion of an abelian topological group](../../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative of a composition of functions](../../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Dominated convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Dual vector space](../../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Fubini's theorem](../../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Matrix exponential](../../../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Prokhorov's theorem](../../../analysis/28-measure-and-integration/part-01/prokhorovs-theorem.md)
- [Sequential space](../../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Stone-Weierstrass theorem](../../../../overview/topology/general-topology/part-02/stone-weierstrass-theorem.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/LevyConvergence.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun` in Mathlib/MeasureTheory/Measure/LevyConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/LevyConvergence.lean#L212)
- [1000+ theorems list: Q1966978](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1958)
- [1000+ theorems project: Q1966978](https://1000-plus.github.io/?length=-1#Q1966978)
- [Wikipedia: Lévy continuity theorem](https://en.wikipedia.org/wiki/L%C3%A9vy_continuity_theorem)
- [Wikidata: Q1966978](https://www.wikidata.org/wiki/Q1966978)
