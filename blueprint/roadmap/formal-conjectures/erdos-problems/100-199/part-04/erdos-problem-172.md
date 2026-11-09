---
declaration: theorem
origin: cited
lean: Erdos172.erdos_172
statement: formalized
---

# Erdős Problem 172

> *References:*
> - [erdosproblems.com/172](https://www.erdosproblems.com/172)
> - [OpenAI26] OpenAI, *Monochromatic finite sums and products in the positive integers*. OpenAI Math
>   Release preprint (September 2026).
>   [github.com/openai/math](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf)

*Quoted from [FormalConjectures/ErdosProblems/172.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/172.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/172](https://www.erdosproblems.com/172).

The file states 1 research or textbook statement: 1 solved.

## `Erdos172.erdos_172`

Solved: stated here; a Lean proof is at [https://github.com/cadamcat/hindman-sums-products-lean4/blob/3064cac5f9133a968482886ab1c7a1d69c16207f/audit/Erdos172.lean#L18](https://github.com/cadamcat/hindman-sums-products-lean4/blob/3064cac5f9133a968482886ab1c7a1d69c16207f/audit/Erdos172.lean#L18).

> Is it true that in any finite colouring of $\mathbb{N}$ there exist arbitrarily large finite $A$ such that all sums
> and products of distinct elements in $A$ are the same colour?

```lean
theorem erdos_172 :
    ∀ (n : ℕ) (color : ℕ → Fin n) (m), ∃ (A : Finset ℕ), A.card ≥ m ∧ ∃ c, ∀ (S : Finset A),
    S.Nonempty → color (∑ x ∈ S, x) = c ∧ color (∏ x ∈ S, x) = c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/172.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/172.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/172.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/172.lean)
- [erdosproblems.com/172](https://www.erdosproblems.com/172)
