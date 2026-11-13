---
declaration: theorem
origin: cited
lean: Erdos616.erdos_616
statement: formalized
---

# Erdős Problem 616

> *References:*
> - [erdosproblems.com/616](https://www.erdosproblems.com/616)
> - [EHT91] Erdős, Paul and Hajnal, András and Tuza, Zsolt, Local constraints ensuring small
>   representing sets. J. Combin. Theory Ser. A (1991), 78-84.

*Quoted from [FormalConjectures/ErdosProblems/616.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/616.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/616](https://www.erdosproblems.com/616).

The file states 1 research or textbook statement: 1 open.

## `Erdos616.erdos_616`

Open: stated without proof.

> Let $r\geq 3$. For an $r$-uniform hypergraph $G$ let $\tau(G)$ denote the covering number (or
> transversal number), the minimum size of a set of vertices which includes at least one from each
> edge in $G$. Determine the best possible $t$ such that, if $G$ is an $r$-uniform hypergraph $G$
> where every subgraph $G'$ on at most $3r-3$ vertices has $\tau(G')\leq 1$, we have $\tau(G)\leq t$.

```lean
theorem erdos_616 :
    ∀ r : ℕ, 3 ≤ r → Hypergraph.localTransversalBound r (3 * r - 3) 1 = erdos_616.answer r
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/616.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/616.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/616.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/616.lean)
- [erdosproblems.com/616](https://www.erdosproblems.com/616)
