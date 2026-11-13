---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Hierholzer.edgeListOf, Cslib.Algorithms.Lean.Hierholzer.edgeList, Cslib.Algorithms.Lean.Hierholzer.walkEdges, Cslib.Algorithms.Lean.Hierholzer.IsBalanced, Cslib.Algorithms.Lean.Hierholzer.IsSemiBalanced, Cslib.Algorithms.Lean.Hierholzer.IsEulerPath, Cslib.Algorithms.Lean.Hierholzer.IsEulerCircuit, Cslib.Algorithms.Lean.Hierholzer.visit
statement: formalized
proof: formalized
---

# Hierholzer's algorithm for Euler circuits

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html).

## Edge list of an adjacency function

Given a directed adjacency graph $G$ and a function
$R$ assigning to each vertex $u$ a list $R(u)$ of vertices, the edge list of $R$ is the list of
pairs $(u, w)$, one for each entry $w$ of $R(u)$, taken over the vertices $u$ in the order of the
vertex enumeration of $G$ and, for each $u$, in the order of $R(u)$. A repeated entry gives a
repeated pair.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.edgeListOf`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#edge-list-of).

## Edge list of a directed graph

The edge list of a directed adjacency graph $G$ is the list
of pairs $(u, w)$, one for each entry $w$ of the adjacency list of $u$, taken over the vertices
$u$ in the order of the vertex enumeration of $G$ and, for each $u$, in adjacency-list order. A
repeated adjacency entry gives a repeated pair, so $G$ is read as a multigraph with one edge
occurrence per entry.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.edgeList`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#edge-list).

## Steps of a walk

For a finite sequence of vertices $W = (w_0, w_1, \dots, w_n)$, the
steps of $W$ are the list of consecutive pairs $((w_0, w_1), (w_1, w_2), \dots, (w_{n-1}, w_n))$,
in order. A sequence with at most one vertex has no steps.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.walkEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#walk-edges).

## Balanced directed multigraph

A finite directed multigraph, read from its adjacency lists
with each entry $w$ in the list of $u$ counted as one occurrence of the edge $u \to w$, is
balanced when every vertex is the source of as many edge occurrences as it is the target of.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.IsBalanced`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-balanced).

## Semi-balanced directed multigraph

A finite directed multigraph is semi-balanced for
vertices $s$ and $t$ when, for every vertex $x$, the number of edge occurrences leaving $x$ plus
$[x = t]$ equals the number entering $x$ plus $[x = s]$, where $[P]$ is $1$ if $P$ holds and $0$
otherwise. So for $s \ne t$, one more edge occurrence leaves $s$ than enters it, one more enters
$t$ than leaves it, and every other vertex is balanced; for $s = t$ every vertex is balanced.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.IsSemiBalanced`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-semi-balanced).

## Euler path in a directed multigraph

In a finite directed multigraph, a list of vertices
$W = (w_0, \dots, w_k)$ is an Euler path from $s$ to $t$ when $w_0 = s$, $w_k = t$, and its list
of steps $(w_0, w_1), \dots, (w_{k-1}, w_k)$ is a permutation of the list of edge occurrences of
the graph, so that each edge occurrence, counted with multiplicity, is traversed exactly once.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.IsEulerPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-euler-path).

## Euler circuit in a directed multigraph

