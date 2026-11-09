---
declaration: theorem
origin: cited
lean: Erdos816.erdos_816, Erdos816.erdos_816.variants.chen_ma, Erdos816.erdos_816.variants.complete_bipartite
statement: formalized
---

# Erdős Problem 816

> *References:*
> - [erdosproblems.com/816](https://www.erdosproblems.com/816)
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [ChMa25] K. Chen and J. Ma, *A problem of Erdős and Hajnal on paths with equal-degree
>   endpoints*. arXiv:2503.19569 (2025).

*Quoted from [FormalConjectures/ErdosProblems/816.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/816.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/816](https://www.erdosproblems.com/816).

The file states 3 research or textbook statements: 3 solved.

## `Erdos816.erdos_816`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos816.lean#L939](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos816.lean#L939).

> Let $G$ be a graph with $2n+1$ vertices and $n^2+n+1$ edges. Must $G$ contain two vertices of the
> same degree which are joined by a path of length $3$?
>
> A problem of Erdős and Hajnal. The example of $K_{n,n+1}$ shows that this fails if we only have
> $n^2+n$ edges.
>
> This is true, and was proved by Chen and Ma [ChMa25], who prove the stronger statement that,
> provided $n\geq 600$, all graphs with $2n+1$ vertices and at least $n^2+n$ edges contain two
> vertices of the same degree joined by a path of length $3$, except $K_{n,n+1}$.
>
> For $n = 1$ the graph is a triangle, which contains no path of length $3$, so we assume $n \geq 2$.

```lean
theorem erdos_816 : ∀ n : ℕ, 2 ≤ n → ∀ G : SimpleGraph (Fin (2 * n + 1)),
    G.edgeFinset.card = n ^ 2 + n + 1 → HasEqualDegreePathThree G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/816.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/816.lean#L62).

## `Erdos816.erdos_816.variants.chen_ma`

Solved: stated here without proof.

> Chen and Ma [ChMa25] proved that, provided $n\geq 600$, all graphs with $2n+1$ vertices and at
> least $n^2+n$ edges contain two vertices of the same degree joined by a path of length $3$, except
> $K_{n,n+1}$.

```lean
theorem erdos_816.variants.chen_ma : ∀ n : ℕ, 600 ≤ n →
    ∀ G : SimpleGraph (Fin (2 * n + 1)), n ^ 2 + n ≤ G.edgeFinset.card →
      ¬ Nonempty (G ≃g completeBipartiteGraph (Fin n) (Fin (n + 1))) →
        HasEqualDegreePathThree G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/816.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/816.lean#L73).

## `Erdos816.erdos_816.variants.complete_bipartite`

Solved: stated here without proof.

> The example of $K_{n,n+1}$ shows that this fails if we only have $n^2+n$ edges.

```lean
theorem erdos_816.variants.complete_bipartite : ∀ n : ℕ,
    (completeBipartiteGraph (Fin n) (Fin (n + 1))).edgeFinset.card = n ^ 2 + n ∧
      ¬ HasEqualDegreePathThree (completeBipartiteGraph (Fin n) (Fin (n + 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/816.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/816.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/816.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/816.lean)
- [erdosproblems.com/816](https://www.erdosproblems.com/816)
