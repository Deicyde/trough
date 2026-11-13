---
declaration: theorem
origin: cited
lean: Erdos268.erdos_268
statement: formalized
---

# Erdős Problem 268

> *Reference:*
>  - [erdosproblems.com/268](https://www.erdosproblems.com/268)
>  - [KoTa24] Kova\vC, V. and Tao T., On several irrationality problems for Ahmes series.

*Quoted from [FormalConjectures/ErdosProblems/268.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/268.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/268](https://www.erdosproblems.com/268).

The file states 1 research or textbook statement: 1 solved.

## `Erdos268.erdos_268`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/madeve-unipi/62a8f68cdb4864b85b81a6752dcb0aa4/raw/5793aaa51089c25c37d8d63f60540367f6abe506/Erdos268.lean](https://gist.githubusercontent.com/madeve-unipi/62a8f68cdb4864b85b81a6752dcb0aa4/raw/5793aaa51089c25c37d8d63f60540367f6abe506/Erdos268.lean).

> Let `X` be the set of points in `Fin d → ℝ` of the shape
> `fun i : Fin d => ∑' n : A, (1 : ℝ) / (n + i)` for some infinite subset `A ⊆ ℕ` such that
> `1 / n` is summable over `A`. `X` has nonempty interior. This is proved in [KoTa24].
> -

```lean
theorem erdos_268 (d : ℕ) : (interior {x : Fin d → ℝ | ∃ A : Set ℕ, A.Infinite ∧
    Summable (fun n : A => (1 : ℝ) / n ) ∧
    x = fun i : Fin d => ∑' n : A, (1 : ℝ) / (n + i)}).Nonempty
```

Category `research solved`; AMS [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [54 General topology](../../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/ErdosProblems/268.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/268.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/268.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/268.lean)
- [erdosproblems.com/268](https://www.erdosproblems.com/268)
