---
declaration: section
origin: cited
lean: SimpleGraph.Walk.IsEulerian.countP_edges_eq_degree, SimpleGraph.Connected.exists_isEulerian, SimpleGraph.Reachable.induce_support, SimpleGraph.ConnectedSupport.exists_isEulerian, SimpleGraph.EdgeIndexedMultigraph, SimpleGraph.EdgeIndexedMultigraph.IndexedWalk, SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.support, SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.edges
statement: formalized
proof: formalized
---

# Eulerian circuits

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html).

## Edges at a vertex of an Eulerian trail

Let $G$ be a finite simple graph and let $p$ be an
Eulerian trail in $G$, that is, a walk between any two vertices that uses every edge of $G$
exactly once. Then for every vertex $x$, the number of edges of $p$ that contain $x$, counted
with multiplicity along $p$, equals the degree of $x$ in $G$.

Formalized by `SimpleGraph.Walk.IsEulerian.countP_edges_eq_degree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#count-p-edges-eq-degree).

## Euler circuits in connected even graphs

Every finite connected simple graph in which every
vertex has even degree has a closed Eulerian trail, that is, a closed walk that uses every edge of
the graph exactly once.

Formalized by `SimpleGraph.Connected.exists_isEulerian`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#exists-is-eulerian).

## Reachability among non-isolated vertices

Let $G$ be a simple graph and let $u$ and $v$ be
non-isolated vertices of $G$, that is, vertices with at least one neighbour. If $v$ is reachable
from $u$ in $G$, then $v$ is reachable from $u$ in the subgraph of $G$ induced on the set of
non-isolated vertices.

Formalized by `SimpleGraph.Reachable.induce_support`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#induce-support).

## Euler circuits in simple graphs whose non-isolated vertices are connected

Let $G$ be a
finite simple graph in which every vertex has even degree, and suppose that the subgraph of $G$
induced on its non-isolated vertices is connected (in particular nonempty, so $G$ has at least
one edge). Then $G$ has a closed Eulerian trail, that is, a closed walk that uses every edge of
$G$ exactly once.

Isolated vertices are irrelevant to an Euler tour.

Formalized by `SimpleGraph.ConnectedSupport.exists_isEulerian`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EulerCircuit.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#exists-is-eulerian-2).

## Edge-indexed multigraph

An edge-indexed multigraph with vertex type $V$ and edge type
$E$ assigns to each edge $e \in E$ an unordered pair of endpoints in $V$, such that no edge has
two equal endpoints. Distinct edges may have the same endpoints, so parallel edges are
distinguished by their elements of $E$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#edge-indexed-multigraph).

## Indexed walk

In an edge-indexed multigraph, an indexed walk is a walk that records which
edge it traverses at each step. Indexed walks are defined inductively: for every vertex $v$ there
is the empty indexed walk from $v$ to $v$, and if $e$ is an edge with endpoints $u$ and $v$ and
$p$ is an indexed walk from $v$ to $w$, then traversing $e$ from $u$ to $v$ and then following
$p$ is an indexed walk from $u$ to $w$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#indexed-walk).

## Vertex list of an indexed walk

The support of an indexed walk $p$ from $u$ to $v$ in
an edge-indexed multigraph is the list of the vertices that $p$ visits, in order and with
repetitions, including both endpoints: the empty walk at $w$ has support $[w]$, and a walk that
starts at $u$ with an edge and continues with an indexed walk $q$ has support $u$ followed by
the support of $q$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.support`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#support).

## Edge list of an indexed walk

The edge list of an indexed walk is the list of the edge
identities it traverses, in order and with repetitions: the empty walk has the empty edge list,
and the walk that traverses an edge $e$ and then follows an indexed walk $p$ has edge list $e$
followed by the edge list of $p$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.edges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#edges).

## Indexed trail

An indexed walk $p$ in an edge-indexed multigraph is a trail when its edge
list has no repeated entries, that is, $p$ traverses each edge of the multigraph at most once.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.IsTrail`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#is-trail).

## Characterization of indexed trails

An indexed walk is a trail exactly when its edge
list has no duplicates.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.isTrail_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#is-trail-iff).

## Eulerian indexed walk

An indexed walk is Eulerian when it is a trail, that is, it uses
no edge identity twice, and every edge identity of the multigraph occurs in its edge list.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.IsEulerian`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#is-eulerian).

## Characterization of Eulerian indexed walks

An indexed walk is Eulerian exactly when it
is a trail whose edge list contains every edge identity of the multigraph.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.isEulerian_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#is-eulerian-iff).

