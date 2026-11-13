---
declaration: section
origin: cited
lean: MetaMathlibExt.latticeCell, MetaMathlibExt.faceAdjacent, MetaMathlibExt.isPolycubeCells, MetaMathlibExt.isCanonicalCells, MetaMathlibExt.properDimension, MetaMathlibExt.fixedPolycube, MetaMathlibExt.fixedPolycubeCount, MetaMathlibExt.properFixedPolycube
statement: formalized
proof: formalized
---

# Fixed polycubes

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html).

## Lattice cells

For a natural number $d$, a lattice cell in dimension $d$ is a point of
$\mathbb{Z}^d$, that is, a function assigning an integer to each of the $d$ coordinate axes.

## Sources

- Sebastian Luther and Stephan Mertens, *The Perimeter of Proper Polycubes*, Journal of Integer Sequences 20 (2017), Article 17.9.5, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Mertens/mert4.tex>: a `d`-dimensional polycube is a set of face-connected cells in `ℤ^d`, lines 115–117 (also arXiv:1705.03688v1).

Formalized by `MetaMathlibExt.latticeCell`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#lattice-cell).

## Face adjacency of lattice cells

Two lattice cells $x, y \in \mathbb{Z}^d$ are face
adjacent when there is an axis $k$ such that $x_j = y_j$ for every axis $j \ne k$ and
$|x_k - y_k| = 1$.

## Sources

- Luther–Mertens, JIS 20 (2017), Article 17.9.5, lines 277–279: this is the "neighbors in the polycube" relation underlying the adjacency graph, in which two vertices are connected if the corresponding cells are neighbors.

Formalized by `MetaMathlibExt.faceAdjacent`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#face-adjacent).

## Polycube

A finite set $S$ of lattice cells in $\mathbb{Z}^d$ is a polycube when it is
nonempty and any two cells $x, y \in S$ are joined by a finite sequence of cells of $S$, starting
at $x$ and ending at $y$, in which consecutive cells are face adjacent.

## Sources

- Luther–Mertens, JIS 20 (2017), Article 17.9.5, lines 115–117: a `d`-dimensional polycube is a set of face-connected cells in `ℤ^d`. Connectivity is expressed by reflexive transitive closure of face adjacency restricted to the set `S`.

Formalized by `MetaMathlibExt.isPolycubeCells`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#is-polycube-cells).

## Canonical position of a cell set

A finite set $S$ of lattice cells in $\mathbb{Z}^d$ is
in canonical position when, for every axis $k$, every cell $x \in S$ has $x_k \ge 0$ and some
cell $x \in S$ has $x_k = 0$; that is, the minimum of each coordinate over $S$ is $0$.

## Sources

- Luther–Mertens, JIS 20 (2017), Article 17.9.5, lines 115–117: fixed polycubes are identified up to translation. Each class has a unique representative with minima at zero. Only translations are quotiented, so rotations and reflections stay distinct orientations.

Formalized by `MetaMathlibExt.isCanonicalCells`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#is-canonical-cells).

## Proper dimension

The proper dimension of a finite set $S$ of lattice cells in
$\mathbb{Z}^d$ is the number of axes $k$ on which $S$ varies, that is, for which there are
cells $x, y \in S$ with $x_k \ne y_k$.

## Sources

- Luther–Mertens, JIS 20 (2017), Article 17.9.5, lines 160–162: a polycube spanning `i` dimensions is proper in `i` dimensions. Asinowski–Barequet–Barequet–Rote, *Proper n-Cell Polycubes in n−3 Dimensions*, Journal of Integer Sequences 15 (2012), Article 12.8.4, lines 171–172: proper dimension is the dimension of the convex hull of cell centers, which for axis-aligned cells equals the count of varying axes.

Formalized by `MetaMathlibExt.properDimension`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#proper-dimension).

## Fixed polycubes

For natural numbers $d$ and $n$, the fixed $n$-cell polycubes in
dimension $d$ are represented by the finite sets $S$ of lattice cells in $\mathbb{Z}^d$ that are
polycubes (nonempty and connected through face adjacency), have exactly $n$ cells, and are in
canonical position (the minimum of each coordinate over $S$ is $0$).

Formalized by `MetaMathlibExt.fixedPolycube`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#fixed-polycube).

## Number of fixed polycubes

For natural numbers $d$ and $n$, $A_d(n)$ is the number of
fixed $n$-cell polycubes in dimension $d$, that is, the number of $n$-cell polycubes in
$\mathbb{Z}^d$ that are in canonical position.

Formalized by `MetaMathlibExt.fixedPolycubeCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#fixed-polycube-count).

## Proper fixed polycubes

For natural numbers $n$ and $i$, the fixed $n$-cell polycubes
proper in dimension $i$ are the fixed $n$-cell polycubes in dimension $i$ whose proper dimension
is $i$, that is, which vary along each of the $i$ axes.

Formalized by `MetaMathlibExt.properFixedPolycube`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#proper-fixed-polycube).

## Number of proper fixed polycubes

For natural numbers $n$ and $i$, $\mathrm{DX}(n,i)$ is
the number of fixed $n$-cell polycubes proper in dimension $i$, that is, of fixed $n$-cell
polycubes in dimension $i$ whose proper dimension is $i$.

## Sources

- Asinowski et al., JIS 15 (2012), Article 12.8.4, line 978, state $\mathrm{DX}(n,0) = 0$ for $n > 1$.

Formalized by `MetaMathlibExt.properFixedPolycubeCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#proper-fixed-polycube-count).

## Lunnon's dimension decomposition for fixed polycubes

Let $d$ and $n$ be natural numbers
with $n > 1$, let $A_d(n)$ be the number of fixed $n$-cell polycubes in dimension $d$, and for
each $i$ let $\mathrm{DX}(n,i)$ be the number of fixed $n$-cell polycubes proper in dimension $i$.
Then

$$A_d(n) = \sum_{i=1}^{n-1} \binom{d}{i} \, \mathrm{DX}(n,i).$$

The hypothesis $n > 1$ is needed: the printed formula omits its domain and fails at $n = 1$,
where the single cell is a polycube proper in dimension $0$ and so is counted only by the
$i = 0$ term, which the sum excludes. For $n > 1$ that term vanishes, since
$\mathrm{DX}(n,0) = 0$.

## Sources

- Sebastian Luther and Stephan Mertens, *The Perimeter of Proper Polycubes*, Journal of Integer Sequences 20 (2017), Article 17.9.5, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Mertens/mert4.tex>: Lunnon's classical formula `eq:lunnon-a`, lines 172–175, with sum `i = 1, …, n-1` and factor `C(d,i)`; `DX` notation and the at-most-`n-1` dimensions bound, lines 163–166. Original: W. F. Lunnon, *Counting multidimensional polyominoes*, Comput. J. 18 (1975), 366–367. `DX(n,0) = 0` for `n > 1` from Asinowski–Barequet–Barequet–Rote, JIS 15 (2012), Article 12.8.4, line 978, <https://cs.uwaterloo.ca/journals/JIS/VOL15/Barequet/barequet2.tex>.

Formalized by `MetaMathlibExt.lunnon_fixed_polycube_dimension_decomposition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean, line 948](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LunnonDimensionDecomposition.lean#L948). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html#lunnon-fixed-polycube-dimension-decompos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed polycubes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/tilings-board-placements/fixed-polycubes)
