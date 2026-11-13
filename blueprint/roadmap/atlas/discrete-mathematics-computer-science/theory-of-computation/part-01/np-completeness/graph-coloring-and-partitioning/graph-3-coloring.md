---
declaration: section
origin: cited
lean: Cslib.Complexity.Karp.encodeE, Cslib.Complexity.Karp.edgeGraph, Cslib.Complexity.Karp.col3Dec, Cslib.Complexity.Karp.ColSt, Cslib.Complexity.Karp.consEdges, Cslib.Complexity.Karp.colOcc, Cslib.Complexity.Karp.colOr, Cslib.Complexity.Karp.colLits
statement: formalized
proof: formalized
---

# Graph 3-coloring

165 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/index.html).

## Bit-string encoding of a graph

The graph encoding of a number $n$ and a list $E$ of pairs
of natural numbers is the bit string that writes $n$ in unary and then, for each pair $(u, v)$
of $E$ in order, writes $u$ and then $v$ in unary, where a natural number $k$ is written in
unary as $k$ ones followed by one zero.

Formalized by `Cslib.Complexity.Karp.encodeE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#encode-e).

## Graph of an edge list

For a natural number $n$ and a list $es$ of pairs of natural
numbers, the graph of $es$ on $n$ vertices is the simple graph on $\{0, \dots, n-1\}$ in which
distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $es$. Loops are
dropped, and pairs with an endpoint at least $n$ contribute no edge.

Formalized by `Cslib.Complexity.Karp.edgeGraph`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#edge-graph).

## 3-COLOR

The decision problem 3-COLOR accepts a bit string $x$ exactly when there are a
natural number $n$ and a list $es$ of pairs of natural numbers such that $x$ is the encoding of
$n$ and $es$ ($n$ in unary, then each edge $(u, v)$ as $u$ and $v$ in unary), every edge
$(u, v)$ in $es$ has $u < n$ and $v < n$, and the graph on $\{0, \dots, n - 1\}$ with edge list
$es$ (symmetrized, loops dropped) is $3$-colorable.

Formalized by `Cslib.Complexity.Karp.col3Dec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col3-dec).

## State of the SAT-to-3-COLOR construction

A state of the graph construction reducing CNF
satisfiability to 3-colorability consists of a natural number, the next free vertex; a list of
quadruples $(x, b, L, M)$ of a variable index $x$, a polarity $b$, the vertex $L$ of the literal
and the vertex $M$ of its negation, recording the earlier literal occurrences with the latest
first; and a list of pairs of natural numbers, the edges emitted so far, in emission order.

Formalized by `Cslib.Complexity.Karp.ColSt`, a structure declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-st).

## Consistency edges between two occurrences of a variable

Let $l = (x, b)$ be a literal
with variable index $x$ and polarity $b$, let $L$, $M$ be the vertices of a new occurrence of
$l$, and let $(x', b', L', M')$ be an earlier occurrence. If $x' \ne x$ the list of consistency
edges is empty. If $x' = x$ and $b' = b$ it is $[(L', M), (M', L)]$; if $x' = x$ and $b' \ne b$
it is $[(L', L), (M', M)]$.

Formalized by `Cslib.Complexity.Karp.consEdges`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#cons-edges).

## Adding a literal occurrence in the 3-COLOR construction

Given a literal $l = (x, b)$
with variable index $x$ and polarity $b$, and a state whose next free vertex is $n$, let $L = n$
and $M = n + 1$. The new state has next free vertex $n + 2$, records the occurrence
$(x, b, L, M)$ at the front of the list of earlier occurrences, and appends to the emitted edges
first $(L, M)$, $(L, 2)$, $(M, 2)$ (a triangle with the palette vertex $2$), then the
consistency edges of the new occurrence $(L, M)$ of $l$ with each earlier occurrence, taken
latest first. The result is this new state together with the vertex $L$.

Formalized by `Cslib.Complexity.Karp.colOcc`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-occ).

## OR gadget of the 3-COLOR construction

Given vertices $a$ and $o$ and a state whose next
free vertex is $n$, let $u = n$, $v = n + 1$ and $w = n + 2$. The new state has next free vertex
$n + 3$, the same earlier occurrences, and the emitted edges followed by $(a, u)$, $(o, v)$,
$(u, v)$, $(u, w)$, $(v, w)$, $(w, 2)$. The result is this new state together with the output
vertex $w$.

Formalized by `Cslib.Complexity.Karp.colOr`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-or).

## Processing the remaining literals of a clause

Given a list of literals, a vertex $o$
(the output so far) and a state, the result is defined by recursion on the list. For the empty
list, the emitted edges of the state are followed by $(o, 1)$ and $(o, 2)$, joining $o$ to the
palette vertices $1$ and $2$, and the other components are unchanged. For a list with head $l$
and tail $ls$, first add an occurrence of $l$, obtaining a state and the literal vertex $L$;
then add an OR gadget with inputs $L$ and $o$, obtaining a state and its output vertex $w$;
then process $ls$ with output $w$ from that state.

Formalized by `Cslib.Complexity.Karp.colLits`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-lits).

## Processing one clause in the 3-COLOR construction

Given a clause $C$ and a state
whose next free vertex is $n$, the literals of $C$ are read from the last one. If $C$ is empty,
the new state has next free vertex $n + 1$, the same earlier occurrences, and the emitted edges
followed by $(n, 0)$, $(n, 1)$, $(n, 2)$, joining the fresh vertex $n$ to the palette vertices
$0$, $1$, $2$. Otherwise let $l$ be the last literal of $C$ and $ls$ the other literals in
reverse order: add an occurrence of $l$, obtaining a state and the literal vertex $L$, then
process the remaining literals $ls$ with output $L$ from that state.

Formalized by `Cslib.Complexity.Karp.colClause`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-clause).

## The SAT-to-3-COLOR graph construction

For a CNF formula $\varphi$, start from the state
whose next free vertex is $3$, with no earlier occurrences and with emitted edges $(0, 1)$,
$(0, 2)$, $(1, 2)$ (the palette triangle on the vertices $0$, $1$, $2$), and process the
clauses of $\varphi$ one at a time, from the last clause to the first. The result is the final
state.

Formalized by `Cslib.Complexity.Karp.colSt`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#col-st-2).

## The 3-COLOR instance of a CNF formula

Run the gadget construction on a CNF formula
$\varphi$; it ends with a next free vertex $N$ and a list of emitted edges. The 3-COLOR instance
of $\varphi$ is the graph encoding of the number $N$ and the emitted edges in reverse order.

Formalized by `Cslib.Complexity.Karp.toCol`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#to-col).

## The complete graph on four vertices as a bit string

This is the graph encoding of the
number $4$ and the edge list $(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)$, in that order,
that is, of the complete graph on the vertices $0, 1, 2, 3$.

This graph is not 3-colorable; the reduction from SAT to 3-COLOR sends undecodable input to it.

Formalized by `Cslib.Complexity.Karp.noCol`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#no-col).

## The SAT to 3-COLOR reduction map on bit strings

The map sends a bit string $x$ that
decodes to a CNF formula $\varphi$ to the 3-COLOR instance of $\varphi$, and sends every bit
string that does not decode to a CNF formula to the graph encoding of the number $4$ and the
edge list $(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)$, in that order, that is, of the
complete graph on four vertices.

Formalized by `Cslib.Complexity.Karp.reduceCol`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#reduce-col).

## Reading a unary number shortens the input

If reading a unary length prefix from a bit
string $x$ succeeds with value $u$ and unconsumed suffix $r$, then $r$ is strictly shorter
than $x$.

Formalized by `Cslib.Complexity.Karp.length_lt_of_readUnaryLength`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#length-lt-of-read-unary-length).

## Edge-list decoder

The edge-list decoder reads a bit string as a list of pairs of natural
numbers, each number written in unary as that many $1$s followed by a $0$. On the empty string
it returns the empty list. Otherwise it reads a number $u$, then a number $v$, decodes the rest
recursively, and returns $(u, v)$ followed by the result; it fails if the input ends inside a
number or after an unpaired number, or if decoding the rest fails.

In a graph encoding it parses what follows the vertex count.

Formalized by `Cslib.Complexity.Karp.decodeEs`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#decode-es).

## Decoding a graph

To decode a bit string $x$, read a unary number $n$ from the front of
$x$ ($n$ copies of true ended by false); if there is none, decoding fails. Otherwise decode the
rest of $x$ as an edge list $es$ (pairs of unary numbers until the input ends); if that fails,
decoding fails, and otherwise the result is the pair $(n, es)$.

Formalized by `Cslib.Complexity.Karp.decodeE`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#decode-e).

## Bit encoding of an edge list

The edge bits of a list of pairs of natural numbers are the
concatenation, over its pairs $(u, v)$ in order, of $u$ ones, a zero, $v$ ones and a zero.

Formalized by `Cslib.Complexity.Karp.edgeBits`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#edge-bits).

## Decoding the empty input

The edge-list decoder, applied to the empty bit string,
succeeds and returns the empty edge list.

Formalized by `Cslib.Complexity.Karp.decodeEs_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#decode-es-nil).

## The edge-list decoder fails on a cut-off first number

If $x$ is a nonempty bit string
and reading a unary length prefix from $x$ fails, then the edge-list decoder fails on $x$.

Formalized by `Cslib.Complexity.Karp.decodeEs_of_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#decode-es-of-none).

## Decoding fails on a dangling half-pair

If reading a unary length prefix from a bit string
$x$ returns a number $u$ and the remaining suffix $r$, and reading a unary length prefix from $r$
fails, then the edge-list decoder fails on $x$.

Formalized by `Cslib.Complexity.Karp.decodeEs_of_some_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-01/index.html#decode-es-of-some-none).

## Decoding one pair, then the rest

If reading a unary length prefix from a bit string $x$
returns $u$ with remaining suffix $r$, and reading one from $r$ returns $v$ with remaining suffix
$r'$, then the edge-list decoder succeeds on $x$ exactly when it succeeds on $r'$, and in that
case its result on $x$ is its result on $r'$ with the pair $(u, v)$ put in front.

Formalized by `Cslib.Complexity.Karp.decodeEs_of_some_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#decode-es-of-some-some).

## Decoding the bits of an edge list

For every list $es$ of pairs of natural numbers, the
edge-list decoder applied to the edge bits of $es$ succeeds and returns $es$.

Formalized by `Cslib.Complexity.Karp.decodeEs_edgeBits`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#decode-es-edge-bits).

## The edge-list decoder succeeds only on edge bits

For every bit string $x$ and every list
$es$ of pairs of natural numbers, if the edge-list decoder returns $es$ on $x$, then $x$ is the
edge bits of $es$.

Formalized by `Cslib.Complexity.Karp.edgeBits_of_decodeEs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#edge-bits-of-decode-es).

## Graph encoding as vertex count plus edge bits

For every natural number $n$ and every list
$es$ of pairs of natural numbers, the graph encoding of $n$ and $es$ is $n$ ones, then a zero,
then the edge bits of $es$.

Formalized by `Cslib.Complexity.Karp.encodeE_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#encode-e-eq).

## Graph decoding inverts graph encoding

