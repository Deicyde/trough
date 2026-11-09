---
declaration: theorem
origin: cited
lean: Erdos145.erdos_145, Erdos145.erdos_145.variants.le_two, Erdos145.erdos_145.variants.le_three, Erdos145.erdos_145.variants.lt_eleven_thirds
statement: formalized
---

# Erdős Problem 145

> *Reference:* [erdosproblems.com/145](https://www.erdosproblems.com/145)

*Quoted from [FormalConjectures/ErdosProblems/145.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/145](https://www.erdosproblems.com/145).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos145.erdos_145`

Open: stated without proof.

> Let $s_1 < s_2 < \cdots$ be the sequence of squarefree numbers. Is it true that, for any
> $\alpha\geq 0$,
>
> $$
> \lim_{x\to\infty} \frac{1}{x}\sum_{s_n\leq x}(s_{n+1}-s_n)^\alpha
> $$
>
> exists?

```lean
theorem erdos_145 :
    ∀ α ≥ (0 : ℝ), ∃ β : ℝ,
      atTop.Tendsto (fun x : ℝ ↦ 1 / x * ∑ n ∈ A x, (s (n + 1) - s n : ℝ) ^ α) (𝓝 β)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/145.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean#L49).

## `Erdos145.erdos_145.variants.le_two`

Solved: stated here without proof.

> Erdős [Er51] proved this for all $0\leq \alpha\leq 2$.
>
> [Er51] Erdös, P., Some problems and results in elementary number theory.
>   Publ. Math. Debrecen (1951), 103-109.

```lean
theorem erdos_145.variants.le_two {α : ℝ} (hα : α ∈ Set.Icc 0 2) :
    ∃ β : ℝ,
      atTop.Tendsto (fun x : ℝ ↦ 1 / x * ∑ n ∈ A x, (s (n + 1) - s n : ℝ) ^ α) (𝓝 β)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/145.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean#L61).

## `Erdos145.erdos_145.variants.le_three`

Solved: stated here without proof.

> Hooley [Ho73] extended this to all $0 \leq \alpha\leq 3$.
>
> [Ho73] Hooley, Christopher, On the intervals between consecutive terms of sequences. Proc. Symp. Pure Math, vol. 24, pp. 129-140. 1973.

```lean
theorem erdos_145.variants.le_three {α : ℝ} (hα : α ∈ Set.Icc 0 3) :
    ∃ β : ℝ,
      atTop.Tendsto (fun x : ℝ ↦ 1 / x * ∑ n ∈ A x, (s (n + 1) - s n : ℝ) ^ α) (𝓝 β)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/145.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean#L72).

## `Erdos145.erdos_145.variants.lt_eleven_thirds`

Solved: stated here without proof.

> Greaves, Harman, and Huxley showed (in Chapter 11 of [GHH97]) that this is true for
> $0 \leq \alpha < 11/3$.
>
> [GHH97] Greaves, G. R. H. and Harman, G. and Huxley, M. N., Sieve Methods, Exponential Sums, and
>   their Applications in Number Theory. (1997).

```lean
theorem erdos_145.variants.lt_eleven_thirds {α : ℝ} (hα : α ∈ Set.Ico 0 (11 / 3)) :
    ∃ β : ℝ,
      atTop.Tendsto (fun x : ℝ ↦ 1 / x * ∑ n ∈ A x, (s (n + 1) - s n : ℝ) ^ α) (𝓝 β)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/145.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/145.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/145.lean)
- [erdosproblems.com/145](https://www.erdosproblems.com/145)
