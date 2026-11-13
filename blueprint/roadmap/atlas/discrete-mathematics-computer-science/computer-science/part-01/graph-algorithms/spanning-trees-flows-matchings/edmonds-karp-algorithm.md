---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.EdmondsKarp.Flow, Cslib.Algorithms.Lean.EdmondsKarp.flowValue, Cslib.Algorithms.Lean.EdmondsKarp.IsFeasible, Cslib.Algorithms.Lean.EdmondsKarp.zeroFlow, Cslib.Algorithms.Lean.EdmondsKarp.zeroFlow_feasible, Cslib.Algorithms.Lean.EdmondsKarp.IsFeasible.capacity_bounds, Cslib.Algorithms.Lean.EdmondsKarp.residualGraph, Cslib.Algorithms.Lean.EdmondsKarp.residualGraph_edge_iff
statement: formalized
proof: formalized
---

# Edmonds–Karp algorithm

50 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html).

## Flow

A flow on $n$ vertices, labelled $0, \dots, n-1$, is an integer matrix: it assigns
an integer $f(u, v)$ to each ordered pair of vertices $(u, v)$.

No condition is imposed here; skew symmetry, capacity bounds and conservation are required by
feasibility.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.Flow`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow).

## Flow value

For a flow $f$ on $n$ vertices and a vertex $s$, the value of $f$ at $s$ is
the net flow leaving $s$, namely the integer $\sum_v f(s, v)$, where $v$ runs over all vertices.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value).

## Feasible flow

Let $c$ be a capacity function assigning a natural number $c(u, v)$ to
each ordered pair of vertices, and let $s$ and $t$ be vertices. A flow $f$ is feasible for $c$,
$s$ and $t$ when it is skew symmetric, $f(u, v) = -f(v, u)$ for all $u$ and $v$; it respects
the capacities, $f(u, v) \le c(u, v)$ for all $u$ and $v$; and it is conserved: for every vertex
$v$ other than $s$ and $t$, the net flow $\sum_w f(v, w)$ leaving $v$ is $0$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.IsFeasible`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#is-feasible).

## Zero flow

The zero flow on the vertices $\{0, \dots, n - 1\}$ is the integer-valued matrix
$f$ with $f(u, v) = 0$ for all vertices $u$ and $v$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.zeroFlow`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#zero-flow).

## The zero flow is feasible

For every capacity matrix $c$ with natural-number entries on the
vertices $\{0, \dots, n - 1\}$ and all vertices $s$ and $t$, the zero flow is feasible for $c$ with
source $s$ and sink $t$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.zeroFlow_feasible`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#zero-flow-feasible).

## Two-sided capacity bounds for a feasible flow

Let $c$ be a capacity matrix with
natural-number entries on the vertices $\{0, \dots, n-1\}$, let $s$ and $t$ be vertices,
and let $f$ be a flow that is feasible for $c$, $s$, $t$. Then for all vertices $u$ and
$v$, we have $-c(v, u) \le f(u, v) \le c(u, v)$.

The lower bound follows from skew symmetry and the upper bound on the reverse entry.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.IsFeasible.capacity_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#capacity-bounds).

## Residual graph

Let $c$ be a capacity matrix assigning a natural number $c(u, v)$ to each
ordered pair of vertices among $0, \dots, n - 1$, and let $f$ be a flow on these vertices. The
residual graph of $c$ and $f$ is the directed adjacency graph whose vertices $0, \dots, n - 1$ are
enumerated in increasing order and in which the adjacency list of $u$ consists of the vertices $v$
with $f(u, v) < c(u, v)$, that is, with positive residual capacity $c(u, v) - f(u, v)$, in
increasing order.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.residualGraph`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#residual-graph).

## Edges of the residual graph

Let $c$ be a capacity matrix with natural-number entries and
$f$ an integer matrix (the flow) on the vertices $0, \dots, n - 1$. For all vertices $u$ and $v$,
the residual graph of $c$ and $f$ has an edge from $u$ to $v$ if and only if
$f(u, v) < c(u, v)$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.residualGraph_edge_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#residual-graph-edge-iff).

## Directed path

In a directed graph $G$, a list $p$ of vertices is a path from $s$ to $t$
when it is nonempty, its first entry is $s$, its last entry is $t$, every pair of consecutive
entries $u, v$ forms a directed edge of $G$ from $u$ to $v$, and no vertex occurs twice in $p$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.IsPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#is-path).

## Distance-guided path reconstruction

Let $G$ be a directed graph with ordered adjacency
lists, $d$ a partial labelling of its vertices by natural numbers, $t$ a vertex, and $\equiv$ a
given Boolean test on pairs of vertices (not required to be equality). The reconstruction from
a vertex $u$ with $k$ steps left returns the one-element list $[u]$ when $k = 0$ and $u \equiv t$
holds, and fails when $k = 0$ and $u \equiv t$ fails. When $k \ge 1$, it takes the first
out-neighbour $w$ of $u$ in adjacency order with $d(w) = k - 1$; it fails if there is none, and
otherwise returns $u$ followed by the reconstruction from $w$ with $k - 1$ steps left, failing
if that fails.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.pathFromDistances`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#path-from-distances).

