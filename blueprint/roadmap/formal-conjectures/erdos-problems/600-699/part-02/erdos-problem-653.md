---
declaration: theorem
origin: cited
lean: Erdos653.erdos_653
statement: formalized
---

# Erdős Problem 653

> *Reference:* [erdosproblems.com/653](https://www.erdosproblems.com/653)

*Quoted from [FormalConjectures/ErdosProblems/653.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/653.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/653](https://www.erdosproblems.com/653).

The file states 1 research or textbook statement: 1 open.

## `Erdos653.erdos_653`

Open: stated without proof.

> Let $x_1,\ldots,x_n\in \mathbb{R}^2$ and let $R(x_i)=\#\{ \lvert x_j-x_i\rvert : j\neq i\}$,
> where the points are ordered such that
>
> $$R(x_1)\leq \cdots \leq R(x_n).$$
>
> Let $g(n)$ be the maximum number of distinct values the $R(x_i)$ can take. Is it true that
> $g(n) \geq (1-o(1))n$?

```lean
theorem erdos_653 : ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ n in atTop, (1 - o n) * n ≤ maximalDistinctDistancesFrom n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/653.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/653.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/653.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/653.lean)
- [erdosproblems.com/653](https://www.erdosproblems.com/653)
