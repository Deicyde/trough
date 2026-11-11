---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MetricTSP.IsMetricCost, Cslib.Algorithms.Lean.MetricTSP.pathFrom, Cslib.Algorithms.Lean.MetricTSP.tourCost, Cslib.Algorithms.Lean.MetricTSP.Forest, Cslib.Algorithms.Lean.MetricTSP.Forest.preorder, Cslib.Algorithms.Lean.MetricTSP.Forest.weight, Cslib.Algorithms.Lean.MetricTSP.Forest.chain, Cslib.Algorithms.Lean.MetricTSP.preorderWalkAux
statement: formalized
proof: formalized
---

# Double-tree approximation for metric TSP

46 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html).

## Metric cost function

A cost function $d$ assigning to each pair of vertices a value in a
linearly ordered additive commutative monoid is metric when, for all vertices $x$, $y$, $z$, it
is symmetric, $d(x, y) = d(y, x)$, zero on the diagonal, $d(x, x) = 0$, nonnegative,
$0 \le d(x, y)$, and satisfies the triangle inequality $d(x, z) \le d(x, y) + d(y, z)$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.IsMetricCost`, a structure declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-metric-cost).

## Cost of a walk

Let $d$ be a cost function on the vertices with values in an additive
commutative monoid. For a vertex $x$ and a list $L = [y_1, \dots, y_n]$ of vertices, the cost of
the walk from $x$ through $L$ is $d(x, y_1) + d(y_1, y_2) + \dots + d(y_{n-1}, y_n)$, and $0$
when $L$ is empty.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.pathFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#path-from).

## Cost of a closed tour

For a cost function $d$ on the vertices with values in an additive
commutative monoid, the cost of the closed tour that visits $x_0, x_1, \dots, x_k$ in order and
returns to its first vertex is $\sum_{i=1}^{k} d(x_{i-1}, x_i) + d(x_k, x_0)$. The empty tour
costs $0$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.tourCost`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#tour-cost).

## Rooted forest in left-child right-sibling form

A rooted forest with vertices in $\alpha$
is either empty, or consists of a first tree with root $v$, whose subtrees form a forest (the
children of $v$), followed by a forest of the remaining trees (the siblings of $v$).

Formalized by `Cslib.Algorithms.Lean.MetricTSP.Forest`, an inductive type declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#forest).

## Preorder of a forest

The list of the vertices of a forest in preorder: empty for the empty
forest, and for a forest with first root $v$, children forest $C$ and sibling forest $S$, the
vertex $v$, followed by the preorder of $C$, followed by the preorder of $S$.

The preorder walk computes this list without appending lists.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.Forest.preorder`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#preorder).

## Weight of a forest below a vertex

For a cost function $d$ and a vertex $p$, the weight
of a forest hanging below $p$ is the total cost of its tree edges: each top-level vertex $v$ is
joined to $p$ by an edge of cost $d(p, v)$, and each vertex $u$ is joined to each of its children
$c$ by an edge of cost $d(u, c)$. The empty forest has weight $0$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.Forest.weight`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#weight).

## Path as a forest

The forest of a list $x_1, x_2, \dots, x_n$ of vertices is the path
$x_1, x_2, \dots, x_n$: $x_1$ is its only top-level vertex and each $x_{i+1}$ is the only child
of $x_i$. The empty list gives the empty forest.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.Forest.chain`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#chain).

## Preorder walk with an accumulator

For a forest $F$ and a list $a$ of vertices, this is the
timed computation defined as follows. On the empty forest it returns $a$ at no cost. On a forest
with first root $v$, children forest $C$ and sibling forest $S$, it charges one time unit, walks
$S$ with accumulator $a$ to get a list $b$, walks $C$ with accumulator $b$ to get a list $c$, and
returns $v$ followed by $c$. It thus returns the vertices of $F$ in preorder followed by $a$, at
one time unit per vertex of $F$.

The accumulator means no list is ever appended, so the untimed work is linear as well.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.preorderWalkAux`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#preorder-walk-aux).

## Preorder walk

For a forest $F$, the preorder walk of $F$ is the preorder walk of $F$ with
the empty list as accumulator: a timed computation that returns the vertices of $F$ in preorder,
at one time unit per vertex.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.preorderWalk`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#preorder-walk).

## The APPROX-TSP-TOUR algorithm

CLRS `APPROX-TSP-TOUR`, steps 3 and 4: given a root $r$
and a forest $F$ (the subtrees of a spanning tree with root $r$), return the tour that lists $r$
followed by the vertices of $F$ in preorder. As a timed computation it charges one unit for $r$
and one unit for each vertex visited by the preorder walk of $F$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.approxTSPTour`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#approx-tsptour).

