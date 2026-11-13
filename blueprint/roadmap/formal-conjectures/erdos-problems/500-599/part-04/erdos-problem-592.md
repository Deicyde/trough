---
declaration: theorem
origin: cited
lean: Erdos592.erdos_592
statement: formalized
---

# Erdős Problem 592

> *Reference:* [erdosproblems.com/592](https://www.erdosproblems.com/592)

*Quoted from [FormalConjectures/ErdosProblems/592.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/592.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/592](https://www.erdosproblems.com/592).

The file states 1 research or textbook statement: 1 open.

## `Erdos592.erdos_592`

Open: stated without proof.

> Determine which countable ordinals $β$ have the property that, if $α = \omega^β$, then in any
> red/blue colouring of the edges of $K_α$ there is either a red $K_α$ or a blue $K_3$.

```lean
theorem erdos_592 (β : Ordinal.{u}) : β.card ≤ ℵ₀ →
    (OrdinalCardinalRamsey (ω ^ β) (ω ^ β) 3 ↔ erdos_592.answer β)
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/592.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/592.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/592.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/592.lean)
- [erdosproblems.com/592](https://www.erdosproblems.com/592)
