---
declaration: section
origin: cited
lean: SimpleGraph.collapseOutside, SimpleGraph.collapseOutside_of_mem, SimpleGraph.collapseOutside_of_notMem, SimpleGraph.collapseOutside_eq_some_iff, SimpleGraph.collapseOutside_eq_none_iff, SimpleGraph.collapseOutside_surjective, SimpleGraph.contractOutside, SimpleGraph.contractOutside_adj_some
statement: formalized
proof: formalized
---

# Fleischner's theorem

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html).

## Collapsing the complement of a set

For a set $D \subseteq V$, the collapse map sends $V$
to $D$ together with one new vertex, the contraction vertex: each $v \in D$ is sent to itself,
and each $v \notin D$ is sent to the contraction vertex.

Formalized by `SimpleGraph.collapseOutside`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside).

## The collapse map fixes the retained set

For a set $D \subseteq V$, the collapse map from
$V$ to $D$ together with the contraction vertex sends each $v \in D$ to $v$ itself.

Formalized by `SimpleGraph.collapseOutside_of_mem`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside-of-mem).

## The collapse map sends the complement to the contraction vertex

For a set
$D \subseteq V$, the collapse map from $V$ to $D$ together with the contraction vertex sends each
vertex $v \notin D$ to the contraction vertex.

Formalized by `SimpleGraph.collapseOutside_of_notMem`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside-of-not-mem).

## Preimages of retained vertices under the collapse map

For a set $D \subseteq V$, a vertex
$v \in V$ and an element $a \in D$, the collapse map from $V$ to $D$ together with the
contraction vertex sends $v$ to $a$ if and only if $v = a$.

Formalized by `SimpleGraph.collapseOutside_eq_some_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside-eq-some-iff).

## Preimage of the contraction vertex under the collapse map

For a set $D \subseteq V$ and a
vertex $v \in V$, the collapse map from $V$ to $D$ together with the contraction vertex sends $v$
to the contraction vertex if and only if $v \notin D$.

Formalized by `SimpleGraph.collapseOutside_eq_none_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside-eq-none-iff).

## The collapse map is surjective

For a set $D \subseteq V$ whose complement $V \setminus D$
is nonempty, the collapse map from $V$ to $D$ together with the contraction vertex is
surjective.

Formalized by `SimpleGraph.collapseOutside_surjective`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#collapse-outside-surjective).

## Contracting the complement of a vertex set

Let $G$ be a simple graph on a vertex set $V$
and let $D \subseteq V$. Contracting the complement of $D$ to a single vertex gives the simple
graph whose vertices are the elements of $D$ together with one new vertex $\ast$, in which two
vertices $a, b \in D$ are adjacent exactly when they are adjacent in $G$, and a vertex $a \in D$
is adjacent to $\ast$ exactly when $a$ has a neighbour in $G$ outside $D$. The new vertex $\ast$
is present even when $D = V$, and is then isolated.

Formalized by `SimpleGraph.contractOutside`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#contract-outside).

## Contraction preserves adjacency among retained vertices

Let $G$ be a graph on $V$, let
$D \subseteq V$, and contract $V \setminus D$ to a single vertex. Two vertices $a, b \in D$ are
adjacent in the contracted graph if and only if they are adjacent in $G$.

Formalized by `SimpleGraph.contractOutside_adj_some`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#contract-outside-adj-some).

## Neighbors of the contraction vertex

Let $G$ be a graph on $V$, let $D \subseteq V$, and
contract $V \setminus D$ to a single vertex. A vertex $a \in D$ is adjacent to the contraction
vertex in the contracted graph if and only if $a$ is adjacent in $G$ to some vertex
$v \notin D$.

Formalized by `SimpleGraph.contractOutside_adj_none`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#contract-outside-adj-none).

## Contracting the complement preserves 2-connectivity

Let $G$ be a 2-vertex-connected
graph on a finite vertex set $V$, and let $D \subseteq V$ be a set with at least two elements
that induces a connected subgraph of $G$ and whose complement $V \setminus D$ is nonempty. Then
the graph obtained from $G$ by contracting $V \setminus D$ to a single vertex is
2-vertex-connected.

Formalized by `SimpleGraph.IsVertexConnected.contractOutside`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#contract-outside-2).

## Cardinality bound for contracting the complement

Let $V$ be a finite set and
$D \subseteq V$. If the complement $V \setminus D$ has at least two elements, then $D$ together
with one new vertex has fewer elements than $V$, that is, $|D| + 1 < |V|$.

This counts the vertices of the graph obtained by contracting $V \setminus D$ to a single
vertex.

Formalized by `SimpleGraph.card_contractOutside_lt`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Contraction.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Contraction.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#card-contract-outside-lt).

## Strong square cycle at a vertex

Let $G$ be a graph on a finite vertex set $V$ and let
$x \in V$. Then $G$ has a strong square cycle at $x$ if the square $G^2$ of $G$ has a Hamiltonian
cycle that starts and ends at $x$ and whose two edges at $x$, its first and its last edge, are
edges of $G$.

Formalized by `SimpleGraph.HasStrongSquareCycle`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/StrongSquareCycle.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StrongSquareCycle.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#has-strong-square-cycle-2).

## Characterization of strong square cycles

Let $G$ be a graph on a finite vertex set $V$
and let $x \in V$. Then $G$ has a strong square cycle at $x$ if and only if the square $G^2$ of
$G$ has a Hamiltonian cycle $p$ that starts and ends at $x$ such that $x$ is adjacent in $G$ to
the second vertex of $p$ and the second-to-last vertex of $p$ is adjacent in $G$ to $x$.

Formalized by `SimpleGraph.hasStrongSquareCycle_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/StrongSquareCycle.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/StrongSquareCycle.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#has-strong-square-cycle-iff).

## Strengthened Fleischner theorem

Let $G$ be a finite simple graph that is
2-vertex-connected, that is, $G$ has at least three vertices and stays connected after deleting at
most one vertex. Let $G^2$ be the square of $G$: the graph on the same vertices in which two
distinct vertices are adjacent if and only if they are adjacent in $G$ or have a common neighbour
in $G$. Then for every vertex $x$ of $G$, the graph $G^2$ has a Hamiltonian cycle whose two edges
at $x$ are edges of $G$.

Formalized by `SimpleGraph.IsVertexConnected.hasStrongSquareCycle`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/FleischnerStrong.lean, line 6724](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/FleischnerStrong.lean#L6724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#has-strong-square-cycle).

## Fleischner's theorem

Let $G$ be a finite simple graph that is 2-vertex-connected, that is,
$G$ has at least three vertices and stays connected after deleting at most one vertex. Let $H$ be
the square of $G$: the graph on the same vertices in which two distinct vertices are adjacent if
and only if they are adjacent in $G$ or have a common neighbour in $G$. Then $H$ is Hamiltonian:
it has a cycle that passes through every vertex exactly once.

## Sources

- Herbert Fleischner, "The Square of Every Two-Connected Graph Is Hamiltonian," Journal of Combinatorial Theory, Series B 16 (1974), 29–34, DOI 10.1016/0095-8956(74)90091-4, https://doi.org/10.1016/0095-8956(74)90091-4. Proof: the strengthened vertex-rooted induction of A. Georgakopoulos, "A short proof of Fleischner's theorem", Discrete Math. 309 (2009), 6632–6634.

Formalized by `MetaMathlibExt.fleischner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Fleischner.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Fleischner.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html#fleischner).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fleischner's theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/fleischner-s-theorem)
