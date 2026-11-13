---
declaration: theorem
origin: cited
lean: Erdos266.erdos_266, Erdos266.erdos_266.variants.all_rationals
statement: formalized
---

# Erdős Problem 266

> *Reference:* [erdosproblems.com/266](https://www.erdosproblems.com/266)

*Quoted from [FormalConjectures/ErdosProblems/266.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/266.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/266](https://www.erdosproblems.com/266).

The file states 2 research or textbook statements: 2 solved.

## `Erdos266.erdos_266`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos266.lean#L306](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos266.lean#L306).

> Let $a_n$ be an infinite sequence of positive integers such that $\sum \frac{1}{a_n}$ converges.
> There exists some integer $t \ge 1$ such that $\sum \frac{1}{a_n + t}$ is irrational.
>
> This was disproven by Kovač and Tao in [KoTa24].
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series.
>          [arXiv:2406.17593](https://arxiv.org/abs/2406.17593) (2024).

```lean
theorem erdos_266 :
    ¬ ∀ (a : ℕ → ℕ), ((∀ n : ℕ, a n ≥ 1) ∧ Summable ((1 : ℝ) / a ·) →
      ∃ t ≥ (1 : ℕ), Irrational <| ∑' n, (1 : ℝ) / ((a n) + t))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/266.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/266.lean#L44).

## `Erdos266.erdos_266.variants.all_rationals`

Solved: stated here; a Lean proof is at [https://github.com/benkeene/erdos266/blob/ef01b23804a60669f24b25733f1a2b688084609d/Solution.lean#L27](https://github.com/benkeene/erdos266/blob/ef01b23804a60669f24b25733f1a2b688084609d/Solution.lean#L27).

> In fact, Kovač and Tao proved in [KoTa24] that there exists a strictly increasing
> sequence $a_n$ of positive integers such that $\sum \frac{1}{a_n + t}$ converges to a rational
> number for all $t \in \mathbb{Q}$ such that $t \ne -a_n$ for any $n$.
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series.
>          [arXiv:2406.17593](https://arxiv.org/abs/2406.17593) (2024).
>
> Lean formalization by Ben Keene, with AI assistance.

```lean
theorem erdos_266.variants.all_rationals:
    ∃ a : ℕ → ℕ, StrictMono a ∧ a 0 ≥ 1 ∧
      (∀ t : ℚ, (¬ ∃ n : ℕ, t = -(a n)) →
        (∃ q : ℚ, HasSum (fun n : ℕ => ((1 : ℝ) / ((a n) + t))) q))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/266.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/266.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/266.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/266.lean)
- [erdosproblems.com/266](https://www.erdosproblems.com/266)