## Soundness of distance-guided path reconstruction

Let $G$ be a directed adjacency graph on
a type $V$ whose Boolean test $\equiv$ on pairs of vertices holds exactly for equal vertices, let
$d$ be a partial labelling of the vertices by natural numbers, let $t$ and $u$ be vertices, and let
$k$ be a natural number. If the distance-guided reconstruction for $G$, $d$ and $t$ from $u$ with
$k$ steps left succeeds and returns a list $p$, then $p$ is a walk from $u$ to $t$ in $G$ (it is
nonempty, its first entry is $u$, its last entry is $t$, and every pair of consecutive entries is
an edge of $G$) and $p$ has exactly $k + 1$ entries.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.pathFromDistances_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#path-from-distances-sound).

## Shortest path via breadth-first search

Let $G$ be a finite directed graph on the vertices
$\{0, \dots, n - 1\}$ with ordered adjacency lists, and let $s$ be a source and $t$ a sink. Run
breadth-first search from $t$ in the reverse graph of $G$; it labels each vertex $v$ from which $t$
is reachable with the distance from $v$ to $t$ in $G$. If $s$ has no label, the search returns no
path. Otherwise, starting at $s$ with label $d$, take $d$ steps, each time moving to the first
out-neighbour (in adjacency order) whose label is one less than that of the current vertex. The
search returns the list of visited vertices, from $s$ to the last one, if every step succeeds and
the last vertex is $t$, and no path otherwise.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.shortestPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#shortest-path).

## Soundness of the shortest-path search

Let $G$ be a finite directed graph on the vertices
$\{0, \dots, n - 1\}$ and let $s$ and $t$ be vertices. If the breadth-first shortest-path search in
$G$ from $s$ to $t$ returns a list $P$ of vertices, then $P$ is a directed path in $G$ from $s$ to
$t$ without repeated vertices, and breadth-first search in $G$ from $s$ assigns $t$ a distance $d$
such that $P$ has exactly $d + 1$ vertices.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.shortestPath_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#shortest-path-sound).

## The shortest-path search succeeds exactly when the sink is reachable

Let $G$ be a finite
directed graph on the vertices $\{0, \dots, n - 1\}$ and let $s$ and $t$ be vertices. The
breadth-first shortest-path search in $G$ from $s$ to $t$ returns some path if and only if $t$ is
reachable from $s$ in $G$ (every vertex counts as reachable from itself).

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.shortestPath_present_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#shortest-path-present-iff-reachable).

## The shortest-path search fails exactly when the sink is unreachable

Let $G$ be a finite
directed graph on the vertices $\{0, \dots, n - 1\}$ and let $s$ and $t$ be vertices. The
breadth-first shortest-path search in $G$ from $s$ to $t$ returns no path if and only if $t$ is not
reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.shortestPath_eq_none_iff_not_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#shortest-path-eq-none-iff-not-reachable).

## Edges of a path

The edges of a list $v_0, v_1, \dots, v_k$ are the list of its
consecutive ordered pairs $(v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k)$, in this order; the
empty list and one-element lists have no edges.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.pathEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#path-edges).

## Residual capacity

