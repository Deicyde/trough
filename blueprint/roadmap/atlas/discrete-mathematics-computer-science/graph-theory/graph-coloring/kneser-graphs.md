---
declaration: section
origin: cited
lean: MetaMathlibExt.kneserGraph, MathlibExt.Combinatorics.SimpleGraph.KneserLovaszWanted.kneserGraph_adj_iff, MathlibExt.Combinatorics.SimpleGraph.KneserLovaszWanted.kneser_lovasz
statement: formalized
proof: formalized
---

# Kneser graphs

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs/index.html).

## Kneser graph

For natural numbers $v$ and $k$, the Kneser graph $K_{v:k}$ has as vertices
the $k$-element subsets of the $v$-element set $\{0, 1, \dots, v-1\}$, with two distinct vertices
adjacent when they are disjoint.

By definition, $K_{v:k}$ is the generalized Johnson graph $J(v, k, 0)$.

Formalized by `MetaMathlibExt.kneserGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Kneser.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Kneser.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs/index.html#kneser-graph).

## Adjacency in the Kneser graph

For natural numbers $n$ and $k$ and $k$-element subsets
$x$ and $y$ of $\{0, 1, \dots, n-1\}$, the vertices $x$ and $y$ of the Kneser graph $K(n, k)$
are adjacent if and only if $x$ and $y$ are disjoint and $x \ne y$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.KneserLovaszWanted.kneserGraph_adj_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/KneserLovasz.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/KneserLovasz.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs/index.html#kneser-graph-adj-iff).

## Kneser–Lovász theorem

Let $n$ and $k$ be natural numbers with $0 < k$ and $2k \le n$. The
Kneser graph $K(n, k)$, whose vertices are the $k$-element subsets of $\{0, 1, \dots, n-1\}$ and
in which two such subsets are adjacent when they are disjoint and distinct, has chromatic number
$n - 2k + 2$.

## Sources

- L. Lovasz, JCT A 25 (1978), 319-324, DOI 10.1016/0097-3165(78)90022-5.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.KneserLovaszWanted.kneser_lovasz`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/KneserLovasz.lean, line 3113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/KneserLovasz.lean#L3113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs/index.html#kneser-lovasz).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kneser graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/kneser-graphs)
