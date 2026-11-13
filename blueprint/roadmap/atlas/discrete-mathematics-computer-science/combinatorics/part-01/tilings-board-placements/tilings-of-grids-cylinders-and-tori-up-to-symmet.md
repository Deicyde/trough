---
declaration: section
origin: cited
lean: MetaMathlibExt.cellF, MetaMathlibExt.cellR2, MetaMathlibExt.cellR2F, MetaMathlibExt.cellR, MetaMathlibExt.cellR3, MetaMathlibExt.cellRF, MetaMathlibExt.cellR3F, MetaMathlibExt.fixedTilingCount
statement: formalized
---

# Tilings of grids, cylinders and tori up to symmetry

81 results, 24 proved and 57 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html).

## Cell map of the reflection f

For natural numbers $n$ and $m$, the reflection $f$ acts on
the cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of the $n \times m$
grid by $(x, y) \mapsto (-1 - x, y)$, that is, $(x, y) \mapsto (n - 1 - x, y)$ with the first
coordinate taken modulo $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellF`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-f).

## Cell map of the half-turn r²

For natural numbers $n$ and $m$, the half-turn $r^2$ acts
on the cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of the $n \times m$
grid by $(x, y) \mapsto (-1 - x, -1 - y)$, that is, $(x, y) \mapsto (n - 1 - x, m - 1 - y)$ with
the coordinates taken modulo $n$ and $m$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellR2`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-r2).

## Cell map of the reflection r²f

For natural numbers $n$ and $m$, the reflection $r^2 f$
acts on the cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of the
$n \times m$ grid by $(x, y) \mapsto (x, -1 - y)$, that is, $(x, y) \mapsto (x, m - 1 - y)$ with
the second coordinate taken modulo $m$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellR2F`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-r2-f).

## Cell map of the quarter-turn r

For a natural number $n$, the quarter-turn $r$ acts on the
cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ of the $n \times n$ grid by
$(x, y) \mapsto (-1 - y, x)$, that is, $(x, y) \mapsto (n - 1 - y, x)$ modulo $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellR`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-r).

## Cell map of the three-quarter turn r³

For a natural number $n$, the three-quarter turn
$r^3$ acts on the cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ of the
$n \times n$ grid by $(x, y) \mapsto (y, -1 - x)$, that is, $(x, y) \mapsto (y, n - 1 - x)$
modulo $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellR3`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-r3).

## Cell map of the diagonal reflection rf

For a natural number $n$, the diagonal reflection
$rf$ acts on the cells $(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ of the
$n \times n$ grid by $(x, y) \mapsto (y, x)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellRF`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-rf).

## Cell map of the antidiagonal reflection r³f

