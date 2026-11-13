---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Johnson.johnson, Cslib.Algorithms.Lean.Johnson.johnson_eq_none_iff, Cslib.Algorithms.Lean.Johnson.johnson_distance_spec, Cslib.Algorithms.Lean.Johnson.johnson_time_of_success, Cslib.Algorithms.Lean.Johnson.johnson_time_le
statement: formalized
proof: formalized
---

# Johnson's algorithm

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html).

## Johnson's algorithm

Let $E$ be a list of directed edges on the vertices
$\{0, \dots, n-1\}$ with integer weights. Johnson's algorithm adds a new vertex $s$ with an
edge of weight $0$ to every original vertex and runs Bellman–Ford from $s$. If Bellman–Ford
reports a negative cycle, the algorithm returns no table. Otherwise let $h(v)$ be the
Bellman–Ford distance of $v$ (taken to be $0$ if $v$ is unreached). Each edge from $u$ to $v$ of
weight $w$ gets the new weight $\max(0, w + h(u) - h(v))$.
For each original vertex $u$ the algorithm runs Dijkstra from $u$ on the original vertices,
where the weight from $x$ to $y$ is the least new weight of an edge from $x$ to $y$. It
returns the table whose entry at $(u, v)$ is $\infty$ if Dijkstra does not reach $v$, and
$d'(u, v) + h(v) - h(u)$ otherwise, where $d'(u, v)$ is the Dijkstra distance.

The cost counts the selected construction, scan, relaxation and decoding actions, not full RAM
or bit complexity.

Formalized by `Cslib.Algorithms.Lean.Johnson.johnson`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Basic.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Basic.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html#johnson).

## Johnson's algorithm fails exactly on reachable negative cycles

For every list $E$ of
directed edges on the vertices $\{0, \dots, n-1\}$ with integer weights, Johnson's algorithm on
$E$ returns no table if and only if there is a vertex $s$ from which a negative cycle of $E$ is
reachable.

Formalized by `Cslib.Algorithms.Lean.Johnson.johnson_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Correctness.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Correctness.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html#johnson-eq-none-iff).

## Correctness of Johnson's algorithm

Let $E$ be a list of directed edges on the vertices
$\{0, \dots, n-1\}$ with integer weights, and suppose Johnson's algorithm on $E$ returns a
table $d$. Then for all vertices $s$ and $t$, $d(s, t) = \infty$ if and only if $t$ is not
reachable from $s$ along edges of $E$. Moreover, if $d(s, t)$ is an integer $x$, then some
weighted path in $E$ from $s$ to $t$ has weight $x$, and every weighted path in $E$ from $s$ to
$t$ has weight at least $x$.

Formalized by `Cslib.Algorithms.Lean.Johnson.johnson_distance_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Correctness.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Correctness.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html#johnson-distance-spec).

## Exact cost of a successful run of Johnson's algorithm

Let $E$ be a list of $m$ directed
edges on the vertices $\{0, \dots, n-1\}$ with integer weights. If Johnson's algorithm on $E$
returns a table, then its counted cost is exactly
$n^3 + nm + (n+1)(m+n) + 2n^2 + 4m + 5n + 1$.

Formalized by `Cslib.Algorithms.Lean.Johnson.johnson_time_of_success`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Costs.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Costs.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html#johnson-time-of-success).

## Cost bound for Johnson's algorithm

For every list $E$ of $m$ directed edges on the
vertices $\{0, \dots, n-1\}$ with integer weights, the counted cost of Johnson's algorithm on
$E$, including the case where it extracts a negative cycle, is at most
$n^3 + nm + (n+1)(m+n) + 2n^2 + 4m + 5n + 1 + 3(n+1)$.

Formalized by `Cslib.Algorithms.Lean.Johnson.johnson_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Costs.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Johnson/Costs.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html#johnson-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Johnson's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/johnson-s-algorithm)
