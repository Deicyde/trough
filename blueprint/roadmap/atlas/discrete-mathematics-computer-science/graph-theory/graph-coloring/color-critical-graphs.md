---
declaration: section
origin: cited
lean: SimpleGraph.IsCriticalEdges, SimpleGraph.IsCriticalEdge, SimpleGraph.Subgraph.IsCriticalVerts, SimpleGraph.Subgraph.IsCriticalVertex, SimpleGraph.IsCritical, SimpleGraph.Cocolorable, SimpleGraph.Colorable.cocolorable, SimpleGraph.cocolorable_of_fintype
statement: formalized
proof: formalized
---

# Color-critical graphs

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html).

## Critical edge sets

Let $G$ be a graph and $S$ a set of unordered pairs of its
vertices. Then $S$ is critical for $G$ if deleting the edges of $G$ that lie in $S$ strictly
lowers the chromatic number, as an element of $\mathbb{N} \cup \{\infty\}$.

Formalized by `SimpleGraph.IsCriticalEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-critical-edges).

## Critical edge

For a graph $G$ and an unordered pair $e$ of vertices, $e$ is a critical
edge of $G$ if removing $e$ from the edge set of $G$ strictly lowers the chromatic number of $G$,
taken in $\mathbb{N} \cup \{\infty\}$.

Only edges of $G$ can be critical.

Formalized by `SimpleGraph.IsCriticalEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-critical-edge).

## Critical vertex sets of a subgraph

Let $G'$ be a subgraph of a graph $G$. A set $S$ of
vertices is critical for $G'$ if deleting the vertices in $S$ from $G'$ strictly lowers the
chromatic number of $G'$, viewed as a graph on its own vertex set, with chromatic numbers taken
in $\mathbb{N} \cup \{\infty\}$.

Formalized by `SimpleGraph.Subgraph.IsCriticalVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-critical-verts).

## Critical vertices of a subgraph

Let $G'$ be a subgraph of a graph $G$. A vertex $v$ is
critical for $G'$ if $\{v\}$ is a critical vertex set of $G'$, that is, deleting $v$ from $G'$
strictly lowers the chromatic number of $G'$, viewed as a graph on its own vertex set, with
chromatic numbers taken in $\mathbb{N} \cup \{\infty\}$.

Formalized by `SimpleGraph.Subgraph.IsCriticalVertex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-critical-vertex).

## Vertex-critical graphs

Let $k$ be a natural number. A graph $G$ is $k$-critical (or
vertex-critical) if its chromatic number equals $k$ and every vertex $v$ of $G$ is critical,
that is, deleting $v$ from $G$ strictly lowers the chromatic number.

Formalized by `SimpleGraph.IsCritical`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-critical).

## Cocolorable graphs

A graph $G$ is cocolorable with $n$ colors if there is a map from its
vertices to the colors $\{0, \dots, n-1\}$ such that each color class induces either an
independent set or a complete graph in $G$.

Formalized by `SimpleGraph.Cocolorable`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cocolorable).

## Colorable graphs are cocolorable

For every natural number $n$, if a graph $G$ has a
proper coloring with $n$ colors, then $G$ is cocolorable with $n$ colors.

Each color class of a proper coloring induces an independent set.

Formalized by `SimpleGraph.Colorable.cocolorable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cocolorable-2).

## Finite graphs are cocolorable

Every graph $G$ on a finite vertex set $V$ is cocolorable
with $|V|$ colors.

Giving every vertex its own color is a proper coloring.

Formalized by `SimpleGraph.cocolorable_of_fintype`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cocolorable-of-fintype).

## Cochromatic number

The cochromatic number of a graph $G$, an element of
$\mathbb{N} \cup \{\infty\}$, is the least natural number $n$ such that $G$ is cocolorable with
$n$ colors, that is, the least number of colors in a coloring of the vertices of $G$ in which
each color class induces either an independent set or a complete graph. It is $\infty$ exactly
when $G$ is not cocolorable with any finite number of colors.

Formalized by `SimpleGraph.cochromaticNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cochromatic-number).

## Cochromatic number as a minimum

If a graph $G$ is cocolorable with $n$ colors for some
natural number $n$, then the cochromatic number of $G$ equals the least natural number $m$ such
that $G$ is cocolorable with $m$ colors.

Formalized by `SimpleGraph.Cocolorable.cochromaticNumber_eq_sInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cochromatic-number-eq-s-inf).

## Cochromatic number of a finite graph

For every graph $G$ on a finite vertex set, the
cochromatic number of $G$, converted from $\mathbb{N} \cup \{\infty\}$ to $\mathbb{N}$ by sending
$\infty$ to $0$, equals the least natural number $m$ such that $G$ is cocolorable with $m$
colors.

Formalized by `SimpleGraph.cochromaticNumber_toNat_eq_sInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cochromatic-number-to-nat-eq-s-inf).

## Chromatic cardinal of a graph

The chromatic cardinal is the minimal number of colors need to color it. In contrast to
`chromaticNumber`, which assigns `⊤ : ℕ∞` to all non-finitely colorable graphs, this definition
returns a `Cardinal` and can therefore distinguish between different infinite chromatic numbers.

Formalized by `SimpleGraph.chromaticCardinal`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#chromatic-cardinal-of-a-graph).

## Largest union of independent sets

For a graph $G$ on a finite vertex set and a
natural number $k$, this is the maximum number of vertices in a union of $k$ (possibly empty,
possibly overlapping) independent sets of $G$.

Formalized by `SimpleGraph.indepNumK`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#indep-num-k).

## CDS-colorable graphs

A graph $G$ on a finite vertex set is CDS-colorable if it has a
proper coloring $C$ with colors in $\mathbb{N}$ such that for every $k \in \mathbb{N}$, the number
of vertices whose color under $C$ is less than $k$ equals the maximum size of a union of $k$
independent sets of $G$.

Formalized by `SimpleGraph.CDSColorable`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#cdscolorable).

## Rainbow homomorphisms

Let $f$ be a graph homomorphism from $H$ to $G$ and let $c$ be a
labeling of the edges of $G$ by elements of a type $K$. Then $f$ is rainbow for $c$ if distinct
edges of $H$ are mapped to edges of $G$ with distinct labels, that is, the labeling
$e \mapsto c(f(e))$ of the edges of $H$ is injective.

Formalized by `SimpleGraph.IsRainbow`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#is-rainbow).

## Anti-Ramsey number

For a graph $H$ on a finite vertex type and a natural number $n$, the
anti-Ramsey number $\mathrm{AR}(n, H)$ is the largest $k$ for which there is a coloring of the edges
of the complete graph $K_n$ on $\{0, \dots, n-1\}$ with colors $\{0, \dots, k-1\}$, every color
used, that contains no rainbow copy of $H$. Here a copy of $H$ is an injective homomorphism from
$H$ to $K_n$, and it is rainbow when distinct edges of $H$ are sent to edges of distinct colors.
If no such $k$ exists, $\mathrm{AR}(n, H) = 0$.

Formalized by `SimpleGraph.antiRamseyNum`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Coloring/Vertex.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html#anti-ramsey-num).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Color-critical graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/color-critical-graphs)
