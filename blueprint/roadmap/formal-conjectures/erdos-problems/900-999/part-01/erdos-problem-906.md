---
declaration: theorem
origin: cited
lean: Erdos906.erdos_906
statement: formalized
---

# Erdős Problem 906

> *Reference:* [erdosproblems.com/906](https://www.erdosproblems.com/906)

*Quoted from [FormalConjectures/ErdosProblems/906.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/906.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/906](https://www.erdosproblems.com/906).

The file states 1 research or textbook statement: 1 open.

## `Erdos906.erdos_906`

Open: stated without proof.

> Does there exists an entire non-zero transcendental function `f : ℂ → ℂ` such that for any
> sequence `n₀ < n₁ < ...`, `{ z | ∃ k, iteratedDeriv (n k) f z = 0 }` is dense.

```lean
theorem erdos_906 : ∃ f : ℂ → ℂ, Transcendental (Polynomial ℂ) f ∧
    Differentiable ℂ f ∧ ∀ n : ℕ → ℕ, StrictMono n →
    Dense { z | ∃ k, iteratedDeriv (n k) f z = 0 }
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/906.lean, line 33](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/906.lean#L33).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/906.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/906.lean)
- [erdosproblems.com/906](https://www.erdosproblems.com/906)