Let $c$ be a capacity matrix with natural-number entries and $f$ an
integer matrix (the flow) on the vertices $0, \dots, n - 1$. The residual capacity of an ordered
pair of vertices $(u, v)$ is the integer $c(u, v) - f(u, v)$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.residualAmount`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#residual-amount).

## Bottleneck of a path

Let $c$ be a capacity matrix with natural-number entries and $f$
an integer matrix (the flow) on the same vertices. The bottleneck of a list of vertices
$v_0, v_1, \dots, v_k$ with $k \ge 1$ is the integer
$\min_{i < k} \bigl(c(v_i, v_{i+1}) - f(v_i, v_{i+1})\bigr)$, the least residual capacity of a
consecutive pair; a list with at most one vertex has bottleneck $0$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.pathBottleneck`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#path-bottleneck).

## Unit skew flow along an oriented edge

For vertices $a$, $b$, $u$, $v$,
the unit skew flow of the oriented edge $(a, b)$ at the ordered pair $(u, v)$ is the integer
$[u = a \text{ and } v = b] - [u = b \text{ and } v = a]$, where $[P]$ is $1$ if $P$ holds
and $0$ otherwise.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.localDelta`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#local-delta).

## Edge delta of a path

For a list $P$ of elements of a set $V$ and elements $u, v$
of $V$, the edge delta of $P$ at $(u, v)$ is the integer obtained as the number of
consecutive pairs of $P$ equal to $(u, v)$ minus the number of consecutive pairs of $P$
equal to $(v, u)$, counted with multiplicity. It is $0$ when $P$ has fewer than two
elements.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edgeDelta`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edge-delta).

## Augmenting a flow along a path

Given an integer flow matrix $f$ on the vertices
$\{0, \dots, n-1\}$, a list of vertices $P$ and an integer $a$, the augmentation of $f$
along $P$ by $a$ is the matrix whose entry at $(u, v)$ is $f(u, v) + a \cdot d$, where $d$
is the number of consecutive pairs of $P$ equal to $(u, v)$ minus the number of
consecutive pairs of $P$ equal to $(v, u)$, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.augment`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#augment).

## Augmenting paths have positive bottleneck

Let $c$ be a capacity matrix with
natural-number entries and $f$ any integer matrix (the flow) on the vertices $0, \dots, n - 1$,
and let $s \ne t$ be vertices. If $p$ is a duplicate-free path from $s$ to $t$ in the residual
graph of $c$ and $f$, then the bottleneck of $p$, the minimum of $c(u, v) - f(u, v)$ over
consecutive vertices $u, v$ of $p$, is positive.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.pathBottleneck_pos`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#path-bottleneck-pos).

## Augmentation within residual capacities preserves feasibility

Let $c$ be a
capacity matrix with natural-number entries on the vertices $\{0, \dots, n-1\}$, let $s$
and $t$ be vertices, and let $f$ be a flow that is feasible for $c$, $s$, $t$. Let
$P = (v_0, \dots, v_k)$ be a nonempty list of pairwise distinct vertices with $v_0 = s$ and
$v_k = t$, and let $a$ be an integer with $0 \le a$ and
$a \le c(v_i, v_{i+1}) - f(v_i, v_{i+1})$ for every $i < k$. Then the augmentation of $f$
along $P$ by $a$ is feasible for $c$, $s$, $t$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.augment_feasible`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#augment-feasible).

## Augmenting along a path changes the flow value by the amount

Let $s \ne t$ be vertices,
$f$ a flow, $a$ an integer, and $p$ a nonempty list of vertices whose first entry is $s$ and whose
last entry is $t$. Then the net flow leaving $s$ under the flow obtained by augmenting $f$ along
$p$ by $a$ equals the net flow leaving $s$ under $f$, plus $a$.

No feasibility of $f$, no edge condition on consecutive entries of $p$, and no duplicate-freeness
of $p$ is needed.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue_augment`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value-augment).

## Bottleneck augmentation preserves feasibility

