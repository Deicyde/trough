---
declaration: section
origin: cited
lean: SimpleGraph.maximalCliqueSizes, SimpleGraph.trianglesContaining
statement: formalized
proof: formalized
---

# Maximal cliques and triangles

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/maximal-cliques-and-triangles/index.html).

## Sizes of maximal cliques

For a simple graph $G$, this is the set of natural numbers $k$
such that some finite clique of $G$ with exactly $k$ vertices is maximal under inclusion among
the finite cliques of $G$, that is, no finite clique of $G$ strictly contains it.

An infinite maximal clique of $G$ contributes no size to this set.

Formalized by `SimpleGraph.maximalCliqueSizes`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Clique.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Clique.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/maximal-cliques-and-triangles/index.html#maximal-clique-sizes).

## Triangles containing an edge

For a simple graph $G$ on a finite vertex set and an edge
$uv$ of $G$, this is the finite set of triangles of $G$ that contain the edge $uv$, where a
triangle is the vertex set of a $3$-clique of $G$; that is, the $3$-cliques of $G$ containing
both $u$ and $v$.

Formalized by `SimpleGraph.trianglesContaining`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Clique.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Clique.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/maximal-cliques-and-triangles/index.html#triangles-containing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximal cliques and triangles](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/maximal-cliques-and-triangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/independence-and-domination/maximal-cliques-and-triangles)
