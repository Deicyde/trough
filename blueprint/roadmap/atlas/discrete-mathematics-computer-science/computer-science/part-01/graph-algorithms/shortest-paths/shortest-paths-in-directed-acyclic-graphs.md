---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.DAGShortestPaths.Cost, Cslib.Algorithms.Lean.DAGShortestPaths.run, Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths, Cslib.Algorithms.Lean.DAGShortestPaths.run_vertexVisits, Cslib.Algorithms.Lean.DAGShortestPaths.run_edgeRelaxations, Cslib.Algorithms.Lean.DAGShortestPaths.run_distanceUpdates_le, Cslib.Algorithms.Lean.DAGShortestPaths.run_distance_realized, Cslib.Algorithms.Lean.DAGShortestPaths.run_source
statement: formalized
proof: formalized
---

# Shortest paths in directed acyclic graphs

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html).

## Cost of the DAG shortest-path pass

The cost of the one-pass relaxation in topological
order consists of three natural-number counters: the number of vertices taken from the order, the
number of edge occurrences checked for relaxation, and the number of distance installations
(strict improvements or first finite distances).

Preparation and topological sorting are not counted.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.Cost`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#cost).

## One-pass DAG shortest-path relaxation

Let $E$ be a list of integer-weighted directed
edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a source vertex, and let
$\sigma$ be a topological order of the directed graph obtained from $E$ by forgetting weights.
The relaxation starts from distance estimate $0$ at $s$, infinite estimates at every other
vertex and no predecessor edges. It then takes the vertices $u$ of $\sigma$ in turn and relaxes
each occurrence $e$ in $E$ from $u$ to some $v$ with weight $c$, in the order of $E$: if the
estimate $d$ at $u$ is finite and the estimate at $v$ is infinite or greater than $d + c$, it
sets the estimate at $v$ to $d + c$ and the predecessor of $v$ to $e$. The result records $s$ as
its source together with the final estimates and predecessors. Its cost counts one vertex visit
per vertex of $\sigma$, one edge relaxation per occurrence relaxed, and one distance update per
estimate set.

The original edge occurrences are retained, so every parallel occurrence is checked. The proof
that $\sigma$ is a topological order is not used by the computation.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run).

## Shortest paths in a DAG with a topology check

Given a list $E$ of integer-weighted edges
on the vertices $0, \dots, n-1$ and a source $s$, run Kahn's topological sort on the directed graph
obtained from $E$ by forgetting weights. If it succeeds with order $\sigma$, start from distance
$0$ at $s$ and $\infty$ elsewhere, relax the outgoing edge occurrences of each vertex in the order
$\sigma$, and return the resulting distances and predecessor edges. If it fails after processing
the list $P$ of vertices and leaving the list $R$, return the error $(P, R)$. Only the relaxation
pass is charged in the recorded cost.

Failure preserves the sorter's processed and remaining lists; it does not return a cycle list.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths).

## The DAG shortest-path pass is charged one vertex visit per vertex

Let $E$ be a list of
integer-weighted directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a
source vertex, and let $\sigma$ be a topological order of the directed graph obtained from $E$
by forgetting weights. The one-pass DAG shortest-path relaxation of $E$ from $s$ in the order
$\sigma$ is charged exactly $n$ vertex visits.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_vertexVisits`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-vertex-visits).

## Edge relaxation count of the DAG pass

Let $E$ be a list of integer-weighted edges on $n$
vertices, $s$ a source, and $\sigma$ a topological order of the directed graph obtained from $E$ by
forgetting weights. In the cost of the one-pass relaxation from $s$ in the order $\sigma$, the
number of edge relaxations equals the length of $E$, with identical duplicate edges counted
separately.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_edgeRelaxations`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-edge-relaxations).

## Distance updates are bounded by edge relaxations

Let $E$ be a list of integer-weighted
edges on $n$ vertices, $s$ a source, and $\sigma$ a topological order of the directed graph
obtained from $E$ by forgetting weights. In the cost of the one-pass relaxation from $s$ in the
order $\sigma$, the number of distance installations is at most the number of edge relaxations.

Only actual strict improvements or first finite estimates install a predecessor.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_distanceUpdates_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-distance-updates-le).

## Finite DAG distances are path weights

Let $E$ be a list of integer-weighted edges on $n$
vertices, $s$ a source, and $\sigma$ a topological order of the directed graph obtained from $E$ by
forgetting weights. If the one-pass relaxation from $s$ in the order $\sigma$ gives a vertex $t$
the finite distance $d$, then there is a path from $s$ to $t$ made of edge occurrences of $E$
whose edge weights sum to $d$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_distance_realized`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-distance-realized).

## The DAG shortest-path pass keeps its source

