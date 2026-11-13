---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.UnionFind.Forest, Cslib.Algorithms.Lean.UnionFind.find, Cslib.Algorithms.Lean.UnionFind.pathLength, Cslib.Algorithms.Lean.UnionFind.findWithCost, Cslib.Algorithms.Lean.UnionFind.Equivalent, Cslib.Algorithms.Lean.UnionFind.find_isRoot, Cslib.Algorithms.Lean.UnionFind.find_parent, Cslib.Algorithms.Lean.UnionFind.find_in_class
statement: formalized
proof: formalized
---

# Disjoint-set data structure

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html).

## Parent forest with a depth certificate

A parent forest on the vertices
$\{0, \dots, n-1\}$ consists of a parent map $p$ from the vertices to themselves (a vertex $x$
with $p(x) = x$ is a root) and a depth certificate $d$ assigning a natural number to every
vertex, such that every non-root edge strictly decreases the certificate: if $p(x) \ne x$, then
$d(p(x)) < d(x)$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.Forest`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#forest).

## Root of a vertex in a parent forest

For a parent forest $F$ with parent map $p$ and a
vertex $x$, the root of $x$ is found by following parent pointers from $x$: it is $x$ itself
if $p(x) = x$, and otherwise it is the root of $p(x)$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find).

## Path length to the root

For a parent forest $F$ with parent map $p$ and a vertex $x$,
the path length of $x$ is the number of parent edges followed from $x$ to its root: it is $0$ if
$p(x) = x$, and otherwise one more than the path length of $p(x)$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.pathLength`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#path-length).

## Find with cost

For a vertex $x$ of a parent forest $F$, find with cost returns the root
that find returns for $x$, together with the cost $\ell(x) + 1$, where $\ell(x)$ is the path
length of $x$ (the number of non-root parent edges that find traverses from $x$). That is, it
charges one unit for every visited vertex, including the root.

Formalized by `Cslib.Algorithms.Lean.UnionFind.findWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-with-cost).

## Equivalent vertices of a parent forest

Two vertices $x$ and $y$ of a parent forest $F$
are equivalent when find returns the same root for $x$ as for $y$ in $F$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.Equivalent`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#equivalent).

## Find returns a root

For every vertex $x$ of a parent forest $F$, the vertex $r$ that find
returns for $x$ is a root of $F$: the parent of $r$ in $F$ is $r$ itself.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find_isRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-is-root).

## Find is unchanged along a parent pointer

For every vertex $x$ of a parent forest $F$,
find returns the same root for the parent of $x$ in $F$ as for $x$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find_parent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-parent).

## Every vertex is equivalent to its representative

For every vertex $x$ of a parent
forest $F$, the vertex $x$ is equivalent in $F$ to the root that find returns for $x$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find_in_class`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-in-class).

## The cost of find is the path length plus one

For every vertex $x$ of a parent forest $F$,
the cost that find with cost charges on $x$ equals $\ell(x) + 1$, where $\ell(x)$ is the path
length of $x$: the number of non-root parent edges that find traverses from $x$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.findWithCost_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-with-cost-time).

## The cost of find is at most the depth certificate plus one

For every vertex $x$ of a
parent forest $F$ with depth certificate $d$, the cost that find with cost charges on $x$ is at
most $d(x) + 1$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.findWithCost_time_le_depth`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-with-cost-time-le-depth).

## Parent map after linking two roots

Let $F$ be a parent forest with parent map $p$, and
let $r$ and $s$ be vertices. The linked parent map sends $r$ to $s$ and agrees with $p$ on every
other vertex: it maps $z$ to $s$ if $z = r$, and to $p(z)$ otherwise.

Formalized by `Cslib.Algorithms.Lean.UnionFind.linkParent`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#link-parent).

## Depth certificate after linking two roots

Let $F$ be a parent forest with depth
certificate $d$, and let $r$ and $s$ be vertices. The linked depth certificate assigns to a
vertex $z$ the number $d(z) + d(s) + 1$ if $z$ is equivalent to $r$ in $F$ (that is, $z$ and $r$
have the same root), and $d(z)$ otherwise.

Formalized by `Cslib.Algorithms.Lean.UnionFind.linkDepth`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#link-depth).

## Linking two roots of a parent forest