Let $c$ be a capacity matrix with
natural-number entries on the vertices $\{0, \dots, n-1\}$, let $s$ and $t$ be vertices,
and let $f$ be a flow that is feasible for $c$, $s$, $t$. If $P$ is a path from $s$ to $t$
in the residual graph of $f$, that is, a nonempty list of pairwise distinct vertices
starting at $s$ and ending at $t$ whose consecutive pairs are residual edges, then the
augmentation of $f$ along $P$ by the bottleneck of $P$ is again feasible for $c$, $s$,
$t$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.augment_pathBottleneck_feasible`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#augment-path-bottleneck-feasible).

## One augmenting-path step

Let $c$ be a capacity matrix with natural-number entries on the
vertices $\{0, \dots, n - 1\}$, let $s$ be a source and $t$ a sink, and let $f$ be a flow (an
integer-valued matrix on pairs of vertices). Run the breadth-first shortest-path search from $s$ to
$t$ in the residual graph of $f$ with respect to $c$. If it finds no path, the step returns $f$. If
it returns a path $P$, let $b$ be the bottleneck of $P$, the least residual capacity
$c(u, v) - f(u, v)$ over the edges $(u, v)$ of $P$ (and $b = 0$ if $P$ has no edges); the step
returns $f$ augmented along $P$ by $b$, that is, $b$ is added to $f(u, v)$ and subtracted from
$f(v, u)$ for each edge $(u, v)$ of $P$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.step`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#step).

## One augmentation step keeps or strictly raises the flow value

Let $c$ be a capacity
function and $s \ne t$ vertices. For every flow $f$, the flow obtained from $f$ by one step of
bottleneck augmentation either has the same net flow leaving $s$ as $f$, or a strictly larger
one.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue_step`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value-step).

## Augmenting-path iteration with fuel

Let $c$ be a capacity matrix with natural-number
entries on the vertices $\{0, \dots, n - 1\}$, let $s$ be a source and $t$ a sink, let $k$ be a fuel
bound and let $f$ be a flow (an integer-valued matrix on pairs of vertices). The iteration returns
$f$ if $k = 0$ or $s = t$. Otherwise it runs the breadth-first shortest-path search from $s$ to $t$
in the residual graph of $f$ with respect to $c$. If the search finds no path, the iteration returns
$f$. If it returns a path $P$, let $b$ be the bottleneck of $P$, the least residual capacity
$c(u, v) - f(u, v)$ over the edges $(u, v)$ of $P$; the iteration augments $f$ along $P$ by $b$,
adding $b$ to $f(u, v)$ and subtracting $b$ from $f(v, u)$ for each edge $(u, v)$ of $P$, and
continues from the augmented flow with fuel $k - 1$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.run`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#run).

## The augmentation loop never decreases the flow value

Let $c$ be a capacity function and
$s \ne t$ vertices. For every flow $f$ and every natural number $k$, the net flow leaving $s$
after running at most $k$ rounds of bottleneck augmentation from $f$ is at least the net flow
leaving $s$ under $f$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue_le_run`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 751](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value-le-run).

## Source capacity

For a capacity matrix $c$ with natural-number entries on the vertices
$\{0, \dots, n - 1\}$ and a source $s$, the source capacity is the total capacity leaving $s$,
namely $\sum_{v} c(s, v)$, where $v$ ranges over all vertices, including $s$ itself.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.sourceCapacity`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 778](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L778). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#source-capacity).

## Edmonds–Karp maximum flow

Let $c$ be a capacity function assigning a natural number
$c(u, v)$ to each ordered pair of vertices, and let $s$ and $t$ be vertices. If $s = t$, the
Edmonds–Karp flow is the zero flow. Otherwise it is the result of running at most $C + 1$ rounds
of bottleneck augmentation from the zero flow, where $C = \sum_v c(s, v)$ is the total capacity
leaving $s$: each round looks for a shortest path from $s$ to $t$ in the residual graph, stops if
there is none, and otherwise augments the flow along that path by its bottleneck.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edmondsKarp`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp).

## The Edmonds–Karp flow is feasible

For every capacity matrix $c$ with
natural-number entries on the vertices $\{0, \dots, n-1\}$ and all vertices $s$ and $t$,
the flow $f$ returned by the Edmonds–Karp algorithm on $c$, $s$, $t$ is feasible for $c$,
$s$, $t$: it is skew-symmetric, satisfies $f(u, v) \le c(u, v)$ for all vertices $u, v$,
and has zero net outflow at every vertex other than $s$ and $t$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edmondsKarp_feasible`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 817](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp-feasible).

## The iteration stops when there is no augmenting path