For a natural number $n$, the antidiagonal
reflection $r^3 f$ acts on the cells
$(x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ of the $n \times n$ grid by
$(x, y) \mapsto (-1 - y, -1 - x)$, that is, $(x, y) \mapsto (n - 1 - y, n - 1 - x)$ modulo $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellR3F`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-r3-f).

## Number of fixed tilings

Let $\alpha$ (the cells) and $T$ (the tile designs) be finite sets,
let $\varphi : \alpha \to \alpha$ be a map and let $\sigma$ be a permutation of $T$. The number of
tilings fixed by $(\varphi, \sigma)$ is the number of maps $F : \alpha \to T$ such that
$F(\varphi(c)) = \sigma(F(c))$ for every $c \in \alpha$.

This is the paper's fixed-point condition $F(c \cdot s) = F(c) \cdot g$, with $\varphi$ encoding
the action on cells and $\sigma$ the action on designs. No ambient group action is assumed, since
each fixed-point formula involves a single symmetry.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.fixedTilingCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#fixed-tiling-count).

## Tile designs fixed by a power of a permutation

For a finite set $T$ of tile designs, a
permutation $\sigma$ of $T$ and a natural number $k$, this is the number of designs $d \in T$ with
$\sigma^k(d) = d$.

When $\sigma$ is the action of a symmetry $g$ on tile designs, this is the paper's $t_{g^k}$; for
$k = 0$ it is $t_{\mathrm{id}} = |T|$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.tileFixedCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#tile-fixed-count).

## Orbit of a cell under a permutation

Let $\alpha$ be a finite set, $\varphi$ a permutation
of $\alpha$ and $c \in \alpha$. The orbit of $c$ under $\varphi$ is the finite set
$\{\varphi^k(c) : k \in \mathbb{N}\}$ of images of $c$ under the nonnegative powers of $\varphi$.
Since $\alpha$ is finite, this is the orbit of $c$ under the cyclic group generated by $\varphi$.

A fixed point $c$ of $\varphi$ has the singleton orbit $\{c\}$; these one-cycles are kept.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 20.

Formalized by `MetaMathlibExt.permOrbit`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#perm-orbit).

## Orbits of a permutation

Let $\alpha$ be a finite set and $\varphi$ a permutation of
$\alpha$. For $c \in \alpha$ let $O(c) = \{\varphi^k(c) : k \in \mathbb{N}\}$ be the orbit of $c$
under $\varphi$. The set of orbits of $\varphi$ is the set $\{O(c) : c \in \alpha\}$ of subsets of
$\alpha$, in which each orbit occurs once.

Fixed points of $\varphi$ contribute singleton orbits, which the paper's Theorem 20 needs.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 20.

Formalized by `MetaMathlibExt.permOrbits`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#perm-orbits).

## Cylinder shift sum

Let $T$ be a finite set of tile designs, let $n, m \ge 1$, let $g$ be
a map from the cells $\mathbb{Z}/n \times \mathbb{Z}/m$ to themselves, and let $\sigma$ be a
permutation of $T$. The cylinder shift sum of $g$ and $\sigma$ is the sum, over all shifts
$a \in \mathbb{Z}/n$, of the number of tilings $F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$
with $F(g(x + a, y)) = \sigma(F(x, y))$ for every cell $(x, y)$.

The shift is applied before $g$, following the paper's right-action convention, and $\sigma$
is the action of $g$ on tile designs.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cylinderShiftSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-shift-sum).

## Torus shift sum

Let $n, m \ge 1$, let $T$ be a finite set of tile designs, let $g$ be a
map from $\mathbb{Z}/n \times \mathbb{Z}/m$ (the cells of the $n \times m$ torus) to itself and
let $\sigma$ be a permutation of $T$. For a shift $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$,
count the tilings $F \colon \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with
$F(g(x + a, y + b)) = \sigma(F(x, y))$ for every cell $(x, y)$. The torus shift sum is the sum of
these counts over all $nm$ shifts $(a, b)$.

Shifting the cell first and applying $g$ afterwards follows the right-action convention of the
source; shifts act trivially on tile designs.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.torusShiftSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#torus-shift-sum).

## The reflection f of grid cells is an involution

For all natural numbers $n$ and $m$ and
every cell $c = (x, y) \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$, applying the cell
map $(x, y) \mapsto (-1 - x, y)$ of the reflection $f$ twice returns $c$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Setting.

Formalized by `MetaMathlibExt.cellF_involutive`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cell-f-involutive).

## Fixed tilings of two cells under the identity

Let the set of cells and the set of tile
designs both be the two-element set $\{0, 1\}$. The number of maps $F : \{0, 1\} \to \{0, 1\}$
with $F(\varphi(c)) = \sigma(F(c))$ for every cell $c$, where $\varphi$ is the identity map on
cells and $\sigma$ is the identity permutation of designs, equals $4$; that is, all $2^2$ tilings
are fixed.

This is a sanity check of the definition of fixed tilings, not one of the paper's enumerative
theorems.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Encoding check.

Formalized by `MetaMathlibExt.fixedTilingCount_fin_two_identity`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#fixed-tiling-count-fin-two-identity).

## Fixed tilings of the $2 \times 1$ grid under reflection and a design swap

On the grid
$\mathbb{Z}/2 \times \mathbb{Z}/1$ with two tile designs, exactly two tilings $F$ satisfy
$F(f(c)) = \sigma(F(c))$ for every cell $c$, where $f : (x, y) \mapsto (-1 - x, y)$ is the
reflection exchanging the two cells and $\sigma$ swaps the two designs.

This is a check of the encoding, verified by computation.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Encoding check.

Formalized by `MetaMathlibExt.fixedTilingCount_cellF_two_one_swap`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#fixed-tiling-count-cell-f-two-one-swap).

## Fixed tilings as a product over orbits

Let $\alpha$ be a finite set of cells, $T$ a
finite set of tile designs, $\varphi$ a permutation of $\alpha$ and $\sigma$ a permutation of
$T$. The number of tilings $F : \alpha \to T$ with $F(\varphi(c)) = \sigma(F(c))$ for every
cell $c$ equals $\prod_{\theta} t(|\theta|)$, where $\theta$ runs over the orbits of $\varphi$
on $\alpha$, fixed cells included as orbits of size one, and $t(k)$ is the number of designs
fixed by $\sigma^k$.

No order hypothesis on $\sigma$ is needed.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 20.

Stated but not proved: `MetaMathlibExt.fixedTilingCount_eq_orbit_product` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#fixed-tiling-count-eq-orbit-product).

## Rectangular-grid tilings fixed by the identity

Let $n$ and $m$ be positive integers, let
$T$ be a finite set of tiles and let $\sigma$ be a permutation of $T$ with $\sigma^1 = 1$, that is,
the identity. Then the number of tilings $F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with
$F(c) = \sigma(F(c))$ for every cell $c$ equals $|T|^{nm}$.

The Burnside conclusion of Theorem 22 is not part of this single-element fixed-point statement.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-identity).

## Rectangular-grid tilings fixed by the half-turn, $nm$ even

Let $n$ and $m$ be positive
integers with $nm$ even, let $T$ be a finite set of tiles and let $\sigma$ be a permutation of $T$
with $\sigma^2 = 1$. Let $r^2$ be the half-turn of $\mathbb{Z}/n \times \mathbb{Z}/m$ given by
$r^2(x, y) = (-1 - x, -1 - y)$. Then the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(r^2(c)) = \sigma(F(c))$ for every cell $c$
equals $|T|^{nm/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_r2_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-r2-even).

## Rectangular-grid tilings fixed by the half-turn, $nm$ odd

Let $n$ and $m$ be positive
integers with $nm$ odd, let $T$ be a finite set of tiles, let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$, and let $t$ be the number of tiles $d \in T$ with $\sigma(d) = d$. Let $r^2$ be
the half-turn of $\mathbb{Z}/n \times \mathbb{Z}/m$ given by $r^2(x, y) = (-1 - x, -1 - y)$. Then
the number of tilings $F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with
$F(r^2(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{(nm-1)/2} \, t$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_r2_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-r2-odd).

## Rectangular-grid tilings fixed by the reflection $f$, $n$ even

Let $n$ and $m$ be
positive integers with $n$ even, let $T$ be a finite set of tiles and let $\sigma$ be a
permutation of $T$ with $\sigma^2 = 1$. Let $f$ be the reflection of
$\mathbb{Z}/n \times \mathbb{Z}/m$ given by $f(x, y) = (-1 - x, y)$. Then the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(f(c)) = \sigma(F(c))$ for every cell $c$
equals $|T|^{nm/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-f-even).

## Rectangular-grid tilings fixed by the reflection $f$, $n$ odd

Let $n$ and $m$ be positive
integers with $n$ odd, let $T$ be a finite set of tiles, let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$, and let $t$ be the number of tiles $d \in T$ with $\sigma(d) = d$. Let $f$ be the
reflection of $\mathbb{Z}/n \times \mathbb{Z}/m$ given by $f(x, y) = (-1 - x, y)$. Then the number
of tilings $F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(f(c)) = \sigma(F(c))$ for every
cell $c$ equals $|T|^{m(n-1)/2} \, t^m$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-f-odd).

## Rectangular-grid tilings fixed by the reflection $r^2 f$, $m$ even

Let $n$ and $m$ be
positive integers with $m$ even, let $T$ be a finite set of tiles and let $\sigma$ be a
permutation of $T$ with $\sigma^2 = 1$. Let $g$ be the reflection $r^2 f$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$, given by $g(x, y) = (x, -1 - y)$. Then the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(g(c)) = \sigma(F(c))$ for every cell $c$
equals $|T|^{nm/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_r2f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-r2f-even).

## Rectangular-grid tilings fixed by the reflection $r^2 f$, $m$ odd

Let $n$ and $m$ be
positive integers with $m$ odd, let $T$ be a finite set of tiles, let $\sigma$ be a permutation of
$T$ with $\sigma^2 = 1$, and let $t$ be the number of tiles $d \in T$ with $\sigma(d) = d$. Let $g$
be the reflection $r^2 f$ of $\mathbb{Z}/n \times \mathbb{Z}/m$, given by $g(x, y) = (x, -1 - y)$.
Then the number of tilings $F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with
$F(g(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{n(m-1)/2} \, t^n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 22.

Stated but not proved: `MetaMathlibExt.rectangularGrid_r2f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-grid-r2f-odd).

## Square-grid tilings fixed by the identity

Let $n$ be a positive integer, let $T$ be a
finite set and let $\sigma$ be a permutation of $T$ with $\sigma^1 = 1$. Then the number of maps
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(c) = \sigma(F(c))$ for every cell $c$ is
$|T|^{n^2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-identity).

## Square-grid tilings fixed by the half-turn for even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set and let $\sigma$ be a permutation of $T$ with $\sigma^2 = 1$.
Let $r^2$ be the half-turn of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by
$r^2(x, y) = (-1 - x, -1 - y)$. Then the number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(r^2(c)) = \sigma(F(c))$ for every cell $c$ is $|T|^{n^2/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r2_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r2-even).

