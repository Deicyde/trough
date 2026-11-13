---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsTriangleRamsey, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsTriangleRamseyDeleteVertex, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsRamseyMinimal, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.HasMinDegree, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.sRamsey, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.conjecture, MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.conjecture_holds, MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.IsTriangleTree
statement: formalized
---

# Ramsey graphs for the triangle

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html).

## Ramsey graphs for the triangle

A graph $G$ on the vertex set $\{0, \dots, n - 1\}$ is
$r$-Ramsey for the triangle when every colouring $c$ of the ordered pairs of vertices with $r$
colours that is symmetric ($c(a, b) = c(b, a)$) admits three distinct vertices $u, v, w$ that form
a triangle in $G$ with $c(u, v) = c(v, w) = c(w, u)$.

For $r \ge 1$ this says that every colouring of the edges of $G$ with $r$ colours has a
monochromatic triangle.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsTriangleRamsey`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#is-triangle-ramsey).

## Ramsey property for the triangle after deleting a vertex

Let $G$ be a graph on the vertex
set $\{0, \dots, n - 1\}$, $r$ a natural number and $x$ a vertex. The property holds when every
colouring $c$ of the ordered pairs of vertices with $r$ colours that is symmetric
($c(a, b) = c(b, a)$) admits three distinct vertices $u, v, w$, all different from $x$, that form a
triangle in $G$ with $c(u, v) = c(v, w) = c(w, u)$.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsTriangleRamseyDeleteVertex`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#is-triangle-ramsey-delete-vertex).

## Ramsey-minimal graphs for the triangle

A graph $G$ on the vertex set $\{0, \dots, n - 1\}$
is $r$-Ramsey-minimal for the triangle when $G$ is $r$-Ramsey for the triangle, no proper spanning
subgraph of $G$ (a graph on the same vertices whose edges are edges of $G$, missing at least one
of them) is $r$-Ramsey for the triangle, and for every vertex $x$ it is false that every symmetric
colouring of the ordered pairs of vertices with $r$ colours admits a triangle of $G$ avoiding $x$
whose three edges have the same colour.

Given the first two conditions, the last one says exactly that $G$ has no isolated vertices.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.IsRamseyMinimal`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#is-ramsey-minimal).

## Minimum degree of a finite graph

A graph $G$ on the vertex set $\{0, \dots, n - 1\}$ has
minimum degree $d$ when every vertex of $G$ has at least $d$ neighbours and some vertex of $G$ has
exactly $d$ neighbours; in particular $n \ge 1$.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.HasMinDegree`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#has-min-degree).

## Least minimum degree of Ramsey-minimal graphs for the triangle

For a natural number $r$,
$s_r(K_3)$ is the least natural number $d$ such that, for some $n$, some graph on the vertex set
$\{0, \dots, n - 1\}$ is $r$-Ramsey-minimal for the triangle and has minimum degree $d$; if no
such graph exists, $s_r(K_3) = 0$.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory, Conjecture `$s_r(3) = \Theta(r^2 \log r)$`.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.sRamsey`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#s-ramsey).

## Minimum-degree conjecture for minimal Ramsey graphs of the triangle

The statement that
$s_r(K_3) = \Theta(r^2 \log r)$ as the natural number $r$ tends to infinity, where $s_r(K_3)$ is
the least minimum degree of a graph that is $r$-Ramsey-minimal for the triangle ($0$ if there is
none) and $\log$ is the natural logarithm: there are constants $c, C > 0$ such that
$c \, r^2 \log r \le s_r(K_3) \le C \, r^2 \log r$ for all sufficiently large $r$.

## Sources

- [AIM-COMBINATORICS-0060], `aim-combinatorics-notes.json notes[59]`, Source item 13, Section Ramsey minimal graphs, Workshop Graph Ramsey theory, Canonical tag conjecture.

Formalized by `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#conjecture).

## Minimum degree of minimal Ramsey graphs for the triangle (Guo–Warnke)

Let $s_r(K_3)$ be
the least minimum degree of a graph that is $r$-Ramsey-minimal for the triangle, with
$s_r(K_3) = 0$ if there is no such graph, as defined for the conjecture. Then
$s_r(K_3) = \Theta(r^2 \log r)$ as the natural number $r$ tends to infinity, where $\log$ is the
natural logarithm: there are constants $c, C > 0$ such that
$c \, r^2 \log r \le s_r(K_3) \le C \, r^2 \log r$ for all sufficiently large $r$.