## Result of the preorder walk with an accumulator

For every forest $F$ and every list $a$
of vertices, the preorder walk of $F$ with accumulator $a$ returns the vertices of $F$ in
preorder followed by $a$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.preorderWalkAux_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#preorder-walk-aux-ret).

## Running time of `APPROX-TSP-TOUR`

For every root $r$ and forest $F$, the running time of
`APPROX-TSP-TOUR` on $r$ and $F$ equals the length of the list of $r$ followed by the vertices of
$F$ in preorder: one unit per vertex of the returned tour.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.approxTSPTour_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#approx-tsptour-time).

## Changing the starting vertex of a walk

Let $d$ be a cost function on the vertices with
values in a linearly ordered additive commutative monoid, which is symmetric, zero on the
diagonal, nonnegative, and satisfies the triangle inequality. For vertices $q$, $p$ and a list $L$
of vertices, the cost of the walk from $q$ through $L$ is at most $d(q, p)$ plus the cost of the
walk from $p$ through $L$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.pathFrom_le_add`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#path-from-le-add).

## Shortcutting a closed walk through its base point

Let $d$ be a cost function on the
vertices with values in a linearly ordered additive commutative monoid, which is symmetric, zero
on the diagonal, nonnegative, and satisfies the triangle inequality. For a vertex $p$ and lists
$A$, $B$ of vertices, the cost of the walk that starts at $p$, visits $A$ and then $B$ in order
and returns to $p$ is at most the cost of the walk from $p$ through $A$ back to $p$ plus the cost
of the walk from $p$ through $B$ back to $p$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.pathFrom_append_append_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#path-from-append-append-le).

## Rerouting the end of a walk

Let $d$ be a cost function on the vertices with values in a
linearly ordered additive commutative monoid, which is symmetric, zero on the diagonal,
nonnegative, and satisfies the triangle inequality. For vertices $v$, $p$ and a list $C$ of
vertices, the cost of the walk from $v$ through $C$ ending at $p$ is at most the cost of the walk
from $v$ through $C$ ending back at $v$, plus $d(v, p)$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.pathFrom_append_singleton_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#path-from-append-singleton-le).

## The closed preorder walk below a vertex costs at most twice the forest

Let $d$ be a cost
function on the vertices with values in a linearly ordered additive commutative monoid, which is
symmetric, zero on the diagonal, nonnegative, and satisfies the triangle inequality. For a forest
$F$ and a vertex $p$, let $w$ be the weight of $F$ hanging below $p$: the total cost of the edges
joining $p$ to the top-level vertices of $F$ and each vertex of $F$ to its children. Then the cost
of the walk that starts at $p$, visits the vertices of $F$ in preorder and returns to $p$ is at
most $w + w$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.pathFrom_preorder_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#path-from-preorder-le).

## The preorder tour costs at most twice the tree

Let $d$ be a cost function on the
vertices with values in a linearly ordered additive commutative monoid that is symmetric, zero on
the diagonal, nonnegative and satisfies the triangle inequality. Let $T$ be a rooted tree with
root $r$, given by the forest $F$ of the subtrees of $r$, and let $w(T)$ be its weight, the total
cost of its edges. Then the closed tour that visits $r$, then the vertices of $F$ in preorder, and
returns to $r$ costs at most $2\,w(T)$.

## Sources

- CLRS Theorem 35.2, first half.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.tourCost_preorder_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#tour-cost-preorder-le).

## Preorder of a path

For every list $L$ of vertices, the preorder of the forest of $L$
(the path through the vertices of $L$ in order) is $L$ itself.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.Forest.preorder_chain`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#preorder-chain).

## Rooted spanning tree of a vertex list

The tree with root $r$ and subtree forest $F$ is a
spanning tree of a list $V$ of vertices when the vertices of $V$ are distinct and the list of $r$
followed by the vertices of $F$ in preorder is a permutation of $V$: the vertices of the tree are
those of $V$, each exactly once.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.IsSpanning`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-spanning).

## Minimum spanning tree of a vertex list

Let $d$ be a cost function on the vertices with
values in a linearly ordered additive commutative monoid. The tree with root $r$ and subtree
forest $F$ is a minimum spanning tree of a list $V$ of vertices for $d$ when it is a spanning tree
of $V$ (the vertices of $V$ are distinct and the list of $r$ followed by the vertices of $F$ in
preorder is a permutation of $V$) and, for every vertex $r'$ and forest $F'$ such that the tree
with root $r'$ and subtree forest $F'$ is a spanning tree of $V$, the weight of $F$ below $r$ is
at most the weight of $F'$ below $r'$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.IsMinSpanning`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-min-spanning).

