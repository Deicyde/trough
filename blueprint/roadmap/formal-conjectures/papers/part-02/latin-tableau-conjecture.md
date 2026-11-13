---
declaration: theorem
origin: cited
lean: LatinTableau.SimpleGraph.LatinTableauConjecture
statement: formalized
---

# Latin Tableau Conjecture

> The Latin Tableau Conjecture states that the graph associated
> to any (finite) Young diagram (i.e., whose vertices are the
> cells of the diagram, with edges between cells in the same row
> or column) is CDS-colorable, meaning that there exists a proper
> coloring of the vertices of the graph such that for all k > 0, the
> number of vertices with color < k equals the maximum size of
> the union of k independent sets of the graph.
>
> *References:*
>
> * [The Latin Tableau Conjecture](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i2p48)

*Quoted from [FormalConjectures/Paper/LatinTableau.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinTableau.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `LatinTableau.SimpleGraph.LatinTableauConjecture`

Open: stated without proof.

> The Latin Tableau Conjecture: If G is the simple graph
> of a Young diagram, then G is CDS-colorable.

```lean
theorem LatinTableauConjecture (μ : YoungDiagram) :
     μ.toSimpleGraph.CDSColorable
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinTableau.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinTableau.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/LatinTableau.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinTableau.lean)
- [The Latin Tableau Conjecture](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i2p48)