## Square-grid tilings fixed by the half-turn for odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set, let $\sigma$ be a permutation of $T$ with $\sigma^2 = 1$, and
write $t_\sigma$ for the number of elements $t \in T$ with $\sigma(t) = t$. Let $r^2$ be the
half-turn of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by $r^2(x, y) = (-1 - x, -1 - y)$.
Then the number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r^2(c)) = \sigma(F(c))$
for every cell $c$ is $|T|^{(n^2 - 1)/2} \cdot t_\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r2_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r2-odd).

## Square-grid tilings fixed by the reflection $f$ for even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set and let $\sigma$ be a permutation of $T$ with $\sigma^2 = 1$.
Let $f$ be the reflection of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by
$f(x, y) = (-1 - x, y)$. Then the number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with
$F(f(c)) = \sigma(F(c))$ for every cell $c$ is $|T|^{n^2/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-f-even).

## Square-grid tilings fixed by the reflection $f$ for odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set, let $\sigma$ be a permutation of $T$ with $\sigma^2 = 1$, and
write $t_\sigma$ for the number of elements $t \in T$ with $\sigma(t) = t$. Let $f$ be the
reflection of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by $f(x, y) = (-1 - x, y)$. Then the
number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(f(c)) = \sigma(F(c))$ for every
cell $c$ is $|T|^{(n^2 - n)/2} \cdot t_\sigma^{\,n}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-f-odd).

## Square-grid tilings fixed by the reflection $r^2 f$ for even $n$

Let $n$ be an even
positive integer, let $T$ be a finite set and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $r^2 f$ be the reflection of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by
$(r^2 f)(x, y) = (x, -1 - y)$. Then the number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F((r^2 f)(c)) = \sigma(F(c))$ for every cell $c$ is $|T|^{n^2/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r2f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r2f-even).

## Square-grid tilings fixed by the reflection $r^2f$, odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $r^2f$ be the cell map $(x, y) \mapsto (x, -1-y)$ of the $n \times n$ grid
$(\mathbb{Z}/n\mathbb{Z})^2$. Then the number of tilings $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(r^2f(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{(n^2-n)/2} \, t^n$, where $t$ is
the number of designs in $T$ fixed by $\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r2f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r2f-odd).

## Square-grid tilings fixed by the quarter-turn for even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set and let $\sigma$ be a permutation of $T$ with $\sigma^4 = 1$.
Let $r$ be the quarter-turn of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by
$r(x, y) = (-1 - y, x)$. Then the number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with
$F(r(c)) = \sigma(F(c))$ for every cell $c$ is $|T|^{n^2/4}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r-even).

## Square-grid tilings fixed by the quarter-turn for odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set, let $\sigma$ be a permutation of $T$ with $\sigma^4 = 1$, and
write $t_\sigma$ for the number of elements $t \in T$ with $\sigma(t) = t$. Let $r$ be the
quarter-turn of the grid $(\mathbb{Z}/n\mathbb{Z})^2$ given by $r(x, y) = (-1 - y, x)$. Then the
number of maps $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r(c)) = \sigma(F(c))$ for every
cell $c$ is $|T|^{(n^2 - 1)/4} \cdot t_\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r-odd).

## Square-grid tilings fixed by the rotation $r^3$, even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^4 = 1$. Let $r^3$ be the cell map $(x, y) \mapsto (y, -1-x)$ of the $n \times n$ grid
$(\mathbb{Z}/n\mathbb{Z})^2$. Then the number of tilings $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(r^3(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{n^2/4}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r3_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r3-even).

## Square-grid tilings fixed by the rotation $r^3$, odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^4 = 1$. Let $r^3$ be the cell map $(x, y) \mapsto (y, -1-x)$ of the $n \times n$ grid
$(\mathbb{Z}/n\mathbb{Z})^2$. Then the number of tilings $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(r^3(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{(n^2-1)/4} \, t$, where $t$ is the
number of designs in $T$ fixed by $\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r3_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r3-odd).

## Square-grid tilings fixed by the diagonal reflection $rf$

Let $n$ be a positive integer,
let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $rf$ be the cell map $(x, y) \mapsto (y, x)$ of the $n \times n$ grid
$(\mathbb{Z}/n\mathbb{Z})^2$. Then the number of tilings $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(rf(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{(n^2-n)/2} \, t^n$, where $t$ is
the number of designs in $T$ fixed by $\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_rf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-rf).

## Square-grid tilings fixed by the diagonal reflection $r^3f$

Let $n$ be a positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $r^3f$ be the cell map $(x, y) \mapsto (-1-y, -1-x)$ of the $n \times n$ grid
$(\mathbb{Z}/n\mathbb{Z})^2$. Then the number of tilings $F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$
with $F(r^3f(c)) = \sigma(F(c))$ for every cell $c$ equals $|T|^{(n^2-n)/2} \, t^n$, where $t$ is
the number of designs in $T$ fixed by $\sigma$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 24.

Stated but not proved: `MetaMathlibExt.squareGrid_r3f` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-grid-r3f).

## Solution of $x = -1-x-a$ modulo odd $n$

Let $n$ be a positive odd integer and
$a \in \mathbb{Z}/n$. Then the set of $x \in \mathbb{Z}/n$ with $x = -1-x-a$ is the singleton
$\{k(-1-a)\}$, where $k$ is the residue mod $n$ of the integer $(n+1)/2$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Lemma 25.

Stated but not proved: `MetaMathlibExt.reflection_shift_solutions_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#reflection-shift-solutions-odd).

## Solutions of $x = -1-x-a$ modulo even $n$ for odd $a$

Let $n$ be a positive even
integer and $a \in \mathbb{Z}/n$ whose representative $\bar a \in \{0, \dots, n-1\}$ is odd.
Then the set of $x \in \mathbb{Z}/n$ with $x = -1-x-a$ consists of the residues mod $n$ of the
integers $(-1-\bar a)/2$ and $(n-1-\bar a)/2$.

The divisions by $2$ are exact divisions of integers, carried out before reducing mod $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Lemma 25.

Stated but not proved: `MetaMathlibExt.reflection_shift_solutions_even_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#reflection-shift-solutions-even-odd).

## No solutions of $x = -1-x-a$ modulo $n$ when $n$ and $a$ are even

Let $n$ be a
positive even integer and $a \in \mathbb{Z}/n$ whose representative in $\{0, \dots, n-1\}$ is
even. Then no $x \in \mathbb{Z}/n$ satisfies $x = -1-x-a$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Lemma 25.

Stated but not proved: `MetaMathlibExt.reflection_shift_solutions_even_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#reflection-shift-solutions-even-even).

## Cylinder fixed-tiling count for the identity

Let $T$ be a finite set of tile designs,
let $n, m \ge 1$, and let $\sigma$ be a permutation of $T$ with $\sigma^1 = 1$, that is, the
identity. Then the cylinder shift sum of the identity map of $\mathbb{Z}/n \times \mathbb{Z}/m$
and $\sigma$ equals $\sum_{d \mid n} \varphi(d)\, |T|^{nm/d}$, where $d$ runs over the positive
divisors of $n$ and $\varphi$ is Euler's totient function.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 28.

Stated but not proved: `MetaMathlibExt.cylinder_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-identity).

## Cylinder fixed-tiling count for the half-turn when $m$ is even

Let $T$ be a finite set of
tile designs, let $n, m \ge 1$ with $m$ even, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $r^2$ be the cell map $(x, y) \mapsto (-1 - x, -1 - y)$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$. Then the cylinder shift sum of $r^2$ and $\sigma$ equals
$n \cdot |T|^{nm/2}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 29.

Stated but not proved: `MetaMathlibExt.cylinder_r2_m_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-r2-m-even).

## Cylinder fixed-tiling count for the half-turn when $m$ is odd and $n$ is even

Let $T$ be
a finite set of tile designs, let $n, m \ge 1$ with $m$ odd and $n$ even, and let $\sigma$ be a
permutation of $T$ with $\sigma^2 = 1$. Let $r^2$ be the cell map
$(x, y) \mapsto (-1 - x, -1 - y)$ of $\mathbb{Z}/n \times \mathbb{Z}/m$, and let $t$ be the
number of designs fixed by $\sigma$. Then twice the cylinder shift sum of $r^2$ and $\sigma$
equals $n \left(|T|^{nm/2} + |T|^{(nm - 2)/2}\, t^2\right)$.

The identity is stated after multiplying by $2$, so that it involves no fractions.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 29.

Stated but not proved: `MetaMathlibExt.cylinder_r2_m_odd_n_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-r2-m-odd-n-even).

