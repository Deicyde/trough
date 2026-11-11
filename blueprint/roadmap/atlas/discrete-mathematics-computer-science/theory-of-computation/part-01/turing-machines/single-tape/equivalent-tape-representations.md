---
declaration: section
origin: cited
lean: Cslib.Turing.StackTape.toListBlank, Cslib.Turing.StackTape.toListBlank_nil, Cslib.Turing.StackTape.toListBlank_cons, Cslib.Turing.StackTape.head_toListBlank, Cslib.Turing.StackTape.tail_toListBlank, Cslib.Turing.StackTape.nth_toListBlank, Cslib.Turing.StackTape.toListBlank_mapSome, Cslib.Turing.StackTape.toListBlank_injective
statement: formalized
proof: formalized
---

# Equivalent tape representations

50 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html).

## Half-tape view of a stack tape

A stack tape $s$ over an alphabet $\Gamma$ is a finite list
of cells, each a symbol of $\Gamma$ or the blank cell, that does not end in a blank cell. Its
half-tape view is the half-tape of cells (a sequence of cells taken up to trailing blanks, the
blank cell being the default) whose cells are those of $s$ in order, followed by blank cells.

Formalized by `Cslib.Turing.StackTape.toListBlank`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-2).

## Half-tape view of the empty stack tape

The half-tape view of the empty stack tape over
$\Gamma$ is the half-tape all of whose cells are blank.

Formalized by `Cslib.Turing.StackTape.toListBlank_nil`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-nil-2).

## Pushing a cell onto a stack tape

For every cell $c$ (a symbol of $\Gamma$ or the blank
cell) and every stack tape $s$ over $\Gamma$, the half-tape view of the stack tape obtained by
pushing $c$ onto $s$ is the half-tape view of $s$ with $c$ pushed onto its front.

For the blank cell this holds because the half-tape is blank beyond its end.

Formalized by `Cslib.Turing.StackTape.toListBlank_cons`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-cons-2).

## First cell of the half-tape view of a stack tape

For every stack tape $s$ over $\Gamma$
(a finite list of cells, each a symbol of $\Gamma$ or the blank, that does not end in a blank), the
first cell of the half-tape view of $s$ (its cells followed by infinitely many blanks) is the
first cell of $s$, which is the blank if $s$ is empty.

Formalized by `Cslib.Turing.StackTape.head_toListBlank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#head-to-list-blank-2).

## Tail of the half-tape view of a stack tape

For every stack tape $s$ over $\Gamma$ (a list
of cells, each a symbol of $\Gamma$ or the blank cell, not ending in a blank cell), the tail of
the half-tape view of $s$ is the half-tape view of the tail of $s$: dropping the first cell of
$s$ drops the first cell of its half-tape.

Formalized by `Cslib.Turing.StackTape.tail_toListBlank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#tail-to-list-blank-2).

## Cells of the half-tape view of a stack tape

For every stack tape $s$ over $\Gamma$ (a
finite list of cells, each a symbol of $\Gamma$ or the blank, that does not end in a blank) and
every $n \in \mathbb{N}$, the cell at position $n$ of the half-tape view of $s$ (its cells followed
by infinitely many blanks) is the $n$-th cell of $s$, counting from $0$, if $n$ is less than the
length of $s$, and the blank otherwise.

Formalized by `Cslib.Turing.StackTape.nth_toListBlank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-list-blank).

## Half-tape view of a word

For every word $a_1 \cdots a_n$ over $\Gamma$, the half-tape
view of the stack tape whose cells are the non-blank cells $a_1, \dots, a_n$ is the half-tape
whose first $n$ cells are $a_1, \dots, a_n$ and whose later cells are blank.

Formalized by `Cslib.Turing.StackTape.toListBlank_mapSome`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-map-some-2).

## The half-tape view of stack tapes is injective

If two stack tapes over $\Gamma$ have the
same half-tape view, then they are equal.

This holds because a stack tape does not end in a blank cell, so trailing blanks of a half-tape
do not come from cells.

Formalized by `Cslib.Turing.StackTape.toListBlank_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-injective-2).

## Cell view of a two-way tape

A CSLib tape $t$ over an alphabet $\Gamma$ has a head cell
and two halves, each a finite list of cells not ending in a blank, where a cell is a symbol of
$\Gamma$ or the blank. Its cell view is the Mathlib tape over cells, with the blank as default
symbol, whose head is the head cell of $t$ and whose left and right halves are the halves of $t$,
blank past their ends. So the cell at position $i \in \mathbb{Z}$ of the view is the cell $i$
places to the right of the head of $t$ (to the left when $i < 0$).

