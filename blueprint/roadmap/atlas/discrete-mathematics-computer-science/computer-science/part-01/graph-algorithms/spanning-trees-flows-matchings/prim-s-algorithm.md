---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Prim.prim, Cslib.Algorithms.Lean.Prim.prim_inspections, Cslib.Algorithms.Lean.Prim.prim_key_tests_le, Cslib.Algorithms.Lean.Prim.prim_heap_time, Cslib.Algorithms.Lean.Prim.prim_edge_inspections, Cslib.Algorithms.Lean.Prim.prim_root, Cslib.Algorithms.Lean.Prim.prim_parent_edge, Cslib.Algorithms.Lean.Prim.prim_isTree
statement: formalized
proof: formalized
---

# Prim's algorithm

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html).

## Prim's algorithm with an indexed binary heap

Let $W$ be a linearly ordered type with a
zero element, let $W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined, let $D$
be a directed adjacency structure on the vertices $0, \dots, n-1$, with vertex list $L$ and
adjacency lists $A(u)$, let $w$ assign a weight $w(\{u, v\}) \in W$ to every unordered pair
$\{u, v\}$ of vertices, not necessarily distinct, and let $r$ be a vertex. Prim's algorithm
starts with no vertex having a parent and inserts the vertices, in the order of $L$, into an
empty indexed minimum queue over the identities $0, \dots, n-1$, with key $0$ for $r$ and key
$\top$ for every other vertex. It then repeats the following at most $n$ times, stopping early
when the queue is empty: it extracts the entry of minimum key, ties broken by the smaller
vertex, say with vertex $u$, and for each entry $v$ of $A(u)$ in order, if $v$ is still in the
queue and $w(\{u, v\})$ is strictly smaller than the current key of $v$, it sets the parent of
$v$ to $u$ and decreases the key of $v$ to $w(\{u, v\})$. It returns, for each vertex, its
parent or nothing.

Costs are counted as seven numbers: the five event counts of the queue operations (comparisons,
swaps, reads of the position vector, writes to the position vector, and entry appends, pops or
replacements), the number of adjacency entries inspected, and the number of inspected entries
found still in the queue, which is the number of key comparisons. On a disconnected graph every
vertex is still extracted and the parents form a forest.

Formalized by `Cslib.Algorithms.Lean.Prim.prim`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Basic.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Basic.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim).

## Number of adjacency inspections in Prim's algorithm

Let $W$ be a linearly ordered type
with a zero element, let $D$ be a directed adjacency structure on the vertices $0, \dots, n-1$
with adjacency lists $A(u)$, let $w$ assign a weight in $W$ to every unordered pair of vertices,
not necessarily distinct, and let $r$ be a vertex. The number of adjacency entries inspected by
Prim's algorithm on $D$, $w$ and $r$ equals the sum of the lengths $|A(u)|$ over all vertices
$u$.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_inspections`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-inspections).

## Bound on key comparisons in Prim's algorithm

Let $W$ be a linearly ordered type with a
zero element, let $D$ be a directed adjacency structure on the vertices $0, \dots, n-1$ with
adjacency lists $A(u)$, let $w$ assign a weight in $W$ to every unordered pair of vertices, not
necessarily distinct, and let $r$ be a vertex. The number of inspected adjacency entries that
Prim's algorithm on $D$, $w$ and $r$ finds still in the queue, which is its number of key
comparisons, is at most the sum of the lengths $|A(u)|$ over all vertices $u$.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_key_tests_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-key-tests-le).

## Logarithmic heap cost of Prim's algorithm

Let $W$ be a linearly ordered type with a zero
element, let $D$ be a directed adjacency structure on the vertices $0, \dots, n-1$ with adjacency
lists $A(u)$, let $w$ assign a weight in $W$ to every unordered pair of vertices, not necessarily
distinct, let $r$ be a vertex, and let $a$ be the sum of the lengths $|A(u)|$ over all vertices
$u$. Each of the five heap event counts of Prim's algorithm on $D$, $w$ and $r$ (comparisons,
swaps, reads of the position vector, writes to the position vector, and entry appends, pops or
replacements) is at most $20(2n + a)(\lfloor \log_2(n + 1) \rfloor + 1) + a$.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_heap_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-heap-time).

## Adjacency inspections of Prim's algorithm on a simple graph

Let $W$ be a linearly
ordered type with a zero element, let $G$ be a simple graph on the vertices $0, \dots, n-1$, let
$D$ be a directed adjacency structure on the same vertices with adjacency lists $A(u)$, let $w$
assign a weight in $W$ to every unordered pair of vertices, not necessarily distinct, and let
$r$ be a vertex. Suppose that for all vertices $u$ and $v$, $v$ occurs in $A(u)$ exactly when
$u$ and $v$ are adjacent in $G$, and that no list $A(u)$ has repeated entries. Then the number
of adjacency entries inspected by Prim's algorithm on $D$, $w$ and $r$ is twice the number of
edges of $G$.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_edge_inspections`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Complexity.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-edge-inspections).