Let $F$ be a parent forest with parent map $p$ and
depth certificate $d$, and let $r \ne s$ be two distinct roots of $F$. Linking $r$ to $s$ gives
the parent forest whose parent map is the linked parent map (the parent of $r$ becomes $s$ and
all other parents are unchanged) and whose depth certificate is the linked depth certificate (the
certificate of every vertex equivalent to $r$ grows by $d(s) + 1$ and all others are unchanged).
These still satisfy the decreasing-certificate condition.

Formalized by `Cslib.Algorithms.Lean.UnionFind.link`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#link).

## Union in a union-find forest

Let $F$ be a union-find forest on $n$ vertices: each vertex
$z$ has a parent $p(z)$, where roots are their own parents, and a depth certificate
$d(z) \in \mathbb{N}$ with $d(p(z)) < d(z)$ whenever $p(z) \ne z$. Let $x$ and $y$ be vertices,
and let $r_x$ and $r_y$ be the roots reached from $x$ and $y$ by following parent pointers. If
$r_x = r_y$, the union of $x$ and $y$ in $F$ is $F$ itself. Otherwise it is the forest obtained
from $F$ by linking $r_x$ to $r_y$: the parent of $r_x$ becomes $r_y$, all other parent pointers
are unchanged, every vertex $z$ whose root is $r_x$ gets depth certificate $d(z) + d(r_y) + 1$,
and every other vertex keeps $d(z)$.

The operation is persistent: it returns a new forest and does not modify $F$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.union`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union).

## Representatives after a union

Let $F$ be a parent forest, let $x, y, z$ be vertices of
$F$, and let $F'$ be the forest obtained from $F$ by the union of $x$ and $y$. If $z$ is
equivalent to $x$ in $F$, then find returns for $z$ in $F'$ the root that find returns for $y$
in $F$; otherwise find returns the same root for $z$ in $F'$ as in $F$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-union).

## Union makes its arguments equivalent

For every parent forest $F$ and vertices $x$ and
$y$, the vertices $x$ and $y$ are equivalent in the forest obtained from $F$ by the union of $x$
and $y$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.union_equivalent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union-equivalent).

## Union of equivalent vertices changes nothing

If $x$ and $y$ are equivalent vertices of a
parent forest $F$, then the union of $x$ and $y$ in $F$ is $F$ itself.

Formalized by `Cslib.Algorithms.Lean.UnionFind.union_eq_self_of_equivalent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union-eq-self-of-equivalent).

## Equivalence after a union

Let $F$ be a parent forest and let $x, y, a, b$ be vertices of
$F$. Then $a$ and $b$ are equivalent in the forest obtained from $F$ by the union of $x$ and $y$
if and only if $a$ and $b$ are equivalent in $F$, or $a$ is equivalent to $x$ and $b$ is
equivalent to $y$ in $F$, or $a$ is equivalent to $y$ and $b$ is equivalent to $x$ in $F$.

Thus the union merges exactly the old classes of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.equivalent_union_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#equivalent-union-iff).

## Union preserves the representatives of unrelated classes

Let $F$ be a parent forest and
let $x, y, z$ be vertices of $F$. If $z$ is not equivalent to $x$ in $F$, then find returns the
same root for $z$ in the forest obtained from $F$ by the union of $x$ and $y$ as in $F$.

No hypothesis on $y$ is needed.

Formalized by `Cslib.Algorithms.Lean.UnionFind.find_union_of_unrelated`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-union-of-unrelated).

## Union in a parent forest with cost

For a parent forest $F$ and vertices $x$ and $y$, the
costed union returns the union of $x$ and $y$ in $F$ together with a cost equal to the cost of
finding the root of $x$ plus the cost of finding the root of $y$ (each one unit per visited
vertex, including the root), plus one more unit when the roots of $x$ and $y$ are distinct; when
they coincide, union performs no link and none is charged.

