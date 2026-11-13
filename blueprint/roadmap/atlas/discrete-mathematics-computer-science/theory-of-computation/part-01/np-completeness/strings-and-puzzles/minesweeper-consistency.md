---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Minesweeper.MinesweeperInstance, MetaMathlibExt.Complexity.NPComplete.Minesweeper.WellFormed, MetaMathlibExt.Complexity.NPComplete.Minesweeper.MinesweeperFeasible, MetaMathlibExt.Complexity.NPComplete.Minesweeper.minesweeperDec, MetaMathlibExt.Complexity.NPComplete.Minesweeper.minesweeper_npComplete
statement: formalized
---

# Minesweeper consistency

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html).

## Minesweeper instances

A Minesweeper instance consists of a number of rows $R$, a number of
columns $C$ and a finite list of clues, where $R$ and $C$ are natural numbers and each clue is a
triple $(r, c, k)$ of natural numbers giving a row $r$, a column $c$ and the number $k$ shown.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Minesweeper.MinesweeperInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinesweeperWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinesweeperWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html#minesweeper-instance).

## Well-formed Minesweeper instances

A Minesweeper instance with $R$ rows, $C$ columns and a
list of clues is well formed when every clue $(r, c, k)$ in the list satisfies $r < R$, $c < C$
and $k \le 8$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Minesweeper.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinesweeperWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinesweeperWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html#well-formed).

## Feasible Minesweeper instances

Index rows and columns by natural numbers, and call a cell
$(r', c') \ne (r, c)$ a neighbour of $(r, c)$ when $|r' - r| \le 1$ and $|c' - c| \le 1$. A
Minesweeper instance with $R$ rows, $C$ columns and a list of clues is feasible when there is a
finite set $M$ of cells $(r, c)$ with $r < R$ and $c < C$ (the mines) such that for every clue
$(r, c, k)$ in the list the cell $(r, c)$ is not in $M$ and exactly $k$ cells of $M$ are
neighbours of $(r, c)$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Minesweeper.MinesweeperFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinesweeperWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinesweeperWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html#minesweeper-feasible).

## Minesweeper consistency as a decision problem

The Minesweeper consistency decision
problem accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding,
to a Minesweeper instance that is well formed and feasible, that is, admits a mine placement
consistent with all of its clues. It rejects every bitstring that does not decode to a Minesweeper
instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Minesweeper.minesweeperDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinesweeperWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinesweeperWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html#minesweeper-dec).

## MINESWEEPER CONSISTENCY is NP-complete

The Minesweeper consistency decision problem lies
in NP, and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- R. Kaye, "Minesweeper is NP-complete" (2000).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Minesweeper.minesweeper_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinesweeperWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinesweeperWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html#minesweeper-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minesweeper consistency](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/minesweeper-consistency)
