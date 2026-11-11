---
declaration: section
origin: cited
lean: MetaMathlibExt.ferrersBoardCells, MetaMathlibExt.ferrersBoardCells_card_1124, MetaMathlibExt.filePlacements, MetaMathlibExt.levelRookPlacements, MetaMathlibExt.levelRookNumber, MetaMathlibExt.mFallingFactorial, MetaMathlibExt.mFallingFactorial_one_three_two, MetaMathlibExt.filePlacementWeight
statement: formalized
---

# Weighted file placements on Ferrers boards

24 results, 15 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html).

## Cells of a Ferrers board

For a list $b = (b_1, \ldots, b_n)$ of natural numbers, the
cells of the Ferrers board with column heights $b$ are the pairs $(i, r)$ of natural numbers with
$i < n$ and $r < b_{i+1}$; columns and rows are numbered from $0$, so column $i$ has height
$b_{i+1}$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 2.1 (definition of the Ferrers board `B = (b_1, …, b_n)`).

Formalized by `MetaMathlibExt.ferrersBoardCells`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#ferrers-board-cells).

## The board $(1, 1, 2, 4)$ has eight cells

The Ferrers board with column heights
$(1, 1, 2, 4)$, the board $B_1$ of Figure 2, has exactly $8$ cells.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Figure 2.

Formalized by `MetaMathlibExt.ferrersBoardCells_card_1124`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#ferrers-board-cells-card-1124).

## File placements

A file placement on the Ferrers board with column heights $b$ is a set of
cells of the board no two of which lie in the same column.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 3.1 (definition of a file placement).

Formalized by `MetaMathlibExt.filePlacements`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#file-placements).

## Level rook placements

Let $m$ be a natural number and let $B$ be the board with column
heights $b_1, \dots, b_n$, rows numbered from $0$, where row $r$ lies in level $\lfloor r/m \rfloor$
(every row lies in level $0$ when $m = 0$). An $m$-level rook placement on $B$ is a file placement
on $B$, that is a set of cells of $B$ with no two in the same column, that has no two cells in the
same level.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 2.2 (definition of `m`-level rook placements, after Briggs and Remmel).

Formalized by `MetaMathlibExt.levelRookPlacements`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-placements).

## Level rook number

Let $m$ and $k$ be natural numbers and let $B$ be the board with column
heights $b_1, \dots, b_n$, with rows numbered from $0$, where row $r$ lies in level
$\lfloor r/m \rfloor$ (every row lies in level $0$ when $m = 0$). The $k$-th $m$-level rook number
$r_{k,m}(B)$ is the number of $m$-level rook placements on $B$ with exactly $k$ cells, that is, of
sets of $k$ cells of $B$ with no two in the same column and no two in the same level.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 2.2.

Formalized by `MetaMathlibExt.levelRookNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-number).

## The $m$-falling factorial

For an integer $x$ and natural numbers $k$ and $m$, the
$m$-falling factorial is the integer
$x\downarrow_{k,m} = \prod_{i=0}^{k-1} (x - mi) = x(x-m)\cdots(x-(k-1)m)$, which is $1$ for $k = 0$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 2.2 (definition of the `m`-falling factorial).

Formalized by `MetaMathlibExt.mFallingFactorial`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#m-falling-factorial).

## The value $1\downarrow_{3,2} = 3$

The $2$-falling factorial of $1$ with three factors is
$1\downarrow_{3,2} = 1 \cdot (1 - 2) \cdot (1 - 4) = 3$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 4 (value `1↓_{3,2} = 3` after Lemma 8).

Formalized by `MetaMathlibExt.mFallingFactorial_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#m-falling-factorial-one-three-two).

## The $m$-weight of a file placement

For a natural number $m$ and a finite set $F$ of cells
$(i, j)$ (column $i$, row $j$), let $f_j$ be the number of cells of $F$ in row $j$. The $m$-weight
of $F$ is $\mathrm{wt}_m(F) = \prod_j 1\downarrow_{f_j, m}$, the product over the rows $j$ that
contain a cell of $F$, where $x\downarrow_{k, m} = \prod_{i < k} (x - m i)$ is the $m$-falling
factorial.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 3.1 (definition of `wt_m`).