Formalized by `Cslib.Turing.BiTape.toTape`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-2).

## Head cell of the view of a two-way tape

For every two-way tape $t$ over $\Gamma$ (a head
cell with a left and a right stack tape), the head cell of the view of $t$ as a tape of cells is
the head cell of $t$.

Formalized by `Cslib.Turing.BiTape.head_toTape`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#head-to-tape-2).

## Left half of the view of a two-way tape

For every two-way tape $t$ over $\Gamma$ (a head
cell with a left and a right stack tape), the left half of the view of $t$ as a tape of cells is
the half-tape view of the left stack tape of $t$.

Formalized by `Cslib.Turing.BiTape.left_toTape`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#left-to-tape).

## Right half of the tape view

For every two-sided tape $t$ over $\Gamma$ (a head cell
together with a left and a right stack tape), the right half of the tape view of $t$ is the
half-tape view of the right half of $t$.

Formalized by `Cslib.Turing.BiTape.right_toTape`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#right-to-tape).

## The cells of the view

Let $t$ be a two-way tape over $\Gamma$ with head cell $h$, left
stack tape $(\ell_0, \dots, \ell_{p-1})$ and right stack tape $(r_0, \dots, r_{q-1})$. For every
integer $i$, the cell at position $i$ of the view of $t$ as a tape of cells is $h$ if $i = 0$,
$r_{i-1}$ if $0 < i \le q$, $\ell_{-i-1}$ if $-p \le i < 0$, and the blank otherwise.

Formalized by `Cslib.Turing.BiTape.nth_toTape`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape).

## The cell view commutes with writing

For every tape $t$ and every cell $a$ (a symbol or
the blank), the cell view of the tape obtained from $t$ by writing $a$ under the head equals the
tape obtained from the cell view of $t$ by writing $a$ under its head.

Formalized by `Cslib.Turing.BiTape.toTape_write`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-write-2).

## The cell view commutes with head moves

For every tape $t$ and each direction $d$ (left or
right), the cell view of the tape obtained from $t$ by moving the head one cell in direction $d$
equals the tape obtained from the cell view of $t$ by moving its head one cell in direction $d$.

Formalized by `Cslib.Turing.BiTape.toTape_move`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-move-2).

## The cell view commutes with optional head moves

For every two-way tape $t$ over $\Gamma$
and every optional head move $d$, which is either no move or a move one cell in a direction, the
cell view of the tape obtained from $t$ by the optional move $d$ is the cell view of $t$ when $d$
is no move, and the cell view of $t$ with its head moved one cell in direction $d$ when $d$ is a
direction.

Formalized by `Cslib.Turing.BiTape.toTape_optionMove`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-option-move-2).

## Offset of an optional head move

The offset of an optional head move $d$ is $0$ if $d$ is
no move, $-1$ if $d$ is a move to the left and $1$ if $d$ is a move to the right.

After the move $d$, the cell at position $i$ relative to the head is the cell that was at
position $i$ plus the offset of $d$.

Formalized by `Cslib.Turing.BiTape.optionMoveOffset`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#option-move-offset).

## The offset of an optional move is at most one

For every optional head move $d$ (no move,
a move to the left, or a move to the right), the offset of $d$ lies between $-1$ and $1$, that is,
$-1 \le \mathrm{offset}(d) \le 1$.

Formalized by `Cslib.Turing.BiTape.optionMoveOffset_bound`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#option-move-offset-bound).

## Cells after a write

For every two-way tape $t$ over $\Gamma$, every cell $a$ (a symbol of
$\Gamma$ or the blank) and every integer $i$, the cell at position $i$ of the view of the tape
obtained from $t$ by writing $a$ under the head is $a$ if $i = 0$, and the cell at position $i$
of the view of $t$ otherwise.

Formalized by `Cslib.Turing.BiTape.nth_toTape_write`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape-write).

## Cells after an optional move

For an optional direction $d$, let $\delta(d)$ be $0$ if $d$
is no move, $-1$ if $d$ is a move to the left and $1$ if $d$ is a move to the right. For every
two-way tape $t$ over $\Gamma$ and every integer $i$, the cell at position $i$ of the view of the
tape obtained from $t$ by the optional move $d$ is the cell at position $i + \delta(d)$ of the view
of $t$.

