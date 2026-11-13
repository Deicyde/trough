---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BreadthFirstSearch.BFSResult, Cslib.Algorithms.Lean.BreadthFirstSearch.bfsModel, Cslib.Algorithms.Lean.BreadthFirstSearch.bfs, Cslib.Algorithms.Lean.BreadthFirstSearch.bfs_eq_bfsModel, Cslib.Algorithms.Lean.BreadthFirstSearch.bfsFin, Cslib.Algorithms.Lean.BreadthFirstSearch.distance_present_iff_reachable, Cslib.Algorithms.Lean.BreadthFirstSearch.order_mem_iff_reachable, Cslib.Algorithms.Lean.BreadthFirstSearch.order_nodup
statement: formalized
proof: formalized
---

# Breadth-first search

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html).

## Result of breadth-first search

A breadth-first search result on a vertex type $V$
consists of a distance function, assigning to each vertex either a natural number or none,
and a list of vertices. They are meant to record the shortest distance from the source (none
when the vertex is unreachable) and the vertices in first-discovery order.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSResult`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfsresult).

## List model of breadth-first search

Given a finite directed graph $G$ with ordered
adjacency lists and a source vertex $s$, the list model keeps a list of processed pairs and a
queue of pairs $(v, d)$ of a vertex and a distance, starting with no processed pairs and the
queue $[(s, 0)]$. It performs one round per vertex of $G$: if the queue is empty, nothing
changes; otherwise the front pair $(u, d)$ is removed from the queue and recorded as processed,
and then each entry $w$ of the adjacency list of $u$, from left to right, is appended to the
queue as $(w, d + 1)$ unless $w$ already occurs in a processed or queued pair. The reported
distance of a vertex $v$ is the distance in the first pair for $v$ in the list of processed pairs
in processing order followed by the queue, or none if there is no such pair; the reported order
lists the processed vertices in processing order.

The model can be evaluated by kernel reduction, which is used to check concrete results.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsModel`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-model).

## Breadth-first search

Given a finite directed graph $G$ with ordered adjacency lists and a
source vertex $s$, breadth-first search keeps a FIFO queue of pairs $(v, d)$ of a vertex and a
distance and a table of discovered vertices with their distances, starting with the queue
$[(s, 0)]$ and $s$ discovered at distance $0$. It performs one round per vertex of $G$: if the
queue is empty, nothing changes; otherwise it dequeues the front pair $(u, d)$, records $u$ as
processed, and scans the adjacency list of $u$ from left to right, enqueueing each entry $w$ that
is not yet discovered as $(w, d + 1)$ and discovering it at distance $d + 1$. The result reports
for each vertex its discovered distance, or none if it was never discovered, and lists the
processed vertices in processing order.

The table is a hash map, so the search runs in expected time linear in the number of vertices
plus the total length of the adjacency lists.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfs`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs).

## The executable BFS agrees with the list model

For every finite directed graph $G$ with
ordered adjacency lists and every source vertex $s$, the result of the executable breadth-first
search from $s$ equals the result of the list model of breadth-first search from $s$: both
report the same distance (or none) for every vertex and the same first-discovery order.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfs_eq_bfsModel`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1009](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1009). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-eq-bfs-model).

## Breadth-first search on the vertices $0, \dots, n-1$

Given a natural number $n$, an
adjacency function assigning to each vertex $i < n$ an ordered list of vertices among
$0, \dots, n-1$, and a source vertex $s < n$, this is the result of breadth-first search from $s$
on the finite directed graph with vertex enumeration $0, 1, \dots, n-1$ and these adjacency
lists.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsFin`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1026](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1026). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-fin).

## BFS reports a distance exactly for the reachable vertices

For every finite directed graph
$G$ with ordered adjacency lists and all vertices $s$ and $v$, breadth-first search from $s$
reports some distance for $v$ (rather than none) if and only if $v$ is reachable from $s$
in $G$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.distance_present_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1047](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1047). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#distance-present-iff-reachable).

## BFS lists exactly the reachable vertices

For every finite directed graph $G$ with ordered
adjacency lists and all vertices $s$ and $v$, the vertex $v$ occurs in the first-discovery order
of breadth-first search from $s$ if and only if $v$ is reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.order_mem_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1059](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1059). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#order-mem-iff-reachable).

## BFS discovers each vertex at most once

For every finite directed graph $G$ with ordered
adjacency lists and every vertex $s$, no vertex occurs twice in the first-discovery order of
breadth-first search from $s$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.order_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1073](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1073). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#order-nodup).

## BFS reports exactly the shortest walk length

For every finite directed graph $G$ with
ordered adjacency lists, all vertices $s$ and $v$, and every natural number $d$, breadth-first
search from $s$ reports distance $d$ for $v$ if and only if there is a walk of exactly $d$ edges
from $s$ to $v$ in $G$ and $d \le k$ for every natural number $k$ such that there is a walk of
exactly $k$ edges from $s$ to $v$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.distance_eq_some_iff_shortest`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1081](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1081). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#distance-eq-some-iff-shortest).

