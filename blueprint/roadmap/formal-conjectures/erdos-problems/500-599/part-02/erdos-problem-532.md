---
declaration: theorem
origin: cited
lean: Erdos532.erdos_532
statement: formalized
---

# Erdős Problem 532

> *References:*
> - [erdosproblems.com/532](https://www.erdosproblems.com/532)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of combinatorial theory (1973), 117-138.
> - [Er75b] Erdős, Paul, *Problems and results in combinatorial number theory*. Journées Arithmétiques de Bordeaux (1975), 295-310.
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory day (1977), 43-72.
> - [Hi74] Hindman, Neil, *Finite sums from sequences within cells of a partition of $\mathbb{N}$*. J. Combinatorial Theory Ser. A (1974), 1-11.

*Quoted from [FormalConjectures/ErdosProblems/532.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/532.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/532](https://www.erdosproblems.com/532).

The file states 1 research or textbook statement: 1 solved.

## `Erdos532.erdos_532`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos532.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos532.lean).

> If $\mathbb{N}$ is 2-coloured then is there some infinite set $A\subseteq \mathbb{N}$ such that
> all finite subset sums$$ \sum_{n\in S}n$$(as $S$ ranges over all non-empty finite subsets of $A$)
> are monochromatic?
>
> Asked by Graham and Rothschild. Proved by Hindman [Hi74] (for any number of colours).

```lean
theorem erdos_532 :
    ∀ (c : ℕ → Fin 2),
      ∃ A : Set ℕ, A.Infinite ∧
        ∃ color : Fin 2,
          ∀ S : Finset ℕ, S.Nonempty → ↑S ⊆ A →
            c (∑ n ∈ S, n) = color
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/532.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/532.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/532.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/532.lean)
- [erdosproblems.com/532](https://www.erdosproblems.com/532)
