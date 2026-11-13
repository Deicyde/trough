---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BellmanFord.Edge, Cslib.Algorithms.Lean.BellmanFord.toDirectedAdjacency, Cslib.Algorithms.Lean.BellmanFord.pathVertices, Cslib.Algorithms.Lean.BellmanFord.pathWeight, Cslib.Algorithms.Lean.BellmanFord.IsWeightedPath, Cslib.Algorithms.Lean.BellmanFord.edge_toDirectedAdjacency_iff, Cslib.Algorithms.Lean.BellmanFord.isWeightedPath_tail, Cslib.Algorithms.Lean.BellmanFord.isWeightedPath_append_edge
statement: formalized
proof: formalized
---

# Bellman–Ford algorithm

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html).

## Weighted directed edge

A weighted directed edge on the vertices $0, \dots, n-1$ consists
of a source vertex, a target vertex and an integer weight.

Bellman-Ford takes a list of such edges, so each entry is one edge occurrence.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Edge`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#edge).

## Weight-forgetting directed graph

For a list of weighted edges on the vertices
$\{0, \dots, n-1\}$, the associated ordered directed graph enumerates its vertices as
$0, 1, \dots, n-1$, and the outgoing neighbor list of a vertex $u$ is the list of targets of the
edges of the list with source $u$, in the order in which they occur and with repetitions.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.toDirectedAdjacency`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#to-directed-adjacency).

## Vertices of a path

For a vertex $s$ of $\{0, \dots, n-1\}$ and a list of weighted edges
$e_1, \dots, e_k$ on these vertices, the vertices of the path from $s$ along this list are the
list $s, t_1, \dots, t_k$, where $t_i$ is the target of $e_i$.

The edges are not required to be consecutive.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.pathVertices`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#path-vertices).

## Bellman–Ford path weight

The weight of a list of integer-weighted edges is the sum of the
weights of its entries, an edge occurring several times being counted each time.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.pathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#path-weight).

## Weighted path in an edge list

Let $E$ be a list of weighted directed edges on the vertices
$0, \dots, n-1$. A list $P = (e_1, \dots, e_k)$ of weighted directed edges is a weighted path in $E$
from $s$ to $t$ when every $e_i$ belongs to $E$, the target of $e_i$ is the source of $e_{i+1}$ for
every $i < k$, and either $k = 0$ and $s = t$, or $k \ge 1$, the source of $e_1$ is $s$ and the
target of $e_k$ is $t$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.IsWeightedPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#is-weighted-path).

## Edges of the weight-forgetting graph

For a list $E$ of weighted directed edges on the
vertices $0, \dots, n-1$ and vertices $u$, $v$, the graph obtained from $E$ by forgetting weights
has an edge from $u$ to $v$ if and only if some edge in $E$ has source $u$ and target $v$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.edge_toDirectedAdjacency_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#edge-to-directed-adjacency-iff).

## Tail of a weighted path

Let $E$ be a list of weighted directed edges on the vertices
$0, \dots, n-1$ and let $s$ and $t$ be vertices. If the list consisting of an edge $e$ followed by
a list $R$ of edges is a weighted path in $E$ from $s$ to $t$, then $R$ is a weighted path in $E$
from the target of $e$ to $t$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.isWeightedPath_tail`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#is-weighted-path-tail).

## Appending an edge to a weighted path

Let $E$ be a list of weighted directed edges on the
vertices $0, \dots, n-1$ and let $s$, $m$ and $t$ be vertices. If $P$ is a weighted path in $E$
from $s$ to $m$ and $e$ is an edge belonging to $E$ with source $m$ and target $t$, then the list
$P$ followed by $e$ is a weighted path in $E$ from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.isWeightedPath_append_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#is-weighted-path-append-edge).

## Weight of a path with an edge appended

For every list $P$ of weighted directed edges on
the vertices $0, \dots, n-1$ and every weighted directed edge $e$ on these vertices, the weight of
the list $P$ followed by $e$ is the weight of $P$ plus the weight of $e$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.pathWeight_append_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#path-weight-append-edge).

## Weighted paths give walks of the same length

