---
declaration: theorem
origin: cited
lean: Erdos761.erdos_761.parts.i, Erdos761.erdos_761.parts.ii, Erdos761.erdos_761.variants.parts_ii_imp_i
statement: formalized
---

# Erdős Problem 761

> *References:*
> - [erdosproblems.com/761](https://www.erdosproblems.com/761)
> - [ErGi93] Erdős, P. and Gimbel, J., *Some problems and results in cochromatic theory*.
>   Quo vadis, graph theory? (1993), 261-264.

*Quoted from [FormalConjectures/ErdosProblems/761.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/761.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/761](https://www.erdosproblems.com/761).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos761.erdos_761.parts.i`

Open: stated without proof.

> The dichromatic number of $G$, denoted by $\delta(G)$, is the minimum number $k$ of colours
> required such that, in any orientation of the edges of $G$, there is a $k$-colouring of the
> vertices of $G$ such that there are no monochromatic oriented cycles.
>
> Must a graph with large chromatic number have large dichromatic number?
>
> This question is due to Erdős and Neumann-Lara. We read it for finite graphs: for every $k$ there
> is $m$ such that every finite graph with $\chi(G)\geq m$ has $\delta(G)\geq k$.

```lean
theorem erdos_761.parts.i :
    ∀ k : ℕ, ∃ m : ℕ, ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
      (m : ℕ∞) ≤ G.chromaticNumber → (k : ℕ∞) ≤ dichromaticNumber G
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/761.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/761.lean#L68).

## `Erdos761.erdos_761.parts.ii`

Open: stated without proof.

> The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed to
> colour the vertices of $G$ such that each colour class induces either a complete graph or empty
> graph.
>
> Must a graph with large cochromatic number contain a graph with large dichromatic number?
>
> This question is due to Erdős and Gimbel. We read it for finite graphs and subgraphs: for every
> $k$ there is $m$ such that every finite graph with $\zeta(G)\geq m$ has a subgraph $H$ with
> $\delta(H)\geq k$.

```lean
theorem erdos_761.parts.ii :
    ∀ k : ℕ, ∃ m : ℕ, ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
      (m : ℕ∞) ≤ G.cochromaticNumber →
        ∃ H : G.Subgraph, (k : ℕ∞) ≤ dichromaticNumber H.coe
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/761.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/761.lean#L85).

## `Erdos761.erdos_761.variants.parts_ii_imp_i`

Solved: stated here without proof.

> A positive answer to the second question implies a positive answer to the first via the bound
> mentioned in [760].

```lean
theorem erdos_761.variants.parts_ii_imp_i :
    (∀ k : ℕ, ∃ m : ℕ, ∀ (V : Type u) [Finite V] (G : SimpleGraph V),
      (m : ℕ∞) ≤ G.cochromaticNumber →
        ∃ H : G.Subgraph, (k : ℕ∞) ≤ dichromaticNumber H.coe) →
    ∀ k : ℕ, ∃ m : ℕ, ∀ (V : Type u) [Finite V] (G : SimpleGraph V),
      (m : ℕ∞) ≤ G.chromaticNumber → (k : ℕ∞) ≤ dichromaticNumber G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/761.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/761.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/761.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/761.lean)
- [erdosproblems.com/761](https://www.erdosproblems.com/761)
