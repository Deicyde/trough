---
declaration: section
origin: cited
lean: MetaMathlibExt.HasK5Minor, MetaMathlibExt.HasK33Minor, MetaMathlibExt.IsPlanar, MetaMathlibExt.fourColorTheorem
statement: formalized
---

# Four color theorem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html).

## Graphs with a $K_5$ minor

A simple graph $G$ has $K_5$ as a minor if there are five
nonempty, pairwise disjoint sets of vertices $S_1, \dots, S_5$ such that any two vertices in the
same set are joined by a walk in $G$ all of whose vertices lie in that set, and for all distinct
$i, j$ some vertex of $S_i$ is adjacent in $G$ to some vertex of $S_j$.

Together with $K_{3,3}$, this is one of the two forbidden minors for planarity (Wagner,
Kuratowski).

## Sources

- https://en.wikipedia.org/wiki/Four_color_theorem.

Formalized by `MetaMathlibExt.HasK5Minor`, a definition declared in [WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html#has-k5-minor).

## Graphs with a $K_{3,3}$ minor

A simple graph $G$ has $K_{3,3}$ as a minor if there are
six nonempty, pairwise disjoint sets of vertices $L_1, L_2, L_3, R_1, R_2, R_3$ such that any two
vertices in the same set are joined by a walk in $G$ all of whose vertices lie in that set, and
for all $i, j \in \{1, 2, 3\}$ some vertex of $L_i$ is adjacent in $G$ to some vertex of $R_j$.

Together with $K_5$, this is one of the two forbidden minors for planarity (Wagner, Kuratowski).

## Sources

- https://en.wikipedia.org/wiki/Four_color_theorem.

Formalized by `MetaMathlibExt.HasK33Minor`, a definition declared in [WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html#has-k33-minor).

## Planarity by forbidden minors

A simple graph $G$ is called planar here if it has neither
$K_5$ nor $K_{3,3}$ as a minor.

Without this condition the four color theorem fails: $K_5$ is not 4-colorable.

## Sources

- https://en.wikipedia.org/wiki/Four_color_theorem.

Formalized by `MetaMathlibExt.IsPlanar`, a definition declared in [WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html#is-planar).

## Four color theorem

Let $G$ be a simple graph on a finite vertex set $V$ that has neither
$K_5$ nor $K_{3,3}$ as a minor, and let $\ell$ assign a natural number $\ell(u, v)$ to every
ordered pair of vertices $u, v$ such that $u$ and $v$ are adjacent in $G$ if and only if
$u \ne v$ and $\ell(u, v) > 0$. Then $G$ has a proper vertex coloring with four colors.

Here the vertices stand for the regions of a map and $\ell(u, v)$ for the length of their common
boundary, so regions that meet only at a corner are not adjacent. Without the minor condition the
conclusion fails: $K_5$ needs five colors.

## Sources

- https://en.wikipedia.org/wiki/Four_color_theorem.

Stated but not proved: `MetaMathlibExt.fourColorTheorem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Graph/FourColorTheoremWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html#four-color-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Four color theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/four-color-theorem)