For every natural number $n$ and every list $es$
of pairs of natural numbers, decoding the graph encoding of $n$ and $es$ succeeds and returns
$(n, es)$.

Formalized by `Cslib.Complexity.Karp.decodeE_encodeE`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#decode-e-encode-e).

## Graph decoding succeeds only on encodings

Let $x$ be a bit string. If decoding $x$ as a
graph yields a number $n$ and a list $E$ of pairs of natural numbers, then $x$ is the graph
encoding of $n$ and $E$.

Formalized by `Cslib.Complexity.Karp.encodeE_of_decodeE`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Color.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Color.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#encode-e-of-decode-e).

## The complete graph on four vertices is not 3-colorable

The graph on the vertices
$0, 1, 2, 3$ with an edge between every two distinct vertices has no proper coloring with
$3$ colors.

Formalized by `Cslib.Complexity.Karp.not_colorable_noCol`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#not-colorable-no-col).

## Proper 3-colorings of an edge list

A map $c : \mathbb{N} \to \{0, 1, 2\}$ properly colors
a list $E$ of pairs of natural numbers when $c(a) \ne c(b)$ for every pair $(a, b)$ in $E$.

Formalized by `Cslib.Complexity.Karp.ColProper`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-proper).

## 3-colorability through colorings of the natural numbers

Let $n$ be a natural number and
$E$ a list of pairs $(a, b)$ of natural numbers with $a < n$, $b < n$ and $a \ne b$. The graph on
$\{0, \dots, n - 1\}$ with edge list $E$ is 3-colorable if and only if some map
$c : \mathbb{N} \to \{0, 1, 2\}$ satisfies $c(a) \ne c(b)$ for every pair $(a, b)$ in $E$.

Formalized by `Cslib.Complexity.Karp.colorable_iff_exists_colProper`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#colorable-iff-exists-col-proper).

## Coloring an OR gadget

Read the colors $0, 1, 2$ as $T$, $F$ and $B$. For all
colors $c_a, c_o \in \{0, 1, 2\}$ with $c_a \ne 2$ and $c_o \ne 2$, there are colors
$c_u, c_v, c_w \in \{0, 1, 2\}$ with $c_a \ne c_u$, $c_o \ne c_v$, $c_u \ne c_v$,
$c_u \ne c_w$, $c_v \ne c_w$ and $c_w \ne 2$, such that $c_w = 0$ if and only if
$c_a = 0$ or $c_o = 0$.

These are the conditions for a proper coloring of an OR gadget with inputs $a, o$, fresh
vertices $u, v, w$ and edges $au$, $ov$, $uv$, $uw$, $vw$, $wB$, where $B$ has color $2$:
if both inputs are colored $T$ or $F$, the gadget can be colored so that its output $w$ is
$T$ or $F$, and $T$ exactly when some input is $T$.

Formalized by `Cslib.Complexity.Karp.or_gadget_colors`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#or-gadget-colors).

## Soundness of the OR gadget

Read the colors $0, 1, 2$ as $T$, $F$ and $B$. If
colors $c_a, c_o, c_u, c_v, c_w \in \{0, 1, 2\}$ satisfy $c_a \ne 2$, $c_o \ne 2$,
$c_a \ne c_u$, $c_o \ne c_v$, $c_u \ne c_v$, $c_u \ne c_w$, $c_v \ne c_w$ and $c_w = 0$,
then $c_a = 0$ or $c_o = 0$.

That is, in a proper coloring of an OR gadget with inputs $a, o$, fresh vertices $u, v, w$
and edges $au$, $ov$, $uv$, $uw$, $vw$, if both inputs are colored $T$ or $F$ and the
output $w$ is $T$, then some input is $T$.

Formalized by `Cslib.Complexity.Karp.or_gadget_sound`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#or-gadget-sound).

## Adding a literal occurrence takes two new vertices

For a literal $l$ and a state $s$ of
the SAT-to-3-COLOR construction whose next free vertex is $n$, the state obtained by adding the
occurrence $l$ to $s$ has next free vertex $n + 2$.

Formalized by `Cslib.Complexity.Karp.colOcc_next`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-occ-next).

## Growth of construction states

A construction state $s'$ extends a construction state $s$
when the next free vertex of $s'$ is at least that of $s$, every edge emitted in $s$ is emitted in
$s'$, and every occurrence recorded in $s$ is recorded in $s'$.

Formalized by `Cslib.Complexity.Karp.ColGrows`, a structure declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-grows).

## Extending a state makes it grow

Let $s$ be a construction state with next free vertex
$m$, let $n \ge m$, and let $E$ be a list of pairs of natural numbers. Then the state with next
free vertex $n$, the same recorded occurrences as $s$, and emitted edges those of $s$ followed by
$E$ extends $s$: its next free vertex is at least that of $s$, and its emitted edges and recorded
occurrences include those of $s$.

Formalized by `Cslib.Complexity.Karp.colGrows_extend`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-grows-extend).

## Well-formed construction states

A construction state $s$ with next free vertex $n$ is
well formed when $3 \le n$; every emitted edge $(a, b)$ has $a < n$, $b < n$ and $a \ne b$; the
literal vertex and the negation vertex of every recorded occurrence are smaller than $n$; the
pairs $(0, 1)$, $(0, 2)$ and $(1, 2)$ are emitted edges (the palette triangle); for every
recorded occurrence with literal vertex $L$ and negation vertex $M$, the pairs $(L, M)$, $(L, 2)$
and $(M, 2)$ are emitted edges; and whenever an occurrence with variable $x$, polarity $b$,
literal vertex $L$ and negation vertex $M$ comes before an occurrence with the same variable $x$,
polarity $b'$, literal vertex $L'$ and negation vertex $M'$ in the list of recorded occurrences
(which lists the latest first), the pairs $(L', M)$ and $(M', L)$ are emitted edges if $b' = b$,
and the pairs $(L', L)$ and $(M', M)$ are emitted edges if $b' \ne b$.

Formalized by `Cslib.Complexity.Karp.ColGood`, a structure declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-good).

## Extending a well-formed state keeps it well formed

Let $s$ be a well-formed
construction state with next free vertex $m$, let $n \ge m$, and let $E$ be a list of pairs
$(a, b)$ of natural numbers with $a < n$, $b < n$ and $a \ne b$. Then the state with next free
vertex $n$, the same recorded occurrences as $s$, and emitted edges those of $s$ followed by $E$
is well formed.

Formalized by `Cslib.Complexity.Karp.ColGood.extend`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#extend).

## The construction's edges lie below its vertex count

For every CNF formula $\varphi$,
both endpoints of every edge emitted by the construction for $\varphi$ are smaller than the
number of vertices the construction allocates (its next free vertex).

Formalized by `Cslib.Complexity.Karp.colSt_em_lt`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-st-em-lt).

## Colorings that follow an assignment

Let $s$ be a construction state, let
$v : \mathbb{N} \to \mathrm{Bool}$ be an assignment, and let $c : \mathbb{N} \to \{0, 1, 2\}$ be a
coloring. Then $c$ colors $s$ according to $v$ when $c(0) = 0$, $c(1) = 1$ and $c(2) = 2$ (the
palette vertices $T$, $F$, $B$), $c(a) \ne c(b)$ for every edge $(a, b)$ emitted in $s$, and for
every occurrence recorded in $s$ with variable $x$, polarity $b$, literal vertex $L$ and negation
vertex $M$: if $v(x) = b$ then $c(L) = 0$ and $c(M) = 1$, and otherwise $c(L) = 1$ and
$c(M) = 0$.

Formalized by `Cslib.Complexity.Karp.ColColored`, a structure declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#col-colored).

## Output of the OR gadget under a proper 3-coloring

Let $c : \mathbb{N} \to \{0, 1, 2\}$
with $c(2) = 2$, let $a$ and $o$ be natural numbers, let $s$ be a state of the SAT-to-3-COLOR
construction and let $E$ be a list of pairs of natural numbers such that $c(u) \ne c(v)$ for
every pair $(u, v)$ in $E$. Apply the OR gadget to $a$, $o$ and $s$, giving a new state and an
output vertex $w$, and suppose every edge in the emitted-edge list of the new state belongs to
$E$. If $c(a) \ne 2$ and $c(o) \ne 2$, then $c(w) \ne 2$, and if $c(w) = 0$ then $c(a) = 0$ or
$c(o) = 0$.

Formalized by `Cslib.Complexity.Karp.sound_colOr`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#sound-col-or).

## Correctness of the reduction from SAT to 3-coloring

A CNF formula $\varphi$ is satisfiable
if and only if the graph built from $\varphi$ by the Garey–Johnson–Stockmeyer construction is
3-colorable. Here, writing $n$ for the number of vertices the construction allocates, the graph
has vertex set $\{0, \dots, n - 1\}$, and two distinct vertices are adjacent when the
construction emits an edge between them in either order.

Formalized by `Cslib.Complexity.Karp.cnfSat_iff_colorable`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-02/index.html#cnf-sat-iff-colorable).

## Correctness of the SAT to 3-COLOR map on bit strings

For every bit string $x$, SAT
accepts $x$ if and only if 3-COLOR accepts the image of $x$ under the SAT to 3-COLOR reduction
map on bit strings.

Formalized by `Cslib.Complexity.Karp.satDec_eq_col3Dec_reduceCol`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorCorrect.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#sat-dec-eq-col3-dec-reduce-col).

## Bit encoding of an edge

The bits of an edge $(u, v)$ in the edge-list encoding of a
graph: $u$ copies of true, then false, then $v$ copies of true, then false.

Formalized by `Cslib.Complexity.Karp.EmitColor.eB`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#e-b).

## Bits pushed for a list of edges

For a list of edges $e_1, \dots, e_k$ (pairs of
natural numbers), the output is the concatenation $b(e_k) \cdots b(e_1)$, where $b(u, v)$ is
$u$ ones, a zero, $v$ ones and a zero.

This is what the output stack gains, read top-first, when the edges are pushed in the order
$e_1, \dots, e_k$.

Formalized by `Cslib.Complexity.Karp.EmitColor.out`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#out).

## Stacks of the 3-coloring emitter

The emitter has thirteen stacks: $T$ (tokens), $O$
(output), $N$ (the next free vertex), $R$ (the current OR output), $D$ (earlier occurrences),
$E$ (the walk's other side), $A$ (the current name), $P$ (its polarity), $F$ (the first-literal
flag), $U$ (an earlier literal vertex), and the scratch stacks $X$ and $B$ for comparisons and
$W$ for copies.

Formalized by `Cslib.Complexity.Karp.EmitColor.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#k).

## Stack alphabets of the 3-coloring emitter

The output stack has the booleans (bits) as
its alphabet; every other stack has the token symbols as its alphabet.

The counter stacks hold only the clause-end symbol, used as a unary unit.

Formalized by `Cslib.Complexity.Karp.EmitColor.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#untitled).

## Counters read by copy sites of the 3-COLOR emitter

The type with the three elements
$n, r, u$, naming the counters of the 3-coloring emitter that a copy site can read: the next free
vertex $n$, the current OR output $r$ and an earlier literal vertex $u$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Src`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#src).

## Stack of a counter

The counter $n$ (the next vertex) is held on stack $N$, the counter
$r$ (the OR output) on stack $R$, and the counter $u$ (an earlier literal vertex) on stack $U$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Src.k`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#k-2).

