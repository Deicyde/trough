---
declaration: section
origin: cited
lean: SimpleGraph.IsPhiCenter, SimpleGraph.IsCentered, SimpleGraph.isPhiCenter_iff_existsUnique, SimpleGraph.isPhiCenter_singleton, SimpleGraph.isCentered_of_injective, SimpleGraph.selfColoring_isCentered
statement: formalized
proof: formalized
---

# Centered colorings

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html).

## Center of a vertex set under a coloring

Let $\varphi$ be a proper vertex coloring of a
simple graph $G$, let $s$ be a set of vertices of $G$ and let $v$ be a vertex of $G$. Then $v$ is
a $\varphi$-center of $s$ if $v \in s$ and no other vertex of $s$ has the color $\varphi(v)$.

Formalized by `SimpleGraph.IsPhiCenter`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#is-phi-center).

## Centered coloring

A proper vertex coloring $\varphi$ of a simple graph $G$ is centered
if, for every set $s$ of vertices of $G$ whose induced subgraph is connected, some vertex is a
$\varphi$-center of $s$.

Quantifying over vertex sets whose induced subgraph is connected suffices: adding all induced
edges on the same vertices keeps a connected subgraph connected, and whether a color occurs
exactly once depends only on the vertex set together with the coloring.

Formalized by `SimpleGraph.IsCentered`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#is-centered).

## Centers via unique existence

Let $\varphi$ be a proper vertex coloring of a simple graph
$G$, let $s$ be a set of vertices of $G$ and let $v$ be a vertex of $G$. Then $v$ is a
$\varphi$-center of $s$ if and only if $v \in s$ and there is exactly one vertex $u \in s$ with
$\varphi(u) = \varphi(v)$.

Formalized by `SimpleGraph.isPhiCenter_iff_existsUnique`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#is-phi-center-iff-exists-unique).

## A vertex is a center of its singleton

For every proper vertex coloring $\varphi$ of a
simple graph $G$ and every vertex $v$ of $G$, $v$ is a $\varphi$-center of $\{v\}$.

Formalized by `SimpleGraph.isPhiCenter_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#is-phi-center-singleton).

## Injective colorings are centered

Every injective proper vertex coloring of a simple graph
is centered: any vertex of a set whose induced subgraph is connected is a center of that set.

Formalized by `SimpleGraph.isCentered_of_injective`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#is-centered-of-injective).

## The identity coloring is centered

For every simple graph $G$ with vertex set $V$, the
proper vertex coloring of $G$ by $V$ that gives each vertex itself as its color is centered.

Formalized by `SimpleGraph.selfColoring_isCentered`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CenteredColoring.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html#self-coloring-is-centered).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Centered colorings](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/centered-colorings)
