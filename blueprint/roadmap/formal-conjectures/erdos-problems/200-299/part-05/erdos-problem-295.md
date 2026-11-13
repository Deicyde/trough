---
declaration: lemma
origin: cited
lean: Erdos295.exists_k, Erdos295.erdos_295, Erdos295.erdos_295.variants.erdos_straus
statement: formalized
---

# Erdős Problem 295

> *Reference:* [erdosproblems.com/295](https://www.erdosproblems.com/295)

*Quoted from [FormalConjectures/ErdosProblems/295.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/295.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/295](https://www.erdosproblems.com/295).

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result.

## `Erdos295.exists_k`

Textbook result, stated without proof.

> Helper lemma: for each $N$, there exists $k$ and $n_1 < ... < n_k$ such that
> $N ≤ n_1 < ⋯ < n_k$ with $\frac 1 {n_1} + ... + \frac 1 {n_k} = 1$.

```lean
lemma exists_k (N : ℕ) : ∃ (k : ℕ) (n : Fin k → ℕ),
    (∀ i, N ≤ n i) ∧ StrictMono n ∧ ∑ i, (1 / n i : ℝ) = 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/295.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/295.lean#L37).

## `Erdos295.erdos_295`

Open: stated without proof.

> Let $k(N)$ denote the smallest $k$ such that there exists
> $N ≤ n_1 < ⋯ < n_k$ with $\frac 1 {n_1} + ... + \frac 1 {n_k} = 1$
>
> Is it true that $\lim_{N \to \infty} k(N) - (e - 1)N = \infty$?

```lean
theorem erdos_295 :
    Filter.atTop.Tendsto (fun N => k N - (rexp 1 - 1)*N) Filter.atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/295.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/295.lean#L58).

## `Erdos295.erdos_295.variants.erdos_straus`

Solved: stated here without proof.

> Erdős and Straus have proved the existence of some constant $c>0$
> such that $-c < k(N)-(e-1)N \ll \frac N {\log N}$

```lean
theorem erdos_295.variants.erdos_straus :
    ∃ᵉ (C > 0) (O > 0), ∀ᶠ (N : ℕ) in Filter.atTop,
      (k N - (rexp 1 - 1)*N) ∈ Set.Ioc (-C) (O * N / (N : ℝ).log)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/295.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/295.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/295.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/295.lean)
- [erdosproblems.com/295](https://www.erdosproblems.com/295)
