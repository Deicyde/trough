---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Geometry.popNonLeft, Cslib.Algorithms.Lean.Geometry.chainScan, Cslib.Algorithms.Lean.Geometry.lowerHull, Cslib.Algorithms.Lean.Geometry.lowerHullOfPoints, Cslib.Algorithms.Lean.Geometry.lowerHull_sublist, Cslib.Algorithms.Lean.Geometry.lowerHull_head?, Cslib.Algorithms.Lean.Geometry.lowerHull_getLast?, Cslib.Algorithms.Lean.Geometry.lowerHull_turn_left
statement: formalized
proof: formalized
---

# Monotone chain convex hull algorithm

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html).

## Pop step of the monotone-chain scan

Let $\Bbbk$ be a linearly ordered field, let
$p \in \Bbbk^2$, and write $u \times v = u_1 v_2 - v_1 u_2$ for the cross product. Given a
stack of points of $\Bbbk^2$ listed top first, while the stack has at least two points, with
top $a$ and next point $b$, and $(a - b) \times (p - b) \le 0$ (so $b \to a \to p$ is not a
strict left turn), remove $a$. The result is the first stack reached that has fewer than two
points or whose top two points $a, b$ satisfy $(a - b) \times (p - b) > 0$; that stack is
returned unchanged. Each test of the sign of $(a - b) \times (p - b)$ costs one unit, and
nothing else is charged.

Formalized by `Cslib.Algorithms.Lean.Geometry.popNonLeft`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#pop-non-left).

## Monotone chain scan

Let $\Bbbk$ be a field with a linear order. Given a stack $S$ of
points of $\Bbbk^2$, listed top first, and a list of points $p_1, \dots, p_n$ of $\Bbbk^2$, the
scan processes $p_1, \dots, p_n$ in order: for each point $p = p_i$ it removes the top $a$ of the
stack as long as the stack has a second element $b$ with
$(a_x - b_x)(p_y - b_y) - (p_x - b_x)(a_y - b_y) \le 0$, and then pushes $p$. Starting from $S$,
the result is the final stack, top first. Each evaluation of this inequality costs one unit;
nothing else is counted.

Formalized by `Cslib.Algorithms.Lean.Geometry.chainScan`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#chain-scan).

## Lower chain

Let $\Bbbk$ be a field with a linear order. The lower chain of a list of
points $p_1, \dots, p_n$ of $\Bbbk^2$ is computed by Andrew's monotone chain scan: start with an
empty stack and process $p_1, \dots, p_n$ in order; for each point $p = p_i$, remove the top $a$
of the stack as long as the stack has a second element $b$ with
$(a_x - b_x)(p_y - b_y) - (p_x - b_x)(a_y - b_y) \le 0$, then push $p$. The lower chain is the
final stack read from bottom to top. Each evaluation of the inequality costs one unit; nothing
else is counted.

The scan is meant for points sorted strictly in lexicographic $(x, y)$ order; the chain then runs
from left to right.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull).

## Lower chain of unsorted points

Let $\Bbbk$ be a field with a linear order. For a list
$P$ of points of $\Bbbk^2$, sort $P$ by merge sort into nondecreasing lexicographic $(x, y)$
order and return the lower chain of the sorted list. Only the orientation tests of the lower
chain are counted; sorting costs nothing.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHullOfPoints`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-of-points).

## The lower chain is a sublist of the input

Let $\Bbbk$ be a linearly ordered field and
let $p_1, \dots, p_n$ be points of $\Bbbk^2$ that are strictly increasing in lexicographic
$(x, y)$ order. Then the lower chain of $p_1, \dots, p_n$ is a sublist of $p_1, \dots, p_n$: it
is $p_{i_1}, \dots, p_{i_m}$ for some indices $i_1 < \dots < i_m$.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-sublist).

## The lower chain starts at the first point

Let $\Bbbk$ be a linearly ordered field and
let $p_1, \dots, p_n$ be points of $\Bbbk^2$ that are strictly increasing in lexicographic
$(x, y)$ order. If $n \ge 1$, the lower chain of $p_1, \dots, p_n$ starts at $p_1$; if $n = 0$,
the lower chain is empty.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_head?`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-head).

## The lower chain ends at the last point

Let $\Bbbk$ be a linearly ordered field and let
$p_1, \dots, p_n$ be points of $\Bbbk^2$ that are strictly increasing in lexicographic
$(x, y)$ order. If $n \ge 1$, the lower chain of $p_1, \dots, p_n$ ends at $p_n$; if $n = 0$,
the lower chain is empty.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_getLast?`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-get-last).

## The lower chain turns strictly left

Let $\Bbbk$ be a linearly ordered field and let
$p_1, \dots, p_n$ be points of $\Bbbk^2$ that are strictly increasing in lexicographic $(x, y)$
order, with lower chain $c_0, \dots, c_{m-1}$. Writing
$\operatorname{cross}(u, v) = u_x v_y - v_x u_y$, for every $i$ with $i + 2 < m$ we have
$\operatorname{cross}(c_{i+1} - c_i, c_{i+2} - c_i) > 0$.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_turn_left`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-turn-left).