## Breadth-first search places the source at distance zero

For every finite directed graph
$G$ given by ordered adjacency lists and every vertex $s$ of $G$, breadth-first search in $G$
from $s$ reports a distance for $s$ itself, and that distance is $0$ edges.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.source_distance`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#source-distance).

## BFS discovers vertices in nondecreasing distance

For every finite directed graph $G$ with
ordered adjacency lists and every vertex $s$, the distances reported by breadth-first search
from $s$, listed along its first-discovery order, form a nondecreasing sequence, where a vertex
without a reported distance counts as $0$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.order_distances_nondecreasing`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean, line 1108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch.lean#L1108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#order-distances-nondecreasing).

## Breadth-first search forest

A breadth-first search forest on a vertex type $V$ consists
of a breadth-first search result, namely a partial distance function from $V$ to the natural
numbers and a list of vertices, together with a partial predecessor function from $V$ to $V$.
For a search from a source vertex $s$, these are meant to give the distance from $s$ of each
reachable vertex, the reachable vertices in first-discovery order, and the vertex from which
each reachable vertex other than $s$ was first discovered, with $s$ and the unreachable vertices
having no predecessor; the structure itself imposes none of these properties.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfsforest).

## Breadth-first search with parent pointers

Given a finite directed graph $G$ on a vertex
type $V$, with ordered adjacency lists, and a source vertex $s$, this runs first-in-first-out
breadth-first search from $s$ for $|V|$ rounds. The queue starts with $s$ at distance $0$. Each
round tries to dequeue a vertex $u$; if it succeeds, it scans the neighbors of $u$ in
adjacency-list order, and each neighbor not yet discovered gets distance one more than $u$,
records $u$ as its parent and is enqueued. An already discovered vertex keeps its distance and
parent. The result is the search forest: the distance of each discovered vertex, the vertices in
the order they were dequeued, and the parent of each discovered vertex other than $s$. The cost
counts one unit for each dequeue attempt, each check of an adjacency entry against the
discovered set, each enqueue (including that of $s$) and each parent write.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsWithParents`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-with-parents).

## Path reconstruction from BFS parents

Let $p$ be the predecessor function of a
breadth-first search forest, let $n$ be the length of its discovery order, and let $s$ and $t$ be
vertices. Starting from $v_k = t$, this walks back along $p$, setting $v_{i-1} = p(v_i)$,
until it reaches a vertex $v_0$ that tests equal to $s$, and returns the list
$v_0, v_1, \dots, v_k$. It returns no list if the walk meets a vertex that does not test equal to
$s$ and has no predecessor, or if none of the first $n + 1$ vertices $t, p(t), \dots$ of the walk
tests equal to $s$. The cost counts one unit for each test against $s$, each predecessor lookup
and each vertex prepended to the list.

The bound $n$ makes the walk terminate even when the predecessor table contains a cycle.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Internal.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to).

## Breadth-first search with parents returns the ordinary BFS result

For every finite
directed graph $G$ with ordered adjacency lists and every source vertex $s$, the output of
breadth-first search with parents from $s$ in $G$, with its cost and its predecessor table
forgotten, equals the result of ordinary FIFO breadth-first search from $s$ in $G$: the same
distance table and the same first-discovery order.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsWithParents_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-with-parents-ret).

## Exactly the source and the unreachable vertices have no BFS parent

Let $G$ be a finite
directed graph with ordered adjacency lists, $s$ a vertex, and $F$ the predecessor forest
computed by breadth-first search with parents from $s$ in $G$. A vertex $v$ has no recorded
predecessor in $F$ if and only if $v = s$ or $v$ is not reachable from $s$ along directed edges
of $G$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-eq-none-iff).

## BFS parents are joined by graph edges

Let $G$ be a finite directed graph with ordered
adjacency lists, $s$ a vertex, and $F$ the predecessor forest computed by breadth-first search
with parents from $s$ in $G$. If $F$ records $p$ as the predecessor of a vertex $v$, then $G$ has
a directed edge from $p$ to $v$, that is, $v$ occurs in the adjacency list of $p$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-edge).

## A BFS parent is one step closer to the source

Let $G$ be a finite directed graph with
ordered adjacency lists, $s$ a vertex, and $F$ the predecessor forest computed by breadth-first
search with parents from $s$ in $G$. If $F$ records $p$ as the predecessor of a vertex $v$, then
there is a natural number $d$ such that $F$ records distance $d$ for $p$ and distance $d + 1$
for $v$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_distance`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-distance).

## The BFS parent is the first discovered in-neighbour

