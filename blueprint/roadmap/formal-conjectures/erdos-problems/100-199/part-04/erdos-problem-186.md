---
declaration: theorem
origin: cited
lean: Erdos186.erdos_186, Erdos186.erdos_186.variants.pham_zakharov, Erdos186.erdos_186.variants.bosznay, Erdos186.erdos_186.variants.erdos_sarkozy
statement: formalized
---

# Erdős Problem 186

> *References:*
> - [erdosproblems.com/186](https://www.erdosproblems.com/186)
> - [Bo89] Bosznay, Á. P., *On the lower estimation of nonaveraging sets*. Acta Math. Hungar.
>   (1989), 155-157.
> - [ErSa90] Erdős, P. and Sárközy, A., *On a problem of Straus*. Disorder in physical systems
>   (1990), 55-66.
> - [PhZa24] Pham, H. T. and Zakharov, D., *Sharp bound for the Erdős–Straus non-averaging set
>   problem*. [arXiv:2410.14624](https://arxiv.org/abs/2410.14624) (2024).

*Quoted from [FormalConjectures/ErdosProblems/186.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/186](https://www.erdosproblems.com/186).

The file states 4 research or textbook statements: 4 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `Erdos186.erdos_186`

Solved: stated here without proof.

> Let $F(N)$ be the maximal size of $A\subseteq \{1,\ldots,N\}$ which is 'non-averaging', so that
> no $n\in A$ is the arithmetic mean of at least two elements in $A$. What is the order of growth
> of $F(N)$?
>
> It is known that $N^{1/4}\ll F(N) \ll N^{1/4+o(1)}$: the lower bound is due to Bosznay [Bo89] and
> the upper bound to Pham and Zakharov [PhZa24, Theorem 1]. So $\log F(N)/\log N\to 1/4$.

```lean
theorem erdos_186 :
    Tendsto (fun N : ℕ ↦ Real.log (F N) / Real.log N) atTop (𝓝 (1 / 4))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/186.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean#L78).

## `Erdos186.erdos_186.variants.pham_zakharov`

Solved: stated here without proof.

> Pham and Zakharov [PhZa24, Theorem 1] proved that every non-averaging subset of
> $\{1,\ldots,N\}$ has size at most $N^{1/4+o(1)}$.

```lean
theorem erdos_186.variants.pham_zakharov :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, (F N : ℝ) ≤ (N : ℝ) ^ ((1 : ℝ) / 4 + ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/186.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean#L87).

## `Erdos186.erdos_186.variants.bosznay`

Solved: stated here without proof.

> The lower bound $N^{1/4}\ll F(N)$ is due to Bosznay [Bo89].

```lean
theorem erdos_186.variants.bosznay :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop, c * (N : ℝ) ^ ((1 : ℝ) / 4) ≤ F N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/186.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean#L93).

## `Erdos186.erdos_186.variants.erdos_sarkozy`

Solved: stated here without proof.

> The original upper bound of Erdős and Sárközy [ErSa90] was $F(N)\ll (N\log N)^{1/2}$.

```lean
theorem erdos_186.variants.erdos_sarkozy :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ N : ℕ in atTop, (F N : ℝ) ≤ C * Real.sqrt ((N : ℝ) * Real.log N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/186.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/186.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/186.lean)
- [erdosproblems.com/186](https://www.erdosproblems.com/186)
