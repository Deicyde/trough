---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.AztecCell, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.ciucuMatrix, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.edgeRow, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.edgeCol, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.ciucuWeight, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.dragonGraph, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.aztecDragonCount, MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.aztecDragonCount_holds
statement: formalized
---

# Aztec dragon tilings

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html).

## Cells of the Aztec diamond

For $m \in \mathbb{N}$, the cells of the Aztec diamond region of
order $m$ are the pairs of integers $(i, j)$ with $|2i + 1| + |2j + 1| \le 2m$. The pair $(i, j)$
stands for the unit square with lower-left corner $(i, j)$ and center $(i + \frac12, j + \frac12)$,
so the condition says that this center satisfies $|i + \frac12| + |j + \frac12| \le m$.

The Aztec diamond graph $AD_m$ has these $2m(m + 1)$ cells as vertices and joins two cells when
they share a side.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.AztecCell`, an abbreviation declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#aztec-cell).

## Ciucu's weight matrix for the Aztec dragon

Ciucu's periodic weight matrix of Section 7 (the
display before (7.1)) is the $4 \times 4$ matrix with natural number entries, rows and columns
indexed by $0, 1, 2, 3$,

$$A = \begin{pmatrix}1 & 1 & 1 & 1\\1 & 0 & 1 & 1\\0 & 1 & 1 & 1\\1 & 1 & 1 & 1\end{pmatrix}.$$

Its two zero entries, in positions $(1, 1)$ and $(2, 0)$, delete edges of the Aztec diamond
graph.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.ciucuMatrix`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#ciucu-matrix).

## Row index of an edge of the Aztec diamond

For $m \in \mathbb{N}$ and pairs of integers
$c = (c_1, c_2)$ and $d = (d_1, d_2)$, put $X = c_1 + d_1 + 1$ and $Y = c_2 + d_2 + 1$, the
doubled coordinates of the center of the edge joining $c$ and $d$. The row index of this edge is
$\lfloor (X + Y + 2m - 1) / 2 \rfloor$, so the rows of the $2m \times 2m$ array of edge centers of
the Aztec diamond graph $AD_m$ are the diagonals $X + Y = \mathrm{const}$, numbered
$0, \dots, 2m - 1$.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.edgeRow`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#edge-row).

## Column index of an edge of the Aztec diamond

For $m \in \mathbb{N}$ and pairs of integers
$c = (c_1, c_2)$ and $d = (d_1, d_2)$, put $X = c_1 + d_1 + 1$ and $Y = c_2 + d_2 + 1$, the
doubled coordinates of the center of the edge joining $c$ and $d$. The column index of this edge is
$\lfloor (X - Y + 2m - 1) / 2 \rfloor$, so the columns of the array of edge centers of the Aztec
diamond graph $AD_m$ are the diagonals $X - Y = \mathrm{const}$, numbered $0, \dots, 2m - 1$.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.edgeCol`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#edge-col).

## Ciucu's periodic weight

For $m \in \mathbb{N}$ and pairs of integers $c$ and $d$, let
$r$ and $s$ be the row and column indices of the pair $(c, d)$ in the array of edge centers of the
Aztec diamond graph $AD_m$. The weight $\mathrm{wt}_A(c, d)$ is the entry of Ciucu's matrix $A$ in
row $r \bmod 4$ and column $s \bmod 4$; that is, $A$ is placed in a corner of the array and
repeated with period $4$ in both directions (Ciucu's Definition 3.3).

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.ciucuWeight`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#ciucu-weight).

## The Aztec dragon graph

For $n \in \mathbb{N}$, the dragon graph of order $n$ is the graph
on the cells of the Aztec diamond of order $2n$ in which two cells $c$ and $d$ are adjacent when
they share a side (their coordinates differ by $1$ in exactly one place) and the edge joining them
has weight $\mathrm{wt}_A(c, d) = 1$ under Ciucu's periodic weight. It is the spanning subgraph of
the Aztec diamond graph $AD_{2n}$ obtained by deleting the edges of weight $0$; Ciucu's (7.1)
shows that its perfect matchings are equinumerous with the tilings of the Aztec dragon $R_n$.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.dragonGraph`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#dragon-graph).

## Propp's Aztec dragon count

The statement that for every natural number $n$ the dragon
graph of order $n$ (the spanning subgraph of the Aztec diamond graph $AD_{2n}$ that keeps exactly
the edges of weight $1$ under Ciucu's periodic weight $\mathrm{wt}_A$) has exactly $2^{n(n+1)}$
perfect matchings. This is Propp's Problem 15 in the form of Ciucu's (7.1) and Theorem 7.1 at
$a = 1$.

Formalized by `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.aztecDragonCount`, a definition declared in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#aztec-dragon-count).

## Perfect matchings of the Aztec dragon graph (Ciucu, Wieland)

For every natural number $n$,
the dragon graph of order $n$ (the spanning subgraph of the Aztec diamond graph $AD_{2n}$ that
keeps exactly the edges of weight $1$ under Ciucu's periodic weight $\mathrm{wt}_A$) has exactly
$2^{n(n+1)}$ perfect matchings.

Ciucu proves that the number of perfect matchings of $AD_{2n}$ with the periodic weight
$\mathrm{wt}_A$ is $2^{n(n+1)}$ (Theorem 7.1 at $a = 1$) and, by his identification (7.1) of these
matchings with the tilings of the Aztec dragon $R_n$, that $R_n$ has $2^{n(n+1)}$ tilings
(Corollary 7.2), as Propp's Problem 15 asks.

## Sources

- J. Propp, Twenty open problems in enumeration of matchings (1998), arXiv:math/9801060, Problem 15; resolution: M. Ciucu, Perfect matchings and perfect powers, J. Algebraic Combin. 17 (2003), 335-375, arXiv:math/0501521, Section 7 (The Aztec dragon): (7.1) M(R_n) = M(AD_2n; wt_A) for the displayed 4 × 4 matrix A; Theorem 7.1, M(AD_2n; wt_B) = (1 + a²)^(n(n+1)), where B at a = 1 is A; Corollary 7.2, T(R_n) = 2^(n(n+1)); Ciucu calls it an ex-conjecture of Propp first proved by B. Wieland (unpublished; Propp's progress report arXiv:math/9904150, Problem 15: 'Ben Wieland solved this problem'), https://arxiv.org/abs/math/0501521.

Stated but not proved: `MathlibExt.Combinatorics.AztecDragonPowerOfTwoAMR122Problem0015Wanted.aztecDragonCount_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AztecDragonPowerOfTwoAMR122Problem0015Wanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html#aztec-dragon-count-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aztec dragon tilings](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/aztec-dragon-tilings)
