# Fernique's theorem

**Fernique's theorem**: for a Gaussian measure, there exists `C > 0` such that the function
`x ↦ exp (C * ‖x‖ ^ 2)` is integrable.

```lean
ProbabilityTheory.IsGaussian.exists_integrable_exp_sq.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [SecondCountableTopology E] [CompleteSpace E]
  (μ : MeasureTheory.Measure E) [ProbabilityTheory.IsGaussian μ] :
  ∃ C, 0 < C ∧ MeasureTheory.Integrable (fun x => Real.exp (C * ‖x‖ ^ 2)) μ
```

## Depends on

- [Gaussian measures](../../../overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md)
- [Fubini's theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Probability measure](../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Trigonometric functions](../../../overview/analysis/special-functions/trigonometric-functions.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Fernique.html#ProbabilityTheory.IsGaussian.exists_integrable_exp_sq)
- [Source of `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq` in Mathlib/Probability/Distributions/Gaussian/Fernique.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Distributions/Gaussian/Fernique.lean#L161)
- [1000+ theorems list: Q5445112](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L3195)
- [1000+ theorems project: Q5445112](https://1000-plus.github.io/all.html?length=-1#Q5445112)
- [Wikipedia: Fernique's theorem](https://en.wikipedia.org/wiki/Fernique's_theorem)
- [Wikidata: Q5445112](https://www.wikidata.org/wiki/Q5445112)
