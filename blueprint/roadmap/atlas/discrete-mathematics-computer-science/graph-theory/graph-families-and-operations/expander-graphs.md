---
declaration: section
origin: cited
lean: SimpleGraph.externalNeighborSet, SimpleGraph.mem_externalNeighborSet, SimpleGraph.externalNeighborSet_disjoint, SimpleGraph.exists_adj_of_mem_externalNeighborSet, SimpleGraph.IsCExpander, SimpleGraph.IsCExpander.pos, SimpleGraph.IsCExpander.small_expansion, SimpleGraph.IsCExpander.large_edge
statement: formalized
proof: formalized
---

# Expander graphs

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html).

## External neighbourhood

For a simple graph $G$ on a vertex set $V$ and a set
$A \subseteq V$, the external neighbourhood of $A$ in $G$ is the set of vertices $v \notin A$
that are adjacent in $G$ to some vertex of $A$.

Formalized by `SimpleGraph.externalNeighborSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#external-neighbor-set).

## Membership in the external neighbourhood

Let $G$ be a simple graph on a vertex set
$V$, let $A \subseteq V$ and let $v \in V$. Then $v$ lies in the external neighbourhood of $A$
in $G$ if and only if $v \notin A$ and $v$ is adjacent in $G$ to some vertex $a \in A$.

Formalized by `SimpleGraph.mem_externalNeighborSet`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#mem-external-neighbor-set).

## The external neighbourhood is disjoint from the set

For every simple graph $G$ on a
vertex set $V$ and every set $A \subseteq V$, the external neighbourhood of $A$ in $G$ is
disjoint from $A$.

Formalized by `SimpleGraph.externalNeighborSet_disjoint`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#external-neighbor-set-disjoint).

## External neighbours have a neighbour in the set

Let $G$ be a simple graph on a vertex
set $V$ and let $A \subseteq V$. If $v$ is an external neighbour of $A$ in $G$, then $v$ is
adjacent in $G$ to some vertex $a \in A$.

Formalized by `SimpleGraph.exists_adj_of_mem_externalNeighborSet`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#exists-adj-of-mem-external-neighbor-set).

## C-expander

Let $G$ be a simple graph on a finite vertex set $V$ with $n$ vertices, and
let $C$ be a real number. Then $G$ is a $C$-expander if $C > 0$, every set $A \subseteq V$
with $|A| < n/(2C)$ has an external neighbourhood in $G$ with at least $C|A|$ vertices, and
for any two disjoint sets $A, B \subseteq V$ with $|A| \ge n/(2C)$ and $|B| \ge n/(2C)$ some
vertex of $A$ is adjacent in $G$ to some vertex of $B$.

## Sources

- Krivelevich, Lew and Michaeli, *Rigidity of expanders and pseudorandom graphs*, Definition 1.

Formalized by `SimpleGraph.IsCExpander`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#is-cexpander).

## The parameter of a C-expander is positive

Let $G$ be a simple graph on a finite vertex
set $V$ and let $C$ be a real number. If $G$ is a $C$-expander, then $C > 0$.

Formalized by `SimpleGraph.IsCExpander.pos`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#pos).

## Small sets expand in a $C$-expander

Let $C$ be a real number and let $G$ be a
$C$-expander on a finite vertex set $V$. Then every set $A \subseteq V$ with $|A| < |V|/(2C)$ has
at least $C|A|$ external neighbours, that is, at least $C|A|$ vertices outside $A$ are adjacent to
some vertex of $A$.

Formalized by `SimpleGraph.IsCExpander.small_expansion`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#small-expansion).

## Large disjoint sets in a C-expander span an edge

Let $G$ be a simple graph on a finite
vertex set $V$ with $n$ vertices, let $C$ be a real number, and suppose $G$ is a $C$-expander.
If $A, B \subseteq V$ are disjoint sets with $|A| \ge n/(2C)$ and $|B| \ge n/(2C)$, then some
vertex $a \in A$ is adjacent in $G$ to some vertex $b \in B$.

Formalized by `SimpleGraph.IsCExpander.large_edge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#large-edge).

## Uniform vertex expander

Let $G$ be a simple graph on a finite vertex set $V$ and let
$h$ be a real number. Then $G$ is a uniform vertex expander with parameter $h$ if $h > 0$ and
every set $S \subseteq V$ with $|S| \le |V|/2$ has an external neighbourhood in $G$ with at
least $h|S|$ vertices.

Formalized by `SimpleGraph.IsUniformVertexExpander`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#is-uniform-vertex-expander).

## The parameter of a uniform vertex expander is positive

Let $G$ be a simple graph on a
finite vertex set $V$ and let $h$ be a real number. If $G$ is a uniform vertex expander with
parameter $h$, then $h > 0$.

Formalized by `SimpleGraph.IsUniformVertexExpander.pos`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#pos-2).

## Small sets expand in a uniform vertex expander

Let $G$ be a simple graph on a finite
vertex set $V$ and let $h$ be a real number. If $G$ is a uniform vertex expander with parameter
$h$ and $S \subseteq V$ satisfies $|S| \le |V|/2$, then the external neighbourhood of $S$ in
$G$ has at least $h|S|$ vertices.

Formalized by `SimpleGraph.IsUniformVertexExpander.small_expansion`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Expander.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Expander.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html#small-expansion-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Expander graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/expander-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-families-and-operations/expander-graphs)
