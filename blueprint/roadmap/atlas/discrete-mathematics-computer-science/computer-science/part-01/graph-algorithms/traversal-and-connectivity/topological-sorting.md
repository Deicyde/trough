---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TopologicalSort.indegreeWithin, Cslib.Algorithms.Lean.TopologicalSort.indegree, Cslib.Algorithms.Lean.TopologicalSort.Result, Cslib.Algorithms.Lean.TopologicalSort.sort, Cslib.Algorithms.Lean.TopologicalSort.DirectedCycleIn, Cslib.Algorithms.Lean.TopologicalSort.directedCycleIn_iff, Cslib.Algorithms.Lean.TopologicalSort.IsAcyclic, Cslib.Algorithms.Lean.TopologicalSort.isAcyclic_iff_no_directedCycle
statement: formalized
proof: formalized
---

# Topological sorting

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html).

## Indegree within a vertex list

For a finite directed graph $G$, a list $R$ of vertices and
a vertex $v$, the indegree of $v$ within $R$ is the number of entries $u$ of $R$, counted with
multiplicity, such that $G$ has an edge from $u$ to $v$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.indegreeWithin`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#indegree-within).

## Indegree

The indegree of a vertex $v$ in a finite directed graph $G$ is the number of
vertices $u$ such that $G$ has an edge from $u$ to $v$; repeated entries in adjacency lists
count once.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.indegree`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#indegree).

## Outcome of Kahn's topological sort

The result of Kahn's topological sorting algorithm on a
graph with vertices of type $\alpha$ is either a success, carrying a list of vertices, or a failure,
carrying the list of vertices processed before the queue emptied and the list of vertices that
remain.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.Result`, an inductive type declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#result).

## Kahn's topological sort

Run Kahn's algorithm with a first-in first-out queue on a finite
directed graph $G$ whose vertices are enumerated as $v_1, \dots, v_n$. Initially every vertex is
remaining, the counter of each vertex is its number of in-neighbours, and the queue holds the
vertices with no in-neighbours in enumeration order. At each of $n$ steps, if the queue is nonempty,
its front vertex $x$ is removed from the queue and from the remaining vertices and appended to the
output; then each distinct out-neighbour $y$ of $x$ that is still remaining, taken in order of first
occurrence in the adjacency list of $x$, has its counter decreased by one and joins the back of the
queue if that counter was $1$. If no vertices remain after the $n$ steps, the result is a success
with the output list; otherwise it is a failure with the output list as the processed vertices and
the remaining vertices in enumeration order.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.sort`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#sort).

## Directed cycle within a vertex list

Let $G$ be a finite directed graph and $R$ a list of
vertices. A list $c = [c_1, \dots, c_k]$ of vertices is a directed cycle of $G$ in $R$ when
$k \ge 1$, the vertices $c_1, \dots, c_k$ are pairwise distinct, $G$ has an edge from $c_i$ to
$c_{i+1}$ for each $1 \le i < k$ and an edge from $c_k$ to $c_1$, and every $c_i$ lies in $R$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.DirectedCycleIn`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#directed-cycle-in).

## Characterization of directed cycles within a vertex list

Let $G$ be a finite directed
graph and let $R$ and $c = [c_1, \dots, c_k]$ be lists of vertices. Then $c$ is a directed cycle
of $G$ in $R$ if and only if $k \ge 1$, the vertices $c_1, \dots, c_k$ are pairwise distinct,
$G$ has an edge from $c_i$ to $c_{i+1}$ for every $1 \le i < k$, $G$ has an edge from $c_k$ to
$c_1$, and every $c_i$ lies in $R$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.directedCycleIn_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#directed-cycle-in-iff).

## Acyclic directed graph

A finite directed graph $G$ is acyclic when it has no directed
cycle, that is, no nonempty list $[c_1, \dots, c_k]$ of pairwise distinct vertices such that $G$
has an edge from $c_i$ to $c_{i+1}$ for each $1 \le i < k$ and an edge from $c_k$ to $c_1$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.IsAcyclic`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#is-acyclic).

## Acyclicity means having no directed cycle

