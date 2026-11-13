---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FloydWarshall.IsEdgeBoundedShortestPathWeight, Cslib.Algorithms.Lean.FloydWarshall.isEdgeBoundedShortestPathWeight_iff, Cslib.Algorithms.Lean.Matrix.matrixAccumulate_minPlus_apply, Cslib.Algorithms.Lean.Matrix.matrixAccumulate_edgeBounded, Cslib.Algorithms.Lean.Matrix.matrix_pow_edgeBounded, Cslib.Algorithms.Lean.Matrix.copyCells, Cslib.Algorithms.Lean.Matrix.copyCells_ret, Cslib.Algorithms.Lean.Matrix.copyCells_time
statement: formalized
proof: formalized
---

# All-pairs shortest paths by min-plus products

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html).

## Shortest path weight with at most $r$ edges

Let $w$ be an $n \times n$ matrix of
weights in $\mathbb{Z} \cup \{\infty\}$ on the vertices $\{0, \dots, n-1\}$, let $r$ be a natural
number, let $i$ and $j$ be vertices, and let $d \in \mathbb{Z} \cup \{\infty\}$. A weighted path
from $i$ to $j$ is a nonempty list $p$ of vertices that starts at $i$, ends at $j$ and has finite
weight on each pair of consecutive vertices; its number of edges is its length minus one, and its
weight $w(p)$ is the sum of the weights of its edges. Then $d$ is the shortest weight of a path
from $i$ to $j$ with at most $r$ edges when $d \le w(p)$ for every weighted path $p$ from $i$ to
$j$ with at most $r$ edges, and either $d = \infty$ or $d = w(p)$ for some weighted path $p$ from
$i$ to $j$ with at most $r$ edges.

Paths may repeat vertices; no absence-of-negative-cycles hypothesis is needed.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.IsEdgeBoundedShortestPathWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#is-edge-bounded-shortest-path-weight).

## Characterization of the shortest path weight with at most $r$ edges

Let $w$ be an
$n \times n$ matrix of weights in $\mathbb{Z} \cup \{\infty\}$ on the vertices
$\{0, \dots, n-1\}$, let $r$ be a natural number, let $i$ and $j$ be vertices, and let
$d \in \mathbb{Z} \cup \{\infty\}$. For a weighted path $p$, write $w(p)$ for its weight. Then $d$
is the shortest weight of a path from $i$ to $j$ with at most $r$ edges if and only if
$d \le w(p)$ for every weighted path $p$ from $i$ to $j$ with at most $r$ edges, and either
$d = \infty$ or $d = w(p)$ for some weighted path $p$ from $i$ to $j$ with at most $r$ edges.