Let $c$ be a capacity matrix with
natural-number entries on the vertices $\{0, \dots, n - 1\}$, let $s$ and $t$ be vertices, and let
$f$ be a flow (an integer-valued matrix on pairs of vertices). If the breadth-first shortest-path
search finds no path from $s$ to $t$ in the residual graph of $f$ with respect to $c$, then for
every fuel bound $k$, the augmenting-path iteration started at $f$ with fuel $k$ returns $f$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.run_eq_of_no_path`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 827](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L827). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#run-eq-of-no-path).

## The flow value is at most the source capacity

Let $c$ be a capacity function, $s$ and
$t$ vertices, and $f$ a flow that is feasible for $c$, $s$ and $t$. Then the net flow leaving $s$
under $f$ is at most $\sum_v c(s, v)$, the total capacity leaving $s$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue_le_sourceCapacity`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 868](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L868). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value-le-source-capacity).

## No augmenting path remains after Edmonds–Karp

Let $c$ be a capacity matrix with
natural-number entries on the vertices $\{0, \dots, n-1\}$ and let $s$ and $t$ be distinct
vertices. Then $t$ is not reachable from $s$ in the residual graph of the flow returned
by the Edmonds–Karp algorithm on $c$, $s$, $t$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edmondsKarp_no_augmenting_path`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp-no-augmenting-path).

## Cut capacity

For a capacity matrix $c$ with natural-number entries on the vertices
$\{0, \dots, n-1\}$ and a set $S$ of vertices, the capacity of the cut $S$ is the integer
$\sum_{u \in S} \sum_{v \notin S} c(u, v)$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.cutCapacity`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 920](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L920). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#cut-capacity).

## Weak max-flow min-cut duality

Let $c$ be a capacity function, $s$ and $t$ vertices, and
$f$ a flow that is feasible for $c$, $s$ and $t$. For every set $S$ of vertices with $s \in S$
and $t \notin S$, the net flow leaving $s$ under $f$ is at most the capacity of the cut $S$,
namely $\sum_{u \in S} \sum_{v \notin S} c(u, v)$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.flowValue_le_cutCapacity`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 975](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L975). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-value-le-cut-capacity).

## Residual cut

Let $c$ be a capacity matrix assigning a natural number $c(u, v)$ to each
ordered pair of vertices among $0, \dots, n - 1$, let $f$ be a flow on these vertices, and let $s$
be a vertex. The residual cut of $c$, $f$ and $s$ is the set of vertices visited by breadth-first
search from $s$ in the residual graph of $c$ and $f$, that is, the set of vertices reachable from
$s$ in that residual graph.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.residualCut`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 989](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L989). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#residual-cut).

## The Edmonds–Karp flow value equals its residual cut capacity

