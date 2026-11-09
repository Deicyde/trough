---
declaration: theorem
origin: cited
lean: Erdos549.erdos_549
statement: formalized
---

# Erdős Problem 549

> *References:*
> - [erdosproblems.com/549](https://www.erdosproblems.com/549)
> - [Bu74] Burr, S. A., Generalized Ramsey theory for graphs—a survey. Graphs and combinatorics
>   (Proc. Capital Conf., George Washington Univ., Washington, D.C., 1973) (1974), 52-75.
> - [NSZ16] S. Norin and Y. R. Sun and Y. Zhao, Asymptotics of Ramsey numbers of double stars.

*Quoted from [FormalConjectures/ErdosProblems/549.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/549.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/549](https://www.erdosproblems.com/549).

The file states 1 research or textbook statement: 1 solved.

## `Erdos549.erdos_549`

Solved: stated here without proof.

> If $T$ is a tree which is a bipartite graph with $k$ vertices in one class and $2k$ vertices
> in the other class then
> $$R(T)=4k-1.$$
>
> This is false: Norin, Sun, and Zhao [NSZ16] have proved that if $T$ is the union of two stars on $k$
> and $2k$ vertices, with an edge joining the centre of the two stars, then $R(T)\geq (4.2-o(1))k$,
> and conjectured that $R(T)=(4.2+o(1))k$.
>
> This problem is #15 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_549 :
    ¬ ∀ (k : ℕ) (hk : 2 ≤ k) (T : SimpleGraph (Fin k ⊕ Fin (2 * k))),
      T.IsTree →
      (∀ x₁ x₂, ¬ T.Adj (Sum.inl x₁) (Sum.inl x₂)) →
      (∀ y₁ y₂, ¬ T.Adj (Sum.inr y₁) (Sum.inr y₂)) →
      SimpleGraph.diagonalGraphRamsey T = 4 * k - 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/549.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/549.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/549.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/549.lean)
- [erdosproblems.com/549](https://www.erdosproblems.com/549)
