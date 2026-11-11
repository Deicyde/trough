---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FloydWarshall.pathWeight, Cslib.Algorithms.Lean.FloydWarshall.IsWeightedPath, Cslib.Algorithms.Lean.FloydWarshall.InternalVerticesBelow, Cslib.Algorithms.Lean.FloydWarshall.IsStageShortestPathWeight, Cslib.Algorithms.Lean.FloydWarshall.IsNegativeCycle, Cslib.Algorithms.Lean.FloydWarshall.HasNegativeCycle, Cslib.Algorithms.Lean.FloydWarshall.NoNegativeCycle, Cslib.Algorithms.Lean.FloydWarshall.Cost
statement: formalized
proof: formalized
---

# Floyd–Warshall algorithm

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html).

## Weight of a vertex path in an extended-integer weight matrix

Let $w$ assign to each
ordered pair of vertices in $\{0, \dots, n-1\}$ a weight in $\mathbb{Z} \cup \{\infty\}$. The
weight of a list of vertices $v_0, v_1, \dots, v_m$ with $m \ge 1$ is
$w(v_0, v_1) + w(v_1, v_2) + \cdots + w(v_{m-1}, v_m)$, computed in $\mathbb{Z} \cup \{\infty\}$
where adding $\infty$ gives $\infty$. The empty list and every single-vertex list have
weight $0$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.pathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#path-weight).

## Finite-weight vertex path in a weight matrix

Let $w$ assign to each ordered pair of
vertices in $\{0, \dots, n-1\}$ a weight in $\mathbb{Z} \cup \{\infty\}$, and let $s$ and $t$ be
vertices. A list of vertices $p$ is a weighted path from $s$ to $t$ when $p$ is nonempty, its
first entry is $s$, its last entry is $t$, and $w(u, v) \ne \infty$ for every pair of consecutive
entries $u, v$ of $p$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.IsWeightedPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#is-weighted-path).

## Intermediate vertices below a bound

For a natural number $k$, a list of vertices in
$\{0, \dots, n - 1\}$ has all its intermediate vertices below $k$ when every entry of the list
other than its first and its last is less than $k$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.InternalVerticesBelow`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#internal-vertices-below).

## Stage-$k$ shortest-path weight

Let $w$ assign to each ordered pair of vertices in
$\{0, \dots, n-1\}$ a weight in $\mathbb{Z} \cup \{\infty\}$, let $k$ be a natural number, let
$s$ and $t$ be vertices and let $d \in \mathbb{Z} \cup \{\infty\}$. A weighted path from $s$ to
$t$ is a nonempty list of vertices that starts at $s$, ends at $t$ and has $w(u, v) \ne \infty$
for every pair of consecutive vertices $u, v$; its weight is the sum of these values $w(u, v)$,
and its intermediate vertices are all its entries except the first and the last. Then $d$ is the
stage-$k$ shortest-path weight from $s$ to $t$ when $d$ is at most the weight of every weighted
path from $s$ to $t$ whose intermediate vertices are all less than $k$, and either $d = \infty$ or
some such path has weight exactly $d$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.IsStageShortestPathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#is-stage-shortest-path-weight).

## Negative cycles

For an $n \times n$ matrix $w$ of weights in $\mathbb{Z} \cup \{+\infty\}$,
a list of vertices $v_0, \dots, v_m$ is a negative cycle when $m \ge 1$, $v_m = v_0$, every
weight $w_{v_i v_{i+1}}$ with $i < m$ is finite, the vertices $v_0, \dots, v_{m-1}$ are
pairwise distinct, and the path weight $\sum_{i < m} w_{v_i v_{i+1}}$ is negative.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.IsNegativeCycle`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#is-negative-cycle).

## Matrices with a negative cycle

An $n \times n$ matrix $w$ of weights in
$\mathbb{Z} \cup \{+\infty\}$ has a negative cycle when some list of vertices is a negative
cycle for $w$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.HasNegativeCycle`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#has-negative-cycle).

## Weight matrices without negative cycles

Let $w$ assign to each ordered pair of vertices
in $\{0, \dots, n-1\}$ a weight in $\mathbb{Z} \cup \{\infty\}$. Then $w$ has no negative cycle
when there is no list of vertices $v_0, v_1, \dots, v_m$ with $m \ge 1$ such that $v_m = v_0$,
the vertices $v_0, \dots, v_{m-1}$ are pairwise distinct, $w(v_{i-1}, v_i) \ne \infty$ for
$1 \le i \le m$, and $w(v_0, v_1) + \cdots + w(v_{m-1}, v_m) < 0$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.NoNegativeCycle`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#no-negative-cycle).

## Floyd–Warshall cost record

A cost record for the Floyd–Warshall algorithm is a pair of
natural numbers: the number of initialization events (input matrix cells copied into the initial
distance table) and the number of min-plus transition events (table entries updated).

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.Cost`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#cost).

## Total Floyd–Warshall cost

The total of a Floyd–Warshall cost record is its number of
initialization events plus its number of min-plus transition events.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.Cost.total`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#total).

## Floyd–Warshall algorithm

Given an $n \times n$ matrix $w$ of weights in
$\mathbb{Z} \cup \{+\infty\}$ indexed by the vertices $0, \dots, n - 1$, the Floyd–Warshall
algorithm starts from the table with $d^{(0)}_{ii} = \min(w_{ii}, 0)$ and $d^{(0)}_{ij} = w_{ij}$
for $i \ne j$, and for $k = 0, \dots, n - 1$ computes the table
$d^{(k+1)}_{ij} = \min\bigl(d^{(k)}_{ij}, d^{(k)}_{ik} + d^{(k)}_{kj}\bigr)$. It returns the
matrix $d^{(n)}$ together with its cost: one initialization event for each entry of $d^{(0)}$
and one transition event for each entry of each table $d^{(k+1)}$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall).

