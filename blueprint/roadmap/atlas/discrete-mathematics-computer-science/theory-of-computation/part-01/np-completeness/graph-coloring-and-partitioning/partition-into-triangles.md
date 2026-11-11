---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.PartitionIntoTrianglesInstance, MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.Graph, MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.WellFormed, MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.PartitionIntoTrianglesFeasible, MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.partitionIntoTrianglesDec, MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.partitionIntoTriangles_npComplete
statement: formalized
---

# Partition into triangles

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html).

## Instances of PARTITION INTO TRIANGLES

An instance of PARTITION INTO TRIANGLES is a pair
consisting of a natural number $n$, the number of vertices, and a list of pairs of natural
numbers, the edges.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.PartitionIntoTrianglesInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#partition-into-triangles-instance).

## Graph of a PARTITION INTO TRIANGLES instance

For an instance consisting of a natural number
$n$ and a list $E$ of pairs of natural numbers, its graph is the graph of the edge list $E$ on $n$
vertices: the simple graph on $\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are
adjacent when $(i, j)$ or $(j, i)$ belongs to $E$. Pairs with an endpoint at least $n$ contribute
no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#graph).

## Well-formed PARTITION INTO TRIANGLES instances

An instance consisting of a natural number
$n$ and a list $E$ of pairs of natural numbers is well formed when $E$ has no repeated entries
and every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#well-formed).

## Partition into triangles

An instance consisting of a natural number $n$ and a list $E$ of
pairs of natural numbers admits a partition into triangles when the vertex set
$\{0, \dots, n - 1\}$ can be partitioned into sets of three vertices, any two of which are
adjacent in the graph of $E$ on $n$ vertices.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.PartitionIntoTrianglesFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#partition-into-triangles-feasible).

## PARTITION INTO TRIANGLES as a decision problem

The decision problem PARTITION INTO
TRIANGLES accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to an instance consisting of a natural number $n$ and a list $E$ of pairs of natural
numbers such that $E$ has no repeated entries, every pair $(u, v)$ in $E$ satisfies $u < n$,
$v < n$, $u \ne v$ and $(v, u) \notin E$, and the vertex set $\{0, \dots, n - 1\}$ can be
partitioned into sets of three vertices, any two of which are adjacent in the graph of $E$ on $n$
vertices. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.partitionIntoTrianglesDec`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#partition-into-triangles-dec).

## PARTITION INTO TRIANGLES is NP-complete

The decision problem PARTITION INTO TRIANGLES
lies in NP, and every decision problem in NP has a polynomial-time many-one reduction to
PARTITION INTO TRIANGLES.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), PARTITION INTO TRIANGLES; D. G. Kirkpatrick and P. Hell, "On the complexity of general graph factor problems", SIAM Journal on Computing 12 (1983), 601-609.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.PartitionIntoTriangles.partitionIntoTriangles_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoTrianglesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html#partition-into-triangles-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition into triangles](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-triangles)
