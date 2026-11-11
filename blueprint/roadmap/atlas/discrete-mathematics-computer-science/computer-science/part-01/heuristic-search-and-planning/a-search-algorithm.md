---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.AStar.Consistent, Cslib.Algorithms.Lean.AStar.Admissible, Cslib.Algorithms.Lean.AStar.reducedWeight, Cslib.Algorithms.Lean.AStar.AStarResult, Cslib.Algorithms.Lean.AStar.AStarResult.pathTo?, Cslib.Algorithms.Lean.AStar.aStar, Cslib.Algorithms.Lean.AStar.pathWeight_reducedWeight, Cslib.Algorithms.Lean.AStar.admissible_of_consistent
statement: formalized
proof: formalized
---

# A\* search algorithm

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html).

## Consistent heuristic

Let $G$ be a directed graph on the vertices $\{0, \dots, n-1\}$ and
let $w$ assign a natural number $w(u, v)$ to each pair of vertices. A heuristic $h$ assigning a
natural number to each vertex is consistent (monotone) if $h(u) \le w(u, v) + h(v)$ for every
edge $u \to v$ of $G$.

Formalized by `Cslib.Algorithms.Lean.AStar.Consistent`, a definition declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#consistent).

## Admissible heuristic

For a directed graph $G$ with natural edge weights $w$, a heuristic
$h$ with natural values is admissible for a goal vertex $t$ when it never overestimates the weight
of a path to $t$: $h(v) \le d$ for every vertex $v$ and every weight $d$ of a path in $G$ from $v$
to $t$.

Formalized by `Cslib.Algorithms.Lean.AStar.Admissible`, a definition declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#admissible).

## Reduced weight

Let $w$ assign a natural number $w(u, v)$ to each pair of vertices and let
$h$ assign a natural number to each vertex. The reduced weight of the pair $(u, v)$ is the
natural number $w(u, v) + h(v) - h(u)$, computed with truncated subtraction, so it is $0$ when
$h(u) > w(u, v) + h(v)$.

Formalized by `Cslib.Algorithms.Lean.AStar.reducedWeight`, a definition declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#reduced-weight).

## Output of A-star search

An A* result on $n$ vertices consists of a Dijkstra result on $n$
vertices (the underlying search, with its source, final keys and predecessor pointers) and a
vector that assigns to each vertex $v$ a value $g(v) \in \mathbb{N} \cup \{\infty\}$. In the
output of A* from a source $s$ with a consistent heuristic $h$, the underlying search runs on the
reduced weights, its keys are $f(v) - h(s)$ where $f = g + h$, and $g(v)$ is the least weight of
a path from $s$ to $v$, with $\infty$ when there is none.

Formalized by `Cslib.Algorithms.Lean.AStar.AStarResult`, a structure declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#astar-result).

## Path recovered from an A-star result

Given an A* result $r$ on $n$ vertices and a vertex
$v$, follow the predecessor pointers of the underlying Dijkstra search backward from $v$, at most
$n$ times, until the source is reached, and return the visited vertices in order from the source
to $v$. There is no result if a vertex without a predecessor is met before the source, or if the
source is not reached within $n$ steps.

Formalized by `Cslib.Algorithms.Lean.AStar.AStarResult.pathTo?`, a definition declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#path-to).

## A\* search

**A\* search.** Given a directed graph $G$ on the vertices $\{0, \dots, n-1\}$ with natural
edge weights $w$, a heuristic $h$ with natural values and a source vertex $s$, A* runs Dijkstra's
algorithm from $s$ on the reduced weights $w(u, v) + h(v) - h(u)$ at Dijkstra's cost, and returns
Dijkstra's result (its distances $g'$ and predecessor pointers) together with the path weights
$g(v) = g'(v) + h(s) - h(v)$, where both subtractions are truncated at $0$ and $g(v)$ is infinite
when $g'(v)$ is.