In a finite directed multigraph, a list of
vertices $W$ is an Euler circuit from a vertex $s$ when it is an Euler path from $s$ to $s$: it
starts and ends at $s$, and its list of consecutive pairs is a permutation of the list of edge
occurrences of the graph.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.IsEulerCircuit`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-euler-circuit).

## Hierholzer's recursion

Given a fuel $n$, a vertex $v$, an assignment $R$ of a list of
remaining out-neighbours to each vertex, and a list $\mathit{acc}$ of vertices, the recursion
returns a list of vertices and a new assignment, with a cost. With fuel $0$ it returns
$(\mathit{acc}, R)$ at cost $0$. With fuel $n + 1$: if $R(v)$ is empty, it returns $v$ followed by
$\mathit{acc}$ together with $R$, at cost $0$; otherwise $R(v)$ is $w$ followed by a list
$\mathit{rest}$, and it replaces $R(v)$ by $\mathit{rest}$, runs the recursion with fuel $n$ from
$w$ on the new assignment with accumulator $\mathit{acc}$, obtaining $(L_1, R_1)$, and returns the
result of the recursion with fuel $n$ from $v$ on $R_1$ with accumulator $L_1$, at cost $1$ plus
the costs of the two calls.

This follows unused edges depth first and splices sub-tours in; too little fuel can stop it
early. Hierholzer's algorithm runs it with fuel one more than the number of edge occurrences.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.visit`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#visit).

## Hierholzer's algorithm

Let $G$ be a directed adjacency graph, read as a multigraph with
one edge occurrence per adjacency entry, let $s$ be a vertex, and let $m$ be the number of edge
occurrences of $G$, that is, the length of its edge list. Hierholzer's algorithm on $G$ from $s$
runs Hierholzer's recursion from $s$ with fuel $m + 1$, with the adjacency list of each vertex as
its list of remaining out-neighbours and the empty list as accumulator, and returns the list of
vertices produced by the recursion, at the cost of the recursion.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.hierholzer`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#hierholzer).

## Steps of a concatenated walk

Let $A$ and $B$ be nonempty vertex sequences, where $A$
ends at the vertex $a$ and $B$ starts at the vertex $b$. Then the steps of the concatenation
$A B$ are the steps of $A$, followed by the step $(a, b)$, followed by the steps of $B$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.walkEdges_append`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#walk-edges-append).

## Moving a block of a list in front of an element is a permutation

For an element $e$ and
lists $A$, $B$, $C$ of the same type, the list $e \cdot A \cdot B \cdot C$ is a permutation of
$B \cdot e \cdot A \cdot C$, where $\cdot$ denotes concatenation and $e$ stands for the
one-element list.

This is how a sub-tour $B$ is spliced in front of the edge $e$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.perm_splice`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#perm-splice).

## Semi-balanced edge list

A list $E$ of ordered pairs of vertices is semi-balanced for
vertices $v$ and $t$ when, for every vertex $x$, the number of pairs in $E$ with first component
$x$ plus $[x = t]$ equals the number with second component $x$ plus $[x = v]$, where $[P]$ is $1$
if $P$ holds and $0$ otherwise. So for $v \ne t$, $v$ has one more outgoing than incoming
occurrence, $t$ one more incoming than outgoing, and every other vertex is balanced; for $v = t$
every vertex is balanced.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.SemiBalancedEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#semi-balanced-edges).

## Balanced edge list

A list $E$ of ordered pairs of vertices, read as directed edge
occurrences, is balanced when every vertex $x$ occurs as the first component of exactly as many
entries of $E$ as it occurs as the second component, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.BalancedEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#balanced-edges).

## Contract of Hierholzer's recursion

Let $G$ be a finite directed multigraph, let $R$
assign to each vertex $u$ a list $R(u)$ of remaining out-neighbours, and let $E(R)$ be the list
of remaining edge occurrences, one pair $(u, w)$ for each entry $w$ of $R(u)$. Let $v$ and $t$ be
vertices, $\mathit{acc}$ a list of vertices and $n$ a natural number with $|E(R)| < n$, and
suppose $E(R)$ is semi-balanced for $v$ and $t$: for every vertex $x$, the number of pairs in
$E(R)$ with first component $x$ plus $[x = t]$ equals the number with second component $x$ plus
$[x = v]$, where $[P]$ is $1$ if $P$ holds and $0$ otherwise. Let $(L, R')$ be the result and $c$
the cost of Hierholzer's recursion with fuel $n$ from $v$ on $R$ with accumulator $\mathit{acc}$.
Then there is a list of vertices $W$ such that $L$ is $W$ followed by $\mathit{acc}$; $W$ starts
at $v$ and ends at $t$; $E(R)$ is a permutation of the steps (consecutive pairs) of $W$ followed
by $E(R')$; every vertex is the first component of as many pairs of $E(R')$ as it is the second
component of; $R'(x)$ is empty for every vertex $x$ of $W$; $R'(x)$ is a suffix of $R(x)$ for
every vertex $x$; and $c + |E(R')| = |E(R)|$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.visit_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#visit-spec).

## Hierholzer's algorithm returns a trail in a directed multigraph

Let $G$ be a directed
adjacency graph, read as a multigraph with one edge per adjacency entry, and let $s$ and $t$ be
vertices such that $G$ is semi-balanced for $s$ and $t$. Then the vertex sequence $W$ returned by
Hierholzer's algorithm on $G$ from $s$ starts at $s$ and ends at $t$, and the edge list of $G$ is a
permutation of the list of consecutive pairs of $W$ followed by some further list of pairs. So $W$
is a walk from $s$ to $t$ that uses each edge occurrence at most once; reachability is not
assumed.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.hierholzer_trail`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#hierholzer-trail).