## The root has no parent in Prim's algorithm

Let $W$ be a linearly ordered type with a
zero element, let $D$ be a directed adjacency structure on the vertices $0, \dots, n-1$, let $w$
assign a weight in $W$ to every unordered pair of vertices, not necessarily distinct, and let
$r$ be a vertex. In the output of Prim's algorithm on $D$, $w$ and $r$, the vertex $r$ has no
parent.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_root`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-root).

## Parents returned by Prim's algorithm are adjacency-list neighbors

Let $W$ be a linearly
ordered type with a zero element, let $D$ be a directed adjacency structure on the vertices
$0, \dots, n-1$ with adjacency lists $A(u)$, let $w$ assign a weight in $W$ to every unordered
pair of vertices, not necessarily distinct, and let $r$ be a vertex. For all vertices $u$ and
$v$, if Prim's algorithm on $D$, $w$ and $r$ returns $u$ as the parent of $v$, then $v$ occurs
in $A(u)$.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_parent_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-parent-edge).

## Prim's algorithm returns a tree

Let $W$ be a linearly ordered type with a zero element,
let $G$ be a connected simple graph on the vertices $0, \dots, n-1$, let $D$ be a directed
adjacency structure on the same vertices with adjacency lists $A(u)$ such that for all vertices
$u$ and $v$, $v$ occurs in $A(u)$ exactly when $u$ and $v$ are adjacent in $G$, let $w$ assign
a weight in $W$ to every unordered pair of vertices, not necessarily distinct, and let $r$ be a
vertex. Let $T$ be the simple graph on the vertices $0, \dots, n-1$ in which two distinct
vertices are adjacent when one of them is the parent of the other in the output of Prim's
algorithm on $D$, $w$ and $r$. Then $T$ is a tree.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_isTree`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-is-tree).

## Prim's algorithm returns a minimum spanning tree

Let $G$ be a connected simple graph on
the vertices $0, \dots, n-1$, let $D$ be a directed adjacency structure on the same vertices with
adjacency lists $A(u)$ such that for all vertices $u$ and $v$, $v$ occurs in $A(u)$ exactly when
$u$ and $v$ are adjacent in $G$, let $w$ assign a real weight $w(e)$ to every unordered pair $e$
of vertices, not necessarily distinct, and let $r$ be a vertex. Let $T$ be the simple graph on
the vertices $0, \dots, n-1$ in which two distinct vertices are adjacent when one of them is the
parent of the other in the output of Prim's algorithm on $D$, $w$ and $r$, and write $E(H)$ for
the edge set of a graph $H$. Then every edge of $T$ is an edge of $G$, $T$ is a tree, and every
graph $H$ on the vertices $0, \dots, n-1$ that is a tree and whose edges are all edges of $G$
satisfies $\sum_{e \in E(T)} w(e) \le \sum_{e \in E(H)} w(e)$.

Weights are arbitrary signed real numbers, and ties are allowed.

Formalized by `Cslib.Algorithms.Lean.Prim.prim_minimum_spanningTree`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Prim/Correctness.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html#prim-minimum-spanning-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prim's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/prim-s-algorithm)
