---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.DirectedAdjacency, Cslib.Algorithms.Lean.DirectedAdjacency.Edge, Cslib.Algorithms.Lean.DirectedAdjacency.Walk, Cslib.Algorithms.Lean.DirectedAdjacency.toDigraph, Cslib.Algorithms.Lean.DirectedAdjacency.toDigraph_adj, Cslib.Algorithms.Lean.DirectedAdjacency.walk_zero_iff, Cslib.Algorithms.Lean.DirectedAdjacency.walk_succ_iff, Cslib.Algorithms.Lean.DirectedAdjacency.Walk.append
statement: formalized
proof: formalized
---

# Adjacency list

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html).

## Directed adjacency graph

A directed adjacency graph on a type $V$ consists of a list of
vertices that has no duplicates and contains every element of $V$ (so $V$ is finite), together
with, for each vertex $v$, an ordered list of the out-neighbors of $v$, in which entries may
repeat.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#directed-adjacency).

## Edge of a directed adjacency graph

For a directed adjacency graph $G$ on $V$ and
vertices $s, t \in V$, there is an edge from $s$ to $t$ in $G$ when $t$ occurs in the adjacency
list of $s$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.Edge`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#edge).

## Walks of a given length

For a directed adjacency graph $G$, a natural number $n$ and
vertices $s$ and $t$, there is a walk of length $n$ from $s$ to $t$ in $G$ when there are
vertices $v_0, \dots, v_n$ with $v_0 = s$ and $v_n = t$ such that $(v_i, v_{i+1})$ is an edge
of $G$ for every $i < n$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.Walk`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk).

## The digraph of a directed adjacency graph

The digraph associated with a directed
adjacency graph $G$ on a vertex type $V$ is the directed graph on $V$ in which $s$ is adjacent to
$t$ exactly when $G$ has an edge from $s$ to $t$. It forgets the order of the adjacency lists and
the multiplicity of their entries.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.toDigraph`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#to-digraph).

## Adjacency in the associated digraph

For a directed adjacency graph $G$ and vertices $s$
and $t$, $s$ is adjacent to $t$ in the digraph associated with $G$ if and only if $G$ has an edge
from $s$ to $t$, that is, $t$ occurs in the adjacency list of $s$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.toDigraph_adj`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#to-digraph-adj).

## Walks of length zero

In a directed adjacency graph, there is a walk of length $0$ from
a vertex $s$ to a vertex $t$ if and only if $s = t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.walk_zero_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk-zero-iff).

## Splitting off the first edge of a walk

In a directed adjacency graph $G$, for every
natural number $n$ and all vertices $s$ and $t$, there is a walk of length $n + 1$ from $s$ to
$t$ if and only if there is a vertex $v$ such that $(s, v)$ is an edge of $G$ and there is a
walk of length $n$ from $v$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.walk_succ_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk-succ-iff).

## Concatenation of walks

Let $G$ be a directed adjacency graph on $V$ and let
$s, m, t \in V$. If $G$ has a walk of length exactly $a$ from $s$ to $m$ and a walk of length
exactly $b$ from $m$ to $t$, then $G$ has a walk of length exactly $a + b$ from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.Walk.append`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#append).

## Reachability in a directed graph

For a directed adjacency graph $G$ and vertices $s$
and $t$, $t$ is reachable from $s$ when the pair $(s, t)$ lies in the reflexive-transitive
closure of the edge relation of $G$: either $s = t$, or a finite sequence of edges of $G$ leads
from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.Reachable`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable).

## Reachability by walks

In a directed adjacency graph $G$, a vertex $t$ is reachable from
a vertex $s$ if and only if there is a natural number $n$ such that $G$ has a walk of length
exactly $n$ from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_iff_exists_walk`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-iff-exists-walk).

## Reachability is the reflexive-transitive closure of the edge relation

In a directed
adjacency graph $G$, a vertex $t$ is reachable from a vertex $s$ if and only if $(s, t)$ lies
in the reflexive-transitive closure of the edge relation of $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_iff_reflTransGen`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-iff-refl-trans-gen).

## The transition system of a directed adjacency graph