## Hierholzer's algorithm finds Euler paths in directed multigraphs

Let $G$ be a directed
adjacency graph, read as a multigraph with one edge per adjacency entry, and let $s$ and $t$ be
vertices such that $G$ is semi-balanced for $s$ and $t$ (at $s$ one more edge occurrence leaves
than enters, at $t$ one more enters than leaves, and at every other vertex as many leave as enter;
at every vertex when $s = t$) and the source of every edge of $G$ is reachable from $s$. Then the
vertex sequence returned by Hierholzer's algorithm on $G$ from $s$ is an Euler path of $G$ from $s$
to $t$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.hierholzer_isEulerPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#hierholzer-is-euler-path).

## Hierholzer's algorithm finds Euler circuits in directed multigraphs

Let $G$ be a directed
adjacency graph, read as a multigraph with one edge per adjacency entry, that is balanced (every
vertex is the source of exactly as many edge occurrences as it is the target of), and let $s$ be a
vertex such that the source of every edge of $G$ is reachable from $s$. Then the vertex sequence
returned by Hierholzer's algorithm on $G$ from $s$ is an Euler circuit of $G$ from $s$.

## Sources

- CLRS, third edition, Problem 22-3, sufficiency with the algorithm; strong connectivity is weakened to reachability from $s$ of the source of every edge.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.hierholzer_isEulerCircuit`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#hierholzer-is-euler-circuit).

## Running time of Hierholzer's algorithm

Let $G$ be a directed adjacency graph, read as a
multigraph with one edge per adjacency entry, and let $s$ and $t$ be vertices such that $G$ is
semi-balanced for $s$ and $t$ and the source of every edge of $G$ is reachable from $s$. Then
Hierholzer's algorithm on $G$ from $s$ costs exactly $|E|$ units, where $|E|$ is the number of
edge occurrences of $G$, that is, the length of its edge list.

The cost model charges one unit per edge traversal (removing the head of an adjacency list);
reading an adjacency list and emitting a vertex are free.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.hierholzer_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#hierholzer-time).

## A directed multigraph with an Euler path is semi-balanced

If a finite directed
multigraph has an Euler path from $s$ to $t$, then it is semi-balanced for $s$ and $t$: counting
edge occurrences, $s$ has one more outgoing than incoming edge, $t$ one more incoming than
outgoing, and every other vertex is balanced (every vertex, when $s = t$).

Formalized by `Cslib.Algorithms.Lean.Hierholzer.isSemiBalanced_of_isEulerPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-semi-balanced-of-is-euler-path).

## A directed multigraph with an Euler circuit is balanced

