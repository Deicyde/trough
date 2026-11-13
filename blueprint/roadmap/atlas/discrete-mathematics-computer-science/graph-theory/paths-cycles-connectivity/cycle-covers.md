---
declaration: section
origin: cited
lean: SimpleGraph.Cycle, SimpleGraph.Cycle.edges, SimpleGraph.Cycle.length, SimpleGraph.IsCycleCover, SimpleGraph.totalLength
statement: formalized
proof: formalized
---

# Cycle covers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html).

## Cycles in a graph

A cycle in a simple graph $G$ consists of a base vertex $v$ of $G$
together with a closed walk $v = v_0, v_1, \dots, v_n = v$ in $G$ such that $n \ge 1$, the $n$
edges $v_{k-1} v_k$ of the walk are pairwise distinct, and the vertices $v_1, \dots, v_n$ are
pairwise distinct. In a simple graph this forces $n \ge 3$.

The base vertex and the direction of traversal are part of the data, so a single cycle subgraph
of $G$ arises from several such cycles.

Formalized by `SimpleGraph.Cycle`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html#cycle).

## Edges of a cycle

The edges of a cycle $c$ in a simple graph form the list of the edges of
its closed walk, in the order in which $c$ traverses them starting from its base vertex; each edge
is the unordered pair of its two endpoints.

Formalized by `SimpleGraph.Cycle.edges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html#edges).

## Length of a cycle

The length of a cycle in a simple graph is the number of edges of its
closed walk.

Formalized by `SimpleGraph.Cycle.length`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html#length).

## Cycle covers

Let $G$ be a finite simple graph. A finite multiset $C$ of cycles in $G$ is a
cycle cover of $G$ when every edge of $G$ is an edge of at least one cycle in $C$.

Formalized by `SimpleGraph.IsCycleCover`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html#is-cycle-cover).

## Total length of a multiset of cycles

The total length of a finite multiset $C$ of cycles in
a simple graph is the sum of the lengths of the cycles in $C$, each counted with its multiplicity.

Formalized by `SimpleGraph.totalLength`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CycleCover.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html#total-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cycle covers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/cycle-covers)
