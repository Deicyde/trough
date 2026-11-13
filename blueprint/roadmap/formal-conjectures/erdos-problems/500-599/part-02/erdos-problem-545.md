---
declaration: theorem
origin: cited
lean: Erdos545.erdos_545
statement: formalized
---

# Erdős Problem 545

> *References:*
> - [erdosproblems.com/545](https://www.erdosproblems.com/545)
> - [ErGr75] Erdős, P. and Graham, R. L., On partition theorems for finite graphs.
>   Infinite and finite sets (1975), 515-527.
> - [Er84b] Erdős, P., On some problems in graph theory, combinatorial analysis and combinatorial
>   number theory. Graph theory and combinatorics (Cambridge, 1983) (1984), 1-17.

*Quoted from [FormalConjectures/ErdosProblems/545.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/545.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/545](https://www.erdosproblems.com/545).

The file states 1 research or textbook statement: 1 open.

## `Erdos545.erdos_545`

Open: stated without proof.

> Let $m$ be sufficiently large and let $G$ be a graph with $m$ edges and no isolated vertices.
> Is the Ramsey number $R(G)$ maximised when $G$ is 'as complete as possible'?
> That is, if $m=\binom{n}{2}+t$ edges with $0\leq t < n$
> then is
>
> $$R(G)\leq R(H),$$
>
> where $H$ is the graph formed by connecting a new vertex to $t$ of the vertices of $K_n$?
>
> A question of Erdős and Graham. The restriction to sufficiently large $m$ excludes the
> small counterexamples recorded on the source page.
>
> This problem is #10 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_545 :
    ∀ᶠ m : ℕ in atTop, ∀ (n t : ℕ), t < n → m = n.choose 2 + t →
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj],
        (∀ v, 0 < G.degree v) →
        G.edgeSet.ncard = m →
        SimpleGraph.diagonalGraphRamsey G ≤
          SimpleGraph.diagonalGraphRamsey (knPlusTEdges n t)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/545.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/545.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/545.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/545.lean)
- [erdosproblems.com/545](https://www.erdosproblems.com/545)