Formalized by `Cslib.Algorithms.Lean.FloydWarshall.isEdgeBoundedShortestPathWeight_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#is-edge-bounded-shortest-path-weight-iff).

## Entries of the min-plus matrix accumulator

Let $A$, $B$ and $C$ be $n \times n$
matrices with entries in $\mathbb{Z} \cup \{\infty\}$, viewed in the min-plus semiring. For all
$i, j \in \{0, \dots, n-1\}$, the entry $(i, j)$ of the matrix returned by the matrix
accumulator on $A$, $B$ and the accumulator $C$ equals
$\min\bigl(C_{ij}, \min_{k} (A_{ik} + B_{kj})\bigr)$, where $k$ ranges over
$\{0, \dots, n-1\}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.matrixAccumulate_minPlus_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#matrix-accumulate-min-plus-apply).

## One min-plus multiplication extends shortest paths by one edge

Let $A$ and $B$ be
$n \times n$ matrices with entries in $\mathbb{Z} \cup \{\infty\}$, viewed in the min-plus
semiring, and let $r$ be a natural number. Suppose that $B_{jj} = 0$ for every $j$, and that for
all $i$ and $j$ the entry $A_{ij}$ is the shortest weight of a path from $i$ to $j$ with at most
$r$ edges for the weight matrix $B$. Then for all $i$ and $j$, the entry $(i, j)$ of the matrix
returned by the matrix accumulator on $A$, $B$ and the accumulator whose entries are all $\infty$
is the shortest weight of a path from $i$ to $j$ with at most $r + 1$ edges for the weight
matrix $B$.

Paths may repeat vertices and edge weights may be negative.

Formalized by `Cslib.Algorithms.Lean.Matrix.matrixAccumulate_edgeBounded`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/Extend.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#matrix-accumulate-edge-bounded).

## Min-plus matrix powers give shortest path weights with at most $r$ edges

Let $W$ be an
$n \times n$ matrix with entries in $\mathbb{Z} \cup \{\infty\}$, viewed in the min-plus
semiring, with $W_{ii} = 0$ for every $i$. Then for every natural number $r$ and all $i$ and $j$,
the entry $(W^r)_{ij}$ of the $r$-th min-plus power of $W$ is the shortest weight of a path from
$i$ to $j$ with at most $r$ edges for the weight matrix $W$.

Paths may repeat vertices.

Formalized by `Cslib.Algorithms.Lean.Matrix.matrix_pow_edgeBounded`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/MatrixPower.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/MatrixPower.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#matrix-pow-edge-bounded).

## Counted copy of a square matrix

Given an $n \times n$ matrix $A$ (a vector of $n$ rows,
each a vector of $n$ entries), this computation returns the matrix whose $(i, j)$ entry is
$A_{ij}$, traversing the entries row by row and charging a cost of $(1, (0, 0))$ for each entry,
that is, one logical assignment in the first cost coordinate and nothing in the other two.

Formalized by `Cslib.Algorithms.Lean.Matrix.copyCells`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#copy-cells).

## The counted matrix copy returns its input

For every $n \times n$ matrix $A$ with entries
in any type, the value returned by the counted copy of $A$ is $A$ itself.

Formalized by `Cslib.Algorithms.Lean.Matrix.copyCells_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#copy-cells-ret).

## Cost of the counted matrix copy

For every $n \times n$ matrix $A$ with entries in any
type, the counted copy of $A$ has total cost $(n^2, (0, 0))$: exactly $n^2$ logical assignments
in the first cost coordinate and zero in the other two.

Formalized by `Cslib.Algorithms.Lean.Matrix.copyCells_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#copy-cells-time).

## Counted zero initialization of a square matrix

For a type $\alpha$ with a zero element
and a natural number $n$, this computation returns the $n \times n$ matrix over $\alpha$ all of
whose entries are $0$, producing the entries row by row and charging a cost of $(1, (0, 0))$ for
each entry, that is, one logical assignment in the first cost coordinate and nothing in the
other two.

Formalized by `Cslib.Algorithms.Lean.Matrix.fillCells`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#fill-cells).

## The counted zero initialization returns the zero matrix

For every type $\alpha$ with a
zero element and every natural number $n$, the counted zero initialization of size $n$ over
$\alpha$ returns the $n \times n$ matrix all of whose entries are $0$.

Formalized by `Cslib.Algorithms.Lean.Matrix.fillCells_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#fill-cells-ret).

## Cost of the counted zero initialization

For every type $\alpha$ with a zero element and
every natural number $n$, the counted zero initialization of size $n$ over $\alpha$ has total
cost $(n^2, (0, 0))$: exactly $n^2$ logical assignments in the first cost coordinate and zero in
the other two.

