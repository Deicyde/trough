---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.laplacianInt, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.reducedLaplacian, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.IsSpanningTree, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.numSpanningTrees, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.laplacianInt_eq_lapMatrix, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.reducedLaplacian_eq_lapMatrix_submatrix, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.spanningTreeSubgraphEquiv, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.numSpanningTrees_eq_card_trees
statement: formalized
proof: formalized
---

# Kirchhoff's matrix-tree theorem

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html).

## Integer Laplacian of a graph

For a simple graph $G$ on a finite vertex set $V$, the integer
Laplacian of $G$ is the $V \times V$ integer matrix $L$ with $L_{uu} = \deg u$ for every vertex
$u$, $L_{uv} = -1$ when $u \ne v$ are adjacent, and $L_{uv} = 0$ when $u \ne v$ are not adjacent.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.laplacianInt`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#laplacian-int).

## Reduced Laplacian

For a simple graph $G$ on a finite vertex set $V$ and a vertex
$r \in V$, the reduced Laplacian of $G$ at $r$ is the integer Laplacian of $G$ with the row and
the column of $r$ deleted, a matrix indexed by the vertices of $G$ other than $r$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.reducedLaplacian`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#reduced-laplacian).

## Spanning tree

A subgraph $T$ of a simple graph $G$ is a spanning tree of $G$ if it contains
every vertex of $G$ and, regarded as a graph on its own vertex set, it is a tree (connected and
acyclic).

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.IsSpanningTree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#is-spanning-tree).

## Number of spanning trees

For a simple graph $G$ on a finite vertex set, the number of
spanning trees of $G$ is the number of subgraphs of $G$ that are spanning trees, that is,
subgraphs that contain every vertex of $G$ and are trees.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.numSpanningTrees`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#num-spanning-trees).

## The integer Laplacian is degree minus adjacency

For a simple graph $G$ on a finite vertex
set, the integer Laplacian of $G$ equals $D - A$, where $D$ is the diagonal matrix of vertex
degrees and $A$ is the adjacency matrix of $G$, both with integer entries.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.laplacianInt_eq_lapMatrix`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#laplacian-int-eq-lap-matrix).

## The reduced Laplacian is a principal submatrix

Let $G$ be a simple graph on a finite vertex
set $V$ and let $L = D - A$ be its Laplacian matrix over $\mathbb{Z}$, where $D$ is the diagonal
matrix of vertex degrees and $A$ is the adjacency matrix of $G$. For every vertex $r \in V$, the
reduced Laplacian of $G$ at $r$ equals the submatrix of $L$ obtained by deleting the row and the
column of $r$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.reducedLaplacian_eq_lapMatrix_submatrix`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#reduced-laplacian-eq-lap-matrix-submatri).

## Spanning trees as trees contained in the graph

For a simple graph $G$ on a vertex set $V$,
there is an equivalence between the spanning trees of $G$ (subgraphs of $G$ that contain every
vertex and are trees) and the simple graphs $H$ on $V$ that are trees with $H \le G$, that is,
every edge of $H$ is an edge of $G$. It sends a spanning tree to the graph on $V$ with the same
edges.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.spanningTreeSubgraphEquiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#spanning-tree-subgraph-equiv).

## Spanning trees as trees on the whole vertex set

For a simple graph $G$ on a finite vertex
set $V$, the number of spanning trees of $G$ equals the number of simple graphs $H$ on $V$ such
that every edge of $H$ is an edge of $G$ and $H$ is a tree.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.numSpanningTrees_eq_card_trees`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#num-spanning-trees-eq-card-trees).

## Matrix-tree theorem for a chosen root

Let $G$ be a simple graph on a finite vertex set $V$
and let $r \in V$. Then the determinant of the reduced Laplacian of $G$ at $r$, that is, the
integer Laplacian of $G$ with the row and the column of $r$ deleted, equals the number of spanning
trees of $G$.

No separate nonemptiness hypothesis on $V$ is needed, since $r$ is a vertex.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.kirchhoff_matrix_tree_of_root`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 826](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L826). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#kirchhoff-matrix-tree-of-root).

## Matrix-tree theorem for principal minors of the Laplacian

Let $G$ be a simple graph on a
finite vertex set $V$, let $L = D - A$ be its Laplacian matrix over $\mathbb{Z}$, where $D$ is the
diagonal matrix of vertex degrees and $A$ is the adjacency matrix of $G$, and let $r \in V$. Then
the determinant of the submatrix of $L$ obtained by deleting the row and the column of $r$ equals
the number of spanning trees of $G$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.kirchhoff_matrix_tree_lapMatrix`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#kirchhoff-matrix-tree-lap-matrix).

## Kirchhoff's matrix-tree theorem

Let $G$ be a simple graph on a finite nonempty vertex set $V$
and let $r \in V$. Then the determinant of the reduced Laplacian of $G$ at $r$, that is, the
integer Laplacian of $G$ with the row and the column of $r$ deleted, equals the number of spanning
trees of $G$.

In particular, this determinant is $0$ when $G$ is disconnected.

## Sources

- G. Kirchhoff, "Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Verteilung galvanischer Ströme geführt wird", Annalen der Physik und Chemie 72 (1847), 497–508, DOI 10.1002/andp.18471481202

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.kirchhoff_matrix_tree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean, line 855](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/MatrixTree.lean#L855). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html#kirchhoff-matrix-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kirchhoff's matrix-tree theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/kirchhoff-s-matrix-tree-theorem)