Let $c$ be a capacity
matrix with natural-number entries on the vertices $\{0, \dots, n-1\}$, let $s$ and $t$ be
distinct vertices, and let $f$ be the flow returned by the Edmonds–Karp algorithm on $c$,
$s$, $t$. Then the net flow of $f$ out of $s$ equals the capacity of the cut formed by the
vertices reachable from $s$ in the residual graph of $f$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edmondsKarp_minCut`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 1029](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L1029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp-min-cut).

## Maximality of the Edmonds–Karp flow

Let $c$ be a capacity matrix with
natural-number entries on the vertices $\{0, \dots, n-1\}$, let $s$ and $t$ be distinct
vertices, and let $f$ be the flow returned by the Edmonds–Karp algorithm on $c$, $s$, $t$.
Then every integer flow $g$ that is feasible for $c$, $s$, $t$ has value at $s$ at most
the value of $f$ at $s$, where the value of a flow at $s$ is its net flow out of $s$.

Formalized by `Cslib.Algorithms.Lean.EdmondsKarp.edmondsKarp_maximal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean, line 1051](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/EdmondsKarp.lean#L1051). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp-maximal).

## Real capacities

For a capacity function $c$ on the vertices $0, \dots, n-1$ with
natural-number values, the real capacities are the same values viewed as real numbers,
$(u, v) \mapsto c(u, v) \in \mathbb{R}$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.realCap`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#real-cap).

## Arc flow of an integer flow

For an integer flow matrix $f$ on the vertices
$0, \dots, n-1$, its arc flow is the natural-number matrix whose entry at $(u, v)$ is the positive
part $\max(f(u, v), 0)$ of $f(u, v)$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.arcFlow`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#arc-flow).

## Real arc flow

For an integer flow matrix $f$ on the vertices $0, \dots, n-1$, its real
arc flow is the function $(u, v) \mapsto \max(f(u, v), 0)$, the arc flow of $f$, viewed as real
numbers.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.realFlow`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#real-flow).

## A skew flow is the difference of its arc flows

Let $f$ be an integer flow matrix on the
vertices $0, \dots, n-1$ that is skew-symmetric, $f(u, v) = -f(v, u)$ for all $u, v$, and let
$a(u, v) = \max(f(u, v), 0)$ be its arc flow. Then $f(u, v) = a(u, v) - a(v, u)$ for all
vertices $u$ and $v$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.flow_eq_arcFlow_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#flow-eq-arc-flow-sub).

## Net outflow in the arc representation

Let $f$ be a skew-symmetric integer flow matrix on
the vertices $0, \dots, n-1$, so $f(u, v) = -f(v, u)$ for all $u, v$, and let
$a(u, v) = \max(f(u, v), 0)$ be its arc flow, viewed as real numbers. Then for every vertex $v$,
$\sum_w a(v, w) - \sum_u a(u, v) = \sum_w f(v, w)$, the net flow leaving $v$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.sum_realFlow_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#sum-real-flow-sub).

## A feasible skew flow gives a feasible flow

Let $c$ be a capacity function on the vertices
$0, \dots, n-1$ with natural-number values and let $s, t$ be vertices. If an integer flow matrix
$f$ is a feasible skew-symmetric $s$-$t$ flow for $c$, then its arc flow
$(u, v) \mapsto \max(f(u, v), 0)$, viewed as a real function, is a feasible $s$-$t$ flow for $c$
viewed as real capacities.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.isFeasibleFlow_realFlow`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#is-feasible-flow-real-flow).

## The Edmonds-Karp residual cut separates source and sink

Let $c$ be a capacity function
on the vertices $0, \dots, n-1$ with natural-number values and let $s \ne t$ be vertices. The set
of vertices reachable from $s$ in the residual graph of the flow computed by the Edmonds-Karp
algorithm on $c$, $s$, $t$ is an $s$-$t$ cut: it contains $s$ and not $t$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.isSTCut_residualCut`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#is-stcut-residual-cut).

## Edmonds-Karp computes a maximum flow and a minimum cut

Let $c$ be a capacity function on
the vertices $0, \dots, n-1$ with natural-number values, viewed as real capacities, and let
$s \ne t$ be vertices. Let $f$ be the real arc flow of the flow computed by the Edmonds-Karp
algorithm on $c$, $s$, $t$ (its positive part, viewed as real numbers), and let $S_0$ be the set
of vertices reachable from $s$ in the residual graph of that flow. Then $f$ is a feasible $s$-$t$
flow for $c$; every feasible real-valued $s$-$t$ flow for $c$ has value at most the value of $f$;
the value of $f$ is at most the capacity of every $s$-$t$ cut; $S_0$ is an $s$-$t$ cut; and the
value of $f$ equals the capacity of $S_0$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.edmondsKarp_max_flow_min_cut`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#edmonds-karp-max-flow-min-cut).

## No $s$-$t$ cut is smaller than the Edmonds–Karp residual cut

Let $c$ be a capacity
function on the vertices $0, \dots, n-1$ with natural-number values, viewed as real capacities,
and let $s \ne t$ be vertices. Let $S_0$ be the set of vertices reachable from $s$ in the residual
graph of the flow computed by the Edmonds–Karp algorithm on $c$, $s$, $t$. Then for every $s$-$t$
cut $S$, the capacity of $S_0$ is at most the capacity of $S$.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.cutCapacity_residualCut_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#cut-capacity-residual-cut-le).

## Integral flow theorem

Let $c$ be a capacity function on the vertices $0, \dots, n-1$
with natural-number values, viewed as real capacities, and let $s \ne t$ be vertices. Then there
is a natural-number valued function $f$ on pairs of vertices which, viewed as a real function, is
a feasible $s$-$t$ flow for $c$ whose value is at least the value of every feasible real-valued
$s$-$t$ flow for $c$.

The proof takes $f$ to be the arc flow of the flow computed by the Edmonds-Karp algorithm.

Formalized by `Cslib.Algorithms.Lean.Graph.MaxFlowMinCut.exists_nat_max_flow`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/MaxFlowMinCut.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html#exists-nat-max-flow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edmonds–Karp algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/edmonds-karp-algorithm)