## Support of the empty indexed walk

The support of the empty indexed walk at a vertex $v$
is the one-element list $[v]$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.support_nil`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#support-nil).

## Support of a walk extended at the front

If $e$ is an edge with endpoints $u$ and $v$ and
$p$ is an indexed walk starting at $v$, then the support of the walk that traverses $e$ from $u$
to $v$ and then follows $p$ is $u$ followed by the support of $p$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.support_cons`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#support-cons).

## The empty indexed walk has no edges

For every vertex $v$ of an edge-indexed multigraph,
the edge list of the empty indexed walk at $v$ is the empty list.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.edges_nil`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#edges-nil).

## Edge list of an extended indexed walk

Let $p$ be an indexed walk from $v$ to $w$ in an
edge-indexed multigraph $M$, and let $e$ be an edge of $M$ with endpoints $u$ and $v$. The edge
list of the walk from $u$ to $w$ that traverses $e$ and then follows $p$ is $e$ followed by the
edge list of $p$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.edges_cons`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#edges-cons).

## Incidence

In an edge-indexed multigraph, a vertex $v$ is incident with an edge $e$ when
$v$ belongs to the unordered pair of endpoints of $e$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.Inc`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#inc).

## Incidence is membership in the endpoint pair

In an edge-indexed multigraph, a vertex $v$
is incident with an edge $e$ if and only if $v$ belongs to the unordered pair of endpoints of
$e$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.inc_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#inc-iff).

## Underlying simple graph of an edge-indexed multigraph

The underlying simple graph of an
edge-indexed multigraph $M$ with vertex set $V$ is the simple graph on $V$ whose edges are the
unordered pairs $\{u, v\}$ that are the endpoint pair of some edge of $M$; such pairs have
$u \ne v$ because $M$ is loopless. It forgets edge multiplicities.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.underlying`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#underlying).

## Adjacency in the underlying graph

Let $M$ be an edge-indexed multigraph. Two vertices $u$
and $v$ are adjacent in the underlying simple graph of $M$ if and only if some edge $e$ of $M$ has
endpoint pair $\{u, v\}$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.underlying_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#underlying-adj).

## From an indexed walk to a walk in the underlying graph

Let $M$ be an edge-indexed
multigraph. An indexed walk $p$ in $M$ from $u$ to $v$ yields a walk from $u$ to $v$ in the
underlying simple graph of $M$ by forgetting edge identities: the empty indexed walk at $w$ goes
to the empty walk at $w$, and an indexed walk that first traverses an edge $e$ with endpoints
$\{u, x\}$ and then continues with an indexed walk $q$ goes to the walk that first steps from $u$
to $x$, an edge of the underlying graph because $e$ has these endpoints, and then follows the
image of $q$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.toWalk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#to-walk).

## Forgetting edge identities preserves the vertex sequence

Let $M$ be an edge-indexed
multigraph and $p$ an indexed walk in $M$ from $u$ to $v$. The walk from $u$ to $v$ in the
underlying simple graph of $M$ obtained from $p$ by forgetting edge identities visits the same
vertices as $p$, in the same order: the two supports are equal as lists.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.support_toWalk`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#support-to-walk).

## Edges of the forgetful walk

For every indexed walk $p$ from $u$ to $v$ in an
edge-indexed multigraph, the edge list of the walk in the underlying simple graph obtained from
$p$ by forgetting edge identities is the list of the endpoint pairs of the edges of $p$, taken in
the same order.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.edges_toWalk`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#edges-to-walk).

## Forgetting edge identities preserves length

For an indexed walk $p$, the walk in the
underlying simple graph obtained by forgetting edge identities has the same length as $p$, namely
the number of entries in the edge list of $p$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.IndexedWalk.length_toWalk`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#length-to-walk).

## Degree in an edge-indexed multigraph

The degree of a vertex $v$ in an edge-indexed
multigraph $M$ is the number of edges of $M$ incident with $v$, that is, the cardinality of the
set of edges whose endpoint pair contains $v$; it is defined to be $0$ when this set is
infinite.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.degree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#degree).

## Degree as the number of incident edges

For every vertex $v$ of an edge-indexed
multigraph $M$, the degree of $v$ equals the cardinality of the set of edges of $M$ whose
endpoint pair contains $v$, where this cardinality is taken to be $0$ when the set is infinite.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.degree_eq_ncard_inc`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#degree-eq-ncard-inc).

## Disjoint sum of edge-indexed multigraphs