## Negative-diagonal test

For an $n \times n$ matrix $d$ with entries in
$\mathbb{Z} \cup \{+\infty\}$, the negative-diagonal test on $d$ is the Boolean value that is
true exactly when $d_{vv} < 0$ for some vertex $v$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.hasNegativeDiagonal`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#has-negative-diagonal).

## Initialization count of Floyd–Warshall

For every $n$ and every $n \times n$ matrix of
weights in $\mathbb{Z} \cup \{+\infty\}$, the Floyd–Warshall algorithm performs exactly $n^2$
initialization events, one for each ordered pair of vertices.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_initializations`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-initializations).

## Transition count of Floyd–Warshall

For every $n$ and every $n \times n$ matrix of weights
in $\mathbb{Z} \cup \{+\infty\}$, the Floyd–Warshall algorithm performs exactly $n^3$ min-plus
transition events, one for each triple $(k, i, j)$ of vertices.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_transitions`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-transitions).

## Floyd–Warshall performs $n^2 + n^3$ steps

For every $n$ and every $n \times n$ matrix of
weights in $\mathbb{Z} \cup \{+\infty\}$, the total number of events counted by the Floyd–Warshall
algorithm, initialization events plus min-plus transition events, is exactly $n^2 + n^3$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-time).

## Characterization of the negative-diagonal test

For every $n \times n$ matrix $d$ with
entries in $\mathbb{Z} \cup \{+\infty\}$, the negative-diagonal test on $d$ returns true if and
only if $d_{vv} < 0$ for some vertex $v$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.hasNegativeDiagonal_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Basic.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#has-negative-diagonal-eq-true-iff).

## Floyd–Warshall computes shortest-path distances

Let $w$ assign a weight in
$\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in $\{0, \dots, n-1\}$, suppose that
$w$ has no negative cycle, and let $D$ be the distance matrix computed by Floyd–Warshall from $w$.
Then for all vertices $s$ and $t$, $D(s, t)$ is at most the weight of every weighted path from $s$
to $t$, and either $D(s, t) = \infty$ or $D(s, t)$ is the weight of some weighted path from $s$ to
$t$. Here a weighted path is a nonempty vertex sequence in which every consecutive pair has finite
weight, and its weight is the sum of these weights.

Formally this is the stage-$n$ characterization, which considers only paths whose intermediate
vertices are all below $n$; every path qualifies.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_distance_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-distance-spec).

## Finite Floyd–Warshall distances are attained

Let $w$ assign a weight in
$\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in $\{0, \dots, n-1\}$, and let $D$
be the distance matrix computed by Floyd–Warshall from $w$. If $D(s, t) = d$ for vertices $s$, $t$
and an integer $d$, then there is a weighted path from $s$ to $t$ (a nonempty vertex sequence from
$s$ to $t$ in which every consecutive pair has finite weight) whose weight, the sum of the weights
of its consecutive pairs, is $d$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_distance_realized`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-distance-realized).

## No path is shorter than the Floyd–Warshall distance

Let $w$ assign a weight in
$\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in $\{0, \dots, n-1\}$, suppose that
$w$ has no negative cycle, and let $D$ be the distance matrix computed by Floyd–Warshall from $w$.
Then for all vertices $s$ and $t$ and every weighted path $p$ from $s$ to $t$ (a nonempty vertex
sequence from $s$ to $t$ in which every consecutive pair has finite weight), $D(s, t)$ is at most
the weight of $p$, the sum of the weights of its consecutive pairs.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_distance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-distance-minimal).

## Floyd–Warshall reports $\infty$ exactly for unreachable pairs

Let $w$ assign a weight
in $\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in $\{0, \dots, n-1\}$, and let $D$
be the distance matrix computed by Floyd–Warshall from $w$. For all vertices $s$ and $t$,
$D(s, t) = \infty$ if and only if there is no weighted path from $s$ to $t$, that is, no nonempty
vertex sequence from $s$ to $t$ in which every consecutive pair has finite weight.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_distance_eq_top_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-distance-eq-top-iff).

## A negative diagonal entry in Floyd–Warshall reveals a negative cycle

Let $w$ assign a
weight in $\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in $\{0, \dots, n-1\}$, and
let $D$ be the distance matrix computed by Floyd–Warshall from $w$. If $D(v, v) < 0$ for some vertex
$v$, then $w$ has a negative cycle: a vertex sequence $v_0, v_1, \dots, v_m$ with $m \ge 1$ and
$v_m = v_0$, whose vertices $v_0, \dots, v_{m-1}$ are pairwise distinct, in which every consecutive
pair has finite weight, and whose total weight is negative.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_hasNegativeDiagonal_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-has-negative-diagonal-sou).

## Without negative cycles, Floyd–Warshall finds no negative diagonal entry

Let $w$
assign a weight in $\mathbb{Z} \cup \{\infty\}$ to each ordered pair of vertices in
$\{0, \dots, n-1\}$, and let $D$ be the distance matrix computed by Floyd–Warshall from $w$. If $w$
has no negative cycle, then the negative-diagonal check on $D$ returns false, that is,
$D(v, v) \ge 0$ for every vertex $v$.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.floydWarshall_hasNegativeDiagonal_eq_false`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FloydWarshall/Correctness.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html#floyd-warshall-has-negative-diagonal-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Floyd–Warshall algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/floyd-warshall-algorithm)
