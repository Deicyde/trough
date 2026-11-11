---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Nonogram.NonogramInstance, MetaMathlibExt.Complexity.NPComplete.Nonogram.RunsStep, MetaMathlibExt.Complexity.NPComplete.Nonogram.Runs, MetaMathlibExt.Complexity.NPComplete.Nonogram.NonogramFeasible, MetaMathlibExt.Complexity.NPComplete.Nonogram.nonogramDec, MetaMathlibExt.Complexity.NPComplete.Nonogram.nonogram_npComplete
statement: formalized
---

# Nonogram

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html).

## Nonogram instances

A nonogram instance is a pair $(R, C)$ of finite lists, the row clues
$R$ and the column clues $C$, where each clue is a finite list of natural numbers.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Nonogram.NonogramInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#nonogram-instance).

## One step of the run-length computation

For a Boolean $b$ and a pair $(k, R)$ of a
natural number $k$ and a finite list $R$ of natural numbers, the step returns $(k + 1, R)$ if $b$
is true. If $b$ is false it returns $(0, R)$ when $k = 0$, and $(0, R')$ when $k > 0$, where $R'$
is the list $R$ with $k$ prepended.

Here $k$ is the length of the current run of true cells and $R$ is the list of completed runs.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Nonogram.RunsStep`, a definition declared in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#runs-step).

## Run lengths of a row

For a finite list $l$ of Booleans, the runs of $l$ are its maximal
blocks of consecutive true entries. The run list of $l$ is the list of the lengths of these
blocks, in order from left to right; it is empty when $l$ has no true entry.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Nonogram.Runs`, a definition declared in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#runs).

## Feasible nonogram instances

A nonogram instance with row clues $R_0, \dots, R_{m-1}$ and
column clues $C_0, \dots, C_{n-1}$ is feasible when there is a picture, a list of $m$ rows of
Booleans each of length $n$, such that for every $r < m$ the run list of row $r$ equals $R_r$,
and for every $c < n$ the run list of column $c$, read from row $0$ to row $m - 1$, equals $C_c$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Nonogram.NonogramFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#nonogram-feasible).

## The NONOGRAM decision problem

NONOGRAM is the decision problem that accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding of nonogram instances, to a
feasible nonogram instance. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Nonogram.nonogramDec`, a definition declared in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#nonogram-dec).

## NONOGRAM is NP-complete

The NONOGRAM decision problem belongs to NP, and every decision
problem in NP reduces to NONOGRAM by a polynomial-time many-one reduction.

## Sources

- N. Ueda and T. Nagao, "NP-completeness results for nonogram via parsimonious reductions" (1996).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Nonogram.nonogram_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/NonogramWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/NonogramWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html#nonogram-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nonogram](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/nonogram)