## Unit symbol of a counter

For each of the three counters read by copy sites of the
3-coloring emitter, the unit symbol in the alphabet of the counter's stack is the clause-end
token symbol.

Formalized by `Cslib.Complexity.Karp.EmitColor.Src.unit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#unit).

## Copy sites of the 3-COLOR emitter

The type of copy sites has 29 distinct elements:
$o_1, \dots, o_4$ for the occurrence triangle; $c_1, \dots, c_4$ and $d_1, \dots, d_4$ for the
consistency edges with an earlier occurrence of equal and of opposite polarity;
$r_1, \dots, r_{11}$ for the OR gadget; $e_1, e_2$ for the clause end; $z_1, z_2, z_3$ for the
empty clause; and one site for the vertex count. Equality of sites is decidable.

Formalized by `Cslib.Complexity.Karp.EmitColor.Site`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#site).

## The copy sites of the 3-COLOR emitter, listed

The list of all copy sites of the 3-COLOR
emitter, each exactly once, in the order $o_1, \dots, o_4$, $c_1, \dots, c_4$, $d_1, \dots, d_4$,
$r_1, \dots, r_{11}$, $e_1, e_2$, $z_1, z_2, z_3$ and the vertex-count site.

Formalized by `Cslib.Complexity.Karp.EmitColor.Site.all`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#all).

## Counter copied by a copy site

In the 3-coloring emitter, the sites $c_2$, $c_4$,
$d_2$ and $d_4$ copy the earlier-literal counter $U$, the sites $r_4$, $e_1$ and $e_2$ copy the
OR-output counter $R$, and every other site copies the next-vertex counter $N$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Site.src`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#src-2).

## Constant block of a copy site

The list of bits a copy site of the 3-coloring emitter
pushes onto the output stack below its counter copy, read top-first and written with $1$ for
true and $0$ for false: $o_1$: 10, $o_2$: 0, $o_3$: 0110, $o_4$: 10110; $c_1$: 10, $c_2$: 0,
$c_3$: 0, $c_4$: 10; $d_1$: 0, $d_2$: 0, $d_3$: 10, $d_4$: 10; $r_1$: 110, $r_2$: 0,
$r_3$: 1110, $r_4$: 0, $r_5$: 1110, $r_6$: 110, $r_7$: 11110, $r_8$: 110, $r_9$: 11110,
$r_{10}$: 1110, $r_{11}$: 11110110; $e_1$: 010, $e_2$: 0110; $z_1$: 00, $z_2$: 010,
$z_3$: 0110; and the vertex-count site: 0.

Formalized by `Cslib.Complexity.Karp.EmitColor.Site.top`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#top).

## Control labels of the 3-coloring emitter

`init`: palette; `cls`: next clause; `lits`:
next literal; `lp`, `nm`: pop the polarity and the name; `walk` to `dr`: walk `D` (compare,
restore, select the polarity case, move the name and the vertex to `E`, or the vertex to `U`
and push the consistency edges); `back`: move `E` back to `D`; `putN` to `putP`: put the
occurrence on `D`; `aft`, `fA` to `fC`: set `R` and advance `N`; `clr`: clear `R`; `zN`:
advance `N` after an empty clause; `pre j`, `cpA j`, `cpB j`: copy site `j`; `done`: halt.

Formalized by `Cslib.Complexity.Karp.EmitColor.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#lab).

## Successor label of a copy site

The label at which the 3-COLOR emitter continues
after a copy site. In each of the chains $o_1, \dots, o_4$; $c_1, \dots, c_4$; $d_1, \dots, d_4$;
$r_1, \dots, r_{11}$; $e_1, e_2$; $z_1, z_2, z_3$, every site but the last continues with
$\mathtt{pre}$ of the next site of its chain. The last sites continue as follows: $o_4$ with
$\mathtt{lp}$, $c_4$ and $d_4$ with $\mathtt{dr}$, $r_{11}$ with $\mathtt{clr}(\mathrm{true})$,
$e_2$ with $\mathtt{clr}(\mathrm{false})$, $z_3$ with $\mathtt{zN}$, and the site
$\mathrm{fin}$ with $\mathtt{done}$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Site.nxt`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#nxt).

## Literal-marker test

For an optional symbol (the top of a stack, absent when the stack is
empty), the test is true exactly when the symbol is present and is a literal marker of some
polarity; it is false for every other symbol and for an empty stack.

Formalized by `Cslib.Complexity.Karp.EmitColor.isLit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#is-lit).

## Reading unary units

The partial reading of token symbols as unary units used by the
3-coloring emitter: the clause-end symbol is read as the bit true, and every other symbol has
no reading, so it ends a run of units.

Formalized by `Cslib.Complexity.Karp.EmitColor.unitOf`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#unit-of).

## Bits of the palette triangle

The bits pushed for the edges $(0, 1)$, $(0, 2)$,
$(1, 2)$ in this order, that is, for the triangle on the palette vertices $0$, $1$, $2$.

Formalized by `Cslib.Complexity.Karp.EmitColor.pal`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#pal).

## The 3-COLOR emitter machine

The TM2 program, with the stacks, stack alphabets and
labels of the emitter and a Boolean local state, that builds the 3-COLOR instance of a CNF
formula from its token stack. It first pushes the palette triangle on the output stack and
adds $3$ to the next free vertex $N$. It then reads the clauses one at a time. For each
literal occurrence it pushes the occurrence triangle, walks the earlier occurrences comparing
variable names, and for each one with the same variable pushes the consistency edges for
equal or opposite polarity; it then records the occurrence. After the first literal of a
clause it adds $N$ to the current OR output $R$ and adds $2$ to $N$; after a later literal it
pushes an OR gadget with inputs $N$ and $R$, sets $R$ to $N + 4$ and adds $5$ to $N$. At the
end of a clause it joins $R$ to the vertices $1$ and $2$ and clears $R$; an empty clause gets
the vertex $N$ joined to $0$, $1$ and $2$, and $N$ is increased by $1$. When the tokens run
out it pushes the vertex count $N$ and halts. Apart from the palette, every edge is pushed by
copy sites, each of which pushes a constant block of bits and then the value of a counter in
ones, restoring the counter through a scratch stack.

Formalized by `Cslib.Complexity.Karp.EmitColor.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#prog).

## Start label of the 3-coloring emitter

The emitter machine starts at its palette label,
the label whose instruction pushes the palette triangle onto the output stack.

Formalized by `Cslib.Complexity.Karp.EmitColor.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#start).

## Quiescent states of the 3-COLOR emitter

A quiescent state records the contents of
the token stack $T$ and of the stacks $D$, $E$, $A$, $P$ (lists of token symbols), the content
of the output stack $O$ (a list of bits), and four natural numbers $n$, $r$, $f$, $u$: the
values of the counters $N$ (next free vertex), $R$ (current OR output), $F$ (first-literal flag)
and $U$ (an earlier literal vertex).

On the machine, $N$, $R$, $F$, $U$ hold that many clause tokens $\mathtt{cl}$ and the scratch
stacks $X$, $B$, $W$ are empty.

Formalized by `Cslib.Complexity.Karp.EmitColor.MS`, a structure declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-03/index.html#ms).

## Stacks of a quiescent state

The stack contents of a quiescent state $m$ of the
3-coloring emitter: the token, output, earlier-occurrence, walk, name and polarity stacks hold
the corresponding lists of $m$; the counters $N$, $R$, $F$ and $U$ hold $n$, $r$, $f$ and $u$
copies of the clause-end symbol, where $n$, $r$, $f$, $u$ are the counter values of $m$; and
the scratch stacks $X$, $B$ and $W$ are empty.

Formalized by `Cslib.Complexity.Karp.EmitColor.MS.stk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#stk).

## Counter values of a quiescent state

For a quiescent state $m$ of the 3-coloring emitter,
the value of the next-vertex counter is the next free vertex $n$ of $m$, that of the OR-output
counter is the current OR output $r$ of $m$, and that of the earlier-literal counter is the
earlier literal vertex $u$ of $m$.

Formalized by `Cslib.Complexity.Karp.EmitColor.MS.val`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#val).

## Counters are not held on the output stack

For each of the three counters read by copy
sites of the 3-coloring emitter, the stack of the counter is not the output stack $O$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Src.k_ne_O`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#k-ne-o).

## Copying a counter through $W$

Let $s$ be a counter, $c$ a stack different from the stack
of $s$ and from $W$, and $x$ a symbol of $c$. Suppose the instruction at label $l_1$ pops the
stack of $s$ until it is empty, pushing $x$ onto $c$ and the unit symbol onto $W$ for each popped
symbol, then goes to $l_2$; and the instruction at $l_2$ pops $W$ until it is empty, pushing the
unit symbol of $s$ onto the stack of $s$ for each popped symbol, then goes to $\ell$. Then for
every $n$, every flag and all stacks $S$ in which the stack of $s$ holds $n$ unit symbols of $s$
and $W$ is empty, the emitter goes from label $l_1$ with stacks $S$ to label $\ell$ in exactly
$2n + 2$ steps, with some flag and the stacks $S$ except that $n$ copies of $x$ are pushed onto
$c$.

Formalized by `Cslib.Complexity.Karp.EmitColor.dup_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#dup-run).

## Bit list of a copy site of the 3-COLOR emitter

For a quiescent state $m$ of the 3-COLOR
emitter and a copy site $j$, the bit list of $j$ at $m$ is $v$ ones followed by the constant
block of $j$, where $v$ is the value in $m$ of the counter that $j$ copies. Read top-first, the
ones lie above the constant block.

Formalized by `Cslib.Complexity.Karp.EmitColor.atom`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#atom).

## Running a copy site of the 3-COLOR emitter

Let $j$ be a copy site, $m$ a quiescent
state and $v$ a local state, and let $c$ be the value in $m$ of the counter that $j$ copies.
From the label that starts site $j$, with local state $v$, the machine runs in exactly
$2c + 3$ steps to the label where $j$ continues, in some local state and in the quiescent
state obtained from $m$ by pushing onto the output stack $c$ ones above the constant block of
$j$.

Formalized by `Cslib.Complexity.Karp.EmitColor.site_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#site-run).

## Copy sites of the 3-COLOR emitter running in sequence

Copy sites $j_1, \dots, j_k$ run in
sequence from label $\ell_0$ to label $\ell$ when $\ell_0$ is the entry label of $j_1$, the
continuation label of each $j_i$ with $i < k$ is the entry label of $j_{i+1}$, and the
continuation label of $j_k$ is $\ell$; for $k = 0$ this means $\ell_0 = \ell$. The condition is
a Boolean test.

Formalized by `Cslib.Complexity.Karp.EmitColor.Chain`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#chain).

## Bits pushed by a sequence of copy sites of the 3-COLOR emitter

For a quiescent state $m$
of the 3-COLOR emitter and copy sites $j_1, \dots, j_k$, the bits of the sequence at $m$ are the
bit lists at $m$ of $j_k, j_{k-1}, \dots, j_1$, concatenated in that order. Read top-first, the
bits of the last site lie on top.

Formalized by `Cslib.Complexity.Karp.EmitColor.chainOut`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#chain-out).

## Running a sequence of copy sites of the 3-COLOR emitter

Let copy sites
$j_1, \dots, j_k$ run in sequence from label $\ell_0$ to label $\ell$, and let $m$ be a quiescent
state of the 3-COLOR emitter whose counters $N$, $R$, $U$ have values $n$, $r$, $u$. Then for
every Boolean $v$ there is a Boolean $v'$ such that the emitter goes in at most
$k (2 (n + r + u) + 3)$ steps from label $\ell_0$ with internal state $v$ and the stacks of $m$
to label $\ell$ with internal state $v'$ and the stacks of $m$ with the bits of the sequence
$j_1, \dots, j_k$ at $m$ placed on top of the output stack.

Formalized by `Cslib.Complexity.Karp.EmitColor.chain_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#chain-run).