Formalized by `Cslib.Turing.BiTape.nth_toTape_optionMove`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape-option-move).

## Cells after a write and an optional move

For an optional direction $d$, let $\delta(d)$ be
$0$ if $d$ is no move, $-1$ if $d$ is a move to the left and $1$ if $d$ is a move to the right. For
every two-way tape $t$ over $\Gamma$, every cell $a$ (a symbol of $\Gamma$ or the blank) and every
integer $i$, the cell at position $i$ of the view of the tape obtained from $t$ by writing $a$
under the head and then performing the optional move $d$ is $a$ if $i + \delta(d) = 0$, and the
cell at position $i + \delta(d)$ of the view of $t$ otherwise.

Formalized by `Cslib.Turing.BiTape.nth_toTape_write_optionMove`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape-write-option-move).

## Cells after $n$ moves to the right

For every two-way tape $t$ over $\Gamma$, every
$n \in \mathbb{N}$ and every integer $i$, the cell at position $i$ of the view of the tape obtained
from $t$ by moving the head $n$ times to the right is the cell at position $i + n$ of the view
of $t$.

Formalized by `Cslib.Turing.BiTape.nth_toTape_moveRight_iterate`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape-move-right-iterate).

## The cell view of an input tape

For every word $w = w_0 w_1 \cdots w_{n-1}$ over $\Gamma$,
the cell view of the input tape of $w$ is the Mathlib input tape of the list of non-blank cells
$w_0, \dots, w_{n-1}$: the head is on $w_0$, the letters $w_1, \dots, w_{n-1}$ lie to its right
in order, and every other cell is blank (for the empty word, every cell is blank).

Formalized by `Cslib.Turing.BiTape.toTape_mk₁`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-mk-2).

## Cells of an input tape

For every word $w = w_0 \cdots w_{m-1}$ over $\Gamma$ and every
integer $i$, the cell at position $i$ of the view of the input tape of $w$ is $w_i$ if
$0 \le i < m$, and the blank otherwise.

Formalized by `Cslib.Turing.BiTape.nth_toTape_mk₁`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#nth-to-tape-mk).

## The tape view is injective

If two two-sided tapes $t$ and $t'$ over $\Gamma$ (each a head
cell together with a left and a right stack tape) have the same tape view as a tape of cells,
then $t = t'$.

Formalized by `Cslib.Turing.BiTape.toTape_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/TapeView.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-injective-2).

## Non-blank symbols

For an alphabet $\Gamma_0$ with a distinguished blank symbol $b$, the
non-blank symbols of $\Gamma_0$ are the elements $x \in \Gamma_0$ with $x \ne b$. They form the
tape alphabet of the single-tape machine that simulates a Post–Turing machine over $\Gamma_0$.

Formalized by `Cslib.Turing.SingleTapeTM.NonBlank`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#non-blank).

## Cell symbol

Let $\Gamma_0$ be an alphabet with blank symbol $b$. A tape cell over the
non-blank symbols of $\Gamma_0$ is either blank or holds a symbol $x \ne b$ of $\Gamma_0$. Its cell
symbol is $b$ for the blank cell and $x$ for the cell holding $x$. This map from cells to
$\Gamma_0$ sends the blank cell to the blank symbol, so it is a pointed map.

Formalized by `Cslib.Turing.SingleTapeTM.cellSymbol`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#cell-symbol).

## Value of the cell-symbol map

For every cell $o$ over the non-blank symbols of an alphabet
$\Gamma_0$ with blank symbol $b$, the cell symbol of $o$ is $b$ when $o$ is the blank cell and is
$x$ when $o$ holds the non-blank symbol $x$.

Formalized by `Cslib.Turing.SingleTapeTM.cellSymbol_apply`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#cell-symbol-apply).

## The cell-symbol map is injective

Distinct cells over the non-blank symbols of an alphabet
$\Gamma_0$ have distinct cell symbols in $\Gamma_0$.

Formalized by `Cslib.Turing.SingleTapeTM.cellSymbol_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#cell-symbol-injective).

## Half-tape of a stack tape of non-blank symbols

Let $\Gamma_0$ be an alphabet with blank
symbol $b$ and $N = \Gamma_0 \setminus \{b\}$ its non-blank symbols. A stack tape $s$ over $N$, a
finite list of cells each blank or holding a symbol of $N$ and not ending in a blank cell, is read
as the TM0 half-tape over $\Gamma_0$ whose $i$-th symbol is that of the $i$-th cell of $s$: $b$
for a blank cell, $x$ for a cell holding $x$, and $b$ past the end of $s$.

