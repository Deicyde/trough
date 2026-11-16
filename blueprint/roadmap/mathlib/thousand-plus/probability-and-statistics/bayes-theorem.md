# Bayes' theorem

**Bayes' Theorem**

```lean
ProbabilityTheory.cond_eq_inv_mul_cond_mul.{u_1} {Ω : Type u_1} {m : MeasurableSpace Ω}
  {s t : Set Ω} (hms : MeasurableSet s) (hmt : MeasurableSet t) (μ : MeasureTheory.Measure Ω)
  [MeasureTheory.IsFiniteMeasure μ] : μ[t | s] = (μ s)⁻¹ * μ[s | t] * μ t
```

## Depends on

- [Conditional probability](../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.cond_eq_inv_mul_cond_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/ConditionalProbability.html#ProbabilityTheory.cond_eq_inv_mul_cond_mul)
- [Source of `ProbabilityTheory.cond_eq_inv_mul_cond_mul` in Mathlib/Probability/ConditionalProbability.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Probability/ConditionalProbability.lean#L272)
- [1000+ theorems list: Q182505](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L108)
- [1000+ theorems project: Q182505](https://1000-plus.github.io/all.html?length=-1#Q182505)
- [Wikipedia: Bayes' theorem](https://en.wikipedia.org/wiki/Bayes'_theorem)
- [Wikidata: Q182505](https://www.wikidata.org/wiki/Q182505)
