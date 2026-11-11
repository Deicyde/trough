---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Kruskal.RawEdge, Cslib.Algorithms.Lean.Kruskal.Graph, Cslib.Algorithms.Lean.Kruskal.WeightedEdge, Cslib.Algorithms.Lean.Kruskal.WeightedEdge.key, Cslib.Algorithms.Lean.Kruskal.KeyLE, Cslib.Algorithms.Lean.Kruskal.decodeAt, Cslib.Algorithms.Lean.Kruskal.validEdgesFrom, Cslib.Algorithms.Lean.Kruskal.validEdges
statement: formalized
proof: formalized
---

# Kruskal's algorithm

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html).

## Raw input edge

A raw edge is an undirected weighted input edge given by three natural
numbers: two endpoints, which are not yet checked to be vertices of the graph, and a weight.

Formalized by `Cslib.Algorithms.Lean.Kruskal.RawEdge`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#raw-edge).

## Kruskal input graph

For a natural number $n$, an input graph on the vertices
$\{0, \dots, n-1\}$ consists of a list of raw edges, kept in input order; the same pair of
endpoints may occur on several edges.

The endpoints of a raw edge are natural numbers and are not required to be below $n$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.Graph`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#graph).

## Weighted edge

A weighted edge on the vertices $\{0, \dots, n-1\}$ consists of an ordinal,
a natural number recording its zero-based position in the original input list, two endpoints in
$\{0, \dots, n-1\}$, and a natural-number weight.

Formalized by `Cslib.Algorithms.Lean.Kruskal.WeightedEdge`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#weighted-edge).

## Sorting key of a weighted edge

The sorting key of a weighted edge $e$ is the pair
$(w(e), i(e)) \in \mathbb{N} \times \mathbb{N}$ of its weight $w(e)$ and its input ordinal $i(e)$,
the zero-based position of $e$ in the original input edge list.

Keys are compared lexicographically.

Formalized by `Cslib.Algorithms.Lean.Kruskal.WeightedEdge.key`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#key).

## Lexicographic order on edge keys

For pairs of natural numbers $(w, i)$ and $(w', i')$,
$(w, i) \preceq (w', i')$ holds when $w < w'$, or $w = w'$ and $i \le i'$. This is the
non-strict lexicographic order on $\mathbb{N} \times \mathbb{N}$; Kruskal's algorithm applies it to
keys (weight, input ordinal).

Formalized by `Cslib.Algorithms.Lean.Kruskal.KeyLE`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#key-le).

## Decoding a raw edge at an ordinal

Given natural numbers $n$ and $i$ and a raw edge
with source $s$, target $t$ and weight $w$, decoding at ordinal $i$ returns the validated
edge on the vertices $\{0, \dots, n-1\}$ with ordinal $i$, source $s$, target $t$ and
weight $w$ when $s < n$ and $t < n$, and returns no edge otherwise.

Formalized by `Cslib.Algorithms.Lean.Kruskal.decodeAt`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#decode-at).

## Validating an edge list from a given ordinal

Given $n$, a starting ordinal $o$ and a
list of raw edges $e_0, e_1, \dots, e_{m-1}$, this returns, in input order, the weighted edges on
the vertices $\{0, \dots, n-1\}$ obtained from those $e_k$ whose two endpoints are both less than
$n$; each keeps the endpoints and weight of $e_k$ and carries the ordinal $o + k$. Edges with an
endpoint at least $n$ are omitted, but they still count towards the ordinals of later edges.

Formalized by `Cslib.Algorithms.Lean.Kruskal.validEdgesFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#valid-edges-from).

## Valid edges of an input graph

For a graph $G$ on the vertices $\{0, \dots, n-1\}$ given
by its list of raw edges $e_0, e_1, \dots, e_{m-1}$, the valid edges of $G$ are, in input order,
the weighted edges obtained from those $e_k$ whose two endpoints are both less than $n$; each
keeps the endpoints and weight of $e_k$ and carries its zero-based input ordinal $k$. Edges with an
endpoint at least $n$ are omitted.

Formalized by `Cslib.Algorithms.Lean.Kruskal.validEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#valid-edges).

## Sorting edges by weight and input position

Sorting a list of validated edges is merge
sort with the comparison $(w, i) \preceq (w', i')$ if $w < w'$, or $w = w'$ and $i \le i'$, applied
to the pairs (weight, input position) of the edges.

Formalized by `Cslib.Algorithms.Lean.Kruskal.sortEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#sort-edges).

## Valid edges in Kruskal order

For a finite weighted multigraph $G$ on the vertices
$\{0, \dots, n-1\}$, the ordered edges of $G$ are its valid input edges (those whose endpoints
are both less than $n$), sorted by merge sort in lexicographic order of (weight, input position):
by nondecreasing weight, with edges of equal weight in input order.

Formalized by `Cslib.Algorithms.Lean.Kruskal.orderedEdges`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#ordered-edges).

## Discrete parent forest

The initial forest on the vertices $\{0, \dots, n-1\}$ is
the parent forest in which every vertex is its own parent, so every vertex is a root, and
whose depth certificate is $0$ at every vertex.