If a finite directed multigraph
has an Euler circuit from some vertex $s$, then it is balanced: every vertex is the source of as
many edge occurrences as it is the target of.

This is the necessity direction of CLRS Problem 22-3.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.isBalanced_of_isEulerCircuit`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-balanced-of-is-euler-circuit).

## Euler path criterion for directed multigraphs

Let $G$ be a directed adjacency graph, read
as a multigraph with one edge per adjacency entry, and let $s$ and $t$ be vertices such that the
source of every edge of $G$ is reachable from $s$. Then $G$ has an Euler path from $s$ to $t$ if
and only if $G$ is semi-balanced for $s$ and $t$: at $s$ one more edge occurrence leaves than
enters, at $t$ one more enters than leaves, and every other vertex is the source of exactly as
many edge occurrences as it is the target of (every vertex, when $s = t$).

Formalized by `Cslib.Algorithms.Lean.Hierholzer.exists_isEulerPath_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#exists-is-euler-path-iff).

## Euler circuit criterion for directed multigraphs

Let $G$ be a directed adjacency graph,
read as a multigraph with one edge per adjacency entry, and let $s$ be a vertex such that the
source of every edge of $G$ is reachable from $s$. Then $G$ has an Euler circuit from $s$ if and
only if $G$ is balanced, that is, every vertex is the source of exactly as many edge occurrences
as it is the target of.

## Sources

- CLRS, third edition, Problem 22-3; strong connectivity is weakened to reachability from $s$ of the source of every edge.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.exists_isEulerCircuit_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/Hierholzer.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#exists-is-euler-circuit-iff).

## Unordered edge of an ordered pair

The ordered pair $(a, b)$ of vertices, viewed as the
unordered pair $\{a, b\}$, so that $(a, b)$ and $(b, a)$ give the same unordered edge.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.usym`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#usym).

## Degree in an undirected edge list

For a finite list $R$ of edges of an undirected
multigraph, each given as a pair $(a, b)$, the degree of a vertex $x$ is the number of edges in
$R$ whose first component is $x$ plus the number whose second component is $x$; parallel edges
count separately and a loop $(x, x)$ counts twice.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.udeg`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#udeg).

## Degree parity condition for two endpoints

For a finite list $R$ of edges of an
undirected multigraph and vertices $v$, $t$, the condition holds when for every vertex $x$ the
number $\deg_R(x) + [x = v] + [x = t]$ is even, where $\deg_R$ is the degree in $R$ (a loop counts
twice) and $[P]$ is $1$ if $P$ holds and $0$ otherwise. Thus if $v \ne t$, exactly $v$ and $t$
have odd degree, and if $v = t$, every degree is even.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.EvenExcept`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#even-except).

## Reachability in an undirected multigraph

For a list $E$ of edges (ordered pairs of
vertices), a vertex $x$ is reachable from a vertex $s$ when there are vertices
$s = v_0, v_1, \dots, v_n = x$ with $n \ge 0$ such that for each $i < n$, $(v_i, v_{i+1})$ or
$(v_{i+1}, v_i)$ belongs to $E$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.UReach`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#ureach).

## Euler path in an undirected multigraph

For a finite list $E$ of edges of an undirected
multigraph and vertices $s$, $t$, a sequence of vertices $W = (w_0, \dots, w_n)$ is an Euler path
of $E$ from $s$ to $t$ when $w_0 = s$, $w_n = t$, and the multiset of unordered pairs
$\{w_{i-1}, w_i\}$ for $1 \le i \le n$ equals the multiset of the edges of $E$ taken as unordered
pairs. Thus every edge is traversed exactly once, in either direction.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.IsUEulerPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#is-ueuler-path).

## Other endpoint of an edge

