---
declaration: theorem
origin: cited
lean: Erdos81.erdos_81, Erdos81.erdos_81.variants.split
statement: formalized
---

# Erdős Problem 81

> *References:*
> - [erdosproblems.com/81](https://www.erdosproblems.com/81)
> - [EOZ93] Erdős, Paul and Ordman, Edward T. and Zalcstein, Yechezkel,
>   *Clique partitions of chordal graphs*. Combin. Probab. Comput. (1993), 409–415.
> - [CEO94] Chen, Guan-Tao and Erdős, Paul and Ordman, Edward T.,
>   *Clique partitions of split graphs*. Combinatorics, graph theory, algorithms and applications
>   (Beijing, 1993) (1994), 21–30.

*Quoted from [FormalConjectures/ErdosProblems/81.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/81.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/81](https://www.erdosproblems.com/81).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos81.erdos_81`

Open: stated without proof.

> Let $G$ be a chordal graph on $n$ vertices - that is, $G$ has no induced cycles of
> length greater than $3$. Can the edges of $G$ be partitioned into $n^2/6+O(n)$ many cliques?

```lean
theorem erdos_81 :
    ∃ C : ℝ, ∀ n : ℕ, ∀ G : SimpleGraph (Fin n), G.IsChordal →
      ∃ P : Finset (Finset (Fin n)), G.IsCliqueEdgePartition P ∧
        (P.card : ℝ) ≤ (n : ℝ) ^ 2 / 6 + C * n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/81.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/81.lean#L41).

## `Erdos81.erdos_81.variants.split`

Solved: stated here without proof.

> Chen, Erdős, and Ordman [CEO94] have shown that any split graph can be partitioned
> into $\frac{3}{16}n^2+O(n)$ many cliques.

```lean
theorem erdos_81.variants.split :
    ∃ C : ℝ, ∀ n : ℕ, ∀ G : SimpleGraph (Fin n), G.IsSplitGraph →
      ∃ P : Finset (Finset (Fin n)), G.IsCliqueEdgePartition P ∧
        (P.card : ℝ) ≤ 3 * (n : ℝ) ^ 2 / 16 + C * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/81.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/81.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/81.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/81.lean)
- [erdosproblems.com/81](https://www.erdosproblems.com/81)