Formalized by `MetaMathlibExt.filePlacementWeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#file-placement-weight).

## The $3$-weight of the placement of Figure 4

The file placement $F$ consisting of the cells
$(0, 1)$, $(1, 1)$, $(2, 3)$, $(3, 3)$ and $(4, 3)$, written as (column, row) and numbered from
$0$, has two cells in the second row and three in the fourth, and its $3$-weight is
$\mathrm{wt}_3(F) = -20$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Figure 4 and the computation of `wt_3(F)`.

Formalized by `MetaMathlibExt.filePlacementWeight_figure_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#file-placement-weight-figure-four).

## Weighted file placement numbers

For a board $B$ given by a list of column heights and for
$m, k \in \mathbb{N}$, the $k$-th $m$-weighted file placement number of $B$ is the integer
$f_{k,m}(B) = \sum_F \mathrm{wt}_m(F)$, where $F$ runs over the file placements on $B$ with exactly
$k$ cells and $\mathrm{wt}_m(F)$ is the $m$-weight of $F$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 3.1.

Formalized by `MetaMathlibExt.weightedFileNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#weighted-file-number).

## Two rooks on the $2 \times 2$ board with $m = 2$

For the board $B = (2, 2)$, the number
$r_{2,2}(B)$ of $2$-level rook placements of two rooks on $B$ is $0$, and the weighted file
placement number $f_{2,2}(B)$, the sum of the $2$-weights of the file placements of two rooks
on $B$, is also $0$.

The four file placements of two rooks have $2$-weights $1, 1, -1, -1$, which cancel.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 3.2 (cancellation of the weights of non-rook file placements).

Formalized by `MetaMathlibExt.levelRookNumber_weightedFileNumber_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-number-weighted-file-number-t).

## Singleton boards

For natural numbers $h$ and $m$, write $\lfloor h \rfloor_m$ for the
largest multiple of $m$ that is at most $h$. A list $b = (b_1, \ldots, b_n)$ of natural numbers
is a singleton board for $m$ when it is weakly increasing (the column heights of a Ferrers board)
and, for every $1 \le i < n$, $b_i - \lfloor b_i \rfloor_m \ne 0$ implies
$\lfloor b_i \rfloor_m < \lfloor b_{i+1} \rfloor_m$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 2.2 (definition of singleton boards).

Formalized by `MetaMathlibExt.IsSingletonBoard`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#is-singleton-board).

## A singleton board for $2$ but not for $3$

The Ferrers board with column heights
$(1, 2, 2, 3)$ is a singleton board for $m = 2$ and is not a singleton board for $m = 3$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Figure 3 and the discussion after it.

Formalized by `MetaMathlibExt.isSingletonBoard_1223`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#is-singleton-board-1223).

## Goldman–Joichi–White factorization theorem

Let $B = (b_1, \dots, b_n)$ be a Ferrers
board, that is $b_1 \le \dots \le b_n$, and let $r_k(B) = r_{k,1}(B)$ be the number of placements
of $k$ non-attacking rooks on $B$ (no two in the same row or column). Then for every integer $x$,

$$
\sum_{k=0}^{n} r_k(B)\, x\downarrow_{n-k} = \prod_{i=1}^{n} \bigl(x + b_i - (i-1)\bigr),
$$

where $x\downarrow_j = x(x-1)\cdots(x-j+1)$ is the falling factorial, the $m$-falling factorial
for $m = 1$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 1 (Goldman, Joichi and White).

Stated but not proved: `MetaMathlibExt.rookNumber_factorization` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#rook-number-factorization).

## Briggs–Remmel factorization on singleton boards

Let $m \ge 1$ and let
$B = (b_1, \dots, b_n)$ be a singleton board for $m$. Then for every integer $x$,

$$
\sum_{k=0}^{n} r_{k,m}(B)\, x\downarrow_{n-k,m} = \prod_{i=1}^{n} \bigl(x + b_i - m(i-1)\bigr),
$$

where $r_{k,m}(B)$ is the $k$-th $m$-level rook number of $B$ and
$x\downarrow_{k,m} = x(x-m)\cdots(x-(k-1)m)$ is the $m$-falling factorial.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 2 (Briggs and Remmel).

Stated but not proved: `MetaMathlibExt.levelRookNumber_factorization_of_singleton` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-number-factorization-of-singl).

## Zone factorization of the $m$-level rook polynomial