For an edge $e = (a, b)$ and a vertex $v$, the other endpoint
of $e$ at $v$ is $b$ if $a = v$, and $a$ otherwise; in particular a loop $(v, v)$ gives $v$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.otherEnd`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#other-end).

## Undirected Hierholzer recursion

The recursion takes a fuel $f \in \mathbb{N}$, a vertex
$v$, a list $R$ of remaining edges and an accumulator list $A$ of vertices, and returns a list of
vertices and a list of remaining edges. With fuel $0$ it returns $A$ and $R$ unchanged. With fuel
$f + 1$: if no edge of $R$ has $v$ as an endpoint, it returns $v$ prepended to $A$, together with
$R$; otherwise, with $e$ the first such edge, it removes $e$ from $R$ at a cost of one unit,
recurses with fuel $f$ from the other endpoint of $e$ at $v$ on the shortened list with
accumulator $A$, obtaining a vertex list $A'$ and remaining edges $R'$, and then recurses with fuel
$f$ from $v$ on $R'$ with accumulator $A'$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uvisit`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uvisit).

## Undirected Hierholzer's algorithm

Given a list $E$ of undirected edges (ordered pairs of
vertices) and a start vertex $s$, run the undirected Hierholzer recursion from $s$ on $E$ with an
empty accumulator and fuel $|E| + 1$, and return the list of emitted vertices; its cost is the
cost of that recursion.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uhierholzer`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uhierholzer).

## Degree after removing an edge

Let $R$ be a finite list of edges of an undirected
multigraph, each an ordered pair of vertices, let $e = (a, b)$ be an edge in $R$, and let $x$ be a
vertex. Then the degree of $x$ in $R$ equals the degree of $x$ in the list obtained from $R$ by
removing the first occurrence of $e$, plus $[x = a] + [x = b]$, where $[P]$ is $1$ if $P$ holds
and $0$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.udeg_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#udeg-erase).

## An edge at a vertex joins it to its other endpoint

If an ordered pair $e = (a, b)$ of
vertices has $a = v$ or $b = v$, then the unordered pair $\{a, b\}$ equals $\{v, w\}$, where $w$
is the other endpoint of $e$ at $v$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.usym_eq_otherEnd`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#usym-eq-other-end).

## Invariant of the undirected Hierholzer recursion

Let $R$ be a list of edges, $v$, $t$
vertices such that exactly $v$ and $t$ have odd degree in $R$ (no vertex when $v = t$), $A$ a list
of vertices, and $f > |R|$ a fuel bound. Run the undirected Hierholzer recursion with fuel $f$
from $v$ on $R$ with accumulator $A$, and let $R'$ be the remaining edge list it returns and $c$
its cost. Then there is a vertex sequence $W$ starting at $v$ and ending at $t$ such that the
returned vertex list is $W$ followed by $A$; the edges of $R$, as unordered pairs, are a
permutation of the consecutive pairs of $W$ followed by the edges of $R'$, all as unordered pairs;
every vertex has even degree in $R'$; every vertex of $W$ has degree $0$ in $R'$; $R'$ is a
sublist of $R$; and $c + |R'| = |R|$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uvisit_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uvisit-spec).

## Undirected Hierholzer's algorithm returns a trail

Let $E$ be a list of undirected edges
and $s$, $t$ vertices such that exactly $s$ and $t$ have odd degree in $E$ (no vertex has odd
degree when $s = t$). Then the vertex sequence $W$ returned by the undirected Hierholzer algorithm
on $E$ from $s$ starts at $s$ and ends at $t$, and the consecutive pairs of $W$, as unordered
pairs, form a sub-multiset of the edges of $E$ as unordered pairs: no edge is traversed more often
than it occurs in $E$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uhierholzer_trail`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uhierholzer-trail).

## Undirected Hierholzer's algorithm finds Euler paths

Let $E$ be a list of undirected edges
(ordered pairs of vertices) and $s$, $t$ vertices such that exactly $s$ and $t$ have odd degree in
$E$ (no vertex has odd degree when $s = t$), and suppose the first endpoint of every edge of $E$ is
reachable from $s$ through edges of $E$. Then the vertex sequence returned by the undirected
Hierholzer algorithm on $E$ from $s$ is an Euler path of $E$ from $s$ to $t$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uhierholzer_isUEulerPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uhierholzer-is-ueuler-path).

## Undirected Hierholzer's algorithm finds Euler circuits

Let $E$ be a list of undirected
edges (ordered pairs of vertices) in which every vertex has even degree, and let $s$ be a vertex
such that the first endpoint of every edge of $E$ is reachable from $s$ through edges of $E$. Then
the vertex sequence returned by the undirected Hierholzer algorithm on $E$ from $s$ is an Euler
path of $E$ from $s$ to $s$, that is, an Euler circuit at $s$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uhierholzer_isUEulerCircuit`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uhierholzer-is-ueuler-circuit).