Formalized by `Cslib.Algorithms.Lean.Kruskal.initialForest`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#initial-forest).

## Connectivity by a newest-first edge list

Connectivity of vertices $u$ and $v$ of
$\{0, \dots, n-1\}$ by a list of validated edges, read newest first, is defined by recursion
on the list. By the empty list, $u$ and $v$ are connected exactly when $u = v$. By a list
whose first edge $e$ has source $a$ and target $b$ and whose remaining edges form the list
$L$, the vertices $u$ and $v$ are connected when $u$ and $v$ are connected by $L$, or $u$ is
connected to $a$ and $v$ is connected to $b$ by $L$, or $u$ is connected to $b$ and $v$ is
connected to $a$ by $L$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.ConnectedRev`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#connected-rev).

## Connectivity by an edge list

Vertices $u$ and $v$ of $\{0, \dots, n-1\}$ are
connected by a list $e_1, \dots, e_k$ of validated edges when they are connected by the
reversed list $e_k, \dots, e_1$ in the sense of connectivity by a newest-first edge list.

Formalized by `Cslib.Algorithms.Lean.Kruskal.Connected`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#connected).

## Acyclicity of a newest-first edge list

A list $e_1, \dots, e_k$ of validated edges
on the vertices $\{0, \dots, n-1\}$, read newest first, is newest-first acyclic when, for
every $i$, the endpoints of $e_i$ are not connected by the later list $e_{i+1}, \dots, e_k$
in the sense of connectivity by a newest-first edge list.

Formalized by `Cslib.Algorithms.Lean.Kruskal.AcyclicRev`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#acyclic-rev).

## Acyclic edge list

A list $e_1, \dots, e_k$ of validated edges on the vertices
$\{0, \dots, n-1\}$ is acyclic when, for every $i$, the endpoints of $e_i$ are not connected
by the preceding edges $e_1, \dots, e_{i-1}$, in the sense of connectivity by an edge list.

Formalized by `Cslib.Algorithms.Lean.Kruskal.Acyclic`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#acyclic).

## Edge lists spanning a graph

A list $L$ of validated edges spans a finite weighted
multigraph $G$ on the vertices $\{0, \dots, n-1\}$ when, for every valid input edge of $G$ (one
whose endpoints are both less than $n$), the two endpoints of that edge are connected using the
edges of $L$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.Spans`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#spans).

## Spanning forest of an input graph

For an input graph $G$ on the vertices
$\{0, \dots, n-1\}$, a list $F$ of validated edges is a spanning forest of $G$ when every
edge of $F$ is a valid edge of $G$, $F$ is acyclic, and $F$ spans $G$: for every valid edge
of $G$, its endpoints are connected by $F$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.IsSpanningForest`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#is-spanning-forest).

## Ordered spanning forest

For an input graph $G$ on the vertices $\{0, \dots, n-1\}$,
a list $e_1, \dots, e_k$ of validated edges is an ordered spanning forest of $G$ when it is a
spanning forest of $G$ and its keys are nondecreasing: for all $i < j$, the key of $e_i$ is
at most the key of $e_j$, where the key of an edge with weight $w$ and input ordinal $o$ is
the pair $(w, o)$ and keys are compared lexicographically.

Formalized by `Cslib.Algorithms.Lean.Kruskal.IsOrderedSpanningForest`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#is-ordered-spanning-forest).

## Total weight of a Kruskal edge list

The total weight of a list of validated edges is the
sum of the weights of its entries, each entry counted once, so parallel edges and repeated
entries each contribute their weight.

Formalized by `Cslib.Algorithms.Lean.Kruskal.totalWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#total-weight).

## Kruskal scan state

A state of the Kruskal scan on the vertices $\{0, \dots, n-1\}$
consists of a union-find parent forest on these vertices, which records the current partition,
and the list of edges accepted so far, newest first.

Formalized by `Cslib.Algorithms.Lean.Kruskal.State`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#state).

## One Kruskal step

Let $s$ be a Kruskal scan state and $e$ a validated edge with endpoints
$u$ and $v$. If $u$ and $v$ are equivalent in the union-find forest of $s$, processing $e$ leaves
$s$ unchanged. Otherwise $e$ is accepted: the new forest is the union of $u$ and $v$ in the forest
of $s$, and $e$ is put at the front of the list of accepted edges.

Formalized by `Cslib.Algorithms.Lean.Kruskal.State.step`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#step).

## Scanning a list of edges

