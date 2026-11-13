---
declaration: section
origin: cited
lean: MetaMathlibExt.SimpleGraph.IsLineGraph, SimpleGraph.lexProduct
statement: formalized
proof: formalized
---

# Graph families and operations: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/index.html).

Graph products, line graphs and other constructions, together with special families such as expanders and the hypercubic lattice.

## Graphs that are line graphs

A simple graph $G$ on a finite vertex type is a line graph if
there are a natural number $k$ and a simple graph $H$ on the vertex set $\{0, \dots, k-1\}$ such
that $G$ is isomorphic to the line graph $L(H)$. Here $L(H)$ has the edges of $H$ as its vertices,
and two distinct edges of $H$ are adjacent in $L(H)$ when they share an endpoint.

Formalized by `MetaMathlibExt.SimpleGraph.IsLineGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/LineGraph.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/LineGraph.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/index.html#is-line-graph).

## Lexicographic product of graphs

Given simple graphs $X$ and $Y$, the *lexicographic
product* $X[Y]$ of $X$ and $Y$ is the simple graph with vertex set $V(X) \times V(Y)$ in which
two vertices $(x_1, y_1)$ and $(x_2, y_2)$ are adjacent exactly when $x_1$ and $x_2$ are
adjacent in $X$, or $x_1 = x_2$ and $y_1$ and $y_2$ are adjacent in $Y$.

Formalized by `SimpleGraph.lexProduct`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/GraphProducts/LexProduct.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GraphProducts/LexProduct.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/index.html#lex-product).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph families and operations](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-families-and-operations)
