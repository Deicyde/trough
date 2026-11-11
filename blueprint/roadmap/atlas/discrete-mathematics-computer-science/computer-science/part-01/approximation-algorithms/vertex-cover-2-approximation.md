---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.vertexCoverScan, Cslib.Algorithms.Lean.TimeM.approxVertexCover, Cslib.Algorithms.Lean.TimeM.vertexCoverScan_time, Cslib.Algorithms.Lean.TimeM.approxVertexCover_time, Cslib.Algorithms.Lean.TimeM.subset_vertexCoverScan, Cslib.Algorithms.Lean.TimeM.approxVertexCover_covers, Cslib.Algorithms.Lean.TimeM.approxVertexCover_isVertexCover, Cslib.Algorithms.Lean.TimeM.card_vertexCoverScan_le
statement: formalized
proof: formalized
---

# Vertex cover 2-approximation

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html).

## Vertex cover scan

Given a finite set $C$ of vertices and a list of pairs of vertices,
the scan processes the pairs in order, starting from the cover $C$ and charging one time unit
per pair. A pair $(u, v)$ is covered when $u$ or $v$ is already in the current cover; a covered
pair is skipped, and an uncovered pair adds both $u$ and $v$ to the cover. The scan returns the
cover reached after the last pair.

Formalized by `Cslib.Algorithms.Lean.TimeM.vertexCoverScan`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#vertex-cover-scan).

## APPROX-VERTEX-COVER

Given a list $L$ of ordered pairs of vertices, APPROX-VERTEX-COVER
starts from the empty cover and goes through $L$ in order: a pair $(u, v)$ with $u$ or $v$ already
in the cover is skipped, and otherwise both $u$ and $v$ are added to the cover. It returns the
final cover, a finite set of vertices, at a cost of one unit per pair of $L$.

CLRS (third edition, Section 35.1) takes an arbitrary uncovered edge at each step; here it is the
first uncovered pair in list order.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover).

## Running time of the vertex cover scan

For every finite set $C$ of vertices and every list
$L$ of pairs of vertices, the running time of the vertex cover scan starting from $C$ on $L$ is
the length of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.vertexCoverScan_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#vertex-cover-scan-time).

## Running time of APPROX-VERTEX-COVER

For every list $L$ of ordered pairs of vertices, the
cost of APPROX-VERTEX-COVER on $L$ is the length of $L$: one unit per listed pair.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover-time).

## The vertex cover scan only adds vertices

For every finite set $C$ of vertices and every
list of pairs of vertices, the cover returned by the vertex cover scan starting from $C$ on that
list contains $C$.

Formalized by `Cslib.Algorithms.Lean.TimeM.subset_vertexCoverScan`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#subset-vertex-cover-scan).

## APPROX-VERTEX-COVER covers every listed pair

For every list $L$ of ordered pairs of
vertices and every pair $(u, v)$ in $L$, the cover that APPROX-VERTEX-COVER returns on $L$
contains $u$ or $v$.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover_covers`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover-covers).

## APPROX-VERTEX-COVER returns a vertex cover

Let $G$ be a simple graph and $L$ a list of
ordered pairs of vertices such that for every edge $uv$ of $G$, $(u, v)$ or $(v, u)$ is in $L$.
Then the cover that APPROX-VERTEX-COVER returns on $L$ is a vertex cover of $G$.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover_isVertexCover`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover-is-vertex-cover).

## Counting invariant of the vertex cover scan

Let $G$ be a simple graph, $S$ a vertex cover
of $G$, $C_0$ a finite set of vertices with $|C_0| \le 2|C_0 \cap S|$, and $L$ a list of ordered
pairs of vertices such that $u$ and $v$ are adjacent in $G$ for every $(u, v)$ in $L$. Then the
cover $C$ that the vertex cover scan returns on $L$ starting from $C_0$ satisfies
$|C| \le 2|C \cap S|$.

The invariant holds because each taken edge adds two new vertices, at least one of them in $S$.

Formalized by `Cslib.Algorithms.Lean.TimeM.card_vertexCoverScan_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#card-vertex-cover-scan-le).

## APPROX-VERTEX-COVER is at most twice any vertex cover

Let $G$ be a simple graph and $L$ a
list of ordered pairs of vertices such that $u$ and $v$ are adjacent in $G$ for every $(u, v)$ in
$L$. Then for every vertex cover $S$ of $G$, finite or infinite, the cover $C$ that
APPROX-VERTEX-COVER returns on $L$ satisfies $|C| \le 2|S|$, with sizes in
$\mathbb{N} \cup \{\infty\}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.card_approxVertexCover_le_two_mul`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#card-approx-vertex-cover-le-two-mul).

## APPROX-VERTEX-COVER is a 2-approximation

Let $G$ be a simple graph and $L$ a list of
ordered pairs of vertices that lists exactly the edges of $G$, each in at least one orientation:
$u$ and $v$ are adjacent in $G$ for every $(u, v)$ in $L$, and for every edge $uv$ of $G$,
$(u, v)$ or $(v, u)$ is in $L$. Then the cover $C$ that APPROX-VERTEX-COVER returns on $L$ is a
vertex cover of $G$ and $|C| \le 2\tau(G)$, where $\tau(G) \in \mathbb{N} \cup \{\infty\}$ is the
vertex cover number of $G$, the minimum size of a vertex cover of $G$.

## Sources

- CLRS, third edition, Theorem 35.1.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover_two_approximation`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover-two-approximation).

## Vertex-disjoint pairs

Two pairs $(a, b)$ and $(c, d)$ of vertices are vertex-disjoint
when they share no endpoint: $a \ne c$, $a \ne d$, $b \ne c$ and $b \ne d$.

Formalized by `Cslib.Algorithms.Lean.TimeM.VertexDisjoint`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#vertex-disjoint).

## Matching invariant of the vertex cover scan

Let $G$ be a simple graph, $C_0$ a finite set
of vertices, and $L$ a list of ordered pairs of vertices such that $u$ and $v$ are adjacent in $G$
for every $(u, v)$ in $L$, and let $C$ be the cover that the vertex cover scan returns on $L$
starting from $C_0$. Then there is a sublist $A$ of $L$ such that neither endpoint of any pair in
$A$ lies in $C_0$, pairs at different positions of $A$ are vertex-disjoint, a vertex lies in $C$
exactly when it lies in $C_0$ or is an endpoint of some pair in $A$, and $|C| = |C_0| + 2|A|$,
where $|A|$ is the length of $A$.

Formalized by `Cslib.Algorithms.Lean.TimeM.exists_matching_vertexCoverScan`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#exists-matching-vertex-cover-scan).

## The edges APPROX-VERTEX-COVER takes form a maximal matching of the listed pairs

Let $G$
be a simple graph and $L$ a list of ordered pairs of vertices such that $u$ and $v$ are adjacent
in $G$ for every $(u, v)$ in $L$, and let $C$ be the cover that APPROX-VERTEX-COVER returns on
$L$. Then there is a sublist $A$ of $L$ such that pairs at different positions of $A$ are
vertex-disjoint, every pair in $L$ shares an endpoint with some pair in $A$, a vertex lies in $C$
exactly when it is an endpoint of some pair in $A$, and $|C| = 2|A|$, where $|A|$ is the length of
$A$.

Formalized by `Cslib.Algorithms.Lean.TimeM.approxVertexCover_matching`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/VertexCover.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html#approx-vertex-cover-matching).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vertex cover 2-approximation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/approximation-algorithms/vertex-cover-2-approximation)