Formalized by `Cslib.Turing.SingleTapeTM.toListBlank`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank).

## Post–Turing reading of a tape over the non-blank symbols

Let $\Gamma_0$ be an alphabet
whose default symbol is the blank. The Post–Turing reading of a two-way tape $t$ whose cells are
blank or hold non-blank symbols of $\Gamma_0$ is the Post–Turing machine tape over $\Gamma_0$
obtained cell by cell: take the view of $t$ as a tape of cells, each cell at its position relative
to the head and blank cells past the ends, and replace each cell by its symbol, a non-blank symbol
$x$ by $x$ itself and the blank cell by the blank of $\Gamma_0$.

Formalized by `Cslib.Turing.SingleTapeTM.toTape`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape).

## The empty stack tape reads as the blank half-tape

For an alphabet $\Gamma_0$ with blank
symbol $b$, the empty stack tape over the non-blank symbols of $\Gamma_0$ reads as the half-tape
of the empty list, all of whose symbols are $b$.

Formalized by `Cslib.Turing.SingleTapeTM.toListBlank_nil`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-nil).

## Pushing a cell onto a stack tape of non-blank symbols

Let $\Gamma_0$ be an alphabet with
blank symbol $b$ and $N = \Gamma_0 \setminus \{b\}$. Read a cell over $N$ as a symbol of
$\Gamma_0$: $b$ for the blank cell, $x$ for a cell holding $x$. For every cell $o$ and every stack
tape $s$ over $N$, the half-tape read from the stack tape obtained by pushing $o$ onto $s$ is the
half-tape read from $s$ with the symbol of $o$ pushed onto its front.

For the blank cell this holds because the half-tape is blank beyond its end.

Formalized by `Cslib.Turing.SingleTapeTM.toListBlank_cons`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-cons).

## First symbol of a half-tape read from non-blank cells

Let $\Gamma_0$ be an alphabet with
blank symbol $b$. For every stack tape $s$ of cells over the non-blank symbols of $\Gamma_0$ (a
finite list of cells, blank beyond its end), the first symbol of the half-tape over $\Gamma_0$
read from $s$ is the cell symbol of the first cell of $s$; when $s$ is empty this is $b$.

Formalized by `Cslib.Turing.SingleTapeTM.head_toListBlank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#head-to-list-blank).

## Dropping the first cell of a stack tape of non-blank symbols

For an alphabet $\Gamma_0$
with blank symbol $b$ and every stack tape $s$ over the non-blank symbols of $\Gamma_0$, dropping
the first symbol of the half-tape read from $s$ gives the half-tape read from $s$ with its first
cell removed (the empty stack tape staying empty).

Formalized by `Cslib.Turing.SingleTapeTM.tail_toListBlank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#tail-to-list-blank).

## A word of non-blank symbols reads as itself

For an alphabet $\Gamma_0$ with blank symbol
$b$ and a word $w$ of non-blank symbols of $\Gamma_0$, the half-tape read from the stack tape whose
cells hold the letters of $w$ in order is the half-tape of $w$, viewed as a word over $\Gamma_0$.

Formalized by `Cslib.Turing.SingleTapeTM.toListBlank_mapSome`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-map-some).

## Distinct stack tapes of non-blank symbols read as distinct half-tapes

For an alphabet
$\Gamma_0$ with blank symbol $b$, two stack tapes over the non-blank symbols of $\Gamma_0$ that read
as the same half-tape over $\Gamma_0$ are equal.

A stack tape does not end in a blank, so the trailing blanks of a half-tape do not come from
cells.