Formalized by `Cslib.Algorithms.Lean.Matrix.fillCells_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Assignments.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Matrix/Assignments.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#fill-cells-time).

## FASTER-APSP

Let $W$ be an $n \times n$ matrix over a type with addition, multiplication
and zero. FASTER-APSP copies $W$ into a matrix $L$ and sets $r = 1$. While $r < n - 1$, it fills
a new $n \times n$ matrix $M$ with zeros, sets each entry to
$M_{ij} = 0 + L_{i0} L_{0j} + \dots + L_{i,n-1} L_{n-1,j}$ (adding the terms from left to right),
copies $M$ into $L$ and doubles $r$. It returns the final $L$. The run also records three counts:
one assignment for each matrix cell copied or filled with zero, and one scalar addition and one
scalar multiplication for each term added to an entry of $M$.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp).

## FASTER-APSP returns a power of the input matrix

Let $\alpha$ be a semiring, let $W$ be
an $n \times n$ matrix over $\alpha$, and let $k = \lceil \log_2 (n - 1) \rceil$ be the least
natural number with $n - 1 \le 2^k$ (so $k = 0$ when $n \le 2$). The matrix returned by
FASTER-APSP on $W$ is the matrix power $W^{2^k}$, with products computed in $\alpha$.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp-ret).

## Operation counts of FASTER-APSP

Let $\alpha$ be a type with addition, multiplication and
zero, let $W$ be an $n \times n$ matrix over $\alpha$, and let $k = \lceil \log_2 (n - 1) \rceil$ be
the least natural number with $n - 1 \le 2^k$. On input $W$, FASTER-APSP performs exactly
$n^2 + 2 k n^2$ copy and fill assignments, $k n^3$ scalar additions and $k n^3$ scalar
multiplications.

Assignments count the matrix cells copied or filled with zero; the accumulator vector updates
inside the matrix multiplications are not counted.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Basic.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp-time).

## Asymptotic operation count of FASTER-APSP

Let $\alpha$ be a type with addition,
multiplication and zero, and for each $n$ let $W_n$ be an $n \times n$ matrix over $\alpha$. The
total number of copy and fill assignments, scalar additions and scalar multiplications that
FASTER-APSP performs on $W_n$ is $\Theta(n^3 \log n)$ as $n \to \infty$.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP_time_isTheta`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Complexity.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Complexity.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp-time-is-theta).

## Slow all-pairs shortest paths (SLOW-APSP)

Let $W$ and $L^{(0)}$ be $n \times n$ matrices
over the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, in which addition is $\min$ and
multiplication is $+$. SLOW-APSP copies $L^{(0)}$ cell by cell and then runs $\max(n - 1, 0)$
phases. Phase $r$ fills a fresh $n \times n$ matrix $M$ with $\infty$, then for each triple
$(i, j, k)$ in increasing $i$-$j$-$k$ order sets $M_{ij} \leftarrow \min(M_{ij}, L^{(r-1)}_{ik} +
W_{kj})$, and finally copies $M$ cell by cell to give $L^{(r)}$; the result is $L^{(n-1)}$. The
cost is a triple of natural numbers: the first coordinate counts one assignment for each cell
copied or filled, and the second and third coordinates count one scalar addition and one scalar
minimum for each update $M_{ij} \leftarrow \min(M_{ij}, L^{(r-1)}_{ik} + W_{kj})$.

Accumulator updates inside the loop are not charged as assignments.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp).

## SLOW-APSP returns a min-plus matrix power

For $n \times n$ matrices $W$ and $L^{(0)}$ over
the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, in which addition is $\min$ and
multiplication is $+$, the matrix returned by SLOW-APSP on $W$ and $L^{(0)}$ equals the
min-plus matrix product $L^{(0)} W^{n-1}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp-ret).

## Bounded-edge shortest weights from SLOW-APSP