## Every input point lies on or left of each lower-chain edge

Let $\Bbbk$ be a linearly
ordered field and let $p_1, \dots, p_n$ be points of $\Bbbk^2$ that are strictly increasing in
lexicographic $(x, y)$ order, and write $\operatorname{cross}(u, v) = u_x v_y - v_x u_y$. For
every $s \in \{p_1, \dots, p_n\}$ and every pair of consecutive vertices $a, b$ of the lower chain
of $p_1, \dots, p_n$ we have $\operatorname{cross}(b - a, s - a) \ge 0$: the point $s$ lies on or
to the left of the directed edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_left_of_edges`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-left-of-edges).

## The lower-chain scan makes linearly many tests

Let $\Bbbk$ be a field with a linear
order. For every list of $n$ points of $\Bbbk^2$, computing its lower chain makes at most $2n$
orientation tests (cross-product evaluations).

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHull_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-time-le).

## Correctness of the lower chain for unsorted input

Let $\Bbbk$ be a linearly ordered
field, let $P$ be a list of pairwise distinct points of $\Bbbk^2$ in any order, write $\preceq$
for the lexicographic $(x, y)$ order on $\Bbbk^2$, and let $C = c_0, \dots, c_{m-1}$ be the
lower chain of the list obtained by sorting $P$ into $\preceq$-increasing order. Write
$\operatorname{cross}(u, v) = u_x v_y - v_x u_y$. Then every $c_j$ is a point of $P$; if $P$ is
nonempty then $m \ge 1$; if $m \ge 1$ then $c_0 \preceq s \preceq c_{m-1}$ for every $s \in P$;
for every $i$ with $i + 2 < m$ we have $\operatorname{cross}(c_{i+1} - c_i, c_{i+2} - c_i) > 0$;
and for every $s \in P$ and every pair of consecutive vertices $a, b$ of $C$ we have
$\operatorname{cross}(b - a, s - a) \ge 0$.

Formalized by `Cslib.Algorithms.Lean.Geometry.lowerHullOfPoints_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHull.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#lower-hull-of-points-spec).

## Upper chain

Let $K$ be a field with a linear order. The upper chain of a list of points
$p_1, \dots, p_n \in K^2$ is the lower chain of the reversed list $p_n, \dots, p_1$, together with
its cost: the same scan, counting the same orientation tests. For points sorted by $(x, y)$ it
runs from the last point back to the first.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull).

## Convex hull by the monotone chain algorithm

Let $\Bbbk$ be a field with a linear order.
The convex hull of a list $P$ of points of $\Bbbk^2$ is the lower chain of $P$ followed by the
upper chain of $P$ with its first and last points removed, together with its cost: the cost of
computing the lower chain plus the cost of computing the upper chain.

For points sorted strictly in lexicographic $(x, y)$ order, the result runs counterclockwise from
the first point.

Formalized by `Cslib.Algorithms.Lean.Geometry.convexHull`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#convex-hull).

## The upper chain is a reflected lower chain

Let $\Bbbk$ be a field with a linear order.
For every list $p_1, \dots, p_n$ of points of $\Bbbk^2$, the upper chain of the list is the image
under $p \mapsto -p$ of the lower chain of $-p_n, \dots, -p_1$, and the two computations have the
same cost.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-eq).

## The upper chain is a subsequence of the reversed input

Let $K$ be an ordered field and
let $p_1, \dots, p_n \in K^2$ be strictly increasing in the lexicographic $(x, y)$ order. Then the
upper chain of $p_1, \dots, p_n$ is a sublist of the reversed list $p_n, \dots, p_1$: it is
obtained from $p_n, \dots, p_1$ by deleting some of the entries.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-sublist).

## The upper chain starts at the last point

Let $p_1, \dots, p_n$ be points of $\Bbbk^2$,
for an ordered field $\Bbbk$, strictly increasing in the lexicographic order on $(x, y)$. If
$n = 0$ the upper chain is empty; otherwise its first vertex is $p_n$.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_head?`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-head).

## The upper chain ends at the first point

Let $p_1, \dots, p_n$ be points of $\Bbbk^2$, for
an ordered field $\Bbbk$, strictly increasing in the lexicographic order on $(x, y)$. If $n = 0$
the upper chain is empty; otherwise its last vertex is $p_1$.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_getLast?`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-get-last).

## The upper chain turns strictly left