## Walk tokens

A symbol is a walk token, one the walk moves between the stacks $D$ and $E$,
when it is a name bit, a literal marker or the clause symbol (which also serves as the unary
unit); the value symbols and the dead symbol are not walk tokens.

Formalized by `Cslib.Complexity.Karp.EmitColor.isTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#is-tok).

## Name of a variable

The name of a variable $x \in \mathbb{N}$ is the list of name-bit
tokens $\mathtt{bit}(b)$, one for each bit $b$ of Mathlib's binary encoding of $x$ (least
significant bit first, empty for $x = 0$), in that order; this is how the stacks $A$ and $D$
hold it.

Formalized by `Cslib.Complexity.Karp.EmitColor.name`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#name).

## Encoding of an earlier occurrence on stack $D$

An occurrence $q = (x, p, L, M)$ of the
literal $(x, p)$ with vertices $L$ and $M$ is written, top first, as the polarity marker of $p$,
then the name bits of the variable $x$, then $L$ unit symbols (its literal vertex in unary);
the vertex $M$ is not recorded.

Formalized by `Cslib.Complexity.Karp.EmitColor.dTok`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#d-tok).

## Moving the current name from $T$ to $A$

Let $m$ be a quiescent state of the 3-COLOR
emitter whose stack $A$ is empty, $v$ a bit, $x \in \mathbb{N}$, and $R$ a list of token symbols
whose first element, if any, is not a name bit. If the token stack $T$ of $m$ is the name of $x$
in reverse order followed by $R$, then for some bit $v'$ the emitter machine runs in exactly
$k + 1$ steps, where $k$ is the length of the binary encoding of $x$, from label $\mathtt{nm}$
with internal bit $v$ and the stacks of $m$ to label $\mathtt{walk}$ with internal bit $v'$ and
the stacks of the quiescent state obtained from $m$ by setting $T$ to $R$ and $A$ to the name
of $x$.

Formalized by `Cslib.Complexity.Karp.EmitColor.nm_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#nm-run).

## Name comparison in the 3-COLOR emitter

Let $m$ be a quiescent state, $u$ and $w$ lists
of bits, and $R$ a list of symbols that is empty or does not start with a name bit. If stack $A$
of $m$ holds $u$ as name bits and stack $D$ holds $w$ as name bits followed by $R$, then from
label $\mathsf{cmp}$ with the stacks of $m$ and any flag, the emitter reaches, in at most
$3|w| + 3$ steps, label $\mathsf{sel}$ if $u = w$ and label $\mathsf{mvN}(\mathrm{none})$
otherwise, with the stacks of $m$ restored and some flag.

Formalized by `Cslib.Complexity.Karp.EmitColor.cmp_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#cmp-run).

## Moving an earlier name from $D$ to $E$

Let $m$ be a quiescent state of the 3-COLOR
emitter, $v$ a bit, $r$ either empty or a bit $b$, $w$ a list of bits, and $R$ a list of token
symbols whose first element, if any, is not a name bit. If the stack $D$ of $m$ is the name bits
of $w$ followed by $R$, then for some bit $v'$ the emitter machine runs in exactly $|w| + 1$
steps from label $\mathtt{mvN}(r)$ with internal bit $v$ and the stacks of $m$ to internal bit
$v'$, label $\mathtt{skU}$ if $r$ is empty and $\mathtt{mvU}(b)$ if $r = b$, and the stacks of
the quiescent state obtained from $m$ by setting $D$ to $R$ and putting the name bits of $w$, in
reverse order, on top of $E$.

Formalized by `Cslib.Complexity.Karp.EmitColor.mvN_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#mv-n-run).

## Skipping an earlier literal vertex

Let $m$ be a quiescent state of the 3-COLOR emitter
whose occurrence stack consists of $j$ units above a stack $R$ that is empty or does not have
a unit on top. From the label $\mathsf{skU}$, with any local state, the machine runs in
exactly $j + 1$ steps to the label $\mathsf{walk}$, in some local state and in the quiescent
state obtained from $m$ by replacing the occurrence stack with $R$ and pushing $j$ units onto
the other side of the walk.

Formalized by `Cslib.Complexity.Karp.EmitColor.skU_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#sk-u-run).

## Moving an earlier literal vertex from $D$ to $U$

Let $m$ be a quiescent state of the
3-COLOR emitter whose counter $U$ is $0$, let $v$ and $b$ be bits, $j \in \mathbb{N}$, and $R$ a
list of token symbols whose first element, if any, is not the clause token $\mathtt{cl}$. If
the stack $D$ of $m$ is $j$ copies of $\mathtt{cl}$ followed by $R$, then for some bit $v'$ the
emitter machine runs in exactly $j + 1$ steps from label $\mathtt{mvU}(b)$ with internal bit $v$
and the stacks of $m$ to label $\mathtt{pre}(c_1)$ if $b$ is true and $\mathtt{pre}(d_1)$ if $b$
is false, internal bit $v'$, and the stacks of the quiescent state obtained from $m$ by setting
$D$ to $R$ and $U$ to $j$.

Formalized by `Cslib.Complexity.Karp.EmitColor.mvU_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#mv-u-run).

## Moving $U$ onto $E$

Let $m$ be a quiescent state and $u$ the value of its counter $U$.
From label $\mathsf{dr}$ with the stacks of $m$ and any flag, the emitter reaches label
$\mathsf{walk}$ in exactly $u + 1$ steps, with some flag and the stacks of $m$ except that $U$ is
empty (value $0$) and $u$ unit symbols are pushed onto $E$.

Formalized by `Cslib.Complexity.Karp.EmitColor.dr_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#dr-run).

## The 3-COLOR emitter clears its OR-output counter

Let $m$ be a quiescent state of the
3-COLOR emitter whose OR-output counter $R$ has value $r$, let $v$ be a Boolean and $b$ a Boolean.
Then there is a Boolean $v'$ such that the emitter runs in exactly $r + 1$ steps from label
$\mathsf{clr}(b)$ with internal state $v$ and the stacks of $m$ to the stacks of $m$ with $R$ set
to $0$ and internal state $v'$, at label $\mathsf{fA}(\mathrm{false})$ if $b$ is true and at
label $\mathsf{cls}$ otherwise.

Formalized by `Cslib.Complexity.Karp.EmitColor.clr_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#clr-run).

## Adding the vertex counter to the OR output

For every quiescent state $m$ with counters
$n$ on stack $N$ and $r$ on stack $R$, every local state $v$ and every boolean $b$, the emitter
goes from label $\mathrm{fA}(b)$ with state $(v, m)$ to label $\mathrm{fC}(b)$, with some local
state, in exactly $2n + 2$ steps, ending in the state $m$ with the counter on $R$ replaced by
$n + r$; the counter $N$ is restored through the scratch stack $W$.

Formalized by `Cslib.Complexity.Karp.EmitColor.fAB_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-04/index.html#f-ab-run).

## 3-COLOR emitter: moving the walk side back

Let $L$ be a list of token symbols each of
which is a walk token (a name bit, a literal marker or the clause symbol), let $m$ be a quiescent
state of the 3-COLOR emitter whose stack $E$ (the walk's other side) holds $L$, and let $v$ be a
Boolean. Then there is a Boolean $v'$ such that the emitter runs in exactly $|L| + 1$ steps from
label $\mathsf{back}$ with internal state $v$ and the stacks of $m$ to label $\mathsf{putN}$ with
internal state $v'$ and the stacks of the quiescent state obtained from $m$ by emptying $E$ and
replacing the occurrence stack $D$ by the reverse of $L$ followed by the old contents of $D$.

Formalized by `Cslib.Complexity.Karp.EmitColor.back_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 719](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L719). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#back-run).

## Recording the current occurrence

Let $m$ be a quiescent state of the 3-COLOR emitter
with next free vertex $n$, whose name stack holds the name bits of a variable $x$ and whose
polarity stack holds only the marker for polarity $b$. From the label $\mathsf{putN}$, with
any local state, the machine runs in exactly $2n + 2|w| + 5$ steps, where $w$ is the binary
encoding of $x$, to the label $\mathsf{aft}$, in some local state and in the quiescent state
obtained from $m$ by emptying the name and polarity stacks and pushing onto the occurrence
stack the entry of the occurrence $(x, b, n, n + 1)$: the polarity marker of $b$ above the
name bits of $x$ above $n$ units.

Formalized by `Cslib.Complexity.Karp.EmitColor.put_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#put-run).

## Copy sites of the occurrence triangle

The list of copy sites $o_1, o_2, o_3, o_4$, in
this order.

Run in sequence, these sites push the edges $(L, M)$, $(L, 2)$, $(M, 2)$ of the occurrence
triangle, where $L = N$ and $M = N + 1$ for the next-vertex counter $N$.

Formalized by `Cslib.Complexity.Karp.EmitColor.occSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#occ-sites).

## Copy sites of the consistency edges

For a flag $b$, the list of copy sites that push the
consistency edges with an earlier occurrence whose literal vertex $L'$ is on stack $U$: the
sites $c_1, c_2, c_3, c_4$ (equal polarity) when $b$ is true, and the sites
$d_1, d_2, d_3, d_4$ (opposite polarity) when $b$ is false.

Formalized by `Cslib.Complexity.Karp.EmitColor.consSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#cons-sites).

## The OR-gadget copy sites

The list of the eleven copy sites $r_1, \dots, r_{11}$ of
the 3-COLOR emitter, in this order.

Run in sequence, they push the OR gadget whose inputs are the next free vertex $N$ and the
current OR output $R$ and whose fresh vertices are $N + 2$, $N + 3$ and $N + 4$.

Formalized by `Cslib.Complexity.Karp.EmitColor.orSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#or-sites).

## Copy sites of the clause end

The list of copy sites $e_1, e_2$, which push the edges
joining the current OR output $R$ to the palette vertices $F = 1$ and $B = 2$.