Formalized by `Cslib.Turing.SingleTapeTM.toListBlank_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-list-blank-injective).

## Head symbol of a tape read from non-blank cells

For every two-way tape $t$ of cells over
the non-blank symbols of an alphabet $\Gamma_0$, the symbol under the head of the tape over
$\Gamma_0$ read from $t$ is the cell symbol of the cell under the head of $t$.

Formalized by `Cslib.Turing.SingleTapeTM.head_toTape`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#head-to-tape).

## Writing commutes with the Post–Turing reading of a tape

Let $\Gamma_0$ be an alphabet
whose default symbol is the blank, and for a two-way tape $t$ whose cells are blank or hold
non-blank symbols of $\Gamma_0$, let $\tau(t)$ be the Post–Turing reading of $t$, a Post–Turing
machine tape over $\Gamma_0$. For every such $t$ and every cell $o$, blank or holding a non-blank
symbol, $\tau$ of $t$ with $o$ written under the head is $\tau(t)$ with the symbol of $o$ written
under the head, where the symbol of $o$ is $x$ if $o$ holds $x$ and the blank of $\Gamma_0$ if $o$
is blank.

Formalized by `Cslib.Turing.SingleTapeTM.toTape_write`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-write).

## Head moves commute with the Post–Turing reading of a tape

Let $\Gamma_0$ be an alphabet
whose default symbol is the blank, and for a two-way tape $t$ whose cells are blank or hold
non-blank symbols of $\Gamma_0$, let $\tau(t)$ be the Post–Turing reading of $t$, a Post–Turing
machine tape over $\Gamma_0$. For every such $t$ and every direction $d$, left or right, $\tau$ of
$t$ with its head moved in direction $d$ is $\tau(t)$ with its head moved in direction $d$.

Formalized by `Cslib.Turing.SingleTapeTM.toTape_move`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-move).

## Optional head moves commute with the Post–Turing reading of a tape

Let $\Gamma_0$ be an
alphabet whose default symbol is the blank, and for a two-way tape $t$ whose cells are blank or
hold non-blank symbols of $\Gamma_0$, let $\tau(t)$ be the Post–Turing reading of $t$, a
Post–Turing machine tape over $\Gamma_0$. For every such $t$ and every optional move $d$, which is
either no move or a direction, $\tau$ of $t$ after the optional move $d$ is $\tau(t)$ when $d$ is
no move, and $\tau(t)$ with its head moved in direction $d$ when $d$ is a direction.

Formalized by `Cslib.Turing.SingleTapeTM.toTape_optionMove`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-option-move).

## The Post–Turing reading of an input tape

Let $\Gamma_0$ be an alphabet whose default
symbol is the blank. For every word $l$ of non-blank symbols of $\Gamma_0$, the Post–Turing
reading of the two-way input tape of $l$ (the head on the first symbol of $l$, the rest of $l$ to
its right, every other cell blank) is the Post–Turing machine input tape of $l$ read as a word
over $\Gamma_0$, with the head on the first symbol of $l$ and the rest of $l$ to its right.

Formalized by `Cslib.Turing.SingleTapeTM.toTape_mk₁`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-mk).

## Distinct tapes of non-blank symbols read as distinct TM0 tapes

For an alphabet
$\Gamma_0$ with blank symbol $b$, two tapes over the non-blank symbols of $\Gamma_0$ that read,
cell by cell, as the same TM0 tape over $\Gamma_0$ are equal.

Formalized by `Cslib.Turing.SingleTapeTM.toTape_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#to-tape-injective).

## Single-tape simulation of a Post–Turing machine

Let $\Gamma_0$ be a finite alphabet with
blank symbol $b$ and at least one non-blank symbol, and let $M$ be a Post–Turing machine over
$\Gamma_0$ with start state $q_0$, supported by the finite set of states $S$ (so $q_0 \in S$, and
from a state in $S$ the machine $M$ only enters states in $S$). The single-tape machine simulating
$M$ has the non-blank symbols of $\Gamma_0$ as tape alphabet, $S$ as set of states and $q_0$ as
start state. In a state $q$, reading a cell $s$ whose cell symbol is $a$, it acts as follows. If
$M$ halts in $q$ on $a$, it writes $s$ back and halts. If $M$ moves the head in direction $d$ and
enters $q'$, it writes $s$ back, moves in direction $d$ and enters $q'$. If $M$ writes $a'$ and
enters $q'$, it writes the blank cell when $a' = b$ and otherwise the cell holding $a'$, does not
move, and enters $q'$.

CSLib machines need a chosen symbol of their alphabet, so an alphabet whose only symbol is the
blank is excluded.

Formalized by `Cslib.Turing.SingleTapeTM.ofTM0`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#of-tm0).

## The simulation halts one step after the TM0 machine

Let $M$ be a TM0 machine over a
finite alphabet $\Gamma_0$ with blank symbol $b$ and at least one non-blank symbol, supported by a
finite set $S$ of states, and let $\widehat{M}$ be the single-tape machine over the non-blank
symbols $N = \Gamma_0 \setminus \{b\}$ simulating $M$. For a tape $t$ over $N$, write $\tau(t)$
for the TM0 tape read from $t$ cell by cell. If $q \in S$ and $M$ has no step from the
configuration $(q, \tau(t))$, then one step of $\widehat{M}$ from the configuration $(q, t)$
leads to its halting state with the tape $t$ unchanged.

