---
declaration: theorem
origin: cited
lean: Erdos952.erdos_952
statement: formalized
---

# Erdős Problem 952

> *References:*
> - [erdosproblems.com/952](https://www.erdosproblems.com/952)
> - [Wikipedia](https://wikipedia.org/wiki/Gaussian_moat)
> - [OAI26a] OpenAI, *Bounded-Step Walks on Gaussian Primes*. OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/952.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/952.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/952](https://www.erdosproblems.com/952).

The file states 1 research or textbook statement: 1 solved.

## `Erdos952.erdos_952`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/GaussianMoat/Main.lean#L102](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/GaussianMoat/Main.lean#L102).

> Is there an infinite sequence of distinct Gaussian primes $x_1,x_2,\ldots$
> such that $\lvert x_{n+1}-x_n\rvert \ll 1$?
>
> No. This was disproved by an internal OpenAI model in September 2026 [OAI26a]; see the linked
> Lean proof.

```lean
theorem erdos_952 :
  ¬ ∃ (x : ℕ → GaussianInt) (C : ℤ),
    Function.Injective x ∧
      ∀ n, Prime (x n) ∧ (x (n + 1) - x n).norm < C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/952.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/952.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/952.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/952.lean)
- [erdosproblems.com/952](https://www.erdosproblems.com/952)
