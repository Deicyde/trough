---
declaration: theorem
origin: cited
lean: Erdos647.erdos_647, Erdos647.erdos_647.variants.twenty_four, Erdos647.erdos_647.variants.lim, Erdos647.erdos_647.variants.infinite
statement: formalized
---

# Erdős Problem 647

> *Reference:* [erdosproblems.com/647](https://www.erdosproblems.com/647)

*Quoted from [FormalConjectures/ErdosProblems/647.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/647](https://www.erdosproblems.com/647).

The file states 4 research or textbook statements: 3 open and 1 solved.

## `Erdos647.erdos_647`

Open: stated without proof.

> Let $\tau(n)$ count the number of divisors of $n$. Is there some $n > 24$ such that
> $$
>   \max_{m < n}(m + \tau(m)) \leq n + 2?
> $$

```lean
theorem erdos_647 : ∃ n > 24, ⨆ m : Fin n, m + σ 0 m ≤ n + 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/647.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean#L37).

## `Erdos647.erdos_647.variants.twenty_four`

Proved here.

> This is true for $n = 24$.

```lean
theorem erdos_647.variants.twenty_four : ⨆ m : Fin 24, (m : ℕ) + σ 0 m ≤ 26
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/647.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean#L42).

## `Erdos647.erdos_647.variants.lim`

Open: stated without proof.

> Erdős says 'it is extremely doubtful' that there are infinitely many such $n$, and in
> fact suggests that
> $$
>   lim_{n\to\infty} \max_{m < n}(\tau(m) + m − n) = \infty.
> $$

```lean
theorem erdos_647.variants.lim :
    atTop.Tendsto (fun n ↦ ⨆ m : Fin n, σ 0 m + m - n) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/647.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean#L51).

## `Erdos647.erdos_647.variants.infinite`

Open: stated without proof.

> Erdős says it 'seems certain' that for every $k$ there are infinitely many $n$
> for which
> $$
>   \max_{n−k < m < n}(m + \tau(m)) ≤ n + 2.
> $$

```lean
theorem erdos_647.variants.infinite :
    ∀ k, { n | ⨆ m : Set.Ioo (n - k) n, ↑m + σ 0 m ≤ n + 2 }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/647.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/647.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/647.lean)
- [erdosproblems.com/647](https://www.erdosproblems.com/647)