## Tour of a vertex list

A list $H$ is a tour of a list $V$ of vertices when the vertices of
$V$ are distinct and $H$ is a permutation of $V$: $H$ lists each vertex of $V$ exactly once and
nothing else.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.IsTour`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-tour).

## A minimum spanning tree costs at most any tour

Let $d$ be a cost function on the
vertices with values in a linearly ordered additive commutative monoid that is symmetric, zero on
the diagonal, nonnegative and satisfies the triangle inequality. Let $V$ be a list of distinct
vertices. Let $T$ be a minimum spanning tree of $V$ for $d$: a rooted tree whose vertices are the
elements of $V$, each once, whose weight (the total cost of its edges) is at most that of every
such tree. Let $H$ be a tour of $V$, a list that is a permutation of $V$. Then the weight of $T$
is at most the cost of the closed tour $H$.

A tour minus its closing edge is a spanning path, which is a spanning tree.

## Sources

- CLRS Theorem 35.2, second half.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.weight_le_tourCost`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#weight-le-tour-cost).

## The approximate TSP tour is a tour

Let $V$ be a list of distinct vertices, and let $r$
and $F$ be such that $r$ followed by the vertices of the forest $F$ in preorder is a permutation
of $V$ (the tree with root $r$ and subtree forest $F$ spans $V$). Then the list returned by
`APPROX-TSP-TOUR` on $r$ and $F$ is a tour of $V$: it is a permutation of $V$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.approxTSPTour_isTour`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#approx-tsptour-is-tour).

## APPROX-TSP-TOUR on a given minimum spanning tree costs at most twice any tour

Let $d$ be a
cost function on vertices with values in a linearly ordered additive commutative monoid that is
symmetric, zero on the diagonal, nonnegative and satisfies the triangle inequality. Let $V$ be a
list of vertices, let the tree with root $r$ and subtree forest $F$ be a minimum spanning tree of
$V$ for $d$, and let $H$ be a tour of $V$. Then the cost under $d$ of the closed tour returned by
`APPROX-TSP-TOUR` on $r$ and $F$ is at most twice the cost under $d$ of the closed tour $H$.

## Sources

- CLRS, third edition, Theorem 35.2.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.approxTSPTour_two_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSP.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#approx-tsptour-two-approx).

## One step up a parent array

Let $p$ be a parent array on the vertices $\{0, \dots, n-1\}$,
assigning to each vertex $v$ either a parent $p(v)$ or no parent. Then $\operatorname{up}(v)$ is
the parent $p(v)$ when $v$ has one, and $v$ itself otherwise, so a root stays put.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.up`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#up).

## Children in a parent array

Let $p$ assign to each vertex of $\{0, \dots, n-1\}$
either a parent or nothing. The children of a vertex $v$ are the vertices $c$ whose parent
$p(c)$ is $v$, listed in increasing order.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.children`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#children).

## Forest of a parent array below a vertex

Let $p$ assign to each vertex of
$\{0, \dots, n-1\}$ either a parent or nothing. For $k \in \mathbb{N}$ and a vertex $v$, the
forest below $v$ of depth $k$ is empty when $k = 0$. For depth $k + 1$ it has one tree for each
child $c$ of $v$ (each vertex whose parent is $v$), in increasing order of $c$, namely $c$ with
the forest below $c$ of depth $k$ as its subtrees.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.buildForest`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#build-forest).

## Parent tree

Let $p$ assign to each vertex of $\{0, \dots, n-1\}$ either a parent or
nothing, and let a step up move a vertex to its parent, leaving a vertex without parent in place.
The parent array $p$ is a parent tree with root $r$ when $r$ has no parent and every vertex
reaches $r$ after finitely many steps up.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.ParentTree`, a structure declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#parent-tree).

## Descendant within $k$ levels

Let $p$ assign to each vertex of $\{0, \dots, n-1\}$
either a parent or nothing, and let a step up move a vertex to its parent, leaving a vertex
without parent in place. For $k \in \mathbb{N}$, a vertex $u$ lies strictly below a vertex $v$,
at most $k$ levels down, when for some $j < k$ the vertex reached from $u$ after $j$ steps up has
parent $v$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.DescK`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#desc-k).