## Cylinder fixed-tiling count for the half-turn when $m$ and $n$ are odd

Let $T$ be a
finite set of tile designs, let $n, m \ge 1$ both be odd, and let $\sigma$ be a permutation of
$T$ with $\sigma^2 = 1$. Let $r^2$ be the cell map $(x, y) \mapsto (-1 - x, -1 - y)$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$, and let $t$ be the number of designs fixed by $\sigma$. Then
the cylinder shift sum of $r^2$ and $\sigma$ equals $n \cdot |T|^{(nm - 1)/2} \cdot t$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 29.

Stated but not proved: `MetaMathlibExt.cylinder_r2_odd_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-r2-odd-odd).

## Fixed cylinder tilings of the reflection f, n even

Let $T$ be a finite set of tile
designs, let $\sigma$ be a permutation of $T$ with $\sigma^2 = 1$, and let $n, m \ge 1$ with $n$
even. For $a \in \mathbb{Z}/n\mathbb{Z}$ count the tilings
$F : \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z} \to T$ with
$F(-1 - x - a, y) = \sigma(F(x, y))$ for every cell $(x, y)$, and let $N$ be the sum of these
counts over all $a \in \mathbb{Z}/n\mathbb{Z}$. If $t_f$ is the number of designs $d \in T$ with
$\sigma(d) = d$, then

$$2N = n\left(|T|^{nm/2} + |T|^{(nm - 2m)/2} t_f^{2m}\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 30.

Stated but not proved: `MetaMathlibExt.cylinder_f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-f-even).

## Cylinder fixed-tiling count for the reflection $f$ when $n$ is odd

Let $T$ be a finite set
of tile designs, let $n, m \ge 1$ with $n$ odd, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. Let $f$ be the cell map $(x, y) \mapsto (-1 - x, y)$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$, and let $t$ be the number of designs fixed by $\sigma$. Then
the cylinder shift sum of $f$ and $\sigma$ equals $n \cdot |T|^{(nm - m)/2} \cdot t^m$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 30.

Stated but not proved: `MetaMathlibExt.cylinder_f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-f-odd).

## Cylinder fixed-tiling count for the reflection $r^2 f$ when $m$ is even

Let $T$ be a
finite set of tile designs, let $n, m \ge 1$ with $m$ even, and let $\sigma$ be a permutation of
$T$ with $\sigma^2 = 1$. Let $r^2 f$ be the cell map $(x, y) \mapsto (x, -1 - y)$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$. Then the cylinder shift sum of $r^2 f$ and $\sigma$ equals
$\sum_{d \mid n} \varphi(d)\, |T|^{nm / \operatorname{lcm}(d, 2)}$, where $d$ runs over the
positive divisors of $n$ and $\varphi$ is Euler's totient function.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 31.

Stated but not proved: `MetaMathlibExt.cylinder_r2f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-r2f-even).

## Cylinder fixed-tiling count for the reflection $r^2 f$ when $m$ is odd

Let $T$ be a
finite set of tile designs, let $n, m \ge 1$ with $m$ odd, and let $\sigma$ be a permutation of
$T$ with $\sigma^2 = 1$. Let $r^2 f$ be the cell map $(x, y) \mapsto (x, -1 - y)$ of
$\mathbb{Z}/n \times \mathbb{Z}/m$, and for $k \ge 0$ let $t_k$ be the number of designs fixed
by $\sigma^k$. Then the cylinder shift sum of $r^2 f$ and $\sigma$ equals
$\sum_{d \mid n} \varphi(d)\, |T|^{(nm - n) / \operatorname{lcm}(d, 2)}\, t_d^{\,n/d}$, where
$d$ runs over the positive divisors of $n$ and $\varphi$ is Euler's totient function.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 31.

Stated but not proved: `MetaMathlibExt.cylinder_r2f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-r2f-odd).

## Torus fixed-tiling sum for the identity

Let $n$ and $m$ be positive integers, let $T$ be
a finite set of tiles and let $\sigma$ be a permutation of $T$ with $\sigma^1 = 1$, that is, the
identity. For $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$ let $N(a, b)$ be the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(x + a, y + b) = \sigma(F(x, y))$ for every
cell $(x, y)$. Then, with $\varphi$ Euler's totient function,

$$\sum_{a \in \mathbb{Z}/n} \sum_{b \in \mathbb{Z}/m} N(a, b) =
\sum_{c \mid m} \sum_{d \mid n} \varphi(c) \, \varphi(d) \, |T|^{mn / \operatorname{lcm}(c, d)}.$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 34.

Stated but not proved: `MetaMathlibExt.rectangularTorus_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-identity).

## Half-turn fixed points on the rectangular torus, both sides even

Let $T$ be a finite
set of tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, and $n, m$ positive even
integers. For a shift $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(-1-x-a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the half-turn $r^2$). Write $t_{\mathrm{id}} = |T|$ and let
$t_{r^2}$ be the number of designs $d \in T$ with $\sigma(d) = d$. Then