Let $m \ge 1$ and let
$B = (b_1, \dots, b_n)$ be a Ferrers board, that is $b_1 \le \dots \le b_n$. Write
$\lfloor b \rfloor_m = m \lfloor b/m \rfloor$ for the largest multiple of $m$ that is at most $b$,
and $\rho_i = b_i - \lfloor b_i \rfloor_m$. The zone of column $i$ is the set $z$ of columns $k$
with $\lfloor b_k \rfloor_m = \lfloor b_i \rfloor_m$ (a maximal run of consecutive columns, since
the heights increase weakly), and $\rho_z = \sum_{k \in z} \rho_k$. Column $i$ is last in its zone
when $i = n$ or $\lfloor b_{i+1} \rfloor_m \ne \lfloor b_i \rfloor_m$. Let $\varepsilon_i = \rho_z$,
for $z$ the zone of $i$, if column $i$ is last in its zone, and $\varepsilon_i = 0$ otherwise.
Then for every integer $x$,

$$
\sum_{k=0}^{n} r_{k,m}(B)\, x\downarrow_{n-k,m} =
\prod_{i=1}^{n} \bigl(x + \lfloor b_i \rfloor_m - m(i-1) + \varepsilon_i\bigr),
$$

where $r_{k,m}(B)$ is the $k$-th $m$-level rook number of $B$ and
$x\downarrow_{k,m} = x(x-m)\cdots(x-(k-1)m)$ is the $m$-falling factorial.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 3 (Barrese, Loehr, Remmel and Sagan).

Stated but not proved: `MetaMathlibExt.levelRookNumber_factorization_zones` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-number-factorization-zones).

## Level-number factorization of the $m$-level rook polynomial

Let $m \ge 1$ and let
$B = (b_1, \dots, b_n)$ be a Ferrers board, that is $b_1 \le \dots \le b_n$, with $b_i \le mn$ for
every $i$. Number the rows from $0$ at the bottom, so that column $i$ has the cells in rows
$0, \dots, b_i - 1$, and for $1 \le j \le n$ let $l_j$ be the number of cells of $B$ whose row $r$
satisfies $\lfloor r/m \rfloor = n - j$ (the $j$-th level from the top). Then for every integer $x$,

$$
\sum_{k=0}^{n} r_{k,m}(B)\, x\downarrow_{n-k,m} = \prod_{j=1}^{n} \bigl(x + l_j - m(j-1)\bigr),
$$

where $r_{k,m}(B)$ is the $k$-th $m$-level rook number of $B$ and
$x\downarrow_{k,m} = x(x-m)\cdots(x-(k-1)m)$ is the $m$-falling factorial.

The bound $b_i \le mn$ makes $B$ lie in $n$ levels, as in the paper's setting; without it the
formula fails ($m = 1$, $B = (2)$).

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 4 (Barrese, Loehr, Remmel and Sagan).

Stated but not proved: `MetaMathlibExt.levelRookNumber_factorization_levels` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#level-rook-number-factorization-levels).

## Factorization theorem for weighted file placements

Let $m \ge 1$ and let $B$ be a Ferrers
board with $n$ columns of weakly increasing heights $b_0 \le b_1 \le \dots \le b_{n-1}$ (columns
indexed from $0$). Then for every integer $x$,

$$\sum_{k=0}^{n} f_{k,m}(B)\, x\downarrow_{n-k,m} = \prod_{i=0}^{n-1} (x + b_i - mi),$$

where $f_{k,m}(B)$ is the $k$-th $m$-weighted file placement number of $B$ and
$x\downarrow_{j,m} = \prod_{i\lt j} (x - mi)$ is the $m$-falling factorial.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 5 (Barrese, Loehr, Remmel and Sagan).

Stated but not proved: `MetaMathlibExt.weightedFileNumber_factorization` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#weighted-file-number-factorization).

## Weighted file numbers equal level rook numbers on singleton boards

Let $m \ge 1$ and let
$B$ be a singleton board for $m$. Then for every $k \in \mathbb{N}$ the $k$-th $m$-weighted file
placement number of $B$ equals its $k$-th $m$-level rook number: $f_{k,m}(B) = r_{k,m}(B)$.

Equivalently, the $m$-weights of the file placements with $k$ cells that are not $m$-level rook
placements sum to $0$. The paper prints the corollary as the polynomial identity
$\sum_k f_{k,m}(B)\, x\downarrow_{n-k,m} = \sum_k r_{k,m}(B)\, x\downarrow_{n-k,m}$, where $n$ is
the number of columns and $x\downarrow_{j,m} = \prod_{i\lt j} (x - mi)$; it follows by summing, and the
paper derives it from this cancellation for each $k$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Corollary 6 and the sentence before it.

Stated but not proved: `MetaMathlibExt.weightedFileNumber_eq_levelRookNumber_of_singleton` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#weighted-file-number-eq-level-rook-numbe).