Formalized by `Cslib.Algorithms.Lean.UnionFind.unionWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union-with-cost).

## Cost bound for union in a parent forest

For every parent forest $F$ with depth
certificate $d$ and vertices $x$ and $y$, the cost charged for the union of $x$ and $y$ in $F$
(two root searches at one unit per visited vertex, plus one unit for the link when the roots
differ) is at most $d(x) + d(y) + 3$.

Formalized by `Cslib.Algorithms.Lean.UnionFind.unionWithCost_time_le_depth`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union-with-cost-time-le-depth).

## Correctness of the union-find equivalence query

Call two natural numbers $a$ and $c$
equivalent in a union-find structure when they have the same root, where a number that is not a
node is its own root. Let $U$ be a union-find structure with nodes $0, \dots, N-1$ and let
$x, y < N$. The equivalence query on $x$ and $y$, which runs FIND-SET with path compression on
$x$ and then on $y$, returns a union-find structure $U'$ and a boolean $b$ such that $U'$ has
$N$ nodes, $b$ is true if and only if $x$ and $y$ are equivalent in $U$, and for all natural
numbers $a$ and $c$, $a$ and $c$ are equivalent in $U'$ if and only if they are equivalent
in $U$.

Formalized by `Batteries.UnionFind.checkEquiv_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#check-equiv-spec).

## Connected components via union-find

Given a natural number $n$ and a list $E$ of pairs
of vertices in $\{0, \dots, n-1\}$, CONNECTED-COMPONENTS first builds the union-find structure
with $n$ singleton nodes $0, \dots, n-1$ by $n$ MAKE-SET calls. It then processes the pairs
$(u, v)$ of $E$ in list order: it asks whether $u$ and $v$ are equivalent using two FIND-SET
calls, keeping the path compression done by the query, and if they are not equivalent it
performs UNION on $u$ and $v$ (union by rank with path compression). It returns the final
union-find structure, which has $n$ nodes, together with the numbers of MAKE-SET, FIND-SET and
UNION calls made.

Formalized by `Batteries.UnionFind.connectedComponents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#connected-components).

## Connected components allocates $n$ nodes

For every natural number $n$ and every list
$E$ of pairs of vertices in $\{0, \dots, n-1\}$, the union-find structure returned by
CONNECTED-COMPONENTS on $n$ and $E$ has exactly $n$ nodes.

Formalized by `Batteries.UnionFind.connectedComponents_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#connected-components-size).

## Connected components computes reachability

Let $n$ be a natural number and let $E$ be a
list of pairs of vertices in $\{0, \dots, n-1\}$. For all vertices $a, b < n$, $a$ and $b$ are
equivalent in the union-find structure returned by CONNECTED-COMPONENTS on $n$ and $E$ if and
only if $a$ and $b$ are joined by a path in the simple graph on $\{0, \dots, n-1\}$ whose edges
are the unordered pairs $\{u, v\}$ with $(u, v)$ in $E$ and $u \ne v$.

Formalized by `Batteries.UnionFind.connectedComponents_equiv_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#connected-components-equiv-iff-reachable).

## Operation counts of connected components

Let $n$ be a natural number, let $E$ be a list
of pairs of vertices in $\{0, \dots, n-1\}$ and let $m$ be the length of $E$. Let $G$ be the
simple graph on $\{0, \dots, n-1\}$ whose edges are the unordered pairs $\{u, v\}$ with $(u, v)$
in $E$ and $u \ne v$, and let $k$ be the number of connected components of $G$. Running
CONNECTED-COMPONENTS on $n$ and $E$ makes exactly $n$ MAKE-SET calls, $2m$ FIND-SET calls and
$n - k$ UNION calls. Moreover, $k$ plus the number of UNION calls equals $n$, and if $n > 0$
then the number of UNION calls is at most $n - 1$.

These are the call counts recorded by the cost annotation, not bounds on parent-pointer visits.

Formalized by `Batteries.UnionFind.connectedComponents_time_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/ConnectedComponents.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#connected-components-time-spec).

## Cost-counted FIND auxiliary

For a union-find structure $S$ with node array $A$ and a
node $x < |S|$, this is the recursive path-compression routine of FIND, paired with a cost in
$\mathbb{N} \times \mathbb{N}$. It charges $(1, 0)$ for testing whether $x$ is a root. If the
parent $y$ of $x$ in $A$ equals $x$, it returns $A$ and the root $x$. Otherwise it runs on $y$,
obtaining an array $A'$ and a root $r$, charges $(0, 1)$ for one parent write, and returns $A'$
with the parent of $x$ set to $r$, together with $r$. The first cost coordinate thus counts root
tests and the second counts parent writes.

