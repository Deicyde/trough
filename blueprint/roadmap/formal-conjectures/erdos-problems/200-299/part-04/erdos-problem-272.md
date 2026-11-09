---
declaration: theorem
origin: cited
lean: Erdos272.erdos_272, Erdos272.erdos_272.variants.isBigO_sq, Erdos272.erdos_272.variants.szabo, Erdos272.erdos_272.variants.szabo_strong
statement: formalized
---

# Erdős Problem 272

> *Reference:* [erdosproblems.com/272](https://www.erdosproblems.com/272)

*Quoted from [FormalConjectures/ErdosProblems/272.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/272](https://www.erdosproblems.com/272).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos272.erdos_272`

Open: stated without proof.

> Let $N\geq 1$. What is the largest $t$ such that there are
> $A_1,\ldots,A_t\subseteq \{1,\ldots,N\}$ with $A_i\cap A_j$ a non-empty
> arithmetic progression for all $i\neq j$?

```lean
theorem erdos_272 :
    ∀ N ≥ 1, maxArithInterCard N = erdos_272.answer N
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/272.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean#L53).

## `Erdos272.erdos_272.variants.isBigO_sq`

Solved: stated here without proof.

> Simonovits and Sós have shown that $t\ll N^2$.

```lean
theorem erdos_272.variants.isBigO_sq :
    (fun N ↦ (maxArithInterCard N : ℝ)) =O[atTop] fun N ↦ (N : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/272.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean#L61).

## `Erdos272.erdos_272.variants.szabo`

Solved: stated here without proof.

> Szabo showed that the maximal $t$ is equal to
> $$
>   \frac{N^2}{2} + O(N^{5/3}\log^3N).
> $$

```lean
theorem erdos_272.variants.szabo :
    (fun N ↦ (maxArithInterCard N - N ^ 2 / 2 : ℝ)) =O[atTop]
      fun N : ℕ ↦ N ^ ((5 : ℝ) /  3) * (Real.log N) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/272.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean#L71).

## `Erdos272.erdos_272.variants.szabo_strong`

Open: stated without proof.

> Szabo asks whether the maximal $t$ is given by
> $$
>   \frac{N^2}{2} + O(N)
> $$

```lean
theorem erdos_272.variants.szabo_strong :
    (fun N ↦ (maxArithInterCard N - N ^ 2 / 2 : ℝ)) =O[atTop] fun N : ℕ ↦ (N : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/272.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/272.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/272.lean)
- [erdosproblems.com/272](https://www.erdosproblems.com/272)
