---
declaration: theorem
origin: cited
lean: Erdos1198.erdos_1198, Erdos1198.erdos_1198.variants.hindman
statement: formalized
---

# Erdős Problem 1198

> *References:*
> - [erdosproblems.com/1198](https://www.erdosproblems.com/1198)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [Hi74] Hindman, Neil, *Finite sums from sequences within cells of a partition of $\mathbb{N}$*.
>   J. Combinatorial Theory Ser. A (1974), 1-11.
> - [Sm95] Smith, Gregory L., *Partitions and ($m$ and $n$) sums of products*. J. Combin. Theory
>   Ser. A (1995), 77-94.

*Quoted from [FormalConjectures/ErdosProblems/1198.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1198.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1198](https://www.erdosproblems.com/1198).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1198.erdos_1198`

Solved: stated here without proof.

> If $\mathbb{N}$ is $2$-coloured, must there exist an infinite set $A=\{a_1\lt a_2\lt \cdots\}$ such that
> all expressions of the shape
>
> $$\sum_{j=1}^{k}\prod_{i\in S_j}a_i,$$
>
> for $k\geq 1$ and pairwise disjoint nonempty finite sets of indices $S_1,\ldots,S_k$ (excluding the
> trivial expressions $a_i$, that is $k=1$ and $|S_1|=1$), have the same colour?
>
> Erdős [Er80, p.104] wrote that "one would perhaps guess that the answer must be 'no' but no
> counterexample is in sight". The case where every $S_j$ is a singleton is Hindman's theorem [Hi74].
> The answer is no: a counterexample was given by Smith [Sm95].

```lean
theorem erdos_1198 :
    ¬ ∀ c : ℕ → Fin 2, ∃ a : ℕ → ℕ, StrictMono a ∧ 0 < a 0 ∧ ∃ col : Fin 2,
      ∀ (k : ℕ) (S : Fin k → Finset ℕ), 0 < k → (∀ j, (S j).Nonempty) →
        Pairwise (fun j j' => Disjoint (S j) (S j')) → ¬ (k = 1 ∧ ∀ j, #(S j) = 1) →
        c (∑ j, ∏ i ∈ S j, a i) = col
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1198.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1198.lean#L51).

## `Erdos1198.erdos_1198.variants.hindman`

Solved: stated here without proof.

> The case where every $S_j$ is a singleton (Hindman's theorem [Hi74]): for every $2$-colouring of
> $\mathbb{N}$ there is an infinite set all of whose finite sums of distinct elements have the same
> colour.

```lean
theorem erdos_1198.variants.hindman :
    ∀ c : ℕ → Fin 2, ∃ a : ℕ → ℕ, StrictMono a ∧ 0 < a 0 ∧ ∃ col : Fin 2,
      ∀ T : Finset ℕ, T.Nonempty → c (∑ i ∈ T, a i) = col
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1198.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1198.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1198.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1198.lean)
- [erdosproblems.com/1198](https://www.erdosproblems.com/1198)