Formalized by `Cslib.Complexity.Karp.EmitColor.endSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#end-sites).

## Copy sites of the empty clause

The list of copy sites $z_1, z_2, z_3$, which push the
edges joining the next free vertex $N$ to the palette vertices $0$, $1$ and $2$.

Formalized by `Cslib.Complexity.Karp.EmitColor.empSites`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 779](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L779). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#emp-sites).

## Consistency edges of two occurrences of the same variable

Let $x$, $L'$ and $n$ be
natural numbers and let $p$, $b$ be Booleans. The consistency edges between a new occurrence of
the literal $(x, p)$ with vertices $L = n$, $M = n + 1$ and an earlier occurrence
$(x, b, L', L' + 1)$ are $[(L', n + 1), (L' + 1, n)]$ if $b = p$, and
$[(L', n), (L' + 1, n + 1)]$ otherwise.

Formalized by `Cslib.Complexity.Karp.EmitColor.consEdges_same`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 807](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L807). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#cons-edges-same).

## One step of the walk over earlier occurrences

Let $l = (x, p)$ be a new occurrence and
$q = (x', b', L', M')$ an earlier one with $M' = L' + 1$. Let $m$ be a quiescent state whose
stack $D$ holds the tokens of $q$ (the marker of polarity $b'$, the name bits of $x'$, then $L'$
unary unit symbols) above a list $S$ whose first symbol, if any, is neither a unary unit nor a
name bit; whose stack $A$ holds the name bits of $x$; whose stack $P$ holds only the marker of
polarity $p$; and whose counter $U$ is $0$. Write $n$ and $r$ for the counters $N$ and $R$ of $m$
and $k$ for the number of tokens of $q$. Then for every local state $v$, the emitter goes from
label walk with state $(v, m)$ to label walk again, with some local state, in at most
$12k + 8(n + r) + 21$ steps. It ends in the state $m$ with $D$ replaced by $S$, with $E$ holding
the tokens of $q$ in reverse order above its old contents, and with the output stack holding
the bits of the consistency edges of $l$ (with literal vertex $n$ and negation vertex $n + 1$)
with $q$ above its old contents.

Formalized by `Cslib.Complexity.Karp.EmitColor.ent_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#ent-run).

## Walking the earlier occurrences

Let $l = (x, b)$ be a literal and let
$q_1, \dots, q_k$ be earlier occurrences, each a tuple $(y, c, L, M)$ of a variable, a polarity,
a literal vertex and a negation vertex with $M = L + 1$. Let $m$ be a quiescent state of the
3-coloring emitter whose earlier-occurrence stack $D$ holds the concatenation $\delta$ of the
stack encodings of $q_1, \dots, q_k$, whose name stack holds the name bits of $x$, whose
polarity stack holds the single marker of polarity $b$, and whose earlier-literal counter is $0$;
let $n$ and $r$ be its next-vertex and OR-output counter values. Then for every internal state,
the emitter runs in at most $12|\delta| + k(8(n + r) + 21) + 1$ steps from the walk label with
the stacks of $m$ to the back label, with some internal state, and with the stacks of the
quiescent state obtained from $m$ by emptying $D$, putting the reverse of $\delta$ on top of the
walk stack $E$, and putting on top of the output stack the output for the consistency edges of
$l$, with literal vertex $n$ and negation vertex $n + 1$, with $q_1, \dots, q_k$ in turn.

Formalized by `Cslib.Complexity.Karp.EmitColor.walk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#walk-run).

## Emitting one literal occurrence

Let $\ell = (x, p)$ be a literal, $R$ a list of token
symbols whose first element, if any, is not a name bit, and $qs$ a list of earlier occurrences
$(x_i, p_i, L_i, M_i)$ with $M_i = L_i + 1$ for each. Let $m$ be a quiescent state of the
3-COLOR emitter with counter values $n$ for $N$ and $r$ for the OR output, and $v$ a bit.
Suppose the token stack of $m$ is the tokens of $\ell$ (its polarity marker above its name in
reverse order) followed by $R$, the stack $D$ is the concatenated stack encodings of the
occurrences in $qs$, the stacks $E$, $A$, $P$ are empty and the counter $U$ is $0$. Let $d$ be
the length of $D$ and $k$ the length of the binary encoding of $x$. Then for some bit $v'$ the
emitter machine runs in at most
$13 d + |qs| (8 (n + r) + 21) + 10 (n + r) + 3 k + 30$
steps from label $\mathtt{lits}$ with internal bit $v$ and the stacks of $m$ to label
$\mathtt{aft}$ with internal bit $v'$ and the stacks of the quiescent state obtained from $m$
as follows: the token stack is $R$; $D$ holds the stack encodings of $(x, p, n, n + 1)$ and then
of the occurrences in $qs$; and the output is the old output with the edges $(n, n + 1)$,
$(n, 2)$, $(n + 1, 2)$ and then the consistency edges of the new occurrence $(\ell, n, n + 1)$
with the occurrences in $qs$, in order, pushed on top. The counter $N$ is not advanced.

Formalized by `Cslib.Complexity.Karp.EmitColor.occ_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 915](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L915). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#occ-run).

## Size invariant of the 3-coloring emitter

A construction state $s$ satisfies the size
invariant after $\tau$ tokens when its next free vertex $n$ is at most $5\tau + 3$, it has at
most $\tau$ earlier occurrences, the total number of tokens of its earlier occurrences as they
lie on stack $D$ is at most $\tau (n + 1)$, and every earlier occurrence $(x, b, L, M)$ has
$M = L + 1$.

Formalized by `Cslib.Complexity.Karp.EmitColor.Inv`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 954](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L954). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#inv).

## One more token preserves the 3-COLOR emitter's size invariant

Let $s$ and $s'$ be
construction states with the same earlier occurrences, such that the next free vertex of $s'$ is
at least that of $s$ and at most that of $s$ plus $5$. If $s$ satisfies the size invariant after
$\tau$ tokens, then $s'$ satisfies the size invariant after $\tau + 1$ tokens.

Formalized by `Cslib.Complexity.Karp.EmitColor.Inv.bump`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 963](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L963). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#bump).

## The size invariant survives a new literal occurrence

Let $s$ and $s'$ be states of
the 3-COLOR construction with next free vertices $n$ and $n'$, and let $l = (x, p)$ be a
literal. Suppose that $s$ satisfies the size invariant after $\tau$ tokens, that the earlier
occurrences of $s'$ are those of $s$ preceded by the occurrence of $l$ with literal vertex $n$
and negation vertex $n + 1$, and that $n \le n' \le n + 5$. Then $s'$ satisfies the size
invariant after $\tau + t$ tokens, where $t$ is the number of tokens of $l$ on the token
stack.

Formalized by `Cslib.Complexity.Karp.EmitColor.Inv.occ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 972](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L972). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#occ).

## Per-token step budget of the 3-COLOR emitter

For a bound $L$ on the number of tokens of
a formula, the step budget per token is $400 (L + 1)^2$.

Formalized by `Cslib.Complexity.Karp.EmitColor.budget`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1040](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1040). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#budget).

## The emitter state of a construction state

For a construction state $s$, a token list $t$,
a bit list $o_0$ and natural numbers $r$ and $f$: the quiescent state whose token stack is $t$,
whose output stack is the bits of the edges emitted by $s$ (the last one on top) above $o_0$,
whose counter $N$ is the next free vertex of $s$, whose counter $R$ is $r$, whose stack $D$
holds the encodings of the earlier occurrences of $s$ (latest on top), whose stacks $E$, $A$
and $P$ are empty, whose counter $F$ is $f$, and whose counter $U$ is $0$.

Formalized by `Cslib.Complexity.Karp.EmitColor.enc`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1044](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1044). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#enc).

## Step budget for one literal

Let $L_b, \tau, n, r, P, D, w$ be natural numbers with
$\tau + w + 1 \le L_b$, $n \le 5\tau + 3$, $r \le n$, $P \le \tau$ and $D \le \tau (n + 1)$. Then
$13 D + P (8 (n + r) + 21) + 40 (n + r) + 3 w + 100 \le \mathrm{budget}(L_b)$, where
$\mathrm{budget}(L_b) = 400 (L_b + 1)^2$ is the per-token step budget of the 3-COLOR emitter.

Formalized by `Cslib.Complexity.Karp.EmitColor.lit_cost`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1051](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1051). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#lit-cost).

## The emitter processes the remaining literals of a clause

Let $L_b \in \mathbb{N}$, let
$R$ be a list of token symbols that is empty or starts with the clause token $\mathtt{cl}$, and
let $o_0$ be a list of bits. Let $ls$ be a list of literals, $o, \tau \in \mathbb{N}$, $s$ a
construction state and $v$ a bit, and write $T$ for the concatenation of the token-stack tokens
of the literals of $ls$ and $TR$ for $T$ followed by $R$. Suppose $s$ satisfies the size
invariant after $\tau$ tokens, $o$ is at most the next free vertex of $s$, and
$\tau + |T| \le L_b$. Then for some bit $v'$ the emitter machine runs in at most
$(|T| + 1) \cdot \mathrm{budget}(L_b)$ steps from label $\mathtt{lits}$ with internal bit $v$
and the stacks of the quiescent state $\mathrm{enc}(s, TR, o_0, o, 0)$ to label $\mathtt{cls}$
with internal bit $v'$ and the stacks of $\mathrm{enc}(\mathrm{colLits}(ls, o, s), R, o_0, 0, 0)$.
Here $\mathrm{enc}(s, t, o_0, r, f)$ is the quiescent state of $s$ with token stack $t$, output
above $o_0$, OR output $r$ and first-literal flag $f$; $\mathrm{colLits}(ls, o, s)$ is $s$ after
the occurrences and OR gadgets of $ls$, starting from OR output $o$, and the clause end; and
$\mathrm{budget}(L_b) = 400 (L_b + 1)^2$.

Formalized by `Cslib.Complexity.Karp.EmitColor.lits_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1073](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1073). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#lits-run).

## The 3-COLOR emitter processes one clause

Let $C$ be a CNF clause, $T_C$ its tokens as
they lie on the token stack, $s$ a construction state that satisfies the size invariant after
$\tau$ tokens, and $L$ a bound with $\tau + |T_C| \le L$. Let $Y$ be a list of symbols that is
empty or starts with the clause marker, and $o_0$ a list of bits. For a construction state $t$
and a symbol list $X$, write $q(t, X)$ for the quiescent state encoding $t$ with token stack $X$,
output stack holding the bits of the edges emitted in $t$ above $o_0$, OR output $0$ and
first-literal flag $0$. Then for every Boolean $v$ there is a Boolean $v'$ such that the emitter
goes in at most $|T_C| \cdot (400 (L + 1)^2 + 1)$ steps from label $\mathsf{cls}$ with internal
state $v$ and the stacks of $q(s, T_C Y)$ to label $\mathsf{cls}$ with internal state $v'$ and
the stacks of $q(s_C, Y)$, where $T_C Y$ is $T_C$ on top of $Y$ and $s_C$ is the construction
state after clause $C$ is processed from $s$.