Let $W$ and $L^{(0)}$ be
$n \times n$ matrices over the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, and let $w_{xy}$
be the underlying value in $\mathbb{Z} \cup \{\infty\}$ of $W_{xy}$. Suppose that $w_{ii} = 0$ for
every $i$ and that the underlying value of $L^{(0)}_{ij}$ is $0$ if $i = j$ and $\infty$ otherwise.
Then for all $i, j \in \{0, \dots, n-1\}$, the underlying value $d$ of the $(i, j)$ entry of the
matrix returned by SLOW-APSP on $W$ and $L^{(0)}$ is at most the weight of every path from $i$ to
$j$ with at most $n - 1$ edges, and $d$ is either $\infty$ or the weight of such a path. Here a
path from $i$ to $j$ is a nonempty sequence of vertices that starts at $i$, ends at $j$ and has
$w_{xy} \ne \infty$ for each pair of consecutive vertices $x, y$; vertices may repeat, its number
of edges is its number of vertices minus one, and its weight is the sum of these $w_{xy}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP_edgeBounded`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp-edge-bounded).

## SLOW-APSP computes shortest-path weights

Let $W$ and $L^{(0)}$ be $n \times n$ matrices
over the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, and let $w_{xy}$ be the underlying value
in $\mathbb{Z} \cup \{\infty\}$ of $W_{xy}$. Suppose that $w_{ii} = 0$ for every $i$, that the
underlying value of $L^{(0)}_{ij}$ is $0$ if $i = j$ and $\infty$ otherwise, and that $w$ has no
negative cycle. Then for all $i, j \in \{0, \dots, n-1\}$, the underlying value $d$ of the
$(i, j)$ entry of the matrix returned by SLOW-APSP on $W$ and $L^{(0)}$ is at most the weight of
every path from $i$ to $j$, and $d$ is either $\infty$ or the weight of some path from $i$ to $j$.
Here a path from $i$ to $j$ is a nonempty sequence of vertices that starts at $i$, ends at $j$ and
has $w_{xy} \ne \infty$ for each pair of consecutive vertices $x, y$; its weight is the sum of
these $w_{xy}$. A negative cycle is a path from a vertex to itself with at least two vertices,
negative weight, and no repeated vertex once its last vertex is removed.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP_distance_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp-distance-spec).

## Exact operation counts of SLOW-APSP

For all $n \times n$ matrices $W$ and $L^{(0)}$ over
the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, the cost of SLOW-APSP on $W$ and $L^{(0)}$
is the triple $(n^2 + 2(n-1)n^2,\ (n-1)n^3,\ (n-1)n^3)$ of cell assignments (copies and fills),
scalar additions and scalar minimums, where $n - 1$ means $\max(n - 1, 0)$.

The assignment count excludes the accumulator updates inside the min-plus accumulation loop.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp-time).

## SLOW-APSP takes quartic time

For any choice, for each $n$, of $n \times n$ matrices $W_n$
and $L^{(0)}_n$ over the min-plus semiring on $\mathbb{Z} \cup \{\infty\}$, the total cost of
SLOW-APSP on $W_n$ and $L^{(0)}_n$, that is the number of cell assignments (copies and fills)
plus the number of scalar additions plus the number of scalar minimums, is $\Theta(n^4)$ as
$n \to \infty$.

Formalized by `Cslib.Algorithms.Lean.Matrix.slowAPSP_time_isTheta`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/SlowAPSP.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#slow-apsp-time-is-theta).

## FASTER-APSP computes edge-bounded shortest-path weights

Let $W$ be an $n \times n$
matrix with entries in $\mathbb{Z} \cup \{\infty\}$, read as edge weights of a directed graph on
the vertices $0, \dots, n - 1$ (weight $\infty$ meaning no edge), with $W_{ii} = 0$ for every
$i$, and let $k = \lceil \log_2 (n - 1) \rceil$ be the least natural number with
$n - 1 \le 2^k$. Run FASTER-APSP on $W$ over the min-plus semiring, whose addition is $\min$
and whose multiplication is $+$. Then for all vertices $i$ and $j$, the returned entry $d$ at
$(i, j)$ is at most the weight of every path from $i$ to $j$ with at most $2^k$ edges, all of
finite weight, and either $d = \infty$ or $d$ is the weight of such a path. Paths are
nonempty vertex sequences and may repeat vertices; no assumption on negative cycles is made.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP_edgeBounded`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Correctness.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Correctness.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp-edge-bounded).

## FASTER-APSP computes shortest-path weights

Let $W$ be an $n \times n$ matrix with
entries in $\mathbb{Z} \cup \{\infty\}$, read as edge weights of a directed graph on the
vertices $0, \dots, n - 1$ (weight $\infty$ meaning no edge), such that $W_{ii} = 0$ for every
$i$ and $W$ has no negative cycle. Run FASTER-APSP on $W$ over the min-plus semiring, whose
addition is $\min$ and whose multiplication is $+$. Then for all vertices $i$ and $j$, the
returned entry $d$ at $(i, j)$ is the shortest-path weight from $i$ to $j$: $d$ is at most the
weight of every path from $i$ to $j$ all of whose edges have finite weight, and either
$d = \infty$ or $d$ is the weight of such a path. Paths are nonempty vertex sequences and may
repeat vertices.

Formalized by `Cslib.Algorithms.Lean.Matrix.fasterAPSP_distance_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Correctness.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/ShortestPath/FasterAPSP/Correctness.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html#faster-apsp-distance-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: All-pairs shortest paths by min-plus products](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/shortest-paths/all-pairs-shortest-paths-by-min-plus-products)