Starting from a Kruskal scan state $s$, scanning a list of
validated edges $e_1, \dots, e_k$ applies one Kruskal step to each edge in list order: the scan
of the empty list returns $s$, and the scan of $e_1, \dots, e_k$ is the scan of $e_2, \dots, e_k$
from the state obtained by processing $e_1$ in $s$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.scan`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#scan).

## Greedy cut property of Kruskal's scan

Let $G$ be an input graph on the vertices
$\{0, \dots, n-1\}$, give each valid edge with weight $w$ and input ordinal $o$ the key
$(w, o)$, and compare keys lexicographically. The graph $G$ has the greedy cut property when
the following holds for every way of splitting the valid edges of $G$, sorted by key, into an
initial segment, an edge $e$ and a final segment. Let $P$ be the union-find partition obtained
by scanning the initial segment from the discrete parent forest with no accepted edges. If the
endpoints of $e$ lie in different classes of $P$, then the key of $e$ is at most the key of
every valid edge of $G$ whose endpoints lie in different classes of $P$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.HasGreedyCutProperty`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#has-greedy-cut-property).

## Kruskal's algorithm

For a finite weighted multigraph $G$ on the vertices
$\{0, \dots, n-1\}$, Kruskal's algorithm starts from the partition of the vertices into
singletons and processes the valid input edges of $G$ (those whose endpoints are both less than
$n$) in lexicographic order of (weight, input position). An edge whose endpoints lie in different
classes of the current partition is accepted and its two classes are merged; an edge whose
endpoints lie in the same class is skipped. The result is the list of accepted edges in the order
in which they were processed.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal).

## Kruskal selects only valid input edges

For every graph $G$ on $n$ vertices, every edge
in the list returned by Kruskal's algorithm on $G$ is a valid edge of $G$: an input edge whose
two endpoints are both below $n$, carrying its input ordinal.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_edge_mem_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-edge-mem-valid).

## Kruskal's output is acyclic

For every graph $G$, the edge list returned by Kruskal's
algorithm on $G$ is acyclic: each edge in it joins two vertices that are not connected by the
edges before it in the list.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-acyclic).

## Kruskal's selected edges span the graph

For every finite weighted multigraph $G$ on the
vertices $\{0, \dots, n-1\}$, given by its list of input edges, and every valid input edge of $G$
(one whose endpoints are both less than $n$), the two endpoints of that edge are connected by the
edges that Kruskal's algorithm selects on $G$.

The graph $G$ need not be connected.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_spans`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-spans).

## Kruskal's output is sorted by key

For every graph $G$, if an edge $e$ comes before an
edge $f$ in the list returned by Kruskal's algorithm on $G$, then $e$ has smaller weight than
$f$, or the same weight as $f$ and input ordinal at most that of $f$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_pairwise_key_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-pairwise-key-le).

## Kruskal's greedy cut property

Let $G$ be a graph and let $e_1, \dots, e_m$ be its valid
edges sorted lexicographically by key (weight, then input ordinal). For a position $k$, let
$P_k$ be the partition of the vertices given by the union-find forest after Kruskal's scan,
started from the discrete forest, has processed $e_1, \dots, e_{k-1}$. If the endpoints of $e_k$
lie in different classes of $P_k$, then for every valid edge $c$ of $G$ whose endpoints lie in
different classes of $P_k$, the key of $e_k$ is lexicographically at most the key of $c$: either
$e_k$ has smaller weight than $c$, or the same weight and input ordinal at most that of $c$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_greedy_cut_property`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-greedy-cut-property).

## Kruskal accepts light edges

Let $G$ be a graph and let $e_1, \dots, e_m$ be its valid
edges sorted lexicographically by key (weight, then input ordinal). For a position $k$, let
$P_k$ be the partition of the vertices given by the union-find forest after Kruskal's scan,
started from the discrete forest, has processed $e_1, \dots, e_{k-1}$. If the endpoints of $e_k$
lie in different classes of $P_k$, then the weight of $e_k$ is at most the weight of every valid
edge of $G$ whose endpoints lie in different classes of $P_k$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_light_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-light-edge).

## Kruskal's output is a spanning forest

For every graph $G$, the edge list returned by
Kruskal's algorithm on $G$ is a spanning forest of $G$: every edge in it is a valid edge of $G$,
it is acyclic, and it connects the two endpoints of every valid edge of $G$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_isSpanningForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-is-spanning-forest).

## Kruskal's output is a sorted spanning forest

For every graph $G$, the edge list returned
by Kruskal's algorithm on $G$ is a spanning forest of $G$ (its edges are valid edges of $G$, it
is acyclic, and it connects the endpoints of every valid edge of $G$), and whenever an edge $e$
comes before an edge $f$ in it, the key (weight, input ordinal) of $e$ is lexicographically at
most that of $f$.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_isOrderedSpanningForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-is-ordered-spanning-forest).

## Kruskal's algorithm gives a minimum spanning forest

Let $G$ be a graph with
natural-number edge weights, and let $F$ be any spanning forest of $G$: a list of valid edges of
$G$ that is acyclic and connects the endpoints of every valid edge of $G$. Then the total weight
of the edge list returned by Kruskal's algorithm on $G$ is at most the total weight of $F$.

Total weights count parallel edge occurrences separately, and $G$ need not be connected.

## Sources

- CLRS, fourth edition, §21.2, cut-exchange argument.

Formalized by `Cslib.Algorithms.Lean.Kruskal.kruskal_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/Kruskal.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/Kruskal.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html#kruskal-minimal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kruskal's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/kruskal-s-algorithm)
