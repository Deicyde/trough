---
declaration: theorem
origin: cited
lean: Erdos243.erdos_243
statement: formalized
---

# Erdős Problem 243

> *Reference:* [erdosproblems.com/243](https://www.erdosproblems.com/243)

*Quoted from [FormalConjectures/ErdosProblems/243.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/243.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/243](https://www.erdosproblems.com/243).

The file states 1 research or textbook statement: 1 open.

## `Erdos243.erdos_243`

Open: stated without proof.

> Let $a_1 < a_2 < \dots$ be a sequence of integers such that
> $\lim_{n\to\infty} \frac{a_n}{a_{n-1}^2} = 1$ and $\sum \frac{1}{a_n} \in \mathbb{Q}$.
>
> Then, for all sufficiently large $n \ge 1$, $a_n = a_{n-1}^2 - a_{n-1} + 1$.

```lean
theorem erdos_243 (a : ℕ → ℕ) (ha₀ : StrictMono a)
    (ha₁ : Tendsto (fun n ↦ (a n : ℝ) / a (n - 1) ^ 2) atTop (𝓝 1))
    (ha₂ : Summable ((1 : ℚ) / a ·)) :
      ∀ᶠ n in atTop, a n = a (n - 1) ^ 2 - a (n - 1) + 1
```

Category `research open`; AMS [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/243.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/243.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/243.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/243.lean)
- [erdosproblems.com/243](https://www.erdosproblems.com/243)