Let $K$ be an ordered field, let
$p_1, \dots, p_n \in K^2$ be strictly increasing in the lexicographic $(x, y)$ order, and let
$c_0, c_1, \dots, c_{m-1}$ be the upper chain of $p_1, \dots, p_n$. Then for every $i$ with
$i + 2 < m$, we have $(c_{i+1} - c_i) \times (c_{i+2} - c_i) > 0$, where
$(u_1, u_2) \times (v_1, v_2) = u_1 v_2 - v_1 u_2$ is the cross product: the vertices $c_i$,
$c_{i+1}$, $c_{i+2}$ make a strict left turn.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_turn_left`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-turn-left).

## Every input point lies left of the upper chain

Let $p_1, \dots, p_n$ be points of
$\Bbbk^2$, for an ordered field $\Bbbk$, strictly increasing in the lexicographic order on
$(x, y)$. Then for every input point $s$ and every two consecutive vertices $a, b$ of the upper
chain, the cross product $(b - a) \times (s - a)$ is nonnegative: $s$ lies on or to the left of
the edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_left_of_edges`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-left-of-edges).

## Running time of the upper chain scan

Let $K$ be a field with a linear order and let
$p_1, \dots, p_n \in K^2$ be any $n$ points, sorted or not. Computing the upper chain of
$p_1, \dots, p_n$ costs at most $2n$, where the cost counts one unit per orientation test (one
cross-product comparison) and nothing else.

Formalized by `Cslib.Algorithms.Lean.Geometry.upperHull_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#upper-hull-time-le).

## The hull's vertices are input points

Let $p_1, \dots, p_n$ be points of $\Bbbk^2$, for an
ordered field $\Bbbk$, strictly increasing in the lexicographic order on $(x, y)$. Then every
vertex of their convex hull computed by the monotone chain algorithm is one of the $p_i$.

Formalized by `Cslib.Algorithms.Lean.Geometry.convexHull_subset`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#convex-hull-subset).

## The hull polygon contains every input point

Let $p_1, \dots, p_n$ be $n \ge 2$ points of
$\Bbbk^2$, for an ordered field $\Bbbk$, strictly increasing in the lexicographic order on $(x, y)$,
and let $v_1, \dots, v_m$ be the vertices of their convex hull computed by the monotone chain
algorithm. Then for every input point $s$ and every edge $(a, b)$ of the closed polygon
$v_1, \dots, v_m, v_1$ (that is, $a, b$ consecutive in this sequence), the cross product
$(b - a) \times (s - a)$ is nonnegative: $s$ lies on or to the left of the edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.Geometry.convexHull_left_of_edges`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#convex-hull-left-of-edges).

## The monotone chain hull makes at most $4n$ orientation tests

Let $\Bbbk$ be a field with
a linear order. For every list of $n$ points of $\Bbbk^2$, computing their convex hull by the
monotone chain algorithm costs at most $4n$, where each orientation test costs one unit.

Formalized by `Cslib.Algorithms.Lean.Geometry.convexHull_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#convex-hull-time-le).

## Lists of points turning strictly left

Let $\Bbbk$ be a field with a linear order and write
$(u_1, u_2) \times (v_1, v_2) = u_1 v_2 - v_1 u_2$ for the cross product on $\Bbbk^2$. A list
$q_1, \dots, q_k$ of points of $\Bbbk^2$ turns strictly left when every three consecutive points
do: $(q_{i+1} - q_i) \times (q_{i+2} - q_i) > 0$ for every $i$ with $1 \le i \le k - 2$. In
particular, every list of fewer than three points turns strictly left.

Formalized by `Cslib.Algorithms.Lean.Geometry.TurnsLeft`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#turns-left).

## The monotone chain hull of non-collinear points turns strictly left at every vertex

Let
$\Bbbk$ be a linearly ordered field and write $(u_1, u_2) \times (v_1, v_2) = u_1 v_2 - v_1 u_2$
for the cross product on $\Bbbk^2$. Let $P$ be a list of points of $\Bbbk^2$ that is strictly
increasing in the lexicographic order on $(x, y)$, and suppose the points of $P$ are not all
collinear: there are points $a, b, c$ of $P$ with $(b - a) \times (c - a) \ne 0$. Let $H$ be the
list of points returned by the monotone chain convex hull algorithm on $P$. Then the list
obtained from $H$ by appending its first two points (all of $H$ if $H$ has fewer than two points)
turns strictly left: any three consecutive points $q, r, s$ of it satisfy
$(r - q) \times (s - q) > 0$.

Read cyclically, this says the hull polygon turns strictly left at every vertex, including the
two vertices where the lower and upper chains meet.

Formalized by `Cslib.Algorithms.Lean.Geometry.convexHull_turnsLeft`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/ConvexHullPolygon.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html#convex-hull-turns-left).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone chain convex hull algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/computational-geometry/monotone-chain-convex-hull-algorithm)
