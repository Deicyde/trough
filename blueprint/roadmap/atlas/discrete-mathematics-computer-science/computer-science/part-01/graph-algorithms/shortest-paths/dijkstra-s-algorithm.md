---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.DirectedAdjacency.pathWeight, Cslib.Algorithms.Lean.DirectedAdjacency.HasPathWeight, Cslib.Algorithms.Lean.DirectedAdjacency.reachable_iff_exists_hasPathWeight, Cslib.Algorithms.Lean.DirectedAdjacency.adjacencyEntryCount, Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraCost, Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraCost.total, Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraResult, Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraResult.pathTo?
statement: formalized
proof: formalized
---

# Dijkstra's algorithm

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html).

## Endpoint-weight sum along a vertex list

Given a weight $w(u, v) \in \mathbb{N}$ for each
ordered pair of vertices, the weight of a list of vertices $v_0, v_1, \dots, v_k$ is
$w(v_0, v_1) + w(v_1, v_2) + \dots + w(v_{k-1}, v_k)$. In particular the empty list and every
one-vertex list have weight $0$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.pathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#path-weight).

## Walks of a given weight

Let $G$ be a directed graph given by adjacency lists, let
$w(u, v) \in \mathbb{N}$ be a weight for each ordered pair of vertices, let $s$ and $t$ be
vertices and let $d$ be a natural number. Then $s$ reaches $t$ with weight $d$ when there is a
nonempty list of vertices $v_0, v_1, \dots, v_k$ with $v_0 = s$, $v_k = t$ and each $v_{i+1}$ in
the adjacency list of $v_i$, such that $w(v_0, v_1) + \dots + w(v_{k-1}, v_k) = d$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.HasPathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#has-path-weight).

## Reachability via weighted walks

Let $G$ be a directed graph given by adjacency lists and
let $w(u, v) \in \mathbb{N}$ be a weight for each ordered pair of vertices. For vertices $s$ and
$t$, $t$ is reachable from $s$ in $G$ if and only if there is a natural number $d$ such that $s$
reaches $t$ with weight $d$ with respect to $w$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.reachable_iff_exists_hasPathWeight`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#reachable-iff-exists-has-path-weight).

## Adjacency entry count

For a directed graph $G$ given by an out-neighbour list
$\mathrm{adj}(v)$ for each vertex $v$, the adjacency entry count of $G$ is the total length
$\sum_{v} |\mathrm{adj}(v)|$ of these lists over all vertices $v$, so repeated entries and
self-loops are counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.adjacencyEntryCount`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#adjacency-entry-count).

## Cost of dense Dijkstra

A Dijkstra cost is a pair of natural numbers that counts two
kinds of events separately: the number of vertex entries inspected during minimum selection,
and the number of adjacency-list entries inspected during relaxation.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraCost`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-cost).

## Total Dijkstra cost

The total of a Dijkstra cost record is its number of vertex entries
inspected by minimum selection plus its number of adjacency entries inspected by relaxation.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraCost.total`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#total).

## Output of Dijkstra's algorithm

For vertices $0, \dots, n-1$, a Dijkstra result consists
of a source vertex $s$, a distance entry $d(v)$ for each vertex $v$ that is either a natural
number or $\infty$, and a predecessor entry $p(v)$ for each vertex $v$ that is either a vertex or
undefined. The entries are stored as arrays of length $n$; $d(v)$ is meant as the computed
distance from $s$ to $v$ and $p(v)$ as the vertex before $v$ on a shortest path from $s$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraResult`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-result).

## Path recovery from Dijkstra predecessors

Let a Dijkstra result on $n$ vertices have
source $s$ and predecessor entries $p$. The path to a vertex $t$ follows predecessors backwards:
starting from $u_0 = t$, as long as $u_i \ne s$ it sets $u_{i+1} = p(u_i)$. If $u_k = s$ for
some $k \le n$, the result is the list $u_k, u_{k-1}, \dots, u_0$ from $s$ to $t$. If some
$p(u_i)$ is undefined before $s$ is reached, or $s$ is not reached within $n$ steps, there is no
result.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.DijkstraResult.pathTo?`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#path-to).

## Dense Dijkstra's algorithm

Let $G$ be a directed graph on the vertices $0, \dots, n-1$
given by a fixed enumeration of its vertices and adjacency lists, let $w(u, v) \in \mathbb{N}$ be
a weight for each ordered pair of vertices, and let $s$ be a source vertex. The algorithm starts
with $d(s) = 0$, $d(v) = \infty$ for $v \ne s$, no predecessors and no settled vertices, and runs
$n$ rounds. In each round it scans all vertices in the order of the enumeration of $G$ and
selects the first unsettled vertex $u$ in that order whose value $d(u)$ is minimal among
unsettled vertices; if every vertex is settled the round does nothing. Otherwise it marks $u$
settled and, for each entry $v$ of the adjacency list of $u$ in order, if $v$ is unsettled,
$d(u)$ is finite and $d(u) + w(u, v) < d(v)$, it sets $d(v) := d(u) + w(u, v)$ and makes $u$ the
predecessor of $v$. The result is $s$ together with the final distances and predecessors. The
cost charges one minimum-selection step for each vertex inspected during selection and one
relaxation step for each adjacency entry inspected during relaxation.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra).