Formalized by `Cslib.Complexity.Karp.EmitColor.clause_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#clause-run).

## The emitter on a list of clauses

Let $L_b$ be a natural number, $o_0$ a list of bits,
$C_s$ a list of clauses, $s$ a construction state and $\tau$ a natural number, and let $T$ be the
concatenation over the clauses $C$ of $C_s$, in order, of the tokens of $C$ as they lie on the
token stack. If the size invariant holds for $\tau$ and $s$ and $\tau + |T| \le L_b$, then for
every local state $v$ the emitter goes from label cls with the quiescent state of $s$ with
tokens $T$, output above $o_0$, OR output $0$ and first-literal flag $0$, to label cls again,
with some local state, in at most $|T| \cdot (400 (L_b + 1)^2 + 1)$ steps. It ends in the
quiescent state of $s'$ with no tokens, output above $o_0$, OR output $0$ and first-literal
flag $0$, where $s'$ is obtained from $s$ by applying the one-clause step of the 3-coloring
construction to the clauses of $C_s$ in order.

Formalized by `Cslib.Complexity.Karp.EmitColor.formula_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-05/index.html#formula-run).

## Correctness and step bound of the 3-COLOR emitter

Let $\varphi$ be a CNF formula
with token list $t(\varphi)$, let $o$ be a bit list and $v$ a Boolean. Started at its start
label with local state $v$, with the token stack holding $t(\varphi)$ reversed, the output
stack holding $o$ and every other stack empty, the emitter machine reaches the label
$\mathsf{done}$ within $500\,(|t(\varphi)| + 1)^4$ steps, in some local state and with some
stacks whose output stack holds the 3-COLOR instance of $\varphi$ followed by $o$ (read
top-first).

Formalized by `Cslib.Complexity.Karp.EmitColor.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorEmit.lean, line 1223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorEmit.lean#L1223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#run).

## Color code of a vertex in a witness

The color code of vertex $i$ in a bit string $w$ is
the pair of bits at positions $2i$ and $2i + 1$ of $w$ (counting from $0$), where a position past
the end of $w$ reads as $0$. The codes $00$, $01$, $10$ stand for the colors $0$, $1$, $2$; $11$
is invalid.

Formalized by `Cslib.Complexity.Karp.ColVerify.col`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col).

## Valid color code

A color code, a pair of bits $(c_1, c_2)$, is valid when it is not
$11$, that is, when $c_1$ and $c_2$ are not both $1$.

Formalized by `Cslib.Complexity.Karp.ColVerify.okCol`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#ok-col).

## The 3-COLOR verifier

The verifier accepts an input $x$ and a witness $w$ (bit strings)
iff $x$ decodes to a number $n$ and an edge list $E$, every endpoint of an edge in $E$ is less
than $n$, $w$ has at least $2n$ bits, every vertex $i < n$ has a valid color code in $w$ (bits
$2i$ and $2i + 1$, not $11$), and the two ends of every edge $(u, v) \in E$ with $u \ne v$ have
different color codes.

Formalized by `Cslib.Complexity.Karp.ColVerify.colCheck`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col-check).

## Acceptance condition of the 3-COLOR verifier

For all bit strings $x$ and $w$, the verifier
accepts $(x, w)$ iff there are a natural number $n$ and a list $E$ of pairs of natural numbers
such that $x$ is the encoding of the graph with $n$ vertices and edge list $E$, both entries of
every pair in $E$ are less than $n$, $w$ has at least $2n$ bits, the color code of every vertex
$i < n$ in $w$ is valid, and for every $(u, v) \in E$ with $u \ne v$ the color codes of $u$ and
$v$ in $w$ differ.

Formalized by `Cslib.Complexity.Karp.ColVerify.colCheck_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col-check-iff).

## Two-bit code of a color

The code of a color $c \in \{0, 1, 2\}$ is the pair of bits whose
first bit is $1$ iff $c = 2$ and whose second bit is $1$ iff $c = 1$: $0 \mapsto 00$,
$1 \mapsto 01$ and $2 \mapsto 10$.

Formalized by `Cslib.Complexity.Karp.ColVerify.code`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#code).

## Decoding a color code

The color in $\{0, 1, 2\}$ of a pair of bits $(a, b)$, writing $0$
for false and $1$ for true: $(0, 1)$ decodes to $1$, $(1, 0)$ decodes to $2$, and both $(0, 0)$
and the invalid code $(1, 1)$ decode to $0$.

Formalized by `Cslib.Complexity.Karp.ColVerify.uncode`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#uncode).

## Decoding a color code recovers the color

For every color $c \in \{0, 1, 2\}$, decoding
the two-bit code of $c$ (where $0 \mapsto 00$, $1 \mapsto 01$, $2 \mapsto 10$) gives back $c$.

Formalized by `Cslib.Complexity.Karp.ColVerify.uncode_code`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#uncode-code).

## Color codes are valid

For each color $c \in \{0, 1, 2\}$, the code of $c$ (which is
$00$, $01$ or $10$) is a valid color code, that is, it is not $11$.

Formalized by `Cslib.Complexity.Karp.ColVerify.okCol_code`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#ok-col-code).

## Re-encoding a decoded valid color

For every valid color code $c$ (a pair of bits other
than $11$), the code of the color that $c$ decodes to is $c$.

Formalized by `Cslib.Complexity.Karp.ColVerify.code_uncode`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#code-uncode).

## Flattening pairs of bits

The flattening of a list $[(a_1, b_1), \dots, (a_k, b_k)]$ of
pairs of bits is the list of bits $[a_1, b_1, \dots, a_k, b_k]$.

Formalized by `Cslib.Complexity.Karp.ColVerify.flat`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#flat).

## Flattening the empty list

The flattening of the empty list of pairs of bits is the empty
list of bits.

Formalized by `Cslib.Complexity.Karp.ColVerify.flat_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#flat-nil).

## Flattening a nonempty list

For a pair of bits $c = (a, b)$ and a list $cs$ of pairs of
bits, the flattening of the list with head $c$ and tail $cs$ is the list with $a$ first, then $b$,
then the flattening of $cs$.

Formalized by `Cslib.Complexity.Karp.ColVerify.flat_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#flat-cons).

## Flattening a concatenation

For lists $cs$ and $ds$ of pairs of bits, the flattening of
the concatenation of $cs$ and $ds$ is the concatenation of the flattening of $cs$ and the
flattening of $ds$.

Formalized by `Cslib.Complexity.Karp.ColVerify.flat_append`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#flat-append).

## Length of a flattening

For every list $cs$ of pairs of bits, the flattening of $cs$ has
length $2|cs|$, two bits per pair.

Formalized by `Cslib.Complexity.Karp.ColVerify.length_flat`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#length-flat).

## Color codes of flattened pairs

For every list $cs$ of pairs of bits and every natural
number $i$, the color code of vertex $i$ in the flattening of $cs$ is the $i$-th pair of $cs$
(counting from $0$) if $i$ is less than the length of $cs$, and $00$ otherwise.

Formalized by `Cslib.Complexity.Karp.ColVerify.col_flat`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col-flat).

## Color codes of a flattened coloring

For every $n$, every map $f$ from $\{0, \dots, n - 1\}$
to pairs of bits and every $i < n$, the color code of vertex $i$ in the flattening of the list
$f(0), \dots, f(n - 1)$ is $f(i)$.

Formalized by `Cslib.Complexity.Karp.ColVerify.col_flat_ofFn`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col-flat-of-fn).

## 3-colorability by witness bits

Let $n \in \mathbb{N}$ and let $es$ be a list of pairs of
natural numbers whose entries are all less than $n$. The graph on the vertices $0, \dots, n-1$
with edge list $es$ (symmetrized, loops dropped) is 3-colorable iff there is a list $w$ of exactly
$2n$ bits such that, writing the color code of vertex $i$ for the pair of bits $2i$ and $2i+1$ of
$w$, the color code of every vertex $i < n$ is valid (not $11$), and for every edge $(u, v)$ in
$es$ with $u \ne v$ the color codes of $u$ and $v$ differ.

Formalized by `Cslib.Complexity.Karp.ColVerify.colorable_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#colorable-iff).

## 3-COLOR is verified by the witness check

A bit string $x$ is in 3-COLOR iff some bit
string $w$ of length at most $2|x|$ is accepted together with $x$ by the 3-COLOR verifier.

Formalized by `Cslib.Complexity.Karp.ColVerify.col3Dec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#col3-dec-iff).

## Witness colors of the first $n$ vertices

For a bit list $w$ and $n \in \mathbb{N}$, the
list of the color codes of the vertices $0, 1, \dots, n-1$ in $w$, in that order, where the color
code of vertex $i$ is the pair of bits $2i$ and $2i+1$ of $w$ (a missing bit reads as false).

Formalized by `Cslib.Complexity.Karp.ColVerify.cols`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-06/index.html#cols).

## Edge verdict

For a list $cs$ of color codes (pairs of bits), one per vertex, and
$u, v \in \mathbb{N}$, the edge $(u, v)$ passes iff $u$ and $v$ are both less than the length of
$cs$ and either $u = v$ or entries $u$ and $v$ of $cs$ differ.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgeOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#edge-ok).

## Edge-loop verdict

For a list $cs$ of color codes and a bit list $r$, the verdict is true
iff $r$ parses as a list of edges, each written as two unary numbers $u$ and $v$ (a number $k$ as
$k$ ones, then a zero), and every edge $(u, v)$ of that list passes the edge verdict with vertex
colors $cs$.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgesOk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#edges-ok).

## Number of witness colors

For every list of bits $w$ and every $n \in \mathbb{N}$, the
list of the witness color codes of the vertices $0, \dots, n - 1$ read from $w$ has length $n$.

Formalized by `Cslib.Complexity.Karp.ColVerify.length_cols`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#length-cols).

## Reading a witness color

For a list of bits $w$ and natural numbers $i$ and $n$, write
$c_w(j)$ for the color code of vertex $j$ in $w$: the pair of bits $2j$ and $2j + 1$ of $w$
(counting from $0$), each read as false past the end of $w$. If $i < n$, then entry $i$
(counting from $0$) of the list $c_w(0), \dots, c_w(n - 1)$ of witness colors is $c_w(i)$.

Formalized by `Cslib.Complexity.Karp.ColVerify.getD_cols`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#get-d-cols).

## Peeling a vertex off the witness colors

For bits $a, b$, a bit list $w$ and
$n \in \mathbb{N}$, the color codes of the vertices $0, \dots, n$ read from the bit list $a, b, w$
(the list $w$ with $a$ and $b$ prepended) are $(a, b)$ followed by the color codes of the vertices
$0, \dots, n-1$ read from $w$.

Formalized by `Cslib.Complexity.Karp.ColVerify.cols_cons_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#cols-cons-cons).

## The 3-COLOR verifier as an edge loop

For all bit strings $x$ and $w$, the verifier accepts
$(x, w)$ iff reading a unary prefix $1^n 0$ off $x$ succeeds, giving $n$ and the rest $r$ of $x$,
and then $w$ has at least $2n$ bits, each of the witness colors $c_0, \dots, c_{n-1}$ of $w$ is
valid (not $11$), and the edge loop accepts $r$ with the vertex colors $c_0, \dots, c_{n-1}$.

Formalized by `Cslib.Complexity.Karp.ColVerify.colCheck_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#col-check-eq).

## Shifting the edge verdict past the first color

For a color code $c$, a list $cs$ of color
codes and $u, v \in \mathbb{N}$, the edge verdict for $(u + 1, v + 1)$ with vertex colors $c$
followed by $cs$ equals the edge verdict for $(u, v)$ with vertex colors $cs$.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgeOk_cons_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#edge-ok-cons-succ).

