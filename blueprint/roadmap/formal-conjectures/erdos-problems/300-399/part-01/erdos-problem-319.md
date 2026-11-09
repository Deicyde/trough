---
declaration: theorem
origin: cited
lean: Erdos319.erdos_319, Erdos319.erdos_319.variants.isTheta, Erdos319.erdos_319.variants.lb
statement: formalized
---

# Erdős Problem 319

> *Reference:* [erdosproblems.com/319](https://www.erdosproblems.com/319)

*Quoted from [FormalConjectures/ErdosProblems/319.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/319.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/319](https://www.erdosproblems.com/319).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos319.erdos_319`

Open: stated without proof.

> What is the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
> $\delta : A \to \{-1, 1\}$ such that
>
> $$
>   \sum_{n\in A} \frac{\delta n}{n} = 0
> $$
>
> and
>
> $$
>   \sum_{n\in A'}\frac{\delta n}{n} \neq 0
> $$
>
> for all non-empty $A'\subsetneq A$.

```lean
theorem erdos_319 (N : ℕ) : IsGreatest
    { #A | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) }
    erdos_319.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/319.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/319.lean#L47).

## `Erdos319.erdos_319.variants.isTheta`

Solved: stated here without proof.

> Let $c(N)$ be the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
> $\delta : A \to \{-1, 1\}$ such that
>
> $$
>   \sum_{n\in A} \frac{\delta n}{n} = 0
> $$
>
> and
>
> $$
>   \sum_{n\in A'}\frac{\delta n}{n} \neq 0
> $$
>
> for all non-empty $A'\subsetneq A$. What is $\Theta(c(N))$?
>
> Trivially $c(N) \leq N$, and `erdos_319.variants.lb` gives $c(N) \geq (1 - \frac{1}{e} + o(1))N$,
> so $c(N) = \Theta(N)$.

```lean
theorem erdos_319.variants.isTheta (N : ℕ) (c : ℕ → ℝ)
    (h : ∀ N, IsGreatest
    { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) } (c N)) :
    c =Θ[atTop] erdos_319.variants.isTheta.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/319.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/319.lean#L73).

## `Erdos319.erdos_319.variants.lb`

Solved: stated here without proof.

> Adenwalla has observed that a lower bound (on the maximum size of $A$) of
>
> $$
>   |A| \geq (1 - \frac{1}{e} + o(1))N
> $$
>
> follows from the main result of Croot [Cr01].
>
> [Cr01] Croot, III, Ernest S., _On unit fractions with denominators in short intervals_.
> Acta Arith. (2001), 99-114.

```lean
theorem erdos_319.variants.lb : ∃ (o : ℕ → ℝ), (o =o[atTop] (1 : ℕ → ℝ)) ∧
    ∀ᶠ N in atTop, (1 - 1 / rexp 1 + o N) * N ≤ sSup { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) }
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/319.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/319.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/319.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/319.lean)
- [erdosproblems.com/319](https://www.erdosproblems.com/319)