Let $E$ be a list of weighted directed
edges on the vertices $0, \dots, n-1$ and let $s$ and $t$ be vertices. If a list $P$ of $k$ edges
is a weighted path in $E$ from $s$ to $t$, then there is a walk of length $k$ from $s$ to $t$ in
the directed graph obtained from $E$ by forgetting the weights.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.isWeightedPath_walk`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#is-weighted-path-walk).

## Reachability by weighted paths

For a list of weighted edges on the vertices
$\{0, \dots, n-1\}$ and vertices $s$ and $t$, the vertex $t$ is reachable from $s$ in the directed
graph obtained from the list by forgetting the weights if and only if there is a weighted path
from $s$ to $t$ using edges of the list.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.reachable_iff_exists_isWeightedPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#reachable-iff-exists-is-weighted-path).

## Reachable negative cycle witness

For a list of weighted edges on the vertices
$\{0, \dots, n-1\}$ and a source vertex $s$, a reachable negative cycle consists of a base
vertex $b$, a weighted path $p$ from $s$ to $b$ using edges of the list whose vertices along $p$
from $s$ are pairwise distinct, and a nonempty weighted path $c$ from $b$ to $b$ using edges of
the list whose edges have pairwise distinct sources and whose weight is negative.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.ReachableNegativeCycle`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#reachable-negative-cycle).

## Existence of a reachable negative cycle

Let $E$ be a list of weighted directed edges on
the vertices $0, \dots, n-1$ and $s$ a vertex. Then $E$ has a negative cycle reachable from $s$
when there is a reachable negative cycle witness for $E$ and $s$: a base vertex $b$, a weighted
path in $E$ from $s$ to $b$ that visits no vertex twice, and a nonempty weighted path in $E$ from
$b$ to $b$ whose edge sources are pairwise distinct and whose total weight is negative.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.HasReachableNegativeCycle`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#has-reachable-negative-cycle).

## Bellman-Ford distance table

For a graph on the vertices $0, \dots, n-1$, the output of a
successful Bellman-Ford run consists of a source vertex $s$, for every vertex a distance that is
either an integer or $\infty$, and for every vertex an optional predecessor edge (a weighted
directed edge, or none).

The structure only records these values; that they are shortest-path data is proved separately.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Distances`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#distances).

## Bellman-Ford path reconstruction

Let the output of a Bellman-Ford run on $n$ vertices
have source $s$. The path to a vertex $t$ is built backwards from $t$: at a vertex $v \ne s$, take
the recorded predecessor edge $e$ of $v$, put it in front of the edges collected so far, and
continue from the source of $e$. When $s$ is reached within at most $n$ such steps, the result is
the collected list of edges (empty if $t = s$). If some vertex on the way has no predecessor edge,
or $s$ is not reached within $n$ steps, there is no result.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Distances.pathTo?`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#path-to).

## Bellman-Ford cost counters

The cost of a Bellman-Ford run is a pair of natural numbers:
the number of edge occurrences checked by relaxation passes, and the number of predecessor edges
read or emitted while reconstructing a negative-cycle witness.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Cost`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#cost).

## Total Bellman–Ford cost

The total of a Bellman–Ford cost record is its number of edge
relaxation checks plus its number of negative-cycle witness reconstruction steps.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Cost.total`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#total).

## Bellman–Ford result

For a list of weighted edges on the vertices $\{0, \dots, n-1\}$ and
a source vertex $s$, a Bellman–Ford result is either a distance record (a source vertex, an
optional integer distance for each vertex and an optional predecessor edge for each vertex) or a
reachable negative cycle witness for the list and $s$.

The type itself does not require the distances to be correct.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Result`, an inductive type declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Basic.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#result).

## Bellman–Ford algorithm

Let $E$ be a list of integer-weighted directed edges on the
vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex. Bellman–Ford run on $E$ from $s$ starts
with distance $d(s) = 0$ and $d(v) = \infty$ for every other vertex $v$, and makes $n - 1$ passes
over $E$ followed by one final pass. A pass goes through the edges of $E$ in list order, charging
one relaxation check per edge occurrence; an edge from $u$ to $v$ of weight $w$ with $d(u)$ finite
sets $d(v)$ to $d(u) + w$ and records the edge as the predecessor edge of $v$ when $d(v) = \infty$
or $d(u) + w < d(v)$. If the final pass changes no distance, the result is the distances and
predecessor edges. Otherwise, starting from the vertex whose distance the final pass changed
last, the algorithm follows $n$ predecessor edges back to a vertex $b$; it then collects the
cycle of predecessor edges through $b$, following at most $n$ predecessor edges back from $b$
until it reaches an edge with source $b$, and collects a path from $s$ to $b$ of at most $n - 1$
edges by following back from $b$ the edges by which vertices first received a finite distance.
Each lookup of a recorded edge in these three steps is charged as one witness step, also when
no edge is recorded. If all three steps succeed and give a reachable negative cycle witness for
$E$ and $s$, that witness is the result; otherwise the result is the distances and predecessor
edges.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 964](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford).