Let $E$ be a list of integer-weighted
directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a source vertex, and
let $\sigma$ be a topological order of the directed graph obtained from $E$ by forgetting
weights. The result of the one-pass DAG shortest-path relaxation of $E$ from $s$ in the order
$\sigma$ records $s$ as its source.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_source`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-source).

## The DAG shortest-path pass gives the source distance zero

Let $E$ be a list of
integer-weighted directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a
source vertex, and let $\sigma$ be a topological order of the directed graph obtained from $E$
by forgetting weights. The one-pass DAG shortest-path relaxation of $E$ from $s$ in the order
$\sigma$ ends with distance estimate $0$ at $s$.

This holds even when edges of negative weight enter $s$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_source_distance`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-source-distance).

## The source has no DAG shortest-path predecessor

Let $E$ be a list of integer-weighted
directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a source vertex, and
let $\sigma$ be a topological order of the directed graph obtained from $E$ by forgetting
weights. The one-pass DAG shortest-path relaxation of $E$ from $s$ in the order $\sigma$ records
no predecessor edge for $s$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_source_predecessor`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-source-predecessor).

## Finite DAG distances are at most every path weight

Let $E$ be a list of integer-weighted
edges on $n$ vertices, $s$ a source, and $\sigma$ a topological order of the directed graph
obtained from $E$ by forgetting weights. If the one-pass relaxation from $s$ in the order $\sigma$
gives a vertex $t$ the finite distance $d$, then $d \le w(p)$ for every path $p$ from $s$ to $t$
made of edge occurrences of $E$, where $w(p)$ is the sum of the weights of the edges of $p$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_distance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 902](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L902). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-distance-minimal).

## Infinite DAG distances are exactly unreachable vertices

Let $E$ be a list of
integer-weighted edges on $n$ vertices, $s$ a source, and $\sigma$ a topological order of the
directed graph $G$ obtained from $E$ by forgetting weights. For every vertex $t$, the one-pass
relaxation from $s$ in the order $\sigma$ leaves the distance of $t$ infinite if and only if $t$ is
not reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_distance_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 914](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L914). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-distance-eq-none-iff).

## Predecessor edges of the DAG shortest-path pass

Let $E$ be a list of integer-weighted
directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a source vertex, and
let $\sigma$ be a topological order of the directed graph obtained from $E$ by forgetting
weights. Suppose the one-pass DAG shortest-path relaxation of $E$ from $s$ in the order $\sigma$
records an edge occurrence $e$ from $u$ to $w$ with weight $c$ as the predecessor of a vertex
$v$. Then $e$ occurs in $E$, $w = v$, and there is an integer $d$ such that the final distance
estimate at $u$ is $d$, the final distance estimate at $v$ is $d + c$, and the position of $u$
in $\sigma$ is less than the position of $v$ in $\sigma$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_predecessor_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 934](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L934). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-predecessor-spec).

## Unreached vertices have no DAG shortest-path predecessor

Let $E$ be a list of
integer-weighted directed edge occurrences on the vertices $\{0, \dots, n-1\}$, let $s$ be a
source vertex, and let $\sigma$ be a topological order of the directed graph obtained from $E$
by forgetting weights. If the one-pass DAG shortest-path relaxation of $E$ from $s$ in the
order $\sigma$ ends with an infinite distance estimate at a vertex $v$, then it records no
predecessor edge for $v$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_infinite_predecessor`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 948](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L948). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-infinite-predecessor).

## Finite non-source vertices have predecessors