The returned array and root are exactly those of the Batteries FIND auxiliary; only the costs
are added.

Formalized by `Batteries.UnionFind.Internal.countedAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux).

## The cost-counted FIND auxiliary returns the uncounted result

For a union-find
structure $S$ and a node $x < |S|$, the value returned by the cost-counted FIND auxiliary on $x$
(the compressed node array together with the root of $x$), with its cost discarded, equals the
result of the Batteries path-compression auxiliary routine of FIND on $x$.

Formalized by `Batteries.UnionFind.Internal.countedAux_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux-ret).

## Cost of the FIND auxiliary at a root

Let $S$ be a union-find structure and $x < |S|$
a node. If the parent of $x$ in $S$ is $x$ itself, then the cost-counted FIND auxiliary on $x$
has cost $(1, 0)$: one root test and no parent writes.

Formalized by `Batteries.UnionFind.Internal.countedAux_time_root`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux-time-root).

## Cost recurrence of the FIND auxiliary at a non-root

Let $S$ be a union-find structure
and $x < |S|$ a node whose parent $y$ in $S$ differs from $x$. If $c_x$ and $c_y$ are the costs
of the cost-counted FIND auxiliary on $x$ and on $y$, then $c_x = (1, 0) + (c_y + (0, 1))$:
one root test at $x$, then the run on $y$, then one parent write.

Formalized by `Batteries.UnionFind.Internal.countedAux_time_step`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux-time-step).

## Root tests exceed parent writes by one

For a union-find structure $S$ and a node
$x < |S|$, if the cost-counted FIND auxiliary on $x$ has cost $(t, w)$, where $t$ counts root
tests and $w$ counts parent writes, then $t = w + 1$.

Formalized by `Batteries.UnionFind.Internal.countedAux_time_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux-time-balance).

## Cost-counted FIND

For a union-find structure $S$ and a node $x < |S|$, this runs the
cost-counted FIND auxiliary on $x$, obtaining a node array $A'$, a root $r$ and a cost $(t, w)$.
It returns the union-find structure with node array $A'$, together with $r$ as a node of that
structure (whose size equals $|S|$), at cost $(t, w)$.

It reuses the array and root of that single run; FIND is not run a second time.

Formalized by `Batteries.UnionFind.Internal.countedFind`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-find).

## The cost-counted FIND returns the FIND result

For a union-find structure $S$ and a node
$x < |S|$, the value returned by the cost-counted FIND on $x$ (the compressed union-find
structure together with the root of $x$), with its cost discarded, equals the result of the
Batteries FIND with path compression on $x$.

Formalized by `Batteries.UnionFind.Internal.countedFind_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-find-ret).

## Parent writes are bounded by the rank gap

Let $S$ be a union-find structure, let $R$
be one more than the maximum rank of a node of $S$, and let $x < |S|$ be a node. The number of
parent writes performed by the cost-counted FIND auxiliary on $x$ (the second coordinate of its
cost) is at most $R - \operatorname{rank}(x)$.

This is a per-call bound, not a logarithmic or amortized inverse-Ackermann bound.

