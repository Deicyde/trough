# Schroeder–Bernstein theorem for measurable spaces

The **measurable Schröder-Bernstein Theorem**: given measurable embeddings
`α → β` and `β → α`, we can find a measurable equivalence `α ≃ᵐ β`.

```lean
MeasurableEmbedding.schroederBernstein.{u_1, u_2} {α : Type u_1} {β : Type u_2} [MeasurableSpace α]
  [MeasurableSpace β] {f : α → β} {g : β → α} (hf : MeasurableEmbedding f)
  (hg : MeasurableEmbedding g) : α ≃ᵐ β
```

## Depends on

- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `MeasurableEmbedding.schroederBernstein`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Embedding.html#MeasurableEmbedding.schroederBernstein)
- [Source of `MeasurableEmbedding.schroederBernstein` in Mathlib/MeasureTheory/MeasurableSpace/Embedding.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/MeasureTheory/MeasurableSpace/Embedding.lean#L723)
- [1000+ theorems list: Q7432915](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L3782)
- [1000+ theorems project: Q7432915](https://1000-plus.github.io/all.html?length=-1#Q7432915)
- [Wikipedia: Schroeder–Bernstein theorem for measurable spaces](https://en.wikipedia.org/wiki/Schroeder%E2%80%93Bernstein_theorem_for_measurable_spaces)
- [Wikidata: Q7432915](https://www.wikidata.org/wiki/Q7432915)