## Bellman-Ford succeeds exactly when no negative cycle is reachable

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex.
Bellman-Ford run on $E$ from $s$ returns distances if and only if there is no negative cycle
reachable from $s$, that is, no simple path from $s$ to a vertex $b$ together with a nonempty
cycle through $b$ along edges of $E$ whose edge sources are pairwise distinct and whose total
weight is negative.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_returns_distances_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-returns-distances-iff).

## Bellman-Ford reports a negative cycle exactly when one is reachable

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex.
Bellman-Ford run on $E$ from $s$ returns a reachable negative cycle witness if and only if a
negative cycle is reachable from $s$, that is, there are a simple path from $s$ to a vertex $b$
and a nonempty cycle through $b$ along edges of $E$ whose edge sources are pairwise distinct and
whose total weight is negative.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_returns_negativeCycle_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 987](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-returns-negative-cycle-iff).

## Bellman-Ford distances are realized by walks

Let $E$ be a list of integer-weighted
directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex. If Bellman-Ford run
on $E$ from $s$ returns distances $d$ and the distance $d(t)$ of a vertex $t$ is a finite integer
$\delta$, then there is a walk from $s$ to $t$ along edges of $E$ whose total weight is
$\delta$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_distance_realized`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-distance-realized).

## Bellman-Ford distances are lower bounds on walk weights

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex.
If Bellman-Ford run on $E$ from $s$ returns distances $d$, the distance $d(t)$ of a vertex $t$
is a finite integer $\delta$, and $P$ is a walk from $s$ to $t$ along edges of $E$ (vertices may
repeat), then $\delta$ is at most the total weight of $P$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_distance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1031](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1031). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-distance-minimal).

## Bellman-Ford leaves exactly the unreachable vertices at infinite distance

Let $E$ be a
list of integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a
vertex. If Bellman-Ford run on $E$ from $s$ returns distances $d$, with $\infty$ marking a vertex
that has no finite distance, then for every vertex $t$, $d(t) = \infty$ if and only if $t$ is not
reachable from $s$ in the directed graph obtained from $E$ by forgetting the weights.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_distance_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1044](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1044). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-distance-eq-none-iff).

## Bellman-Ford predecessor edges are tight

Let $E$ be a list of integer-weighted directed
edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex. Suppose Bellman-Ford run on
$E$ from $s$ returns distances $d$ together with predecessor edges, and the predecessor edge of a
vertex $t$ is an edge $e$ from $u$ to $v$ of weight $w$. Then $e$ belongs to $E$, $v = t$, and
$d(u)$ and $d(t)$ are both finite with $d(t) = d(u) + w$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_predecessor_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1055](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1055). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-predecessor-spec).

## Bellman-Ford gives the source no predecessor

Let $E$ be a list of integer-weighted
directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex. If Bellman-Ford run
on $E$ from $s$ returns distances together with predecessor edges, then $s$ has no predecessor
edge.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_source_predecessor_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1081](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1081). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-source-predecessor-eq-none).

## Bellman-Ford path reconstruction fails exactly at infinite distances

Let $E$ be a list of
integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex. If
Bellman-Ford run on $E$ from $s$ returns distances $d$, with $\infty$ marking a vertex that has
no finite distance, together with predecessor edges, then for every vertex $t$, reconstructing a
path to $t$ (following predecessor edges back from $t$ for at most $n$ steps until $s$ is
reached) fails if and only if $d(t) = \infty$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_pathTo?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1091](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1091). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-path-to-eq-none-iff).

## Bellman-Ford reconstructed paths are simple and realize the distances

Let $E$ be a list
of integer-weighted directed edges on the vertices $\{0, \dots, n-1\}$ and let $s$ be a vertex.
Suppose Bellman-Ford run on $E$ from $s$ returns distances $d$ together with predecessor edges,
and that reconstructing a path to a vertex $t$ (following predecessor edges back from $t$ for at
most $n$ steps until $s$ is reached) yields the edge sequence $P$. Then $P$ is a walk from $s$
to $t$ along edges of $E$, $d(t)$ is finite and equals the total weight of $P$, the vertex $s$
and the targets of the edges of $P$ are pairwise distinct, and $P$ has fewer than $n$ edges.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-path-to-spec).

## Predecessor paths realize the distances under a decreasing rank

Let $R$ be a
distances record on $n$ vertices with source $s$, distance table $d$ (each $d(v)$ is an integer
or infinite) and predecessor table $p$; let $E$ be a list of weighted edges; and let $r$ assign to
each vertex $v$ a natural number $r(v) < n$. Suppose that $d(s) = 0$, that every vertex $v$ with
$d(v)$ infinite has no predecessor, that every vertex $v \ne s$ with $d(v)$ finite has a
predecessor, and that whenever $p(v) = e$, the edge $e$ occurs in $E$, ends at $v$, and its start
$u$ has $d(u)$ finite, $d(v) = d(u) + w(e)$ where $w(e)$ is the weight of $e$, and $r(u) < r(v)$.
Then for every vertex $t$, following predecessors from $t$ back to $s$ for at most $n$ edges fails
exactly when $d(t)$ is infinite; and whenever it returns a path $P$ and $d(t)$ is finite, $P$ is a
path from $s$ to $t$ made of edges of $E$, its total weight is $d(t)$, and it has fewer than $n$
edges.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.Distances.pathTo?_spec_of_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean, line 1136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Correctness.lean#L1136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#path-to-spec-of-rank).

## Relaxation checks of Bellman-Ford pass by pass

For every list $E$ of weighted edges on
$n$ vertices and every source $s$, Bellman-Ford run on $E$ from $s$ charges exactly
$(n - 1) \cdot |E| + |E|$ relaxation checks, where $|E|$ is the length of $E$.

The two terms count one check per edge occurrence in each of the $n - 1$ ordinary passes and in
the final pass.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_relaxationChecks`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-relaxation-checks).

