---
declaration: section
origin: cited
lean: MetaMathlibExt.TilingCell, MetaMathlibExt.TilingCell.Adjacent, MetaMathlibExt.IsSquareOrDomino, MetaMathlibExt.isSquareOrDomino_iff, MetaMathlibExt.IsSquareDominoTiling, MetaMathlibExt.IsVerticalFaultFree, MetaMathlibExt.verticalFaultFreeTilingCount, MetaMathlibExt.tilingCount
statement: formalized
proof: formalized
---

# Fault-free tilings of 3 × n rectangles

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html).

## Cells of the $3 \times n$ rectangle

A cell of the $3 \times n$ rectangle is a pair
$(r, c)$ of a row $r \in \{0, 1, 2\}$ and a column $c \in \{0, \dots, n-1\}$.

Formalized by `MetaMathlibExt.TilingCell`, an abbreviation declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#tiling-cell).

## Adjacent cells

Two cells $x$ and $y$ of the $3 \times n$ rectangle are adjacent when they
share an edge: they lie in the same row and their columns differ by $1$, or they lie in the same
column and their rows differ by $1$.

Formalized by `MetaMathlibExt.TilingCell.Adjacent`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#adjacent).

## Square and domino tiles

A set $d$ of cells of the $3 \times n$ rectangle is a
square-or-domino tile when it consists of exactly one cell, or of exactly two cells that are
adjacent.

Formalized by `MetaMathlibExt.IsSquareOrDomino`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#is-square-or-domino).

## Characterization of square and domino tiles

A set $d$ of cells of the $3 \times n$
rectangle is a square-or-domino tile if and only if either $d = \{x\}$ for some cell $x$, or
$d = \{x, y\}$ for some distinct adjacent cells $x$ and $y$.

Formalized by `MetaMathlibExt.isSquareOrDomino_iff`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#is-square-or-domino-iff).

## Square-and-domino tilings

A square-and-domino tiling of the $3 \times n$ rectangle is a
finite family $T$ of sets of cells such that every member of $T$ is a square-or-domino tile (a
single cell or two adjacent cells), any two distinct members of $T$ are disjoint, and every cell
of the rectangle lies in some member of $T$.

Formalized by `MetaMathlibExt.IsSquareDominoTiling`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#is-square-domino-tiling).

## Vertical-fault-free families

A family $T$ of sets of cells of the $3 \times n$ rectangle,
with columns numbered $0, \dots, n-1$, is vertical-fault-free when for every natural number $k$
with $k + 1 < n$ some member of $T$ contains two cells of the same row lying in columns $k$ and
$k + 1$. For a square-and-domino tiling this says that every internal vertical boundary is
crossed by a horizontal domino.

Formalized by `MetaMathlibExt.IsVerticalFaultFree`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#is-vertical-fault-free).

## Number of vertical-fault-free tilings of the $3 \times n$ rectangle

For every natural
number $n$, this is the number of square-and-domino tilings of the $3 \times n$ rectangle that
are vertical-fault-free.

Formalized by `MetaMathlibExt.verticalFaultFreeTilingCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 1298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L1298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#vertical-fault-free-tiling-count).

## Recurrence sequence for vertical-fault-free $3 \times n$ tilings

The integer sequence
$(V_n)_{n \ge 0}$ is defined by $V_0 = 0$, $V_1 = 3$, $V_2 = 13$, $V_3 = 26$, $V_4 = 66$,
$V_5 = 154$, $V_6 = 380$ and $V_n = V_{n-1} + 4 V_{n-2} - V_{n-3} - V_{n-4}$ for $n \ge 7$.

The value $V_0 = 0$ is a placeholder; the source considers only $n \ge 1$.

Formalized by `MetaMathlibExt.tilingCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 1304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L1304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#tiling-count).

## Recurrence for vertical-fault-free tilings of the $3 \times n$ rectangle

For $n \ge 1$, let
$V_n$ be the number of vertical-fault-free tilings of the $3 \times n$ rectangle by unit squares
and dominoes. Then $V_1 = 3$, $V_2 = 13$, $V_3 = 26$, $V_4 = 66$, $V_5 = 154$, $V_6 = 380$, and
$V_n = V_{n-1} + 4 V_{n-2} - V_{n-3} - V_{n-4}$ for every $n \ge 7$.

Here $V_n$ counts the tilings directly; the recurrence is a theorem, not its definition.

Proof: The count is encoded by a transfer matrix over column profiles. An annihilating
polynomial for that matrix gives the recurrence after the six initial values.

## Sources

- Oluwatobi Jemima Alabi and Greg Dresden, "Fault-Free Tilings of the 3 × n Rectangle With Squares and Dominos," Journal of Integer Sequences 24 (2021), Article 21.1.2, theorem on vertical-fault-free `V_n` (unlabeled), lines 358–364, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Dresden/dresden7.tex>.

Formalized by `MetaMathlibExt.fault_free_3xn_tiling_recursion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean, line 1377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FaultFree3xnTiling.lean#L1377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html#fault-free-3xn-tiling-recursion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fault-free tilings of 3 × n rectangles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/fault-free-tilings-of-3-n-rectangles)
