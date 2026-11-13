---
declaration: theorem
origin: cited
lean: Erdos131.erdos_131.variants.pham_zakharov, Erdos131.erdos_131.variants.elrss, Erdos131.erdos_131
statement: formalized
---

# Erdős Problem 131

> *References:*
> - [erdosproblems.com/131](https://www.erdosproblems.com/131)
> - [ELRSS99] Erdős, P. and Lev, V. and Rauzy, G. and Sándor, C. and Sárközy, A., *Greedy
>   algorithm, arithmetic progressions, subset sums and divisibility*. Discrete Math. (1999),
>   119-135.
> - [PhZa24] Pham, H. T. and Zakharov, D., *Sharp bound for the Erdős–Straus non-averaging set
>   problem*. [arXiv:2410.14624](https://arxiv.org/abs/2410.14624) (2024).

*Quoted from [FormalConjectures/ErdosProblems/131.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/131.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/131](https://www.erdosproblems.com/131).

The file states 3 research or textbook statements: 3 solved. It also has 5 API statements, counted here but not shown.

## `Erdos131.erdos_131.variants.pham_zakharov`

Solved: stated here without proof.

> Every non-dividing set is non-averaging. Pham and Zakharov [PhZa24] proved that a
> non-averaging subset of $\{1, \dots, N\}$ has size at most $N^{1/4 + o(1)}$, so
> $F(N) \le N^{1/4 + o(1)}$.

```lean
theorem erdos_131.variants.pham_zakharov :
    ∃ f : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧
      ∀ᶠ N : ℕ in atTop, (F N : ℝ) ≤ (N : ℝ) ^ ((1 : ℝ) / 4 + f N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/131.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/131.lean#L93).

## `Erdos131.erdos_131.variants.elrss`

Solved: stated here without proof.

> Erdős, Lev, Rauzy, Sándor and Sárközy [ELRSS99] proved $F(N) < 3 N^{1/2} + 1$.

```lean
theorem erdos_131.variants.elrss (N : ℕ) : (F N : ℝ) < 3 * Real.sqrt N + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/131.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/131.lean#L100).

## `Erdos131.erdos_131`

Proved here.

> Let $F(N)$ be the maximal size of $A \subseteq \{1, \dots, N\}$ such that no $a \in A$ divides
> the sum of any distinct elements of $A \setminus \{a\}$. Is it true that
> $F(N) > N^{1/2 - o(1)}$?
>
> The answer is no, by the bound of Pham and Zakharov [PhZa24]
> (`erdos_131.variants.pham_zakharov`).

```lean
theorem erdos_131 :
    ¬ ∃ f : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧
      ∀ᶠ N : ℕ in atTop, (N : ℝ) ^ ((1 : ℝ) / 2 - f N) < (F N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/131.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/131.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/131.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/131.lean)
- [erdosproblems.com/131](https://www.erdosproblems.com/131)
