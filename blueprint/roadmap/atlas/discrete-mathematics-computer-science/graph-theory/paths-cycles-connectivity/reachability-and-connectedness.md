---
declaration: section
origin: cited
lean: SimpleGraph.exists_parent, SimpleGraph.InternallyDisjoint, SimpleGraph.InfinitelyConnected, SimpleGraph.bfsStep, SimpleGraph.bfsIterate, SimpleGraph.reachableFinset
statement: formalized
proof: formalized
---

# Reachability and connectedness

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html).

## Parent vertex towards a root in a connected graph

In a connected graph every vertex `v ≠ s` has a neighbor `p` one step closer to `s`
(a parent of `v` in a breadth-first tree rooted at `s`).

Formalized by `SimpleGraph.exists_parent`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ConnectedParent.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ConnectedParent.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#exists-parent).

## Internally disjoint walks

Two walks $p$ and $q$ in a simple graph $G$ are internally
disjoint if no vertex is an interior vertex of both, where the interior vertices of a walk are
the entries of its vertex sequence other than the first and the last.

Formalized by `SimpleGraph.InternallyDisjoint`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#internally-disjoint).

## Infinitely connected graphs

A simple graph $G$ is infinitely connected if it has at
least two vertices and, for any two distinct vertices $u$ and $v$, there is an infinite set of
paths from $u$ to $v$ in $G$ that are pairwise internally disjoint.

In particular, a graph with at most one vertex is not infinitely connected.

Formalized by `SimpleGraph.InfinitelyConnected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#infinitely-connected).

## One round of breadth-first search

For a simple graph $G$ on a finite vertex set and a
set $s$ of vertices, this is the set of vertices that lie in $s$ or are adjacent to some vertex
of $s$, that is, $s$ together with all neighbours of its vertices.

Formalized by `SimpleGraph.bfsStep`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#bfs-step).

## Breadth-first search with a round limit

For a simple graph $G$ on a finite vertex set,
a natural number $n$ and a set $s$ of vertices, this applies rounds of breadth-first search to
$s$ (each round adds all neighbours of the current vertices), stopping after $n$ rounds or as
soon as a round adds no new vertex, whichever comes first, and returns the resulting set.

Formalized by `SimpleGraph.bfsIterate`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#bfs-iterate).

## Vertices reachable from a vertex

For a simple graph $G$ on a finite vertex set $V$ and
a vertex $u$, this is the set obtained from $\{u\}$ by breadth-first search with at most $|V|$
rounds, stopping early as soon as a round adds no new vertex.

It consists exactly of the vertices reachable from $u$ in $G$.

Formalized by `SimpleGraph.reachableFinset`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Connectivity.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html#reachable-finset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reachability and connectedness](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/reachability-and-connectedness)
