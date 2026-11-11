---
declaration: section
origin: cited
lean: MetaMathlibExt.andrasfaiGraph, MetaMathlibExt.directedCayleyGraph, MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.cayley_formula, MetaMathlibExt.coxeterGraph, MetaMathlibExt.edgeTranspositionGraph, MathlibExt.Combinatorics.SimpleGraph.FruchtWanted.frucht, MetaMathlibExt.IsMooreGraph, MetaMathlibExt.petersenGraph
statement: formalized
proof: formalized
---

# Algebraic graph theory: its own results

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/index.html).

Graphs studied through groups and matrices: Cayley and vertex-transitive graphs, strongly regular and Moore graphs, graph homomorphisms, Laplacians and the matrix-tree theorem, and named graphs such as the Petersen and Coxeter graphs.

## Andrásfai graph

For a natural number $k$, the Andrásfai graph is the Cayley graph of
the cyclic group $\mathbb{Z}/(3k+2)\mathbb{Z}$ whose connection set $C$ consists of the residues
whose representative in $\{0, 1, \dots, 3k+1\}$ is congruent to $1$ modulo $3$: two distinct
residues $x$ and $y$ are adjacent when $y - x \in C$ or $x - y \in C$.

Formalized by `MetaMathlibExt.andrasfaiGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Andrasfai.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Andrasfai.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#andrasfai-graph).

## Cayley digraph

Let $G$ be a set with a binary operation written as multiplication,
and let $C \subseteq G$. The *Cayley digraph* $X(G, C)$ is the directed graph whose vertices
are the elements of $G$, with an arc $u \to v$ exactly when $v = uc$ for some $c \in C$.

Usually $G$ is a group and $C$ does not contain the identity, so that $X(G, C)$ has no loops;
neither condition is imposed here.

Formalized by `MetaMathlibExt.directedCayleyGraph`, a definition declared in [MathlibExt/Combinatorics/Digraph/DirectedCayley.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/DirectedCayley.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#directed-cayley-graph).

## Cayley's formula

For every natural number $n \ge 2$, the complete graph on $n$ vertices has
exactly $n^{n-2}$ spanning trees.

## Sources

- A. Cayley, "A theorem on trees", Quarterly Journal of Pure and Applied Mathematics 23 (1889), 376-378.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MatrixTreeWanted.cayley_formula`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Cayley.lean, line 1065](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Cayley.lean#L1065). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#cayley-formula).

## Coxeter graph

The Coxeter graph is the simple graph whose $28$ vertices are the pairs
$(i, j)$ with $i \in \{0, 1, 2, 3\}$ and $j \in \mathbb{Z}/7\mathbb{Z}$, and whose edges are the
following: for each $i \in \{1, 2, 3\}$, the vertices $(i, j)$ and $(i, j')$ are adjacent when
$j - j' = i$ or $j' - j = i$ in $\mathbb{Z}/7\mathbb{Z}$, and for each $j$ the vertex $(0, j)$ is
adjacent to $(1, j)$, $(2, j)$ and $(3, j)$. There are no other edges.

Formalized by `MetaMathlibExt.coxeterGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CoxeterGraph.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/CoxeterGraph.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#coxeter-graph).

## Edge-transposition graph

Let $n$ be a natural number and let $T$ be a set of permutations
of $\{0, 1, \dots, n - 1\}$, typically a set of transpositions in the symmetric group $S_n$. The
edge-transposition graph of $T$ is the simple graph with vertex set $\{0, 1, \dots, n - 1\}$ in
which two distinct vertices $i$ and $j$ are adjacent if and only if the transposition swapping $i$
and $j$ belongs to $T$.

Formalized by `MetaMathlibExt.edgeTranspositionGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeTranspositionGraph.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeTranspositionGraph.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#edge-transposition-graph).

## Frucht's theorem

Every finite group is isomorphic to the automorphism group of a finite simple
graph.

## Sources

- R. Frucht, Compositio Math. 6 (1939), 239-250.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.FruchtWanted.frucht`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Frucht.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Frucht.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#frucht).

## Moore graph

Let $G$ be a simple graph on a finite vertex set and let $d$ be a natural
number. Then $G$ is a Moore graph of diameter $d$ when $G$ has diameter $d$ and girth $2d + 1$.

Formalized by `MetaMathlibExt.IsMooreGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Moore.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Moore.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#is-moore-graph).

## Petersen graph

The Petersen graph is the generalized Johnson graph $J(5,2,0)$: its
vertices are the $2$-element subsets of $\{0, 1, 2, 3, 4\}$, and two of them are adjacent
exactly when they are disjoint.

Formalized by `MetaMathlibExt.petersenGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Petersen.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Petersen.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#petersen-graph).

## Powers of a weighted adjacency matrix sum the weights of walks

Let $R$ be a commutative
semiring, let $k$ and $n$ be natural numbers, and let $A$ be a $k \times k$ matrix over $R$ with
rows and columns indexed by $\{0, \dots, k-1\}$, viewed as the weighted adjacency matrix of a
weighted digraph on these $k$ vertices. Then for all vertices $i$ and $j$,

$$(A^n)_{ij} = \sum_{p} \prod_{t=0}^{n-1} A_{p_t p_{t+1}},$$

where the sum runs over all sequences $p = (p_0, \dots, p_n)$ of vertices with $p_0 = i$ and
$p_n = j$, that is, over all walks of length $n$ from $i$ to $j$, each weighted by the product
of the entries of $A$ along its edges.

The source states $n \ge 1$; the case $n = 0$ is included, where both sides equal $1$ if
$i = j$ and $0$ otherwise.

## Sources

- Thomas Koshy, "A Graph-Theoretic Model for a Generalized Fibonacci Gem," Journal of Integer Sequences 22 (2019), Article 19.4.1, Theorem, lines 128–130, https://cs.uwaterloo.ca/journals/JIS/VOL22/Koshy/koshy7.tex

Formalized by `MetaMathlibExt.adjMatrix_pow_weighted_walk_sum`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/AdjMatrixPowWalk.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/AdjMatrixPowWalk.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/index.html#adj-matrix-pow-weighted-walk-sum).

## Vertex-transitive graph

A graph is vertex-transitive when its automorphism group acts transitively
on vertices.

Formalized by `SimpleGraph.IsVertexTransitive`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/VertexTransitive.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexTransitive.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-02/index.html#is-vertex-transitive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebraic graph theory](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/algebraic-graph-theory)
