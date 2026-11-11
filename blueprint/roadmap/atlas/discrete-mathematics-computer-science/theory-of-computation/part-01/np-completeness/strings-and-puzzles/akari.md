---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Akari.AkariInstance, MetaMathlibExt.Complexity.NPComplete.Akari.Illuminates, MetaMathlibExt.Complexity.NPComplete.Akari.WellFormed, MetaMathlibExt.Complexity.NPComplete.Akari.AkariFeasible, MetaMathlibExt.Complexity.NPComplete.Akari.akariDec, MetaMathlibExt.Complexity.NPComplete.Akari.akari_npComplete
statement: formalized
---

# Akari

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html).

## Akari boards

An Akari instance is a board given as a list of rows, each row a list of
natural numbers: the entry $0$ is an empty cell, $1$ is a wall, and $2 + k$ is a wall numbered $k$.
The rows need not have the same length; that is part of well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Akari.AkariInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#akari-instance).

## Illumination on an Akari board

Let $B$ be a board, a list of rows of natural numbers, and
write $B_{r,c}$ for the entry in row $r$ and column $c$, read as $1$ when there is no such entry. A
bulb at $(b_r, b_c)$ illuminates the cell $(r, c)$ when either $b_r = r$ and $B_{r,c'} = 0$ for
every column $c'$ strictly between $b_c$ and $c$, or $b_c = c$ and $B_{r',c} = 0$ for every row
$r'$ strictly between $b_r$ and $r$. In particular, a bulb illuminates its own cell.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Akari.Illuminates`, a definition declared in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#illuminates).

## Well-formed Akari boards

An Akari board is well formed when every entry is at most $6$
and all its rows have the same length.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Akari.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#well-formed).

## Feasible Akari boards

Let $B$ be an Akari board with $m$ rows, let $n$ be the length of its
first row ($n = 0$ when there are no rows), and write $B_{r,c}$ for the entry in row $r$ and column
$c$, read as $1$ when there is no such entry. The board $B$ is feasible when there is a finite set
$S$ of pairs of natural numbers (the bulbs) such that every bulb $(r, c) \in S$ has $r < m$,
$c < n$ and $B_{r,c} = 0$; every cell $(r, c)$ with $r < m$, $c < n$ and $B_{r,c} = 0$ is
illuminated by some bulb in $S$; no bulb in $S$ illuminates a different bulb in $S$; and for every
$(r, c)$ with $r < m$, $c < n$ and $B_{r,c} \ge 2$, the number of bulbs $(r', c') \in S$ with
$|r - r'| + |c - c'| = 1$ equals $B_{r,c} - 2$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Akari.AkariFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#akari-feasible).

## The Akari decision problem

The Akari (Light Up) decision problem accepts a list of
booleans $x$ exactly when $x$ decodes, under the canonical bitstring encoding of lists of lists of
natural numbers, to an Akari board that is well formed and feasible; it rejects every list that
does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Akari.akariDec`, a definition declared in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#akari-dec).

## AKARI (LIGHT UP) is NP-complete

The Akari decision problem belongs to NP, and every
decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- Brandon McPhail, "Light Up is NP-complete", unpublished manuscript, 2005.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Akari.akari_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/AkariWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AkariWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html#akari-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Akari](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/akari)