$$4\,\mathrm{fxpt} =
nm\left(3\,t_{\mathrm{id}}^{nm/2} + t_{\mathrm{id}}^{nm/2-2}\,t_{r^2}^4\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 35.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2_even_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2-even-even).

## Half-turn fixed points on the rectangular torus, both sides odd

Let $T$ be a finite
set of tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, and $n, m$ positive odd
integers. For a shift $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(-1-x-a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the half-turn $r^2$). Write $t_{\mathrm{id}} = |T|$ and let
$t_{r^2}$ be the number of designs $d \in T$ with $\sigma(d) = d$. Then

$$\mathrm{fxpt} = nm\,t_{\mathrm{id}}^{(nm-1)/2}\,t_{r^2}.$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 35.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2_odd_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2-odd-odd).

## Half-turn fixed points on the rectangular torus, $n$ even and $m$ odd

Let $T$ be a
finite set of tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, $n$ a positive
even integer and $m$ a positive odd integer. For a shift
$(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(-1-x-a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the half-turn $r^2$). Write $t_{\mathrm{id}} = |T|$ and let
$t_{r^2}$ be the number of designs $d \in T$ with $\sigma(d) = d$. Then

$$2\,\mathrm{fxpt} = nm\left(t_{\mathrm{id}}^{nm/2} + t_{\mathrm{id}}^{nm/2-1}\,t_{r^2}^2\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 35.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2_even_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2-even-odd).

## Half-turn fixed points on the rectangular torus, $n$ odd and $m$ even

Let $T$ be a
finite set of tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, $n$ a positive
odd integer and $m$ a positive even integer. For a shift
$(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(-1-x-a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the half-turn $r^2$). Write $t_{\mathrm{id}} = |T|$ and let
$t_{r^2}$ be the number of designs $d \in T$ with $\sigma(d) = d$. Then

$$2\,\mathrm{fxpt} = nm\left(t_{\mathrm{id}}^{nm/2} + t_{\mathrm{id}}^{nm/2-1}\,t_{r^2}^2\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 35.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2_odd_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2-odd-even).

## Torus fixed-tiling sum for the reflection $f$, $n$ even

Let $n$ and $m$ be positive
integers with $n$ even, let $T$ be a finite set of tiles, let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$, and for $k \ge 0$ let $t_k$ be the number of tiles $d \in T$ with
$\sigma^k(d) = d$. Let $f(x, y) = (-1 - x, y)$ on $\mathbb{Z}/n \times \mathbb{Z}/m$, and for
$(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$ let $N(a, b)$ be the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(f(x + a, y + b)) = \sigma(F(x, y))$ for every
cell $(x, y)$. Then, with $\varphi$ Euler's totient function,

$$2 \sum_{a \in \mathbb{Z}/n} \sum_{b \in \mathbb{Z}/m} N(a, b) =
n \sum_{c \mid m} \varphi(c) \left(|T|^{nm / \operatorname{lcm}(2, c)} +
t_c^{2m/c} \, |T|^{(n-2)m / \operatorname{lcm}(2, c)}\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 36.

Stated but not proved: `MetaMathlibExt.rectangularTorus_f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-f-even).

## Torus fixed-tiling sum for the reflection $f$, $n$ odd

Let $n$ and $m$ be positive
integers with $n$ odd, let $T$ be a finite set of tiles, let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$, and for $k \ge 0$ let $t_k$ be the number of tiles $d \in T$ with
$\sigma^k(d) = d$. Let $f(x, y) = (-1 - x, y)$ on $\mathbb{Z}/n \times \mathbb{Z}/m$, and for
$(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$ let $N(a, b)$ be the number of tilings
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(f(x + a, y + b)) = \sigma(F(x, y))$ for every
cell $(x, y)$. Then, with $\varphi$ Euler's totient function,

$$\sum_{a \in \mathbb{Z}/n} \sum_{b \in \mathbb{Z}/m} N(a, b) =
n \sum_{c \mid m} \varphi(c) \, |T|^{(n-1)m / \operatorname{lcm}(2, c)} \, t_c^{m/c}.$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 36.

Stated but not proved: `MetaMathlibExt.rectangularTorus_f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-f-odd).

## Fixed points of $r^2 f$ on the rectangular torus, $m$ even

Let $T$ be a finite set of
tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, $n$ a positive integer and $m$ a
positive even integer. For a shift $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(x+a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the reflection $r^2 f$). Write $t_{\mathrm{id}} = |T|$, let
$t_{(r^2f)^d}$ be the number of designs $e \in T$ with $\sigma^d(e) = e$, and let $\varphi$ be
Euler's totient function. Then, with $d$ running over the positive divisors of $n$,

$$2\,\mathrm{fxpt} = m \sum_{d \mid n} \varphi(d)\left(
t_{\mathrm{id}}^{nm/\operatorname{lcm}(d,2)} +
t_{\mathrm{id}}^{n(m-2)/\operatorname{lcm}(d,2)}\,t_{(r^2f)^d}^{2n/d}\right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 36.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2f-even).

## Fixed points of $r^2 f$ on the rectangular torus, $m$ odd

Let $T$ be a finite set of
tile designs, $\sigma$ a permutation of $T$ with $\sigma^2 = 1$, $n$ a positive integer and $m$ a
positive odd integer. For a shift $(a, b) \in \mathbb{Z}/n \times \mathbb{Z}/m$, count the maps
$F : \mathbb{Z}/n \times \mathbb{Z}/m \to T$ with $F(x+a, -1-y-b) = \sigma(F(x, y))$ for all
cells $(x, y)$, and let $\mathrm{fxpt}$ be the sum of these counts over all $nm$ shifts (the
torus fixed-point count of the reflection $r^2 f$). Write $t_{\mathrm{id}} = |T|$, let
$t_{(r^2f)^d}$ be the number of designs $e \in T$ with $\sigma^d(e) = e$, and let $\varphi$ be
Euler's totient function. Then, with $d$ running over the positive divisors of $n$,

$$\mathrm{fxpt} = m \sum_{d \mid n} \varphi(d)\,
t_{\mathrm{id}}^{n(m-1)/\operatorname{lcm}(d,2)}\,t_{(r^2f)^d}^{n/d}.$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 36.

Stated but not proved: `MetaMathlibExt.rectangularTorus_r2f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rectangular-torus-r2f-odd).

## Square-torus fixed points of the identity

Let $n$ be a positive integer, let $T$ be a
finite set of tile designs, and let $\sigma$ be the identity permutation of $T$. Let $S$ be the
sum, over all shifts $v \in (\mathbb{Z}/n\mathbb{Z})^2$, of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(c + v) = \sigma(F(c))$ for every cell $c$. Then
$S = \sum_{d_1 \mid n} \sum_{d_2 \mid n} \varphi(d_1) \, \varphi(d_2) \,
|T|^{n^2/\operatorname{lcm}(d_1, d_2)}$, where $d_1$ and $d_2$ run over the positive divisors of
$n$ and $\varphi$ is Euler's totient function.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 777](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-identity).

## Fixed tilings of the odd square torus under a half-turn

Let $n$ be an odd positive
integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with $\sigma^2 = 1$,
and write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$. Let $S$ be the torus
shift sum of the half-turn cell map $r^2(x, y) = (-1-x, -1-y)$ on $(\mathbb{Z}/n\mathbb{Z})^2$,
that is, the sum over all shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r^2(c + (a, b))) = \sigma(F(c))$ for every cell
$c$. Then $S = n^2 \, |T|^{(n^2-1)/2} \, t_1$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_r2_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r2-odd).

## Fixed tilings of the even square torus under a half-turn

Let $n$ be an even positive
integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with $\sigma^2 = 1$,
and write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$. Let $S$ be the torus
shift sum of the half-turn cell map $r^2(x, y) = (-1-x, -1-y)$ on $(\mathbb{Z}/n\mathbb{Z})^2$,
that is, the sum over all shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r^2(c + (a, b))) = \sigma(F(c))$ for every cell
$c$. Then $4S = n^2 \left(3 \, |T|^{n^2/2} + |T|^{n^2/2 - 2} \, t_1^4\right)$.

Multiplying by four replaces the paper's coefficients $3/4$ and $1/4$ by integers.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_r2_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r2-even).

## Square-torus fixed points of the reflection $f$, even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. For $k \ge 1$ let $t_k$ be the number of designs in $T$ fixed by $\sigma^k$. Let
$f$ be the cell map $(x, y) \mapsto (-1-x, y)$ of $(\mathbb{Z}/n\mathbb{Z})^2$, and let $S$ be the
sum, over all shifts $v \in (\mathbb{Z}/n\mathbb{Z})^2$, of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(f(c + v)) = \sigma(F(c))$ for every cell $c$.
Then $2S = n \sum_{d \mid n} \varphi(d) \, (a_d + b_d)$, where $d$ runs over the positive
divisors of $n$, $\varphi$ is Euler's totient function, $\ell_d = \operatorname{lcm}(2, d)$,
$a_d = |T|^{n^2/\ell_d}$ and $b_d = |T|^{(n^2-2n)/\ell_d} \, t_d^{2n/d}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 818](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L818). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-f-even).

## Square-torus fixed points of the reflection $f$, odd $n$

Let $n$ be an odd positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^2 = 1$. For $k \ge 1$ let $t_k$ be the number of designs in $T$ fixed by $\sigma^k$. Let
$f$ be the cell map $(x, y) \mapsto (-1-x, y)$ of $(\mathbb{Z}/n\mathbb{Z})^2$, and let $S$ be the
sum, over all shifts $v \in (\mathbb{Z}/n\mathbb{Z})^2$, of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(f(c + v)) = \sigma(F(c))$ for every cell $c$.
Writing $\varphi$ for Euler's totient function,

$$S = n \sum_{d \mid n} \varphi(d) \, |T|^{(n^2-n)/\operatorname{lcm}(2, d)} \, t_d^{n/d},$$

where $d$ runs over the positive divisors of $n$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-f-odd).

## Fixed tilings of the even square torus under the reflection $r^2 f$

Let $n$ be an even
positive integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with
$\sigma^2 = 1$; for $k \in \mathbb{N}$ write $t_k$ for the number of designs $d \in T$ with
$\sigma^k(d) = d$, and let $\varphi$ be Euler's totient function. Let $S$ be the torus shift sum
of the cell map $g(x, y) = (x, -1-y)$ of $r^2 f$ on $(\mathbb{Z}/n\mathbb{Z})^2$, that is, the
sum over all shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(g(c + (a, b))) = \sigma(F(c))$ for every cell $c$.
Then $2S = n \sum_{d \mid n} \varphi(d) \left(|T|^{n^2/\operatorname{lcm}(2, d)} + |T|^{(n^2-2n)/
\operatorname{lcm}(2, d)} \, t_d^{2n/d}\right)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_r2f_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 847](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r2f-even).

## Fixed tilings of the odd square torus under the reflection $r^2 f$

Let $n$ be an odd
positive integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with
$\sigma^2 = 1$; for $k \in \mathbb{N}$ write $t_k$ for the number of designs $d \in T$ with
$\sigma^k(d) = d$, and let $\varphi$ be Euler's totient function. Let $S$ be the torus shift sum
of the cell map $g(x, y) = (x, -1-y)$ of $r^2 f$ on $(\mathbb{Z}/n\mathbb{Z})^2$, that is, the
sum over all shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(g(c + (a, b))) = \sigma(F(c))$ for every cell $c$.
Then $S = n \sum_{d \mid n} \varphi(d) \, |T|^{(n^2-n)/\operatorname{lcm}(2, d)} \, t_d^{n/d}$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 38.

Stated but not proved: `MetaMathlibExt.squareTorus_r2f_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 862](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L862). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r2f-odd).

## Fixed tilings of the odd square torus under a quarter-turn

Let $n$ be an odd positive
integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with $\sigma^4 = 1$,
and write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$. Let $S$ be the torus
shift sum of the quarter-turn cell map $r(x, y) = (-1-y, x)$ on $(\mathbb{Z}/n\mathbb{Z})^2$, that
is, the sum over all shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r(c + (a, b))) = \sigma(F(c))$ for every cell $c$.
Then $S = n^2 \, |T|^{(n^2-1)/4} \, t_1$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 39.