## Stacks of the 3-COLOR verifier

The verifier has seven stacks: the input $X$ and the
witness $W$; the counter $N$ (for the number $n$ of vertices); the color stack $P$ (the $n$ color
codes, vertex $0$ on top) and its scratch stack $T$; and the endpoint counters $U$ and $V$.

Formalized by `Cslib.Complexity.Karp.ColVerify.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#k).

## Labels of the 3-COLOR verifier

The labels are: read the number $n$ of vertices onto the
counter stack $N$; load the witness colors onto the scratch stack $T$; move them onto the color
stack $P$; start an edge; read its first endpoint onto the counter stack $U$; read its second
endpoint onto the counter stack $V$; walk the colors towards both endpoints; for each pair of
bits $(a, b)$, walk on towards the farther endpoint holding the nearer one's color $(a, b)$, one
label for counter $U$ and one for counter $V$; restore $P$; accept; reject.

Formalized by `Cslib.Complexity.Karp.ColVerify.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#lab).

## Statements of the 3-COLOR verifier

The type of statements of the verifier as a
multi-stack Turing machine in Mathlib's model: each of the seven stacks (the input, the witness,
the counter for the number of vertices, the color stack and its scratch stack, and the two
endpoint counters) holds symbols of the SAT verifier's alphabet, the labels are the verifier's
labels, and the internal state is a single bit.

Formalized by `Cslib.Complexity.Karp.ColVerify.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#stmt).

## Unary reader of the 3-COLOR verifier

Given a counter stack $c$ and labels $s$ (its own)
and $t$ (the next): if the input stack $X$ is empty, reject; otherwise pop a bit off $X$; if it
is $1$, push a unit onto $c$ and go back to $s$, and if it is $0$, go to $t$. A symbol of $X$
that is not a bit is read as $0$.

Formalized by `Cslib.Complexity.Karp.ColVerify.readU`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#read-u).

## Load step of the 3-COLOR verifier

If the counter stack $N$ is empty, go to the label
that moves the codes onto the color stack $P$. Otherwise pop one symbol off $N$ and two bits $a$,
$b$ off the witness stack $W$, pushing each onto the scratch stack $T$ as it is popped (so the
codes end up reversed on $T$), and go back to the load label; reject instead if $W$ is empty
when a bit is due, or if $a$ and $b$ are both $1$ (the invalid code $11$). A symbol of $W$ that
is not a bit is read as $0$.

Formalized by `Cslib.Complexity.Karp.ColVerify.loadS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#load-s).

## Edge-loop start of the 3-COLOR verifier

The verifier statement that begins checking the
next edge: if the input stack $X$ is empty it goes to the accepting label, and otherwise it goes
to the label that reads the first endpoint of the next edge onto the counter $U$.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgeS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#edge-s).

## Moving one color code in the 3-COLOR verifier

Given a map $f$ from pairs of bits to
labels: if the color stack $P$ is empty, reject (an endpoint lies past the last vertex);
otherwise pop two bits $a$, $b$ off $P$, push them onto the scratch stack $T$ in that order (so
$b$ ends on top), and go to the label $f(a, b)$. A missing or non-bit symbol is read as $0$.

Formalized by `Cslib.Complexity.Karp.ColVerify.mvP`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#mv-p).

## One step of the joint walk of the 3-COLOR verifier

The statement pops the top symbol of
each of the endpoint counters $U$ and $V$ (a pop from an empty counter leaves it empty) and then
moves the next color code $(a, b)$ from the color stack $P$ onto the scratch stack $T$, rejecting
if $P$ is empty. It continues at the joint walk again if both counters were nonempty; at the walk
towards the endpoint of $U$, holding the color $(a, b)$, if only $U$ was nonempty (so $(a, b)$ is
the color of the endpoint of $V$); at the walk towards the endpoint of $V$, holding $(a, b)$, if
only $V$ was nonempty; and at the restoring label $\mathsf{back}$ if both were empty. In the last
case the edge is a loop, which passes once its endpoint's color exists.

Formalized by `Cslib.Complexity.Karp.ColVerify.walkS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#walk-s).

## One step of the walk towards the farther endpoint

Given a stack $k$ of the 3-COLOR
verifier (used as a counter), a label $\ell$ and a pair of bits $(a, b)$ (the color of the
nearer endpoint), the statement pops the top symbol of $k$ and then moves the next color code
$(a', b')$ from the color stack $P$ onto the scratch stack $T$, rejecting if $P$ is empty. If $k$
was nonempty it continues at $\ell$. Otherwise $(a', b')$ is the color of the farther endpoint,
and the statement rejects if $(a', b') = (a, b)$ and continues at the restoring label
$\mathsf{back}$ if not.

Formalized by `Cslib.Complexity.Karp.ColVerify.walk1S`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#walk1-s).

## The 3-COLOR verifier machine

The verifier is the program on the seven stacks $X$
(input), $W$ (witness), $N$, $P$, $T$, $U$, $V$, with internal state a bit, that runs as follows.
It reads the unary number $n$ off $X$ onto the counter $N$; loads the first $n$ color codes of
$W$ onto $T$, rejecting if $W$ runs out or one of these $n$ codes is $11$; moves the bits on top
of $T$ onto the color stack $P$; and then repeatedly starts an edge, accepting if $X$ is
exhausted and otherwise reading the endpoints $u$ and $v$ in unary onto the counters $U$ and
$V$, walking the colors from $P$ onto $T$ towards both endpoints, and moving the passed colors
back from $T$ onto $P$ before the next edge. Reading a number rejects if $X$ runs out; the walk
rejects if an endpoint has no color or if the two endpoints of a non-loop edge have the same
color. The accepting and rejecting labels halt.

Formalized by `Cslib.Complexity.Karp.ColVerify.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#prog).

## Start label of the 3-coloring verifier

The 3-coloring verifier machine starts at the
label that reads the vertex count $n$, written in unary on the input stack $X$, onto the counter
stack $N$.

Formalized by `Cslib.Complexity.Karp.ColVerify.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#start).

## One step of the 3-COLOR verifier

Let $l$ and $l'$ be labels, $v$ an internal state and
$S$ an assignment of stacks. If executing the verifier's statement at $l$ from state $v$ and
stacks $S$ ends at label $l'$, then for some internal state $v'$ and stacks $S'$ the verifier
goes in one step from label $l$ with state $v$ and stacks $S$ to label $l'$ with state $v'$ and
stacks $S'$.

Formalized by `Cslib.Complexity.Karp.ColVerify.run_one`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#run-one).

## Interleaved updates of two stacks of the 3-COLOR verifier

Let $a \ne b$ be two stacks of
the verifier, $S$ an assignment of a list of symbols to every stack, and $p, p', t, t'$ lists of
symbols. Setting stack $a$ to $p$, then $b$ to $t$, then $a$ to $p'$, then $b$ to $t'$ gives the
same assignment as setting $a$ to $p'$ and then $b$ to $t'$.

Formalized by `Cslib.Complexity.Karp.ColVerify.update_update_update_update`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-07/index.html#update-update-update-update).

## Moving one color code from the color stack

Let $f$ assign a label to each pair of
bits, and suppose the color stack $P$ of stacks $S$ holds, from the top, the bit symbols $c_1$
and $c_2$ followed by a rest $r$. Then executing the color-moving block with continuation $f$,
from any internal value and the stacks $S$, ends at label $f(c_1, c_2)$ with internal value
$c_2$ and with the stacks $S$ changed only in that $P$ becomes $r$ and the scratch stack $T$
gets $c_1$ and then $c_2$ pushed on top (so $c_2$ is on top).

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_mvP_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-mv-p-cons).

## The color-moving block rejects on an empty color stack

If the color stack $P$ of
stacks $S$ is empty, then for every continuation $f$ (a label for each pair of bits), executing
the color-moving block with continuation $f$ from any internal value and the stacks $S$ ends at
the rejecting label with internal value true and the stacks $S$ unchanged.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_mvP_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-mv-p-nil).

## Walk-on step with the counter exhausted

Let $k$ be a stack, $\ell$ a label and $a, b$
bits. If stack $k$ of stacks $S$ is empty, then executing the walk-on block for counter $k$,
label $\ell$ and held color $(a, b)$, from any internal value and the stacks $S$, has the same
outcome as executing, from internal value false and the stacks $S$, the color-moving block
that continues to the rejecting label if the color it moves is $(a, b)$ and to the label that
restores the color stack otherwise.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walk1S_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk1-s-nil).

## Walk-on step with a unit on the counter

Write $1^j$ for the stack of $j$ copies of the
bit symbol for true. Let $k$ be a stack, $\ell$ a label and $a, b$ bits. If stack $k$ of
stacks $S$ holds $1^{j+1}$, then executing the walk-on block for counter $k$, label $\ell$ and
held color $(a, b)$, from any internal value and the stacks $S$, has the same outcome as
executing, from internal value true and the stacks $S$ with stack $k$ replaced by $1^j$, the
color-moving block that continues to $\ell$ whatever color it moves.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walk1S_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk1-s-cons).

## The walk towards the farther endpoint decides the edge

Let $k$ be a stack of the 3-COLOR
verifier other than the color stack $P$ and the scratch stack $T$, $(a, b)$ a pair of bits, and
$\ell$ a label whose statement is the step of the walk towards the farther endpoint on the
counter $k$, holding the color $(a, b)$ and continuing at $\ell$. Let $j$ be a natural number,
$\mathit{pre}$ and $\mathit{post}$ lists of color codes, $s$ a bit and $S$ an assignment of a list
of symbols to every stack. Suppose that $S$ holds $j$ unit symbols on $k$, the bits of
$\mathit{post}$ on $P$ (each code $(a', b')$ contributing $a'$ then $b'$, the first code on top),
and the bits of $\mathit{pre}$, flattened the same way, in reverse order on $T$. Started at $\ell$
with internal state $s$ and stacks $S$, the verifier reaches within at most $j + 1$ steps, with
some internal state and stacks $S'$, the label $\mathsf{back}$ if $j$ is less than the length of
$\mathit{post}$ and the code at position $j$ of $\mathit{post}$ differs from $(a, b)$, and the
label $\mathsf{no}$ otherwise. If $j$ is less than the length of $\mathit{post}$, the stacks $S'$
hold the bits of $\mathit{post}$ after its first $j + 1$ codes on $P$, the bits of $\mathit{pre}$
followed by those of the first $j + 1$ codes of $\mathit{post}$, flattened and in reverse order,
on $T$, nothing on $k$, and agree with $S$ on every other stack.

Formalized by `Cslib.Complexity.Karp.ColVerify.walk1_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#walk1-run).

## Joint-walk step with both counters nonempty

Write $1^j$ for the stack of $j$ copies of
the bit symbol for true. If the endpoint counters of stacks $S$ hold $U = 1^{u+1}$ and
$V = 1^{v+1}$, then executing the joint-walk block from any internal value and the stacks $S$
has the same outcome as executing, from internal value true and the stacks $S$ with $U$
replaced by $1^u$ and $V$ by $1^v$, the color-moving block that continues to the joint-walk
label whatever color it moves.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walkS_cons_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk-s-cons-cons).

## Joint-walk step when the second endpoint counter runs out first