## Weight of the forest built from a parent array

Let $p$ be a parent array on the vertices
$\{0, \dots, n-1\}$, let $d$ be a cost on ordered pairs of vertices with values in an additive
commutative monoid, and let $\operatorname{up}(u)$ be the parent of $u$, or $u$ itself if $u$ has
no parent. For every $k \in \mathbb{N}$ and every vertex $v$, let $F$ be the forest of the subtrees
of the children of $v$ in $p$, cut off $k$ levels below $v$. Then the weight under $d$ of $F$
hanging below $v$ equals the sum of $d(\operatorname{up}(u), u)$ over the vertices $u$ of $F$ in
preorder.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.weight_buildForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#weight-build-forest).

## Every non-root vertex lies below the root

Let $p$ assign to each vertex of
$\{0, \dots, n-1\}$ either a parent or nothing, forming a parent tree with root $r$, and let a
step up move a vertex to its parent, leaving a vertex without parent in place. Then every vertex
$u \ne r$ lies strictly below $r$, at most $n$ levels down: for some $j < n$, the vertex reached
from $u$ after $j$ steps up has parent $r$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.descK_root`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#desc-k-root).

## The forest of a parent tree spans all vertices

Let $p$ assign to each vertex of
$\{0, \dots, n-1\}$ either a parent or nothing, forming a parent tree with root $r$. Then $r$
together with the forest below $r$ of depth $n$ built from $p$ is a spanning tree of
$\{0, \dots, n-1\}$: $r$ followed by the vertices of the forest in preorder lists every vertex
exactly once.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.isSpanning_buildForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-spanning-build-forest).

## Complete graph as an ordered adjacency

For $n \in \mathbb{N}$, the complete graph on the
vertices $\{0, \dots, n-1\}$ as a directed adjacency: the vertices are listed in increasing
order, and the neighbours of each vertex $u$ are all vertices other than $u$, in increasing
order.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.completeAdjacency`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#complete-adjacency).

## Symmetrized edge weights

Given costs $d(u,v)$ on the vertices $\{0, \dots, n-1\}$ with
values in a type with commutative addition, the weight of an unordered pair $\{u, v\}$ is
$d(u,v) + d(v,u)$, which does not depend on the order of $u$ and $v$. When $d$ is symmetric this
is twice the cost, which leaves minimum spanning trees unchanged.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.symWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#sym-weight).

## Prim's parent array on the complete graph

Given costs $d(u,v)$ on the vertices
$\{0, \dots, n-1\}$ with values in a linearly ordered type with a zero and commutative addition,
and a root $r$, this is the parent array returned by Prim's algorithm run from $r$ on the
complete graph on these vertices, with the weight of the edge $\{u, v\}$ equal to
$d(u,v) + d(v,u)$: it sends each vertex to its parent, or to no parent.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primParents`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-parents).

## Forest of Prim's tree

Given costs $d(u,v)$ on the vertices $\{0, \dots, n-1\}$ with
values in a linearly ordered type with a zero and commutative addition, and a root $r$, take
Prim's parent array for $d$ and $r$ (Prim's algorithm run from $r$ on the complete graph with
edge weights $d(u,v) + d(v,u)$). This forest is the forest of the subtrees below $r$ in that
parent array, cut off $n$ levels below $r$, in left-child right-sibling form, with the children
of each vertex in vertex order.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primForest`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-forest).

## APPROX-TSP-TOUR with Prim's tree

Given costs $d(u,v)$ on the vertices
$\{0, \dots, n-1\}$ with values in a linearly ordered type with a zero and commutative addition,
and a root $r$, the tour is $r$ followed by the vertices of the forest of Prim's tree below $r$
in preorder. Its running time counts one unit per vertex of the tour; running Prim's algorithm
and building the forest are not counted.

This is CLRS APPROX-TSP-TOUR, with the minimum spanning tree computed by Prim.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTSPTour`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tsptour).

## Neighbours in the complete adjacency

For all vertices $u, v$ of $\{0, \dots, n-1\}$,
$v$ is listed among the neighbours of $u$ in the complete graph as an ordered adjacency if and
only if $u$ and $v$ are adjacent in the complete simple graph on $\{0, \dots, n-1\}$, that is,
$u \ne v$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.mem_completeAdjacency`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#mem-complete-adjacency).