Let $E$ be a list of integer-weighted edges on
$n$ vertices, $s$ a source, and $\sigma$ a topological order of the directed graph obtained from $E$
by forgetting weights. If the one-pass relaxation from $s$ in the order $\sigma$ gives a vertex
$t \ne s$ a finite distance, then it records a predecessor edge for $t$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_finite_predecessor`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 956](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L956). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-finite-predecessor).

## Successful output of DAG shortest paths

For a list $E$ of integer-weighted edges on $n$
vertices, a source $s$, and a distance record $D$, the DAG shortest-path algorithm on $E$ from $s$
returns $D$ if and only if there is a topological order $\sigma$ of the directed graph obtained
from $E$ by forgetting weights such that Kahn's topological sort of that graph succeeds with
$\sigma$ and $D$ is the result of the one-pass relaxation from $s$ in the order $\sigma$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_eq_ok_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 965](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L965). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-eq-ok-iff).

## Failure output of DAG shortest paths

For a list $E$ of integer-weighted edges on $n$
vertices, a source $s$, and lists $P$ and $R$ of vertices, the DAG shortest-path algorithm on $E$
from $s$ returns the error $(P, R)$ if and only if Kahn's topological sort of the directed graph
obtained from $E$ by forgetting weights fails after processing $P$ and leaving $R$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_eq_error_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean, line 993](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Basic.lean#L993). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-eq-error-iff).

## Predecessor extraction fails exactly at infinite distances

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$, $s$ a source vertex, and
$\sigma$ a topological order of the directed graph with an edge $u \to v$ for each edge of $E$
from $u$ to $v$. After the one-pass relaxation of $E$ from $s$ in the order $\sigma$, for every
vertex $t$, following the predecessor edges back from $t$ fails to reach $s$ within $n$ steps if
and only if the computed distance to $t$ is infinite.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_pathTo?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-path-to-eq-none-iff).

## Paths extracted after topological relaxation are shortest paths

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$, $s$ a source vertex, and
$\sigma$ a topological order of the directed graph with an edge $u \to v$ for each edge of $E$
from $u$ to $v$. After the one-pass relaxation of $E$ from $s$ in the order $\sigma$, suppose
following the predecessor edges back from a vertex $t$ reaches $s$ within $n$ steps, giving the
path $P$. Then $P$ is a path from $s$ to $t$ in $E$, the computed distance to $t$ is finite and
equals the weight of $P$, $P$ has fewer than $n$ edges, and every path from $s$ to $t$ in $E$ has
weight at least the weight of $P$. Here a path from $s$ to $t$ in $E$ is a list of edges of $E$,
each starting where the previous one ends, the first starting at $s$ and the last ending at $t$
(the empty list when $t = s$), and its weight is the sum of its edge weights.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.run_pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#run-path-to-spec).

## A failed DAG shortest-path run exhibits a cycle

Let $E$ be a list of integer-weighted
directed edges on the vertices $\{0, \dots, n-1\}$ and $s$ a source vertex. If the DAG
shortest-path algorithm on $E$ from $s$ fails, reporting the processed vertices and the list $R$
of remaining vertices of its topological sort, then the directed graph with an edge $u \to v$ for
each edge of $E$ from $u$ to $v$ contains a nonempty directed cycle without repeated vertices
whose vertices all lie in $R$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_failure_cycle`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-failure-cycle).

## The DAG shortest-path algorithm succeeds exactly on acyclic graphs

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and $s$ a source vertex. The
DAG shortest-path algorithm on $E$ from $s$ succeeds if and only if the directed graph with an
edge $u \to v$ for each edge of $E$ from $u$ to $v$ has no directed cycle.

This includes disconnected graphs: a cycle unreachable from $s$ still causes failure.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_returns_iff_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-returns-iff-acyclic).

## DAG shortest-path distances are shortest-path weights

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and $s$ a source vertex.
Suppose the DAG shortest-path algorithm on $E$ from $s$ succeeds and returns a finite distance
$d \in \mathbb{Z}$ for a vertex $t$. Then some path from $s$ to $t$ in $E$ has weight $d$, and
every path from $s$ to $t$ in $E$ has weight at least $d$. Here a path from $s$ to $t$ in $E$ is a
list of edges of $E$, each starting where the previous one ends, the first starting at $s$ and
the last ending at $t$ (the empty list when $t = s$), and its weight is the sum of its edge
weights.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_distance_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-distance-spec).

## Unreachable vertices are exactly those at infinite DAG distance

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and $s$ a source vertex.
If the DAG shortest-path algorithm on $E$ from $s$ succeeds, then for every vertex $t$ the
returned distance to $t$ is infinite if and only if $t$ is not reachable from $s$ in the directed
graph with an edge $u \to v$ for each edge of $E$ from $u$ to $v$.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_distance_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-distance-eq-none-iff).

## Extracted DAG shortest paths are shortest paths

Let $E$ be a list of integer-weighted
directed edges on the vertices $\{0, \dots, n-1\}$ and $s$ a source vertex. Suppose the DAG
shortest-path algorithm on $E$ from $s$ succeeds, and following its predecessor edges back from a
vertex $t$ reaches $s$ within $n$ steps, giving the path $P$. Then $P$ is a path from $s$ to $t$
in $E$, the returned distance to $t$ is finite and equals the weight of $P$, $P$ has fewer than
$n$ edges, and every path from $s$ to $t$ in $E$ has weight at least the weight of $P$. Here a
path from $s$ to $t$ in $E$ is a list of edges of $E$, each starting where the previous one ends,
the first starting at $s$ and the last ending at $t$ (the empty list when $t = s$), and its weight
is the sum of its edge weights.

Formalized by `Cslib.Algorithms.Lean.DAGShortestPaths.dagShortestPaths_pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/DAG/Correctness.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html#dag-shortest-paths-path-to-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shortest paths in directed acyclic graphs](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/shortest-paths-in-directed-acyclic-graphs)