Write $1^j$ for the
stack of $j$ copies of the bit symbol for true. If the endpoint counters of stacks $S$ hold
$U = 1^{u+1}$ and $V$ empty, then executing the joint-walk block from any internal value and
the stacks $S$ has the same outcome as executing, from internal value false and the stacks $S$
with $U$ replaced by $1^u$, the color-moving block that, after moving a color $(a, b)$,
continues to the label that walks on along $U$ holding $(a, b)$.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walkS_cons_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk-s-cons-nil).

## Joint-walk step when the first endpoint counter runs out first

Write $1^j$ for the
stack of $j$ copies of the bit symbol for true. If the endpoint counters of stacks $S$ hold
$U$ empty and $V = 1^{v+1}$, then executing the joint-walk block from any internal value and
the stacks $S$ has the same outcome as executing, from internal value true and the stacks $S$
with $V$ replaced by $1^v$, the color-moving block that, after moving a color $(a, b)$,
continues to the label that walks on along $V$ holding $(a, b)$.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walkS_nil_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk-s-nil-cons).

## Joint-walk step with both counters exhausted

If the endpoint counters $U$ and $V$ of
stacks $S$ are both empty, then executing the joint-walk block from any internal value and the
stacks $S$ has the same outcome as executing, from internal value false and the same stacks
$S$, the color-moving block that continues to the label restoring the color stack whatever
color it moves.

This is the case of a loop edge.

Formalized by `Cslib.Complexity.Karp.ColVerify.stepAux_walkS_nil_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#step-aux-walk-s-nil-nil).

## Edge verdict for an edge starting at vertex 0

For a color code $c$, a list $cs$ of color
codes and $v \in \mathbb{N}$, the edge $(0, v + 1)$ passes the edge verdict with vertex colors $c$
followed by $cs$ iff $v$ is less than the length of $cs$ and entry $v$ of $cs$ differs from $c$.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgeOk_zero_succ`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#edge-ok-zero-succ).

## Edge verdict for an edge ending at vertex 0

For a color code $c$, a list $cs$ of color
codes and $u \in \mathbb{N}$, the edge $(u + 1, 0)$ passes the edge verdict with vertex colors $c$
followed by $cs$ iff $u$ is less than the length of $cs$ and entry $u$ of $cs$ differs from $c$.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgeOk_succ_zero`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#edge-ok-succ-zero).

## The joint walk of the 3-COLOR verifier decides one edge

Let $u, v$ be natural numbers,
$\mathit{pre}$ and $\mathit{post}$ lists of color codes (pairs of bits), $s$ a bit and $S$ an
assignment of a list of symbols to every stack. Suppose that $S$ holds $u$ unit symbols on the
counter $U$ and $v$ on the counter $V$, the bits of $\mathit{post}$ on the color stack $P$ (each
code $(a, b)$ contributing $a$ then $b$, the first code on top), and the bits of $\mathit{pre}$,
flattened the same way, in reverse order on the scratch stack $T$. Started at the label
$\mathsf{walk}$ with internal state $s$ and stacks $S$, the verifier reaches within at most
$\max(u, v) + 1$ steps, with some internal state and stacks $S'$, the label $\mathsf{back}$ if the
edge $(u, v)$ passes against the colors $\mathit{post}$ and the label $\mathsf{no}$ otherwise. The
edge passes when $u$ and $v$ are both less than the length of $\mathit{post}$ and either $u = v$
or the codes at positions $u$ and $v$ of $\mathit{post}$ differ. If it passes then, with
$m = \max(u, v) + 1$, the stacks $S'$ hold the bits of $\mathit{post}$ after its first $m$ codes
on $P$, the bits of $\mathit{pre}$ followed by those of the first $m$ codes of $\mathit{post}$,
flattened and in reverse order, on $T$, nothing on $U$ and $V$, and agree with $S$ on every other
stack.

Formalized by `Cslib.Complexity.Karp.ColVerify.walk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#walk-run).

## The unary reader on a terminated number

Let $c \ne X$ be a stack and $s$, $t$ labels
such that the verifier runs, at $s$, the unary reader from $X$ onto the counter $c$ that loops at
$s$ and exits to $t$. Let $k, j$ be natural numbers and $r$ a list of bits. If $X$ holds $k$ ones,
then a zero, then $r$, and $c$ holds exactly $j$ units, then from label $s$, in any internal
state, the verifier reaches label $t$ in exactly $k + 1$ steps, with $X$ holding $r$, $c$ holding
exactly $k + j$ units, and every other stack as at the start.

Formalized by `Cslib.Complexity.Karp.ColVerify.readU_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#read-u-some).

## The unary reader rejects an unterminated number

Let $c \ne X$ be a stack and $s$, $t$
labels such that the verifier runs, at $s$, the unary reader from $X$ onto the counter $c$ that
loops at $s$ and exits to $t$. If $X$ holds a bit list $l$ on which reading a unary number
fails, that is, $l$ consists of ones only, then from label $s$, in any internal state and with
any other stacks, the verifier reaches the rejecting label within at most $|l| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.ColVerify.readU_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#read-u-none).

## Run of the load phase of the 3-COLOR verifier

Let $n$ be a natural number and $w$, $a$
lists of bits. Start the verifier at its load label, in any internal state, with stacks in which
the counter $N$ holds exactly $n$ units, the witness stack $W$ holds $w$ and the scratch stack $T$
holds $a$. Then within at most $n + 1$ steps the verifier reaches the label that moves the codes
onto the color stack $P$ if $w$ has at least $2n$ bits and the color codes of the vertices
$0, \dots, n - 1$ (vertex $i$ has the code $w_{2i} w_{2i+1}$) are all valid, that is, none is
$11$; otherwise it reaches the rejecting label. In the first case $T$ then holds the first $2n$
bits of $w$ in reverse order on top of $a$, and every stack other than $N$, $W$ and $T$ is as at
the start.

Formalized by `Cslib.Complexity.Karp.ColVerify.load_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#load-run).

## Edge-loop verdict after one parsed edge

Let $cs$ be a list of color codes and $r$ a bit
list. If $r$ begins with $u$ in unary ($u$ ones, then a zero) followed by the rest $r_1$, and
$r_1$ begins with $v$ in unary followed by the rest $r_2$, then the edge-loop verdict on $r$ with
vertex colors $cs$ holds iff the edge verdict for $(u, v)$ holds and the edge-loop verdict on
$r_2$ holds.

Formalized by `Cslib.Complexity.Karp.ColVerify.edgesOk_of_some_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#edges-ok-of-some-some).

## Restoring the color stack in the 3-COLOR verifier

Let $\mathit{pre}$ and $\mathit{post}$
be lists of pairs of bits, let $s$ be a Boolean state, and let $S$ assign to each stack a list of
symbols. Suppose that in $S$ the stack $P$ holds the bits of the flattening of $\mathit{post}$
and the stack $T$ holds the bits of the flattening of $\mathit{pre}$ in reverse order (as bit
symbols, top first). Then the verifier program runs in exactly $2 |\mathit{pre}| + 1$ steps from
the label back with state $s$ and stacks $S$ to the label edge with some state $s'$ and stacks
$S'$ such that $T$ is empty in $S'$, $P$ holds the bits of the flattening of $\mathit{pre}$
followed by $\mathit{post}$, and every stack other than $T$ and $P$ is unchanged.

Formalized by `Cslib.Complexity.Karp.ColVerify.back_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#back-run).

## Correctness and running time of the edge loop

Let $cs$ be a list of color codes (pairs
of bits) and $r$ a list of bits, and encode an edge $(u, v)$ of natural numbers as $u$ ones, a
zero, $v$ ones and a zero. Call $r$ good for $cs$ when $r$ is a concatenation of encoded edges
such that, for every edge $(u, v)$ among them, $u$ and $v$ are below the length of $cs$ and, if
$u \ne v$, entries $u$ and $v$ of $cs$ (counting from $0$) differ. Suppose the 3-COLOR verifier
is at its edge label, in any internal state, with the input stack $X$ holding the bits of $r$
(first bit on top), the color stack $P$ holding the bits of the flattening of $cs$, the stacks
$T$, $U$ and $V$ empty, and the other stacks arbitrary. Then in at most $4|r| + 1$ steps it
reaches, in some internal state and with some stack contents, the accepting label if $r$ is good
for $cs$, and the rejecting label otherwise.

Formalized by `Cslib.Complexity.Karp.ColVerify.edges_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#edges-run).

## Correctness and time bound of the 3-coloring verifier machine

Let $x$ and $w$ be
bit strings. Start the verifier machine at its start label, with any internal value, with $x$
written as bit symbols on the input stack $X$, $w$ written as bit symbols on the witness stack
$W$, and all other stacks empty. Then within at most $8(|x| + |w| + 1)^3$ steps it reaches the
accepting label if the 3-coloring check accepts $(x, w)$, and the rejecting label otherwise.

The machine in fact runs in linearly many steps; only the cubic bound is stated here.

Formalized by `Cslib.Complexity.Karp.ColVerify.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorVerify.lean, line 799](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorVerify.lean#L799). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#run).

## The 3-COLOR verifier as a host component

The component machine whose stacks are the
seven stacks $X, W, N, P, T, U, V$ of the 3-COLOR verifier machine, listed in that order and each
over the token alphabet of the SAT verifier, and whose labels and program are those of the
3-COLOR verifier machine.

Formalized by `Cslib.Complexity.Karp.colVerifyComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-08/index.html#col-verify-comp).

## 3-COLOR is in NP

**3-COLOR is in NP**.

Formalized by `Cslib.Complexity.Karp.col3Dec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-09/index.html#col3-dec-mem-np).

## The 3-COLOR emitter

The emitter whose stacks, alphabets, labels, program and start label
are those of the 3-COLOR emitter machine, which exits at the machine's final label, reads the
tokens of a CNF formula from stack $T$ and writes its output bits on stack $O$ (both symbol maps
being the identity), and has step bound $B(n) = 500 (n + 1)^4$ for $n$ tokens. Its output for a
CNF formula $\varphi$ is the encoded 3-COLOR instance of $\varphi$, and for an undecodable input
the encoding of the complete graph $K_4$.

Formalized by `Cslib.Complexity.Karp.emitColor`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-09/index.html#emit-color).

## The SAT-to-3-COLOR reduction is polynomial-time

The map on bit strings that sends a
string decoding to a CNF formula $\varphi$ to the encoding of the 3-COLOR instance of $\varphi$,
and every other string to the encoding of the complete graph $K_4$, is computable in polynomial
time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_reduceCol`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-09/index.html#is-poly-time-reduce-col).

## 3-COLOR is NP-hard

Every decision problem in NP reduces to 3-COLOR by a polynomial-time
many-one reduction.

Formalized by `Cslib.Complexity.Karp.col3Dec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-09/index.html#col3-dec-np-hard).

## 3-COLOR is NP-complete

3-COLOR is in NP, and every decision problem in NP reduces to
3-COLOR by a polynomial-time many-one reduction.

Formalized by `Cslib.Complexity.Karp.col3Dec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/ColorComplete.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/ColorComplete.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/part-09/index.html#col3-dec-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph 3-coloring](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-3-coloring)