For a consistent heuristic, Dijkstra's distances on the reduced weights are A*'s values
$f = g + h$ shifted by $h(s)$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar`, a definition declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star).

## Reduced weights telescope along paths

Let $G$ be a directed graph on the vertices
$\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be a consistent heuristic with natural
values, and let $w_h(x, y) = w(x, y) + h(y) - h(x)$ be the reduced weight, with the subtraction
truncated at $0$. For all vertices $u$ and $v$ and every nonempty list of vertices
$v_0, v_1, \dots, v_k$ with $v_0 = u$, $v_k = v$ and an edge of $G$ from each $v_i$ to $v_{i+1}$,
the sum of $w_h(v_i, v_{i+1})$ over $i < k$, plus $h(u)$, equals the sum of $w(v_i, v_{i+1})$
over $i < k$, plus $h(v)$.

Formalized by `Cslib.Algorithms.Lean.AStar.pathWeight_reducedWeight`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#path-weight-reduced-weight).

## A consistent heuristic that vanishes at the goal is admissible

**A consistent heuristic that vanishes at the goal is admissible.**

Formalized by `Cslib.Algorithms.Lean.AStar.admissible_of_consistent`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#admissible-of-consistent).

## The final keys of A\*

**The final keys of A\*.** Let $G$ be a directed graph on the vertices $\{0, \dots, n-1\}$ with
natural edge weights $w$, let $h$ be a consistent heuristic with natural values and let $s$ be a
source vertex. If the path weight $g(v)$ that A* from $s$ returns for a vertex $v$ is finite, then
the distance $g'(v)$ that Dijkstra's algorithm from $s$ computes for $v$ on the reduced weights
$w(x, y) + h(y) - h(x)$ (subtraction truncated at $0$) is finite as well, and
$g(v) + h(v) = g'(v) + h(s)$; that is, the key $g'(v)$ is A*'s value $f(v) = g(v) + h(v)$ shifted
down by $h(s)$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_key`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-key).

## A\*'s finite path weights are realized by paths

**A\*'s finite path weights are realized by paths.** Let $G$ be a directed graph on the vertices
$\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be a consistent heuristic with natural
values and let $s$ be a source vertex. If the path weight $g(v)$ that A* from $s$ returns for a
vertex $v$ is finite, then some path in $G$ from $s$ to $v$ has weight exactly $g(v)$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_distance_realized`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-distance-realized).

## A\* with a consistent heuristic is optimal

**A\* with a consistent heuristic is optimal.** Let $G$ be a directed graph on the vertices
$\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be a consistent heuristic with natural
values and let $s$ be a source vertex. If the path weight $g(v)$ that A* from $s$ returns for a
vertex $v$ is finite, then $g(v) \le d$ for every weight $d$ of a path in $G$ from $s$ to $v$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_distance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-distance-minimal).

## A\* leaves exactly the unreachable vertices at infinity

**A\* leaves exactly the unreachable vertices at infinity.** Let $G$ be a directed graph on the
vertices $\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be any heuristic with natural
values and let $s$ be a source vertex. The path weight $g(v)$ that A* from $s$ returns for a vertex
$v$ is infinite if and only if $v$ is not reachable from $s$ in $G$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_distance_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-distance-eq-none-iff).

## A\*'s predecessor paths are simple and realize its path weights

**A\*'s predecessor paths are simple and realize its path weights.** Let $G$ be a directed graph
on the vertices $\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be a consistent heuristic
with natural values and let $s$ be a source vertex. If following the predecessor pointers that A*
from $s$ returns, back from a vertex $v$, yields the vertex list $p$ (listed from $s$ to $v$), then
the path weight $g(v)$ that A* returns for $v$ is finite, $p$ starts at $s$ and ends at $v$,
$G$ has an edge from each vertex of $p$ to the next one, no vertex occurs twice in $p$, and the
weight of $p$ (the sum of $w$ over its consecutive pairs) equals $g(v)$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_pathTo?_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-path-to-spec).

## A\*'s predecessor edges are tight

**A\*'s predecessor edges are tight.** Let $G$ be a directed graph on the vertices
$\{0, \dots, n-1\}$ with natural edge weights $w$, let $h$ be a consistent heuristic with natural
values and let $s$ be a source vertex. If A* from $s$ records $u$ as the predecessor of a vertex
$v$, then $G$ has an edge from $u$ to $v$, the path weights $g(u)$ and $g(v)$ that A* returns are
both finite, and $g(v) = g(u) + w(u, v)$.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_predecessor_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-predecessor-spec).

## Cost of A\*

**Cost of A\*.** Let $G$ be a directed graph on the vertices $\{0, \dots, n-1\}$ with natural
edge weights $w$, let $h$ be any heuristic with natural values and let $s$ be a source vertex. In
Dijkstra's dense cost model, which counts the vertex entries inspected by minimum selection and
the adjacency entries inspected by relaxation, A* from $s$ charges exactly $n^2 + m$ events in
total, where $m$ is the number of entries in the adjacency lists of $G$, counting duplicates and
self-loops.

Formalized by `Cslib.Algorithms.Lean.AStar.aStar_time`, a theorem declared in [CSLibExt/Algorithms/Lean/AStar/Consistent.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/AStar/Consistent.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html#a-star-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A* search algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/heuristic-search-and-planning/a-search-algorithm)
