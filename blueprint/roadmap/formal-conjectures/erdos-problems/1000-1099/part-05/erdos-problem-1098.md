---
declaration: theorem
origin: cited
lean: Erdos1098.erdos_1098, Erdos1098.erdos_1098.variants.center_finiteIndex, Erdos1098.erdos_1098.variants.upper_bound
statement: formalized
---

# Erdős Problem 1098

> *References:*
> - [erdosproblems.com/1098](https://www.erdosproblems.com/1098)
> - [Ne76] Neumann, B. H., *A problem of Paul Erdős on groups*. J. Austral. Math. Soc. Ser. A (1976),
>   467-472.

*Quoted from [FormalConjectures/ErdosProblems/1098.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1098.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1098](https://www.erdosproblems.com/1098).

The file states 3 research or textbook statements: 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1098.erdos_1098`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1098.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1098.lean).

> Let $G$ be a group and $\Gamma=\Gamma(G)$ be the non-commuting graph, with vertices the elements
> of $G$ and an edge between $g$ and $h$ if and only if $g$ and $h$ do not commute, $gh\neq hg$.
>
> If $\Gamma$ contains no infinite complete subgraph, then is there a finite bound on the size of
> complete subgraphs of $\Gamma$?
>
> This was solved by Neumann [Ne76], who proved that $\Gamma$ contains no infinite complete subgraph
> if and only if the centre of the group has finite index, and noted that if the centre has index $n$
> then $\Gamma$ contains no complete subgraph on $>n$ vertices.

```lean
theorem erdos_1098 :
    ∀ (G : Type*) [Group G],
      (∀ s : Set G, (nonCommutingGraph G).IsClique s → s.Finite) →
        ∃ n : ℕ, ∀ s : Finset G, (nonCommutingGraph G).IsClique (s : Set G) → s.card ≤ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1098.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1098.lean#L56).

## `Erdos1098.erdos_1098.variants.center_finiteIndex`

Solved: stated here without proof.

> Neumann [Ne76] proved that $\Gamma$ contains no infinite complete subgraph if and only if the
> centre of the group has finite index.

```lean
theorem erdos_1098.variants.center_finiteIndex (G : Type*) [Group G] :
    (∀ s : Set G, (nonCommutingGraph G).IsClique s → s.Finite) ↔
      (Subgroup.center G).FiniteIndex
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1098.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1098.lean#L67).

## `Erdos1098.erdos_1098.variants.upper_bound`

Solved: stated here without proof.

> Neumann [Ne76] noted that if the centre has index $n$ then $\Gamma$ contains no complete subgraph
> on $>n$ vertices.

```lean
theorem erdos_1098.variants.upper_bound (G : Type*) [Group G]
    [(Subgroup.center G).FiniteIndex] :
    (nonCommutingGraph G).CliqueFree ((Subgroup.center G).index + 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1098.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1098.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1098.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1098.lean)
- [erdosproblems.com/1098](https://www.erdosproblems.com/1098)