## Bellman-Ford makes exactly $n \cdot |E|$ relaxation checks

For every list $E$ of weighted
edges on $n$ vertices and every source $s$, Bellman-Ford run on $E$ from $s$ charges exactly
$n \cdot |E|$ relaxation checks, where $|E|$ is the length of $E$ counting repeated edges.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_relaxationChecks_eq_mul`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-relaxation-checks-eq-mul).

## Bellman-Ford spends at most $3n$ witness steps

For every list $E$ of weighted edges on
$n$ vertices and every source $s$, Bellman-Ford run on $E$ from $s$ charges at most $3n$
negative-cycle witness reconstruction steps.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_cycleWitnessSteps_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-cycle-witness-steps-le).

## Bellman-Ford spends no witness steps when it returns distances

For every list $E$ of
weighted edges on $n$ vertices and every source $s$, if Bellman-Ford run on $E$ from $s$ returns
distances rather than a negative cycle, then the run charges zero negative-cycle witness
reconstruction steps.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_cycleWitnessSteps_eq_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-cycle-witness-steps-eq-zero).

## Witness cost of a returned negative cycle

For every list $E$ of weighted edges on $n$
vertices and every source $s$, if Bellman-Ford run on $E$ from $s$ returns a reachable negative
cycle whose cycle has $c$ edges and whose path from $s$ to the cycle has $q$ edges, then the run
charges exactly $n + c + q$ negative-cycle witness reconstruction steps.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_cycleWitnessSteps_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-cycle-witness-steps-eq).

## Bellman-Ford makes at most $4 n |E|$ counted steps

For every list $E$ of weighted edges
on $n$ vertices and every source $s$, the total cost of Bellman-Ford run on $E$ from $s$ (its
relaxation checks plus its negative-cycle witness reconstruction steps) is at most
$4 \cdot n \cdot |E|$, where $|E|$ is the length of $E$.

Formalized by `Cslib.Algorithms.Lean.BellmanFord.bellmanFord_total_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/BellmanFord/Costs.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html#bellman-ford-total-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bellman–Ford algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/bellman-ford-algorithm)
