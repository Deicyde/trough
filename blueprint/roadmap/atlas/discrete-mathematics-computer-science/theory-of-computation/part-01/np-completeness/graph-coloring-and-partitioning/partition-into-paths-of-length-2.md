---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.PartitionIntoP3sInstance, MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.Graph, MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.WellFormed, MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.PartitionIntoP3sFeasible, MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.partitionIntoP3sDec, MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.partitionIntoP3s_npComplete
statement: formalized
---

# Partition into paths of length 2

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html).

## Instances of PARTITION INTO PATHS OF LENGTH 2

An instance of PARTITION INTO PATHS OF
LENGTH 2 is a pair $(n, E)$ of a natural number $n$, the number of vertices, and a finite list
$E$ of pairs of natural numbers, the edge list.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.PartitionIntoP3sInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#partition-into-p3s-instance).

## Graph of a PARTITION INTO PATHS OF LENGTH 2 instance

For an instance $(n, E)$, the graph
of the instance is the simple graph on the vertex set $\{0, \dots, n - 1\}$ in which distinct
vertices $u$ and $v$ are adjacent exactly when $(u, v)$ or $(v, u)$ belongs to $E$. Pairs in $E$
with an entry at least $n$, and pairs $(u, u)$, contribute no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#graph).

## Well-formed PARTITION INTO PATHS OF LENGTH 2 instances

An instance $(n, E)$ is well
formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$ and $u \ne v$, and the reversed pair $(v, u)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#well-formed).

## Partitions into paths of length 2

An instance $(n, E)$ admits a partition into paths of
length 2 when there is a list of triples, each a list of three distinct vertices from
$\{0, \dots, n - 1\}$, such that every vertex occurs exactly once among all the triples taken
together, and every triple contains pairwise distinct vertices $x$, $y$, $z$ such that $x$ is
adjacent to $y$ and $y$ is adjacent to $z$ in the graph of the instance.

The path need not be induced: a triple spanning a triangle qualifies.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.PartitionIntoP3sFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#partition-into-p3s-feasible).

## PARTITION INTO PATHS OF LENGTH 2

The decision problem PARTITION INTO PATHS OF LENGTH 2
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
instances, to an instance $(n, E)$ that is well formed and admits a partition into paths of
length 2. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.partitionIntoP3sDec`, a definition declared in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#partition-into-p3s-dec).

## PARTITION INTO PATHS OF LENGTH 2 is NP-complete

The decision problem PARTITION INTO PATHS
OF LENGTH 2 belongs to NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), PARTITION INTO PATHS; M. E. Dyer and A. M. Frieze, "On the complexity of partitioning graphs into connected subgraphs", Discrete Applied Mathematics 10 (1985), 139-153.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.PartitionIntoP3s.partitionIntoP3s_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PartitionIntoP3sWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html#partition-into-p3s-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition into paths of length 2](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/partition-into-paths-of-length-2)