## Prim's tree

Given costs $d(u,v)$ on the vertices $\{0, \dots, n-1\}$ with values in a
linearly ordered type with a zero and commutative addition, and a root $r$, Prim's tree is the
simple graph on these vertices in which distinct vertices $u$ and $v$ are adjacent when one of
them is the parent of the other in Prim's parent array for $d$ and $r$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTree`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tree).

## Prim's tree is a spanning tree

For costs $d(u,v)$ on the vertices $\{0, \dots, n-1\}$
with values in any linearly ordered type with a zero and commutative addition, and any root $r$,
Prim's tree for $d$ and $r$ is a tree on all of $\{0, \dots, n-1\}$, that is, a spanning tree of
the complete graph.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTree_isTree`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tree-is-tree).

## Prim's tree is a minimum spanning tree

Let $d(u,v)$ be real costs on the vertices
$\{0, \dots, n-1\}$, let $r$ be a vertex, and weigh each edge $\{u, v\}$ by $d(u,v) + d(v,u)$.
Then Prim's tree for $d$ and $r$ is a tree, and for every tree $H$ on these vertices the total
weight of the edges of Prim's tree is at most the total weight of the edges of $H$.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTree_isMinimumSpanningTree`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tree-is-minimum-spanning-tree).

## Prim's parent array is a parent tree

Let $W$ be a linearly ordered type with a zero and
a commutative addition, let $d$ assign a weight in $W$ to each ordered pair of vertices of
$\{0, \dots, n-1\}$, and let $r$ be a vertex. Then Prim's parent array for $d$ from $r$ is a
parent tree with root $r$: $r$ has no parent, and every vertex reaches $r$ after finitely many
steps up, where a step up moves a vertex to its parent and leaves a vertex without parent in
place.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.parentTree_primParents`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#parent-tree-prim-parents).

## Prim's forest spans all vertices

Let $W$ be a linearly ordered type with a zero and a
commutative addition, let $d$ assign a weight in $W$ to each ordered pair of vertices of
$\{0, \dots, n-1\}$, and let $r$ be a vertex. Then $r$ together with Prim's forest for $d$ and
$r$ is a spanning tree of $\{0, \dots, n-1\}$: $r$ followed by the vertices of the forest in
preorder lists every vertex exactly once.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.isSpanning_primForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#is-spanning-prim-forest).

## The tour from Prim's tree is a tour

For costs $d(u,v)$ on the vertices
$\{0, \dots, n-1\}$ with values in a linearly ordered type with a zero and commutative addition,
and any root $r$, the list returned by APPROX-TSP-TOUR with Prim's tree for $d$ and $r$ is a
permutation of $0, 1, \dots, n-1$: it visits every vertex exactly once.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTSPTour_isTour`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tsptour-is-tour).

## Edge sums over a parent tree

Let $p$ be a parent array on the vertices
$\{0, \dots, n-1\}$ in which the root $r$ has no parent and every chain of parents reaches
$r$, and let $w$ assign to each unordered pair $\{u, v\}$ of vertices (possibly $u = v$) a
value in a commutative additive monoid. Write $\hat p(u)$ for the parent of $u$, or $u$ itself
if $u$ has no parent. Then the sum of $w(e)$ over the edges $e$ of the parent graph (distinct
$u$ and $v$ are adjacent when one is the parent of the other) equals the sum of
$w(\{\hat p(u), u\})$ over the vertices $u$ of the forest built from $p$ below $r$, $n$ levels
deep, listed in preorder.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.sum_edgeFinset_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#sum-edge-finset-eq).

## APPROX-TSP-TOUR with Prim's tree is a 2-approximation

Let $d$ be a real metric cost
on the vertices $\{0, \dots, n-1\}$ (symmetric, zero on the diagonal, nonnegative, and
satisfying the triangle inequality), and let $r$ be a vertex. Then the cost of the closed tour
through the list returned by APPROX-TSP-TOUR with Prim's tree for $d$ and $r$ is at most twice
the cost of the closed tour through $H$, for every list $H$ that visits each of
$0, 1, \dots, n-1$ exactly once.

This is CLRS Theorem 35.2, with the minimum spanning tree computed by Prim.

Formalized by `Cslib.Algorithms.Lean.MetricTSP.primTSPTour_two_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/MetricTSPPrim.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html#prim-tsptour-two-approx).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Double-tree approximation for metric TSP](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/approximation-algorithms/double-tree-approximation-for-metric-tsp)