Given edge-indexed multigraphs $M$ and $N$ on
the same vertex type $V$, with edge types $E$ and $F$, their disjoint sum is the edge-indexed
multigraph on $V$ whose edge type is the disjoint union $E \sqcup F$, where an edge coming from
$E$ has its endpoints in $M$ and an edge coming from $F$ has its endpoints in $N$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.disjointSum`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#disjoint-sum).

## Endpoints of edges from the first summand

Let $M$ and $N$ be edge-indexed multigraphs on
the same vertex type. Every edge $e$ of $M$, viewed as an edge of the disjoint sum of $M$ and
$N$, has the same endpoints as in $M$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.disjointSum_ends_inl`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#disjoint-sum-ends-inl).

## Endpoints of edges from the second summand

Let $M$ and $N$ be edge-indexed multigraphs
on the same vertex type. Every edge $f$ of $N$, viewed as an edge of the disjoint sum of $M$ and
$N$, has the same endpoints as in $N$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.disjointSum_ends_inr`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#disjoint-sum-ends-inr).

## Degrees add under disjoint sums

Let $M$ and $N$ be edge-indexed multigraphs on the same
vertex type, each with finitely many edges. Then for every vertex $v$, the degree of $v$ in the
disjoint sum of $M$ and $N$ equals the degree of $v$ in $M$ plus the degree of $v$ in $N$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.disjointSum_degree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#disjoint-sum-degree).

## Adding edges preserves connectedness

Let $M$ and $N$ be edge-indexed multigraphs on the
same vertex type. If the underlying simple graph of $M$ is connected, then the underlying simple
graph of the disjoint sum of $M$ and $N$ is connected.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.disjointSum_connected_left`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#disjoint-sum-connected-left).

## Handshake lemma for edge-indexed multigraphs

In an edge-indexed multigraph with finitely
many vertices and finitely many edges, the sum of the degrees of all vertices is even.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.even_sum_degree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#even-sum-degree).

## Euler circuits in edge-indexed multigraphs

Let $M$ be an edge-indexed multigraph with
finitely many vertices and finitely many edges. If the underlying simple graph of $M$ is
connected and every vertex of $M$ has even degree, then there are a vertex $u$ and a closed
indexed walk from $u$ to $u$ that is Eulerian, that is, it traverses every edge of $M$ exactly
once.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.exists_indexedEulerian`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#exists-indexed-eulerian).

## Euler circuits in edge-indexed multigraphs whose non-isolated vertices are connected

Let
$M$ be an edge-indexed multigraph with finitely many vertices and finitely many edges. Suppose
that the subgraph of the underlying simple graph of $M$ induced on its non-isolated vertices is
connected, and that every vertex of $M$ has even degree. Then there are a vertex $u$ and a closed
indexed walk from $u$ to $u$ that is Eulerian, that is, it traverses every edge of $M$ exactly
once.

A connected graph has at least one vertex, so the hypothesis requires $M$ to have an edge.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.exists_indexedEulerian_connectedSupport`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#exists-indexed-eulerian-connected-suppor).

## Line graph of an edge-indexed multigraph

The line graph of an edge-indexed multigraph is
the simple graph whose vertices are the edge identities, two of them being adjacent when they are
distinct and share an endpoint. In particular, parallel edges are adjacent.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.lineGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#line-graph).

## Adjacency in the line graph of a multigraph

Two edge identities $e_1$ and $e_2$ are
adjacent in the line graph of an edge-indexed multigraph exactly when $e_1 \ne e_2$ and some
vertex is incident with both of them.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.lineGraph_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#line-graph-adj).

## Maximum degree of a multigraph

For an edge-indexed multigraph with finitely many vertices
and finitely many edge identities, the maximum degree is the largest degree of a vertex, and $0$
when there are no vertices.

Finiteness of the edge identities matters: the degree of a vertex is the cardinality of its set
of incident edges, which is taken to be $0$ for an infinite set, so without it a vertex of
infinite degree could be reported as having degree $0$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.maxDegree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#max-degree).

## Degrees are bounded by the maximum degree

Let $M$ be an edge-indexed multigraph with
finitely many vertices and finitely many edges. Then every vertex of $M$ has degree at most the
maximum degree of $M$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.degree_le_maxDegree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 735](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#degree-le-max-degree).

## Degree counts incident edges

In an edge-indexed multigraph with finitely many edges, the
degree of every vertex $v$ equals the number of edges incident with $v$.

Formalized by `SimpleGraph.EdgeIndexedMultigraph.filter_inc_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeIndexedMultigraph.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html#filter-inc-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eulerian circuits](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/eulerian-circuits)