## Cost of the undirected Hierholzer algorithm

Let $E$ be a list of undirected edges and
$s$, $t$ vertices such that exactly $s$ and $t$ have odd degree in $E$ (no vertex has odd degree
when $s = t$), and suppose the first endpoint of every edge of $E$ is reachable from $s$ through
edges of $E$. Then the undirected Hierholzer algorithm on $E$ from $s$ costs exactly $|E|$, the
number of edges of $E$, in the cost model that charges one unit per removed edge.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.uhierholzer_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#uhierholzer-time).

## Multiplicity of a vertex in an unordered edge

For a vertex $x$, this assigns to an
unordered pair $\{a, b\}$ the number $[x = a] + [x = b]$ of its endpoints equal to $x$, where
$[P]$ is $1$ if $P$ holds and $0$ otherwise; in particular a loop $\{x, x\}$ gives $2$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.endsAt`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#ends-at).

## Degrees depend only on the unordered edges

Let $A$ and $B$ be finite lists of edges of an
undirected multigraph such that the multiset of edges of $A$, taken as unordered pairs, equals that
of $B$. Then every vertex has the same degree in $A$ as in $B$.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.udeg_eq_of_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#udeg-eq-of-perm).

## Degrees along a walk

Let $W = (w_0, \dots, w_n)$ be a nonempty sequence of vertices with
$w_0 = s$ and $w_n = t$, and consider the multigraph whose edges are the consecutive pairs
$(w_{i-1}, w_i)$ for $1 \le i \le n$. In it every vertex other than $s$ and $t$ has even degree
(a loop counts twice); if $s \ne t$, then $s$ and $t$ have odd degree, and if $s = t$, every
vertex has even degree.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.evenExcept_walkEdges`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#even-except-walk-edges).

## Degrees of an undirected Euler path

Let $E$ be a finite list of edges of an undirected
multigraph and let $W$ be an Euler path of $E$ from $s$ to $t$. Then every vertex other than $s$
and $t$ has even degree in $E$ (a loop counts twice); if $s \ne t$, then $s$ and $t$ have odd
degree, and if $s = t$, every vertex has even degree.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.evenExcept_of_isUEulerPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#even-except-of-is-ueuler-path).

## Euler's theorem for undirected multigraphs

Let $E$ be a finite list of edges of an
undirected multigraph (parallel edges and loops allowed), each given as a pair $(a, b)$, and let
$s$, $t$ be vertices such that the first endpoint $a$ of every edge is reachable from $s$ along
edges of $E$ traversed in either direction. Then $E$ has an Euler path from $s$ to $t$ if and only
if, when $s \ne t$, exactly $s$ and $t$ have odd degree, and, when $s = t$, every vertex has even
degree (a loop counts twice towards the degree).

This is the algorithmic form: the proof shows that Hierholzer's algorithm started at $s$ finds
such a path.

Formalized by `Cslib.Algorithms.Lean.Hierholzer.exists_isUEulerPath_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HierholzerUndirected.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html#exists-is-ueuler-path-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hierholzer's algorithm for Euler circuits](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/hierholzer-s-algorithm-for-euler-circuits)