## Dijkstra's finite distances are realized by walks

Let $G$ be a directed graph on the
vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every ordered pair of
vertices, and let $s$ and $t$ be vertices. If Dijkstra's algorithm on $G$ with weights $w$ from
source $s$ outputs a finite distance $d$ for $t$, then $G$ has a walk
$s = v_0, v_1, \dots, v_k = t$, with an edge from each $v_{i-1}$ to $v_i$, of weight
$\sum_{i=1}^{k} w(v_{i-1}, v_i) = d$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_distance_realized`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1693](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-distance-realized).

## Dijkstra's finite distances are lower bounds on walk weights

Let $G$ be a directed graph
on the vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every ordered pair
of vertices, and let $s$ and $t$ be vertices. If Dijkstra's algorithm on $G$ with weights $w$
from source $s$ outputs a finite distance $d$ for $t$, then $d \le d'$ for every walk
$s = v_0, v_1, \dots, v_k = t$ in $G$ (with an edge from each $v_{i-1}$ to $v_i$) of weight
$d' = \sum_{i=1}^{k} w(v_{i-1}, v_i)$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_distance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-distance-minimal).

## Dijkstra's distance is infinite exactly at unreachable vertices

Let $G$ be a directed
graph on the vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every
ordered pair of vertices, and let $s$ and $t$ be vertices. The distance to $t$ output by
Dijkstra's algorithm on $G$ with weights $w$ from source $s$ is infinite if and only if $t$ is
not reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_distance_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1714](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-distance-eq-none-iff).

## Dijkstra's predecessor pointers satisfy the distance equation

Let $G$ be a directed
graph on the vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every
ordered pair of vertices, and let $s$, $t$ and $p$ be vertices. If Dijkstra's algorithm on $G$
with weights $w$ from source $s$ outputs $p$ as the predecessor of $t$, then $G$ has an edge
from $p$ to $t$, the distances $d(p)$ and $d(t)$ output for $p$ and $t$ are both finite, and
$d(t) = d(p) + w(p, t)$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_predecessor_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1735](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-predecessor-spec).

## Dijkstra's path reconstruction fails exactly at infinite distance

Let $G$ be a directed
graph on the vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every
ordered pair of vertices, and let $s$ and $t$ be vertices. Reconstructing a path from $s$ to
$t$ by following, for at most $n$ steps, the predecessor pointers output by Dijkstra's
algorithm on $G$ with weights $w$ from source $s$ fails if and only if the distance output
for $t$ is infinite.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_pathTo?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1879](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1879). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-path-to-eq-none-iff).

## Reconstructed Dijkstra paths are simple and have the output weight

Let $G$ be a directed
graph on the vertices $0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every
ordered pair of vertices, and let $s$ and $t$ be vertices. Suppose that following the
predecessor pointers output by Dijkstra's algorithm on $G$ with weights $w$ from source $s$
reconstructs a list of vertices $P$ for $t$. Then $P$ is nonempty, say $P = v_0, \dots, v_k$,
with $v_0 = s$ and $v_k = t$; there is an edge from each $v_{i-1}$ to $v_i$; the $v_i$ are
pairwise distinct; and the distance $d$ output for $t$ is finite with
$d = \sum_{i=1}^{k} w(v_{i-1}, v_i)$.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1914](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1914). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-path-to-spec).

## Relaxation count of dense Dijkstra

Let $G$ be a directed graph on the vertices
$0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every ordered pair of vertices,
and let $s$ be a vertex. The number of adjacency-list entries that Dijkstra's algorithm on $G$
with weights $w$ from source $s$ inspects during relaxation equals the adjacency entry count
of $G$, the total length of all out-neighbour lists.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_edgeRelaxations`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1945](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1945). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-edge-relaxations).

## Minimum-selection count of dense Dijkstra

Let $G$ be a directed graph on the vertices
$0, \dots, n-1$, let $w(u, v)$ be a natural-number weight for every ordered pair of vertices,
and let $s$ be a vertex. Dijkstra's algorithm on $G$ with weights $w$ from source $s$ inspects
exactly $n^2$ vertex entries during minimum selection.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_minScans`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1976](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1976). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-min-scans).

## Running time of dense Dijkstra

Let $G$ be a directed graph on the vertices
$0, \dots, n-1$ given by adjacency lists, let $w(u, v) \in \mathbb{N}$ be a weight for each
ordered pair of vertices, and let $s$ be a vertex. For dense Dijkstra from $s$, the number of
vertex entries inspected by minimum selection plus the number of adjacency entries inspected by
relaxation is exactly $n^2 + m$, where $m$ is the number of adjacency-list entries of $G$,
counting duplicates and self-loops.

Formalized by `Cslib.Algorithms.Lean.DirectedAdjacency.dijkstra_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean, line 1983](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Dijkstra.lean#L1983). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html#dijkstra-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dijkstra's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/dijkstra-s-algorithm)