Stated but not proved: `MetaMathlibExt.squareTorus_r_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 877](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L877). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r-odd).

## Square-torus fixed points of the rotation $r$, even $n$

Let $n$ be an even positive
integer, let $T$ be a finite set of tile designs, and let $\sigma$ be a permutation of $T$ with
$\sigma^4 = 1$. For $k \ge 1$ let $t_k$ be the number of designs in $T$ fixed by $\sigma^k$. Let
$r$ be the cell map $(x, y) \mapsto (-1-y, x)$ of $(\mathbb{Z}/n\mathbb{Z})^2$, and let $S$ be the
sum, over all shifts $v \in (\mathbb{Z}/n\mathbb{Z})^2$, of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r(c + v)) = \sigma(F(c))$ for every cell $c$. Then

$$2S = n^2 \left( |T|^{n^2/4} + |T|^{(n^2-4)/4} \, t_1^2 \, t_2 \right).$$

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 39.

Stated but not proved: `MetaMathlibExt.squareTorus_r_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 890](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r-even).

## Fixed tilings of the odd square torus under a three-quarter turn

Let $n$ be an odd
positive integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with
$\sigma^4 = 1$, and write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$. Let $S$
be the torus shift sum of the three-quarter-turn cell map $r^3(x, y) = (y, -1-x)$ on
$(\mathbb{Z}/n\mathbb{Z})^2$, that is, the sum over all shifts
$(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r^3(c + (a, b))) = \sigma(F(c))$ for every cell
$c$. Then $S = n^2 \, |T|^{(n^2-1)/4} \, t_1$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 39.

