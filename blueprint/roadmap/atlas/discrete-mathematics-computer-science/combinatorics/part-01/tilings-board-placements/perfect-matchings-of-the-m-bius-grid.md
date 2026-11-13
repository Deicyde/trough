---
declaration: section
origin: cited
lean: MetaMathlibExt.MobiusGridVertex, MetaMathlibExt.MobiusGridEdge, MetaMathlibExt.MobiusGridIncident, MetaMathlibExt.IsMobiusGridPerfectMatching, MetaMathlibExt.mobiusGridPerfectMatchingCount, MetaMathlibExt.lu_wu_mobius_grid_perfect_matching_count
statement: formalized
---

# Perfect matchings of the Möbius grid

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html).

## Vertices of the Möbius grid

For natural numbers $M$ and $N$, the vertices of the
$2M \times N$ Möbius grid are the pairs $(a, b)$ of natural numbers with $a < 2M$ and $b < N$.

Formalized by `MetaMathlibExt.MobiusGridVertex`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#mobius-grid-vertex).

## Edges of the Möbius grid

For natural numbers $M$ and $N$, the labeled edges of the
$2M \times N$ Möbius grid are of three kinds: a horizontal edge $h(i, j)$ for each row $i < 2M$
and column $j < N - 1$, a vertical edge $v(i, j)$ for each row $i < 2M - 1$ and column $j < N$,
and a seam edge $\sigma(i)$ for each row $i < 2M$.

Edges with different labels are different, even when small dimensions make two of them join the
same pair of vertices; this keeps the edge-labeled dimer multiplicities of the source.

Formalized by `MetaMathlibExt.MobiusGridEdge`, an inductive type declared in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#mobius-grid-edge).

## Incidence in the Möbius grid

For natural numbers $M$ and $N$, write a vertex of the
$2M \times N$ Möbius grid as $(a, b)$ with row $a < 2M$ and column $b < N$. The vertex $(a, b)$
is incident to the horizontal edge $h(i, j)$ (with $i < 2M$, $j < N - 1$) exactly when $a = i$
and $b \in \{j, j + 1\}$; to the vertical edge $v(i, j)$ (with $i < 2M - 1$, $j < N$) exactly
when $b = j$ and $a \in \{i, i + 1\}$; and to the seam edge $\sigma(i)$ (with $i < 2M$) exactly
when $(a, b) = (i, N - 1)$ or $(a, b) = (2M - 1 - i, 0)$.

Formalized by `MetaMathlibExt.MobiusGridIncident`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#mobius-grid-incident).

## Perfect matchings of the Möbius grid

For natural numbers $M$ and $N$, a finite set $S$
of labeled edges of the $2M \times N$ Möbius grid is a perfect matching when every vertex of the
grid is incident to exactly one edge of $S$.

Formalized by `MetaMathlibExt.IsMobiusGridPerfectMatching`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#is-mobius-grid-perfect-matching).

## Number of perfect matchings of the Möbius grid

For natural numbers $M$ and $N$, this is
the number of perfect matchings of the $2M \times N$ Möbius grid, counted as sets of labeled
edges.

Formalized by `MetaMathlibExt.mobiusGridPerfectMatchingCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#mobius-grid-perfect-matching-count).

## Lu–Wu formula for perfect matchings of the Möbius grid

Let $M \ge 1$ and let $N \ge 1$
be odd. Then the number of perfect matchings of the $2M \times N$ Möbius grid equals

$$
\operatorname{Re}\Big[(1 - i) \prod_{s=1}^{M} \prod_{r=1}^{N}
\Big(2i\,(-1)^{M+s+1} \sin\frac{(4r-1)\pi}{2N} + 2\cos\frac{s\pi}{2M+1}\Big)\Big].
$$

This is the unweighted formula for an odd number of columns.

Stated but not proved: `MetaMathlibExt.lu_wu_mobius_grid_perfect_matching_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuWuMobiusGridWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html#lu-wu-mobius-grid-perfect-matching-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect matchings of the Möbius grid](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/tilings-board-placements/perfect-matchings-of-the-m-bius-grid)