Formalized by `Batteries.UnionFind.Internal.countedAux_writes_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-aux-writes-rank).

## FIND compresses exactly the original path to the root

Let $S$ be a union-find structure
with parent map $p$ (where $p(i) = i$ for $i \ge |S|$), let $x < |S|$, and let $p'$ be the parent
map of the structure produced by FIND with path compression on $x$. Then for every natural number
$i$, $p'(i)$ is the root of $x$ if $i = p^k(x)$ for some $k \ge 0$, and $p'(i) = p(i)$
otherwise.

Formalized by `Batteries.UnionFind.find_parent_eq_ite_iterate`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#find-parent-eq-ite-iterate).

## Effect of path-compressing find on each node

Let $s$ be a union-find structure on the
indices $0, \dots, n-1$ with parent function $p$, let $x < n$, and let $r$ be the root of $x$ in
$s$. After find with path compression is run on $x$, for every index $i < n$ the node at $i$ in
the resulting array keeps its rank from $s$, and its parent is $r$ if $i = p^k(x)$ for some
$k \ge 0$, and is its original parent $p(i)$ otherwise.

Formalized by `Batteries.UnionFind.getElem_find`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#get-elem-find).

## The root is reached in fewer parent steps than there are nodes

Let $S$ be a
union-find structure with $n$ nodes and parent map $p$, and let $x < n$. Then there is $d < n$
such that $p^d(x)$ is the root of $x$ and $p^k(x)$ is not the root of $x$ for every $k < d$.

Formalized by `Batteries.UnionFind.exists_first_iterate_rootD`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Find.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#exists-first-iterate-root-d).

## Ranks after linking two nodes of an array

For an array $A$ of union-find nodes, write
$\rho_A(i)$ for the rank stored at index $i$ of $A$, or $0$ if $i$ is not an index of $A$. Let
$x, y$ be indices of $A$ and let $A'$ be the array obtained from $A$ by the Batteries link by rank
of $x$ and $y$. Then for every natural number $i$, $\rho_{A'}(i) = \rho_A(y) + 1$ if $x \ne y$,
$\rho_A(x) = \rho_A(y)$ and $i = y$, and $\rho_{A'}(i) = \rho_A(i)$ otherwise.

Formalized by `Batteries.UnionFind.LinkInternal.rankD_linkAux`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#rank-d-link-aux).

## Ranks after linking in a union-find structure

Let $S$ be a union-find structure, write
$\rho(i)$ for the rank of $i$ in $S$ ($0$ if $i$ is not a node of $S$), and let $x, y$ be nodes of
$S$ such that $y$ is a root, that is, the parent of $y$ is $y$. Let $S'$ be the result of linking
$x$ and $y$ by rank. Then for every natural number $i$, the rank of $i$ in $S'$ is $\rho(y) + 1$
if $x \ne y$, $\rho(x) = \rho(y)$ and $i = y$, and is $\rho(i)$ otherwise.

Formalized by `Batteries.UnionFind.rank_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#rank-link).

## Linking two roots by rank

Let $U$ be a union-find structure on $\{0, \dots, n-1\}$ and
let $x, y < n$ be roots of $U$, i.e. each is its own parent. Let $U'$ be obtained by linking $x$
and $y$ by rank: nothing changes if $x = y$; otherwise, if $\operatorname{rank}(y) <
\operatorname{rank}(x)$ then $y$ gets parent $x$, and if not then $x$ gets parent $y$ and, when
the two ranks are equal, the rank of $y$ increases by one. Then for every natural number $i$,
where the root of an index $i \ge n$ is $i$ itself: if the root of $i$ in $U$ is $x$ or $y$, the
root of $i$ in $U'$ is $x$ when $\operatorname{rank}(y) < \operatorname{rank}(x)$ and $y$
otherwise; if the root of $i$ in $U$ is neither $x$ nor $y$, its root in $U'$ is the same as in
$U$.

Formalized by `Batteries.UnionFind.rootD_link_eq_ite`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#root-d-link-eq-ite).

## Union unfolds to two finds and a link

Let $U$ be a union-find structure on
$\{0, \dots, n-1\}$ and let $x, y < n$. Run find with path compression on $x$ in $U$, giving a
structure $U_1$ and a root $r_x$; then run find on $y$ in $U_1$ (not in $U$), giving a structure
$U_2$ and a root $r_y$. Then the node array of the union of $x$ and $y$ in $U$ equals the array
obtained from the node array of $U_2$ by linking $r_x$ and $r_y$ by rank: nothing changes if
$r_x = r_y$; otherwise, if $\operatorname{rank}(r_y) < \operatorname{rank}(r_x)$ then $r_y$ gets
parent $r_x$, and if not then $r_x$ gets parent $r_y$ and, when the two ranks are equal, the rank
of $r_y$ increases by one.

Formalized by `Batteries.UnionFind.LinkInternal.union_carried`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#union-carried).

## Path compression preserves ranks

Let $S$ be a union-find structure and $x$ a node of
$S$, and let $S'$ be the structure returned by FIND on $x$ with path compression. For every
natural number $i$, the rank of $i$ in $S'$ equals the rank of $i$ in $S$, where the rank of an
index that is not a node is $0$.

Formalized by `Batteries.UnionFind.LinkInternal.rank_find`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#rank-find).

