---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsGaussian.exists_integrable_exp_sq
mathlib_file: Mathlib/Probability/Distributions/Gaussian/Fernique.lean
---

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

- [Gaussian measures](../../../../overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)

## Proof depends on

- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Giry monad](../../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Group](../../../../overview/general-algebra/group-theory/part-01/group.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Fernique.html#ProbabilityTheory.IsGaussian.exists_integrable_exp_sq)
- [Source of `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq` in Mathlib/Probability/Distributions/Gaussian/Fernique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Distributions/Gaussian/Fernique.lean#L161)
- [1000+ theorems list: Q5445112](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3195)
- [1000+ theorems project: Q5445112](https://1000-plus.github.io/all.html?length=-1#Q5445112)
- [Wikipedia: Fernique's theorem](https://en.wikipedia.org/wiki/Fernique's_theorem)
- [Wikidata: Q5445112](https://www.wikidata.org/wiki/Q5445112)
