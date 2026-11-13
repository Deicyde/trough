---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected, Cslib.Algorithms.Lean.StronglyConnectedComponents.stronglyConnected_refl, Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected.symm, Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected.trans, Cslib.Algorithms.Lean.StronglyConnectedComponents.stronglyConnectedSetoid, Cslib.Algorithms.Lean.StronglyConnectedComponents.sameComponentB, Cslib.Algorithms.Lean.StronglyConnectedComponents.sameComponentB_eq_true, Cslib.Algorithms.Lean.StronglyConnectedComponents.components
statement: formalized
proof: formalized
---

# Strongly connected components

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html).

## Strongly connected vertices

In a directed adjacency graph $G$, vertices $u$ and $v$ are
strongly connected when $v$ is reachable from $u$ and $u$ is reachable from $v$ in $G$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#strongly-connected).

## Strong connectivity is reflexive

In a directed graph $G$, every vertex is strongly
connected to itself.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.stronglyConnected_refl`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#strongly-connected-refl).

## Strong connectivity is symmetric

In a directed graph $G$, if $u$ is strongly connected to
$v$, then $v$ is strongly connected to $u$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected.symm`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#symm).

## Strong connectivity is transitive

In a directed graph $G$, if $u$ is strongly connected to
$v$ and $v$ is strongly connected to $w$, then $u$ is strongly connected to $w$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.StronglyConnected.trans`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#trans).

## Strong connectivity as an equivalence relation

For a directed graph $G$, the relation on
the vertices of $G$ that holds between $u$ and $v$ exactly when $u$ and $v$ are strongly connected
in $G$, packaged as an equivalence relation.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.stronglyConnectedSetoid`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#strongly-connected-setoid).

## Executable mutual-reachability test

For a directed graph $G$ and vertices $u$ and $v$, the
test returns true exactly when $v$ occurs in the preorder of the depth-first search of $G$ from
the single root $u$, and $u$ occurs in the preorder of the depth-first search of $G$ from the
single root $v$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.sameComponentB`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#same-component-b).

## The mutual-reachability test is correct

For a directed graph $G$ and vertices $u$ and $v$,
the executable mutual-reachability test on $u$ and $v$ returns true if and only if $u$ and $v$ are
strongly connected in $G$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.sameComponentB_eq_true`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#same-component-b-eq-true).

## Strongly connected components algorithm

Let $G$ be a directed graph and let
$v_1, \dots, v_n$ be its vertices in decreasing order of finishing time in a depth-first search of
the whole graph that takes its roots in the vertex order of $G$. For each $i$, let $C_i$ be the
list of those $v_j$, in increasing order of $j$, such that $v_i$ and $v_j$ are strongly connected
(tested by two depth-first searches). The output is the list $C_1, \dots, C_n$ with repeated
blocks removed, keeping the last occurrence of each.

The result is deterministic: within a block, vertices appear in decreasing finish order.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components).

## Computed components are nonempty

For every directed graph $G$, each block returned by the
strongly connected components algorithm on $G$ contains at least one vertex.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components_nonempty`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components-nonempty).

## Computed components have no repeated vertices

For every directed graph $G$, each block
returned by the strongly connected components algorithm on $G$ contains no vertex more than
once.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components-nodup).

## Computed components are pairwise disjoint

For every directed graph $G$, any two blocks at
different positions of the list returned by the strongly connected components algorithm on $G$
have no vertex in common.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components_pairwise_disjoint`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components-pairwise-disjoint).

## The computed components cover the vertex list

For a directed graph $G$ and a vertex
$v$, $v$ belongs to some block of the computed strongly connected components of $G$ if and only
if $v$ occurs in the vertex enumeration of $G$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.mem_flatten_components`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#mem-flatten-components).

## Vertices share a computed component exactly when strongly connected

For a directed graph
$G$ and vertices $u$ and $v$, some block of the computed strongly connected components of $G$
contains both $u$ and $v$ if and only if $u$ and $v$ are strongly connected in $G$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.share_component_iff_stronglyConnected`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#share-component-iff-strongly-connected).

## Each computed component is a full mutual-reachability class

Let $G$ be a directed graph,
let $B$ be one of the blocks returned by the strongly connected components algorithm on $G$, and
let $m$ be a vertex of $B$. Then for every vertex $v$ of $G$, the vertices $m$ and $v$ are strongly
connected (each is reachable from the other) if and only if $v$ lies in $B$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.component_maximal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#component-maximal).

## SCC partition

A list $\mathcal{B}$ of vertex lists is an SCC partition of a directed graph
$G$ when every block of $\mathcal{B}$ is nonempty and contains no vertex twice, blocks at different
positions of $\mathcal{B}$ are disjoint, a vertex lies in some block exactly when it is a vertex of
$G$, two vertices lie in a common block exactly when they are strongly connected (each is
reachable from the other), and for every block $B$, every $m \in B$ and every vertex $v$, the
vertices $m$ and $v$ are strongly connected exactly when $v \in B$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.IsSCCPartition`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#is-sccpartition).

## The computed components form the SCC partition

For every directed graph $G$, the list of
blocks returned by the strongly connected components algorithm on $G$ is an SCC partition of $G$:
every block is nonempty and contains no vertex twice, blocks at different positions of the list
are disjoint, every vertex of $G$ lies in some block, two vertices lie in a common block exactly
when they are strongly connected, and for every vertex $m$ of a block $B$ and every vertex $v$,
the vertices $m$ and $v$ are strongly connected exactly when $v$ lies in $B$.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components_isSCCPartition`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components-is-sccpartition).

## Reachability between components

In a directed graph $G$, a list $S$ of vertices reaches
a list $T$ of vertices when some vertex of $S$ reaches some vertex of $T$ by a directed path in
$G$, possibly of length zero.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.ComponentReaches`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#component-reaches).

## Acyclic condensation

A list $\mathcal{B}$ of vertex lists of a directed graph $G$ has an
acyclic condensation when, for all $S, T \in \mathcal{B}$, if some vertex of $S$ reaches some
vertex of $T$ in $G$ and some vertex of $T$ reaches some vertex of $S$, then $S = T$. That is,
reachability between the blocks is antisymmetric.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.CondensationAcyclic`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#condensation-acyclic).

## The condensation of the computed components is acyclic

Let $G$ be a directed graph and
let $S$ and $T$ be blocks returned by the strongly connected components algorithm on $G$. If some
vertex of $S$ reaches some vertex of $T$ and some vertex of $T$ reaches some vertex of $S$, then
$S = T$.

Equivalently, the condensation relation has no nontrivial directed cycle.

Formalized by `Cslib.Algorithms.Lean.StronglyConnectedComponents.components_condensationAcyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/StronglyConnectedComponents.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html#components-condensation-acyclic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strongly connected components](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/strongly-connected-components)