## The chosen level and its leftmost cell

Let $m$ be a natural number and $F_0$ a finite set
of cells $(i, r)$ (column $i$, row $r$), and call the rows $r$ with $\lfloor r/m \rfloor = l$
level $l$ (for $m = 0$, every row lies in level $0$). A level $l$ and a cell $c_0$ are chosen for
$F_0$ when level $l$ contains at least two cells of $F_0$; every level $l'$ containing at least
two cells of $F_0$ contains strictly more cells of $F_0$ than level $l$, or exactly as many with
$l \le l'$; and $c_0$ is a cell of $F_0$ in level $l$ whose column is at most the column of every
cell of $F_0$ in level $l$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 4 (choice of the level `l` and its leftmost rook).

Formalized by `MetaMathlibExt.IsChosenLevelAndLeftmost`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#is-chosen-level-and-leftmost).

## The block $P(F_0)$

Let $B$ be the Ferrers board with column heights $b$, let $m$ and $l$
be natural numbers, and call the rows $r$ with $\lfloor r/m \rfloor = l$ level $l$ (for $m = 0$,
every row lies in level $0$). For a set $F_0$ of cells and a cell $c_0$, the block $P(F_0)$ is
the set of file placements $F$ on $B$ such that $F$ and $F_0$ have the same cells outside level
$l$, the cells of $F$ in level $l$ occupy exactly the same columns as the cells of $F_0$ in level
$l$, and $c_0 \in F$.

In Section 4, $l$ is the chosen level of $F_0$ and $c_0$ is the leftmost cell of $F_0$ in it.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Section 4 (definition of `P(F₀)`).

Formalized by `MetaMathlibExt.filePlacementBlock`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#file-placement-block).

## Size of the block $P(F_0)$

Let $m \ge 2$, let $B$ be a singleton board for $m$, and call
the rows $r$ with $\lfloor r/m \rfloor = l$ level $l$. Let $F_0$ be a file placement on $B$ that is
not an $m$-level rook placement, let $l$ and $c_0$ be its chosen level and the leftmost cell of
$F_0$ in that level, and suppose level $l$ contains $n$ cells of $F_0$. Then the block $P(F_0)$
determined by $l$ and $c_0$ has exactly $m^{n-1}$ members.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Lemma 7.

Stated but not proved: `MetaMathlibExt.filePlacementBlock_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#file-placement-block-card).

## Weights cancel on a block with two rooks in the chosen level

Let $m \ge 2$, let $B$ be a
singleton board for $m$, with rows numbered from $0$ and row $r$ in level $\lfloor r/m \rfloor$,
and let $F_0$ be a file placement on $B$. Let $l$ be the chosen level of $F_0$ (among the levels
holding at least two cells of $F_0$, one holding the fewest, the lowest on ties) and $c_0$ the
leftmost cell of $F_0$ in level $l$, and suppose that level $l$ holds exactly two cells of $F_0$.
Then the $m$-weights $\operatorname{wt}_m(F)$ of the file placements $F$ in the block $P(F_0)$
sum to $0$, where $P(F_0)$ consists of the file placements on $B$ that agree with $F_0$ outside
level $l$, use the same columns as $F_0$ inside level $l$, and contain $c_0$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Lemma 8.

Stated but not proved: `MetaMathlibExt.sum_filePlacementWeight_block_of_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#sum-file-placement-weight-block-of-two).

## Cancellation of the weights over a block

Let $m \ge 2$ and let $B$ be a singleton board
for $m$. Let $F_0$ be a file placement on $B$ that is not an $m$-level rook placement. Let $l$ be a
level and $c_0$ a cell such that $l$ holds at least two cells of $F_0$ and holds the fewest cells
of $F_0$ among all such levels (the lowest such level on ties), and $c_0$ is the leftmost cell of
$F_0$ in level $l$. Then the $m$-weights of the file placements in the block $P(F_0)$ determined
by $l$ and $c_0$ sum to $0$: $\sum_{F \in P(F_0)} \mathrm{wt}_m(F) = 0$.

## Sources

- Kenny Barrese, *Weighted File Placements on Singleton Boards*, INTEGERS 24 (2024), Article A58, Theorem 9.

Stated but not proved: `MetaMathlibExt.sum_filePlacementWeight_block` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedFilePlacementsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html#sum-file-placement-weight-block).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted file placements on Ferrers boards](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/weighted-file-placements-on-ferrers-boards)
