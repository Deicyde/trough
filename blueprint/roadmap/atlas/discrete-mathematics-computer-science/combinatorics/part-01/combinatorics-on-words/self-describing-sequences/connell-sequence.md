---
declaration: section
origin: cited
lean: MetaMathlibExt.connellRowLength, MetaMathlibExt.connellRowStart, MetaMathlibExt.connellEntry, MetaMathlibExt.connellRowEntries, MetaMathlibExt.ConnellParameters, MetaMathlibExt.connellNext, MetaMathlibExt.connellPosition, MetaMathlibExt.connellSequence
statement: formalized
proof: formalized
---

# Connell sequence

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html).

## Row lengths of the Connell triangle

For natural numbers $r$ and $j$, the length of
row $j$ is $1 + r(j - 1)$, where $j - 1$ is read as $0$ when $j = 0$. For $j \ge 1$ this is the
number of entries in row $j$ of the Connell $(m, r)$ triangle for every $m$; the source numbers
rows from one, and the value at $j = 0$ is a convention.

Formalized by `MetaMathlibExt.connellRowLength`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-row-length).

## First entries of the rows of the Connell triangle

For natural numbers $m$ and $r$, the
numbers $s_j$ are defined by $s_0 = s_1 = 1$ and $s_{j+1} = s_j + m(\ell_j - 1) + 1$ for
$j \ge 1$, where $\ell_j = 1 + r(j - 1)$ is the length of row $j$. For $j \ge 1$, $s_j$ is the
first entry of row $j$ of the Connell $(m, r)$ triangle: each row starts one above the last
entry $s_j + m(\ell_j - 1)$ of the row before. The source numbers rows from one, and the value
$s_0 = 1$ is a convention.

Formalized by `MetaMathlibExt.connellRowStart`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-row-start).

## Entries of the Connell triangle

For natural numbers $m$, $r$, $j$ and $k$, the entry with
zero-based index $k$ in row $j$ of the Connell $(m, r)$ triangle is $s_j + mk$, where $s_j$ is the
first entry of row $j$. The formula is used for every $k$, also at or beyond the row length.

Formalized by `MetaMathlibExt.connellEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-entry).

## Rows of the Connell triangle

For natural numbers $m$, $r$ and $j$, row $j$ of the
Connell $(m, r)$ triangle is the finite set of the numbers $s_j + mk$ with $0 \le k < \ell_j$, where
$s_j$ is the first entry of row $j$ and $\ell_j = 1 + r(j - 1)$ is its length, with $j - 1$ read
as $0$ when $j = 0$.

Formalized by `MetaMathlibExt.connellRowEntries`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-row-entries).

## Connell parameters

A pair of natural numbers $(m, r)$ with $m \ge 2$ and $r \ge 1$; these
are the admissible parameters of a Connell $(m, r)$ sequence.

Formalized by `MetaMathlibExt.ConnellParameters`, a structure declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-parameters).

## Next position in the Connell triangle

For a natural number $r$, the position following
row $j$, zero-based column $k$, is row $j$, column $k + 1$ if $k + 1 < 1 + r(j - 1)$ (the length
of row $j$, with $j - 1$ read as $0$ when $j = 0$), and row $j + 1$, column $0$ otherwise.

Formalized by `MetaMathlibExt.connellNext`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-next).

## Position of a term in the Connell triangle

For a natural number $r$, the position
$p_n = (j_n, k_n)$ (row $j_n$, zero-based column $k_n$) of index $n \ge 0$ is defined by
$p_0 = (1, 0)$ and $p_{n+1} = (j_n, k_n + 1)$ if $k_n + 1 < 1 + r(j_n - 1)$ (the length of row
$j_n$, with $j_n - 1$ read as $0$ when $j_n = 0$), and $p_{n+1} = (j_n + 1, 0)$ otherwise.

Formalized by `MetaMathlibExt.connellPosition`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-position).

## Connell sequence

For natural numbers $m \ge 2$ and $r \ge 1$, the Connell $(m, r)$
sequence $(a_n)_{n \ge 0}$ reads the Connell triangle row by row: row $j \ge 1$ has
$\ell_j = 1 + r(j - 1)$ entries $s_j, s_j + m, \dots, s_j + m(\ell_j - 1)$, where $s_1 = 1$ and
$s_{j+1} = s_j + m(\ell_j - 1) + 1$. Thus $a_n = s_j + mk$, where row $j$, zero-based column $k$
is the position reached from row $1$, column $0$ after $n$ steps, each step moving one column
right within a row and from the last entry of a row to the first entry of the next.

Formalized by `MetaMathlibExt.connellSequence`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ConnellSequence.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html#connell-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Connell sequence](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/connell-sequence)
