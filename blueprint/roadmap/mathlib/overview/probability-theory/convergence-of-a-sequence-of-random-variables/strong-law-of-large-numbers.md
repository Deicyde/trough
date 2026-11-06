# Strong law of large numbers

**Strong law of large numbers**, almost sure version: if `X n` is a sequence of independent
identically distributed integrable random variables taking values in a Banach space,
then `n⁻¹ • ∑ i ∈ range n, X i` converges almost surely to `𝔼[X 0]`. We give here the strong
version, due to Etemadi, that only requires pairwise independence.

```lean
ProbabilityTheory.strong_law_ae.{u_1, u_2} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [MeasurableSpace E] [BorelSpace E] (X : ℕ → Ω → E)
  (hint : MeasureTheory.Integrable (X 0) μ)
  (hindep : Pairwise (Function.onFun (fun x1 x2 => ProbabilityTheory.IndepFun x1 x2 μ) X))
  (hident : ∀ (i : ℕ), ProbabilityTheory.IdentDistrib (X i) (X 0) μ μ) :
  ∀ᵐ (ω : Ω) ∂μ,
    Filter.Tendsto (fun n => (↑n)⁻¹ • ∑ i ∈ Finset.range n, X i ω) Filter.atTop
      (nhds (∫ (x : Ω), X 0 x ∂μ))
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Approximation by step functions](../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Borel-Cantelli lemma (easy direction)](../../../undergraduate/probability-theory/definitions-of-a-probability-space/borel-cantelli-lemma-easy-direction.md)
- [Chebyshev inequality](chebyshev-inequality.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.strong_law_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/StrongLaw.html#ProbabilityTheory.strong_law_ae)
- [Source of `ProbabilityTheory.strong_law_ae` in Mathlib/Probability/StrongLaw.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/StrongLaw.lean#L783)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L420)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L584)
- [Freek Wiedijk's 100 theorems, no. 59](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L303)
