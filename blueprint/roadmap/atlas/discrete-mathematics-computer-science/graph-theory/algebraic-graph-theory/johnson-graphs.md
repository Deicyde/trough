---
declaration: section
origin: cited
lean: MetaMathlibExt.johnsonGraph, SimpleGraph.johnsonGraph, SimpleGraph.johnsonGraph_adj_iff
statement: formalized
proof: formalized
---

# Johnson graphs

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs/index.html).

## Generalized Johnson graph

For natural numbers $v$, $k$ and $i$, the generalized Johnson
graph $J(v,k,i)$ is the graph whose vertices are the $k$-element subsets of $\{0, 1, \dots, v-1\}$,
in which two distinct vertices are adjacent if and only if their intersection has exactly $i$
elements.

The usual setting is $v \ge k \ge i$; the definition does not require it.

Formalized by `MetaMathlibExt.johnsonGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedJohnson.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/GeneralizedJohnson.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs/index.html#johnson-graph).

## Johnson graph

For natural numbers $n$ and $k$, the Johnson graph $J(n, k)$ has as
vertices the $k$-element subsets of $\{0, 1, \dots, n-1\}$, and two vertices $s$ and $t$ are
adjacent when $|s \cap t| + 1 = k$, that is, when $s$ and $t$ share exactly $k - 1$ elements.

Formalized by `SimpleGraph.johnsonGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Johnson.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Johnson.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs/index.html#johnson-graph-2).

## Adjacency in the Johnson graph

For natural numbers $n$ and $k$ and $k$-element subsets
$s$ and $t$ of $\{0, 1, \dots, n-1\}$, the vertices $s$ and $t$ of the Johnson graph $J(n, k)$
are adjacent if and only if $|s \cap t| + 1 = k$.

Formalized by `SimpleGraph.johnsonGraph_adj_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Johnson.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Johnson.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs/index.html#johnson-graph-adj-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Johnson graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/johnson-graphs)