Stated but not proved: `MetaMathlibExt.squareTorus_r3_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 905](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L905). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r3-odd).

## Fixed tilings of the even square torus under a three-quarter turn

Let $n$ be an even
positive integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with
$\sigma^4 = 1$, and for $k = 1, 2$ write $t_k$ for the number of designs $d \in T$ with
$\sigma^k(d) = d$. Let $S$ be the torus shift sum of the three-quarter-turn cell map
$r^3(x, y) = (y, -1-x)$ on $(\mathbb{Z}/n\mathbb{Z})^2$, that is, the sum over all shifts
$(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(r^3(c + (a, b))) = \sigma(F(c))$ for every cell
$c$. Then $2S = n^2 \left(|T|^{n^2/4} + |T|^{(n^2-4)/4} \, t_1^2 \, t_2\right)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 39.

Stated but not proved: `MetaMathlibExt.squareTorus_r3_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 918](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L918). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r3-even).

## Fixed tilings of the square torus under the diagonal reflection

Let $n$ be a positive
integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with $\sigma^2 = 1$;
write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$, and let $\varphi$ be Euler's
totient function. Let $S$ be the torus shift sum of the cell map $g(x, y) = (y, x)$ of $rf$ on
$(\mathbb{Z}/n\mathbb{Z})^2$, that is, the sum over all shifts
$(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(g(c + (a, b))) = \sigma(F(c))$ for every cell $c$.
Then $S = n \left(\sum_{d \mid n,\ d \text{ odd}} \varphi(d) \, |T|^{(n^2-n)/(2d)} \, t_1^{n/d} +
\sum_{d \mid n,\ d \text{ even}} \varphi(d) \, |T|^{n^2/(2d)}\right)$.

The paper writes this as a single divisor sum with a summand depending on the parity of $d$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 40.

Stated but not proved: `MetaMathlibExt.squareTorus_rf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 933](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L933). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-rf).

## Fixed tilings of the square torus under the anti-diagonal reflection

Let $n$ be a
positive integer, $T$ a finite set of tile designs and $\sigma$ a permutation of $T$ with
$\sigma^2 = 1$; write $t_1$ for the number of designs $d \in T$ with $\sigma(d) = d$, and let
$\varphi$ be Euler's totient function. Let $S$ be the torus shift sum of the cell map
$g(x, y) = (-1-y, -1-x)$ of $r^3 f$ on $(\mathbb{Z}/n\mathbb{Z})^2$, that is, the sum over all
shifts $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$ of the number of tilings
$F : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ with $F(g(c + (a, b))) = \sigma(F(c))$ for every cell $c$.
Then $S = n \left(\sum_{d \mid n,\ d \text{ odd}} \varphi(d) \, |T|^{(n^2-n)/(2d)} \, t_1^{n/d} +
\sum_{d \mid n,\ d \text{ even}} \varphi(d) \, |T|^{n^2/(2d)}\right)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 40.

Stated but not proved: `MetaMathlibExt.squareTorus_r3f` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 950](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L950). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-r3f).

## Action of the rectangle group on grid cells

Let $n, m \in \mathbb{N}$ and view the cells
of the $n \times m$ grid as $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$. Write the
elements of the dihedral group of order $8$ as rotations $r_i$ and reflections $sr_i$ for
$i \in \mathbb{Z}/4\mathbb{Z}$. Each element acts on cells as follows: $r_0$ by the identity,
$r_i$ with $i \ne 0$ by the half-turn $(x, y) \mapsto (-1 - x, -1 - y)$, $sr_0$ by the
reflection $(x, y) \mapsto (-1 - x, y)$, and $sr_i$ with $i \ne 0$ by the reflection
$(x, y) \mapsto (x, -1 - y)$.

The paper's rectangle group $D_4 = \langle r^2, f \rangle$ is the subgroup
$\{r_0, r_2, sr_0, sr_2\}$, with $f = sr_0$, $r^2 = r_2$ and $r^2 f = sr_2$. On this subgroup the
assignment of cell maps is a homomorphism into maps under composition; the values at $r_1$, $r_3$,
$sr_1$ and $sr_3$ are never used.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definitions 1.4.1 and 1.4.2 (the dihedral action on cells).

Formalized by `MetaMathlibExt.rectCellAction`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 969](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L969). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-cell-action).

## Rectangle-group cell action of the identity

Let $n, m \in \mathbb{N}$, and let $r_i$
($i \in \mathbb{Z}/4\mathbb{Z}$) denote the rotations of the dihedral group of order $8$. Under the
rectangle-group action on the cells $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of the
$n \times m$ grid, the identity element $r_0$ acts as the identity map.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.1.

Formalized by `MetaMathlibExt.rectCellAction_r_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-cell-action-r-zero).

## Rectangle-group cell action of the half-turn

Let $n, m \in \mathbb{N}$, and let $r_i$
($i \in \mathbb{Z}/4\mathbb{Z}$) denote the rotations of the dihedral group of order $8$. Under the
rectangle-group action on the cells $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of the
$n \times m$ grid, $r_2$ acts as the half-turn $(x, y) \mapsto (-1 - x, -1 - y)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.1.

Formalized by `MetaMathlibExt.rectCellAction_r_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 983](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L983). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-cell-action-r-two).

## Rectangle-group cell action of the reflection f

Let $n, m \in \mathbb{N}$, and let $sr_i$
($i \in \mathbb{Z}/4\mathbb{Z}$) denote the reflections of the dihedral group of order $8$. Under
the rectangle-group action on the cells $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ of
the $n \times m$ grid, $sr_0$ (the paper's $f$) acts as the reflection $(x, y) \mapsto (-1 - x, y)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.1.

Formalized by `MetaMathlibExt.rectCellAction_sr_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 990](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L990). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-cell-action-sr-zero).

## Rectangle-group cell action of the reflection r²f