The labelled transition system of a
directed adjacency graph $G$ has the vertices of $G$ as states and a single label, and it has a
transition from $s$ to $t$ exactly when $G$ has an edge from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.toLTS`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#to-lts).

## Reachability in the associated transition system

In a directed adjacency graph $G$, a
vertex $t$ is reachable from a vertex $s$ if and only if, in the unit-labelled labelled
transition system of $G$, there is a finite list of labels along which $s$ reaches $t$ by a
multistep transition.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_iff_lts`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-iff-lts).

## Transpose of a directed adjacency graph

For a directed adjacency graph $G$ on a
vertex type with decidable equality, the transpose of $G$ has the same vertex enumeration as
$G$, and the adjacency list of a vertex $v$ consists of the vertices $u$ such that $v$ occurs
in the adjacency list of $u$ in $G$, each listed once and in the order of the vertex
enumeration.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.transpose`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#transpose).

## Edges of the transpose graph

Let $V$ have decidable equality and let $G$ be a directed
adjacency graph on $V$. For all $s, t \in V$, the transpose of $G$ has an edge from $s$ to $t$
if and only if $G$ has an edge from $t$ to $s$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.edge_transpose`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#edge-transpose).

## Walks in the transpose are reversed walks

For a directed adjacency graph $G$ on a
vertex type with decidable equality, every natural number $n$ and all vertices $s$ and $t$,
there is a walk of length $n$ from $s$ to $t$ in the transpose of $G$ if and only if there is
a walk of length $n$ from $t$ to $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.walk_transpose_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk-transpose-iff).

## Reachability in the transpose graph

Let $G$ be a directed adjacency graph on a vertex
type with decidable equality, and let $G^{\mathsf{T}}$ be its transpose. For all vertices $s$ and
$t$, $t$ is reachable from $s$ in $G^{\mathsf{T}}$ if and only if $s$ is reachable from $t$ in
$G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_transpose_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-transpose-iff).

## Semantic equivalence of directed adjacency graphs

Two directed adjacency graphs $G_1$
and $G_2$ on the same vertex type are semantically equivalent when they have the same edges: for
all vertices $s$ and $t$, $G_1$ has an edge from $s$ to $t$ if and only if $G_2$ does.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#semantically-equivalent).

## Semantic equivalence of directed adjacency graphs is reflexive

Every directed adjacency
graph $G$ is semantically equivalent to itself.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.semanticEquivalent_refl`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#semantic-equivalent-refl).

## Semantic equivalence of directed adjacency graphs is symmetric

If a directed adjacency
graph $G_1$ is semantically equivalent to a directed adjacency graph $G_2$, then $G_2$ is
semantically equivalent to $G_1$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent.symm`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#symm).

## Semantic equivalence of directed adjacency graphs is transitive

If a directed adjacency
graph $G_1$ is semantically equivalent to $G_2$, and $G_2$ is semantically equivalent to $G_3$,
then $G_1$ is semantically equivalent to $G_3$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent.trans`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#trans).

## Semantically equivalent graphs have the same walks

If two directed adjacency graphs
$G_1$ and $G_2$ are semantically equivalent, then for every natural number $n$ and all
vertices $s$ and $t$, there is a walk of length $n$ from $s$ to $t$ in $G_1$ if and only if
there is a walk of length $n$ from $s$ to $t$ in $G_2$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent.walk_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk-iff).

## Semantically equivalent graphs have the same reachability

If two directed adjacency
graphs $G_1$ and $G_2$ on $V$ are semantically equivalent, then for all $s, t \in V$, $t$ is
reachable from $s$ in $G_1$ if and only if $t$ is reachable from $s$ in $G_2$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent.reachable_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-iff).

## Transposition preserves semantic equivalence

For directed adjacency graphs $G_1$ and
$G_2$ on a vertex type with decidable equality, if $G_1$ and $G_2$ are semantically
equivalent, then their transposes are semantically equivalent.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.SemanticallyEquivalent.transpose`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#transpose-2).

## Transposing twice gives a semantically equivalent graph

