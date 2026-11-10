---
declaration: theorem
origin: cited
lean: Erdos702.erdos_702, Erdos702.erdos_702.variants.all_n_false
statement: formalized
---

# Erdős Problem 702

> *References:*
> - [erdosproblems.com/702](https://www.erdosproblems.com/702)
> - [Er75f] Erdős, Paul, _On some problems of elementary and combinatorial geometry_. Ann. Mat.
>   Pura Appl. (4) (1975), 99-108.
> - [Er76b] Erdős, P., _Problems and results in graph theory and combinatorial analysis_.
>   Proceedings of the Fifth British Combinatorial Conference (Univ. Aberdeen, Aberdeen, 1975)
>   (1976), 169-192.
> - [Er81] Erdős, P., _On the combinatorial problems which I would most like to see solved_.
>   Combinatorica (1981), 25-42.
> - [Er82e] Erdős, Paul, _Some of my favourite problems which recently have been solved_. (1982),
>   59--79.
> - [Fr77] Frankl, Péter, _On families of finite sets no two of which intersect in a singleton_.
>   Bull. Austral. Math. Soc. (1977), 125-134.

*Quoted from [FormalConjectures/ErdosProblems/702.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/702.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/702](https://www.erdosproblems.com/702).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos702.erdos_702`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos702.lean#L4740](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos702.lean#L4740).

> Let $k\geq 4$. If $\mathcal{F}$ is a family of subsets of $\{1,\ldots,n\}$ with $\lvert A\rvert=k$
> for all $A\in \mathcal{F}$ and $\lvert \mathcal{F}\rvert >\binom{n-2}{k-2}$ then there are
> $A,B\in\mathcal{F}$ such that $\lvert A\cap B\rvert=1$.
>
> A conjecture of Erdős and Sós. Katona (unpublished) proved this when $k=4$, and Frankl [Fr77]
> proved this for all $k\geq 4$.
>
> Frankl's theorem is for $n$ sufficiently large in terms of $k$, and this is the form stated here.
> Without this assumption the statement is false, see `erdos_702.variants.all_n_false`.

```lean
theorem erdos_702 (k : ℕ) (hk : 4 ≤ k) :
    ∀ᶠ n in atTop, ∀ 𝓕 : Finset (Finset (Fin n)), 𝓕.IsUniform k →
      (n - 2).choose (k - 2) < 𝓕.card → ∃ A ∈ 𝓕, ∃ B ∈ 𝓕, (A ∩ B).card = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/702.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/702.lean#L58).

## `Erdos702.erdos_702.variants.all_n_false`

Textbook result, proved here.

> The statement does not hold for all $n$. For $k=4$ and $n=5$, the family of all $4$-subsets of
> $\{1,\ldots,5\}$ has $5>\binom{3}{2}$ members, and any two of them meet in at least $3$ elements.

```lean
theorem erdos_702.variants.all_n_false :
    ¬ ∀ k : ℕ, 4 ≤ k → ∀ (n : ℕ) (𝓕 : Finset (Finset (Fin n))), 𝓕.IsUniform k →
      (n - 2).choose (k - 2) < 𝓕.card → ∃ A ∈ 𝓕, ∃ B ∈ 𝓕, (A ∩ B).card = 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/702.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/702.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/702.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/702.lean)
- [erdosproblems.com/702](https://www.erdosproblems.com/702)
