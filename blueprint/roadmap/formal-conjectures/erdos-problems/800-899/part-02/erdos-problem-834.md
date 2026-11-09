---
declaration: theorem
origin: cited
lean: Erdos834.erdos_834.parts.i, Erdos834.erdos_834.parts.ii
statement: formalized
---

# Erdős Problem 834

> *References:*
> - [erdosproblems.com/834](https://www.erdosproblems.com/834)
> - [Li25] R. Li, On an Erdős-Lovász problem: $3$-critical $3$-graphs of minimum degree $7$.
>   arXiv:2512.24850 (2025).

*Quoted from [FormalConjectures/ErdosProblems/834.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/834.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/834](https://www.erdosproblems.com/834).

The file states 2 research or textbook statements: 2 solved.

## `Erdos834.erdos_834.parts.i`

Solved: stated here without proof.

> Does there exist a $3$-critical $3$-uniform hypergraph in which every vertex has degree
> $\geq 7$, where criticality means that the transversal number is $3$ and deleting any edge
> reduces it to $2$?
>
> In the first formulation, the transversal notion of criticality, Li [Li25] proves that a
> $3$-critical $3$-uniform hypergraph must have a vertex of degree $\leq 6$.

```lean
theorem erdos_834.parts.i :
    ¬ ∃ (n : ℕ) (H : Finset (Finset (Fin n))),
    H.IsUniform 3 ∧ (H : Set (Finset (Fin n))).HasFiniteTransversal 3 ∧
      ¬ (H : Set (Finset (Fin n))).HasFiniteTransversal 2 ∧
      (∀ e ∈ H, (H.erase e : Set (Finset (Fin n))).HasFiniteTransversal 2) ∧
      ∀ v : Fin n, 7 ≤ H.hypergraphDegree v
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/834.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/834.lean#L44).

## `Erdos834.erdos_834.parts.ii`

Solved: stated here without proof.

> Does there exist a $3$-critical $3$-uniform hypergraph with minimum degree at least $7$,
> where criticality means that deleting any edge or vertex reduces chromatic number $3$ to $2$?
>
> In the second formulation, the chromatic notion of criticality, Li [Li25] provides an
> explicit $3$-critical $3$-uniform hypergraph on $9$ vertices with minimum degree $7$.

```lean
theorem erdos_834.parts.ii :
    ∃ (n : ℕ) (H : Finset (Finset (Fin n))),
    H.IsUniform 3 ∧ H.HasHypergraphChromaticNumber 3 ∧
      (∀ e ∈ H, (H.erase e).HypergraphColorable 2) ∧
      (∀ v : Fin n, (H.filter (fun e ↦ v ∉ e)).HypergraphColorable 2) ∧
      ∀ v : Fin n, 7 ≤ H.hypergraphDegree v
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/834.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/834.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/834.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/834.lean)
- [erdosproblems.com/834](https://www.erdosproblems.com/834)
