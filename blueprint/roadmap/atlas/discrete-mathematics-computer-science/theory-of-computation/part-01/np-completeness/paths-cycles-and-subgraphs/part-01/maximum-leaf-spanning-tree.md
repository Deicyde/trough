---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.MaximumLeafSpanningTreeInstance, MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.MaximumLeafSpanningTreeFeasible, MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.maximumLeafSpanningTreeDec, MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.maximumLeafSpanningTree_npComplete
statement: formalized
---

# Maximum leaf spanning tree

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html).

## Instances of MAXIMUM LEAF SPANNING TREE

An instance of MAXIMUM LEAF SPANNING TREE is a
triple $(n, es, K)$ of a natural number $n$ (the number of vertices), a list $es$ of pairs of
natural numbers (the edge list) and a natural number $K$ (the bound on the number of leaves).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.MaximumLeafSpanningTreeInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html#maximum-leaf-spanning-tree-instance).

## Well-formed MAXIMUM LEAF SPANNING TREE instances

An instance $(n, es, K)$ of MAXIMUM LEAF
SPANNING TREE is well formed when $n > 0$, the list $es$ has no repeated entries, and every entry
$(u, v)$ of $es$ satisfies $u < n$, $v < n$ and $u \ne v$, and $(v, u)$ is not an entry of
$es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html#well-formed).

## Feasible MAXIMUM LEAF SPANNING TREE instances

An instance $(n, es, K)$ of MAXIMUM LEAF
SPANNING TREE is feasible when there are a sublist $T$ of $es$ (a list obtained from $es$ by
deleting entries) with no repeated entries and exactly $n - 1$ entries, and a set $L$ of at least
$K$ vertices in $\{0, \dots, n - 1\}$, such that the simple graph on $\{0, \dots, n - 1\}$ in
which distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ is an entry of $T$ is
connected, and each vertex in $L$ is an endpoint of exactly one entry of $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.MaximumLeafSpanningTreeFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html#maximum-leaf-spanning-tree-feasible).

## The decision problem MAXIMUM LEAF SPANNING TREE

The decision problem MAXIMUM LEAF
SPANNING TREE accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding of instances, to an instance $(n, es, K)$ of MAXIMUM LEAF SPANNING TREE that is well
formed and feasible (its graph has a spanning tree with at least $K$ leaves). Bitstrings that do
not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.maximumLeafSpanningTreeDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html#maximum-leaf-spanning-tree-dec).

## MAXIMUM LEAF SPANNING TREE is NP-complete

The decision problem MAXIMUM LEAF SPANNING TREE
belongs to NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MAXIMUM LEAF SPANNING TREE.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaximumLeafSpanningTree.maximumLeafSpanningTree_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumLeafSpanningTreeWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html#maximum-leaf-spanning-tree-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum leaf spanning tree](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-leaf-spanning-tree)