Resolved true: Guo and Warnke (Packing nearly optimal Ramsey R(3,t) graphs, arXiv:1711.05877)
prove this, confirming the conjecture of Fox, Grinshpun, Liebenau, Person and Szabó.

## Sources

- H. Guo and L. Warnke, Packing nearly optimal Ramsey R(3,t) graphs, arXiv:1711.05877, https://arxiv.org/abs/1711.05877.

Stated but not proved: `MathlibExt.Combinatorics.TriangleRamseyMinimalThetaWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRamseyMinimalThetaWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#conjecture-holds).

## Trees of triangles

The trees of triangles on a vertex set $V$ are the graphs on $V$
built recursively as follows. A graph whose edges are exactly the three edges of a triangle on
distinct vertices $a, b, c$ is a tree of triangles. If $H_0$ is a tree of triangles, $xy$ is an
edge of $H_0$, and $z$ is a vertex different from $x$ and $y$ with no neighbours in $H_0$, then
the graph obtained from $H_0$ by joining $z$ to $x$ and to $y$ is a tree of triangles.

## Sources

- AIM-COMBINATORICS-0056, aim-combinatorics-notes.json notes[55]: any graph built recursively by starting with a triangle, and then adding two edges at a time that forms a single new triangle with an existing edge.

Formalized by `MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.IsTriangleTree`, an inductive type declared in [WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#is-triangle-tree).

## Graphs that arrow the triangle

A graph $G$ arrows the triangle in two colours, written
$G \to_2 K_3$, if every colouring of the edges of $G$ with two colours contains a monochromatic
triangle: three distinct pairwise adjacent vertices whose three edges all have the same colour.

## Sources

- AIM-COMBINATORICS-0056, aim-combinatorics-notes.json notes[55]: `G` with `2` colors arrows `K₃`, i.e. every 2-coloring of the edges of `G` contains a monochromatic triangle.

Formalized by `MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.Ramseys2Triangle`, a definition declared in [WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#ramseys2-triangle).

## Graphs that are locally trees of triangles

A graph $G$ on a vertex set $V$ is locally a
tree of triangles on $\ell$ vertices if for every set $S$ of exactly $\ell$ vertices there is a
tree of triangles on $V$ that contains every edge of $G$ with both endpoints in $S$.

## Sources

- AIM-COMBINATORICS-0056, aim-combinatorics-notes.json notes[55]: on every `ℓ` vertices `G` induces a subgraph of a tree of triangles.

Formalized by `MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.IsLocallyTriangleTree`, a definition declared in [WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#is-locally-triangle-tree).

## Rödl's question on Ramsey graphs that are locally trees of triangles

This is the
statement that for every natural number $\ell$ there is a finite graph $G$ with at least $\ell$
vertices such that $G \to_2 K_3$ (every colouring of the edges of $G$ with two colours contains
a monochromatic triangle) and $G$ is locally a tree of triangles on $\ell$ vertices: for every
set $S$ of exactly $\ell$ vertices of $G$, some tree of triangles on the vertex set of $G$
contains every edge of $G$ with both endpoints in $S$.

Posed as an open question, it has been answered in the affirmative.

## Sources

- AIM-COMBINATORICS-0056, aim-combinatorics-notes.json notes[55]: for every `ℓ`, does there exist a graph `G →₂ K₃` which on every `ℓ` vertices induces a subgraph of a tree of triangles.

Formalized by `MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#conjecture-2).

## Ramsey graphs for the triangle that are locally trees of triangles

For every natural number
$\ell$ there is a finite graph $G$ with at least $\ell$ vertices such that $G \to_2 K_3$, that is,
every colouring of the edges of $G$ with two colours contains a monochromatic triangle, and such
that for every set $S$ of exactly $\ell$ vertices of $G$, some tree of triangles on the vertex set
of $G$ contains every edge of $G$ with both endpoints in $S$.

This follows from Reiher and Rödl's girth Ramsey theorem (Theorem 1.6 with $F = K_3$, $r = 2$,
$n = \ell$), which gives a graph $H$ with $H \to_2 K_3$ in which every set of at most $\ell$
vertices induces a partial $K_3$-forest; such graphs have treewidth at most $2$, hence lie in
trees of triangles ($2$-trees).

## Sources

- C. Reiher and V. Rödl, The girth Ramsey theorem, arXiv:2308.15589, https://arxiv.org/abs/2308.15589.

Stated but not proved: `MathlibExt.Combinatorics.TriangleTreeLocalRamseyWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleTreeLocalRamseyWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramsey graphs for the triangle](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-ramsey-theory/ramsey-graphs-for-the-triangle)