Let $G$ be a finite directed graph
with ordered adjacency lists, $s$ a vertex, and $F$ the predecessor forest computed by
breadth-first search with parents from $s$ in $G$. For every vertex $v \ne s$, the predecessor
that $F$ records for $v$ is the first vertex $u$, in the first-discovery order of ordinary FIFO
breadth-first search from $s$ in $G$, whose adjacency list contains $v$; if no vertex in that
order has $v$ in its adjacency list, $F$ records no predecessor for $v$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_eq_find?`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-eq-find).

## Each reachable vertex has a unique saved-parent chain

Let $G$ be a finite directed graph
given by adjacency lists, and let $s$ and $v$ be vertices with $v$ reachable from $s$ in $G$.
There is exactly one list of vertices that starts at $s$, ends at $v$, and in which each vertex
after the first has the preceding vertex as its saved parent in the breadth-first search forest
of $G$ from $s$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_chain_unique`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-chain-unique).

## Saved-parent chains are simple

Let $G$ be a finite directed graph given by adjacency
lists and let $s$ and $v$ be vertices. If a list of vertices starts at $s$, ends at $v$, and each
of its vertices after the first has the preceding vertex as its saved parent in the breadth-first
search forest of $G$ from $s$, then no vertex occurs twice in the list.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_chain_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-chain-nodup).

## The saved-parent relation is acyclic

Let $G$ be a finite directed graph given by
adjacency lists and let $s$ and $v$ be vertices. In the breadth-first search forest of $G$ from
$s$, there is no sequence $v = x_0, x_1, \dots, x_k = v$ with $k \ge 1$ in which each $x_i$ is
the saved parent of $x_{i+1}$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.predecessor_relation_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#predecessor-relation-acyclic).

## Path reconstruction at the source

For every breadth-first search forest $F$ and every
vertex $s$, following the saved parents of $F$ from $s$ back to $s$ returns the one-vertex path
$[s]$. This holds for every forest, including one whose discovery order is empty.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?_source`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to-source).

## Path reconstruction fails exactly at unreachable vertices

Let $G$ be a finite directed
graph given by adjacency lists, and let $s$ and $v$ be vertices. Following the saved parents of the
breadth-first search forest of $G$ from $s$ back from $v$ towards $s$ returns no path if and only
if $v$ is not reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to-eq-none-iff).

## Reconstructed BFS paths are shortest paths

Let $G$ be a finite directed graph given by
adjacency lists, let $s$ and $v$ be vertices, and suppose that following the saved parents of the
breadth-first search forest of $G$ from $s$ back from $v$ returns a list $P$ of vertices. Then $P$
starts at $s$ and ends at $v$, each vertex of $P$ after the first has the preceding vertex as its
saved parent, $G$ has an edge from each vertex of $P$ to the next, no vertex occurs twice in $P$,
breadth-first search from $s$ reports a distance $d$ for $v$ and $P$ has $d + 1$ vertices, and
every list of vertices from $s$ to $v$ such that $G$ has an edge from each of its vertices to the
next has at least as many vertices as $P$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to-spec).

## Cost of path reconstruction for a reachable vertex

Let $G$ be a finite directed graph
given by adjacency lists, let $s$ and $v$ be vertices, and suppose breadth-first search from $s$
reports distance $d$ for $v$. Following the saved parents of the breadth-first search forest of
$G$ from $s$ back from $v$ costs exactly $3d + 2$, counting one unit for each comparison with $s$,
each parent lookup and each vertex prepended to the path.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to-time).

## Cost of path reconstruction for an unreachable vertex

Let $G$ be a finite directed graph
given by adjacency lists, and let $s$ and $v$ be vertices with $v$ not reachable from $s$ in $G$.
Following the saved parents of the breadth-first search forest of $G$ from $s$ back from $v$ costs
exactly $2$, counting one unit for each comparison with $s$, each parent lookup and each vertex
prepended to the path: one comparison of $v$ with $s$ and one lookup of the missing parent of
$v$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.BFSForest.pathTo?_time_of_not_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Correctness.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#path-to-time-of-not-reachable).

## Exact cost of BFS with parents

Let $G$ be a finite directed graph with vertex list $V$
and adjacency lists $\mathrm{adj}(u)$, let $s$ be a vertex, and let $L$ be the list of vertices in
the order in which breadth-first search from $s$ discovers them. The cost of breadth-first search
with parents from $s$, counting dequeue attempts, adjacency checks, enqueues and parent writes,
equals $|V| + \sum_{u \in L} |\mathrm{adj}(u)| + |L| + (|L| - 1)$, where adjacency lists are
counted with repetitions and $|L| - 1$ is truncated at $0$.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsWithParents_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Costs.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Costs.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-with-parents-time).

## Linear bound on the cost of BFS with parents

Let $G$ be a finite directed graph with
vertex list $V$ and adjacency lists $\mathrm{adj}(u)$, and let $s$ be a vertex. The cost of
breadth-first search with parents from $s$, counting dequeue attempts, adjacency checks, enqueues
and parent writes, is at most $3|V| + \sum_{u \in V} |\mathrm{adj}(u)|$, where adjacency lists
are counted with repetitions.

Formalized by `Cslib.Algorithms.Lean.BreadthFirstSearch.bfsWithParents_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Costs.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BreadthFirstSearch/Parents/Costs.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html#bfs-with-parents-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Breadth-first search](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/breadth-first-search)
