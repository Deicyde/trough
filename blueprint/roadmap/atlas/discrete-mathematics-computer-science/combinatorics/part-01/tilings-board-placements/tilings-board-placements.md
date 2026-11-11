---
declaration: section
origin: cited
lean: MetaMathlibExt.quarter_period_factorizations, MetaMathlibExt.domino_tilings_L_grid_via_fibonacci
statement: formalized
---

# Tilings, dimers and board placements: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/index.html).

Covering and placement problems on lattices and boards: domino and lozenge tilings and perfect matchings of grid regions (Aztec diamonds, Möbius grids, cylinders and tori), polyominoes and polycubes, tilings of groups by translates and the periodic tiling conjecture, nonattacking chess pieces, rook and file placements on Ferrers boards, and self-avoiding walks on lattices.

## Quarter-period factorizations of the triangular tiling numbers

Let
$Q \colon \mathbb{N} \to \mathbb{N}$ satisfy $Q(0) = Q(1) = 1$, $Q(2) = 4$ and
$Q(n) = Q(n-1) + 3Q(n-2) + Q(n-3)$ for every $n \ge 3$. Then for every $m \ge 1$,

$$Q(4m) = (2Q(2m-1) + 1)(2Q(2m) - 1),$$



$$Q(4m+1) = (2Q(2m) - 1)^2,$$



$$Q(4m+2) = 2(Q(2m-1) + Q(2m))(Q(2m) + Q(2m+1)),$$



$$Q(4m+3) = 2(Q(2m) + Q(2m+1))^2.$$

All values of $Q$ are at least $1$, so the subtractions above are exact. In the source, $Q(n)$ is
the number of tilings of a triangular strip.

## Sources

- Mark Shattuck, "Combinatorial Proofs of Some Formulas for Triangular Tilings," Journal of Integer Sequences 17 (2014), Article 14.5.5, Theorem (due to Bodeen et al.), lines 103–112, https://cs.uwaterloo.ca/journals/JIS/VOL17/Shattuck/shattuck8.tex

Formalized by `MetaMathlibExt.quarter_period_factorizations`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TriangularStripTilings.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TriangularStripTilings.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/index.html#quarter-period-factorizations).

## Tauraso's Cassini-type identity

Let $f_n$ be the Fibonacci numbers, with $f_0 = 0$ and
$f_1 = 1$. For natural numbers $n, m$ put $L_{n,m} = f_{n+1} f_m + f_n f_{m+1}$ and
$a_n = f_{n+1} f_{n-1} + f_n^2$, where $n - 1$ is truncated subtraction. Then
$L_{n,m} = f_{n+1} f_m + f_n f_{m+1}$ for all $n, m \ge 1$, $L_{n,n-1} = a_n$ for all
$n \ge 2$, and $L_{n,n-1}^2 = L_{n,n} L_{n-1,n-1} + 1$ for all $n \ge 2$.

In the source $L_{n,m}$ is the number of domino tilings of the L-grid, and the Fibonacci
formula for it is a theorem. Here $L_{n,m}$ is defined by that formula, so the first two
equations hold by definition and the content is the Cassini-type identity.

## Sources

- Roberto Tauraso, "A New Domino Tiling Sequence," Journal of Integer Sequences 7 (2004), Article 04.2.3, Lemma (Section 2, equations Lformula and Lcassini), lines 200–221, https://cs.uwaterloo.ca/journals/JIS/VOL7/Tauraso/tauraso3.tex

Stated but not proved: `MetaMathlibExt.domino_tilings_L_grid_via_fibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LGridDominoTilingsWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LGridDominoTilingsWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/index.html#domino-tilings-l-grid-via-fibonacci).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tilings, dimers and board placements](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements)