Let $n, m \in \mathbb{N}$, and let
$sr_i$ ($i \in \mathbb{Z}/4\mathbb{Z}$) denote the reflections of the dihedral group of order $8$.
Under the rectangle-group action on the cells $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$
of the $n \times m$ grid, $sr_2$ (the paper's $r^2 f$) acts as the reflection
$(x, y) \mapsto (x, -1 - y)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.1.

Formalized by `MetaMathlibExt.rectCellAction_sr_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 996](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L996). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-cell-action-sr-two).

## The dihedral action on the cells of the square grid

For a natural number $n$, let $r$ and
$f$ be the maps of $(\mathbb{Z}/n\mathbb{Z})^2$ given by $r(x, y) = (-1 - y, x)$ (the quarter-turn)
and $f(x, y) = (-1 - x, y)$ (the reflection). The dihedral group of order $8$ has the rotations
$r_i$ and the reflections $sr_i$ for $i \in \mathbb{Z}/4\mathbb{Z}$. The action sends $r_i$ to the
$i$-fold iterate $r^i$ and $sr_i$ to $f \circ r^i$, where $i$ is read as an integer in
$\{0, 1, 2, 3\}$.

Since $f \circ r \circ f = r^{-1}$ on cells, this assignment turns the multiplication of the
dihedral group into composition of maps.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.2 (the dihedral action on cells).

Formalized by `MetaMathlibExt.squareCellAction`, a definition declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1007](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1007). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-cell-action).

## The rotation $r$ acts on the square grid as the quarter-turn

For every natural
number $n$, the square cell action of the dihedral group of order $8$ on
$\mathbb{Z}/n \times \mathbb{Z}/n$ sends the rotation $r$ to the quarter-turn
$(x, y) \mapsto (-1-y, x)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.2.

Formalized by `MetaMathlibExt.squareCellAction_r_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1015](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1015). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-cell-action-r-one).

## The reflection $sr_0$ acts on the square grid as $f$

Let $r_i$ and $sr_i$
($i \in \mathbb{Z}/4\mathbb{Z}$) denote the rotations and the reflections of the dihedral group
of order $8$. For every natural number $n$, the dihedral action on the cells
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ of the $n \times n$ grid sends the
reflection $sr_0$ to the reflection $f$, $(x, y) \mapsto (-1 - x, y)$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Definition 1.4.2.

Formalized by `MetaMathlibExt.squareCellAction_sr_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1021](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1021). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-cell-action-sr-zero).

## Burnside count of cylinder tilings under rectangle symmetries

Let $T$ be a finite set of
tile designs, let $n, m \ge 1$, and let $R$ be a subgroup of the dihedral group
$\langle r, f \rangle$ of order $8$ that is contained in the rectangle group
$\lbrace 1, r^2, f, r^2 f \rbrace$ and acts on $T$. For $g \in R$ let $\phi_g$ be its cell map on
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$: $\phi_1(x, y) = (x, y)$,
$\phi_{r^2}(x, y) = (-1 - x, -1 - y)$, $\phi_f(x, y) = (-1 - x, y)$ and
$\phi_{r^2 f}(x, y) = (x, -1 - y)$. Consider the equivalence relation on tilings
$F : \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z} \to T$ generated by relating $F$ to $F'$
whenever there are $a \in \mathbb{Z}/n\mathbb{Z}$ and $g \in R$ with
$F'(x, y) = g^{-1} \cdot F(\phi_g(x + a, y))$ for every cell $(x, y)$. For $g \in R$ let $N_g$ be
the sum over $a \in \mathbb{Z}/n\mathbb{Z}$ of the number of tilings $F$ with
$F(\phi_g(x + a, y)) = g \cdot F(x, y)$ for every cell $(x, y)$. Then the number of equivalence
classes is $\frac{1}{n|R|} \sum_{g \in R} N_g$.

As in the paper, the tile designs form an $R$-set: only the subgroup $R$ acts on $T$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 32 (`jis-2024-24.6.1-thm-32`).

Stated but not proved: `MetaMathlibExt.cylinder_distinctTilings_burnside` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1036](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1036). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#cylinder-distinct-tilings-burnside).

## Burnside count of torus tilings under the rectangle group

Let $T$ be a finite set of tile
designs and let $n, m \ge 1$. Let $R$ be a subgroup of the dihedral group of order $8$, whose
elements are the rotations $r_i$ and reflections $sr_i$ for $i \in \mathbb{Z}/4\mathbb{Z}$, such
that every element of $R$ is one of $r_0$, $r_2$, $sr_0$, $sr_2$, and let $R$ act on $T$. Tilings
of the $n \times m$ torus are maps $F : \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z} \to T$.
Identify tilings under the equivalence relation generated by
$F \sim \bigl(c \mapsto g^{-1} \cdot F(g \cdot (c + v))\bigr)$ for
$v \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ and $g \in R$, where $g$ acts on cells
by the rectangle-group cell action. Then the number of equivalence classes is

$$\frac{1}{n m \lvert R \rvert} \sum_{g \in R} \mathrm{fix}_g,$$

where $\mathrm{fix}_g$ is the torus shift sum of the cell map of $g$ and the permutation
$t \mapsto g \cdot t$ of $T$, that is, the number of pairs $(v, F)$ of a shift
$v \in \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$ and a tiling $F$ with
$F(g \cdot (c + v)) = g \cdot F(c)$ for every cell $c$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 37 (`jis-2024-24.6.1-thm-37`).

Stated but not proved: `MetaMathlibExt.rectTorus_distinctTilings_burnside` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1056](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1056). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#rect-torus-distinct-tilings-burnside).

## Burnside count of tilings of the square torus

Let $n$ be a positive integer and let $T$
be a finite set of tile designs. Let $\rho(x, y) = (-1-y, x)$ and $\phi(x, y) = (-1-x, y)$ on the
cells $(\mathbb{Z}/n\mathbb{Z})^2$ of the $n \times n$ torus, and let the dihedral group
$D_8 = \langle r, f \rangle$ of the square act on cells by $r^i \cdot c = \rho^i(c)$ and
$fr^i \cdot c = \phi(\rho^i(c))$ for $i \in \mathbb{Z}/4\mathbb{Z}$. Let $R$ be a subgroup of
$D_8$ that acts on $T$, and write $g \cdot d$ for the action of $g \in R$ on a design $d \in T$.
Call two tilings $F, F' : (\mathbb{Z}/n\mathbb{Z})^2 \to T$ equivalent when they are related by
the equivalence relation generated by: $F'(c) = g^{-1} \cdot F(g \cdot (c + v))$ for every cell
$c$, for some $v \in (\mathbb{Z}/n\mathbb{Z})^2$ and $g \in R$. Then the number of equivalence
classes is

$$\frac{1}{n^2 |R|} \sum_{g \in R} \sum_{v \in (\mathbb{Z}/n\mathbb{Z})^2} N(g, v),$$

where $N(g, v)$ is the number of tilings $F$ with $F(g \cdot (c + v)) = g \cdot F(c)$ for every
cell $c$; the inner sum is the torus shift sum of $g$.

## Sources

- Peter Kagey, William Keehn, *Counting Tilings of the n × m Grid, Cylinder, and Torus*, Journal of Integer Sequences 27 (2024), Article 24.6.1, Theorem 41 (`jis-2024-24.6.1-thm-41`).

Stated but not proved: `MetaMathlibExt.squareTorus_distinctTilings_burnside` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean, line 1076](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GridCylinderTorusTilingsWanted.lean#L1076). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html#square-torus-distinct-tilings-burnside).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tilings of grids, cylinders and tori up to symmetry](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/tilings-board-placements/tilings-of-grids-cylinders-and-tori-up-to-symmet)