A finite directed graph $G$ is acyclic if and
only if there is no directed cycle of $G$ in its vertex list, that is, no nonempty list of
pairwise distinct vertices in which each vertex has an edge to the next and the last vertex has
an edge to the first.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.isAcyclic_iff_no_directedCycle`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#is-acyclic-iff-no-directed-cycle).

## Topological order

A list $L$ of vertices of a finite directed graph $G$ is a topological
order of $G$ when $L$ has no duplicates, a vertex lies in $L$ exactly when it lies in the vertex
enumeration of $G$, and for every edge $u \to v$ of $G$ the first position of $u$ in $L$ is strictly
smaller than the first position of $v$ in $L$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.IsTopologicalOrder`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#is-topological-order).

## A successful topological sort has no repeated vertex

If Kahn's topological sort on a
finite directed graph $G$ returns a success with list $L$, then $L$ has no duplicates.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.success_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#success-nodup).

## A successful topological sort lists every vertex

If Kahn's topological sort on a finite
directed graph $G$ returns a success with list $L$, then a vertex lies in $L$ if and only if it
lies in the vertex enumeration of $G$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.success_coverage`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#success-coverage).

## A successful topological sort points every edge forward

If Kahn's topological sort on a
finite directed graph $G$ returns a success with list $L$, then for every edge $u \to v$ of $G$ the
first position of $u$ in $L$ is strictly smaller than the first position of $v$ in $L$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.success_edge_forward`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#success-edge-forward).

## A successful topological sort is a topological order

If Kahn's topological sort on a
finite directed graph $G$ returns a success with list $L$, then $L$ is a topological
order of $G$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.success_isTopologicalOrder`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#success-is-topological-order).

## A failed Kahn run splits the vertices into processed and unprocessed ones

Let $G$ be a
finite directed graph. If deterministic FIFO Kahn topological sorting of $G$ fails after
processing the vertex list $P$ and leaving the vertex list $R$ unprocessed, then $R$ is nonempty,
neither $P$ nor $R$ has repeated entries, a vertex lies in the vertex list of $G$ if and only if
it lies in $P$ or in $R$, and no vertex lies in both $P$ and $R$.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.failure_remainder`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#failure-remainder).

## Unprocessed vertices of a failed Kahn run have positive indegree among the unprocessed

Let $G$ be a finite directed graph. If deterministic FIFO Kahn topological sorting of $G$ fails
after processing the vertex list $P$ and leaving the vertex list $R$ unprocessed, then for every
vertex $v$ in $R$ the indegree of $v$ within $R$, the number of entries $u$ of $R$ such that $G$
has an edge from $u$ to $v$, is positive.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.failure_positive_indegree`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#failure-positive-indegree).

## A failed Kahn run leaves a directed cycle

Let $G$ be a finite directed graph. If
deterministic FIFO Kahn topological sorting of $G$ fails after processing the vertex list $P$
and leaving the vertex list $R$ unprocessed, then $G$ has a directed cycle in $R$: a nonempty
list of pairwise distinct vertices of $R$ in which each vertex has an edge to the next and the
last vertex has an edge to the first.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.failure_cycle`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#failure-cycle).

## Success of Kahn's algorithm implies acyclicity

If Kahn's topological sort on a finite
directed graph $G$ returns a success, then $G$ is acyclic.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.success_implies_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#success-implies-acyclic).

## Kahn's algorithm succeeds on acyclic graphs

If a finite directed graph $G$, given by a
vertex enumeration and adjacency lists, is acyclic, then deterministic FIFO Kahn topological
sorting of $G$ returns success with some vertex order.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.acyclic_implies_success`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#acyclic-implies-success).

## Kahn's algorithm succeeds exactly on acyclic graphs

For every finite directed graph $G$,
Kahn's topological sort on $G$ returns a success if and only if $G$ is acyclic.

Formalized by `Cslib.Algorithms.Lean.TopologicalSort.succeeds_iff_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean, line 1531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/TopologicalSort.lean#L1531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html#succeeds-iff-acyclic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topological sorting](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/topological-sorting)