Let $G$ be a directed adjacency
graph on a vertex type with decidable equality. The transpose of the transpose of $G$ is
semantically equivalent to $G$, that is, it has exactly the same edges as $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.semanticEquivalent_transpose_transpose`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#semantic-equivalent-transpose-transpose).

## Boolean edge test

For a type $V$ with decidable equality, a directed adjacency graph
$G$ on $V$ and vertices $s, t \in V$, the edge test of $G$ at $(s, t)$ is the Boolean value
that is true exactly when $t$ occurs in the adjacency list of $s$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.hasEdge`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#has-edge).

## The Boolean edge test is correct

For a type $V$ with decidable equality, a directed
adjacency graph $G$ on $V$ and vertices $s, t \in V$, the Boolean edge test of $G$ at $(s, t)$
returns true if and only if $G$ has an edge from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.hasEdge_eq_true`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#has-edge-eq-true).

## Erasing a directed edge

Given a directed-adjacency graph $G$ and vertices $s$ and $t$,
erasing the edge $s \to t$ gives the directed-adjacency graph with the same vertex enumeration as
$G$ whose out-neighbour list at $s$ is the out-neighbour list of $s$ in $G$ with every occurrence
of $t$ removed (the remaining entries keep their order), and whose out-neighbour list at every
other vertex is the same as in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.eraseEdge`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#erase-edge).

## Erasing an edge keeps the vertex enumeration

For every directed-adjacency graph $G$ and
vertices $s$ and $t$, the graph obtained from $G$ by erasing the edge $s \to t$ has the same
vertex enumeration as $G$: the same list of vertices, in the same order.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.vertices_eraseEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#vertices-erase-edge).

## Out-neighbours of the source after erasing an edge

For every directed-adjacency graph
$G$ and vertices $s$ and $t$, the out-neighbour list of $s$ in the graph obtained from $G$ by
erasing the edge $s \to t$ is the out-neighbour list of $s$ in $G$ with every occurrence of $t$
removed, the remaining entries kept in their original order.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.adjacency_eraseEdge_source`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#adjacency-erase-edge-source).

## Erasing an edge leaves the other out-neighbour lists unchanged

For every
directed-adjacency graph $G$ and vertices $s$, $t$ and $u$ with $u \ne s$, the out-neighbour
list of $u$ in the graph obtained from $G$ by erasing the edge $s \to t$ equals the
out-neighbour list of $u$ in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.adjacency_eraseEdge_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#adjacency-erase-edge-of-ne).

## Edges after erasing an edge

For every directed-adjacency graph $G$ and vertices $s$,
$t$, $u$ and $v$, there is an edge from $u$ to $v$ in the graph obtained from $G$ by erasing
the edge $s \to t$ if and only if there is an edge from $u$ to $v$ in $G$ and it is not the case
that both $u = s$ and $v = t$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.edge_eraseEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#edge-erase-edge).

## The erased edge is absent

For every directed-adjacency graph $G$ and vertices $s$ and
$t$, the Boolean edge lookup for $s \to t$ in the graph obtained from $G$ by erasing the edge
$s \to t$ returns false.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.hasEdge_eraseEdge_self`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#has-edge-erase-edge-self).

## Erasing an edge twice gives the same out-neighbour lists

For every directed-adjacency
graph $G$ and vertices $s$ and $t$, erasing the edge $s \to t$ from $G$ and then erasing it
again gives, at every vertex, the same out-neighbour list as erasing it once.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.eraseEdge_idempotent`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#erase-edge-idempotent).

## Walks after erasing an edge are walks in the original graph

For every
directed-adjacency graph $G$, vertices $s$, $t$, $u$ and $v$, and natural number $n$, if there
is a walk of length $n$ from $u$ to $v$ in the graph obtained from $G$ by erasing the edge
$s \to t$, then there is a walk of length $n$ from $u$ to $v$ in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.walk_eraseEdge_imp`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#walk-erase-edge-imp).

## Reachability after erasing an edge implies reachability in the original graph

For
every directed-adjacency graph $G$ and vertices $s$, $t$, $u$ and $v$, if $v$ is reachable from
$u$ in the graph obtained from $G$ by erasing the edge $s \to t$, then $v$ is reachable from $u$
in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_eraseEdge_imp`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/DirectedAdjacency/EraseEdge.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html#reachable-erase-edge-imp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adjacency list](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-list)
