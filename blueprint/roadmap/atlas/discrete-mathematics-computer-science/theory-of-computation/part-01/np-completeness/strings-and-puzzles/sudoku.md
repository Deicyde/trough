---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Sudoku.SudokuInstance, MetaMathlibExt.Complexity.NPComplete.Sudoku.WellFormed, MetaMathlibExt.Complexity.NPComplete.Sudoku.SudokuFeasible, MetaMathlibExt.Complexity.NPComplete.Sudoku.sudokuDec, MetaMathlibExt.Complexity.NPComplete.Sudoku.sudoku_npComplete
statement: formalized
---

# Sudoku

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html).

## Sudoku instances

A Sudoku instance is a pair $(n, G)$ of a natural number $n$, the block
size, and a grid $G$ given as a finite list of rows, each row a finite list of natural numbers;
an entry $0$ stands for a blank cell.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Sudoku.SudokuInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SudokuWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SudokuWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html#sudoku-instance).

## Well-formed Sudoku instances

A Sudoku instance $(n, G)$, with block size $n$ and grid $G$
a list of rows of natural numbers, is well formed when $n > 0$, $G$ has exactly $n^2$ rows, every
row of $G$ has exactly $n^2$ entries, and every entry of $G$ is at most $n^2$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Sudoku.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SudokuWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SudokuWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html#well-formed).

## Feasible Sudoku instances

A Sudoku instance $(n, G)$, with block size $n$ and grid $G$ a
list of rows of natural numbers, is feasible when there is a grid $C$ of natural numbers with
exactly $n^2$ rows, each of exactly $n^2$ entries, such that, indexing rows and columns from $0$:
for all $r, c < n^2$ the entry $G_{rc}$ is $0$ or equals $C_{rc}$, where an entry missing from
$G$ counts as $0$; every row of $C$ and every column of $C$ lists each of $1, \dots, n^2$ exactly
once; and for all $b, b' < n$ the $n^2$ entries $C_{bn + i,\, b'n + j}$ with $i, j < n$ list each
of $1, \dots, n^2$ exactly once.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Sudoku.SudokuFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SudokuWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SudokuWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html#sudoku-feasible).

## SUDOKU as a decision problem

The decision problem SUDOKU accepts a bitstring $x$ exactly
when $x$ decodes, under the canonical bitstring encoding of pairs of a natural number and a finite
list of finite lists of natural numbers, to a Sudoku instance that is well formed and feasible.
It rejects every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Sudoku.sudokuDec`, a definition declared in [WantedExt/Complexity/NPComplete/SudokuWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SudokuWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html#sudoku-dec).

## SUDOKU is NP-complete

The decision problem SUDOKU lies in NP, and every decision problem
in NP has a polynomial-time many-one reduction to SUDOKU.

## Sources

- T. Yato and T. Seta, "Complexity and completeness of finding another solution and its application to puzzles" (2003).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Sudoku.sudoku_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SudokuWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SudokuWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html#sudoku-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sudoku](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/sudoku)