Formalized by `Cslib.Turing.SingleTapeTM.step_ofTM0_of_step_eq_none`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#step-of-tm0-of-step-eq-none).

## Each TM0 step is one step of the simulation

Let $M$ be a TM0 machine over a finite
alphabet $\Gamma_0$ with blank symbol $b$ and at least one non-blank symbol, supported by a finite
set $S$ of states, and let $\widehat{M}$ be the single-tape machine over the non-blank symbols
$N = \Gamma_0 \setminus \{b\}$ simulating $M$. For a tape $t$ over $N$, write $\tau(t)$ for the
TM0 tape read from $t$ cell by cell. If $q \in S$ and one step of $M$ takes the configuration
$(q, \tau(t))$ to a configuration $(q', T')$, then $q' \in S$ and there is a tape $t'$ over $N$
with $\tau(t') = T'$ such that one step of $\widehat{M}$ takes the configuration $(q, t)$ to the
configuration $(q', t')$.

Formalized by `Cslib.Turing.SingleTapeTM.step_ofTM0_of_step_eq_some`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#step-of-tm0-of-step-eq-some).

## Runs of a TM0 machine are runs of its single-tape simulation

Let $M$ be a TM0 machine
over a finite alphabet $\Gamma_0$ with blank symbol $b$ and at least one non-blank symbol,
supported by a finite set $S$ of states, and let $\widehat{M}$ be the single-tape machine over
the non-blank symbols $N = \Gamma_0 \setminus \{b\}$ simulating $M$. For a tape $t$ over $N$,
write $\tau(t)$ for the TM0 tape read from $t$ cell by cell. If $M$ goes from a configuration
$(q, T)$ to a configuration $(q', T')$ in exactly $n$ steps, $q \in S$, and $\tau(t) = T$, then
$q' \in S$ and there is a tape $t'$ over $N$ with $\tau(t') = T'$ such that $\widehat{M}$ goes
from the configuration $(q, t)$ to the configuration $(q', t')$ in exactly $n$ steps.

Formalized by `Cslib.Turing.SingleTapeTM.relatesInSteps_ofTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#relates-in-steps-of-tm0).

## The simulating machine halts exactly when the Post–Turing machine halts

Let $\Gamma_0$
be a finite alphabet with at least one non-blank symbol, let $M$ be a Post–Turing machine over
$\Gamma_0$ supported by the finite set of states $S$, and let $l$ be a word of non-blank symbols
of $\Gamma_0$. The single-tape machine simulating $M$ halts on the input $l$ if and only if $M$,
started on $l$, halts.

Formalized by `Cslib.Turing.SingleTapeTM.haltsOn_ofTM0_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#halts-on-of-tm0-iff).

## The single-tape simulation outputs within one extra step

Let $\Gamma_0$ be a finite
alphabet with at least one non-blank symbol, let $M$ be a Post–Turing machine over $\Gamma_0$
supported by the finite set of states $S$, and let $l$ and $l'$ be words of non-blank symbols of
$\Gamma_0$. If $M$, started on $l$, reaches in exactly $n$ steps a configuration $c$ in which it
halts, and the tape of $c$ holds $l'$ starting at the head with blanks everywhere else, then the
single-tape machine simulating $M$ outputs $l'$ on the input $l$ within $n + 1$ steps: its run
from the initial configuration on $l$ reaches, in at most $n + 1$ steps, the halting state with
the tape holding exactly $l'$, starting at the head.

Formalized by `Cslib.Turing.SingleTapeTM.outputsWithinTime_ofTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#outputs-within-time-of-tm0).

## The single-tape simulation has the same output

Let $\Gamma_0$ be a finite alphabet with
at least one non-blank symbol, let $M$ be a Post–Turing machine over $\Gamma_0$ supported by the
finite set of states $S$, and let $l$ and $l'$ be words of non-blank symbols of $\Gamma_0$. If
$M$, started on $l$, halts in a configuration whose tape holds $l'$ starting at the head, with
blanks everywhere else, then the single-tape machine simulating $M$ outputs $l'$ on the input
$l$: its run from the initial configuration on $l$ reaches the halting state with the tape
holding exactly $l'$, starting at the head.

Formalized by `Cslib.Turing.SingleTapeTM.outputs_ofTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfTM0.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html#outputs-of-tm0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equivalent tape representations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/turing-machines/single-tape/equivalent-tape-representations)