## Ranks after a union

Let $S$ be a union-find structure, write $\rho(i)$ for the rank of
$i$ in $S$ ($0$ if $i$ is not a node of $S$) and $r(i)$ for the root of $i$ in $S$. For nodes
$x, y$ of $S$ and every natural number $i$, the rank of $i$ in the union of $x$ and $y$ in $S$
(union by rank with path compression) is $\rho(r(y)) + 1$ if $r(x) \ne r(y)$,
$\rho(r(x)) = \rho(r(y))$ and $r(y) = i$, and is $\rho(i)$ otherwise.

Formalized by `Batteries.UnionFind.rank_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#rank-union).

## Linking by rank with operation counts

Given an array $A$ of union-find nodes, each
storing a parent index and a rank, and indices $x, y$ of $A$, this computation returns an array
together with a count $(t, p, w)$ of rank tests $t$, parent writes $p$ and rank writes $w$. If
$x = y$ it returns $A$ with count $(0, 0, 0)$. Otherwise it makes one rank test; if the rank of $y$
is less than the rank of $x$, it sets the parent of $y$ to $x$ (one parent write). If not, it sets
the parent of $x$ to $y$ (one parent write) and makes a second rank test, and if the ranks of $x$
and $y$ are equal it also increases the rank of $y$ by one (one rank write).

The equality test $x = y$ is not counted as a rank test.

Formalized by `Batteries.UnionFind.LinkInternal.countedLinkAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-link-aux).

## Counted linking returns the linked array

For an array $A$ of union-find nodes and
indices $x, y$ of $A$, the array returned by counted linking of $x$ and $y$ in $A$ is exactly the
array produced by the uncounted Batteries link by rank of $x$ and $y$ in $A$.

Formalized by `Batteries.UnionFind.LinkInternal.countedLinkAux_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-link-aux-ret).

## Operation counts of linking by rank

Let $A$ be an array of union-find nodes, let $x, y$
be indices of $A$, and write $r_x$ and $r_y$ for the ranks stored at $x$ and $y$. Counted linking
of $x$ and $y$ in $A$ makes $(t, p, w)$ rank tests, parent writes and rank writes, where
$(t, p, w)$ is $(0, 0, 0)$ if $x = y$, is $(1, 1, 0)$ if $x \ne y$ and $r_y < r_x$, is
$(2, 1, 1)$ if $x \ne y$ and $r_x = r_y$, and is $(2, 1, 0)$ otherwise, that is, if $x \ne y$
and $r_x < r_y$.

Formalized by `Batteries.UnionFind.LinkInternal.countedLinkAux_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-link-aux-time).

## Union by rank with operation counts

For a union-find structure $S$ and indices $x, y$
of $S$, this computation runs counted FIND on $x$ in $S$, giving a structure $S_1$ and a root
$r_x$; then counted FIND on $y$ in $S_1$, giving a structure $S_2$ and a root $r_y$; then counted
linking of $r_x$ and $r_y$ in the node array of $S_2$. It returns the array produced by the
linking, with cost $((a, b), (t, p, w))$, where $a$ and $b$ are the total numbers of root tests
and parent writes of the two FIND calls, and $(t, p, w)$ counts the rank tests, parent writes and
rank writes of the linking.

Formalized by `Batteries.UnionFind.LinkInternal.countedUnion`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-union).

## Counted union returns the union's array

For a union-find structure $S$ and indices
$x, y$ of $S$, the array returned by the counted union of $x$ and $y$ in $S$ equals the node array
of the Batteries union of $x$ and $y$ in $S$ (union by rank with path compression).

Formalized by `Batteries.UnionFind.LinkInternal.countedUnion_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-union-ret).

## The FIND phases of a union make two more root tests than parent writes

For a
union-find structure $S$ and indices $x, y$ of $S$, in the counted union of $x$ and $y$ in $S$ the
total number of root tests made by its two FIND calls equals the total number of parent writes
they make plus $2$.

Formalized by `Batteries.UnionFind.LinkInternal.countedUnion_find_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UnionFind/Union.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html#counted-union-find-balance).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Disjoint-set data structure](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/disjoint-sets-and-dynamic-trees/disjoint-set-data-structure)
