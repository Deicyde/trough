---
declaration: theorem
origin: cited
lean: Erdos431.erdos_431, Erdos431.erdos_431.variants.ostmann
statement: formalized
---

# Erdős Problem 431

> *References:*
> - [erdosproblems.com/431](https://www.erdosproblems.com/431)
> - [OAI26a] OpenAI, *The additive indecomposability of the primes*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/431.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/431.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/431](https://www.erdosproblems.com/431).

The file states 2 research or textbook statements: 2 solved.

## `Erdos431.erdos_431`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Ostmann/Complete.lean#L16](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Ostmann/Complete.lean#L16).

> Are there two infinite sets $A$ and $B$ such that $A+B$ agrees with the primes up to finitely
> many exceptions?
>
> This was disproved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
theorem erdos_431 :
    ¬ ∃ A B : Set ℕ, A.Infinite ∧ B.Infinite ∧
      (A + B : Set ℕ) =ᶠ[Filter.cofinite] {n | n.Prime}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/431.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/431.lean#L46).

## `Erdos431.erdos_431.variants.ostmann`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Ostmann/Result.lean#L14](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Ostmann/Result.lean#L14).

> Ostmann's inverse Goldbach conjecture: if $A$ and $B$ each have at least two elements, then
> $A+B$ differs from the primes in infinitely many elements.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
theorem erdos_431.variants.ostmann :
    ∀ A B : Set ℕ, A.Nontrivial → B.Nontrivial → ((A + B) ∆ {n | n.Prime}).Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/431.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/431.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/431.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/431.lean)
- [erdosproblems.com/431](https://www.erdosproblems.com/431)
